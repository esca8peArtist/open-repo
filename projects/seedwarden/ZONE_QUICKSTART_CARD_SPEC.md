---
title: "Zone Quick-Start Card — Content Specification"
date: 2026-04-28
status: ready-for-production
deliverable-type: Canva/PDF design brief
references: email-automation-blueprint.md, zone-seed-starting-calendar.md, email-and-launch-plan.md
---

# Zone Quick-Start Card — Content Specification

**Purpose**: This document is the production brief for the Zone Quick-Start Card, Seedwarden's Phase 2 lead magnet. It is written for a Canva template builder or graphic designer. It specifies layout, per-zone content, design elements, copy direction, personalization logic, and email integration. The final deliverable is a single-page printable PDF (or 2-page maximum) published in zone-specific variants or as a single interactive document with tabbed sections.

**Context**: The email-automation-blueprint.md identifies this card as the recommended Phase 2 lead magnet upgrade over the existing "5 Heirloom Varieties for Small Spaces" guide. The rationale documented there: zone-specific personalization drives higher completion rates (people read content calibrated to their climate, not generic advice) and higher perceived value. This spec operationalizes that recommendation into a buildable document.

---

## Part 1: Conversion Rationale

### Why This Lead Magnet Outperforms Generic Guides

The existing Seedwarden lead magnet (5-variety guide) is well-written and deployable immediately. The Zone Quick-Start Card replaces it — or supplements it as a second lead magnet — because of a single principle: **personal relevance is the fastest path to perceived value**.

Research on email personalization consistently shows that personalized content reduces unsubscribe rates. The mechanism is straightforward: a subscriber in Minnesota who downloads a guide and immediately sees "Zone 4 — Last frost: May 5–May 25" experiences confirmation that the content was made for their situation. A subscriber in Houston who sees "Zone 9 — Last frost: February 18" receives the same confirmation. A generic guide gives neither subscriber that moment.

Specific conversion implications documented in email-automation-blueprint.md:
- Cold traffic (TikTok/Instagram bio clicks) converts at 15–25% to email sign-ups when the landing page is specific and the lead magnet is genuinely useful.
- Warm traffic (existing Etsy buyers clicking through from PDF end-pages) converts at 25–40%.
- A zone-personalized card increases the "genuinely useful" threshold because the content is immediately actionable — a subscriber can look at the card and know what they should be doing in their garden this month.

The card also creates a natural bridge to the Zone-by-Zone Seed Starting Calendar ($7 individual zone, $18 bundle), which is the logical paid next step for any subscriber who finds value in the free card.

---

## Part 2: Format and Delivery

### Format Decision: Interactive Canva Link Over Static PDF

**Recommendation: Publish as a set of individual zone-specific PDFs** (one per major zone grouping: 3, 4, 5, 6, 7, 8, 9, 10), not as a single multi-zone PDF. Rationale:

- A subscriber receiving "Zone 5b Quick-Start Card" as a PDF download experiences immediate personalization at the file level — they open one clean page about their zone, not a document they have to navigate.
- Individual zone PDFs are easier to update. If frost dates shift or crop recommendations change, updating Zone 5 does not require rebuilding the full document.
- File size stays well under 2MB per card.
- Email delivery: Kit (ConvertKit) can serve different download links based on a tag or form field. A subscriber who selects "Zone 5" on the sign-up form receives the Zone 5 PDF link. This is achievable without paid automation — see Part 6.

**File specs per card:**
- Dimensions: 8.5 x 11 inches (US Letter, landscape or portrait — see layout below)
- Resolution: 300 DPI for print quality
- File format: PDF, exported from Canva
- File size target: Under 1.5MB
- Color mode: RGB (screen-optimized; subscriber prints at home)
- Bleed: None required (home printing)

**How many variants to build:**
Build one card per major zone: Zones 3, 4, 5, 6, 7, 8, 9, 10. Zones 1–2 cover Alaska and subarctic regions with extremely limited Etsy market relevance; skip for launch. Zones 11–13 (tropical) are similarly a small market segment; skip for launch. Add them in Phase 3 if subscriber data shows demand.

Total variants at launch: **8 cards** (Zones 3 through 10).

For zones with meaningful a/b differences (e.g., Zone 7a vs. Zone 7b, or Zone 5a vs. Zone 5b), the card text can note the subzone range without requiring separate files. Example: "Zone 5 — Last frost April 15 to May 10 depending on your subzone (5a or 5b). Check planthardiness.ars.usda.gov for your exact location."

---

## Part 3: Layout Structure

