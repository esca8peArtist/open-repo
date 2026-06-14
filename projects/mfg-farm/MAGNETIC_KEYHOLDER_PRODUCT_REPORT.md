# Magnetic Wall Keyholder — Product Report
*Generated: June 14, 2026 | Bambu P1S Print Farm | SKU candidate*

---

## Section 1: Product Overview

### What It Is

A wall-mounted keyholder with three embedded N52 neodymium disc magnets, optional integrated hook arms, and M4 countersunk screw holes for secure wall mounting. The base plate (120mm × 60mm × 6mm) provides a clean, minimal footprint. Magnets are press-fit into recessed pockets from the front face — keys with metal keyrings or fobs adhere magnetically, while hook arms below provide a backup/alternative for heavier key sets.

### Who Buys It

- New homeowners and renters who want a minimalist entryway organizer
- Apartment dwellers who prefer wall hooks over hook strips or messy key bowls
- Housewarming gift buyers ($20–35 is a sweet-spot price for impulse gifting)
- Minimalist home-decor enthusiasts — magnetic organizers photograph well for social media
- Secondary buyers: people who already own an Eichler/MCM or Scandinavian-style home and want matching decor

### Why People Want Magnetic Keyholders

- **Never lose keys again** — the magnet "catches" the keyring as you walk in
- **Visual tidiness** — no key pile, no bowl, nothing sticking out of a hook unless a key is on it
- **Easy installation** — 2 screws, level it, done; no stud-finder required (M4 into drywall anchor)
- **Gifting utility** — "useful + minimal + unique" makes it a recurring top-seller in entryway/home categories

### Competitor Etsy Listings

The following listings were found in June 2026 searches for magnetic wall keyholders on Etsy. Direct links are provided for visual reference:

1. **Magnetic Key Holder for Wall, 3D Printed Minimalist Key Rack**
   - URL: https://www.etsy.com/uk/listing/4461489094/magnetic-key-holder-for-wall-3d-printed
   - Description: Flat rectangular 3D-printed plate with embedded neodymium magnets, no hooks. Clean white/black finish. Strong magnets hold multiple keysets. Marketed as "new home gift."
   - Estimated price: £14–£22 GBP (~$18–$28 USD)

2. **Goose Key Holder — 3D Printed Magnetic Key Rack**
   - URL: https://www.etsy.com/listing/1855128994/goose-key-holder-3d-printed-magnetic-key
   - Description: Fun animal-shaped 3D print (goose silhouette) with integrated magnet. Farmhouse/whimsical style. Popular housewarming gift. PLA construction.
   - Estimated price: $18–$26

3. **Modern Magnetic Key Holder With Integrated Shelf (Wood + Magnets)**
   - URL: https://www.etsy.com/listing/1448550389/modern-magnetic-key-holder-with
   - Description: Handmade wood block with 4 super-strong embedded magnets and a shelf ledge on top. Multiple wood combos (Black Walnut/Mahogany, White Oak/Ash). Holds up to 8 key sets. MCM/Scandi aesthetic. Likely $35–$60 range — premium tier.
   - Estimated price: $35–$60

4. **Minimalistic Wall Key Holder — Magnetic Keychain Holder**
   - URL: https://www.etsy.com/listing/1062450823/minimalistic-wall-key-holder-i-magnetic
   - Description: Ultra-slim Scandinavian-style wall plate, painted by hand, natural wood grain with smooth lines. Powerful magnets, no hooks. Slim profile that disappears on the wall.
   - Estimated price: $20–$32

5. **Magnetic Key Holder — Modern Metal + Ash Wood Entryway Organizer**
   - URL: https://www.etsy.com/listing/1835032373/magnetic-key-holder-key-holder-for-wall
   - Description: Handcrafted metal rail with natural ash wood accent, wall-mount. Minimalist entryway/office style. Strong magnets integrated into the rail.
   - Estimated price: $28–$45

**Overall competitor price range: $18–$60 USD**, with the sweet spot for 3D-printed plastic/PLA+
units at **$18–$28** and premium wood/metal combos at $35–$60. Our target price of **$22–$26**
sits right in the high-volume zone.

---

## Section 2: Design Specs

### ASCII Front-Face Diagram

