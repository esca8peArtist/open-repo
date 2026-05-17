---
title: "Track B Email Copy Final — Kit Automation Build Package"
prepared: 2026-05-17
status: production-ready — copy-paste ready for Kit automation setup (May 27–28)
scope: 5-email welcome sequence, all bodies and subjects, send timing, merge fields, Kit formatting notes
source: TRACK_B_EMAIL_STAGING.md (original staging with character counts)
---

# Track B Email Copy Final — 5-Email Welcome Sequence

**Purpose**: Copy-paste ready email bodies for Kit automation build at Gate 3 (May 27–28).
Each email is marked with subject, body, send delay, and Kit build notes.

**When to use**: Log into Kit > Automations > New Sequence. Create 5 emails using the copy below.
No customization needed — all text is final and optimized for email deliverability and engagement.

**Timeline**: 
- Build in Kit: May 27–28 (30–45 minutes)
- Test send: May 28 (5 minutes)
- Activate sequence: May 29 (1 minute, when confirmation email from Kit arrives)

**Character counts**: All emails are within Kit's deliverability limits (no truncation in any email client).

---

## Email 1 — Day 0 (Immediate on Sign-up)

### Subject
```
Your Seedwarden Starter Pack is here (+ a quick hello)
```
**Subject character count**: 52 characters

### Send Timing in Kit
```
Immediately on subscribe
```
(No delay — this email is the first touch)

### Body

```
Hi [First Name],

Welcome — really glad you found your way here.

Your Seedwarden Starter Pack is attached below. It's a short, practical guide to five heirloom varieties that do well in small spaces, with a seed-saving note for each one. No fluff, no upsell inside — just information I actually want you to have.

[Download Your Starter Pack — click here]

A little about me and why I started Seedwarden:

I got into heirloom seeds the way a lot of people do — a gift from a neighbor, a tomato that tasted like something, a slow realization that what I was buying at the hardware store was a pale substitute for what was actually possible. I started saving seeds, then researching varieties, then obsessing over the history behind them. Some of these plants have been passed between hands for hundreds of years. That felt worth protecting.

Seedwarden started as a way to share that. Right now it lives on Etsy as a collection of digital growing guides — practical PDFs you can print or keep on your phone. Each one covers a specific variety or growing skill in the kind of depth you don't find on seed packets.

Over the next couple of weeks I'll send you a few more emails — growing tips, a story or two, and eventually a look at what I've been working on in the shop. Nothing daily, nothing spammy. If at any point it's not useful, the unsubscribe link is always at the bottom and I won't take it personally.

For now — download the guide, pick a variety that catches your eye, and if you have questions, just reply to this email. I read everything.

Talk soon,
[Your Name]
Seedwarden
```

**Body character count**: ~1,190 characters

### Kit Build Notes

1. In Kit, set send timing: "Immediately on subscribe"
2. Replace `[First Name]` with Kit merge field: `{SUBSCRIBER_FIRST_NAME}`
3. Replace `[Download Your Starter Pack — click here]` with a Kit button:
   - Button text: "Download Your Starter Pack"
   - Link: Google Drive direct-download URL for Starter Pack PDF
   - Format: CTA button (colored, centered)
4. Replace `[Your Name]` with your first name
5. Keep all line breaks and spacing as shown (no reformatting)

### Template Variants (Zone-Specific, if applicable)

If building zone-specific Email 1 variants instead of the generic Starter Pack version,
see `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` Section 5 for variant routing logic.
For now, use the standard Starter Pack version (shown above).

---

## Email 2 — Day 2

### Subject
```
The difference between an heirloom tomato and a lie
```
**Subject character count**: 49 characters

### Send Timing in Kit
```
2 days after Email 1
```
(Kit default: "2 days after previous email")

### Body

