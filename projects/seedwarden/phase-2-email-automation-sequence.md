---
title: "Phase 2 Email Automation Sequence"
subtitle: "Day-by-day timing, Kit tags, A/B variants, link tracking, and delivery handling"
date: 2026-05-09
session: 907-item36
status: production-ready
scope: Phase 2 launch through Week 4 (May 30 – June 27, 2026)
references:
  - PHASE_2_EMAIL_STRATEGY.md (sequence architecture, platform setup)
  - marketing/email-and-launch-plan.md (full copy for all 5 welcome emails)
  - marketing/email-automation-blueprint.md (automation technical setup)
  - TRACK_B_LAUNCH_DAY_OPERATIONS_GUIDE.md (T+12h, T+38h checkpoints)
  - KIT_SETUP_NOTES.md (Kit platform config)
---

# Phase 2 Email Automation Sequence
## May 30, 2026 — Week 4 (June 27)

This document specifies the complete email automation schedule for Phase 2 — every send, every trigger, every tag, every A/B variant, and all delivery handling logic. No TODOs remain. Execute against this spec directly in Kit.

---

## Part 1: Overview and Sequence Architecture

Phase 2 runs four active email tracks simultaneously. Each track has a distinct trigger and audience.

| Track | Name | Trigger | Audience | Emails | Phase |
|---|---|---|---|---|---|
| A | Welcome Sequence | New sign-up on Kit landing page | New subscribers | 5 emails over 10 days | Active from May 30 |
| B | Launch Broadcast | Manual send, May 30 12:00pm UTC | All confirmed subscribers at launch | 1 broadcast | May 30 only |
| C | Post-Launch Nurture | Completion of Welcome Sequence | Subscribers who finished 5-email series | Weekly newsletter, Thursdays | From June 5 onward |
| D | Re-Engagement | 6 consecutive unopened sends | Inactive subscribers | 3 emails | Phase 3 — do not build yet |

**Build in this order**: B (broadcast first, scheduled before launch), then A (active on launch), then C (first newsletter June 5). Do not build D until subscriber list exceeds 200.

---

## Part 2: Launch Broadcast (Track B) — May 30

### Send Specifications

| Field | Value |
|---|---|
| Send date | May 30, 2026 |
| Send time | 12:00pm UTC (8:00am Eastern, 5:00am Pacific) |
| Recipient list | All Confirmed Subscribers (exclude anyone tagged "bounced" or "unsubscribed") |
| Kit action | Broadcasts > Schedule > enter 12:00pm May 30 UTC |
| Status check | Verify "Scheduled" status appears in Broadcasts list by May 29 17:00 UTC |

### Subject Line (A/B Test)

Run a 50/50 split on the launch broadcast subject line.

| Variant | Subject | Preview text |
|---|---|---|
| A (control) | Phase 2 is live — your zone card library just doubled | What to plant right now in your zone, with two new cards added this week. |
| B (test) | Your Zone [X] just got an upgrade | We added two new zone cards — including yours. Here's what changed. |

**Kit A/B setup**: Broadcasts > New Broadcast > Subject Line Test > 50/50 split. Enter both subjects. Set winner determination to "Open Rate" at 4-hour mark. Kit auto-sends winning variant to the remainder of the list at 4:00pm UTC.

**Note on Variant B**: Kit cannot dynamically insert zone numbers in broadcast subject lines (only in sequence emails where zone is a known subscriber field). Variant B reads as a generic upgrade message — still effective but does not personalize. Use the zone merge tag only if Kit broadcast personalization is available for your account tier.

### Body Copy

Full copy: `marketing/email-and-launch-plan.md` > Launch Broadcast section.

Content summary:
- Opening: acknowledge the subscriber relationship, announce Phase 2 launch
- Body: 2–3 paragraphs on what is new (lifestyle photos live on Etsy, zone card delivery now includes Zones 3 and 4 in addition to Zones 5–10 already available)
- CTA 1: Link to Etsy store (tracked — see Part 5)
- CTA 2: "Share your zone" social link (Pinterest or Instagram profile)
- Closing: reminder that Email 5 coupon SEEDWARDEN15 is still active for any subscribers who have not used it

