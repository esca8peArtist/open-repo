---
title: "Tools, Metalworking, and Blacksmithing: Complete Guide to Forging, Fabrication, and Tool Maintenance"
domain: "tools-metalworking-blacksmithing"
section: "tools-metalworking-blacksmithing-complete-guide"
content_type: "procedure"
difficulty: "beginner-to-advanced"
estimated_read_time: "85 minutes"
author: "Open-Repo Project"
last_updated: "2026-07-08"
version: "1.0"
license: "CC-BY-4.0"
wave: "4"
domain_number: "2"
tags:
  - blacksmithing
  - metalworking
  - tool-making
  - tool-repair
  - forging
  - heat-treatment
  - hand-tools
  - machine-tools
  - fabrication
  - sharpening
  - homesteading
  - resilience
  - community-production
  - appropriate-technology
description: >
  A comprehensive procedural guide to producing, repairing, and maintaining
  the metal tools that every other resilience discipline depends on: forge
  construction and fuel selection, anvil and hand-tool selection, steel
  identification and sourcing from scrap, fundamental forging techniques,
  heat treatment (annealing, hardening, tempering), worked examples for
  making and repairing common hand tools (chisels, hoes, axes, tongs),
  sharpening and maintenance, hand-powered machine tools (treadle lathes,
  hand-crank drills), and community-scale forge/co-op models. Specifications
  sourced from the FAO Agricultural Engineering training-manual series,
  ABANA (Artist-Blacksmith's Association of North America) curricula,
  metallurgical references, and craft-guild/makerspace documentation.
confidence: "82%"
confidence_notes: >
  Core forging technique, tool lists, and heat-treatment fundamentals are
  cross-sourced from ≥2 independent sources, including a full FAO
  Agricultural Engineering Service technical training manual (J.B. Stokes,
  *Advanced Blacksmithing*, FAO, 1992) written specifically for low-resource,
  scrap-material, non-electrified smithing — this is the strongest single
  source in the guide and its farm-tool worked examples (axe, chisel, hoe
  tang) are used directly (confidence 88% for forging/heat-treatment
  fundamentals). Steel identification via spark testing is explicitly
  flagged in its own sourcing as imprecise and requiring practice — treated
  here as a screening method, not a definitive alloy identification method
  (confidence ~70% for spark-test reliability specifically). Zone 5 fuel
  sourcing (coal availability, hardwood charcoal, propane) is grounded in
  regional-market generalizations rather than a Zone-5-specific land-grant
  study, because blacksmithing is a craft trade rather than an agricultural
  extension topic — no university extension service runs a "blacksmithing"
  program comparable to their wool or maple-syrup programs, so extension
  citations are absent from this guide by design, not oversight. Cost
  figures are 2026 USD retail/hobbyist pricing from multiple current
  vendor and hobbyist-budget sources and will vary regionally and with
  used/scrap sourcing. Machine-tool section (treadle lathe, mechanical
  advantage) draws on historical/appropriate-technology sources (Open
  Source Ecology, VITA Village Technology Handbook lineage) with lower
  source density (75% confidence) since these are niche revival crafts
  without contemporary institutional documentation. Overall confidence 82%.
date_sourced: "2026-07-08"
related_guides:
  - "wave-4-textile-clothing-systems/textile-clothing-systems-complete-guide.md"
  - "wave-2-natural-building/natural-building-techniques.md"
  - "wave-3-energy-systems/energy-systems-complete-guide.md"
  - "wave-3-food-production-expanded/food-production-expanded-complete-guide.md"
  - "wave-3-security-defense/security-defense-complete-guide.md"
---

# Tools, Metalworking, and Blacksmithing: Complete Guide to Forging, Fabrication, and Tool Maintenance

**License**: This guide is published under [CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/). You are free to share and adapt it with attribution to the Open-Repo Project.

**Relationship to other Waves**: Every other guide in this project quietly assumes tools exist — a hoe to till soil, shears to shear a sheep, a needle to sew cloth, a knife to prepare food, a saw to frame a wall. This guide is about the capability that makes all of those assumptions keep being true after the hardware store is no longer reliably open: the ability to forge, repair, and sharpen the metal tools that every other domain depends on. It pairs directly with the Wave 4 Textile and Clothing Systems guide (needles, shears, spindle-whorls), the Wave 2 Natural Building guide (nails, hinges, froes, draw-knives), the Wave 3 Energy Systems guide (fittings, brackets), and the Wave 3 Food Production guide (hoes, mattocks, pruning tools).

---

## Overview

Tool-making is the resilience discipline that sits underneath all the others. A household can store seed, learn herbal medicine, and stockpile fabric, but if a hoe blade snaps, a knife loses its edge past the point of resharpening, or an axe head comes loose from its haft, every other skill in the household's repertoire becomes harder to practice. Manufactured tools are themselves the product of a globally concentrated industrial supply chain — forged and cast overseas, shipped, warehoused, and retailed through a chain with many single points of failure. Blacksmithing and metalworking are the capabilities that let a household or small community close that loop locally: take damaged, worn-out, or raw scrap metal and turn it back into working tools.

**What this guide covers**: the complete metal-tool production and maintenance chain —

1. **Forge construction and fuel** — building a working solid-fuel or gas forge and choosing a fuel source
2. **The anvil and essential hand tools** — what to buy, what to improvise, what to make yourself
3. **Steel identification and sourcing** — reading scrap metal, spark testing, and understanding what steel is for what job
4. **Fundamental forging techniques** — drawing out, upsetting, bending, punching, cutting, and welding
5. **Heat treatment** — annealing, hardening, and tempering so tools hold an edge and don't shatter
6. **Making and repairing tools** — worked examples for chisels, hoes, axes, tongs, and handles
7. **Sharpening and maintenance** — keeping edges working between forge sessions
8. **Machine tools beyond the forge** — hand- and treadle-powered lathes, drills, and grinders, and the mechanical-advantage principles behind building your own
9. **Safety** — burns, eyes, lungs, and fire are the four hazard categories that matter most
10. **Community-scale production** — shared-forge and co-op models that make this capability affordable at neighborhood scale

**Who should read this**: anyone building household or community resilience who wants a working understanding of metal tool production and repair without assuming prior smithing experience. It is equally useful for someone starting with a $150 brake-drum forge in a driveway and for a community organizing a shared workshop.

**Scale assumption**: household to small-community scale (1 person to a shared neighborhood shop serving 10–30 households). Costs are 2026 USD. **Climate/region reference: Zone 5 (Upper Midwest / Great Lakes US)** is used for fuel-sourcing and material-availability notes; blacksmithing technique itself is not climate-dependent, but *where* you get coal, charcoal wood, and scrap steel is regional.

**A critical honesty note on this domain**: Blacksmithing is a craft trade, not an agricultural science — there is no land-grant university extension office that publishes "Blacksmithing for the Upper Midwest" the way there is for wool processing or maple syrup. The strongest technical backbone available for this guide is the United Nations Food and Agriculture Organization's own training-manual series for low-resource, scrap-material blacksmithing (written for smallholder farmers in the developing world, where the same "no reliable supply chain" logic applies), cross-checked against the modern ABANA hobbyist/craft curriculum and metallurgical references. This guide is explicit about that sourcing mix rather than implying a level of institutional-extension backing that does not exist for this craft.

---

## Part 1: Setting Up a Forge

### 1.1 What a Forge Actually Does

A forge is not an oven — its job is to deliver concentrated, controllable heat to a small area of a workpiece using a fuel bed *plus a forced air blast*. Simply piling fuel on top of metal is ineffective: heat escapes through the fuel mass and produces mounds of ash without reaching forging temperature. The two things every forge design must get right are (1) enough fuel depth and confinement to hold heat, and (2) a controllable air blast aimed at the base of that fuel bed. [Source: FAO Agricultural Services Bulletin, J.B. Stokes, *Advanced Blacksmithing: A Training Manual*, 1992, Appendix I]

### 1.2 Fuel Choices

| Fuel | Heat output | Learning curve | Cost (2026 USD) | Zone 5 sourcing notes |
|---|---|---|---|---|
| Coal/coke | Highest — reaches forge-welding heat most reliably | Moderate — fire management takes practice | Regionally variable; cheapest near coal-producing regions | Most U.S. coal is mined in the East/Appalachia and the West; Upper Midwest buyers typically order from a blacksmith-supply distributor rather than a local coal seam, raising delivered cost |
| Charcoal (hardwood) | Nearly as good as coke; low-density fuel means more volume burned per session | Low-moderate | Can be self-produced from hardwood in a simple retort/pit, or purchased | Zone 5 hardwoods (oak, maple, hickory, ash) make excellent smithing charcoal; softwood charcoal is much harder to get to forging temperature and is not recommended |
| Propane | High, very controllable, "instant on" | Lowest — easiest fuel for a total beginner | Forge unit ~$250–450 new; fuel ~$20–35 per 40 lb tank, consumed roughly one tank per intensive session | Propane is universally available in Zone 5 through the same suppliers used for grills and rural heating |

[Sources: FAO Agricultural Services Bulletin, *Advanced Blacksmithing*, Appendix I; HubPages, *Basic Blacksmithing: Is Coal, Charcoal, or Propane Best for Forge Fuel*; Small Farmer's Journal, *Choosing a Gas or Coal Forge for the Small Farm Shop*]

**Practical fuel guidance for a resilience context**: propane is the easiest fuel to learn on but represents an ongoing consumable dependency on a purchased, delivered product — exactly the kind of supply-chain dependency this guide is trying to reduce. Coal is the historically standard blacksmithing fuel and, once a supply is laid in, burns hot and predictable, but is not locally produced in most of Zone 5. **Self-produced hardwood charcoal is the most locally resilient long-term fuel option** for a Zone 5 household with woodlot access, even though it requires more fuel volume per session and more fire-tending skill than coal or propane. A realistic strategy is to learn on propane, build skill, and transition toward charcoal or laid-in coal for long-term independence.

### 1.3 Minimum-Viable Forge (Under $50 in Scrap)

A functional forge does not require a purchased forge unit. A widely used, well-documented beginner build uses a **brake drum** (a free or near-free scrapyard item) as the fire pot, mounted on a simple steel or welded-pipe stand, with a hand-crank blower, shop-vac on low, or repurposed hair dryer supplying air through a pipe (the **tuyere**) entering the bottom or side of the drum. An efficient solid-fuel forge can be built for well under $50 using scrap materials, excluding the air source. [Sources: The Crucible, *Blacksmithing Forge 101: How To Make Forges At Home*; RECOIL OFFGRID, *Learn How To Build Your Own Forge*; Instructables, *Mobile Coal Forge Build*]

**Basic brake-drum forge build**:
1. Mount the brake drum, open side up, on a waist-height stand (a metal drum, welded pipe legs, or a stack of concrete blocks all work).
2. Cut or drill a hole in the center/side of the drum for the tuyere pipe (typically 1–1.5 in / 25–40 mm steel pipe).
3. Fit a simple gate or damper at the tuyere so air blast can be controlled — full blast is rarely wanted; usually you want a moderate, steady flow.
4. Line the drum bottom with a shallow bed of sand, ash, or fire clay around the tuyere opening to protect the drum metal and shape the fire.
5. Build the fire on top: kindling, then fuel, packed and confined rather than piled loosely.

**Fire depth**: FAO's field guidance recommends a fire confined to a depression **100–140 mm (4–5.5 in) deep**, with sufficient fuel always maintained between the air blast and the workpiece — small jobs can use a shallower fire, larger stock needs more depth. [Source: FAO, *Advanced Blacksmithing*, Appendix I]

### 1.4 Air Supply Options

| Air source | Cost (2026 USD) | Notes |
|---|---|---|
| Hand-crank blower (cast-iron, geared) | $50–150 used, $150–300 new | Traditional pre-electric standard; a series of gears steps up fan-wheel rotation per crank turn; blower case diameter of roughly 10+ in (250+ mm) is needed for adequate volume — smaller units are often too weak for real smithing work | 
| Box/double-chamber bellows | Self-buildable from wood and leather, or $200+ commercial | Historic standard before cast-iron blowers; two air-tight chambers give more constant flow than a single bellows |
| Shop vac (reversed to blow) or hair dryer | $0–30 (repurposed) | Common budget beginner solution; less controllable than a purpose-built blower but fully functional |
| Electric squirrel-cage blower with damper | $50–100 | Requires grid or generator power — a dependency to weigh against the no-power options above |

[Sources: Air Control Industries, *The Evolution of the Blacksmith Forge Fan*; Centaur Forge, *Hand Crank & Electric Blacksmith Forge Blowers*; The Crucible, *Blacksmithing Forge 101*]

**Resilience note**: a hand-crank blower or box bellows is the only air-supply option on this list with zero electricity or fuel dependency beyond human effort, and is therefore the most resilient long-term choice even though it costs more up front than a repurposed hair dryer.

### 1.5 Location and Ventilation

Set the forge up outdoors or in a very well-ventilated space — never in an enclosed garage or basement without dedicated exhaust. Combustion of coal or propane produces carbon monoxide, an odorless and potentially fatal gas that accumulates without active air exchange; proper ventilation requires a system that actively pulls contaminated air out and brings fresh air in, not just an open window. A driveway, open-sided lean-to, or dedicated fire pit area away from fences, structures, and low tree limbs is the standard recommendation. [Source: Breakthrough Blacksmithing, *Forge Ahead Safely: Essential Precautions for Blacksmithing in the Workshop*]

---

## Part 2: The Anvil and Essential Hand Tools

### 2.1 Choosing an Anvil

The **London pattern anvil** — flat face, single round horn, square heel, hardy hole (square, for holding bottom tools), and pritchel hole (round, for punching through) — is the standard general-purpose choice for most hobbyist and homestead smiths. [Source: Orchard Blacksmith, *Choosing the Right Anvil: Types, Sizes, and What to Look For*]

**Weight guidance**:
- 55 lb (25 kg) is a reasonable absolute floor.
- **70–110 lb (32–50 kg) is the practical sweet spot for a starter anvil** doing hand-tool-scale work.
- 100 lb+ is recommended if the budget allows, since light stock work (hooks, small hardware, hand tools) is genuinely comfortable on a 70 lb anvil, but a smith doing any heavier farm-tool or axe-scale work will quickly find a sub-70 lb anvil frustratingly light — the anvil needs enough mass to absorb hammer energy rather than bounce.

**Hardness**: a good-quality anvil face has a hardness of at least 53 HRC (Rockwell C scale) with 70%+ rebound — a simple field test is dropping a ball bearing from 10 in (25 cm) onto the face and checking that it rebounds at least 7–9 in (70–90%). Low rebound indicates a soft face that will dent and deform under sustained use. [Source: Orchard Blacksmith, *Choosing the Right Anvil*; Anvilfire.com, *Selecting an Anvil*]

**Cost (2026 USD)**: small used anvils (50–70 lb) run $150–350; medium (100–150 lb) up to $700; new cast-steel anvils are more consistent in quality than old, pitted scrapyard finds but cost more. [Source: Begin To Black Smith, *How Much Does It Cost to Begin Blacksmithing*]

**No-anvil alternatives**: a section of railroad rail (a genuinely usable improvised anvil for smaller work, widely used by beginner and hobbyist smiths), a large sledgehammer head set face-up in a stump, or a heavy steel block from a scrapyard can all substitute for a true anvil while a household is building capital toward a proper one. None match the horn, hardy hole, and pritchel hole functionality of a London-pattern anvil, but all provide the essential flat, hard striking surface.

### 2.2 Hammers

| Hammer type | Weight | Use |
|---|---|---|
| Cross-peen hammer | 2–3 lb (0.9–1.4 kg) for a beginner; a common recommendation is ~2 lb to start | General-purpose forging; the peen (narrow end) is used for aggressively lengthening/drawing out stock |
| Ball-peen hammer | Similar range | Riveting, texturing, spreading rivet heads; less ideal than cross-peen for general drawing-out work |
| Rounding hammer | Similar range | Versatile modern hobbyist standard; rounded face reduces hammer marks |
| Sledgehammer (striking, two-person work) | 4–6 kg (9–13 lb), double-faced, full-length wooden handle | Heavy stock work, typically wielded by a second person ("striker") while the smith holds tongs and directs blows with a hand hammer |

[Sources: Working the Flame, *Best Types of Blacksmith Hammers*; Gallivanting Craftsman, *No Bullshit Guide To The Top 10 Blacksmithing Hammers*; FAO, *Advanced Blacksmithing*, Appendix II]

A beginner needs exactly one good hammer to start: a 2–3 lb cross-peen or rounding hammer is the standard first purchase, at roughly $30–80 new. [Source: Begin To Black Smith, *How Much Does It Cost to Begin Blacksmithing*]

### 2.3 Tongs

Tongs are the tool that lets a smith hold hot metal without touching it. Common jaw shapes include **wolf-jaw** (general flat/square stock), **v-bit** (round stock), and **flat-bit** (flat stock, precise grip). A beginner set of 2–3 pairs typically costs $60–120; many experienced smiths eventually forge their own tongs once they have enough skill, since tongs are themselves a classic intermediate forging project (bootstrapping — using your first tongs to help make better ones). [Sources: Hackaday, *Blacksmithing For The Uninitiated: Hammer And Tongs*; Begin To Black Smith, *How Much Does It Cost to Begin Blacksmithing*]

### 2.4 The Rest of the Essential Tool Kit

Based on the FAO recommended tool-and-equipment list for a working rural smithy (Appendix II), a reasonably complete kit beyond the forge, anvil, hammer, and tongs includes:

- **Slack tub / bosh**: a water tank holding at least 100 L (26 gal), for cooling tools and quenching some work
- **Top and bottom fullers**: grooved tools (8, 10, 12, 16, 20, 25 mm sizes useful) for spreading and shaping metal in a controlled direction, rather than all directions as a flat hammer face does
- **Top and bottom swages**: half-round-grooved tool pairs, same size range, for rounding stock
- **Set hammer**: a 25–30 mm square-faced hammer-like tool for reaching into corners and tight spots a hand hammer can't
- **Flatter**: a roughly 50×50 mm flat-faced tool struck with a second hammer, used to smooth and finish forged surfaces
- **Hardy** (bottom tool that fits the anvil's square hardy hole) and **hot set** (a chisel-like cutting tool) for cutting hot metal
- **Floor mandrel**: a tapered cast-iron cone roughly 1–1.5 m tall, for shaping rings and curved work
- **Heavy-duty leg vise**: for cold work-holding
- **Files** (flat, square, round, half-round), a **folding steel rule** (~600 mm), a **blacksmith's square**, and **calipers** (~150 mm) for layout and measurement
- **Hand-powered drilling machine** and **hand- or foot-powered grinding machine** (150–200 mm wheels) for rural/off-grid settings without electricity
- **Set of taps and dies** (6–16 mm) for cutting screw threads by hand

[Source: FAO, *Advanced Blacksmithing*, Appendix II — "Recommended Tools and Equipment"]

This list is deliberately built around **making your own tools as you go** — many of the items above (fullers, swages, set hammer, flatter, hardy) are themselves classic early forging projects, meaning a new smith's tool kit grows through practice rather than purchase alone.

---

## Part 3: Steel — Identification and Sourcing

### 3.1 Why Steel Type Matters

Not all steel behaves the same way in the fire or under heat treatment. Mild (low-carbon) steel forges easily but cannot be hardened to hold a cutting edge — it is the right choice for brackets, hooks, tongs, and structural fittings. Higher-carbon and alloy steels can be hardened and tempered to hold an edge, and are the right choice for chisels, axes, knives, and other cutting or wear-surface tools. Using the wrong steel for a job either wastes effort (trying to harden mild steel) or produces a tool that is unpredictably brittle (over-hardening the wrong alloy).

### 3.2 Common Recognizable Steel Sources and Types

| Steel / source | Approx. carbon content | Typical use | Notes |
|---|---|---|---|
| Mild steel (1018 and similar structural/mystery mild steel) | ~0.15–0.20% | Brackets, hooks, tongs, non-edge hardware | Cannot be usefully hardened; the default "unknown scrap steel" assumption unless proven otherwise |
| 1084 | 0.80–0.93% | Knives, chisels, general tool steel | Widely recommended for beginners because it heat-treats predictably even without advanced equipment |
| 1095 | 0.90–1.03% | Knives, farm-implement edges, springs | High-carbon; used industrially for farm-implement edges and music wire; excellent edge but less tough than lower-carbon steels |
| 5160 | ~0.60% carbon + ~1% chromium | Leaf springs, swords, big impact tools | Extremely tough (resists breaking) but does not hold a razor edge as long as 1084/1095 — the classic "leaf spring" scrap steel |
| W1 (and O1) | Similar to 1095 | Traditional tool steel | W1 is essentially 1095 with a wider tolerance band; shallow-hardening, very tough |

[Sources: World Backyard, *Knife Steel Composition Table Explained*; BladeForums, *1084 vs 1095, 5160, O1, etc.*; Sharpening Made Easy, *Steels Used By Knife Makers*]

### 3.3 Sourcing Steel from Scrap

**The best beginner scrap sources**, per experienced smiths, are consistent and forgiving:
- **Leaf springs** (truck/car suspension): already close to flat bar stock with a slight curve, roughly 5160-equivalent — "phenomenal" material that is widely available at auto scrapyards
- **Coil springs**: good for smaller stock once straightened
- **Old files and rasps**: typically very high-carbon steel (though brittle, and any remaining "teeth" texture needs to be forged/ground away)
- **Large bearings**: high-carbon, consistent

[Source: Make It From Metal, *Where to Find High Carbon Steel Scrap*]

**A caution on rebar**: construction rebar is a very common, very free scrap material, but it is typically a low, inconsistent-carbon steel with unpredictable alloying (often includes recycled scrap of unknown origin) and is a poor choice for any tool that needs to hold an edge or be reliably heat-treated. Use rebar for non-critical, non-edge decorative or low-stress work, not for chisels, axes, or knives.

**The honest limitation of scrap sourcing**: unless steel is bought new with a mill certificate, its exact alloy composition can never be known with certainty — this is an accepted, standard limitation in the craft, not a gap unique to this guide. [Source: Make It From Metal, *Where to Find High Carbon Steel Scrap*]

### 3.4 Spark Testing (Screening Method, Not Definitive Identification)

Touching a piece of steel to a grinding wheel produces a spark pattern whose appearance is caused mainly by carbon in the steel oxidizing as it burns. **Mild steel** produces a duller, less brilliant spark stream with occasional small forks near the base. **High-carbon steel** produces a "bushy," heavily forking spark pattern with brighter, more explosive sparks — the higher the carbon, the more pronounced this pattern. [Source: IspatGuru, *Spark Testing of Steels*; Wasatch Steel, *Basics on the Spark Test for Steel and Other Metals*]

**Important limitation**: spark testing requires practice to interpret correctly, needs consistent grinding pressure and consistent (ideally shaded) lighting to compare results reliably, and with the huge number of modern alloy steels in circulation, cannot definitively identify an exact alloy — it is a useful **screening tool** to sort a scrap pile into "probably mild," "probably medium-carbon," and "probably high-carbon" bins, not a substitute for known material. [Source: IspatGuru, *Spark Testing of Steels*]

### 3.5 The File Hardness Test (Post-Heat-Treatment Check)

A standard mill file is itself hardened to roughly 62–65 HRC. Dragging a sharp file across a piece of steel is a simple, low-equipment way to check whether heat treatment worked: if the file **bites and cuts**, the workpiece is softer than the file (roughly below ~56–58 HRC); if the file **skates** across the surface without cutting, the workpiece is at or above file hardness. This is not a precise Rockwell measurement (accuracy is roughly ±5 HRC, or ±2–3 HRC with practice), but it is the standard field check used by smiths without lab equipment. A calibrated hardness-file set (multiple files pre-hardened in 5-HRC steps from 40–65 HRC) gives a more precise bracket. [Sources: BladeForums, *Proper way to perform a "file test"*; Make It From Metal, *How to Check the Hardness of Metal: A Complete Guide*]

---

## Part 4: Fundamental Forging Techniques

### 4.1 Reading Heat by Color

Steel changes visible color as it heats, and this color is the traditional (and still standard) way a smith judges temperature without a thermometer. Colors are best judged in **shade, not direct sunlight** — a forge fire that looks orange in bright daylight may already be at working-hot yellow in shade.

| Color | Approx. temperature | Significance |
|---|---|---|
| Dark/dull cherry red | ~1,300–1,400°F (700–760°C) | Below full forging temperature for most steels; usable for some bending, too cold for serious hammer work |
| Bright cherry red | ~1,500–1,600°F (815–870°C) | Lower end of the working range for many carbon steels |
| Orange | ~1,650–1,725°F (900–940°C) | Solid working-forge heat |
| Orange-yellow / yellow ("lemon heat") | ~1,900–2,400°F (1,040–1,315°C) | The sweet spot for heavy initial forging of most carbon steels — metal moves easily under the hammer |
| White | Above ~2,400°F (1,315°C) | Approaching burning temperature — sparking/burning steel is being destroyed, not forged; back off immediately |

[Sources: MachineMFG, *Steel Temperature Color Chart: A Complete Comparison*; Knifemaking.com, *Forging Steel Heat & Color Chart*; West Yorkshire Steel, *Steel Hardening & Forging Temperatures Colour Chart*]

**Practical rule**: forge in the orange-to-yellow range; stop hammering and reheat once the work drops to dull red, since hammering cold or near-cold steel work-hardens and cracks it rather than shaping it cleanly.

### 4.2 Drawing Out (Lengthening)

Drawing out lengthens a piece of stock by reducing its cross-section, typically using the cross-peen face or a fuller, working along the length of the bar with overlapping blows and rotating the stock regularly to keep the section even (square or round, as needed). This is the single most-used technique in forging — nearly every project starts by drawing a point, taper, or thinned section from thicker stock. [Source: ABANA Controlled Hand Forging curriculum, Lesson One: Drawing Out]

### 4.3 Upsetting (Thickening)

Upsetting is the reverse operation: making a section of metal *thicker* by shortening it in the other dimension. The classic method is heating the end of a rod and hammering directly on the hot end (as if driving a nail) — the rod shortens and the hot end widens/thickens. An alternative technique places the *hot end down* on the anvil and hammers the *cold end* of the bar, which concentrates the upsetting force at the hot section without requiring the smith to hit a moving hot target directly. [Source: ABANA, Basic forging techniques — Upsetting; Wikipedia, *Blacksmith*]

### 4.4 Bending, Twisting, Punching, and Cutting

- **Bending**: performed at a full working heat (orange-yellow), over the anvil horn (curves) or edge (sharp angles), or in a bending fork/jig for repeatable angles.
- **Twisting**: square or hexagonal stock, heated evenly along the section to be twisted, gripped at both ends (one end often in a vise), and rotated — uneven heating produces an uneven twist, a common beginner mistake.
- **Punching**: a punch (round, square, or slot-shaped) driven partway into hot stock from one side, then finished from the reverse side to avoid tearing/dragging metal through — this is how holes, eyes (for hammer/axe heads), and hardy-hole-fitting tangs are formed. A **drift** (a shaped rod, often slightly tapered) is then driven through to true up and size the punched hole precisely — this is exactly the sequence used in the axe-eye worked example in Part 6. [Source: FAO, *Advanced Blacksmithing*, Practice Job 29 — Making Axes]
- **Cutting**: hot metal is cut with a **hot set** (a chisel-like tool struck with a hammer, or driven by hand into a hardy-hole-mounted hardy for one-handed work) at bright red-to-yellow heat, working from one side partway through and finishing from the other side, then breaking the remaining sliver.

### 4.5 Forge Welding (Advanced)

Forge welding joins two pieces of steel by heating both to near-melting (a "welding heat," well above normal working heat, into the bright yellow/white range) with a flux — traditionally **borax**, a fluxing chemical that prevents oxide scale from blocking a clean weld — sprinkled on the joint, then hammering the pieces together while both are at welding heat. This is the most technically demanding basic forging skill: too cold and the pieces won't fuse; too hot and the steel burns and is ruined. Coal or coke forges reach forge-welding temperatures far more reliably than charcoal, because slower charcoal heating tends to build up oxide on the steel surface, which itself interferes with a clean weld. [Sources: FAO, *Advanced Blacksmithing*, Appendix I and Glossary entries for "Borax" and "Cleft"]

---

## Part 5: Heat Treatment

Heat treatment is what turns a piece of shaped steel into a tool that actually holds up under use. Three distinct operations matter: annealing (softening for further work), hardening (maximizing hardness), and tempering (reducing brittleness while retaining most of the hardness). Skipping tempering after hardening produces a tool that is hard but dangerously brittle — it will chip or shatter rather than hold an edge under impact.

### 5.1 Annealing and Normalizing

- **Annealing**: heating steel to just above its critical (non-magnetic) temperature and then cooling it *as slowly as possible* (buried in ash, sand, vermiculite, or simply left in a shut-off forge overnight) to achieve maximum softness — needed before filing or fine cold-work on high-carbon steel that would otherwise be too hard to file.
- **Normalizing**: heating to the same critical range and air-cooling (not buried/insulated, but not force-cooled either) to relieve internal stresses and return the steel to a "normal," even-grained condition — commonly done between forging and hardening, especially if the piece was hammered unevenly or at inconsistent temperatures. [Sources: FAO, *Advanced Blacksmithing*, Glossary entries "Anneal" and "Normalize"; FAO, Practice Job 29]

### 5.2 Hardening: Quenching

Hardening is achieved by heating the steel to its critical (non-magnetic) temperature — checkable with a magnet, since steel loses magnetism at this point, historically the field method before thermometers — and then **quenching**: cooling it rapidly in a liquid medium.

**Quench medium selection matters and is alloy-dependent**:
- **Water or brine** quenches fastest and hardest but risks cracking, especially in higher-carbon or thin-sectioned steel; some smiths use water for genuinely low-alloy, simple steels where the risk is acceptable and speed is needed.
- **Oil** (commercial quenching oil, or improvised low-viscosity motor, canola, or vegetable oil) quenches more gently and is the standard choice for most tool and knife steel, reducing cracking risk while still achieving full hardness for oil-hardening alloys.
- Cooling below roughly 900°F (480°C) is the critical window — for many carbon steels, full quench engagement (agitating the piece in a slicing motion through the liquid) for 10–30 seconds is sufficient. [Sources: Red Label Abrasives, *How to Heat Treat a Knife*; Knife Steel Nerds, *Which Quenching Oil is Best for Knives?*]

**Farm-tool worked example (from FAO field practice)**: for a ploughshare edge or similar farm-tool cutting edge, the FAO manual's standard field procedure is to heat the cutting edge to dull red and quench in oil — a deliberately gentler heat/quench combination than a fine knife blade would use, appropriate for a tool that needs toughness against rocks and roots more than a fine, brittle edge. [Source: FAO, *Advanced Blacksmithing*, Practice Job 13 — Ploughshares]

### 5.3 Tempering

Immediately after hardening, a tool is too brittle for use and must be tempered: reheated to a **much lower** temperature than hardening (typically 300–500°F / 150–260°C) and held or slow-cooled, which sacrifices a small amount of hardness in exchange for a large gain in toughness. [Source: Red Label Abrasives; Knife Steel Nerds]

**Tempering by color (traditional field method)**: as freshly ground/polished steel is gently reheated, it passes through a sequence of thin-oxide-layer colors that correspond closely to temperature — this is the traditional no-oven tempering method still used in the field:

| Temper color | Approx. temperature | Typical use |
|---|---|---|
| Pale straw | ~400°F (200°C) | Very hard, most brittle — scrapers, some knife edges |
| Medium/dark straw | ~440–460°F (225–240°C) | Chisels, axe edges, punches — hard with reasonable toughness |
| Brown | ~500°F (260°C) | Springs, some striking tools |
| Purple | ~530°F (275°C) | Tools needing more shock resistance |
| Blue | ~570°F (300°C) | Screwdrivers, some striking-tool faces — toughest, softest of the useful range |

[Sources: MachineMFG, *Steel Temperature Color Chart*; FAO, *Advanced Blacksmithing*, Practice Jobs 1 and 26 — describing tempering "at a brownish oxide colour" for lower-carbon tool steel and "in the transition between brown and blue" for higher-carbon steel]

**FAO field method detail**: the manual's standard procedure for a punch or chisel is to harden, then polish a small area, and gently reheat (often using the *residual heat conducted up the shank from a still-hot section*, or a controlled secondary heat source) while watching the oxide color travel to the cutting edge, quenching again the instant a medium-straw color is reached — stopping short of the dark straw/brown range for a tool that needs to stay very hard. [Source: FAO, *Advanced Blacksmithing*, Practice Job 43]

**Oven/toaster-oven tempering (modern equivalent)**: a kitchen or dedicated toaster oven set to the target Fahrenheit temperature above, holding the piece for 45–60 minutes, is a more precise and repeatable modern substitute for color-judging, and is standard practice among hobbyist bladesmiths — two tempering cycles (heat, cool to room temperature, repeat) is common practice for more consistent results than a single cycle. [Source: Knife Steel Nerds, *Which Quenching Oil is Best for Knives?*]

### 5.4 Case Hardening Mild Steel

Mild steel cannot be through-hardened the way high-carbon steel can, but its *surface* can be selectively hardened by **carburizing** — packing or heating the workpiece in contact with a carbon-rich material (traditionally bone char, charcoal, or a commercial case-hardening compound) with air excluded, so carbon diffuses into the surface layer only. After a period at red heat in this carbon-rich environment, the piece is quenched, producing a hard outer shell over a still-tough, non-brittle mild-steel core — useful for wear surfaces on tools that need a soft, shock-absorbing body but a hard working face (e.g., certain jigs, gauges, and wear plates). [Source: FAO, *Advanced Blacksmithing*, Practice Job 24 and Glossary entries "Carburize" / "Case harden"]

---

## Part 6: Making and Repairing Tools — Worked Examples

### 6.1 A Cold Chisel (Beginner Project)

**Material**: high-carbon tool steel (1084/1095-equivalent) or a coil-spring section, roughly 16 mm (5/8 in) round or hex stock.

**Method**:
1. Heat one end to bright orange-yellow.
2. Draw out to a flat point using the cross-peen or a fuller, rotating regularly to keep the taper even.
3. Refine the cutting edge by grinding or careful filing once cool, or fine-forge it with a flatter near the end of the drawing-out process.
4. Anneal if extensive filing/grinding is needed and the steel has become too hard from forging heat cycles.
5. Harden by heating the cutting-edge area to critical (non-magnetic) temperature and quenching in oil (water for some steels, at higher crack risk).
6. Temper to a medium-straw color (or ~440–460°F / 225–240°C in an oven), leaving the striking end (the tang, where a hammer will hit it) noticeably softer than the cutting edge — a fully hardened striking end is prone to chipping and throwing dangerous steel fragments when struck. [Source: FAO, *Advanced Blacksmithing*, Practice Job 43 — flat cold chisel]

### 6.2 Repairing a Hoe or Garden Tool (Practical Homestead Repair)

A bent or cracked hoe blade, or one that has separated from its tang/socket, is one of the most common tool failures a homestead will face — and one of the most directly useful repairs to learn, connecting straight to the Wave 3 Food Production guide's tool-dependent tasks.

**Common failure modes and fixes**:
- **Bent blade**: reheat the bent section to orange heat and straighten over the anvil horn or edge with controlled hammer blows — cold-straightening a hardened blade risks cracking it.
- **Cracked or separated tang** (the shank connecting blade to handle): the FAO manual describes making hoe tangs *separately from blades* specifically so a damaged tang can be replaced without remaking the whole blade — a new tang is forge-welded or riveted onto the salvageable blade body. [Source: FAO, *Advanced Blacksmithing*, Practice Job 30 — "Making Hoe Tangs Separately from Blades"]
- **Dull or rolled edge**: re-drawn at yellow heat with a fuller and hand hammer, then re-hardened and tempered following the same sequence as the cold chisel above, but tempered slightly softer (toward brown) since garden tools benefit more from edge-holding durability against rocks and roots than from maximum hardness.

### 6.3 Making an Eyed Axe Head (Intermediate/Advanced Project)

This worked example follows the FAO manual's field-tested sequence closely, since it is one of the most complete and specific worked examples available in the source literature.

**Material**: leaf-spring steel or carbon-tool-steel bar, 16 mm (5/8 in) thick or more (12 mm spring steel can be upset to sufficient thickness but is more difficult below that).

**Method**:
1. Take a piece roughly 16 × 60 × 100 mm (or a comfortable "hand length" — a length that can be worked without tongs, roughly the distance from fingertips to elbow).
2. Mark 25 mm from one end on a narrow edge; heat to yellow.
3. Using a purpose-made **slot punch**, drive into the marked point, cooling the punch after every 2–3 blows to prevent it from losing its own temper. Punch roughly 8 mm deep from one side, then repeat from the opposite side, working alternately until the slot passes through — the metal width will reduce somewhat during this process.
4. Reheat to bright red and drive an **eye drift** (a tapered, eye-shaped rod) into the slot from each side alternately until the eye (the hole the handle will pass through) is fully formed and correctly shaped; a **U-shaped support piece** is used underneath to support the work during drifting.
5. With the eye formed, draw out the blade portion at yellow heat using a fuller (which spreads metal in the intended direction, unlike a flat hammer face, which spreads it in all directions), then finish/smooth with a flatter, trimming excess with a hot set.
6. Correct any eye distortion caused by the drawing-out process by re-drifting.
7. Finish the cutting edge by grinding or filing; normalize if grinding equipment is available, or fully anneal if extensive filing is needed.
8. Harden and temper the cutting edge to a **medium-straw** color, leaving the poll (back) and eye area of the head noticeably softer/tougher.
9. Final sharpening is done by hand with a carborundum stone or similar. [Source: FAO, *Advanced Blacksmithing*, Practice Job 29 — "Making Axes," including Figures 224–232 in the original manual]

Larger axe heads follow the same sequence with heavier stock and larger drifts sized proportionally.

### 6.4 Bootstrapping Tongs

Tongs are a genuinely useful early-intermediate project because they let a smith with one starter pair of purchased tongs forge additional, better-fitted pairs for specific stock sizes. The basic method: two matching pieces are forged with a flattened, shaped jaw at one end (shaped to grip the stock size intended — flat, round, or square), a **rivet hole** punched through both pieces at the pivot point, joined with a rivet, and the handles drawn out to a comfortable length (with a slight outward spring built into the handles so the jaws naturally want to open). This is a standard early "make your own better tools" project in essentially every basic-blacksmithing curriculum. [Source: Hackaday, *Blacksmithing For The Uninitiated: Hammer And Tongs*]

### 6.5 Making Drill Bits and a Boring Brace (When Manufactured Ones Aren't Available)

Twist drills and boring braces are precision manufactured items — exactly the kind of tool a resilience-focused household should know how to substitute when the supply chain that makes them is unreliable. The FAO field method produces genuinely usable, if crude by factory standards, drill bits from simple round stock.

**Material**: carbon-tool steel or vehicle-spring steel, round section, in whatever diameters are needed.

**Method**:
1. Draw down the shank end of the stock to the diameter needed for the chuck or brace it will be used in — the shank must be *smaller* than the cutting-edge diameter, so for a small-diameter bit, expect to draw the shank down substantially from your starting stock.
2. Reheat and flatten the opposite (cutting) end to slightly wider than the finished bit diameter — accurate, neat work here keeps the cutting point centered on the shank axis, which matters for the bit to drill straight and not wobble.
3. Square off the flattened end and mark a centerline, with layout lines 45° to either side of it.
4. Using a sharp hot chisel on the anvil's cutting table (hardy edge), cut the point — critically, **cut only on the right-hand side of the centerline first, then turn the work and repeat** for the other side; this pre-forms the clearance angles the bit needs to cut rather than just scrape, and reduces the amount of finish-filing needed afterward.
5. Reheat the whole job evenly to red heat, true it up, and fully anneal.
6. Once cool, file the clearance angles precisely, testing by rotating the bit against a flat surface until the cutting edges look symmetric and even.
7. Harden and temper to a **brown** color — noticeably softer than a chisel or axe edge, because a drill bit needs to resist chipping under twisting/torsional load more than it needs maximum edge hardness.
8. Use at slow speed with plenty of lubricant (old motor oil is adequate) — shop-made bits are not designed for the high speeds of a modern powered drill press and will overheat and dull quickly if run that way.

Two shank styles are useful to know: a **hexagonal shank** for a three-jaw chuck (power or hand drill), and a **square, tapered shank** for a traditional carpenter's boring brace or ratchet drill. [Source: FAO, *Advanced Blacksmithing*, Practice Job 3 — "Making Drill Bits for Drilling Metal"]

**A companion project — the boring brace itself**: where a manufactured carpenter's brace isn't available, a functional substitute can be forged from 12 mm (or larger) round mild steel, bent into the offset crank shape of a standard brace, with a simple chuck end (formed with a bolster plate, round punch, and square punch) that grips the tapered-shank bits described above. It is turned by hand with a wooden lever/handle at the crank offset — slower than a geared hand-drill, but fully functional for drilling holes in wood or, with the bits above, in metal. [Source: FAO, *Advanced Blacksmithing*, Practice Job 4 — "Making a Simple Wood-Boring Brace"]

### 6.6 Making Your Own Files and Rasps

This is arguably the single most important "bootstrapping" project in this entire guide: files and rasps are themselves precision tools used to *sharpen and finish everything else*, and in a scenario where they become scarce or expensive, a smith who can make replacement files is no longer blocked by their absence. The FAO manual notes this is standard practice specifically **in rural areas where files and rasps are expensive and scarce** — precisely the resilience scenario this guide addresses.

**Material**: low-carbon (mild) steel flat bar or angle-iron flanges, roughly 25–30 mm wide and 4–6 mm thick, cut to the length needed; case-hardening compound (commercial, or a improvised carbon-rich packing material).

**Method**:
1. Forge, harden, and temper a flat cold chisel for cutting flat-file teeth, sharpened from **one side only**; for rasps (coarser, individually-punched teeth rather than continuous file-cut lines), forge a **round-nosed chisel** instead.
2. Forge the handle as an integral part of the tool blank (rather than a separate tang fitted afterward) — this is more practical for supporting the work while teeth are being cut.
3. Fully anneal the blank, clean off oxide scale, and support it firmly (in a vise or clamped to a bar) for tooth-cutting.
4. **For a rasp**: hold the round-nosed chisel at roughly 60° to the work and strike firmly to raise an indentation, then lower the angle to about 30° and give one or two more light blows to raise the tooth to full size. Repeat down the length of the blank — spacing does not need to be precise and can be judged by eye; staggering the teeth (rather than lining them up in neat rows) gives a better cutting action. With practice, a full rasp can be cut in **15–20 minutes**.
5. **For a flat file**: hold the flat-edged chisel nearly vertical, angled across the width of the blank, and strike sharply — the chisel's edge angle raises a small lip that forms a file tooth as it cuts. Repeat along the blank's length. Teeth are cut on one side and one edge only; a coarser or finer cut depends on hammer-blow force and tooth spacing, and a "second cut" (a finer crosshatch pass) can be added over the first for a smoother-cutting file.
6. **Half-round rasps**: a section of steel water pipe (zinc plating removed, if galvanized) makes a ready-made half-round blank — teeth are cut one-third to halfway around its circumference in the same manner.
7. Straighten any upward bend in the blank (a normal side-effect of the chisel-striking process) against a wooden block — this doesn't damage the newly cut teeth if done carefully.
8. **Case-harden the toothed face only**: heat the file/rasp evenly to bright red along its working length, sprinkle case-hardening compound over the teeth (or press the hot face down onto compound laid on a sheet-metal surface near the fire) so it melts and carbon diffuses into the surface, let it cool slightly below red heat, then reheat evenly to red and quench in cold clean water — **turn your face away while quenching**, since a fast water quench of a thin, hot piece can spit hot droplets. This produces a thin, very hard, effective cutting surface over a tough mild-steel body.
9. When the hardened surface eventually wears through with use, the tool can be fully re-annealed, the teeth re-cut, and the surface re-hardened — a shop-made file is a renewable tool, not a disposable one.

[Source: FAO, *Advanced Blacksmithing*, Practice Job 9 — "Making Carpenters' Rasps and Files"]

### 6.7 Hafting and Handle Fitting

A tool head is only as good as its attachment to a handle. General principles:

- **Eyed tools** (axes, hammers, mauls): the wooden handle is shaped to taper slightly toward the top, driven up through the eye from below, and secured with one or more **wooden or metal wedges** driven into a saw kerf cut into the top of the handle — the wedge spreads the wood tightly against the inside of the eye. Metal wedges are easily smith-made from scrap mild steel. [Source: FAO, *Advanced Blacksmithing*, Practice Job discussing wedge-making, "metal wedges are easily made by a smith, scrap mild steel...quench the work in water and break off the wedge"]
- **Tanged tools** (many hoes, files, chisels used with a separate handle): the tang is heated and driven/burned into a pre-drilled handle socket, or fitted into a socket and secured with a **ferrule** (a metal collar/ring) to prevent the wood from splitting.
- **Handle wood selection**: dense, shock-resistant hardwoods — hickory is the traditional North American standard for striking-tool handles, with ash a widely available Zone 5 alternative.

---

## Part 7: Sharpening and Tool Maintenance

### 7.1 Sharpening Stones and Angle Selection

Sharpening stones range from coarse (fast material removal, for re-establishing a damaged edge) to fine (polishing, for a final working edge). A practical progression for most tool edges is roughly **1,000 grit** for initial edge work, followed by **4,000–6,000 grit** for polishing. [Source: Chubo Knives, *How to Sharpen a Knife with a Stone: Grit, Maintenance & More*]

**Edge angle depends on use, not a single universal number**: fine cutting/paring edges (knives, some chisels) commonly use 15–25° per side; general-purpose tool edges often run 20–30°; consistency of angle matters more than hitting an exact number — a wandering angle produces a rounded, weak edge regardless of grit used. [Source: Garrett Wade, *Using Sharpening Stones*]

**Oil stones vs. water stones**: oil stones are more durable and need less maintenance, making them well suited to garden and farm tool sharpening; water stones cut faster but wear down more quickly and need more frequent flattening — check with a straightedge across the stone face periodically, since stones wear faster in the center than at the edges. [Source: Farmstand App, *7 Approaches to Sharpening Garden Tools That Extend Their Lifespan*; Chubo Knives]

### 7.2 A Basic Tool Maintenance Routine

- Clean and lightly oil edge tools after use to prevent rust, especially important in Zone 5's humid summers and freeze-thaw winters.
- Store edge tools with blade guards or in a way that protects the edge from contacting other metal.
- Re-sharpen at first sign of dulling rather than waiting for a tool to become genuinely difficult to use — a slightly dull edge takes a few strokes to restore; a badly dull or damaged edge requires much more aggressive (coarse-stone or grinding-wheel) correction.
- Inspect handles regularly for cracks, looseness, or splinters, and re-wedge or replace before a head comes loose in use — a loose axe or hammer head is a serious safety hazard.

---

## Part 8: Machine Tools Beyond the Forge

Not every metal- or wood-shaping task is done at the anvil. A resilient household or community workshop benefits from a small set of **hand- or foot-powered machine tools** that extend capability without requiring reliable grid power.

### 8.1 Mechanical Advantage Basics

Every hand- or foot-powered machine tool relies on the same handful of physical principles to trade speed for force (or vice versa):

- **Levers**: force applied at one point on a rigid bar pivoting on a fulcrum is amplified or reduced depending on the relative distances from the fulcrum — the working principle behind treadles, hand-cranked mechanisms, and simple presses.
- **Pulleys**: a single pulley only redirects force (mechanical advantage of 1); combining multiple pulleys (a block-and-tackle) multiplies force roughly in proportion to the number of rope segments supporting the load.
- **Gears**: a gear train where the output gear has more teeth than the input gear reduces output speed but amplifies output torque (a "speed reducer") — this is exactly the mechanism used inside a hand-crank forge blower to make cranking effective. [Source: FAO, *Advanced Blacksmithing*, Glossary — "Fan"; hand-crank blower gearing described in Air Control Industries, *The Evolution of the Blacksmith Forge Fan*]
- **Real-world efficiency**: no mechanism achieves its full theoretical (ideal) mechanical advantage — friction losses always reduce actual output somewhat, which is why hand-built mechanisms benefit from good bearings/bushings and regular lubrication.

[Source: Wikipedia, *Mechanical advantage*; Wikipedia, *Simple machine*]

### 8.2 The Pole Lathe and Treadle Lathe (Wood Turning)

The **pole lathe** is a foot-powered wood-turning lathe using the springiness of a long pole as a return spring: pressing a foot treadle pulls a cord wrapped around the workpiece (spinning it), and the pole's spring-back raises the treadle again for the next stroke — cutting happens only on the down-stroke. This is an ancient design (in continuous documented use since at least the Viking era) that has seen a genuine craft revival in green woodworking. [Source: Wikipedia, *Pole lathe*]

The **treadle lathe** is a related but distinct design using a flywheel for continuous rotation rather than a springy pole, giving more even cutting action across both directions of the treadle stroke — historically more common than pole lathes in North America, often built from wood with purchased metal hardware (bearings, drive components). [Source: Hackaday, *Building A Treadle Powered Lathe*; Open Source Machine Tools, *Make Your Own Treadle Lathe*]

**Resilience relevance**: a working lathe (wood or, with a more robust build, light metal) lets a household turn its own tool handles, wheel hubs, bowls, and round stock — without it, every round wooden part in a household's tool inventory is a purchased-or-scavenged item rather than a producible one.

### 8.3 Hand-Crank Drilling and Grinding

The FAO recommended-tools list (Part 2.4 above) specifically calls out a **hand-powered drilling machine** and a **hand- or foot-powered grinding machine (150–200 mm wheels)** as the standard rural/off-grid substitute for electric drill presses and bench grinders — both remain available as new manufactured items (marketed toward off-grid and antique-tool communities) or can be sourced used, and both are functionally adequate for tool-scale work, if slower than powered equivalents. [Source: FAO, *Advanced Blacksmithing*, Appendix II]

---

## Part 9: Safety

Blacksmithing and metalworking safety concerns fall into four categories, each with a specific, non-negotiable mitigation.

### 9.1 Burns

Hot metal, hot tools, and stray sparks are the most constant hazard. **Never wear synthetic fabrics** (polyester, nylon, and similar) while forging — they melt onto skin on contact with hot metal or a spark, causing far worse burns than natural fibers. Wear natural-fiber clothing (cotton, wool, leather) and heavy-duty gloves; gloves should fit loosely enough that a "flick of the wrist" causes them to fall off if hot metal or a spark lands inside one — a tightly fitted glove traps the hazard against skin instead of letting it be shed. [Source: Breakthrough Blacksmithing, *Forge with Confidence: Essential Blacksmithing Safety Guidelines*]

### 9.2 Eyes and Ears

- **Eye protection**: safety glasses or goggles rated to the **ANSI/ISEA Z87.1** standard (look for "Z87.1+" markings, which indicate the higher impact rating appropriate for grinding, cutting, and spark-producing work) should be worn at all times at the forge and grinder — this is also the OSHA-referenced standard (29 CFR 1910.133) for any workplace eye protection requirement. [Sources: WC Safety, *Guide to Safety Glasses Standards*; Paulson Manufacturing, *Understanding ANSI Z87.1*]
- **Hearing protection**: earmuffs or earplugs during sustained hammering or power-tool use, since repeated hammer-on-anvil impact noise is a genuine long-term hearing hazard. [Source: Breakthrough Blacksmithing]

### 9.3 Lungs and Carbon Monoxide

Coal and propane combustion produce carbon monoxide — an odorless, colorless gas that is fatal in enclosed, poorly ventilated spaces well before it is detectable by smell or symptoms in early stages. Solid-fuel forging also produces particulate smoke and, with coal specifically, sulfur dioxide. **Never operate a solid-fuel or propane forge in an enclosed garage, basement, or shed without dedicated exhaust ventilation** — outdoor or open-sided, well-ventilated setups are the standard safe practice, not an optional precaution. [Source: Breakthrough Blacksmithing, *Forge with Confidence*]

### 9.4 Fire and General Workshop Hazards

Keep a fire extinguisher (or, for a solid-fuel forge, a bucket of sand and a bucket of water — both already present as forge equipment) within immediate reach. Clear the forge area of flammable material, and never leave a lit forge unattended. Crushed fingers, cuts, and puncture wounds from hot-work tools round out the standard hazard list — a deliberate, unhurried pace and clear communication (especially when a striker is swinging a sledgehammer while the smith directs with a hand hammer) prevent most of these incidents. [Source: Breakthrough Blacksmithing, *Forge Ahead Safely*]

---

## Part 10: Community-Scale Production

### 10.1 Why Blacksmithing Suits Shared/Co-op Models Especially Well

A forge, anvil, and full hand-tool kit represent a genuine capital investment (realistically $500–1,600 for a complete beginner setup, per Section 10.2 below) that most single households will not use daily. Unlike a garden or a spinning wheel, a shared forge sees productive, safe use by multiple skilled users on a rotating schedule without much conflict, because forging is inherently a one-project-at-a-time activity at a single workstation — this makes it one of the more naturally cooperative resilience capabilities.

Existing community forge and metalworkers'-guild models — cooperative-structured makerspaces that provide members access to shared metal shops, blacksmithing equipment, welding/fabrication tools, training, and mentorship, often organized as public-benefit or member-owned structures that explicitly prioritize member and community interest over profit — are a proven, currently operating template for this kind of shared capability, not a hypothetical. [Sources: The Indy Forge (community blacksmith makerspace/co-op model); Mill Forge Makerspace (Massachusetts Public Benefit Corporation structure); Past Lives Makerspace metalworkers' guild]

### 10.2 A Realistic Shared-Shop Budget (2026 USD)

| Item | Cost range |
|---|---|
| Forge (propane, new) | $250–450 |
| Forge (solid-fuel, scrap-built brake-drum) | $30–100 |
| Anvil (70–110 lb, used–new) | $150–700 |
| Starter hammer | $30–80 |
| Starter tongs (2–3 pairs) | $60–120 |
| Vise (heavy-duty leg vise, used) | $75–250 |
| Files, rule, square, calipers (basic layout/finishing kit) | $50–150 |
| **Total realistic minimum setup** | **~$440–1,600** depending on new/used mix |

[Sources: Begin To Black Smith, *How Much Does It Cost to Begin Blacksmithing*; Oldboy Metal Co., *Starting a Forge at Home: The 5 Tools You Actually Need*; Homestead Heritage Forge, *Setting up a Home Blacksmith Shop*]

Divided across even a modest 10-household group, this is a one-time cost of roughly $45–160 per household for a genuinely capable shared shop — far more accessible than each household independently equipping its own forge.

### 10.3 Skill-Sharing Structure

The FAO manual's own three-tiered curriculum design (*Basic Blacksmithing → Intermediate Blacksmithing → Advanced Blacksmithing*, each building skill and tool complexity on the last) is itself a usable template for a community teaching sequence: a small group of early learners masters basic drawing-out, bending, and simple hand-tool projects (Part 6.1–6.2 of this guide) before progressing to eyed-tool and forge-welding work (Part 6.3–6.5), with more experienced members mentoring newer ones directly at the anvil — the traditional master/apprentice structure that blacksmithing has used for centuries, and which modern makerspace/guild models explicitly continue. [Source: FAO Agricultural Services Bulletin series structure, cross-referenced against Mill Forge Makerspace and Past Lives Makerspace guild-mentorship models]

---

## Part 11: Troubleshooting Common Forging Problems

| Symptom | Likely cause | Fix |
|---|---|---|
| Hammer blows leave deep dents/marks instead of shaping the metal smoothly | Work is too cold (below dull-red) | Stop, reheat to full orange-yellow before continuing; hammering cold steel work-hardens and can crack it rather than move it |
| Steel sparks and throws bright white sparks with a crumbly, burnt-looking surface | Overheated — steel is burning, not forging | Cut off the burnt section if possible; burnt steel is structurally ruined and cannot be recovered by further forging |
| A punched or drifted hole comes out oval, off-center, or torn rather than clean | Punching too fast without reheating, or not finishing from the reverse side | Reheat between punching stages; always punch partway from one side and finish from the opposite side rather than driving straight through from one face |
| A hardened piece cracked during the water/oil quench | Quench too fast for the alloy, water used on a crack-prone steel, or an uneven/thin cross-section quenched unevenly | Switch to a slower quenchant (oil instead of water) for that alloy; agitate the piece evenly during quenching rather than holding it still; consider quenching only the working edge rather than the whole piece |
| Tool holds an edge briefly, then chips or rolls under normal use | Tempered too hard (temper color too pale/too low a temperature) for the tool's actual use | Re-temper to a slightly higher temperature/darker color (toward brown) for tools that take impact, saving the palest straw temper for pure-cutting, low-impact edges |
| A file "skates" everywhere on a piece that should have hardened, suggesting failure | Steel is actually low-carbon/mild (won't harden by heat treatment at all), or the piece never reached critical (non-magnetic) temperature before quenching | Confirm with the magnet test *before* quenching next time; if the steel truly is mild, no quench schedule will harden it — accept it for non-edge uses instead |
| A twist comes out uneven, tighter in one section than another | Uneven heating along the section being twisted | Reheat evenly across the full twist zone before applying twisting force; twist slowly and check evenness partway through |
| An eye (axe/hammer head) comes out lopsided after drawing out the blade | Drawing-out forces distorted the already-formed eye | Re-drift the eye after drawing-out to true it back up, as described in the axe worked example (Section 6.3) |

[Source: synthesized from FAO, *Advanced Blacksmithing* method notes and ABANA Controlled Hand Forging curriculum troubleshooting guidance embedded throughout individual lessons]

## Part 12: First Forging Session — A Beginner Checklist

For a household or community member forging for the first time, a simple, low-risk first session builds real skill without the complexity of heat-treatment or precision work:

1. **Before lighting the fire**: PPE on (natural-fiber clothing, ANSI Z87.1-rated eye protection, loose-fitting heavy gloves); fire extinguisher or sand/water buckets within reach; forge set up outdoors or in confirmed good ventilation; a helper present if this is a genuinely first-ever session.
2. **Light the fire** and build a confined, appropriately deep fuel bed (100–140 mm for a coal/charcoal fire) before introducing any steel.
3. **Pick a forgiving first project** — a simple S-hook or plant hanger from a single piece of mild-steel round or square stock is the traditional first project: no heat-treatment needed, teaches heating, drawing-out, and bending in one short exercise, and produces a genuinely useful object.
4. **Heat to full orange-yellow** before the first hammer blow — a common beginner mistake is starting to hammer on steel that only looks hot but is still in the dull-red range, producing frustrating, ineffective blows.
5. **Practice drawing out** a taper on scrap stock before attempting the actual project — this single motion (Section 4.2) underlies almost everything else in the craft.
6. **Quench only mild steel in water for cooling between working stages** (not for hardening — mild steel does not harden) — this is safe and normal, distinct from the hardening quench described in Part 5, which applies to carbon-tool-steel projects only.
7. **Debrief after the session**: what felt controlled versus what felt rushed or unclear, and what to focus on next — the ABANA-style lesson progression (Section 10.3) is deliberately built around this kind of incremental, reflective skill-building rather than jumping straight to complex projects.

## Confidence Assessment Summary

**Overall confidence: 82%.**

- **Forging technique, tool lists, and heat-treatment fundamentals (Parts 1–7)**: 85–88% confidence. Backed by a complete, field-tested FAO Agricultural Engineering Service training manual purpose-written for scrap-material, non-electrified smithing, cross-checked against the modern ABANA hobbyist curriculum and independent metallurgical references for temperature/color and quenching data.
- **Steel identification via spark testing**: ~70% confidence in the *method's precision* specifically — explicitly presented here as a screening tool with well-documented, source-acknowledged limitations, not a definitive alloy test.
- **Zone 5-specific fuel/material sourcing**: no land-grant extension program exists for this craft (unlike wool, maple syrup, or fiber crops), so this guide relies on general market/regional generalization rather than a single authoritative regional study. This is disclosed rather than hidden.
- **Machine-tool section (pole/treadle lathes, mechanical advantage)**: ~75% confidence — a niche craft-revival area with fewer independent contemporary sources than the core forging content, though the underlying physics (mechanical advantage) is well-established textbook material.
- **Cost figures**: 2026 USD, drawn from multiple current retail/hobbyist-market sources; expect real-world variation based on region and used-vs-new sourcing decisions.

**Gaps for future research**: this guide does not cover welding (arc/oxy-acetylene) as a distinct skill set, casting/foundry work, or gunsmithing-adjacent metalwork — each is a substantial enough domain to merit separate treatment. It also does not cover the specific mineralogy of locating and smelting bog iron or other primary ore sources — this guide assumes scrap-steel sourcing rather than ore reduction, which is the practically relevant assumption for a Zone 5 household today but would need separate research for a "from raw ore" resilience scenario.

---

## Sources

1. The Crucible. *Blacksmithing Forge 101: How To Make Forges At Home*. [https://www.thecrucible.org/guides/blacksmithing/blacksmithing-forge/](https://www.thecrucible.org/guides/blacksmithing/blacksmithing-forge/)

2. RECOIL OFFGRID. *Learn How To Build Your Own Forge*. [https://www.offgridweb.com/preparation/build-your-own-blacksmithing-forge/](https://www.offgridweb.com/preparation/build-your-own-blacksmithing-forge/)

3. Instructables. *Mobile Coal Forge Build*. [https://www.instructables.com/Coal-Forge-Build/](https://www.instructables.com/Coal-Forge-Build/)

4. ABANA (Artist-Blacksmith's Association of North America). [https://abana.org/](https://abana.org/)

5. ABANA / The Guild of Metalsmiths. *Controlled Hand Forging Study Guide*. [https://www.metalsmith.org/wp-content/uploads/2020/03/TGOM-ABANA-Controlled-Hand-Forging-Study-Guide-Print-File-1-24-20.pdf](https://www.metalsmith.org/wp-content/uploads/2020/03/TGOM-ABANA-Controlled-Hand-Forging-Study-Guide-Print-File-1-24-20.pdf)

6. ABANA Controlled Hand Forging series, Lesson One: Drawing Out. [https://www.ocblacksmith.com/ABANAControlledHandForging.pdf](https://www.ocblacksmith.com/ABANAControlledHandForging.pdf)

7. Stokes, J.B. *Advanced Blacksmithing: A Training Manual*. FAO Agricultural Services Bulletin M-07, Food and Agriculture Organization of the United Nations, 1992. [https://openknowledge.fao.org/server/api/core/bitstreams/f0dbf46e-9bc3-4a3d-a5d4-28df3d15649b/content](https://openknowledge.fao.org/server/api/core/bitstreams/f0dbf46e-9bc3-4a3d-a5d4-28df3d15649b/content)

8. Service Steel. *Steel Temper Colors: Explanation & Chart*. [https://www.servicesteel.org/resources/steel-tempering-colors](https://www.servicesteel.org/resources/steel-tempering-colors)

9. MachineMFG. *Steel Temperature Color Chart: A Complete Comparison*. [https://www.machinemfg.com/temperature-and-color-chart/](https://www.machinemfg.com/temperature-and-color-chart/)

10. Knifemaking.com. *Forging Steel Heat & Color Chart*. [https://knifemaking.com/pages/forging-steel-heat-color-chart](https://knifemaking.com/pages/forging-steel-heat-color-chart)

11. West Yorkshire Steel. *Steel Hardening & Forging Temperatures | Colour Chart*. [https://www.westyorkssteel.com/technical-information/steel-heat-treatment/hardening-temperatures/](https://www.westyorkssteel.com/technical-information/steel-heat-treatment/hardening-temperatures/)

12. Orchard Blacksmith. *Choosing the Right Anvil: Types, Sizes, and What to Look For*. [https://www.orchardblacksmith.com/blog/choosing-the-right-anvil-types-sizes-and-what-to-look-for](https://www.orchardblacksmith.com/blog/choosing-the-right-anvil-types-sizes-and-what-to-look-for)

13. Anvilfire.com. *Selecting an Anvil: Which is right for you?*. [https://www.anvilfire.com/21centbs/Selecting-an-Anvil.php](https://www.anvilfire.com/21centbs/Selecting-an-Anvil.php)

14. IspatGuru. *Spark Testing of Steels*. [https://www.ispatguru.com/spark-testing-of-steels/](https://www.ispatguru.com/spark-testing-of-steels/)

15. Tharwa Valley Forge. *Recycled Steel identification*. [https://www.tharwavalleyforge.com/articles/reference/46-recycled-steel-identification](https://www.tharwavalleyforge.com/articles/reference/46-recycled-steel-identification)

16. Wasatch Steel. *Basics on the Spark Test for Steel and Other Metals*. [https://www.wasatchsteel.com/basics-on-the-spark-test-for-steel-and-other-metals/](https://www.wasatchsteel.com/basics-on-the-spark-test-for-steel-and-other-metals/)

17. Make It From Metal. *Where to Find High Carbon Steel Scrap*. [https://makeitfrommetal.com/where-to-find-high-carbon-steel-scrap/](https://makeitfrommetal.com/where-to-find-high-carbon-steel-scrap/)

18. Make It From Metal. *How to Check the Hardness of Metal: A Complete Guide*. [https://makeitfrommetal.com/how-check-the-hardness-of-metal-a-complete-guide/](https://makeitfrommetal.com/how-check-the-hardness-of-metal-a-complete-guide/)

19. I Forge Iron forum. *Leaf spring steel ID*. [https://www.iforgeiron.com/topic/19127-leaf-spring-steel-id/](https://www.iforgeiron.com/topic/19127-leaf-spring-steel-id/)

20. Red Label Abrasives. *How to Heat Treat a Knife | Easiest 4-Step Method*. [https://www.redlabelabrasives.com/blogs/news/how-to-heat-treat-a-knife](https://www.redlabelabrasives.com/blogs/news/how-to-heat-treat-a-knife)

21. Knife Steel Nerds. *Which Quenching Oil is Best for Knives?*. [https://knifesteelnerds.com/2021/07/19/which-quenching-oil-is-best-for-knives/](https://knifesteelnerds.com/2021/07/19/which-quenching-oil-is-best-for-knives/)

22. HubPages. *Basic Blacksmithing: Is Coal, Charcoal, or Propane Best for Forge Fuel*. [https://discover.hubpages.com/art/Basic-Blacksmithing-coal-charcoal-or-propane-for-forge-fuel](https://discover.hubpages.com/art/Basic-Blacksmithing-coal-charcoal-or-propane-for-forge-fuel)

23. Small Farmer's Journal. *Choosing a Gas or Coal Forge for the Small Farm Shop*. [https://smallfarmersjournal.com/choosing-a-gas-or-coal-forge-for-the-small-farm-shop/](https://smallfarmersjournal.com/choosing-a-gas-or-coal-forge-for-the-small-farm-shop/)

24. Working the Flame. *Best Types of Blacksmith Hammers (Pros, Cons & Uses)*. [https://workingtheflame.com/blacksmith-hammer-guide/](https://workingtheflame.com/blacksmith-hammer-guide/)

25. Gallivanting Craftsman. *No Bullshit Guide To The Top 10 Blacksmithing Hammers*. [https://gallivantingcraftsman.com/guide-to-the-top-10-blacksmith-hammers/](https://gallivantingcraftsman.com/guide-to-the-top-10-blacksmith-hammers/)

26. Hackaday. *Blacksmithing For The Uninitiated: Hammer And Tongs*. [https://hackaday.com/2019/05/09/blacksmithing-for-the-uninitiated-hammer-and-tongs/](https://hackaday.com/2019/05/09/blacksmithing-for-the-uninitiated-hammer-and-tongs/)

27. Blacksmiths Depot. *Essential Blacksmithing Tools & Their Uses*. [https://blacksmithsdepot.com/blog/post/essential-blacksmithing-tools-and-their-uses](https://blacksmithsdepot.com/blog/post/essential-blacksmithing-tools-and-their-uses)

28. Breakthrough Blacksmithing. *Forge with Confidence: Essential Blacksmithing Safety Guidelines*. [https://breakthroughblacksmithing.wordpress.com/2023/08/08/forge-with-confidence-essential-blacksmithing-safety-guidelines/](https://breakthroughblacksmithing.wordpress.com/2023/08/08/forge-with-confidence-essential-blacksmithing-safety-guidelines/)

29. Breakthrough Blacksmithing. *Forge Ahead Safely: Essential Precautions for Blacksmithing in the Workshop*. [https://breakthroughblacksmithing.wordpress.com/2023/10/21/forge-ahead-safely-essential-precautions-for-blacksmithing-in-the-workshop/](https://breakthroughblacksmithing.wordpress.com/2023/10/21/forge-ahead-safely-essential-precautions-for-blacksmithing-in-the-workshop/)

30. Air Control Industries. *The Evolution of the Blacksmith Forge Fan — Lungs, Bellows & Blowers*. [https://www.aircontrolindustries.com/us/blacksmith-forge/evolution-of-forge-fan/](https://www.aircontrolindustries.com/us/blacksmith-forge/evolution-of-forge-fan/)

31. Centaur Forge. *Hand Crank & Electric Blacksmith Forge Blowers*. [https://www.centaurforge.com/Forge-Blowers/products/169/](https://www.centaurforge.com/Forge-Blowers/products/169/)

32. Open Source Ecology. *Village Construction Set*. [https://wiki.opensourceecology.org/wiki/Village_Construction_Set](https://wiki.opensourceecology.org/wiki/Village_Construction_Set)

33. IRC (International Water and Sanitation Centre). *Village Technology Handbook* (VITA). [https://www.ircwash.org/resources/village-technology-handbook](https://www.ircwash.org/resources/village-technology-handbook)

34. Garrett Wade. *Using Sharpening Stones*. [https://garrettwade.com/blogs/blog/sharpening-woodworking-edge-tools/](https://garrettwade.com/blogs/blog/sharpening-woodworking-edge-tools/)

35. Chubo Knives. *How to Sharpen a Knife with a Stone: Grit, Maintenance & More*. [https://www.chuboknives.com/blogs/news/how-to-sharpen-knife-with-stone](https://www.chuboknives.com/blogs/news/how-to-sharpen-knife-with-stone)

36. Farmstand App. *7 Approaches to Sharpening Garden Tools That Extend Their Lifespan*. [https://www.farmstandapp.com/65165/7-approaches-to-sharpening-garden-tools/](https://www.farmstandapp.com/65165/7-approaches-to-sharpening-garden-tools/)

37. World Backyard. *Knife Steel Composition Table Explained*. [https://www.worldbackyard.com/knife-steel-composition-table-explained/](https://www.worldbackyard.com/knife-steel-composition-table-explained/)

38. BladeForums. *1084 vs 1095, 5160, O1, etc.*. [https://www.bladeforums.com/threads/1084-vs-1095-5160-o1-etc.781576/](https://www.bladeforums.com/threads/1084-vs-1095-5160-o1-etc.781576/)

39. BladeForums. *Proper way to perform a "file test"*. [https://www.bladeforums.com/threads/proper-way-to-perform-a-file-test.890795/](https://www.bladeforums.com/threads/proper-way-to-perform-a-file-test.890795/)

40. Sharpening Made Easy. *Steels Used By Knife Makers*. [https://sharpeningmadeeasy.com/steels.htm](https://sharpeningmadeeasy.com/steels.htm)

41. Wikipedia. *Simple machine*. [https://en.wikipedia.org/wiki/Simple_machine](https://en.wikipedia.org/wiki/Simple_machine)

42. Wikipedia. *Mechanical advantage*. [https://en.wikipedia.org/wiki/Mechanical_advantage](https://en.wikipedia.org/wiki/Mechanical_advantage)

43. Wikipedia. *Pole lathe*. [https://en.wikipedia.org/wiki/Pole_lathe](https://en.wikipedia.org/wiki/Pole_lathe)

44. Hackaday. *Building A Treadle Powered Lathe*. [https://hackaday.com/2013/06/04/building-a-treadle-powered-lathe/](https://hackaday.com/2013/06/04/building-a-treadle-powered-lathe/)

45. Open Source Machine Tools. *Make Your Own Treadle Lathe*. [http://www.opensourcemachinetools.org/archive-manuals/treadle_lathe.pdf](http://www.opensourcemachinetools.org/archive-manuals/treadle_lathe.pdf)

46. Renaissance Woodworker. *Foot-Powered Wood Turning*. [https://www.renaissancewoodworker.com/foot-powered-wood-turning/](https://www.renaissancewoodworker.com/foot-powered-wood-turning/)

47. Begin To Black Smith. *How Much Does It Cost to Begin Blacksmithing*. [https://begintoblacksmith.com/how-much-does-it-cost-to-begin-blacksmithing/](https://begintoblacksmith.com/how-much-does-it-cost-to-begin-blacksmithing/)

48. Homestead Heritage Forge. *Setting up a Home Blacksmith Shop*. [https://www.homesteadheritageforge.com/articles/setting-up-shop/](https://www.homesteadheritageforge.com/articles/setting-up-shop/)

49. Oldboy Metal Co. *Starting a Forge at Home: The 5 Tools You Actually Need*. [https://oldboymetal.com/blogs/notes-from-the-forge-new-tricks-from-oldboy/starting-a-forge-at-home-the-5-tools-you-actually-need-where-to-spend-where-to-save-and-how-to-do-it-for-around-1000](https://oldboymetal.com/blogs/notes-from-the-forge-new-tricks-from-oldboy/starting-a-forge-at-home-the-5-tools-you-actually-need-where-to-spend-where-to-save-and-how-to-do-it-for-around-1000)

50. The Indy Forge (community blacksmith makerspace/co-op). [https://theindyforge.com/](https://theindyforge.com/)

51. Mill Forge Makerspace. [https://millforge.org/](https://millforge.org/)

52. Past Lives Makerspace — Metal Shop and Metalworkers Guild. [https://www.pastlives.space/blacksmiths-welders](https://www.pastlives.space/blacksmiths-welders)

53. WC Safety. *Guide to Safety Glasses Standards — ANSI Z87.1 Explained*. [https://wcsafety.com/blogs/reference/ansi-z87-1-explained](https://wcsafety.com/blogs/reference/ansi-z87-1-explained)

54. Paulson Manufacturing. *Understanding ANSI Z87.1: Primary vs. Secondary Eye Protection*. [https://www.paulsonmfg.com/blog/understanding-ansi-z87-1-primary-vs-secondary-eye-protection/](https://www.paulsonmfg.com/blog/understanding-ansi-z87-1-primary-vs-secondary-eye-protection/)

55. Wikipedia. *Blacksmith*. [https://en.wikipedia.org/wiki/Blacksmith](https://en.wikipedia.org/wiki/Blacksmith)

---

*This guide is part of the Open-Repo resilience knowledge base, Phase 5.2, Wave 4. See related guides in the frontmatter above for adjacent domains.*
