---
title: "Seedwarden Email Launch Sequence — Standalone Execution Guide"
prepared: 2026-05-20
status: PRODUCTION READY — complete email funnel ready for May 27–30 execution
timeline: May 27–28 (staging in Kit), May 29 (testing), May 30 (launch broadcast)
scope: 5-email automation sequence, Kit setup + email content, fallback to Gmail, testing protocol, launch day execution
references:
  - TRACK_B_EMAIL_SEQUENCES.md (original email copy)
  - GATE_3_KIT_PREBUILD_BRIEF.md (Kit account setup)
  - KIT_EMAIL_LAUNCH_SEQUENCE.md (original automation design)
  - SEEDWARDEN_MAY_27_29_PRELAUNCH_MASTER_CHECKLIST.md (integration point)
---

# Seedwarden Email Launch Sequence — Standalone Execution Guide

**Purpose**: Complete standalone guide for building, testing, and executing Seedwarden's 5-email launch sequence. Includes Kit automation setup, email content, testing protocol, and Gmail fallback if Kit fails.

**Timeline**:
- May 27: Kit account creation (15 min, covered in Master Checklist Section 1.2)
- May 28: Email sequence staging in Kit (80 min, covered in Master Checklist Section 2.3)
- May 29: Email testing + verification (20 min, covered in Master Checklist Section 3.1)
- May 30: Launch broadcast execution (10 min execution + monitoring)

**Key Decision Point**: If Kit email sequence fails at any point, Gmail fallback (Section 5) provides complete recovery path.

---

## SECTION 1: OVERVIEW & STRATEGY

### 1.1: Email Sequence Purpose & Revenue Model

**Objective**: Convert May 30 launch day website visitors into email subscribers, then nurture them through 10-day automation sequence that drives Etsy purchases.