### Link Tracking for Broadcast

Add UTM parameters to every outbound link in the broadcast:

| Link destination | UTM parameters to append |
|---|---|
| Etsy store root | `?utm_source=kit&utm_medium=email&utm_campaign=phase2_launch&utm_content=broadcast_cta1` |
| Specific Etsy listing | `?utm_source=kit&utm_medium=email&utm_campaign=phase2_launch&utm_content=broadcast_listing_[product-slug]` |
| Kit landing page (zone card) | `?utm_source=kit&utm_medium=email&utm_campaign=phase2_launch&utm_content=broadcast_zonecta` |

UTM parameters are appended directly to the link in Kit's email editor — paste the full URL including UTMs into the link field.

---

## Part 3: Welcome Sequence (Track A) — Ongoing from May 30

### Sequence Configuration in Kit

| Field | Value |
|---|---|
| Sequence name | Seedwarden Welcome |
| Trigger | Form submitted (Zone Quick-Start Card sign-up form) |
| Tags applied on trigger | new-subscriber, zone-[X] (where X is the zone selected on form) |
| Total emails | 5 |
| Total duration | Day 0 through Day 10 |
| Post-sequence action | Add to "Weekly Newsletter" segment. Remove "new-subscriber" tag. |

### Day-by-Day Email Schedule

#### Email 1 — Day 0 (Immediate, within 60 seconds of form submission)

| Field | Value |
|---|---|
| Trigger delay | 0 minutes (immediate) |
| Variants | 8 (one per zone, Zones 3–10) |
| Subject line (all zones) | Your Zone [X] Quick-Start Card is ready |
| Preview text | One page. What to plant right now in Zone [X]. |
| Primary CTA | Download your zone card (Google Drive direct download link, zone-specific) |
| Secondary CTA | None in Email 1 — do not add product links in the first email |
| Tags applied | None new (zone tag already applied at form submission) |
| Copy location | marketing/email-and-launch-plan.md > Email 1 |

Zone routing in Kit:
- Automation rule: IF subscriber custom field "zone" = 3 THEN send Email 1 Zone 3 variant
- Replicate this conditional for Zones 4 through 10
- Verify the conditional rule is published before any subscriber submits the form

**Zone-to-file mapping** (confirm each Google Drive URL is the direct download format `?export=download&id=`):

| Zone | PDF filename | Kit Files URL (fill in after upload) |
|---|---|---|
| 3 | zone-3-quick-start-card.pdf | _[log in WORKLOG.md after upload]_ |
| 4 | zone-4-quick-start-card.pdf | _[log in WORKLOG.md after upload]_ |
| 5 | zone-5-quick-start-card.pdf | _[log in WORKLOG.md after upload]_ |
| 6 | zone-6-quick-start-card.pdf | _[log in WORKLOG.md after upload]_ |
| 7 | zone-7-quick-start-card.pdf | _[log in WORKLOG.md after upload]_ |
| 8 | zone-8-quick-start-card.pdf | _[log in WORKLOG.md after upload]_ |
| 9 | zone-9-quick-start-card.pdf | _[log in WORKLOG.md after upload]_ |
| 10 | zone-10-quick-start-card.pdf | _[log in WORKLOG.md after upload]_ |

**A/B subject test for Email 1** (optional, enable after first 50 subscribers to collect data):

| Variant | Subject |
|---|---|
| A (control) | Your Zone [X] Quick-Start Card is ready |
| B (test) | Here's your Zone [X] planting guide — one page, what to grow right now |

Determine winner by open rate at 24-hour mark. Apply winning subject to all new subscribers from that point forward.

---

#### Email 2 — Day 2