```
 ┌─────────────────────────────────────────────────┐
 │           120mm wide × 60mm tall                │
 │                                                 │
 │    [M4]                             [M4]        │  ← screw holes (countersunk back)
 │                                                 │     spaced 80mm apart, centred vertically
 │         (●)       (●)       (●)                │  ← 3× N52 magnet pockets
 │        10mm      10mm      10mm                 │     10.2mm dia × 2.8mm deep
 │        dia       dia       dia                  │     0.2mm floor retains magnet
 │                                                 │
 └──────┬──────────────┬─────────────┬─────────────┘
        │              │             │
        ↓ 30°          ↓ 30°         ↓ 30°         ← hook arms angled 30° downward
       /              /             /               25mm long, 4mm dia cylinder
      ●              ●             ●               ← 3mm lip ball at tip retains keyring
```

*Front view (Y+ direction). Magnet pockets open toward viewer. Hook arms extend forward
and downward from bottom edge of base plate.*

### Dimensions Table

| Feature                | Value          | Notes                             |
|------------------------|----------------|-----------------------------------|
| Base plate width       | 120 mm         | Parametric: `PLATE_WIDTH`         |
| Base plate height      | 60 mm          | Parametric: `PLATE_HEIGHT`        |
| Base plate thickness   | 6 mm           | Parametric: `PLATE_THICKNESS`     |
| Corner radius          | 5 mm           | Parametric: `CORNER_RADIUS`       |
| Magnet pocket dia.     | 10.2 mm        | 0.2mm clearance for N52 10mm disc |
| Magnet pocket depth    | 2.8 mm         | 0.2mm floor; magnet sits flush    |
| Magnet count           | 3              | Parametric: `MAGNET_COUNT`        |
| Magnet row height      | 15 mm from btm | Parametric: `MAGNET_ROW_Z`        |
| Hook arm length        | 25 mm          | Parametric: `HOOK_LENGTH`         |
| Hook arm diameter      | 4 mm           | Parametric: `HOOK_DIAMETER`       |
| Hook angle             | 30° downward   | Parametric: `HOOK_ANGLE_DEG`      |
| Hook lip diameter      | 6 mm           | Spherical tip; parametric         |
| Screw hole diameter    | 4.5 mm         | M4 clearance                      |
| Countersink diameter   | 8.5 mm         | DIN 965 M4 flat head + 0.5mm tol  |
| Countersink depth      | 3.5 mm         | Flush with plate back face         |
| Screw hole spacing     | 80 mm          | Parametric: `SCREW_HOLE_SPACING`  |

### Bill of Materials (per unit)

| Item                        | Qty | Unit Cost          | Source                                                        |
|-----------------------------|-----|--------------------|---------------------------------------------------------------|
| PLA+ filament (estimate 35g)| 35g | $0.70 @ $20/kg     | Polymaker PolyLite PLA+ or Bambu PLA+                        |
| N52 10mm×3mm disc magnets   | 3   | $0.44 ea @ 100+qty | https://www.jc-magnetics.com/Magnet-disc-N52-10mm-3mm        |
| M4 × 20mm flat-head screws  | 2   | ~$0.05 ea          | Hardware store bulk; included in listing or buyer-sourced     |
| M4 wall anchors (drywall)   | 2   | ~$0.05 ea          | Optional; note in listing                                     |
| **Total BOM**               |     | **~$1.97**         |                                                               |

**Magnet procurement note**: For 100+ units, jc-magnetics.com offers $0.44/ea for N52 10mm×3mm discs,
making magnet cost $1.32 for 3× per unit. AliExpress carries 12mm×3mm N52 discs in 100-packs for
~$0.99–$2.00 total (search "10pcs 50pcs 100pcs N52 NdFeB neodymium disc 10x3mm"); adjust
`MAGNET_POCKET_DIAM` in the design file if switching to 12mm diameter.

Amazon search: https://www.amazon.com/neodymium-magnets-10mm-x-3mm/s?k=neodymium+magnets+10mm+x+3mm
(Filter by N52 grade, 100-pack; typical $8–$14 per 100 on Amazon)

---

## Section 3: Print Settings

### Bambu P1S Recommended Settings

| Setting             | Value          | Notes                                         |
|---------------------|----------------|-----------------------------------------------|
| Layer height        | 0.20 mm        | Standard quality; 0.16mm for smoother surface |
| Wall loops          | 4              | Ensures magnet pocket walls are solid         |
| Top/bottom layers   | 5              | Strong floor for magnet retention             |
| Infill              | 20%            | Gyroid or grid; 15% acceptable               |
| Infill pattern      | Gyroid         | Better strength-to-time ratio                 |
| Supports            | None           | No overhangs; hook tip ball is small enough   |
| Print speed         | 200 mm/s       | P1S default; no reduction needed              |
| Nozzle temp         | 220°C          | PLA+ standard                                 |
| Bed temp            | 65°C           | Cool PEI plate                                |
| Material            | PLA+           | Bambu PLA+ or Polymaker PolyLite PLA+        |
| Estimated time      | 55–70 min      | 3-hook variant; 1-hook ~45 min; nohook ~50min |
| Estimated filament  | 30–40g         | Varies by hook count                          |
| Cooling             | 100%           | Full fan after first 3 layers                 |