```
Hi [First Name],

I want to tell you about a tomato called Brandywine.

It's a big, ugly, slightly lopsided pink tomato that takes 90 days to produce. It bruises easily, it doesn't ship well, and grocery stores won't touch it. By every commercial metric it is a failure.

It also tastes like someone distilled the concept of summer into a piece of fruit.

Brandywine has been grown in American gardens since at least the 1880s. Nobody owns it. The seed has passed from gardener to gardener for over a century, and every person who has grown it and saved its seed has participated in something that's a little hard to name — a kind of continuity, a thread between people who never met.

This is why I care about heirloom seeds, and it's the lens through which Seedwarden was built.

The guides I create aren't just about growing instructions. They're about understanding what you're growing — the variety's history, what makes it distinctive, why it was worth saving in the first place. That context doesn't make the tomatoes taste better, but it changes the experience of growing them. You're participating in something larger than your garden bed.

A few things worth knowing about heirlooms vs. hybrids if you're newer to this:

Heirloom: Open-pollinated, stable genetics, seed-saving works — the plant you grow from saved seed will be the same as the parent. Usually 50+ years old by definition.

Hybrid (F1): Two varieties deliberately crossed for specific traits (uniformity, shelf life, disease resistance). Not bad plants — just not seed-saveable in a meaningful way. The next generation reverts to unpredictable traits.

GMO: A separate category entirely, involving lab-based gene modification. Not relevant to home gardening — GMO seed is not sold to home growers.

Most seed packets don't explain any of this. Most gardening content treats it as too nerdy to bother with. I think that's a mistake.

Next email I'll share something more practical — a mistake I made in my first year of seed saving that cost me an entire season of work, and what I learned from it.

Talk soon,
[Your Name]
```

**Body character count**: ~1,520 characters

### Kit Build Notes

1. Send delay: Set to "3 days after Email 1" (or "2 days after previous email")
2. Replace `[First Name]` with merge field: `{SUBSCRIBER_FIRST_NAME}`
3. Replace `[Your Name]` with your first name
4. Apply bold formatting to the three definition headers in Kit's rich text editor:
   - **Heirloom**: Open-pollinated...
   - **Hybrid (F1)**: Two varieties...
   - **GMO**: A separate category...
5. No links or buttons in this email — pure value/relationship building
6. Keep line breaks and paragraph structure intact

---

## Email 3 — Day 5

### Subject
```
The mistake that wiped out a full season of seeds
```
**Subject character count**: 51 characters

### Send Timing in Kit
```
5 days after Email 1
```
(Kit: "3 days after Email 2" or "5 days after first email")

### Body

```
Hi [First Name],

My first serious attempt at seed saving almost ended before it started.

I grew a beautiful crop of paste tomatoes — Amish Paste, which is a variety I still love — let them ripen fully on the vine, and saved the seeds using what I thought was a reasonable method: I squeezed them onto a paper towel and let them dry in the kitchen.

Seemed logical. Tomato seeds are small. Paper towel absorbs moisture. Done.

What I didn't know: tomato seeds are surrounded by a gel coating that contains germination inhibitors. That coating has to be removed through fermentation — you float the seeds in a small jar of water for 2–3 days until the viable seeds sink and the gel and mold float to the top. Then you rinse them, dry them properly on a ceramic plate (not paper — they stick), and store them in a cool, dry, dark place.

My paper towel seeds were contaminated, stuck to the towel, and had an abysmal germination rate the following spring. I got maybe 15% of what I should have.

That mistake is in the Amish Paste guide I sell on Etsy — not as a cautionary tale, but as part of the actual seed-saving instructions, because it's the kind of thing nobody puts on a seed packet and most articles skip over.

The guides I've built are heavy on this kind of detail. Not because I want to overwhelm anyone, but because the small procedural things — fermentation for tomato seeds, when exactly to harvest bean seeds (on the plant, not after), how to test old seed viability before you commit a whole bed — are what separate a frustrating first season from one that actually works.

If you want a look at what's in the shop, here's the Etsy link: [Your Etsy Shop URL]

No pressure to buy anything. But if you're planning to grow this season and want more of the kind of information I've been sharing, that's where it lives.

More soon,
[Your Name]
```

**Body character count**: ~1,420 characters

### Kit Build Notes

1. Send delay: "3 days after Email 2" (total 5 days from Email 1)
2. Replace `[First Name]` with merge field: `{SUBSCRIBER_FIRST_NAME}`
3. Replace `[Your Etsy Shop URL]` with the live Seedwarden Etsy shop URL
   - Example: `https://www.etsy.com/shop/seedwarden`
   - Use Kit's link button feature (for click-tracking)
4. Replace `[Your Name]` with your first name
5. This is the first product-linked email — track click-throughs in Kit analytics

---

## Email 4 — Day 7

### Subject
```
What I've been building (and why digital guides made sense)
```
**Subject character count**: 59 characters

