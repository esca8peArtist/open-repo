---
title: "Kit Email Launch Sequence — 5-Email Welcome Series"
prepared: 2026-05-13
status: production-ready — copy finalized; user builds in Kit platform
scope: Welcome Email (Day 1), Follow-up 1 (Day 3), Follow-up 2 (Day 7), Retention/Preference (Day 10), Re-engagement (Day 14)
references:
  - marketing/email-and-launch-plan.md (full email body copy for all 5 emails)
  - TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md (Kit platform setup instructions)
  - KIT_SETUP_NOTES.md (15 tags, zone routing, automation build)
  - PHASE_2_EMAIL_STRATEGY.md (sequence architecture and intent)
  - MAY_CONTENT_EXECUTION_PLAN.md (Email 1–3 copy section)
---

# Kit Email Launch Sequence — 5-Email Welcome Series

**How to use this document**: This is the configuration spec for the 5-email welcome
sequence in Kit. The full email body copy is in `marketing/email-and-launch-plan.md`.
This document specifies: subject lines, send timing, trigger conditions, Kit automation
settings, and the goal of each email. Build this in Kit after completing Gate 3 (account
setup + 15 tags).

**Kit automation type**: Sequence (not a Broadcast). Sequences fire automatically when
a subscriber joins, based on triggers and time delays.

**Trigger**: Subscriber signs up on the Kit landing page (Zone Quick-Start Card lead magnet)
and confirms their email. Sequence fires immediately at confirmation.

---

## Email 1: Welcome + Zone Card Delivery (Day 0 — Immediate)

**Send timing**: Immediately upon confirmed subscription (Kit default: "On subscribe")
**Subject line**: "Your Zone [X] Quick-Start Card is here"
**Preview text**: "Exactly what's happening in your zone right now — and what to do about it"

**Kit configuration**:
- Trigger: Tag added "zone-[X]" (one Email 1 variant per zone, 8 variants total)
- Each variant delivers the correct zone card PDF via a Google Drive direct-download link
- Automation path: subscriber selects Zone 5 on form → zone-5 tag applied → Email 1
  Zone 5 variant fires → Zone 5 PDF link in email body
- This zone routing is the most technically complex part of the Kit build. Full build
  instructions in `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` Section 5.

**Email purpose**: Deliver the lead magnet immediately. Confirm Seedwarden is real and
the subscriber made a good decision. Set expectations for what comes next.

**Content outline** (full copy in `marketing/email-and-launch-plan.md` Email 1 section):
1. Subject line delivers on its promise in the first line
2. Zone card Google Drive download link (direct download URL, not viewer)
3. One sentence: what the card tells them
4. One sentence: what Seedwarden is
5. One question: "What's one thing you're trying to grow this season?" (Reply-to seed
   for engagement data)
6. Signature: "— [Founder name], Seedwarden"

**Attachments**: None. PDF is linked via Google Drive, not attached (attachment increases
spam score; Drive link is confirmed working per Gate 3 test protocol).

**Important**: Do not include any product promotion or pricing in Email 1. This email
is a promise delivery, not a sales email. Trust is built here.

---

## Email 2: Follow-Up 1 — Feature Content + Engagement Ask (Day 3)

**Send timing**: 3 days after Email 1
**Subject line**: "One foraging mistake worth avoiding (and what to do instead)"
**Preview text**: "This comes up with every new grower we talk to"

**Kit configuration**:
- Time delay: 3 days after previous email
- No conditional branching — fires to all subscribers regardless of Email 1 open status
- (Note: If open rate on Email 1 is >40%, no changes needed. If below 30%, test an
  alternative subject line on Email 2 and report back before scheduling Email 3.)

**Email purpose**: Deliver educational value. This is the "content email" — no CTA to
purchase, no urgency. The goal is to establish Seedwarden as a source of genuine knowledge,
not a store that wants their money. Subscribers who open Email 2 are highly engaged.

**Content outline** (full copy in `marketing/email-and-launch-plan.md` Email 2 section):
1. Open with a relatable mistake (one specific foraging or growing error a beginner makes)
2. Explain why it happens — empathy-first
3. Show the fix in 2–3 actionable steps
4. Soft tie-in to relevant guide (mention it by name, do not link directly to product in
   this email — the ask comes in Email 3)
5. Close with a question or forward-looking hook to set up Email 3

**Behavioral tag**: If subscriber clicks any link in Email 2, apply tag "engaged-email-2"
for later segmentation. Build this click trigger in Kit Automations.