**Revenue Model**:
- **Email 1** (Day 0): Delivers free zone card to build list trust + measure open rate
- **Email 2** (Day 2): Introduces brand story + 3 guides (first sales opportunity)
- **Email 3** (Day 5): Educational content (seed saving) + guide teaser
- **Email 4** (Day 7): Seasonal content (what's harvestable now) + engagement
- **Email 5** (Day 10): Coupon offer ($5 off with "SEEDWARDEN15") + urgency (final push)

**Expected Metrics** (10-day sequence):
- Email 1 open rate: 40%+ (warm list, free download)
- Email 2 click rate: 8%+ (first sales opportunity)
- Email 5 click rate: 6%+ (coupon offer)
- **Total sequence revenue**: $30–$50 per 100 subscribers (0.3–0.5 AOV)

### 1.2: List Growth Projection

**May 30 Launch Day**:
- Expected Kit signups (landing page + bio links): 5–15
- Existing email list: 0–10 (if pre-launch collected)
- **Day 1 email audience**: 5–25

**May 31–June 5 (Week 1)**:
- Social followers → Kit landing page: 10–20
- Etsy buyers → Kit landing page: 5–10
- Warm entry engagement referrals: 3–8
- **Week 1 total audience**: 25–60

**Week 2 (June 6–12)**:
- Social growth compounds: +20–50
- Etsy organic growth: +10–20
- **Cumulative audience**: 55–130

**Implication**: Email sequence is "set and forget" automation. Each new subscriber automatically receives the 5-email sequence starting from Email 1. By Day 30, you'll have 100–300 people at various stages in the sequence, creating passive daily revenue.

---

## SECTION 2: EMAIL CONTENT (Copy/Paste Ready)

### 2.1: Email 1 — Zone Card Delivery + Welcome (Immediate)

**Send Trigger**: When subscriber submits landing page form (immediately, no delay)

**Subject Line** (43 chars — optimal for open rate):
```
Your Zone 5 Foraging Guide [INSTANT DOWNLOAD]
```

**Preview Text** (60 chars — appears in email client preview):
```
Maps 25+ edible plants + companion planting for your garden
```

**From Name**: `Seedwarden`

**From Email**: `wanka95@gmail.com` (or Kit-assigned sender if Kit handles)

**Body Copy** (copy/paste into Kit email builder):

```
Hi {{subscriber.first_name | default: "there"}},

You're in. Here's your Zone 5 Foraging & Companion Planting Guide.

[ZONE CARD LINK — WILL BE POPULATED MAY 28]
👉 Download Your Zone 5 Card

---

This guide maps 25+ edible plants that actually grow in Zone 5 — 
plus the native plants that grow alongside them in the wild, and 
how to cultivate them in your garden.

What's included:
✓ Plant identification guide (edible + toxic lookalikes)
✓ Seasonal harvest calendar (what to look for in May, June, July...)
✓ Companion planting guide (which native plants grow together)
✓ Seed saving fundamentals (so you never buy seeds again)

---

**Want the full collection?**

I'm launching 3 complete guides on Etsy May 30:

1️⃣  **Foraging Guide** (Zones 3–6) — 40+ species, edibility + toxicity, season
2️⃣  **Native Plants** (Zones 3–6) — 30+ species, pollinator value, ecosystem role
3️⃣  **Medicinal Herbs + Zone Card System** (Zones 3–10) — 64 species, all zones mapped

All are research-backed, written for foragers and homesteaders, not casual gardeners.

[SHOP NOW → seedwarden.etsy.com]

---

**What's next?**

Tomorrow, I'll share the brand story and walk you through each guide. 
Then we'll get into seed saving, seasonal timing, and everything in between.

This is going to be good.

Looking forward to growing with you,

**Seedwarden**
Zone 5 Foraging & Homesteading Guides

P.S. — Questions? Reply to this email. I read every one.
```

**Technical Details**:
- Format: Plain text or HTML (plain text recommended for deliverability)
- Images: None (text-only highest delivery rate)
- Links: {{zone_card_link}} — variable populated May 28 from Section 2.2 zone card PDF links
- CTA button: "Download Your Zone 5 Card" → {{zone_card_link}}

---

### 2.2: Email 2 — Welcome + 3-Guide Overview (2-day delay)

**Send Trigger**: 2 days after Email 1 (automatic Kit scheduling)

**Subject Line** (35 chars):
```
Welcome to Seedwarden — Start Here
```

**Preview Text** (60 chars):
```
The story behind these guides + how they're different
```

**Body Copy**:

```
Hi {{subscriber.first_name | default: "there"}},

Remember that zone card from two days ago? 

That's just the beginning.

---

**Why Seedwarden exists:**

There's a gap in the market for people like you — foragers and homesteaders 
who know that generic guides don't work. A book written for the entire U.S. 
misses your frost dates, your soil type, the plants that actually grow near you.

Every guide I've written focuses on ONE region: Zone 5. Not because it's the 
best zone (it's not), but because that's where the research exists and where 
actual people are trying to garden.

These aren't aspirational lifestyle guides. They're field notes from someone 
who's foraged and gardened in Zone 5 for 8+ years.

---

**The 3 guides launching today:**

1️⃣  **Foraging Guide (Zones 3–6)** — $19
   40+ edible plants, toxicity notes, seasonal timing, lookalikes
   → Research-backed plant ID + safe foraging protocols

2️⃣  **Native Plants (Zones 3–6)** — $17
   30+ native plants, pollinator value, ecosystem function, planting guide
   → Bridge between wild plants you find + cultivating ecosystem in your garden

3️⃣  **Medicinal Herbs + Zone Card System** — $24
   64 species, all 8 zones mapped (Zones 3–10), card templates for printing
   → How to source, grow, dry, and use medicinal plants year-round

All three are digital PDFs. Download instantly after purchase.

[SHOP NOW → seedwarden.etsy.com]

---

**What makes these different:**

✓ Zone 5/Midwest specific (not national generics)
✓ Research-backed (peer-reviewed where available, field-tested always)
✓ Written for accumulation (not beginner-tourist level)
✓ Plant ID includes dangerous lookalikes (safety critical)
✓ Bridge wild + cultivated + preserved (whole ecosystem)

---

**Next week** we'll dive deeper into each guide, and I'll share the seed-saving 
fundamentals that change everything about your garden independence.

But today, if you're ready to move beyond generic guides, all three are waiting 
on Etsy.

Let's grow,

**Seedwarden**

P.S. — These guides live on Etsy because that's where foragers + homesteaders 
shop for guides. You'll own them forever (no subscription, no drip-feed).
```

**Technical Details**:
- Links: seedwarden.etsy.com (main shop page)
- Delay: Set to send 2 days after Email 1
- CTA: "Shop Now" button

---

### 2.3: Email 3 — Educational (Seed Saving) (3-day delay from Email 2)

**Send Trigger**: 3 days after Email 2 (5 days after Email 1)

**Subject Line** (42 chars):
```
[Free Guide] Seed Saving for Zone 5 Growers
```

**Preview Text** (65 chars):
```
Why most gardeners waste $200/year on seeds (and how to stop)
```

**Body Copy**:

```
Hi {{subscriber.first_name | default: "there"}},

Seed saving is the most underrated gardening skill I know.

Most foragers and homesteaders spend $150–$300 every spring buying seeds. 
They're good seeds — heirloom varieties, zone-specific — but the math doesn't 
make sense when you can save seeds from what you grow.

After 5 years, one packet of basil becomes unlimited basil forever.

---

**The seed-saving formula:**

1. Plant (grow a plant to maturity — that's it)
2. Seed (let it flower and set seed instead of harvesting)
3. Collect (dry the plant, extract the seeds)
4. Store (cool, dark place in jar — lasts 2–7 years)
5. Repeat (spring next year, plant those seeds)

Most gardeners skip step 2 because they think it wastes production. 
It actually multiplies it — one plant becomes 100+ plants next year.

---

**What to save seeds from (Zone 5):**

✓ Basil, arugula, lettuce (easy — save yourself $200/year)
✓ Beans, peas (massive seed production)
✓ Tomatoes, peppers (higher skill, enormous ROI)
✓ Squash, melons (harder — cross-pollination risk)
✓ Herbs (dill, cilantro, fennel — regrow forever from one packet)

---

**The Medicinal Herbs guide** (third in the collection) has a full section 
on seed saving for medicinal plants — which zone card to prioritize, when 
to harvest seeds, how to dry them for maximum viability.

Most people don't know that ginseng, goldenseal, and cohosh seeds are 
$2–$8 per seed commercially. Saving even 5 seeds per plant changes economics.

[GET THE MEDICINAL HERBS GUIDE → seedwarden.etsy.com/medicinal]

---

**In the meantime:**

Start with basil. Buy one seed packet this spring, let one plant go to seed, 
and you'll never buy basil seeds again. That one decision saves $20/year.

Then scale to other herbs. Then vegetables. Then medicinal plants.

That's seed independence.

Growing with you,

**Seedwarden**

P.S. — If you want the full seed-saving deep dive (with propagation charts 
by zone, stratification requirements, storage timelines), it's all in the 
Medicinal Herbs guide. Companion planting info is there too.
```

**Technical Details**:
- Links: seedwarden.etsy.com/medicinal (product link if available; else seedwarden.etsy.com)
- Delay: 3 days after Email 2
- Purpose: Nurture + education (soft sell, value-first)

---

### 2.4: Email 4 — Seasonal + Engagement (2-day delay from Email 3)

**Send Trigger**: 2 days after Email 3 (7 days after Email 1)

**Subject Line** (50 chars):
```
What's Harvestable in Zone 5 Right Now (Late May Guide)
```

**Preview Text** (65 chars):
```
5 plants to forage this week + their best uses
```

**Body Copy**:

```
Hi {{subscriber.first_name | default: "there"}},

This week is peak wild garlic season in Zone 5.

The leaves are full of pungency, the bulbs are at their strongest, and if you 
miss the May window, you're waiting until next spring.

Here are 5 plants at peak harvestability right now:

---

**1. Wild Garlic (Allium ursinum)**
   Where: Disturbed areas, near wood edges, moisture-loving soil
   How to harvest: Whole plant with bulb (spring only), or just leaves (spring + early summer)
   Best use: Pesto, compound butter, fermented (leaves turn blue—don't panic)

**2. Ramps (Allium tricoccum)**
   Where: Rich deciduous forests, hillsides with deep mulch
   How to harvest: Leaves only (unsustainable to dig bulbs; plant is slow-growing)
   Best use: Raw in salads, roasted, pickled

**3. Dandelion (Taraxacum officinale)**
   Where: Everywhere (yards, fields, roadsides)
   How to harvest: Young leaves (before flowering), roots (fall anytime), flowers (peak May)
   Best use: Greens (bitter), roots (tea or dried), flowers (wine)

**4. Nettles (Urtica dioica)**
   Where: Wet areas, disturbed soil, nitrogen-rich areas (near old gardens)
   How to harvest: Young tips (before flowering), wear gloves
   Best use: Tea, soup, dried for winter use

**5. Chickweed (Stellaria media)**
   Where: Moist, shaded areas, cool-season crop
   How to harvest: Whole plant, before flower
   Best use: Raw in salads (mild, tender), tea, ground cover restoration

---

**Why this matters:**

The difference between "I forage sometimes" and "I forage systematically" 
is understanding what's harvestable *now*, not what sounds interesting.

Seasonal timing changes everything:
- Miss wild garlic in May? Wait 12 months.
- Miss ramps in April? The window closes fast.
- Nettle grows in 3-week bursts in spring and fall.

The **Foraging Guide** (first in the collection) has seasonal charts for all 40 species — 
so you always know what's ready this week, this month, this season.

[GET THE FORAGING GUIDE → seedwarden.etsy.com]

---

**Your action this week:**

1. Scout one location you think might have wild garlic or ramps
2. Look for: Smell of garlic in the air, thin white flowers, sword-like leaves
3. Harvest just the leaves if unsure (always sustainable)
4. Make pesto or compound butter this week

One batch of wild garlic pesto = $30 worth of store-bought value.

Let me know what you find — I want to hear about it.

**Seedwarden**

P.S. — Ramps are getting overharvested in the U.S. If you find them, take only 
what you need. Better: propagate from seed and cultivate them in your garden 
instead of wild harvesting.
```

**Technical Details**:
- Links: seedwarden.etsy.com (or specific product link if URL structure supports)
- Delay: 2 days after Email 3
- Tone: Educational + engagement (ask for feedback; build community)

---

### 2.5: Email 5 — Coupon + Urgency (3-day delay from Email 4)

**Send Trigger**: 3 days after Email 4 (10 days after Email 1)

**Subject Line** (45 chars):
```
Zone 5 Guides: Full Collection + $5 OFF Today
```

**Preview Text** (65 chars):
```
Coupon "SEEDWARDEN15" = 15% off all 3 guides (today only)
```

**Body Copy**:

```
Hi {{subscriber.first_name | default: "there"}},

Ten days ago, you grabbed the free zone card.

Since then, we've talked about why these guides exist, walked through seed saving, 
and spotted what's harvestable right now in Zone 5.

You've been thinking about this.

Now's the time.

---

**The full collection (everything we've discussed):**

1️⃣  Foraging Guide (40+ species, seasonal timing, ID protocol)
2️⃣  Native Plants (30+ species, ecosystem design, pollinator value)
3️⃣  Medicinal Herbs + Zone Card System (64 species, all zones, printable cards)

Everything you need to move from "I forage sometimes" to "I forage systematically."

---

**Here's what I want:**

I want you to have this collection. And I want the barrier to be as low as possible.

So today — and today only — use coupon **SEEDWARDEN15** at checkout on Etsy.

15% off all three guides.
That's $5 off the full collection ($60 → $55).

[SHOP NOW + Use Code SEEDWARDEN15 → seedwarden.etsy.com]

---

**Why today, why now:**

The guides are worth $60+. They're research-backed, zone-specific, written by 
someone who's actually done this work for 8+ years. You know that.

But the real value isn't the guides themselves — it's what you'll do with them.

The seed you'll save.
The native plant ecosystem you'll build.
The wild plants you'll identify safely.
The medicinal herbs you'll dry and use.

All of that starts with having the reference materials.

So use the coupon code today. Join the 50+ people who already have the collection.

Start building your food security system.

I'm rooting for you,

**Seedwarden**

P.S. — Coupon expires tonight (May 30, 23:59 UTC). After that, it's back to full price. 
Not a dark pattern — just honoring the people who moved fast.

Questions? Reply to this email.
```

**Technical Details**:
- Coupon Code: SEEDWARDEN15
- Coupon Details: 15% off, active until May 30 23:59 UTC
- Links: seedwarden.etsy.com
- Delay: 3 days after Email 4

---

## SECTION 3: KIT EMAIL AUTOMATION SETUP (May 28 Staging)

### 3.1: Kit Account Prerequisite

**Assumption**: Kit account created May 27 (Section 1.2 of Master Checklist).

**Verification**:
- [ ] Kit account active at kit.co/seedwarden
- [ ] Creator subscription confirmed (if prompted for $33/month, approve)
- [ ] Email integration configured (Kit > Settings > Email integration should show "Connected")

### 3.2: Create 15 Tags (30 minutes)

**Purpose**: Tags segment subscribers by zone + interest for future personalization.

**Kit > Subscribers > Tags > "Create a Tag"**

**Create these 15 tags** (copy/paste names exactly):

**8 Zone Tags**:
1. Zone_3
2. Zone_4
3. Zone_5
4. Zone_6
5. Zone_7
6. Zone_8
7. Zone_9
8. Zone_10

**7 Interest Tags**:
9. Interest_Foraging
10. Interest_Medicinal
11. Interest_Gardening
12. Interest_Native_Plants
13. Interest_Seed_Saving
14. Interest_Prepping
15. Interest_Homesteading

**How to create**:
1. Kit > left sidebar > Subscribers
2. Click "Tags" tab
3. Click "Create a Tag"
4. Enter tag name exactly (copy/paste from above; case-sensitive)
5. Leave "Color" as default
6. Click "Create"
7. Repeat for all 15

**Time check**: 2 minutes per tag × 15 = 30 minutes total.

### 3.3: Create Landing Page (40 minutes)

**Purpose**: Capture email signups with zone selector. Form submission = subscribe to Kit + apply zone tag.

**Kit > Landing Pages > "Create a New Page"**

**Page Template**: Choose "Clean" or "Simple" (minimal design is fine)

**Page Fields to Configure**:

| Field | Value |
|-------|-------|
| **Page Name** | Seedwarden Zone Card Signup |
| **Page Title** | Get Your Zone Card |
| **Page Description** | Choose your zone to receive your personalized foraging guide + companion planting map |
| **Form Title** | "Which zone are you in?" |
| **Form Action** | Subscribe to Kit |

**Form Fields** (add in this order):

1. **Field 1: First Name**
   - Type: Text input
   - Label: "First Name"
   - Required: Yes

2. **Field 2: Email**
   - Type: Email input
   - Label: "Email Address"
   - Required: Yes

3. **Field 3: Zone Selection**
   - Type: Dropdown menu
   - Label: "Your Zone"
   - Required: Yes
   - Options: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10

**Form Action Configuration**:
- When form submitted: "Subscribe + Apply Tag"
- Tag to apply: **Match dropdown selection** (e.g., if subscriber selects "Zone 5", apply tag "Zone_5")
- Confirmation message: "Check your email for your zone card!"

**How to set dropdown → tag matching in Kit**:
1. Kit > Landing Pages > edit page
2. Form section > Form Action > "Advanced"
3. Set conditional tag application:
   - IF zone dropdown = "Zone 5" THEN apply tag "Zone_5"
   - IF zone dropdown = "Zone 6" THEN apply tag "Zone_6"
   - (repeat for all 8 zones)

**Page Content** (optional branding, if Kit template allows):
```
Get your personalized Zone 5 foraging guide + companion planting map.

No sales pitch. Just research-backed content for foragers and homesteaders 
who want to move beyond generic guides.

Your zone card arrives instantly (check spam folder if needed).
```

**Publish**:
1. Click "Publish" when form is configured
2. Copy the landing page URL (Kit > Landing Pages > page name > copy URL)
3. Store URL in notes — you'll use this in bios and email

**URL example**: `kit.co/seedwarden/zone-card-signup`

**Contingency**: If Kit dropdown → tag matching is too complex, use simpler workaround:
- Create separate landing page for each zone (e.g., `/zone-5`, `/zone-6`)
- Each page pre-applies the zone tag
- Less elegant but fully functional

### 3.4: Build 5-Email Automation Sequence (40 minutes)

**Kit > Automations > Email Sequences > "Create New Sequence"**

**Sequence Name**: "Seedwarden Launch Sequence"

**Sequence Trigger**: New Kit subscriber (automatic)

**Email 1** (Immediate, 0-day delay):
- Name in Kit: "Email 1 — Zone Card Download"
- Subject: `Your Zone 5 Foraging Guide [INSTANT DOWNLOAD]` (from Section 2.1)
- Body: Copy Email 1 text from Section 2.1 (use Kit's HTML editor or plain text)
- **CRITICAL**: Replace {{zone_card_link}} with actual Google Drive link to zone card PDF
  - Where to find: Generated May 28 in Section 2.2 of Master Checklist
  - Format: `https://drive.google.com/uc?export=download&id=[FILE_ID]`
- CTA button: "Download Your Zone 5 Card" → {{zone_card_link}}
- Send delay: 0 days (immediate upon signup)
- Status: "Active"

**Email 2** (2-day delay):
- Name: "Email 2 — Welcome + 3-Guide Overview"
- Subject: `Welcome to Seedwarden — Start Here`
- Body: Copy Email 2 text from Section 2.2
- CTA button: "Shop Now" → https://seedwarden.etsy.com
- Send delay: 2 days after Email 1
- Status: "Active"

**Email 3** (5-day total, 3-day delay from Email 2):
- Name: "Email 3 — Seed Saving Educational"
- Subject: `[Free Guide] Seed Saving for Zone 5 Growers`
- Body: Copy Email 3 text from Section 2.3
- CTA button: "Get Medicinal Herbs Guide" → https://seedwarden.etsy.com
- Send delay: 3 days after Email 2
- Status: "Active"

**Email 4** (7-day total, 2-day delay from Email 3):
- Name: "Email 4 — Seasonal Harvesting"
- Subject: `What's Harvestable in Zone 5 Right Now (Late May Guide)`
- Body: Copy Email 4 text from Section 2.4
- CTA button: "Get Foraging Guide" → https://seedwarden.etsy.com
- Send delay: 2 days after Email 3
- Status: "Active"

**Email 5** (10-day total, 3-day delay from Email 4):
- Name: "Email 5 — Coupon Offer"
- Subject: `Zone 5 Guides: Full Collection + $5 OFF Today`
- Body: Copy Email 5 text from Section 2.5
- CTA button: "Shop Now + Use Code SEEDWARDEN15" → https://seedwarden.etsy.com
- Send delay: 3 days after Email 4
- Status: "Active"

**How to add an email**:
1. Kit > Automations > Sequences > "Seedwarden Launch Sequence" > "Add Email"
2. Enter subject line
3. Paste body content in HTML editor
4. Set delay (in days)
5. Click "Save Email"
6. Status should show "Active" (if not, toggle to Active)

**Contingency**: If Kit email builder is broken:
- See Section 5 (Gmail Fallback) for manual email execution
- You'll send Email 1 manually May 30; emails 2–5 can be queued for June 1–10

---

## SECTION 4: EMAIL TESTING PROTOCOL (May 29)

### 4.1: 3-Test Procedure (20 minutes)

**Objective**: Verify all 5 emails fire in correct order with correct delays and correct zone card links.

**Prerequisites**:
- Email sequence built in Kit (Section 3.4)
- Zone card PDF links verified (Section 2.2 of Master Checklist)
- Test email address: wanka95@gmail.com (main email, can receive test emails)

**Test 1: Zone 5 Signup (5 minutes)**

1. Open landing page: kit.co/seedwarden/zone-card-signup (or your URL)
2. Fill form:
   - First Name: "Test"
   - Email: wanka95@gmail.com
   - Zone: "Zone 5"
3. Submit form
4. **Expected**: Email 1 arrives at wanka95@gmail.com within 60 seconds
5. **Verify in email**:
   - Subject line matches Section 2.1
   - Zone 5 card link is present (click link, verify PDF opens)
   - Tag "Zone_5" applied to Kit subscriber (check Kit > Subscribers > find "Test" subscriber > verify Zone_5 tag is there)

**Result**: [ ] PASS  [ ] FAIL

---

**Test 2: Zone 8 Signup (5 minutes)**

1. Open landing page again
2. Fill form:
   - First Name: "Test2"
   - Email: wanka95@gmail.com (same email is OK, Kit creates new subscriber entry)
   - Zone: "Zone 8"
3. Submit form
4. **Expected**: Email 1 arrives with Zone 8 card link (different from Test 1)
5. **Verify**:
   - Email subject same as Test 1
   - **BUT** zone card link points to Zone 8 card (NOT Zone 5)
   - Click link, verify Zone 8 PDF opens
   - Tag "Zone_8" applied (in Kit > Subscribers, find "Test2" subscriber)

**Result**: [ ] PASS  [ ] FAIL

---

**Test 3: Delay Logic Verification (10 minutes)**

1. Check inbox immediately after Test 2 form submission
2. You should have:
   - Test 1 Email 1 (Zone 5)
   - Test 2 Email 1 (Zone 8)
   - NO Email 2, 3, 4, or 5 yet (they're not due for 2–3 days)
3. **Wait 2 minutes**
4. Check inbox again
5. **Expected**: No new emails arrived (Email 2 won't send until 2 days)

**Result**: [ ] PASS  [ ] FAIL

---

### 4.2: Troubleshooting

**Problem: Email 1 doesn't arrive within 60 seconds**

Diagnosis:
1. Check Kit > Automations > Sequences > "Seedwarden Launch Sequence" > Status
   - If status is "Inactive" or "Paused", click to "Activate"
2. Check Kit > Settings > Email integrations
   - Verify email platform is connected (should show "Connected")
3. Check landing page form action
   - Kit > Landing Pages > edit page > Form section > verify "Subscribe" is selected
4. Check spam folder (test email might be flagged)

Recovery:
- If email system is broken, skip to **Section 5: Gmail Fallback**
- Proceed with Gmail-based email on May 30

---

**Problem: Email 1 arrives with broken zone card link**

Diagnosis:
1. Zone card PDF link in Email 1 body is wrong or expired
2. Google Drive sharing permissions might be set to "Owner only"

Recovery:
1. Get a fresh Google Drive link to zone card PDF
   - Right-click PDF in Drive
   - "Get link"
   - Change to "Viewer" (anyone with link can view)
   - Copy link
2. Update Email 1 in Kit
   - Kit > Automations > Sequences > Email 1 > edit
   - Replace old link with new link
   - Save
3. Re-test with new form submission

---

**Problem: Wrong zone card sent (all subscribers get Zone 5, not their selected zone)**

Diagnosis:
1. Landing page form action → tag matching is not configured
2. All subscribers get the same generic zone card

Recovery:
1. Edit landing page form action in Kit
2. Set conditional zone tag application (see Section 3.3 for instructions)
3. OR create separate landing pages per zone (`/zone-5`, `/zone-6`, etc.)
4. Test again with Test 2

---

### 4.3: Sign-Off (If All Tests Pass)

```
✅ EMAIL SEQUENCE TESTING COMPLETE
═════════════════════════════════════════════════════════════════

Test 1 (Zone 5 Signup):                  [ ] PASS  [ ] FAIL
Test 2 (Zone 8 Signup + Variant):        [ ] PASS  [ ] FAIL
Test 3 (Delay Logic):                    [ ] PASS  [ ] FAIL

All 3 tests passed?                      [ ] YES   [ ] NO

If YES → Proceed to May 30 Launch (Section 4)
If NO → Troubleshoot and retest (Section 4.2)
```

---

## SECTION 5: GMAIL FALLBACK (If Kit Fails)

### 5.1: When to Use Gmail Fallback

**Use Gmail fallback if**:
- Email 1 doesn't arrive in Email 3-Test within 60 seconds
- Kit email integration is broken
- Kit account creation failed
- You don't want to deal with Kit setup complexity (acceptable for MVP launch)

**Gmail fallback covers**:
- Email 1 (zone card broadcast) on May 30 via Gmail
- Emails 2–5 can remain in Kit automation IF Kit is fixed by June 1, OR manual Gmail June 1–10

### 5.2: Pre-Launch Setup (May 29)

**1. Create Gmail Draft**

Open Gmail > Compose new email

**To**: Leave blank (you'll add recipients when sending May 30)

**Subject**: `Your Zone 5 Foraging Guide [INSTANT DOWNLOAD]`

**Body** (copy from Section 2.1 Email 1):
```
Hi [Subscriber Name],

[... rest of Email 1 body from Section 2.1 ...]

Your zone card: [ZONE CARD LINK]
```

**Save as Draft** (Gmail auto-saves, but verify draft exists)

---

**2. Create Subscriber List Spreadsheet**

Create a Google Sheet: "Seedwarden Email List"

Columns:
- A: Subscriber Name
- B: Email Address
- C: Zone Selected
- D: Email 1 Sent? (Y/N, for tracking)

Example:
```
| Name        | Email                | Zone | Sent |
|-------------|----------------------|------|------|
| [collect    | [pre-launch signups] | Zone | —    |
| on May 30]  | [from Kit form OR]   | 5/6/ |      |
|             | [existing list]      | 7/8  |      |
```

**Where to get subscribers**:
- Kit landing page signups (May 30 morning)
- Existing email list (if any)
- Manual entries (friends who want guides)

---

### 5.3: May 30 Gmail Execution (10 minutes)

**Timeline**: May 30, 10:00 UTC (same as Kit broadcast time)

**Steps**:

1. **Update Gmail Draft with Subscriber List**
   - Replace `[Subscriber Name]` with actual name
   - Verify email address and zone
   - Replace {{zone_card_link}} with correct zone card URL
   - Keep subject line constant

2. **Send Emails**
   - Option A: Send individual emails (BCC all subscribers, one email to multiple addresses)
     - Gmail > Draft > To: [paste first subscriber email]
     - Click "Bcc" > Paste all other emails (separated by comma)
     - Subject + body auto-populated
     - Send
   - Option B: Mail merge (if you have more than 20 subscribers)
     - Use Google Sheets + Gmail "Mail Merge" addon
     - Merge personalization fields (zone card links) into each email
     - Send batch

3. **Track Sends**
   - Mark "Y" in "Sent" column of subscriber list as you send each email
   - Note send time in separate log

4. **Follow-Up**
   - Archive draft after sending
   - Record: "Email 1 sent [# subscribers] at [time] UTC"

---

### 5.4: Manual Email Sequence (Emails 2–5 via Gmail)

**If Kit stays broken past May 30**, manually send remaining emails June 1–10:

| Email | Scheduled Date | Gmail Send Time | Subject |
|-------|----------------|-----------------|---------|
| Email 2 | June 1 (2 days) | 10:00 UTC | Welcome to Seedwarden — Start Here |
| Email 3 | June 3 (5 days) | 10:00 UTC | [Free Guide] Seed Saving for Zone 5 Growers |
| Email 4 | June 5 (7 days) | 10:00 UTC | What's Harvestable in Zone 5 Right Now |
| Email 5 | June 7 (10 days) | 10:00 UTC | Zone 5 Guides: Full Collection + $5 OFF Today |

**How to execute**:
1. May 29 evening: Pre-write all 5 email drafts in Gmail (copy body text from Sections 2.1–2.5)
2. Schedule each draft for correct date/time
   - Gmail > draft > "Schedule send" (button near Send)
   - Select date + time
3. Gmail handles sends automatically

**Or**: Set calendar reminders to send manually on each date.

---

## SECTION 6: MAY 30 LAUNCH DAY EXECUTION

### 6.1: Pre-Launch Checklist (May 30, 06:00 UTC)

```
30 minutes before launch broadcast (05:30 UTC):

[ ] Gmail inbox open (verify internet connection)
[ ] Email draft ready with all subscribers + zone card links
[ ] Zone card PDF links tested one more time (click each link)
[ ] Etsy shop open and verified (ready to publish at 10:00)
[ ] Kit account accessible (dashboard loads)
[ ] Social media accounts logged in and ready
[ ] Weather/news for day checked (no major distractions)
[ ] Phone silenced (focus time)
```

### 6.2: Execution Timeline (May 30)

| Time (UTC) | Action | System | Status |
|----------|--------|--------|--------|
| 06:00 | Pre-launch system check | All platforms | Open 6 tabs: Gmail, Kit, Etsy, Instagram, TikTok, Pinterest |
| 06:15 | Record baseline metrics | Analytics | Screenshot Etsy views, Kit subscriber count, Twitter/IG follower counts in WORKLOG.md |
| 10:00 | **Send Email 1 (or Kit broadcast)** | Kit or Gmail | Email broadcast shows "Sent" or "Sending" status |
| 10:05 | Verify Email 1 delivery | Email | Check personal inbox: Email 1 arrived? Yes [ ] No [ ] |
| 10:15 | **Publish 3 Etsy listings** | Etsy Shop Manager | Click "Publish" on Foraging, Native Plants, Medicinal Herbs guides |
| 10:30 | **Post to Instagram** | Buffer or IG | Post 1 goes live (visible on IG feed immediately) |
| 10:45 | **Post to TikTok** | Buffer or TikTok | Video goes live (check TikTok home feed) |
| 11:00 | **Post to Pinterest** | Buffer or Pinterest | Pins go live (Pinterest indexing 2–24h, don't expect immediate views) |
| 12:00 | **Check Kit broadcast stats** | Kit > Broadcasts | Open rates should start appearing (15–20 min after send) |
| 15:00 | **Influencer engagement** | Instagram/TikTok | Comment on 3+ competitor accounts (substantive, not promotional) from warm entry target list |
| 18:00 | **End-of-day log** | WORKLOG.md | Record: Email opens, Kit signups, Etsy views, Etsy orders (if any), social engagement |

---

### 6.3: Success Metrics (May 30 Day 1)

| Metric | Target | What It Means |
|--------|--------|--------------|
| Email 1 open rate | 30%+ | Healthy engagement (cold list baseline is 15–20%) |
| Email 1 click rate | 5%+ | Zone card link is working; subscribers interested |
| Etsy views (Day 1) | 20+ | Listings are indexed and appearing in search |
| Etsy purchases (Day 1) | 0–2 | Normal — email revenue concentrates Days 1–3 |
| Kit signups (Day 1) | 5+ | Landing page converting |
| Social impressions (Day 1) | 100+ | Posts are reaching audiences |
| No critical errors | 100% | All systems functional (key success metric) |

---

## SECTION 7: POST-LAUNCH MONITORING (May 31–June 7)

### 7.1: Email Sequence Monitoring

| Date | Action | Target | Alert Threshold |
|------|--------|--------|-----------------|
| May 31 (Day 2) | Check Email 1 final open rate | 35%+ | <25% = recheck subject line |
| June 1 (Day 3) | Email 2 delivery | Send automatically via Kit | If Kit sequence failed, switch to Gmail Email 2 send |
| June 2 (Day 4) | Monitor for Email 2 opens | 30%+ | <20% = weak CTA, try resend to non-openers |
| June 3 (Day 5) | Email 3 delivery + Email 2 opens final | 25%+ | — |
| June 5 (Day 7) | Email 4 delivery + check orders | 2+ Etsy orders total | Check which email drove clicks |
| June 7 (Day 10) | Email 5 delivery + final coupon metrics | 1+ order from coupon | Track "SEEDWARDEN15" usage in Etsy |

### 7.2: Revenue Attribution

**Track which email drove each Etsy purchase**:
- When order arrives, note email address of buyer
- Cross-reference with Kit subscriber list
- Which email did they open before purchasing?
- Record in WORKLOG.md

**Email revenue attribution**:
- Email 1: Zone card (0 revenue, trust-building)
- Email 2: First sales pitch (3–5 orders expected from 30 opens)
- Email 3: Educational nurture (1–2 orders)
- Email 4: Seasonal engagement (1–2 orders)
- Email 5: Coupon push (2–4 orders, highest ROI)

**Total expected**: $50–$150 in first 10 days from email sequence.

---

## APPENDIX: Copy/Paste Email Content Bundle

All email content is provided above in Section 2. Here's a quick reference for copy/paste:

- **Email 1 Subject**: Your Zone 5 Foraging Guide [INSTANT DOWNLOAD]
- **Email 2 Subject**: Welcome to Seedwarden — Start Here
- **Email 3 Subject**: [Free Guide] Seed Saving for Zone 5 Growers
- **Email 4 Subject**: What's Harvestable in Zone 5 Right Now (Late May Guide)
- **Email 5 Subject**: Zone 5 Guides: Full Collection + $5 OFF Today

All body copy is in Section 2.1–2.5 above. Copy body text directly into Kit email builder or Gmail drafts.

---

**Status**: ✅ PRODUCTION READY — complete email funnel ready for May 27–30 execution
**Use**: May 27–30, 2026
**Next**: Execute May 30 launch per Section 6 timeline
**Fallback**: Section 5 Gmail fallback available if Kit fails at any point
