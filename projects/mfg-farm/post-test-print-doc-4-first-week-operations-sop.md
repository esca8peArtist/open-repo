---
title: ModRun First-Week Operations SOP
date: 2026-05-05
status: pre-staging-ready
scope: Daily fulfillment procedures, QC checklist, customer communication, performance tracking
related: DAY1_LAUNCH_OPERATIONS_PLAYBOOK.md, etsy-shop-launch-kit.md
---

# ModRun First-Week Operations SOP (Standard Operating Procedure)

**Purpose**: Step-by-step guide for executing daily fulfillment tasks during the first week of sales. This is the "how to actually do the work" document after orders start coming in.

**Target user**: Solo operator (you) printing 1-5 clips per day, packing orders, managing customer communication

**Key outcome**: Every order ships within 3-5 business days of purchase with zero quality issues and every customer receives a thank-you message that builds repeat purchase likelihood.

---

## Phase 0: Pre-Launch Setup (Day Before First Sales)

### Workspace Preparation Checklist

- [ ] Printer tested and working (run a test print, confirm quality)
- [ ] Filament loaded and ready (verify spool is full, filament path clear)
- [ ] Slicer software (Bambu Studio) on computer with ModRun design files
- [ ] All design files (.stl) organized in a folder named `ModRun_STLs/` with variants clearly named
- [ ] Packaging materials purchased and staged:
  - [ ] Poly mailers (9x12", 2.5mil) — at least 20 units
  - [ ] Tissue paper or kraft paper for cushioning — a pad
  - [ ] USPS shipping labels (printed at home or pre-bought from Pirate Ship)
  - [ ] Packing tape, scissors, scale (for weighing packages)
- [ ] Shipping platform account set up and tested:
  - [ ] Pirate Ship account linked to Etsy store
  - [ ] Generated 1 test USPS label to verify format
  - [ ] Printed and tested: Label prints correctly on label stock or 4x6 label sheets
- [ ] Customer communication templates ready (copy-paste messages):
  - [ ] Order acknowledgment template (sent within 2 hours of order)
  - [ ] Shipping notification template (sent when dropping package at USPS)
  - [ ] Thank-you + review request template (sent 3 days after estimated delivery)
- [ ] QC checklist printed out or accessible on phone (see Section 2 below)
- [ ] Performance tracking spreadsheet created (see Section 7 below)

---

## Daily SOP: 5-Step Fulfillment Process

### STEP 1: PICKING (Morning — 5-10 minutes per order)

**When**: Check orders first thing every morning and at lunch

**Action**:
1. Log into Etsy
2. Check "Orders" tab for new orders since yesterday
3. For each new order:
   - [ ] Note order number and customer name
   - [ ] Note product SKU (e.g., "Single Clip — Black — PLA+")
   - [ ] Note variant (color, material)
   - [ ] Note quantity
   - [ ] Create a simple order list on paper or spreadsheet with today's date and order details
4. Verify you have all materials to fulfill:
   - [ ] Correct color filament available
   - [ ] Correct material (PLA+ or PETG) available
   - [ ] Packaging materials (mailer, label stock)
5. **Action**: Print out the order list (or screenshot it). This is your production checklist for the day.

**Example order list format**:
```
TODAY'S ORDERS (May 10):
Order #123456 — Jane Smith — Single Clip (Black, PLA+) — Ship by May 13
Order #123457 — Bob Jones — 3-Pack (Mix Colors, PLA+) — Ship by May 13
Order #123458 — Sarah Lee — Single Clip (Gray, PETG) — Ship by May 13
```

**Target**: Complete picking by 9 AM so you know what's in the queue for printing.

---

### STEP 2: PRINTING (Ongoing throughout the day — 20-60 min per order)

**When**: Start immediately after picking; can run parallel to other tasks

**Process**:
1. **Load filament**: 
   - Remove old spool (if needed)
   - Load correct color/material for today's first order
   - Run 2-inch extrusion test (extrude a little filament at 220°C to confirm color and consistency)
   - Trim extrusion and remove from nozzle

2. **Load design file into Bambu Studio**:
   - Open Bambu Studio
   - Load the ModRun design file (e.g., `modrun_clip_single.stl`)
   - Verify dimensions and orientation on the virtual build plate
   - **Check**: Does the part fit in the available bed space? (Usually yes; confirm)

3. **Slice with appropriate settings**:
   - **Layer height**: 0.20mm (standard; fast and acceptable for cable clips)
   - **Nozzle diameter**: 0.4mm
   - **Infill**: 20% (enough for strength, not overkill)
   - **Walls**: 3 (critical for structural integrity on snap-fit parts)
   - **Temperature**: 220-225°C (PLA+ range; PETG: 230-240°C)
   - **Build plate temp**: 60°C (PLA+); 70°C (PETG)
   - **Bed adhesive**: AABB (Bambu Lab proprietary, included)
   - **Support**: No supports needed for ModRun clip (design is support-free)
   - **Print speed**: Max 250mm/s (Bambu default is fine; this is fast enough)
   
4. **Review slice**:
   - Estimated print time appears (usually 15-25 minutes for a single clip)
   - Check the 3D preview: parts should be clearly separated, no overlaps, no unexpected gaps
   - **Red flags**: If anything looks wrong in preview, do not print. Reload file, re-slice, and re-check.

5. **Send to printer**:
   - Click "Send" to Bambu P1S
   - Confirm printer receives file (check Bambu Handy app)
   - Wait for print to start (usually within 30 seconds)
   - **Monitor first layer** (first 2-3 minutes): Watch via camera to confirm nozzle height is correct, part adhesion looks good
   - **Monitor final 10% of print** (last 2-3 minutes): Confirm part is releasing cleanly from bed, no peeling or warping

6. **Alert points** (things that might go wrong):
   - Nozzle too high: Layer lines widely spaced, part not sticking
   - Nozzle too low: Nozzle dragging on part, excessive layer squishing
   - Filament jam: Extrusion stops mid-print, filament path blocked
   - Bed adhesive contaminated: Part won't stick or slides around mid-print
   
   **If error occurs**: Pause print, diagnose (check nozzle height, clear any debris, reload filament), and resume. Total recovery usually <10 minutes.

7. **While printing**: Move to next order (if multiple orders queued). Load a second printer (if you have one) or prepare materials for the next part.

**Target**: Minimal supervision (< 5 minutes hands-on per print after loading). Bambu Handy app alerts you to problems.

---

### STEP 3: POST-PROCESSING (Afternoon/evening — 5-10 min per part)

**When**: Print completes; process immediately to clear build plate for next print

**Process**:
1. **Remove part from build plate**:
   - Wait for plate to cool to ~40°C (touch test; warm but not hot)
   - Use a spatula or plastic scraper to gently lift one corner
   - Part should pop off cleanly; if stuck, wait another minute and try again
   - **Caution**: Don't force it; forcing can warp the part or damage the PEI plate

2. **Remove support material** (if any):
   - ModRun parts are designed to be support-free
   - If supports were generated in error (shouldn't happen), carefully snap off at the support contact point
   - Sand the contact point smooth with 200-grit sandpaper (takes <30 seconds)

3. **Inspect part for defects**:
   - [ ] Part is the expected color and material (visual check)
   - [ ] No layer artifacts or visible defects on the snap-fit channel
   - [ ] Snap-fit arm feels firm and has proper flex (test manually: snap onto a cable, then pop off)
   - [ ] Dimensions look correct (compare to reference part or spec sheet)
   - [ ] No rough edges or burrs (run finger lightly along channels; should be smooth)
   - **If defect found**: Set aside, note defect type (see QC section below), reprint the part

4. **Optional light sanding** (if needed):
   - If layer lines are visible on the snap-fit engagement area, light sanding (200-grit) for <1 minute
   - Goal: Smooth finish on cable contact surfaces, not perfect aesthetic everywhere
   - **Typical result**: Light sanding on 1 of 20 parts (only if you're targeting premium quality)

5. **Weigh the part** (for shipping cost purposes):
   - Single clip: ~5-8g
   - 3-pack: ~15-20g
   - Note weight on your order tracking spreadsheet (you'll need this for shipping labels)

6. **Package immediately** (don't let finished parts pile up):
   - Proceed to Step 4 below

---

### STEP 4: PACKING (Evening before ship day — 10-15 min per order)

**When**: Once part is printed and QC'd, pack same day if possible (max next morning)

**Process**:
1. **Gather materials for this order**:
   - Finished clip(s)
   - Poly mailer (9x12")
   - Tissue paper or kraft paper
   - Packing slip (see template below)
   - USPS shipping label (to be printed later, or pre-printed if weight is known)

2. **Create packing slip**:
   
   **Packing Slip Template** (print or hand-write):
   ```
   ─────────────────────────────────
   Thank you for your order!
   
   ModRun Cable Management Clips
   Order #{{ORDER_NUMBER}}
   {{DATE}}
   ─────────────────────────────────
   
   WHAT YOU ORDERED:
   {{PRODUCT_DESCRIPTION}} (x{{QUANTITY}})
   Color: {{COLOR}}
   Material: {{MATERIAL}}
   
   HOW TO USE:
   1. Snap the clip onto your cable
   2. Mount to your desk, rail, or wall using M3 hardware
   3. Snap additional cables in as needed
   
   NEED HELP?
   Message me on Etsy or email {{YOUR_EMAIL}}
   Response time: Within 2 hours (9 AM–6 PM Central, M–F)
   
   YOUR FEEDBACK MATTERS:
   If you love it, please leave a review on Etsy!
   Reviews help other cable enthusiasts find ModRun.
   [Include Etsy review link if possible]
   
   Made with care in {{YOUR_LOCATION}}
   ─────────────────────────────────
   ```

3. **Place in mailer**:
   - Lay out tissue paper in mailer (cushioning)
   - Place clip(s) in center
   - Wrap tissue around clip(s) gently
   - Insert packing slip (folded, not loose)
   - Seal mailer with packing tape

4. **Weigh package**:
   - Place mailer + contents on scale
   - Note weight (needed for shipping label)
   - Typical weight: Single clip ~10g (total ~30g with mailer/slip); 3-pack ~80g (total ~110g)

5. **Label and photograph** (before dropping at USPS):
   - Take a quick photo of the package from above (for your records, useful if customer claims non-delivery)
   - Write order number on the photo (phone photo is fine)
   - Save to a folder "Orders Shipped" in your phone or computer

---

### STEP 5: SHIPPING (End of day — 10-15 min per order)

**When**: Once packages are packed, generate shipping label and drop at USPS same day (or next morning latest)

**Process**:
1. **Generate shipping label via Pirate Ship**:
   - Log into Pirate Ship
   - Click "Create Shipment"
   - Select USPS (not UPS/FedEx)
   - Select "First Class Package" (for single clips under 1 lb)
   - Enter destination address (pre-filled from Etsy order data)
   - Enter weight (what you weighed in Step 4)
   - Select "First Class" service (typical: 5-8 business days, ~$5.99)
   - Or select "Small Flat Rate Box" if available (fixed $8.45, guaranteed in that size box)
   - Review and purchase label
   - Print label (on 4x6 label stock if possible, or letter-size paper and tape to package)

2. **Attach label to package**:
   - Affix label to the top-right corner of mailer (standard position)
   - Ensure label is smooth and readable (scanner must read barcode)
   - No tape over barcode

3. **Drop at USPS**:
   - Location: Your nearest USPS collection box or post office
   - Time: Before 5 PM if possible (USPS processes same-day drops before 5 PM)
   - **Don't use home mailbox**: Take packages to USPS directly to guarantee same-day processing
   - Confirm: Keep the receipt or screenshot showing the label was purchased and transmitted

4. **Update Etsy**:
   - Return to Etsy order
   - Click "Print Label" or "Add Tracking"
   - Paste the USPS tracking number (found on Pirate Ship label or receipt)
   - Click "Mark as Shipped"
   - Etsy automatically sends customer an email with tracking number

5. **Customer notification**:
   - Within 1 hour of marking shipped on Etsy: Send customer a message via Etsy
   - Use template below
   - **Timing is important**: Shipping message should arrive while the customer is still thinking about their purchase (psychology: top-of-mind = more likely to review)

   **Shipping Notification Template**:
   ```
   🎉 Your ModRun order is on its way!
   
   Order #{{ORDER_NUMBER}}
   Tracking: {{TRACKING_NUMBER}} (USPS)
   Estimated delivery: {{ESTIMATED_DELIVERY_DATE}}
   
   Your package should arrive in 5–8 business days depending on your location
   and USPS volume.
   
   Click the tracking link in your email to follow along!
   
   Questions? Message me anytime. I'll respond within 2 hours.
   
   – {{YOUR_NAME}}, ModRun
   ```

---

## Summary: Daily Fulfillment Workflow (Timing Example)

**Timeline for 3 orders per day**:

```
09:00 AM — PICKING (5 min)
  Check Etsy orders, create production list for the day
  → 3 orders identified

09:15 AM — PRINTING (Order #1)
  Load filament (black PLA+)
  Slice design
  Send to printer
  Est. 20 minutes
  
09:35 AM — PRINTING (Order #2)
  While Order #1 prints, load Order #2 (gray PLA+) on second printer (if available)
  Or wait for Order #1 to complete
  
10:00 AM — POST-PROCESSING (Order #1)
  Print finished, remove part, inspect for defects, weigh it
  Quick QC: Part looks good ✓
  
10:15 AM — PACKING (Order #1)
  Pack Order #1 into mailer with packing slip
  Seal, ready for label
  
10:30 AM — PRINTING (Order #3)
  Load Order #3 filament (white PLA+)
  
11:00 AM — POST-PROCESSING (Order #2)
  Order #2 done, QC, weigh
  
11:15 AM — PACKING (Order #2)
  Pack Order #2
  
12:00 PM — LUNCH + MONITOR PRINTING
  Order #3 still printing
  
12:30 PM — POST-PROCESSING (Order #3)
  Order #3 done
  QC check
  
12:45 PM — PACKING (Order #3)
  Pack Order #3
  
1:00 PM — SHIPPING
  Weigh all 3 packages
  Log into Pirate Ship, generate 3 shipping labels
  Print labels
  
1:30 PM — DROP AT USPS
  Drive to USPS, drop 3 packages
  Confirm drop (receipt or photo)
  
2:00 PM — CUSTOMER NOTIFICATIONS
  Log into Etsy, mark all 3 orders as shipped
  Add tracking numbers
  Send shipping notification messages to customers
  
2:30 PM — DAILY LOG
  Update performance tracking spreadsheet with today's metrics
  Note any issues (defects, delays)

END OF DAY: All 3 orders processed, shipped, customers notified
```

**Total time for 3 orders**: ~5.5 hours (spread throughout the day, lots of idle time while printing)

---

## Section 2: Quality Control Checklist

**When**: After every print completes, before moving to next step

**Quick check** (< 1 minute, every part):

- [ ] Color correct? (Visual match to reference part)
- [ ] Material correct? (PLA+ smooth, matte; PETG slightly stiffer)
- [ ] Dimensions reasonable? (Not obviously oversized or undersized)
- [ ] Snap-fit arm present and intact? (Visual check; didn't break off during removal)
- [ ] No visible defects? (Cracks, layer separation, warping)

**Detailed check** (< 2 minutes, first 3 parts of each session):

- [ ] Snap fit test: Manually snap clip onto a cable, confirm it holds, pop off cleanly
- [ ] Channel smooth? (No sharp edges, no visible layer artifacts in the cable path)
- [ ] Tolerance correct? (Snap arm 1.4mm ± 0.05mm critical dimension; visual check is good enough for first week)
- [ ] No rough burrs? (Run finger along all edges; should feel smooth)

**Defect types** (if you find one, categorize and log):

| Defect Type | Description | Frequency Target |
|---|---|---|
| Layer line artifacts | Visible lines in snap-fit channel (cosmetic, not functional) | OK if <5% |
| Tolerance fail | Snap-fit too loose or too tight (functional) | REJECT — reprint |
| Warping | Part curves or twists (functional issue) | REJECT — reprint |
| Material issue | Wrong color, material cloudy (shipping issue) | REJECT — document and contact supplier |
| Adhesion failure | Part didn't stick to bed, peeled off mid-print (waste) | Log, adjust nozzle height, reprint |
| Support artifact | Bumpy surface where supports were (if supports used) | Sand smooth, acceptable if <2% |

**Action if defect found**:
1. Set part aside (mark as "defect — reprint")
2. Log defect type in spreadsheet (date, order, defect type)
3. Reprint the part immediately
4. If defect rate exceeds 5% in a single day, troubleshoot:
   - Check nozzle cleanliness (remove any plastic debris)
   - Check bed leveling (use Bambu calibration)
   - Check filament freshness (older filament can degrade)
   - Check slicer settings (verify infill and wall count)

---

## Section 3: Customer Communication Templates

**Goal**: Every customer receives at least 3 messages from you: order confirmation, shipping notification, thank-you + review request.

### Template 1: Order Confirmation (Send within 2 hours of order)

**When**: Customer places order on Etsy

**Message**:
```
Hi {{CUSTOMER_NAME}},

Thank you for your ModRun order! I'm excited to get your clip(s) printed
and shipped out.

YOUR ORDER:
Order #{{ORDER_NUMBER}}
Item: {{PRODUCT}} ({{COLOR}}, {{MATERIAL}})
Quantity: {{QTY}}

WHAT'S NEXT:
I print on-demand, so your order goes straight into the queue. I'll print,
quality-check, and ship within 3–5 business days. You'll receive a tracking
number via email as soon as it ships.

NEED SOMETHING DIFFERENT?
If you'd like a different color, custom configuration, or expedited shipping,
message me now. I can usually accommodate requests.

Thanks for supporting independent makers!

– {{YOUR_NAME}}
ModRun
```

---

### Template 2: Shipping Notification (Send within 1 hour of marking as shipped)

**When**: You've dropped the package at USPS and marked order as shipped on Etsy

**Message**:
```
🎉 Your ModRun order is on its way!

Order #{{ORDER_NUMBER}}
Tracking Number: {{TRACKING_NUMBER}}
Estimated Delivery: {{ESTIMATED_DELIVERY_DATE}}

Click your tracking number (in the email from USPS) to follow your package
in real-time.

SETUP TIPS:
Once it arrives:
1. Snap the clip onto your cable
2. Mount to your desk edge, rail, or wall (M3 hardware if Pro tier)
3. Add more cables as needed — the system is modular!

QUESTIONS?
Hit reply or message me anytime. I'm available 9 AM–6 PM Central, Monday–Friday.

Thanks for choosing ModRun!

– {{YOUR_NAME}}
```

---

### Template 3: Delivery Confirmation & Review Request (Send 3 days after estimated delivery)

**When**: Part of your daily routine; send to all orders shipped 3+ days ago that don't yet have reviews

**Message**:
```
Hi {{CUSTOMER_NAME}},

Got your ModRun clip(s)? 📦

I'm hoping your cable management setup is looking cleaner now. If you've
had a chance to use it, I'd love to hear your thoughts!

⭐ A quick review on Etsy really helps other cable enthusiasts find ModRun:
[Link to your Etsy product listing]

Reviews are what help new products get seen. Even a short one — "Works great!"
or "Exactly what I needed" — makes a difference.

FEEDBACK?
If something isn't working or you have suggestions, reply to this message.
I read every message and often incorporate feedback into new designs.

Thanks for supporting independent makers!

– {{YOUR_NAME}}
ModRun
```

---

### Template 4: Follow-Up (If Issue Reported)

**When**: Customer reports a problem (defective item, didn't arrive, etc.)

**Message**:
```
Hi {{CUSTOMER_NAME}},

I'm sorry to hear {{ISSUE: item arrived damaged / didn't arrive / doesn't fit}}.
That's not the experience I want for you.

HERE'S WHAT I'LL DO:
1. I'm sending a replacement [free of charge] immediately
   Tracking: {{NEW_TRACKING_NUMBER}}
   Expected arrival: {{NEW_ETA}}

2. [Optional] If you'd prefer a refund instead, just reply and let me know.
   I'll process it the same day.

NO NEED TO RETURN:
Keep the original item or recycle it. I'd rather you have a working clip
than deal with return shipping.

GOING FORWARD:
If this happens again, tell me immediately. I take quality seriously and
want to make sure you're happy.

Thanks for your patience!

– {{YOUR_NAME}}
ModRun
```

---

## Section 4: Performance Tracking Spreadsheet

**Purpose**: Daily log of production, sales, quality, and revenue. Use this to spot trends and make optimization decisions.

**Tools**: Google Sheets (easiest; shared syncing), Excel, or even a paper notebook

**Create these columns**:

| Date | Order # | Customer | Product | Material | Color | Status | Print Time | Defects | Weight | Shipped | Revenue | Notes |
|------|---------|----------|---------|----------|-------|--------|------------|---------|--------|---------|---------|-------|
| 5/10 | 123456 | Jane S | Single | PLA+ | Black | Shipped | 18 min | None | 30g | 5/10 | $7.99 | OK |
| 5/10 | 123457 | Bob J | 3-pack | PLA+ | Mix | Shipped | 54 min | 1 failed (reprinted) | 110g | 5/10 | $14.99 | Snap-fit test passed |
| 5/10 | 123458 | Sarah L | Single | PETG | Gray | Shipped | 22 min | None | 32g | 5/10 | $11.99 | Pro tier |

**Daily totals (calculate at end of each day)**:

```
DATE: {{DATE}}
Orders processed: {{N}} (target: 3-5)
Total units printed: {{N}} (target: 3-5)
Total revenue: ${{TOTAL}} (target: $25-50 for Week 1)
Total print time: {{HOURS}} (target: <4 hours active printing)
Defect rate: {{PERCENT}}% (target: <5%)
Feedback/issues: {{NUMBER}} (target: 0)
Action items for tomorrow:
- {{ACTION_1}}
- {{ACTION_2}}
```

---

## Section 5: Daily Performance Metrics & Decision Points

**Track these metrics every single day**:

### Metric 1: Order Fulfillment Time

**Target**: Order received → Shipped within 3 business days

**Calculate**: Date order placed vs. date shipped

**If exceeding 5 days**:
- You're printing too slowly or packing too slowly
- Speed up: Set a morning deadline for printing (9 AM) and shipping deadline (3 PM)

### Metric 2: Defect Rate

**Target**: <5% (i.e., 1 out of 20 prints needs to be reprinted)

**Calculate**: # of reprints ÷ # of total prints × 100

**If exceeding 5%**:
- Printer calibration issue (nozzle height, bed leveling)
- Filament issue (old or damp)
- Slicer settings issue (walls too thin, infill too low)
- Action: Run calibration on printer + do a test print

### Metric 3: Orders Per Day

**Target**: Week 1 = 1-2 orders/day; Week 2 = 2-3 orders/day

**Calculate**: Daily order count

**If <1/day**:
- Listings need optimization (photo swap, tag adjustment, or post to Reddit)
- Too many views but no sales = pricing or description issue
- Check Etsy Stats for view count; if views are low, do photo swap

### Metric 4: Customer Satisfaction (Early Indicator)

**Track**: Messages received, tone, frequency of questions

**If getting lots of questions**:
- Answer them quickly (within 2 hours) and add answers to FAQ section
- Questions = interested buyers; answer thoroughly

### Metric 5: Revenue Tracking

**Track**: Daily revenue, cumulative revenue, target vs. actual

**Week 1 target**: $25-50 total revenue (or 2-5 orders at $7-15 each)

**If below target**: This is normal. New listings take time to rank. By week 2, you should see pickup as you gather initial reviews.

---

## Section 6: Troubleshooting Guide (Quick Reference)

**Problem**: Print failed mid-way (nozzle jam, part fell off, etc.)

**Solution**: 
1. Pause printer
2. Wait 30 seconds, clear any debris from nozzle (if accessible)
3. Reload filament path (re-feed through extruder)
4. Resume print
5. If print fails again, cancel and reprint

**Likely cause**: Filament not feeding smoothly, nozzle debris, or bed adhesive issue

---

**Problem**: Part finished printing but won't pop off the bed

**Solution**:
1. Wait for bed to cool to 40-50°C (usually takes 5 minutes)
2. Use a plastic scraper (not metal) to gently pry one corner
3. If still stuck, wait 2 more minutes
4. Never force it (will warp part or damage PEI plate)

**Likely cause**: Bed too hot, bed adhesive too strong, or part warped during cooling

---

**Problem**: Snap-fit arm is too loose or too tight (defective)

**Solution**:
1. Measure snap-fit arm thickness (calipers if you have them, or visual estimate)
2. Check against spec (should be 1.4mm ± 0.05mm)
3. If loose: Print at higher infill (30% instead of 20%)
4. If tight: Use 0.3mm nozzle instead of 0.4mm for finer detail
5. Test print 1 more and verify before shipping

---

**Problem**: Customer reports clip doesn't fit their cable type

**Solution**:
1. Ask: "What's the cable diameter?" (measure with calipers or compare to reference)
2. ModRun works for 4-12mm diameter cables
3. If <4mm: Suggest a smaller model (can you design one?)
4. If >12mm: Suggest wrapping with electrical tape to reduce diameter, or custom size order
5. Offer refund if it truly doesn't work

---

## Section 7: End-of-Week Summary

**Every Friday**: Spend 30 minutes reviewing the week and planning next week.

**Checklist**:
- [ ] Total orders this week: {{N}}
- [ ] Total revenue this week: ${{AMOUNT}}
- [ ] Defect rate this week: {{PERCENT}}%
- [ ] Average fulfillment time: {{N}} days
- [ ] Customer satisfaction: Any issues? {{YES/NO}}
- [ ] Best-performing SKU: {{PRODUCT}}
- [ ] Worst-performing SKU: {{PRODUCT}}
- [ ] Etsy shop notes: {{INSIGHTS}}
- [ ] Printer performance: Any issues? {{NOTES}}

**Next week action items**:
- [ ] {{ACTION_1}}
- [ ] {{ACTION_2}}
- [ ] {{ACTION_3}}

---

## Final Reminders

1. **Speed over perfection**: Your first orders don't need to be perfect. They need to be on-time and functional. You can optimize quality later.

2. **Respond fast**: A message reply within 2 hours signals you're a professional. It also reduces anxiety-driven refund requests from customers.

3. **Over-communicate**: Customers love updates. It feels like you care and it prevents "where's my order" messages.

4. **Document everything**: Your spreadsheet is your business dashboard. It shows you where bottlenecks are and where to optimize.

5. **The first 10 orders set your trajectory**: Make sure those first 10 orders are perfect. Reviews compound. One 1-star review early can take weeks to recover from.

6. **Enjoy it**: You're shipping real products to real people who are happy to receive them. That's the whole point. Stress less, ship more.