---

## Email 3: Follow-Up 2 — Education + First Product Offer (Day 7)

**Send timing**: 7 days after Email 1 (4 days after Email 2)
**Subject line**: "The native plant guide we built for [Zone X] growers"
**Preview text**: "Not generic advice. Your actual growing zone, your actual species."

**Kit configuration**:
- Time delay: 4 days after Email 2
- Conditional: send to all subscribers; tag "Cohort_Forager" if subscriber clicks foraging
  links; tag "Cohort_Homesteader" if subscriber clicks homesteading links (behavioral tagging)
- This email is the first product ask — use a gentle CTA, not hard sell

**Email purpose**: First product introduction. By Day 7, the subscriber has received their
zone card (Email 1), seen Seedwarden knows its subject (Email 2), and built enough trust for
a product recommendation. This email offers one specific guide at the correct price without
pressure.

**Content outline** (full copy in `marketing/email-and-launch-plan.md` Email 3 section):
1. Restate the zone card's value — connect it to the guide being offered
2. Introduce the Native Plants Regional Guide (or whichever guide is most relevant to the
   zone) by describing one specific thing the subscriber would learn
3. Include the Etsy listing URL with UTM parameters:
   `?utm_source=kit&utm_medium=email&utm_campaign=welcome-sequence-email3`
4. Soft CTA: "If you're curious, take a look — no pressure"
5. PS: include SEEDWARDEN15 coupon code (15% off, no minimum) as a "welcome gift" framing

**Behavioral tag application**:
- Click on any foraging guide link → add tag "Cohort_Forager"
- Click on any preservation/homesteading guide link → add tag "Cohort_Homesteader"
- Click on survival/prepper guide link → add tag "Cohort_Prepper"
- No click → add tag "no-click-email3" for re-engagement consideration at Day 14

---

## Email 4: Preference Center + Value Reinforcement (Day 10)

**Send timing**: 10 days after Email 1 (3 days after Email 3)
**Subject line**: "Quick question about what you're growing"
**Preview text**: "I want to make sure I'm sending you the right stuff"

**Kit configuration**:
- Time delay: 3 days after Email 3
- Send to: all subscribers (including non-openers of Emails 2–3; this re-engages them)
- This email contains the cohort survey — responses apply the Cohort tags

**Email purpose**: Collect preference data to improve future segmentation. Subscribers who
engage with this email identify themselves as engaged. The survey also re-engages subscribers
who have not opened recent emails by offering something personalized in return.

**Content outline** (full copy in `marketing/email-and-launch-plan.md` Email 4 section):
1. Honest framing: "I've been sending you content — I want to make sure it's what you
   actually need. One question:"
2. Survey: a 4-option question asking which best describes them:
   - "I forage and want to know more wild edibles"
   - "I grow food at home and want better results"
   - "I'm preparing for food independence"
   - "I'm buying a gift for someone who grows food"
3. Each option links to a unique Kit "thank you" page that applies the corresponding cohort tag:
   - Option 1 → applies Cohort_Forager
   - Option 2 → applies Cohort_Homesteader
   - Option 3 → applies Cohort_Prepper
   - Option 4 → applies Cohort_GiftBuyer
4. After selection: "Based on your answer, here's what I'll send you next" — preview of
   cohort-specific content to come
5. Unsubscribe reminder: "If these emails aren't useful, you can unsubscribe any time below.
   No hard feelings." (Reduces spam complaints; improves list quality)

**Kit build note**: Each survey link goes to a different Kit "Form Confirmation" page, each
with a different tag trigger. This is a simple URL-click-based tagging approach, not a
native survey form. Build instructions in `KIT_SETUP_NOTES.md`.

---

## Email 5: Re-Engagement + Retention Offer (Day 14)

**Send timing**: 14 days after Email 1 (4 days after Email 4)
**Subject line**: "Still there? Here's something for growers who mean it"
**Preview text**: "A guide preview + a reason to come back"

**Kit configuration**:
- Time delay: 4 days after Email 4
- Conditional send paths:
  - If subscriber has Cohort_Forager tag → forager-specific guide recommendation
  - If subscriber has Cohort_Homesteader tag → homesteader-specific guide recommendation
  - If subscriber has Cohort_Prepper tag → prepper-specific guide recommendation
  - If subscriber has Cohort_GiftBuyer tag → gift guide recommendation
  - If subscriber has NO cohort tag (never clicked survey) → send generic "best sellers" version