### Page Layout (Portrait, 8.5 x 11 inches)

The card uses a three-column structure inside a single page. The following is a zone-by-zone breakdown of content that goes into each block. First, the structural template:

```
+----------------------------------------------------------+
|  SEEDWARDEN LOGO     |  ZONE QUICK-START CARD            |
|  [botanical icon]    |  Zone [X] — [Region Name]         |
|                      |  [Zone color band]                 |
+----------------------------------------------------------+
|                                                          |
|  COLUMN 1 (35%)      |  COLUMN 2 (35%)  |  COL 3 (30%)  |
|                      |                  |                |
|  FROST DATES &       |  QUICK-START     |  STORAGE &     |
|  SEASON AT A         |  CROPS THIS      |  PRESERVATION  |
|  GLANCE              |  SEASON          |  TIPS          |
|                      |                  |                |
|  [calendar icon]     |  [seed icon]     |  [jar icon]    |
|  Last frost:         |  1. Crop name    |  Tip 1         |
|  [date range]        |  2. Crop name    |  Tip 2         |
|  First frost:        |  3. Crop name    |  Tip 3         |
|  [date range]        |                  |                |
|  Season: X days      |  This month in   |                |
|                      |  your zone:      |                |
|  [thermometer icon]  |  [brief note]    |                |
|  THIS MONTH:         |                  |                |
|  [2-3 seasonal       |                  |                |
|  tasks, April 2026]  |                  |                |
|                      |                  |                |
+----------------------------------------------------------+
|                                                          |
|  HEIRLOOM VARIETY SPOTLIGHT (full width, bottom third)  |
|  [seed packet icon] 2-3 recommended varieties for        |
|  this zone, with one-line notes on each                  |
|                                                          |
+----------------------------------------------------------+
|  FOOTER: Get the full Zone [X] calendar — Etsy link     |
|  Free guide: seedwarden.com/zone | Unsubscribe           |
+----------------------------------------------------------+
```

### Design Hierarchy Rules for Canva Builder

1. **Zone color band**: A 12px horizontal rule immediately below the header, color-coded by zone temperature (cool zones: blue-green; temperate zones: green; warm zones: amber; hot zones: terracotta). See color spec in Part 4.

2. **Zone number**: The zone number is the largest typographic element on the page. Size: 72pt minimum. This serves as immediate visual confirmation — subscriber glances at card and sees their zone prominently.

3. **Column headers**: 14pt, all-caps, primary brand color (forest green). Icon sits above each header.

4. **Body text**: 10pt, dark charcoal (not full black — softer on print). Line height 1.4.

5. **Variety spotlight section**: Visually separated from the three columns by a full-width background band in parchment/cream. This section should feel like a bonus, not a continuation of the table above.

6. **Footer**: 8pt, muted — functional, not decorative.

---

## Part 4: Brand and Design Specification

### Color Palette (Concept 1 "The Keeper" from logo-concepts.md)

The card should use the primary recommended logo concept color palette:

| Element | Color | Hex |
|---------|-------|-----|
| Primary brand (headers, borders) | Deep forest green | #2D5016 |
| Background (page) | Warm cream / off-white | #F5EDD6 |
| Accent (icons, CTA, zone number) | Burnt sienna | #A0522D |
| Body text | Dark charcoal | #2C2C2C |
| Variety spotlight band | Slightly darker cream | #EDE0C4 |
| Footer text | Medium warm grey | #7A7060 |

**Zone color band by temperature zone:**

| Zones | Band Color | Hex | Why |
|-------|-----------|-----|-----|
| 3–4 | Cool slate blue | #3D6B8A | Communicates cold/short season |
| 5–6 | Forest green | #2D5016 | Primary brand color; temperate seasons |
| 7–8 | Warm amber | #C9943A | Warm-season emphasis |
| 9–10 | Terracotta | #A0522D | Hot, nearly frost-free |

### Typography

| Element | Font | Size | Style |
|---------|------|------|-------|
| Wordmark "SEEDWARDEN" | Playfair Display or similar sturdy serif | 16pt | Small caps |
| Zone number | Playfair Display | 72pt | Bold |
| Zone name/region | Playfair Display | 18pt | Italic |
| Column headers | Montserrat or similar geometric sans | 11pt | All caps, tracked +50 |
| Body text | Montserrat Light or similar | 10pt | Regular |
| Variety names | Montserrat | 10pt | Italic (species names) |
| Footer | Montserrat Light | 8pt | Regular |