| Field | Value |
|---|---|
| Trigger delay | 2 days after Email 1 send |
| Variants | 1 (same copy for all zones) |
| Subject line | The tomato that changed how I think about seeds |
| Preview text | A 1940s farmer, a Brandywine, and why heirloom seeds matter now. |
| Primary CTA | None (educational email — no product links) |
| Forward hook | Close with: "Next email I'll share a mistake I made that cost me an entire season — and how to avoid it." |
| Tags applied | None |
| Copy location | marketing/email-and-launch-plan.md > Email 2 |

**A/B subject test**:

| Variant | Subject |
|---|---|
| A (control) | The tomato that changed how I think about seeds |
| B (test) | Why the seeds at your local nursery aren't what they used to be |

---

#### Email 3 — Day 5

| Field | Value |
|---|---|
| Trigger delay | 5 days after Email 1 send (3 days after Email 2) |
| Variants | 1 |
| Subject line | The seed-saving mistake that cost me a whole season |
| Preview text | I learned the hard way. You don't have to. |
| Primary CTA | Behavioral tag link: "Read more about seed saving" → links to Seed Saving Field Manual Etsy listing |
| Secondary CTA | None |
| Tags applied on click | Subscribers who click the seed saving link receive tag "seed-saver" |
| Copy location | marketing/email-and-launch-plan.md > Email 3 |

**Tag trigger spec in Kit**:
- Automation: IF subscriber clicks link [Seed Saving Field Manual URL] in Email 3 THEN apply tag "seed-saver"
- This is a link-click trigger in Kit Automations, not a sequence action
- Set up in Kit: Automations > New Rule > Trigger: Subscriber clicks a link > URL contains "etsy.com/listing/[seed-saving-manual-id]" > Action: Add tag "seed-saver"

**A/B subject test**:

| Variant | Subject |
|---|---|
| A (control) | The seed-saving mistake that cost me a whole season |
| B (test) | What I got wrong about tomato seeds (and how to fix it) |

---

#### Email 4 — Day 7

| Field | Value |
|---|---|
| Trigger delay | 7 days after Email 1 send (2 days after Email 3) |
| Variants | 1 |
| Subject line | Here's what I've been building |
| Preview text | Three guides. Three kinds of growers. See which one fits you. |
| Primary CTA | Three segmentation links — each tags a subscriber interest segment |
| Tags applied on click | See segmentation logic below |
| Copy location | marketing/email-and-launch-plan.md > Email 4 |

**Three segmentation CTAs in Email 4**:

| Link text | Destination | Tag applied on click |
|---|---|---|
| "Growing in an apartment or container?" | Container Growing Blueprint Etsy listing | city-grower |
| "Saving seeds and building food sovereignty?" | Seed Saving Field Manual Etsy listing | seed-saver |
| "Preserving your harvest?" | Harvest Preservation Handbook Etsy listing | preservationist |

**Tag trigger spec**: Three separate Kit automation rules, one per link. Same structure as Email 3 tag rule: Trigger = link click containing the listing URL, Action = apply tag.

Subscribers who click no links in Email 4: they remain with no interest tag and receive the full untagged newsletter with mixed product features.

**A/B subject test**:

| Variant | Subject |
|---|---|
| A (control) | Here's what I've been building |
| B (test) | Three guides for three kinds of growers — which one are you? |

---

#### Email 5 — Day 10

| Field | Value |
|---|---|
| Trigger delay | 10 days after Email 1 send (3 days after Email 4) |
| Variants | 1 base + 3 product recommendation variants by tag (see below) |
| Subject line | A thank-you — and an offer that expires in 5 days |
| Preview text | SEEDWARDEN15 takes 15% off anything in the shop. Here's why I made it. |
| Primary CTA | Etsy store link with coupon code SEEDWARDEN15 prominently displayed |
| Coupon code | SEEDWARDEN15 (15% off, no minimum, must be entered manually at Etsy checkout) |
| Tags applied | none new |
| Copy location | marketing/email-and-launch-plan.md > Email 5 |

**Tag-based product recommendation variants**:

Kit conditional content blocks (if Kit account supports conditional content — otherwise send one universal version with all three options):