- This is the first cohort-personalized email in the sequence

**IMPORTANT — copy fix required**: `BUNDLE_E_WRITING_ACCELERATION.md` (Session 2026-05-13)
flagged that a previous draft of Email 5 contained the phrase "May 20 (tomorrow)" — a date
reference that will be incorrect for subscribers receiving this email after May 20. Before
scheduling this email, open `marketing/email-and-launch-plan.md` Email 5, locate any specific
date references, and replace them with relative language ("tomorrow," "this week," "soon").
This is a 5-minute fix.

**Email purpose**: First cohort-personalized email. Delivers a guide preview (excerpt or
teaser) matching the subscriber's interest. The preview is the retention offer — it gives
subscribers a reason to stay on the list and confirms Seedwarden understands their specific need.

**Content outline** (full copy in `marketing/email-and-launch-plan.md` Email 5 section):
1. Open based on cohort:
   - Forager: "Since you're into foraging, here's a section from the Wild Edibles guide..."
   - Homesteader: "Since you're growing food at home, here's the section most home growers..."
   - Prepper: "For people focused on food independence, this section..."
   - Gift Buyer: "If you're buying for someone who grows food..."
2. 3–5 sentence guide preview (excerpt from the most relevant guide)
3. CTA: link to the full guide on Etsy with UTM parameters and SEEDWARDEN15 coupon
4. Forward ask: "If this was useful, forward it to someone who's been asking about growing
   their own food" — referral ask, low pressure
5. What comes next: "I'll send a seasonal foraging update next week" — sets expectation for
   ongoing value

---

## Sequence Architecture Summary

| Email | Day | Subject | Purpose | Kit Trigger |
|---|---|---|---|---|
| Email 1 | Day 0 | "Your Zone [X] Quick-Start Card is here" | Lead magnet delivery, trust establishment | Zone tag applied on sign-up |
| Email 2 | Day 3 | "One foraging mistake worth avoiding" | Educational value, brand authority | Time delay: 3 days |
| Email 3 | Day 7 | "The native plant guide we built for [Zone X] growers" | First product offer + coupon | Time delay: 4 days |
| Email 4 | Day 10 | "Quick question about what you're growing" | Cohort survey, preference data, list hygiene | Time delay: 3 days |
| Email 5 | Day 14 | "Still there? Here's something for growers who mean it" | Cohort-personalized guide preview + retention | Time delay: 4 days + cohort conditional |

---

## Unsubscribe Cadence and Preference Center

**Unsubscribe footer**: Present in all 5 emails (Kit adds automatically — do not suppress).

**Preference center**: Email 4's cohort survey functions as a lightweight preference center.
Kit does not have a native preference center at the free tier. The survey link approach
(click option → tag applied) is the functional equivalent.

**List hygiene recommendation**: After the 5-email sequence, subscribers who have not opened
any email (0 of 5) and have not clicked anything are low-engagement. Add them to a
"re-engagement" segment and send one final email at Day 21: "Should I keep sending you
updates?" with a simple "Yes, keep me subscribed" CTA. Non-responders to this email should
be unsubscribed to maintain deliverability scores.

**Engagement threshold to watch**: If Email 2 open rate falls below 25%, pause the sequence
and review Email 1's subject line and deliverability before continuing. A poor Email 1
experience is the cause, not Email 2.

---

## Launch Broadcast (May 30, 12:00pm — Separate from Sequence)

The launch broadcast is a one-time email to all existing Kit subscribers (not part of the
welcome sequence). It announces Phase 2 is live and links to the Etsy store.

**Subject line**: (from `marketing/email-and-launch-plan.md` Launch Broadcast section)
**Send time**: May 30, 12:00pm — must be staged as a Broadcast in Kit before May 29 9pm
**Recipient list**: "All Confirmed Subscribers"
**UTM parameters on all links**: `?utm_source=kit&utm_medium=email&utm_campaign=may30-launch`

The launch broadcast and the welcome sequence are separate Kit entities. The broadcast
fires once to the existing list. The welcome sequence fires to every new subscriber going
forward, regardless of whether they subscribed before or after May 30.

---

*Prepared: 2026-05-13. Seedwarden Agent. Full email body copy is in
`marketing/email-and-launch-plan.md` — this document specifies configuration only.
Build sequence in Kit after Gate 3 account setup. Test end-to-end by May 28.*