Both Playfair Display and Montserrat are available free on Google Fonts and in Canva's free font library.

### Icon Set

Use a consistent botanical/kitchen icon set throughout. Recommended Canva search terms:
- Calendar icon: "botanical calendar outline"
- Thermometer: "thermometer minimal outline"
- Seed packet: "seed envelope outline" or "seed packet minimal"
- Mason jar / storage: "mason jar outline" or "canning jar line"
- Seedling/plant: "seedling sprout outline"

All icons should be line-style (not filled), in the primary forest green (#2D5016) or burnt sienna (#A0522D) accent color. Size: 24px inside column headers. Do not use emoji — use consistent vector icon style throughout.

---

## Part 5: Per-Zone Content Tables

The following tables provide the content for each of the eight zone cards. Content is calibrated to April 2026 (current month), so the "This Month" tasks reflect what growers in each zone should actually be doing right now. When the card is refreshed for a subsequent season, update the "This Month" block only — frost dates and variety spotlights remain stable.

Content source: zone-seed-starting-calendar.md (Seedwarden's own product, already zone-verified and crop-specific).

---

### Zone 3 Card Content

**Region line**: Northern Plains, Mountain Interior, Upper Great Lakes

**Frost dates block:**
- Last frost: May 15 – June 1
- First frost: September 5 – September 20
- Growing season: 95–125 days
- Example cities: International Falls MN (May 21 / Sept 14), Bismarck ND (May 14 / Sept 22)

**This Month — April 2026 Tasks:**
1. Start cucumbers, squash, melons, and pumpkins indoors now (3–4 weeks before last frost). Do not skip — Zone 3's short season means these crops need the head start.
2. Direct sow peas, spinach, and radishes as soon as soil is workable. These crops tolerate frost and should go in the ground even if snow is still possible.
3. Finish pepper and eggplant seedlings under lights — they were started in February and need another 4–6 weeks before outdoor temperatures allow transplanting.

**Quick-Start Crops:**
1. Bush beans (Provider OP) — direct sow after last frost, 55-day crop, reliable in short seasons.
2. Kale (Lacinato H) — cold-hardy, harvest from June through first hard freeze, frost improves flavor.
3. Stupice tomato (OP) — 52-65 day short-season variety, the standard Zone 3 tomato, produces before frost.

**Storage/Preservation Tips:**
- Zone 3's short harvest window means batch-processing is essential. Learn lacto-fermentation for greens: no canning equipment needed, 20-minute hands-on time per batch.
- Root cellar storage (or equivalent — a cool basement corner, 35–40 F) extends beet, carrot, and potato harvest into spring.
- Freeze or dehydrate beans in July when harvest peaks suddenly — Zone 3 bush beans all ripen within 2 weeks.

**Variety Spotlight:**
- Stupice tomato: Czech heirloom, 52–65 days. The tomato that actually ripens in Zone 3. Small red fruits, reliable producer. Save seed year after year.
- Waltham 29 broccoli (H): 74-day compact heads, handles Zone 3 cold, plant in March for June harvest.
- Golden Bantam sweet corn (H): 75 days, the historic American heirloom corn — grows in Zone 3 in the warmest microsites. Direct sow after last frost.

---

### Zone 4 Card Content

**Region line**: Upper Midwest, Northern New England, Mountain Valleys

**Frost dates block:**
- Last frost: May 5 – May 25
- First frost: September 15 – October 5
- Growing season: 120–150 days
- Example cities: Minneapolis MN (May 5 / Oct 4), Burlington VT (May 10 / Oct 1), Madison WI (May 5 / Oct 3)

**This Month — April 2026 Tasks:**
1. Direct sow cool-season crops now (peas, spinach, lettuce, arugula, radishes, turnips) — soil is workable in April, and these crops need 4–6 weeks before summer heat.
2. Start cucumbers, squash, pumpkins, melons, and watermelons indoors in late April (3–4 weeks before last frost in mid-May).
3. Plant onion sets and seed potatoes as soon as soil is workable — both can handle light frost once in the ground.

**Quick-Start Crops:**
1. Brandywine tomato (H) — 80 days, full Zone 4 season available. More variety options than Zone 3; this is the tomato worth growing in Zone 4.
2. Sugar snap peas (OP) — direct sow April, harvest by June, done before summer heat. Highest reward-to-effort ratio in Zone 4 spring.
3. Detroit Dark Red beet (H) — direct sow mid-April, harvest July through October, stores for months in a cool space.

**Storage/Preservation Tips:**
- Zone 4's brief canning season (August–September) calls for canning supplies ready before harvest, not purchased during peak season when stores run short.
- Dehydrate herbs (dill, basil, parsley) at harvest peak in July — Zone 4 herbs bolt quickly; dehydrating takes 20 minutes of prep and preserves the season for 12 months.
- Root cellar or garage storage: beets, carrots, potatoes, and winter squash store 4–6 months at 35–45 F. Harvest before hard freeze, cure squash in a warm space for 2 weeks first.

**Variety Spotlight:**
- Brandywine tomato (H): The benchmark heirloom, 80 days, full Zone 4 season. Pink beefsteak, rich flavor. Worth every day of the growing season.
- Long Island Improved Brussels sprouts (H): 90 days — Zone 4's long enough for it. Frost improves flavor; harvest into October.
- Scarlet Nantes carrot (H): Direct sow April, reliable germinator in Zone 4 soil, 65 days. The heirloom carrot standard.

---

### Zone 5 Card Content

**Region line**: Central Corridor, Southern New England, Mid-Elevation West

**Frost dates block:**
- Last frost: April 15 – May 10
- First frost: October 1 – October 20
- Growing season: 150–180 days
- Example cities: Denver CO (May 5 / Oct 6), Des Moines IA (Apr 24 / Oct 10), Boston MA suburbs (Apr 26 / Oct 16)

**This Month — April 2026 Tasks:**
1. Transplant broccoli, cauliflower, cabbage, kale, and onion starts outdoors now (mid-April) — they are frost-tolerant and need to get established before heat arrives.
2. Direct sow beets, carrots, and succession lettuce through April — these are your spring harvests.
3. Start cucumbers, squash, pumpkins, and melons indoors in late April (3–4 weeks before your last frost date). Do not start these too early — cucurbits resent root disturbance and should be transplanted within 3–4 weeks of germination.

**Quick-Start Crops:**
1. Dragon Tongue bush bean (H) — direct sow after last frost, 57 days, no staking, high yield, excellent container performer. The easiest bean in Zone 5.
2. Mortgage Lifter tomato (H) — 80 days, large beefsteak, forgiving for beginners, full Zone 5 season with time to spare.
3. Lemon cucumber (H) — 65 days, compact vine, prolific, less bitter than slicing types, great for containers and small spaces.

**Storage/Preservation Tips:**
- Zone 5 gets two natural preservation windows: early summer (peas, greens — blanch and freeze) and late summer (tomatoes, peppers, beans — can, ferment, or dehydrate).
- Tomato sauce is the highest-value Zone 5 preservation project. A day of canning in August can produce 18–24 quarts — 6 months of pasta sauce.
- Hot sauce fermentation is low-effort and uses peppers that ripen just before frost. Ferment 2–3 weeks, then refrigerate — no canning needed.

**Variety Spotlight:**
- Mortgage Lifter tomato (H): 80 days, bred by M.C. Byles of West Virginia specifically for home gardeners. Exceptionally large, sweet pink beefsteak. Seed-saveable, true to type, a Zone 5 staple.
- Dragon Tongue bean (H): Yellow with purple streaks, 57 days, no staking. The variety that converts non-bean-growers.
- Chioggia beet (H): 55 days, candy-stripe interior, dual-purpose (root + greens), grows in 12 inches of soil. Ideal for Zone 5 raised beds and containers.

---

### Zone 6 Card Content

**Region line**: Mid-Atlantic, Ohio Valley, Central Transition Zone

**Frost dates block:**
- Last frost: April 5 – April 25
- First frost: October 10 – November 1
- Growing season: 170–200 days
- Example cities: St. Louis MO (Apr 10 / Oct 18), Philadelphia PA (Apr 10 / Oct 24), Kansas City MO (Apr 9 / Oct 22)

**This Month — April 2026 Tasks:**
1. Tomatoes, peppers, and eggplants can go out in the ground by late April after a proper 7–10 day hardening off period — your last frost is early April in most of Zone 6.
2. Direct sow beans and corn after mid-April (soil temperature above 60 F) — Zone 6 is warm enough now.
3. Plant potatoes (if not done in March) and succession-sow lettuce, radishes, and arugula for a second spring round before summer heat.

**Quick-Start Crops:**
1. Cherokee Purple tomato (H) — 72–80 days, the signature heirloom for Zone 6's long summer. Rich, complex flavor; starts in March, harvests July through October.
2. Rattlesnake pole bean (H) — direct sow after mid-April, 65–70 days, drought-tolerant (important in Zone 6 summers), distinctive purple-streaked pods.
3. Okra — Clemson Spineless (H) — Zone 6 is warm enough for productive okra. Direct sow after mid-April, harvest July–October.

**Storage/Preservation Tips:**
- Zone 6 gardeners can run two full preservation seasons: early (peas, spring brassicas in June) and main (tomatoes, peppers, beans, corn in August–September).
- Tomato canning is the anchor. Zone 6's long tomato season (July–October) means enough volume to can, ferment into hot sauce, and still dry some for winter.
- Fermented pickles (cucumbers, green beans) are a low-equipment preservation option that peaks in Zone 6's July harvest window.

**Variety Spotlight:**
- Cherokee Purple tomato (H): 72–80 days, deeply flavored dark red-purple beefsteak with green shoulders. One of the most widely grown heirlooms in Zone 6–7 for good reason.
- Rattlesnake pole bean (H): Named for its markings. Drought-tolerant, a virtue in Zone 6 summers. 65–70 days, continuous producer if picked regularly.
- Wando pea (OP): The heat-tolerant pea — direct sow in late March or April and it will keep producing into Zone 6's early summer heat when other peas quit.

---

### Zone 7 Card Content

**Region line**: Piedmont South, Oklahoma, North Texas, Maritime Northwest

**Frost dates block:**
- Last frost: March 22 – April 15
- First frost: October 20 – November 10
- Growing season: 190–225 days
- Example cities: Raleigh NC (Apr 6 / Oct 28), Oklahoma City OK (Apr 1 / Nov 3), Seattle WA inland (Mar 24 / Nov 11)

**This Month — April 2026 Tasks:**
1. Tomatoes, peppers, and eggplants are already in the ground or going in now — last frost is behind most of Zone 7 by early April. Transplant after hardening off 7–10 days.
2. Direct sow beans, corn, cucumber, squash, zucchini, and okra throughout April — Zone 7 is warm enough for all of them now.
3. Harvest cool-season crops before they bolt in Zone 7's spring heat — peas, lettuce, spinach, broccoli, and cauliflower finish by late May. Pick now at peak.

**Quick-Start Crops:**
1. Okra — Clemson Spineless (H) or Hill Country Red (OP) — Zone 7 is the sweet spot for okra. Direct sow April, harvest June through October, high success rate even for new growers.
2. Sweet potato — Beauregard (OP) — plant slips after soil reaches 65 F (late April Zone 7b). Harvest October. Stores for months. One of the most productive edible crops per square foot in Zone 7.
3. Amish Paste tomato (H) — 85 days, large paste type, exceptional for sauce, heat-tolerant enough for Zone 7's summer.

**Storage/Preservation Tips:**
- Zone 7's main preservation window is July–October: sweet potatoes, tomatoes, peppers, okra, and beans.
- Okra freezes better than it cans — blanch 3 minutes, freeze on a sheet pan, then bag. Maintains texture better than jars.
- Sweet potato curing (10 days at 85–90 F, then 55–60 F storage) extends shelf life from weeks to 6–12 months. This is a 10-day passive process that dramatically multiplies your harvest value.

**Variety Spotlight:**
- Amish Paste tomato (H): 85 days, large meaty paste type, developed in Amish communities and adapted to Southeastern heat. Superior sauce tomato for Zone 7.
- Clemson Spineless okra (H): The 1939 All-America Selections winner and still the standard. Productive, spineless for easy harvesting, 56 days.
- Beauregard sweet potato (OP): 90 days, copper skin, orange flesh. The most reliable sweet potato for Zone 7 home gardeners. Plant slips, not seeds.

---

### Zone 8 Card Content

**Region line**: Deep South, Coastal Pacific Northwest, Central Texas

**Frost dates block:**
- Last frost: March 5 – March 25
- First frost: November 1 – November 25
- Growing season: 225–265 days
- Example cities: Portland OR (Mar 15 / Nov 7), Dallas TX (Mar 14 / Nov 17), Atlanta GA (Mar 21 / Nov 13)

**This Month — April 2026 Tasks:**
1. Tomatoes, peppers, eggplants, and all warm-season crops are established or in the ground — last frost passed in March. April is full growing season in Zone 8.
2. Plant sweet potato slips now (soil above 65 F) — this is the primary warm-season staple for Zone 8 South. Plant okra and southern peas for summer.
3. Harvest spring crops (lettuce, broccoli, cauliflower, peas) before they bolt in April's rising heat. Succession sow beans and corn for summer harvest.

**Quick-Start Crops:**
1. Homestead tomato (OP) — 80 days, heat-tolerant, disease-resistant, bred for the South. Reliable where heirlooms sometimes struggle in Zone 8's heat and humidity.
2. Clemson Spineless okra (H) — zone staple. Direct sow March–April, harvest June–November. Thrives in Zone 8 heat where other crops fail.
3. Seminole pumpkin (H) — the heat-and-humidity-tolerant heirloom squash bred by the Seminole people of Florida. Resists vine borers, stores for a year without refrigeration.

**Storage/Preservation Tips:**
- Zone 8's summer is hot and humid — fermented vegetables are more reliable than you might expect, because active fermentation cultures out-compete spoilage bacteria. Kimchi, fermented green beans (dilly beans), and hot sauce are all well-suited.
- Sweet potato curing and long storage is the highest-ROI preservation project in Zone 8. One 4×8 ft bed can produce 50–80 lbs. Cured and stored at 55–60 F, they last 8–12 months.
- Dehydration shines in Zone 8: hot peppers, okra, and tomatoes all dehydrate well and reduce to compact shelf-stable storage.

**Variety Spotlight:**
- Homestead tomato (OP): The tomato bred for Southern conditions. 80 days, globe-shaped, disease-resistant. Not the most complex flavor, but reliably productive where Brandywine fails in July humidity.
- Seminole pumpkin (H): The historically grown squash of the Southeast. Pest-resistant, stores 12 months without refrigeration, grows as a sprawling vine that needs space. Culturally significant and practically superior.
- Rattlesnake watermelon (H): 90 days, 25–40 lbs, thrives in Zone 8 heat and humidity. A Southern heirloom worth growing for its own history.

---

### Zone 9 Card Content

**Region line**: Gulf Coast, Southern Texas, Central Florida, SoCal Inland

**Frost dates block:**
- Last frost: February 10 – March 5
- First frost: November 20 – December 15
- Growing season: 260–300 days
- Example cities: Houston TX (Feb 18 / Dec 5), Jacksonville FL (Feb 21 / Dec 3), Sacramento CA (Feb 24 / Nov 26)

**This Month — April 2026 Tasks:**
1. Your spring garden is in full production — tomatoes, peppers, beans, cucumbers, and squash are growing now. Harvest cucumbers and squash frequently to maximize yield before summer heat peaks.
2. The cool-season window has closed: lettuce, spinach, peas, and broccoli are done or finishing. Remove spent plants now, do not let them bolt and use up soil.
3. Begin planning your summer survival strategy: okra, southern peas, and sweet potatoes are the summer workhorses. Get okra seeds in the ground now if not already done.

**Quick-Start Crops:**
1. Okra — Cow Horn (H) or Clemson Spineless (H) — the Zone 9 summer crop. Sow April, harvest June–November. High success, minimal care, productive in Zone 9's heat.
2. Heat Wave II tomato (OP) or Solar Fire (OP) — standard Zone 9 heirlooms/OP selections bred for heat-set. Tomatoes that set fruit at high temperatures when standard varieties drop their blossoms.
3. California Blackeye cowpea (OP) — Southern pea for Zone 9's summer. Direct sow April through June, nitrogen-fixing cover crop that also produces edible beans.

**Storage/Preservation Tips:**
- Zone 9's two preservation windows: spring (February–April, before heat) and fall (October–December, after heat). Plan canning sessions around these, not around August.
- Tomatoes: Process spring tomatoes in April–May before the crop is finished. Fall tomatoes ripen October–November for a second canning session.
- Freeze Zone 9's spring crop for later processing — if canning during April heat is impractical, freeze crushed tomatoes and process in October when the kitchen is bearable.

**Variety Spotlight:**
- Tropic tomato (OP): Bred at the University of Florida specifically for tropical and subtropical heat. 72 days, disease-resistant, heat-set. The workhorse Zone 9 tomato.
- Cow Horn okra (H): Longer pods (8–12 inches), classic Southern heirloom, prolific in Zone 9's heat. Harvest when pods are 4–6 inches for best texture.
- Zipper Cream cowpea (OP): Named for the easy-to-shell pod. Rich, creamy texture. One of the most popular Southern peas for Zone 9 home gardeners.

---

### Zone 10 Card Content

**Region line**: South Florida, Coastal Southern California, Hawaii

**Frost dates block:**
- Last frost: January 31 or earlier; many areas frost-free year-round
- First frost: December 15 or later; many areas frost-free
- Growing season: 300–365 days (essentially year-round)
- Example cities: Miami FL (frost-free), San Diego CA (Jan 29 / Dec 15), Honolulu HI (frost-free)

**This Month — April 2026 Tasks:**
1. Cool-season crops are done or finishing fast — lettuce, spinach, peas, broccoli, and cauliflower bolt in April's Zone 10 heat. Harvest everything remaining now and clear the beds.
2. Okra, southern peas, sweet potatoes, and heat-tolerant crops are the priority. Succession-sow okra through April for a staggered harvest.
3. Start planning your July–August strategy: Zone 10 open gardens enter the hot/rainy season (Florida) or dry season (SoCal) in summer. This is the time to mulch heavily, solarize empty beds, and start fall crops indoors in late July.

**Quick-Start Crops:**
1. Everglades tomato (H) — the cherry tomato native to South Florida, essentially perennial in Zone 10. Small, prolific, disease-resistant, heat-set. Self-sows. The only tomato that thrives in Zone 10 summer heat year after year.
2. Seminole pumpkin (H) — native to Florida, bred for Zone 10 conditions. Resists vine borers, stores 12 months, sprawling vine that produces reliably through Zone 10 heat.
3. Malabar spinach (OP) — not true spinach, but the vine vegetable that fills the spinach role in Zone 10's summer. Heat-loving, productive, and extremely easy to grow as a trellis plant.

**Storage/Preservation Tips:**
- Zone 10's cool-season window (October–April) is the primary preservation season — process spring tomatoes, citrus, and root vegetables while temperatures allow comfortable kitchen work.
- Tropical fruit preservation (Florida: avocado, mango, guava; SoCal: citrus, figs, avocado) is the Zone 10-specific preservation opportunity that most guides overlook. Dehydrated mango and fig preserves are high-value, long-shelf-life products.
- Fermented hot sauce is ideal for Zone 10's prolific hot pepper harvest — minimal equipment, no canning required, and Zone 10's warm temperatures accelerate lacto-fermentation.

**Variety Spotlight:**
- Everglades cherry tomato (H): Native Florida heirloom. Produces prolifically through conditions that kill standard tomatoes. Self-sows. Small fruits (marble-sized), intensely sweet. The one tomato worth growing in Zone 10 summer.
- Seminole pumpkin (H): The historically significant Florida heirloom. Pest-resistant, stores 12 months without refrigeration, heat-adapted.
- Datil pepper (H): St. Augustine, Florida's locally famous hot pepper. Similar heat to habanero, fruitier flavor. The defining Zone 10 (Florida) hot pepper for sauces and ferments.

---

## Part 6: Email Personalization Strategy

### How Zone Selection Works in Kit (ConvertKit)

The personalization mechanism does not require paid automation or Zapier. Here is the implementation path:

**Option A — Form field (simplest, recommended at launch):**
1. Add a dropdown field to the Kit sign-up form: "What's your USDA zone?" with options Zone 3 through Zone 10.
2. Use a different download link per zone in the automated welcome Email 1. In Kit, this requires setting up 8 conditional blocks within a single email, or building 8 separate automations (one per zone tag applied by form submission).
3. The email subject and body remain identical across all zones. Only the PDF download link changes.

Implementation time: 2–3 hours including building the form, uploading 8 PDFs to Google Drive, and setting up the conditional automation in Kit.

**Option B — Post-signup survey (for growers uncertain of their zone):**
Add a link in Email 1: "Not sure of your zone? Enter your zip code at planthardiness.ars.usda.gov — it takes 30 seconds." This reduces the friction of the zone selection step without requiring the subscriber to know their zone before signing up. Follow up with a single-question email (Day 1, same day): "Quick question — what's your USDA zone? I'll send you the right Quick-Start Card." Reply-based zone identification lets you manually tag and send the correct PDF.

**Option B is recommended at launch** if the 8-automation setup in Kit feels complex. It adds one manual step per subscriber but allows a simpler form (no dropdown, lower friction) and gives you a reply — which is a strong inbox deliverability signal.

### Email Welcome Sequence Integration

The Zone Quick-Start Card replaces the "5 Heirloom Varieties" guide as the Email 1 attachment. The email copy in email-and-launch-plan.md remains otherwise unchanged. The key edit to Email 1:

Change this line:
> "Your Seedwarden Starter Pack is attached below."

To this:
> "Your Zone [X] Quick-Start Card is below — it covers your frost dates, what to grow this month, and three heirloom varieties that actually thrive in your climate."

The zone number is populated dynamically if using Kit's liquid tags, or manually if using Option B above.

**Where the card is promoted** (per email-automation-blueprint.md):
1. TikTok/Instagram bio link during non-product-feature weeks
2. Pinterest: dedicated pin linking to the Kit landing page (use zone interest as the hook: "Free Zone 5 garden quick-start card — find out what to plant this month")
3. End-page of every Etsy PDF product: "Get your free Zone Quick-Start Card: [landing page URL]"
4. Reddit: used organically in r/vegetablegardening and r/homesteading when answering zone-specific questions

---

## Part 7: Landing Page Copy

The Kit landing page for the Zone Quick-Start Card needs a zone-selection step. Recommended copy:

**Headline:**
> Your Free Zone Quick-Start Card

**Subheadline:**
> Find out your frost dates, what to plant this month, and which heirloom varieties work best in your climate. One page. Actually useful.

**Body (under 80 words):**
> Most gardening advice ignores where you live. Your Zone 5 last frost is 6 weeks later than Zone 7. That matters when you're deciding whether to start tomatoes indoors today or wait another month.
>
> Enter your email below, select your USDA zone, and I'll send you a one-page quick-start card tailored to your zone's calendar.

**Form fields:**
- First name
- Email
- Zone (dropdown: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10, I'm not sure)

**CTA button:**
> Send me my Zone Quick-Start Card

**Below form (small text):**
> Not sure of your zone? [Check at USDA.gov] — it takes 30 seconds.
> You'll also receive a short series of emails on heirloom seeds and food growing. Unsubscribe anytime.

---

## Part 8: Production Checklist for Canva Builder

Use this checklist to confirm the card is production-ready before uploading to Google Drive and Kit.

### Per-Zone Card Checklist

- [ ] Zone number is the largest typographic element (72pt minimum)
- [ ] Region name is correct and matches zone-seed-starting-calendar.md
- [ ] Frost dates are accurate for the zone (verify against the city reference table in zone-seed-starting-calendar.md)
- [ ] "This Month" tasks are dated/written for the current month (update this block seasonally)
- [ ] Three quick-start crops listed with variety names and one-line descriptions
- [ ] Three storage/preservation tips are zone-appropriate (not generic)
- [ ] Variety spotlight section includes 2–3 varieties with species-level detail
- [ ] Footer includes Etsy link to Zone-by-Zone Seed Starting Calendar ($7 / $18 bundle)
- [ ] Footer includes Kit landing page URL
- [ ] Logo and wordmark present in header
- [ ] Zone color band correct for zone temperature range (see Part 4 color table)
- [ ] All icons are line-style, consistent set, same accent color
- [ ] Body text is 10pt minimum — legible at print scale
- [ ] PDF exported at 300 DPI
- [ ] File size under 1.5MB
- [ ] File named: `seedwarden-zone-[X]-quickstart-card.pdf`
- [ ] Uploaded to Google Drive with "Anyone with link can view" sharing
- [ ] Drive link tested (downloads correctly from incognito window)
- [ ] Drive link entered into Kit automation for correct zone tag

### Global Quality Check

- [ ] 8 zone cards total: Zones 3 through 10
- [ ] All 8 card links entered into Kit form automation
- [ ] Kit sign-up form includes zone dropdown
- [ ] Email 1 copy updated to reference "Zone Quick-Start Card" (not "5 Heirloom Varieties")
- [ ] Landing page live and tested with form submission
- [ ] At least one test submission completed for each zone (confirm correct PDF received)

---

## Part 9: Seasonal Refresh Protocol

The "This Month" block on each card contains time-sensitive content. All other content (frost dates, variety spotlight, storage tips) is stable and does not need seasonal updates.

**Refresh cadence**: Update the "This Month" block at the start of each month. This is a 30-minute Canva edit across all 8 cards — open each, change 3 bullet points, re-export PDF, re-upload to Google Drive (the sharing link does not change when you update a Google Drive file).

**Who does the update**: This is a 30-minute operator task once per month. It does not require the Canva designer to return. The template should be built so that the "This Month" text block is the only element that changes.

**January refresh note**: The January block is the highest-value update of the year — this is when Zone 3–6 subscribers are planning their entire season. Ensure the January card is updated by January 1.

---

*Prepared: 2026-04-28. References: projects/seedwarden/marketing/email-automation-blueprint.md (lead magnet strategy and email integration), projects/seedwarden/products/zone-seed-starting-calendar.md (per-zone crop and frost date data), projects/seedwarden/marketing/email-and-launch-plan.md (Kit setup and welcome sequence copy), projects/seedwarden/logo-concepts.md (brand color palette).*