| Tag condition | Product recommendation in Email 5 |
|---|---|
| Has tag "seed-saver" | Lead with: Seed Saving Field Manual — "This is the guide for where you are right now." |
| Has tag "city-grower" | Lead with: Container Growing Blueprint — "If you're working with limited space, start here." |
| Has tag "preservationist" | Lead with: Harvest Preservation Handbook — "If you're growing more than you can eat, this is the next step." |
| No interest tag | Lead with: Zone Calendar (highest Phase 1 sales volume) — "Most people start here — a planting calendar for your zone." |

**Coupon tracking**: SEEDWARDEN15 is entered manually at Etsy checkout. To attribute redemptions to email:
- In Etsy Shop Manager > Marketing > Coupons, the "Times Used" count tracks total redemptions
- Log "Times Used" count at Day 10 (when Email 5 sends), Day 15 (coupon expiry), and Day 30
- The difference between Day 10 and Day 15 counts represents Email 5 attributed redemptions
- Manual tracking only — Etsy does not provide email-source attribution for coupon use

**Post-sequence action**: When a subscriber completes Email 5, Kit automatically removes the "new-subscriber" tag and adds to the "Weekly Newsletter" segment. Configure this in Kit: Sequences > Seedwarden Welcome > After completion > Add tag "welcome-complete" > Add to segment "Newsletter Subscribers."

---

## Part 4: Post-Launch Nurture (Track C) — Weekly Newsletter, June 5 Onward

### Newsletter Configuration

| Field | Value |
|---|---|
| Cadence | Every Thursday |
| First send | Thursday June 5, 2026 at 10:00am UTC |
| Recipient segment | "Newsletter Subscribers" (all subscribers who have completed the 5-email welcome sequence) |
| Unsubscribe group | "Seedwarden Newsletter" — distinct from the welcome sequence unsubscribe group |

### Four-Section Newsletter Structure

Every newsletter follows this fixed structure (full spec in `marketing/email-automation-blueprint.md` Part 5):

1. Growing update (2–3 sentences, seasonal and specific — what is actually happening in the garden right now)
2. Technique or tip (200–350 words, fully actionable, no teaser-to-click pattern)
3. Product spotlight (3–4 sentences + Etsy listing link, connected naturally to the technique topic)
4. Reader question (50–100 words answering a real question from a recent reply or comment)

### June–July Newsletter Calendar

| Send date | Technique topic | Product spotlight | Source material |
|---|---|---|---|
| June 5 | How to thin seedlings without killing your plants | Zone Quick-Start Card (zone-specific thinning schedules) | Use Cluster A shoot photography in product spotlight if available |
| June 12 | Companion planting: the 5 combinations that actually work | Companion Planting Chart | Cluster A slot 4 flat-lay photo |
| June 19 | Saving tomato seeds: the fermentation method | Seed Saving Field Manual | Cluster A lifestyle image |
| June 26 | Container soil mixing — what to skip at the nursery | Container Growing Blueprint | Cluster B lifestyle image |
| July 3 | Lacto-fermentation basics: the lowest-risk preservation method | Harvest Preservation Handbook | Cluster C lifestyle image |
| July 10 | Reading your zone card: what frost dates actually mean | Zone Calendar 2026 | Zone card PNG preview |

**Tagline for tagged segments**: If subscriber has tag "seed-saver," the Product Spotlight section in the June 19 newsletter should be the Seed Saving Field Manual with slightly more specific copy than the untagged version. This is optional — implement only if Kit's conditional content feature is available on your account tier. A single untagged newsletter still works.

---

## Part 5: Link Tracking Specifications for Cohort Conversion Attribution

Every outbound link in every email must carry UTM parameters. This is required for GA4 to attribute orders to the correct email send.

### UTM Parameter Schema

| Parameter | Values |
|---|---|
| utm_source | always `kit` |
| utm_medium | always `email` |
| utm_campaign | `phase2_launch` (broadcast and first 30 days), `phase2_nurture` (newsletter from June 5) |
| utm_content | identifies the specific link — use the convention below |

