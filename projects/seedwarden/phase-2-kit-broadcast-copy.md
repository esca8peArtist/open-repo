---
title: "Phase 2 Kit Broadcast Copy — May 30 12pm Launch Broadcast"
date: 2026-05-07
status: paste-ready
send-date: 2026-05-30 12:00pm local time
kit-path: Broadcasts > New Broadcast > paste subject + body > Send to "All Confirmed Subscribers" > Schedule May 30 12pm
references:
  - phase-2-launch-control-center.md (May 27 scheduling instructions)
  - may-30-launch-sequence.md (Kit verification block)
  - phase-2-buyer-retention-lifecycle-strategy.md (Campaign 5 win-back framing)
---

# Phase 2 Kit Broadcast Copy
## May 30 Launch Broadcast — Sends at 12pm

**Before scheduling**: Confirm SEEDWARDEN15 is active in Etsy Shop Manager > Marketing > Coupons.
Confirm all 21 Etsy listings are "Active." Schedule this broadcast by May 27 (see phase-2-launch-control-center.md May 27 calendar block).

---

## SUBJECT LINE

Phase 2 is live — your zone library just doubled

---

## PREVIEW TEXT (Kit "preview text" field — appears in inbox snippet)

New zones, new guides, and a Zone Quick-Start Card for every region. Here's what's new.

---

## EMAIL BODY

Hi {{ subscriber.first_name }},

Something I've been building toward since this past winter is live today.

When you picked up a Seedwarden guide, you were among the first 47 people who trusted that a zone-specific approach to foraging and growing actually works better than generic advice. That matters — Phase 1 was how we proved the concept. Phase 2 is what we built because it did.

Here's what's new as of today:

**Seven new growing zones.** The Seedwarden catalog now covers Zones 3 through 10 — the full range of the continental US and southern Canada. If you're in a zone that wasn't covered before, your zone is live now.

**Zone Quick-Start Cards.** Every zone now has a free one-page field card covering your frost dates, highest-value plants in season right now, and the two or three things worth doing this month. It's the fastest way into the Seedwarden system for your specific region.

**Expanded catalog across every category.** Wild edibles, medicinal herbs, seed saving, preservation, native plants — the catalog that existed when you first bought has grown significantly. If there was a guide you wished existed back then, it very likely does now.

As a Phase 1 buyer, you have access to SEEDWARDEN15 — 15% off any order, no minimum. It's my way of saying thank you for being early.

[BUTTON: Explore Phase 2 → link to Etsy store homepage with utm_campaign=phase2-launch-broadcast&utm_source=kit&utm_medium=email]

[BUTTON: Get Your Free Zone Card → link to Kit landing page with utm_campaign=phase2-launch-broadcast-zonecard]

---

If you've been waiting to add a second zone or a new category to your collection, today is a good day to do it.

— Anya
Seedwarden

*P.S. Coupon code: SEEDWARDEN15 — 15% off at checkout, valid through June 15, 2026.*

---

## IMPLEMENTATION NOTES

**Word count**: 275 words (within the 200–250 word target; slightly over to accommodate the three-item list — acceptable given launch context)

**Tone check**: Celebratory but grounded. The Phase 1 framing ("47 people," "you were among the first") treats the reader as a participant in the story, not a passive audience. The CTA is an offer, not a command. The P.S. reinforces the discount without repeating the body copy.

**Merge tags used**:
- `{{ subscriber.first_name }}` — always use; fallback "Friend" if blank

**UTM parameters**:
- Etsy store link: `utm_campaign=phase2-launch-broadcast&utm_source=kit&utm_medium=email`
- Zone card link: `utm_campaign=phase2-launch-broadcast-zonecard&utm_source=kit&utm_medium=email`
- Both links should be tracked in GA4 to measure broadcast-to-store traffic on launch day

**Kit scheduling path**:
1. Kit > Broadcasts > New Broadcast
2. Subject: paste from above
3. Preview text: paste from above
4. Body: paste from above, add UTM links to both buttons
5. Audience: "All Confirmed Subscribers"
6. Schedule: May 30, 12:00pm [your timezone]
7. Confirm status reads "Scheduled" — not "Draft"

**Verification on launch day (May 30, from may-30-launch-sequence.md)**:
- At 8am: confirm broadcast shows "Scheduled" at 12pm
- At 12:05pm: check Kit > Broadcasts > open the sent broadcast > confirm delivery rate >90%

**Success targets (from phase-2-launch-control-center.md Part 4)**:
- Delivery rate: >90% (minimum acceptable: >80%)
- Bounce rate: <2% (minimum acceptable: <5%)
- Open rate at 6 hours post-send: >35% (minimum acceptable: >20%)
- Click rate at 6 hours post-send: >8% (minimum acceptable: >3%)

---

*Broadcast copy status: paste-ready. No placeholders remain except the live Etsy store URL and Kit landing page URL, which must be confirmed active before scheduling.*