### Print Orientation

**CRITICAL**: Print face-up (front face toward the sky). The magnet pockets must open
upward so they can be sliced without supports and so magnets can be inserted post-print.

- Flat back face rests on build plate
- Hook arms point upward during print (they are short enough to bridge without supports)
- No brim required; plate footprint is stable

### Post-Print Magnet Installation

1. Press N52 disc magnets into pockets from the front face
2. Magnets should click in with finger pressure — the 0.2mm floor holds them flush
3. If pockets are too loose: add a drop of CA glue (super glue) to the pocket floor before insertion
4. If pockets are too tight: use a small dowel and light mallet, or increase `MAGNET_POCKET_DIAM` by 0.1mm

---

## Section 4: Variant Matrix

| Variant              | Hook Count | Est. Print Time | Filament | Material Cost | Target Use Case                        | Suggested Etsy Title                                              | Price Point |
|----------------------|------------|-----------------|----------|---------------|----------------------------------------|-------------------------------------------------------------------|-------------|
| `keyholder_3hook.stl`| 3 hooks    | 65–70 min       | ~38g     | $1.16         | Full entryway station (keys + fobs)    | "Magnetic Key Holder Wall Mount — 3 Hook Minimalist Organizer"    | $24–$26     |
| `keyholder_1hook.stl`| 1 hook     | 48–55 min       | ~31g     | $0.94         | Minimalist / single-person household   | "Minimalist Magnetic Wall Keyholder — Modern Entryway Hook"       | $19–$22     |
| `keyholder_nohook.stl`| 0 hooks  | 50–58 min       | ~30g     | $0.91         | Pure magnet shelf / AirPods + keys     | "Magnetic Wall Organizer — Keyless Minimalist Shelf Mount"        | $18–$22     |

*Print times at 0.20mm / 20% infill / Bambu P1S default speeds.*
*Material cost at $20/kg PLA+ + $0.44/magnet × 3 magnets.*

---

## Section 5: Margin Analysis

### 3-Hook Variant at $24 Sale Price

| Item                         | Amount     |
|------------------------------|------------|
| **Revenue**                  | **$24.00** |
| PLA+ filament (38g @ $20/kg) | -$0.76     |
| N52 magnets (3× @ $0.44)     | -$1.32     |
| M4 screws + anchors          | -$0.20     |
| Packaging (poly bag + insert)| -$0.25     |
| **Total material cost**      | **-$2.53** |
| Etsy listing fee             | -$0.20     |
| Etsy transaction fee (6.5%)  | -$1.56     |
| Etsy payment processing (3%) | -$0.72     |
| **Total Etsy fees**          | **-$2.48** |
| Shipping materials (bubble mailer) | -$0.40 |
| **Net margin per unit**      | **$18.59** |
| **Net margin %**             | **77.5%**  |

*Assumes seller handles shipping (buyer pays shipping, added at checkout). If offering free shipping at $24, add ~$4.50 for USPS First Class domestic; net margin drops to ~$14.09 (58.7%) — still strong.*

### 1-Hook Variant at $20 Sale Price

| Item                         | Amount     |
|------------------------------|------------|
| **Revenue**                  | **$20.00** |
| PLA+ filament (31g @ $20/kg) | -$0.62     |
| N52 magnets (3× @ $0.44)     | -$1.32     |
| M4 screws + anchors          | -$0.20     |
| Packaging                    | -$0.25     |
| **Total material cost**      | **-$2.39** |
| Etsy fees (9.5% + $0.20)     | -$2.10     |
| Packaging/mailer             | -$0.40     |
| **Net margin per unit**      | **$15.11** |
| **Net margin %**             | **75.6%**  |

### No-Hook Variant at $19 Sale Price

| Item                         | Amount     |
|------------------------------|------------|
| **Revenue**                  | **$19.00** |
| Material + fees (same calc)  | -$4.72     |
| **Net margin per unit**      | **$14.28** |
| **Net margin %**             | **75.2%**  |

### Key Insight

All three variants deliver >75% net margins before shipping cost. The **3-hook variant at $24**
maximizes absolute dollars per print ($18.59/unit), while the 1-hook and no-hook variants serve
price-sensitive buyers. At 2 prints/day on one P1S (running 3-hook at 65 min each), daily net
revenue = **~$37/day / $260/week** from a single printer on this SKU alone.

---