### utm_content Convention

Format: `[email_type]_[email_number]_[cta_position]`

| Email | Link | utm_content value |
|---|---|---|
| Broadcast | Etsy store CTA | `broadcast_cta1` |
| Broadcast | Specific listing | `broadcast_listing_[product-slug]` |
| Email 1 | Zone card download | `welcome_e1_zonecarddownload` |
| Email 3 | Seed Saving link | `welcome_e3_seedsavinglink` |
| Email 4 | Container link | `welcome_e4_containercta` |
| Email 4 | Seed saving link | `welcome_e4_seedsavingcta` |
| Email 4 | Preservation link | `welcome_e4_preservationcta` |
| Email 5 | Etsy store (coupon) | `welcome_e5_couponcta` |
| Newsletter June 5 | Product spotlight | `nurture_n1_spotlight` |
| Newsletter June 12 | Product spotlight | `nurture_n2_spotlight` |

### Cohort Conversion Attribution in GA4

When a subscriber clicks an email link and purchases on Etsy, the UTM parameters pass through the referral chain. To attribute orders in GA4:

1. GA4 > Reports > Acquisition > Traffic Acquisition > filter by utm_medium = email
2. View conversion events grouped by utm_content to see which email link drove which orders
3. The utm_campaign differentiates broadcast (one-time revenue spike) from nurture (steady ongoing conversions)

**Known limitation**: Etsy's checkout redirect strips UTM parameters from the final purchase event URL in some configurations. If GA4 shows email traffic but no purchase conversions, set up a GA4 goal for "Etsy referral sessions that reached /checkout" as a proxy conversion.

### Kit Click Tracking

Kit natively tracks link clicks in all sequence emails and broadcasts. Access via:
- Broadcasts: Kit > Broadcasts > [broadcast name] > Stats > Clicks
- Sequences: Kit > Sequences > Seedwarden Welcome > [email] > Stats > Clicks

Compare Kit click counts against GA4 email-attributed sessions as a cross-reference. Large discrepancy (Kit shows 50 clicks, GA4 shows 10 sessions) = UTM parameters are being stripped by email clients before the click registers in GA4.

---

## Part 6: Unsubscribe and Bounce Handling

### Unsubscribe Handling

**Kit default behavior**: All Kit emails include a mandatory unsubscribe link in the footer. Kit processes unsubscribes automatically within 24 hours of the subscriber clicking. The subscriber is removed from all active sequences and broadcast lists.

**Your action on an unsubscribe**:
- No action required for routine unsubscribes
- If you receive a reply from an unsubscribed person asking to be removed: Kit has already processed it; reply confirming removal
- Weekly: Kit > Subscribers > filter by "Unsubscribed" to see count. Log total in WORKLOG.md each Friday

**Unsubscribe rate threshold**: If unsubscribes exceed 2% of any single send, investigate content or audience quality before sending the next email. A 2%+ unsubscribe rate on a welcome sequence (not a broadcast) is a strong signal that the sign-up experience is misaligned with email content — review the landing page headline against Email 2's actual content.

**Segment-specific unsubscribes**: Kit allows subscribers to unsubscribe from individual sequences or from all emails. If a subscriber unsubscribes from the welcome sequence but not from all email, they should still receive the broadcast. This edge case is rare but confirm Kit's handling by testing with a secondary email address.

### Bounce Handling

**Soft bounce** (temporary delivery failure — mailbox full, server temporarily down):
- Kit retries soft bounces 3 times over 48 hours automatically
- If still failing after 3 retries, Kit marks the address "inactive" — it is removed from future sends but not deleted
- Soft bounces below 3% of any send are normal and require no action

**Hard bounce** (permanent delivery failure — invalid email, domain does not exist):
- Kit marks hard-bounced addresses as "unsubscribed" automatically
- Hard bounces above 1% of any send are a deliverability signal — investigate list source quality
- If hard bounce rate on a broadcast exceeds 1%: do not send another broadcast until you diagnose the source (spam form signups are the most common cause)