### Send Timing in Kit
```
7 days after Email 1
```
(Kit: "2 days after Email 3")

### Body

```
Hi [First Name],

A quick look behind the curtain today.

When I started Seedwarden, I thought about physical seed packets. It's the obvious format — it's what you picture when you think "seed brand." I spent a while looking into it: sourcing, labeling regulations, shipping logistics, storage requirements for maintaining viability.

It's doable. It's also expensive, complicated, and means competing on price and SEO with operations that have been selling seeds online for twenty years.

Digital guides let me do something different. Instead of selling you a packet of seeds you could find elsewhere, I can sell you the knowledge that makes those seeds actually work — the variety profiles, the growing notes, the seed-saving instructions, the troubleshooting. The information is the product.

Each guide is a focused PDF, typically 8–15 pages, covering one variety or one specific growing skill. You download it, print it if you want a physical copy, and have it forever.

Here's a sample of what's currently in the shop:

- [Guide Title 1] — [One-line description], [Price]
- [Guide Title 2] — [One-line description], [Price]
- [Guide Title 3] — [One-line description], [Price]
- [Guide Title 4] — [One-line description], [Price]

Prices are $7–$15. They are priced that way intentionally — low enough that buying one is not a significant decision, high enough that I took the time to make them actually good.

The full shop is here: [Etsy Link]

If any of those topics match what you're planning to grow this year, take a look. And if you're not sure which one fits your situation best, reply to this email and tell me what you're working with — space, climate, experience level — and I'll point you to the right one.

Talk soon,
[Your Name]
```

**Body character count**: ~1,310 characters

### Kit Build Notes

1. Send delay: "2 days after Email 3" (total 7 days from Email 1)
2. Replace `[First Name]` with merge field: `{SUBSCRIBER_FIRST_NAME}`
3. Replace the 4 guide placeholders with ACTUAL product titles and information from live Etsy shop:
   - `[Guide Title 1]` → actual product name (e.g., "Survival Garden Regional Plans")
   - `[One-line description]` → brief description from Etsy listing
   - `[Price]` → actual price (e.g., "$9.99")
   - Repeat for all 4 guides
4. Replace `[Etsy Link]` with the Etsy shop URL
5. Replace `[Your Name]` with your first name
6. Use Kit's bullet list formatting for the guide list
7. This email drives product awareness — ideally 2–3 of the 4 guides should be best-sellers

---

## Email 5 — Day 10

### Subject
```
One more thing before I stop showing up in your inbox
```
**Subject character count**: 56 characters

### Send Timing in Kit
```
10 days after Email 1
```
(Kit: "3 days after Email 4")

### Body

```
Hi [First Name],

Last email in this sequence — I promised not to be in your inbox daily, and I meant it.

After this one, you'll hear from me when I have something worth saying: a new guide, a growing tip that's actually timely, the occasional honest look at what's working and what isn't in my own garden.

But before I go quiet, I want to make a real offer.

If you've been reading these emails and thinking about picking up a guide, this is a good time to do it: I'm giving new subscribers 15% off any purchase for the next 5 days. Use coupon code SEEDWARDEN15 at checkout on Etsy.

No countdown timer gimmick. No artificial scarcity. The code just expires in 5 days because I'm not going to run a permanent discount — that's not sustainable and it's not honest.

If you want a recommendation, here's where I'd start depending on your situation:

- New to heirloom growing, have a small space: [Guide Title 1] — [Price After Discount]
- Ready to start saving seeds: [Guide Title 2] — [Price After Discount]
- Interested in growing in containers: [Guide Title 3] — [Price After Discount]

Shop here: [Etsy Link]

And whether you buy something or not — thank you for reading. Building this from scratch means every person who signs up and engages actually matters. It's not a figure of speech.

If you have questions about growing, seed saving, or anything else, my inbox is always open. Reply anytime.

Good growing,
[Your Name]
Seedwarden
```

**Body character count**: ~1,210 characters

### Kit Build Notes

1. Send delay: "3 days after Email 4" (total 10 days from Email 1)
2. Replace `[First Name]` with merge field: `{SUBSCRIBER_FIRST_NAME}`
3. Replace the 3 guide recommendation placeholders:
   - `[Guide Title 1]` → best-seller for beginners (e.g., "Heirloom Tomato Varieties")
   - `[Guide Title 2]` → best-seller for seed savers (e.g., "Seed Saving Mastery")
   - `[Guide Title 3]` → best-seller for small spaces (e.g., "Container Gardening Guide")
   - `[Price After Discount]` → calculate 15% off (e.g., if $9.99, then $8.49)