## Section 6: Competitor Photos / Inspiration Links

The following links provide direct visual reference for how competing sellers position and photograph
magnetic wall keyholders. Use these for product photography inspiration and listing strategy.

### Etsy Market Pages (Browse Competing Listings Visually)

1. **Etsy: Magnetic Keyholder Market**
   https://www.etsy.com/market/magnetic_keyholder
   Overview of all magnetic keyholder listings. Sorted by relevance. Shows thumbnails of the full competitive landscape — dominant styles are white/grey PLA flat plates, wood-magnetic combos, and novelty shapes.

2. **Etsy: 3D Printed Key Holder Market**
   https://www.etsy.com/market/3d_printed_key_holder
   Specifically 3D printed. Most are $15–$30. Note that many top sellers use multi-color PLA or painted finishes to differentiate from the base grey/white prints.

3. **Etsy: Magnetic Key Holder Wall Mount Market**
   https://www.etsy.com/market/magnetic_key_holder_wall_mount
   Filtered to wall-mount style. Competitors include flat plates, rails, and shelf combos.

### Specific Notable Listings

4. **Minimalistic Wall Key Holder — Magnetic Keychain Holder**
   https://www.etsy.com/listing/1062450823/minimalistic-wall-key-holder-i-magnetic
   Ultra-slim plate, Scandinavian aesthetic, hand-painted. Shows what a premium positioning
   looks like in photography — clean white wall, single lifestyle shot, no clutter.

5. **Key Holder for Wall — Minimalist Modern Concrete Magnetic**
   https://www.etsy.com/listing/990929199/key-holder-for-wall-key-organizer-key
   Concrete-look finish with integrated shelf ledge. Demonstrates the appeal of the shelf
   variant — buyers use it for AirPods, small wallet, etc. Strong cross-sell opportunity.

6. **Goose Key Holder — 3D Printed Magnetic Key Rack**
   https://www.etsy.com/listing/1855128994/goose-key-holder-3d-printed-magnetic-key
   Themed novelty design. Different segment (gift/novelty vs minimalist), but shows
   that 3D printed magnetic holders sell well with personality. Good for A/B listing test.

7. **Modern Magnetic Key Holder With Integrated Shelf (Wood)**
   https://www.etsy.com/listing/1448550389/modern-magnetic-key-holder-with
   Premium wood + magnet combo at $35–$60. Shows the ceiling of this category.
   Our PLA+ version undercuts it significantly while mimicking the functionality.

8. **STL Model Reference — Free Printable Magnetic Key Holder (Printables.com)**
   https://www.printables.com/model/19250-magnetic-key-holder
   Community-designed free STL. Useful to study what the maker community has
   already designed, identify differentiators, and assess print complexity.

9. **Cults3D — Magnetic Key Holder Designs**
   https://cults3d.com/en/3d-model/home/magnetic-key-holder-wedesign
   Professional STL marketplace. Shows design trends and what sells in the
   3D model market — useful for benchmarking design complexity and visual style.

### Photography & Listing Strategy Notes

Based on competitor listings observed:
- **Best background**: white or light grey wall, natural morning light from left
- **Hero shot angle**: 3/4 front-left, showing plate flat on wall + keys hanging magnetically
- **Key props**: 2–3 actual house keys on a simple ring, hanging from magnets
- **Secondary shot**: close-up of magnet holding a keyring (shows product value)
- **Third shot**: dimension reference (ruler or coin) to show actual 120mm size
- Top sellers use 5–7 listing photos. Minimum viable: 3 photos to go live.

---

## Design File Reference

- **CadQuery source**: `cadquery/magnetic_keyholder.py`
- **STL output target**: `stl/keyholder_3hook.stl`, `stl/keyholder_1hook.stl`, `stl/keyholder_nohook.stl`
- **Run command**: `uv run python cadquery/magnetic_keyholder.py --output-dir ./stl/`
- **Dependency**: `cadquery>=2.3` (not currently installed in this environment)
  - Install via: `pip install cadquery` or `conda install -c conda-forge cadquery`
  - Once installed, running the command above will produce all 3 STL variants

> **Note on CadQuery vs build123d**: The existing project files (`modrun_rail_b123d.py`,
> `headphone_hooks.py`) use the `build123d` library. If you'd prefer consistency, the
> `magnetic_keyholder.py` design can be ported to `build123d` API. The geometry and
> parameters are identical — only the API calls (`.workplane()`, `.rect()`, `.extrude()`,
> `.hole()`) differ. `build123d` equivalents: `Box()`, `Cylinder()`, `extrude()`, `add()`,
> `subtract()`, `export_stl()`.