**ISP-level blocks** (an ISP blocking all Kit emails to its users — rare but possible):
- Signs: open rate drops to 0% for a specific email domain (e.g., all AOL.com addresses show 0 opens)
- Diagnosis: Kit > Broadcasts > Stats > Bounced tab > sort by domain
- Recovery: Contact Kit support; describe the affected domain; Kit's SendGrid infrastructure can request ISP delisting
- Timeline: 24–72 hours for ISP delisting requests

**Gmail tabs**: Kit emails sent from an unauthenticated sender domain may route to Gmail's "Promotions" tab. This reduces open rates by 15–20% compared to Primary inbox placement. Fix: authenticate your sender domain via SPF/DKIM in Kit settings (Settings > Email Settings > Sender Domain Authentication). Once authenticated, Gmail's algorithm re-evaluates placement over 2–4 weeks.

---

## Part 7: Week-by-Week Delivery Timeline Summary

| Week | Dates | Active email sends | Key actions |
|---|---|---|---|
| Launch Week | May 30 | Broadcast (1 send) + Email 1 (all new sign-ups) | Monitor open rate at T+4h, bounce rate at T+12h |
| Week 1 | May 31 – June 5 | Email 2 sends (Day 2 for May 30 sign-ups) | Watch Email 1 open rate: target 45%+ |
| Week 1 | June 2 | Email 3 sends (Day 5 for May 30 sign-ups) | Watch seed-saver tag count |
| Week 2 | June 4 | Email 4 sends (Day 7 for May 30 sign-ups) | Watch all 3 interest tag counts |
| Week 2 | June 5 (Thu) | Newsletter send #1 | First nurture send to completed-sequence subscribers |
| Week 2 | June 7 | Email 5 sends (Day 10 for May 30 sign-ups) | Watch coupon CTA click rate: target 8%+ |
| Week 2 | June 12 | Newsletter send #2 | Monitor open rate: target 28%+ |
| Week 2 | June 12 | Email 5 coupon expires for May 30 sign-ups | Log "Times Used" count in Etsy vs. Day 10 baseline |
| Week 3 | June 19 | Newsletter send #3 (seed saving theme) | Watch seed-saver segment opens vs. untagged: should be 10–15% higher |
| Week 4 | June 26 | Newsletter send #4 | 30-day review: log full subscriber count, average open rate, cumulative Etsy orders attributed to email |
| Week 4 | June 27 | 30-day analytics snapshot | Pull GA4 email acquisition report, Kit analytics export, Etsy "Times Used" count for SEEDWARDEN15 |

---

## Part 8: Email Health Metrics Reference

| Metric | Healthy | Alert | Action |
|---|---|---|---|
| Email 1 open rate | 45–60% | Below 30% | Check spam delivery; verify sender domain authentication; test subject line variant |
| Welcome sequence completion rate | 80–95% | Below 70% | Review Email 2–4 for unsubscribe triggers; check email content quality |
| Email 5 coupon click rate | 8–15% | Below 5% | Revise product recommendations; extend to 7-day window |
| Broadcast open rate | 30–45% | Below 20% | Investigate inbox placement; clean inactive subscribers from list before next broadcast |
| Newsletter open rate | 28–40% | Below 22% | Audit subject lines; reduce to bi-weekly temporarily |
| Unsubscribe rate per send | Below 1% | Above 2% | Review content-audience fit; investigate landing page messaging vs. email content alignment |
| Hard bounce rate | Below 0.5% | Above 1% | Investigate list source for spam signups; consider double opt-in |

---

*Prepared: 2026-05-09. This document is the Phase 2 email automation execution spec. For full email body copy, see `marketing/email-and-launch-plan.md`. For Kit platform setup steps, see `KIT_SETUP_NOTES.md` and `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md`. For launch broadcast send procedures, see `phase-2-launch-day-checklist.md`.*