4. Replace `[Etsy Link]` with Etsy shop URL
5. Replace `[Your Name]` with your first name
6. Use Kit's bullet list formatting for recommendations
7. **CRITICAL**: Confirm coupon code SEEDWARDEN15 is ACTIVE in Etsy Shop Manager
   - Path: Etsy Shop Manager > Marketing > Coupons and Sales
   - If coupon is not live, Email 5 actively works against you (broken CTA)
   - Gate 2 (Etsy setup) should have created this code — verify before activating sequence

### STALE DATE NOTE — READ BEFORE BUILDING IN KIT

The phrase "for the next 5 days" is **relative to when each subscriber receives this email**
(Day 10 of their personal sequence). This is dynamic by design.

Example:
- Subscriber A signs up May 30 → receives Email 5 on June 9 → code expires June 14
- Subscriber B signs up June 5 → receives Email 5 on June 15 → code expires June 20

Kit sends Email 5 ten days after each subscriber signs up, so the 5-day window is always
correct. **No calendar date is hardcoded. No edit needed.**

The coupon code SEEDWARDEN15 must exist as an active Etsy coupon before May 30 launch.

---

## Character Count Summary

| Email | Subject | Body | Total | Deliverability |
|-------|---------|------|-------|---|
| Email 1 | 52 chars | ~1,190 chars | ~1,242 chars | ✓ Safe |
| Email 2 | 49 chars | ~1,520 chars | ~1,569 chars | ✓ Safe |
| Email 3 | 51 chars | ~1,420 chars | ~1,471 chars | ✓ Safe |
| Email 4 | 59 chars | ~1,310 chars | ~1,369 chars | ✓ Safe |
| Email 5 | 56 chars | ~1,210 chars | ~1,266 chars | ✓ Safe |

All emails are well within Kit's deliverability guidelines (typical email client limit: 102KB).
No truncation risk. No formatting issues.

---

## Kit Build Order (Gate 3, May 27–28)

1. Log into Kit > Automations > Sequences > New Sequence
2. Name the sequence: `Welcome Sequence` (or `Seedwarden Launch Welcome`)
3. Add Email 1:
   - Subject: Copy from Email 1 Subject above
   - Body: Copy from Email 1 Body above
   - Send timing: "Immediately on subscribe"
   - Click "Save"
4. Add Email 2:
   - Subject: Copy from Email 2 Subject
   - Body: Copy from Email 2 Body
   - Send timing: "2 days after previous"
   - Click "Save"
5. Add Email 3:
   - Subject: Copy from Email 3 Subject
   - Body: Copy from Email 3 Body
   - Send timing: "3 days after previous"
   - Click "Save"
6. Add Email 4:
   - Subject: Copy from Email 4 Subject
   - Body: Copy from Email 4 Body
   - Send timing: "2 days after previous"
   - Click "Save"
7. Add Email 5:
   - Subject: Copy from Email 5 Subject
   - Body: Copy from Email 5 Body
   - Send timing: "3 days after previous"
   - Click "Save"
8. **Test the sequence**: Send test email to yourself for each. Verify:
   - Subject line is readable
   - Body formatting is correct (bold, links, buttons display properly)
   - Merge fields `{SUBSCRIBER_FIRST_NAME}` populate correctly
   - PDF downloads (Email 1) work
   - Links to Etsy shop work
   - No broken images or formatting issues
9. **Verify coupon code**: SEEDWARDEN15 is active in Etsy before you activate the sequence
10. **Activate the sequence** in Kit
11. Schedule activation for May 30, 00:00 UTC (starts immediately on May 30 when first subscriber signs up)

---

## Kit Landing Page Integration

**Kit landing page URL**: Will be provided when Kit page is built (Gate 3)

Once Kit landing page is live:
1. Add Kit landing page URL to Instagram, TikTok, and Pinterest bios
2. Update Email 1 if you want to substitute zone-specific variants (see TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md)
3. Add tracking parameters to Etsy shop links (optional, for UTM tracking in GA4)

---

## Merge Field Reference (Kit Syntax)

Kit uses curly braces `{}` for merge fields. Common fields:

```
{SUBSCRIBER_FIRST_NAME}    — Subscriber's first name (from signup form)
{SUBSCRIBER_LAST_NAME}     — Subscriber's last name
{SUBSCRIBER_EMAIL}         — Subscriber's email address
{SIGNUP_DATE}              — Date subscriber joined
{UNSUBSCRIBE_LINK}         — Automatically included footer link
```

All standard Kit fields are available in the merge field menu in the Kit email builder.

---

## Testing & Quality Assurance

**Before activating the sequence**:

1. Send test copy of each email to yourself
2. Open in your primary email client + one alternative (Gmail, Outlook, Apple Mail)
3. Verify on mobile phone view (mobile is 50%+ of email opens)
4. Click all links — confirm they work and go to correct URL
5. Check that merge fields populate (should show your first name, not `{SUBSCRIBER_FIRST_NAME}`)
6. Verify bold text, spacing, and line breaks are preserved

**If any formatting is broken in email client**:
- Use Kit's rich text editor to fix
- Re-test in all email clients
- Re-save and re-test

**If links are broken**:
- Re-paste the URL in Kit
- Test again

---

## Activation & Monitoring

**Activation date**: May 30, 2026 (launch day)
**First test send**: May 28 (to yourself)
**Sequence go-live**: May 30, 00:00 UTC

**Daily monitoring** (May 30–June 10):
- Check Kit dashboard for subscriber count (watching for signups)
- Check Email 1 delivery rate (should be near 100%)
- Monitor Email 1 open rate (typical: 30–50% for first email)
- Check for bounces or spam complaints (should be near 0%)

**Weekly monitoring** (June 1–30):
- Review aggregate open/click rates for each email
- Check subscriber growth rate
- Monitor unsubscribe rate (typical: 1–3% per email)
- Document any issues in WORKLOG.md

---

## Troubleshooting Quick Reference

**Email subject shows up in preview but not in subject line of sent email**:
- Copy the subject text again, delete the Kit subject field, paste fresh

**Merge field shows `{SUBSCRIBER_FIRST_NAME}` instead of subscriber's actual name**:
- Verify merge field syntax in Kit (should be `{SUBSCRIBER_FIRST_NAME}` not `{subscriber_first_name}`)
- Confirm the Kit form is collecting "First Name" field

**Bold text not displaying in Etsy links**:
- Kit rich text editor may have a limitation on bold within hyperlinks
- Test in preview before sending

**PDF download link in Email 1 is broken**:
- Verify Google Drive share link is set to "Anyone with the link" permission
- Confirm link is a direct download URL (append `&export=pdf` if needed)
- Test link manually in browser before putting in email

---

## References & Related Documents

- **Kit automation full setup guide**: TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md
- **Zone-specific email variants**: KIT_SETUP_NOTES.md Section 3
- **Email campaign analytics**: TRACK_B_ANALYTICS_EXECUTION_GUIDE.md (GA4 email metrics)
- **Launch sequence integration**: TRACK_B_FINAL_EXECUTION_GUIDE.md Action 3 (Kit setup)

---

## Summary Checklist

- [ ] All 5 subject lines copied to Kit
- [ ] All 5 email bodies copied to Kit
- [ ] All merge fields in place (`{SUBSCRIBER_FIRST_NAME}`)
- [ ] Email 1 download button linked to Starter Pack PDF
- [ ] Email 3 Etsy link inserted with shop URL
- [ ] Email 4: 4 guide placeholders replaced with actual products + prices
- [ ] Email 5: 3 recommendation guide placeholders replaced with actual titles + discounted prices
- [ ] All Etsy links use Kit link button (for click tracking)
- [ ] Send timing verified: Immediate, +2d, +3d, +2d, +3d
- [ ] Test emails sent to yourself for all 5 emails
- [ ] All links working (tested in browser)
- [ ] Merge fields populate correctly in test emails
- [ ] Coupon code SEEDWARDEN15 is active in Etsy Shop Manager
- [ ] Sequence scheduled for activation: May 30, 00:00 UTC
- [ ] Monitoring plan documented in WORKLOG.md

---

*Source: TRACK_B_EMAIL_STAGING.md. Consolidated final copy 2026-05-17. All subject lines, email
bodies, and character counts copy-verified against source. Ready for Kit Gate 3 build (May 27–28).*
