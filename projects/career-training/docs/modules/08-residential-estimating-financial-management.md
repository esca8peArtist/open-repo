---
title: "Residential GC: Estimating, Bidding, and Financial Management"
module: 08
discipline: ["estimating", "financial-management", "contracts", "cash-flow"]
audience: "New residential GC — construction-experienced, new to business/financial side"
status: "reference"
tags: [career-training, residential, estimating, bidding, financial-management, cash-flow, change-orders]
created: 2026-05-12
---

# Module 08 — Residential GC: Estimating, Bidding, and Financial Management

> **Scope.** This is the business-side reference for a residential general contractor — single-family new construction, custom homes, and substantial remodels in California. You already know how to swing a hammer and read a plan. What you need now is the discipline to **price work correctly, win the right jobs, get paid on time, and not go broke between draws.** Numbers in this document are California-biased; adjust productivity and rates to your market.
>
> The single most important sentence in this entire module: **profit is what's left after every cost is captured. If you don't capture a cost in the estimate, you don't earn profit on it — you donate it.**

---

## 1. Estimating Fundamentals

### 1.1 The four cost layers in a bid

Every dollar in a residential bid lives in one of four buckets. Confusing them is the most common cause of money-losing jobs.

| Layer | Definition | Examples | Where it lives in the bid |
|---|---|---|---|
| **Direct costs** | Costs of physically building the work — materials installed in place and the labor that installs them, or sub bids that include both. | Concrete, lumber, drywall, electrician sub bid, framing crew labor + burden | "Trade" lines, one per CSI division or trade |
| **General conditions (GCs)** | Project-specific costs to run *this* job that aren't trade work. Goes away when the job ends. | Super salary, dumpster, port-o-let, temp power, site protection, project clean | "General Conditions" or "Project Indirect" section |
| **Overhead (OH)** | Company-wide costs to keep the doors open. Exists whether you have one job or ten. | Office rent, estimator salary, your truck, insurance premiums, accounting, software | A % applied to (Direct + GC) — usually 10–15% |
| **Profit (P)** | What's left for the owner of the business — return on capital and risk. | The reason you took the job | A % applied to (Direct + GC + OH) — usually 8–15% net target |

**How the layers flow into a final number** (pure-multiplier method, simplest):

```
Direct Costs                 $ 800,000
+ General Conditions           $  80,000   (~10% of direct)
─────────────────────────
Project Cost of Work          $ 880,000
× (1 + Overhead %)             × 1.12      (12% OH)
─────────────────────────
Burdened Cost                 $ 985,600
× (1 + Profit %)               × 1.10      (10% profit)
─────────────────────────
Sell Price to Owner           $1,084,160
```

> **Critical distinction — markup vs. margin.** A 20% markup on $880K = $176K added on top = $1,056K sell price. The *margin* on that $1,056K is only 16.7%, not 20%. If you want a 20% **margin** (i.e. 20% of the sell price is profit-and-overhead), divide by 0.80, don't multiply by 1.20. Many new GCs lose 3–4 points on every job by confusing these. Per Siana Marketing benchmarks, well-managed GCs net 5–7% pre-tax; markup must reach 20–30% to deliver that net after overhead. ([Siana Marketing, 2026][siana])

### 1.2 The estimating process — step by step

| Step | Activity | Output | Time as % of total estimate |
|---|---|---|---|
| 1 | **Scope review** | Read the contract docs front-to-back. Make a one-page "what is this job" memo. | 5% |
| 2 | **Drawings takeoff** | Quantify everything you'll self-perform. For subbed trades, quantify only enough to sanity-check sub bids. | 25% |
| 3 | **Sub solicitation** | Send bid packages to 3+ subs per trade. Set bid-due date 1 week before owner's deadline. | 5% (clock time large) |
| 4 | **Sub bid leveling** | Spread sub bids on a leveling sheet trade-by-trade. Find scope gaps and exclusions. | 15% |
| 5 | **Self-perform pricing** | Price your own labor + material for what you self-perform (often supervision + carpentry + punch). | 15% |
| 6 | **GC costs** | Build the general-conditions section line by line, by week of duration. | 10% |
| 7 | **Markup** | Apply overhead and profit to (Direct + GC). | 2% |
| 8 | **Final check** | One person who didn't price it reviews the summary, exclusions, and totals. | 8% |
| 9 | **Bid form & cover letter** | Format the bid for the owner: summary, exclusions, allowances, alternates, schedule. | 15% |

**Rule of thumb:** if you can't spend at least 40 hours on an estimate for a $1M custom home, decline to bid. Cheap estimates produce expensive jobs.

### 1.3 Reading drawings for takeoff (quantity extraction, not design)

You are not the architect. Your job during takeoff is to **convert lines on paper into countable units of work.** Drawings to read, in order:

| Sheet set | What you pull off | Watch out for |
|---|---|---|
| **A-0 cover / general notes** | Code basis, occupancy, fire rating, project area | "Refer to specifications" — pull specs separately |
| **Civil (C sheets)** | Grading cut/fill CY, paving SF, utilities LF, retaining wall LF & height | Property line vs. limit of work — what's in the contract? |
| **Architectural plans (A-1xx)** | Room SF, floor area, wall LF, openings count | Match plan + RCP + elevations; one will lie |
| **Architectural elevations & sections (A-2xx, A-3xx)** | Roof slope, building height, exterior cladding SF | Hidden bulkheads, soffits, mechanical chases |
| **Door/window/finish schedules** | Each-counts of openings, finish SF by room | Schedule mismatch with plan — note for RFI |
| **Structural (S sheets)** | Concrete CY, rebar LB, structural steel TN, framing BF | Hold-downs, hardware, special inspection notes |
| **MEP (M/E/P sheets)** | Fixture counts, panel sizes, duct LF | Lots of "see specs" — verify scope is in sub bid |

**Takeoff hygiene:**
- Use color highlighters on a printed set as you count (or digital overlay in Bluebeam / PlanSwift). Each color = one trade. Cross out as you count.
- Quantify in the units the trade uses, not what looks easy. Drywall in **sheets**, not SF. Concrete in **CY**, not LF.
- Round up, never down. A partial sheet is a whole sheet.
- Always write the **page reference** next to every quantity on your takeoff sheet — when something is wrong later you need to find it.

### 1.4 Quantity takeoff units by trade

| Trade | Primary unit(s) | Secondary units | Notes |
|---|---|---|---|
| **Site / excavation** | CY (cut/fill, bank vs. compacted) | LF trench, SF clearing | Bank yards × 1.25 ≈ loose yards |
| **Concrete — foundations** | CY of concrete + LB of rebar | LF of footing, EA of anchor bolts | Per 2024 ConcreteCalcs guidance, add 5–10% waste for slabs (8–10% standard) ([NCA waste-factor guidance][nca]) |
| **Concrete — slab on grade** | SF + thickness → CY | LF of edge form, SF of vapor barrier | Don't forget thickening at bearing walls |
| **Concrete — grade beam / pier** | LF × cross-section → CY | EA of piers | Pumping vs. chute is a labor swing |
| **Masonry (CMU, brick)** | SF wall area | EA of openings, LF of bond beam | Block: ~1.125 block/SF of 8×16 wall |
| **Rough framing** | BF (board feet) of lumber + sheet count of OSB/ply | LF of plates, EA of joists/headers, EA of hardware | 1 BF = 1″ × 12″ × 12″. Walls ≈ 6–8 BF/SF of wall. House overall ≈ 8–12 BF/SF of floor |
| **Roofing** | Squares (1 sq = 100 SF) | LF of ridge, hip, valley, eave, rake; EA of pipe flashings | Add 10% for cuts on hips/valleys; 15% on complex roofs |
| **Windows / doors** | EA, by size and type | LF of trim, EA of hardware sets | Always confirm rough opening vs. unit size |
| **Insulation** | SF of wall/ceiling by R-value | LF of rim joist | Match Title 24 compliance form |
| **Drywall** | Sheets (typ. 4×8 = 32 SF or 4×12 = 48 SF) | LF of corner bead, gallons of compound | One bucket of compound ≈ 12 sheets hung + finished |
| **Painting** | SF per coat by surface | EA of doors, LF of trim | Smooth wall ≈ 350 SF/gal; textured ≈ 250 SF/gal. Bedrooms: ~1.5× floor area in wall+ceiling SF |
| **Flooring — wood** | SF + species/grade | LF of base, EA of transitions | Add 7–10% waste |
| **Flooring — tile** | SF | LF of bullnose, EA of accessories | **10% waste field cuts, 15% diagonal, 20% mosaic** ([BuildItCalc][bldc]) |
| **Cabinetry / millwork** | LF of base + LF of upper + EA of tall | SF of countertop | Spec sheet drives more than takeoff |
| **Plumbing** | Fixture count (sinks, WC, tub, shower) | LF of supply / DWV pipe, EA of valves | Fixture units drive sub bid more than LF |
| **HVAC** | EA of equipment (furnace, AC, ERV) | Tons of cooling, LF of duct, EA of registers | Manual J/D should be in design |
| **Electrical** | EA of panel/devices/fixtures | LF of feeder, EA of circuits | Service size is the single biggest cost driver |
| **Stucco / siding** | SF | LF of trim/reveals | Add 10% for cuts and corners |
| **Landscape / hardscape** | SF of plant beds, SF of paving, EA of trees | LF of fence, LF of irrigation main | Usually deferred or owner-direct on residential |

### 1.5 Labor productivity rates — California residential norms

Use these as **starting points only.** Your own field data from completed jobs is gold; published rates from RSMeans, NCE, BNI are silver. ([Construction Bids AI productivity guide][cbai])

| Trade task | Unit | Productivity (man-hours per unit) | Crew |
|---|---|---|---|
| Excavation by hand | CY | 1.0–2.0 | 1 laborer |
| Set forms — strip footing | LF | 0.10–0.15 | 2-person form crew |
| Place + finish slab on grade | CY | 1.5–2.5 | 4-person crew (placer, 2 finishers, helper) |
| Frame exterior wall, 2×6 @ 16″ | SF of wall | 0.04–0.06 | 2 framers |
| Frame floor (joist + sheathing) | SF | 0.04–0.05 | 2 framers |
| Frame roof, complex hip/valley | SF of roof | 0.08–0.12 | 3 framers |
| Install asphalt shingles | Square | 1.5–2.5 | 2-person roofing crew |
| Hang drywall, walls + ceiling | Sheet | 0.5–0.75 | 2 hangers (≈ 30–45 sheets/day per pair) |
| Tape & finish drywall, level 4 | Sheet | 1.0–1.5 | 2 tapers |
| Paint walls — 2 coats roller | SF | 0.005–0.008 | 1 painter |
| Install tile, 12×12 straight set | SF | 0.10–0.15 | 1 tile setter + helper |
| Install hardwood flooring | SF | 0.08–0.12 | 2 installers |
| Set interior door, prehung | EA | 0.75–1.5 | 1 carpenter |
| Run plumbing rough, per fixture | EA fixture | 4–8 | 1 plumber + helper |
| Run electrical rough, per device | EA device | 0.5–1.0 | 1 electrician |

**Converting productivity to labor cost:**

```
Labor hours      = Quantity × Productivity rate
Labor cost (raw) = Labor hours × Wage rate
Labor cost (burdened) = Labor cost × (1 + burden factor)
```

**Burden factor in California** for a residential carpenter ≈ **35–55%** of base wage. Includes:
- FICA (7.65%) + FUTA + SUTA (~1–6%)
- Workers' comp (CA carpentry ~$8–18 per $100 of payroll, i.e. 8–18%)
- General liability allocation (1–3%)
- Health insurance & paid time off if you offer them (5–15%)
- Vacation, holidays, sick pay if salaried

If you pay a framer $35/hr, plan on $50–55/hr burdened cost. Apply a productivity allowance (1.15–1.25×) for breaks, setup, cleanup, and non-productive time — the productivity rate above assumes "on tools" hours. ([Construction Bids AI][cbai])

---

## 2. Sub Bid Process

### 2.1 The bid package — what you send to subs

A complete bid package contains six things. Subs who say "just call me with the scope" produce bids that turn into change orders.

| Element | Contents | Why it matters |
|---|---|---|
| **Invitation to bid (cover letter)** | Project name, location, GC contact, bid due date/time, scope of trade, mandatory site walk date, who's bonded | Sets expectation that this is a competitive solicitation |
| **Scope of work narrative** | 1–3 pages: what's in, what's out, who furnishes what (FBO/IBO matrix), interfaces with adjacent trades | Eliminates "I didn't think that was mine" |
| **Drawings & specs** | Full set or trade-relevant sheets only (be consistent — full set is safer) | Sub needs to see the whole building, not just their sheet |
| **Bid form / proposal form** | Pre-formatted: base bid, unit prices, alternates, allowances, durations, exclusions section | Forces apples-to-apples comparison |
| **Bid leveling instructions** | "Include X. Exclude Y. Price alternates Z. List clarifications." | Disciplines the bidder |
| **Subcontract template** | The agreement they'll sign if awarded — they should price the indemnity / insurance / payment terms before bidding | No surprises at award |

### 2.2 Solicitation strategy

| Decision | Best practice |
|---|---|
| **How many bids per trade?** | Target **3 bids, accept 2 minimum.** With one bid you have no market check; with five you're wasting subs' time and they'll stop bidding you. |
| **Preferred sub list** | Maintain a short list of 5–8 known subs per trade. Rank A (always invite), B (invite when A is busy), C (probationary). Move subs up/down based on each job's performance. |
| **Bid day management** | Bids due 48–72 hours before your bid to the owner. This is when scope gaps surface and you need time to resolve. |
| **Coverage** | If you have a "house" sub (favorite electrician), get 1 outside bid as a sanity check even if you intend to award to your house. |
| **Site walks** | For remodels, **mandatory site walk** — no walk, no bid. Cuts post-award "I didn't see that" claims dramatically. |

### 2.3 Bid leveling — the spreadsheet that saves your job

Put every sub bid for a trade on one row. Compare:

| Line | Sub A | Sub B | Sub C | Notes |
|---|---|---|---|---|
| Base bid | $48,200 | $52,000 | $44,500 | C looks low — why? |
| Includes permit? | Yes | Yes | **No** | Add $850 to C |
| Includes dumpster for trade waste? | Yes | No | No | Add $400 to B & C |
| Includes cleanup of own work? | Yes | Yes | Yes | — |
| Includes temp protection of adjacent? | No | Yes | No | Add $300 to A & C |
| Schedule duration | 3 wk | 4 wk | 3 wk | B is a week slower |
| Insurance limits meet our req? | Yes | Yes | **No** ($1M/$2M vs. $2M/$4M req'd) | Add $400 to C for rider |
| Bonded? | Yes | No | Yes | Risk note |
| **Leveled price** | $48,500 | $52,400 | $46,150 | C still low but real |

**The seven things most often missing from sub bids** (always check explicitly):

1. **Cleanup of their own trade debris** — many subs leave it for "the GC."
2. **Dumpster usage** — they assume yours is free; price how often they fill it.
3. **Temporary utilities** — power for tools, water, lighting after dark.
4. **Permits and plan check fees** — assume *not* included unless stated.
5. **Protection of adjacent work** — floor protection, dust walls, masking.
6. **Hoisting / lifting equipment** — boom truck, scissor lift, crane time.
7. **Testing and inspection** — concrete cylinder breaks, compaction, special inspection.

### 2.4 Scope gaps and overlaps — the #1 source of change orders

A **gap** is work no sub bid because each thought another would. An **overlap** is work two subs both bid (less expensive but creates conflict at award).

Common gaps in residential:

| Gap | Trade A | Trade B | Resolve to |
|---|---|---|---|
| Backing for grab bars, TV mounts, cabinets | Framer | Drywaller | Framer (specify in framing scope) |
| Backing for towel bars / accessories | Tile setter | Plumber | Framer pre-tile (call out by location) |
| Caulking between tile and tub | Tile | Plumber | Tile setter (or punch) |
| Final connection of appliances | Plumber | GC / homeowner | Specify by appliance in plumb scope |
| Smoke / CO detector wiring vs. install | Electrician | Carpenter | Electrician — including battery backup |
| Door hardware install (after paint) | Carpenter | Painter | Carpenter post-paint (separate trip) |
| Floor underlayment | Flooring | Carpenter | Flooring sub (single-source the floor system) |
| Punch list paint touchup | Painter | GC | Painter — one return trip in base bid |
| Final clean after punch | Cleaning sub | GC | GC GC (general conditions) |

**Find gaps before award.** A 30-minute "scope review meeting" with the apparent low bidder *before* writing the contract is the cheapest insurance you'll ever buy.

### 2.5 Award criteria beyond price

Lowest price ≠ best value. Score apparent low bidders on:

| Factor | Weight (typ.) | Red flags |
|---|---|---|
| Price | 50% | More than 15% below mean of bids = re-verify scope |
| Schedule reliability (track record) | 15% | "We can start tomorrow" on a busy market = capacity question |
| Quality track record | 15% | Won't give 3 recent references = pass |
| Bonding capacity / financial strength | 10% | Can't get sub bond, can't show insurance certs = liquidity risk |
| Insurance (limits, additional insured, waiver of subro) | 5% | Won't name you AI = no contract |
| Cash flow needs | 5% | Demands deposit, wants weekly pay = thin balance sheet |

### 2.6 Subcontract essentials

At minimum, every sub contract must have:

| Clause | What it must say |
|---|---|
| **Scope** | Reference the bid documents AND a positive list of inclusions AND a list of exclusions |
| **Price & basis** | Lump sum, unit price, or T&M with NTE — be explicit |
| **Schedule** | Start date / NTP, milestones, completion date, liquidated damages if any |
| **Insurance** | Min limits, naming GC and owner as additional insured, waiver of subrogation, primary & non-contributory |
| **Payment terms** | Pay-when-paid or pay-if-paid (CA enforces pay-when-paid only as a timing mechanism, not a condition), retention %, lien waiver requirement at each pay app |
| **Lien waivers** | Conditional progress with each pay app, unconditional progress with proof of prior payment, conditional/unconditional final with final pay |
| **Change orders** | Written, signed CO required before extra work; T&M ticket procedure; markup % |
| **Warranty** | 1 year minimum on workmanship; pass-through manufacturer warranties; warranty start = substantial completion |
| **Indemnity** | Type I (broad), Type II (intermediate), or Type III (limited) — California Civil Code §2782 prohibits indemnification of GC's sole negligence on residential |
| **Termination** | For cause (default + cure period) and for convenience (with stated costs payable) |

---

## 3. General Conditions Pricing

### 3.1 General conditions vs. overhead — the dividing line

**General conditions** = costs that exist *because of this project*. They go away when the project ends.
**Overhead** = costs that exist *because the company exists*. They continue whether or not this job runs.

A simple test: "If I didn't have this project, would I still pay for this?" Yes → overhead. No → general conditions.

| Cost item | GC or OH? | Why |
|---|---|---|
| Superintendent on this job | GC | Project-specific |
| Office estimator | OH | Bids other jobs too |
| Site trailer rent | GC | This site |
| Office rent | OH | Company HQ |
| Project manager 50% allocated | Mostly GC (allocate by %) | The 50% on this job is GC; the rest is OH |
| Project-specific liability insurance | GC | Job-specific premium |
| Annual umbrella & GL policy | OH | Covers company |
| Job dumpster | GC | This job's waste |
| Company truck (your daily) | OH | Drives to multiple jobs |
| Site truck assigned to this job | GC | Stays on this site |

### 3.2 Typical GC general conditions line items — California residential

Build general conditions by listing every line, pricing each by unit and duration. Example for a 10-month $1.2M custom home in coastal California:

| Line item | Unit / basis | Quantity | Rate | Cost |
|---|---|---|---|---|
| Superintendent labor | Weeks @ burdened salary | 44 wk | $2,800/wk | $123,200 |
| Project manager (allocated 25%) | Weeks @ 25% of salary | 44 wk | $1,000/wk | $44,000 |
| Temporary power (pole, meter, monthly) | Setup + months | 1 + 10 mo | $1,500 + $250 | $4,000 |
| Temporary water | Hookup + months | 1 + 10 | $400 + $80 | $1,200 |
| Temporary toilet (1 ADA, 1 standard) | Months × units | 10 × 2 | $180 ea/mo | $3,600 |
| Site fence (6′ chain link, 200 LF) | Setup + months | 1 setup + 10 mo | $1,500 + $200 | $3,500 |
| Site trailer / job box | Months | 10 | $450 | $4,500 |
| Job signage | EA | 1 | $400 | $400 |
| Dumpsters (20-yd, # of pulls) | Pulls | 18 | $650 | $11,700 |
| Temporary protection (floor, dust walls) | LS by phase | 1 | $4,500 | $4,500 |
| Small tools & consumables | % of direct labor | 1.5% of $200K self-perform | — | $3,000 |
| Safety program (PPE, training, signs, FA kit) | LS | 1 | $2,500 | $2,500 |
| Permits (building, MEP — when GC-paid) | % of valuation or fixed | — | — | $9,800 |
| Survey & layout | LS | 1 | $3,500 | $3,500 |
| Soils testing & compaction | LS | 1 | $2,800 | $2,800 |
| Concrete cylinder breaks / special inspect | LS | 1 | $1,800 | $1,800 |
| Final clean | SF | 4,500 SF | $0.45/SF | $2,025 |
| Construction photography | Monthly | 10 | $100 | $1,000 |
| Builder's risk insurance (this job) | % of value | 0.15% × $1.2M | — | $1,800 |
| GC vehicle / fuel allocation | Weeks | 44 | $150 | $6,600 |
| **Total general conditions** | | | | **$235,425** |

That's about **8.4% of a $2.8M sell price** — typical for this scale. Per Bridgit / SmartBarrel benchmarks, residential GC general conditions normally fall in **5–15% of total project cost**, with 8–12% as the sweet spot. ([Bridgit GC guide][bridgit], [SmartBarrel][smbar])

### 3.3 Three ways to price general conditions

| Method | When to use | Pros | Cons |
|---|---|---|---|
| **Detailed line-item (above)** | Custom homes, GMP, cost-plus, any job > $500K | Defensible, accurate, transparent | Time-consuming |
| **Time-based (super + indirect $/wk × duration)** | Production homes with repeatable cost | Fast, easy to update with schedule slip | Misses one-time costs |
| **% of direct cost (e.g. 8–12%)** | Quick conceptual estimate, small remodels | Fastest | Inaccurate; ignores duration; loses you money on long jobs |

**Best practice:** detailed line-item for any job over $250K. Use % only for back-of-napkin checks.

---

## 4. Overhead and Profit

### 4.1 What's in overhead

| Category | Typical line items |
|---|---|
| **Office** | Rent / mortgage, utilities, internet, office supplies, cleaning |
| **People (non-billable)** | Owner salary (above what you'd pay a hired GM), bookkeeper, estimator, office admin, marketing |
| **Vehicles & equipment** | Company trucks, office laptops, small tool depreciation pool, software |
| **Insurance** | GL annual premium, umbrella, vehicle, E&O, key person life |
| **Professional services** | Accountant / CPA, attorney retainer, IT support |
| **Software & subs** | Estimating software (PlanSwift, STACK), accounting (QuickBooks, Foundation), PM (Procore, Buildertrend), takeoff |
| **Marketing / BD** | Website, ads, photography, trade shows, client gifts |
| **Licenses & dues** | CSLB renewal, NAHB, BIA, local builder association |
| **Bad debt reserve** | 0.5–2% of revenue — money you billed and won't collect |
| **Training & education** | Continuing ed for owner, super certifications, OSHA-30 |

### 4.2 Calculating your overhead rate

```
Step 1.  Total annual overhead (sum the above)         = $300,000
Step 2.  Projected annual revenue (be realistic)        = $3,000,000
Step 3.  Project annual direct cost + GC                = $2,400,000
Step 4.  Overhead rate (on direct + GC)                 = 300 / 2,400 = 12.5%
Step 5.  Apply 12.5% to every bid's (Direct + GC)
```

**Common volume / overhead bands for California residential GCs:**

| Annual revenue | Typical OH % | Comment |
|---|---|---|
| < $500K (owner-operator, no office) | 5–10% | "Office" is a kitchen table; you're an estimator and laborer |
| $500K – $2M (1 office person, super) | 10–15% | First real overhead — bookkeeper, office space |
| $2M – $10M (multiple projects, 3–8 staff) | 12–18% | Layer of management, full software stack |
| $10M+ (multi-crew, multi-PM) | 14–20% | Department heads, BD function |

Per Levelset and Builder's Book benchmarks, **10–20% overhead is the normal residential range**; some niche custom builders hit 25%. ([Levelset CA O&P][levelset])

### 4.3 Profit margin — what's realistic

| Scenario | Realistic NET profit target |
|---|---|
| Plan-built tract / production home | 4–8% |
| Mid-market spec or custom home | 8–12% |
| High-end custom home (>$500/SF) | 10–15% |
| Complex remodel (high risk, schedule uncertainty) | 12–18% |
| Owner-direct repeat client, low risk | 6–10% |
| Hard-bid against 4+ competitors | 5–8% (and you'd better win less than half) |

**Factors that move the profit number up:**

- High project complexity (more risk → more reward)
- Schedule pressure (you're earning a premium for performance)
- Sole-source / negotiated (you have pricing power)
- New client with no track record (uncertainty premium)
- Site difficulty (hillside, no access, regulated jurisdiction)
- Custom design with frequent changes likely

**Factors that push profit down:**

- Repeat owner, strong relationship, transparent books
- Cost-plus contract (less risk, less reward)
- Production work with repeatable cost
- Competitive market with strong bidders

### 4.4 The most common overhead/profit mistakes

| Mistake | Cost |
|---|---|
| Adding 10% OH + 10% profit on direct cost only, forgetting GC | Under-recovers OH on every job; 1–2% margin loss |
| Not updating overhead rate as company grows | A $1M overhead at $4M revenue is 25%; if you still bid at 12% you bleed 13% |
| Letting subs' bids "include their own profit" but not adding GC's profit on top | You earn 0 on the largest cost on the job |
| Cutting profit to win, then "making it up on changes" | Changes get scrutinized; you lose anyway |
| Adding contingency *inside* profit instead of as a line | When the contingency gets spent you have no profit left |
| Confusing markup (% added) with margin (% of sell price) | 20% markup ≠ 20% margin. See section 1.1 |

---

## 5. Bid Strategy and Presentation

### 5.1 Lump sum vs. cost-plus on residential

| Aspect | Lump sum (fixed price) | Cost-plus with fee |
|---|---|---|
| **Best for** | Clear scope, complete design, hard-bid environment | Early-design start, custom with selections-in-progress, gut renovation |
| **GC risk** | High — you eat overruns | Low — owner pays actual cost |
| **GC upside** | Keeps savings if you beat budget | Capped at fee |
| **Owner certainty** | High — knows the price | Low — open-ended |
| **Best fee structure** | Markup on (Direct + GC) | Fixed monthly fee or % of cost (typ. 12–20%) |
| **Books open?** | No, GC keeps internal cost private | Yes — transparent invoicing |

**How to present the case for cost-plus to an owner who wants lump sum:**

> "On a remodel where we'll open up walls and find unknowns, a lump sum forces me to add 15–20% contingency that you pay whether we use it or not. On cost-plus, you only pay what we actually spend, and my fee is fixed. You save money on the unknowns and you see every invoice."

### 5.2 Hard bid vs. negotiated

| Hard bid (competitive) | Negotiated (relationship) |
|---|---|
| 3+ GCs invited | Single GC selected up front |
| Lowest qualified price wins | Owner picks GC, then negotiates price |
| Lower margin (you compete) | Higher margin (you don't compete) |
| Tight scope required | Scope can evolve with design |
| Win rate: 20–35% | Win rate: 70–90% if selected |
| Best for: complete docs, price-driven owner | Best for: design-build, custom homes, return clients |

### 5.3 Presenting the estimate to the owner

The **summary** is what the owner reads. The detail is what gets you in trouble if it's too granular.

| Format | When to use | Trade-off |
|---|---|---|
| **Single number** | Tract / production homes, when contract docs fully describe scope | Owner can't see what they're paying for |
| **By phase** (sitework / foundation / framing / rough-in / finishes) | Most residential — best balance | Doesn't show trade-level detail |
| **By trade / CSI division** | Cost-plus with detailed estimate; sophisticated owner | Invites value engineering nickel-and-diming |
| **Full line-item with subs named** | Rarely — only when contractually required | Sub bids leak; subs get poached |

**Recommended residential format**: cover page summary by phase + exclusions/allowances/alternates + schedule. Detail behind that, available on request.

**Sample summary by phase:**

| Phase | Cost |
|---|---|
| Pre-construction & permits | $14,500 |
| Site work & demolition | $42,300 |
| Foundation | $78,900 |
| Framing & sheathing | $165,400 |
| Roofing | $48,200 |
| Exterior windows, doors, siding | $112,800 |
| MEP rough | $138,500 |
| Insulation & drywall | $76,200 |
| Interior finishes | $284,100 |
| Cabinetry & countertops | $98,000 |
| Flooring | $54,700 |
| Final MEP, fixtures, appliances | $87,000 |
| Exterior, landscape (allowance) | $35,000 |
| **Cost of work** | **$1,235,600** |
| General conditions (8.4%) | $103,800 |
| Contingency (3%, owner-controlled) | $40,200 |
| Overhead (12%) | $167,500 |
| Profit (10%) | $154,700 |
| **Total contract price** | **$1,701,800** |

### 5.4 Exclusions and clarifications — the most important part of the bid

**Rule: if it's not in the bid, write it as an exclusion.** If you go silent on something, you'll be expected to provide it.

Standard residential exclusion list (start here, edit per job):

- Permit fees, plan check fees, school fees, impact fees (unless explicitly included)
- Utility tap fees, water meter, sewer connection, undergrounding from pole
- Soils report, structural engineering, Title 24, energy compliance — all by owner
- Survey beyond foundation layout
- Removal of hazardous materials (lead, asbestos, mold)
- Off-site improvements (curb, gutter, sidewalk replacement) unless on plans
- Landscape, irrigation, fencing beyond limit of construction
- Appliances and FF&E (unless allowance listed)
- Window treatments
- Audio/visual, security, low-voltage beyond rough-in
- Solar (PV), battery storage
- Owner-furnished items (specify with FBO/IBO matrix)
- Premium time / overtime to recover owner-caused delays
- Builder's risk insurance (when owner-procured)
- Sales tax on owner-direct purchases
- Bonding (unless owner has requested)

### 5.5 Allowances — useful tool, frequent disappointment

An **allowance** is a placeholder $ amount for scope not yet defined (e.g. "tile allowance $8/SF installed"). Reconciled at close-out: actual cost > allowance → owner pays the delta + markup; actual < allowance → owner gets a credit.

| Best practice | Common mistake |
|---|---|
| Set allowance at realistic mid-market for the project's grade | Set low to win, then blow it on selections |
| State unit basis ("$8/SF installed including waste, setting, grout") | State only $ — fight over what's included |
| Set allowance for *one* clearly-defined category | Lump "interior finishes" into one allowance — disaster |
| Reconcile allowances in a single change order at close-out, not piecemeal | Reconcile each PO and fight every month |
| Communicate when an owner selection is over budget *before* PO | Order it, then surprise them with a CO |

Typical allowance items: flooring, tile, plumbing fixtures, lighting fixtures, appliances, cabinetry hardware, landscape.

### 5.6 Alternates

Owner can't decide if they want the $40K master bath upgrade? Bid it as an **add alternate**. Doesn't bind anyone, gives flexibility.

| Type | Use |
|---|---|
| **Add alternate** | Base bid does NOT include this scope; price to add if selected |
| **Deduct alternate** | Base bid includes; deduct if owner removes |
| **Substitution alternate** | Price difference for substituting Product B for Product A |

State each alternate's **price + schedule impact** in days. Owner has X days to accept after award; after that, price expires.

---

## 6. Contract Types on Residential

### 6.1 Comparison matrix

| Contract type | When it's right | When it's wrong | CA-specific notes |
|---|---|---|---|
| **Fixed price / lump sum** | Design 95%+ complete; clear scope; competitive market | Remodel with unknowns; early-design; "design as we go" custom | Subject to CSLB §7159 home-improvement contract requirements |
| **Cost-plus fixed fee** | Custom design-build; remodel with significant unknowns | Inexperienced owner who'll second-guess invoices | Owner has full audit rights; books must be open |
| **Cost-plus % of cost** | Same as fixed fee but for smaller / shorter jobs | Discourages efficiency (GC earns more if costs rise) — owners increasingly resist | Disclose % up front in writing |
| **Cost-plus with GMP** | Larger custom homes; design developing but ceiling defined | Very early concept work | Define inclusions/exclusions in the GMP precisely; share savings clause typical 50/50 to 75/25 owner |
| **Time & materials (T&M)** | Discovery work, small repairs, post-loss work | Anything > 2 weeks duration | Set a "not to exceed" cap; require written approval to exceed |

### 6.2 Residential contract documents — California

| Document | Use case |
|---|---|
| **AIA A105–2017** | Small/simple residential, stipulated sum, brief duration. ([AIA contract docs guide][aiaguide]) |
| **AIA A104–2017** (replaced A107) | Mid-size residential, lump sum or cost-plus, with or without GMP |
| **AIA A201** General Conditions | Reference document — incorporated by reference into A104 / A105 |
| **AIA A132 / A133** | Larger projects; CM at-risk; rare on pure residential |
| **CSLB sample home-improvement contract** | Required language for remodels (§7159) — must include 3-day right to cancel, license number, payment schedule, notice to owner |
| **Custom contract** | Most California custom-home GCs use a custom contract built on AIA bones with CA-specific addenda |

**Required clauses for California residential contracts (Bus & Prof Code §7159):**

- Contractor's name, address, license number
- Approximate start and substantial completion dates
- Plain-language description of the work
- Total contract price
- Down payment language: max 10% or $1,000, whichever is less ([CSLB §7159.5][cslb-bp])
- Schedule of progress payments tied to value of work performed
- Notice to Owner (mechanics lien warning)
- 3-day Right to Cancel (in 12-pt boldface)
- Mechanics lien warning
- CSLB contact info for complaints
- Workers' comp & liability insurance statement
- Change order procedure

### 6.3 Down payment & draw schedule — California rules

**Hard rule (BPC §7159.5):** On a home-improvement contract, the down payment may not exceed **10% of the contract price or $1,000, whichever is less.** No exceptions on remodels. ([CSLB Industry Bulletin][cslb-bp]) New construction of an owner-occupied SFD has slightly more flexibility but most GCs still operate under the 10%/$1,000 norm to avoid CSLB attention.

This is brutal for cash flow — see Section 8.

**Typical residential draw schedule** (post-down-payment, tied to value of work in place):

| Draw | Trigger | Typical % of contract |
|---|---|---|
| Down payment | Signing | 1% (max 10% / $1,000) |
| Draw 1 | Mobilization, demo, site work | 8–10% |
| Draw 2 | Foundation complete | 10–15% |
| Draw 3 | Framing & sheathing complete (dry-in) | 15–20% |
| Draw 4 | MEP rough-in & insulation | 15–20% |
| Draw 5 | Drywall complete | 10–15% |
| Draw 6 | Cabinets / interior finishes underway | 10–15% |
| Draw 7 | Substantial completion (less retainage) | 10–15% |
| Final | Punch complete, retainage release | 5–10% (retainage) |

Per ABL and Procore guidance, 5–7 draws plus a final retention release is standard. ([Procore draw schedules][procore-draw], [ABL template][abl])

**Negotiating the draw schedule:**

- Front-load if possible — mobilization + foundation should cover material deposits and the first 6 weeks of labor
- Tie draws to **completion of milestones**, not calendar dates — protects you against owner delay
- Make sure draws don't go below value-of-work-in-place at any time (the "cash negative" trap, see Section 8)
- Negotiate retainage down: 10% on first half, 5% on second half, or 5% throughout

---

## 7. Job Cost Management

### 7.1 Setting up the job cost budget

The estimate is **not** the budget. Convert it:

1. Pick a **cost code structure** and use it everywhere — estimate, accounting, POs, change orders.
2. Two common structures:
   - **Trade-based** (residential default): 01 General, 02 Sitework, 03 Concrete, 06 Framing, 07 Roofing, 09 Drywall, 09.5 Paint, 09.6 Tile, 09.7 Flooring, 11 Cabinets, 15 Plumbing, 15.5 HVAC, 16 Electrical, etc.
   - **CSI MasterFormat** (16 or 50 divisions): more granular, better for large jobs
3. Assign every estimate line to a cost code.
4. Add a buffer code (often 00.99 "Project Contingency") for the contingency line.

### 7.2 Weekly job cost report — what to look at

A working job-cost report has these columns per cost code:

| Column | Meaning |
|---|---|
| Original budget | From the estimate, locked at award |
| Approved CO budget | Owner-approved CO impact |
| **Revised budget** | Original + approved COs |
| Committed cost | Awarded sub contracts + open POs |
| Cost to date | Actually paid + accrued |
| % complete (cost) | Cost to date / revised budget |
| % complete (physical) | Field assessment of work-in-place |
| Estimate to complete (ETC) | Revised budget – cost to date, adjusted for known overruns |
| **Estimate at completion (EAC)** | Cost to date + ETC |
| **Projected variance** | Revised budget – EAC |

**The single metric that catches problems first: physical % complete < cost % complete.** Means you've spent more than you've built. Investigate.

### 7.3 Committed cost tracking

```
Committed cost = signed subcontract value + open PO value + approved sub COs
```

This is what you've **promised to spend**, even if it hasn't hit the books yet. If committed cost > revised budget on a code, you're already over — no recovery possible. **Reconcile committed vs. budget every week**, not just at month-end.

### 7.4 Change order budget impact

Maintain two CO logs:

| Log | Purpose |
|---|---|
| **Owner CO log** | All owner-facing COs: pending price, submitted, approved, rejected. Sum drives revised contract value. |
| **Sub CO log** | All sub-side COs: pending, approved. Sum drives revised committed cost. |

**Always price the sub CO before pricing the owner CO.** If your electrician charges you $4,500 for the added island circuits, your owner CO is $4,500 × (1 + OH%) × (1 + profit%) = ~$5,500. Apply your full markup to sub COs — they consume your time and risk just like base work.

### 7.5 Percent-complete and earned value (simplified for residential)

You don't need full Earned Value, but the concept matters. On each cost code:

- **Earned value** = revised budget × physical % complete
- **Cost performance index (CPI)** = earned value / cost to date
- CPI < 1.0 → over budget on that code
- CPI > 1.0 → under budget on that code

Example: framing budget $165K, physically 60% done, $115K spent.
Earned = $165K × 0.60 = $99K
CPI = 99 / 115 = 0.86 → over budget. EAC = $115K / 0.60 = $192K → projected $27K over.

### 7.6 Forecasting final cost — three methods

| Method | Formula | When to use |
|---|---|---|
| **Optimistic** | EAC = revised budget | Only when actuals are tracking exactly to budget |
| **Linear extrapolation** | EAC = cost to date / % complete | Mid-project after 30%+ complete |
| **Bottom-up reforecast** | EAC = cost to date + revised ETC by line | End of every month — most accurate |

**Recommended:** bottom-up at every month-end. Linear extrapolation as a weekly sanity check.

### 7.7 Cost overruns — what to watch when

| Frequency | Check |
|---|---|
| **Daily** | Field labor hours by code (timecards), material deliveries vs. PO |
| **Weekly** | Committed vs. budget by code; sub progress vs. payment requests; small-tool & consumables; pending CO log |
| **Monthly** | Bottom-up EAC; cash flow vs. forecast; A/R aging; A/P aging; warranty reserve |

**The four codes that overrun most often on residential:**
1. **General conditions** — schedule slippage extends every weekly cost
2. **Self-perform labor** — productivity assumed > productivity actual
3. **Interior finishes** — owner selections drift upward, missed CO discipline
4. **Punch / closeout** — chronically under-budgeted; plan 2–3 weeks of supervision + 1 trip from each finish trade

---

## 8. Cash Flow Management

### 8.1 The residential cash flow cycle

```
You incur cost  →  You bill owner  →  Owner pays  →  You pay subs
   (Day 0)         (Day 25-30)      (Day 35-50)     (Day 40-55)
```

The gap between "you incur cost" and "owner pays" is the **float you finance.** On a $2M residential job it can easily be $200–400K of working capital at any given time.

### 8.2 Draw schedule vs. actual work in place

The classic trap: you're 18% complete (by cost) but you've only collected 15% (down payment + first draw not yet earned). You're **cash negative.** Two ways to avoid:

| Tactic | How |
|---|---|
| **Front-load the draw schedule** | Get mobilization + foundation draws to cover first 8 weeks of cost |
| **Bill by value of work in place** | If contract allows monthly pay apps with schedule-of-values, bill what you've actually built |

**Build a cash flow S-curve at bid time.** Plot expected cumulative cost vs. cumulative billings (and cumulative payments received) by month. Look for the deepest "cash negative" point — that's how much working capital you need to finance.

### 8.3 Retainage

**California residential norms:** 5–10% retention withheld from each pay app, released at substantial completion (sometimes 30 days after). On owner contracts, you can negotiate this; on construction-lender-financed jobs it's typically non-negotiable at 10%.

Retainage is real money you've earned and don't yet have. On a $1.5M job at 10% retention, that's $150K sitting somewhere. **Mirror retention down to your subs** (withhold the same % from them) so you don't finance their portion.

### 8.4 Float financing — your tools

| Tool | What it does | Cost / risk |
|---|---|---|
| **Line of credit (bank LOC)** | Bridges the gap; draw and repay as cash cycles | 7–12% APR currently; requires personal guarantee; covenants |
| **Owner deposit / mobilization** | Front-loaded draw covers initial cost | Limited by CSLB §7159.5 on remodels |
| **Material supplier credit (net 30 / net 60)** | Defers AP by 30–60 days | Requires established relationships; takes 1–2 years to build |
| **Sub pay-when-paid** | You don't pay subs until owner pays you (CA allows as timing mechanism, not condition) | Strains sub relationships if abused |
| **Project-specific financing / construction loan** | Owner's loan funds draws directly | Requires lien releases and inspections per draw |
| **Personal capital (owner's equity)** | Most common on new GC's first jobs | High personal risk; not scalable |

**Practical rule of thumb:** maintain working capital (LOC + cash) of at least **15–20% of your largest job's contract value.** A GC with $300K of liquidity can't run a $5M job safely.

### 8.5 California lien rights — the cash flow safety net

| Tool | What it does | Deadline |
|---|---|---|
| **Preliminary 20-Day Notice** | Reserves your right to file a mechanics lien. Required for any party not in direct contract with owner, AND for direct contractors when there's a construction lender. | Within **20 days of first furnishing labor/materials**. Late notice = lien rights only from 20 days before serving onward. ([Levelset CA prelim notice][lvprelim], [Handle][handle-prelim]) |
| **Mechanics lien (private project)** | Cloud on title; can force foreclosure to collect | Must record within **90 days** of completion of work, or **60 days** after recorded Notice of Completion (whichever is shorter) ([CNS Lien deadlines][cnslien]) |
| **Stop payment notice** | Freezes lender funds | Same 90/60 day window |
| **Bond claim** (if project is bonded) | Claim against payment bond | 90 days |

**Practical workflow for every job:**
1. Day 1 of work: file 20-Day Preliminary Notice on owner, lender, and any GC above you (or, if you're prime GC, on owner and lender). Send certified mail. Keep proof.
2. Require every sub and supplier to send you their own 20-day notice.
3. Track when you have/don't have lien rights every week.

### 8.6 Lien waivers — getting them right

California has **four statutory forms** (Civil Code §8132–8138). Use these exact forms — handwritten or custom waivers are unenforceable.

| Form | When |
|---|---|
| **Conditional Waiver and Release on Progress Payment** | Submit with each pay app; effective only on actual receipt of payment |
| **Unconditional Waiver and Release on Progress Payment** | After payment clears, before next pay app |
| **Conditional Waiver and Release on Final Payment** | Submit with final pay app |
| **Unconditional Waiver and Release on Final Payment** | After final payment clears |

**Critical rule:** never sign an **unconditional** waiver before money is in your bank. Once signed, you've waived rights regardless of payment. ([CSLB lien waiver forms][cslb-waiver], [getbuilt][getbuilt])

**Cash discipline:** get conditional waivers from every sub with every pay app, and unconditional with the next one once their check has cleared. Don't release the next pay app until you have unconditional waivers covering the prior payment.

### 8.7 A/R management — getting paid on time

| Practice | Why |
|---|---|
| Submit pay apps on the same day each month (e.g. 25th) | Predictability for owner and lender |
| Use a clean schedule-of-values matching your contract | Easier approval, fewer back-and-forths |
| Attach photos and progress evidence | Reduces "prove it" questions |
| Follow up at day 7, 14, 21 if not paid | A/R aging > 30 days is a red flag |
| Send a **Notice of Intent to Lien** at day 45 | Last warning; usually shakes payment loose |
| Record a mechanics lien if needed | Day 60–75, after counsel review |

**When an owner stops paying** (mid-job):
1. Stop work after written notice of suspension per contract (typ. 7–10 days unpaid)
2. Document everything in writing
3. File preliminary notice and lien if rights are still alive
4. Don't dump cost into a job you may not get paid for — sub COs and procurement should pause
5. Talk to a CA construction attorney early — fixing a payment dispute legally at month 3 is 10× cheaper than month 12

---

## 9. Change Order Management

### 9.1 Change order triggers

| Source | Example |
|---|---|
| **Owner-requested scope addition** | "Add a 200 SF deck off the master" |
| **Owner-requested change** | "Switch all the cabinets from painted to walnut" |
| **Unforeseen conditions** | Buried oil tank, rotten subfloor under tile, undisclosed termite damage |
| **Design errors / omissions** | Beam wasn't sized for the actual loading; plans don't match elevations |
| **Code interpretation by inspector** | Inspector requires additional bracing not on drawings |
| **Allowance reconciliation** | Tile selected at $14/SF when allowance was $8/SF |
| **Substitutions** | Specified product discontinued; substitute differs in price |
| **Schedule extensions** | Owner-caused delay extends GC duration |

### 9.2 Pricing methods

| Method | Use when | How to price |
|---|---|---|
| **Negotiated lump sum** | Scope is definable in advance | Direct cost + GC + OH + profit. Most common. |
| **Unit prices** | Repetitive items with quantity unknown (e.g. trenching, extra demo) | Pre-agreed unit price × actual quantity verified |
| **T&M with NTE cap** | Discovery / emergent work; can't be scoped in advance | Labor at agreed burdened rate + material at cost + agreed markup. Cap at NTE. |
| **Cost-plus on the change** | When base contract is cost-plus | Sub cost × (1 + agreed markup) |

### 9.3 Change order markup — what's typical

| Element | Typical residential markup |
|---|---|
| GC markup on sub change order | **15–25%** (OH + profit combined) |
| GC markup on self-perform labor & material | **15–25%** on top of cost |
| T&M labor — straight time | Burdened rate × 1.15–1.25 |
| T&M labor — overtime | Burdened rate at 1.5× × 1.15–1.25 |
| Material from owner-direct vendor (you handle) | 10–15% handling fee |
| Schedule extension | Per diem GC rate (super + indirects per day) × days |

If your subcontract says "GC may add 15% OH&P on subcontracted change orders," do not casually agree to 10% — it's a permanent margin compression on every CO over the life of the contract.

### 9.4 Change order documentation — what every CO needs

| Element | Required |
|---|---|
| Sequential CO number | Yes |
| Description of changed work | Yes — narrative, plus drawings/markups if applicable |
| Reason for change | Yes — links to RFI, ASI, owner directive, or field condition |
| Pricing backup | Yes — sub quotes, labor calc, material list |
| Schedule impact (calendar days) | Yes — even if zero, state "no schedule impact" |
| Owner signature | **YES** — before performing the work |
| Updated contract value running total | Yes |
| Updated substantial completion date | Yes |

### 9.5 Getting COs signed before doing the work

This is where new GCs lose the most money. The pattern:

> Owner says "just do it, we'll figure out the cost later." You proceed. At close-out you submit a $40K CO for the cumulative changes. Owner pushes back hard, claims some weren't authorized, demands documentation you don't have. You eat 30–50%.

**How to hold the line without poisoning the relationship:**

| Step | Script |
|---|---|
| 1. Acknowledge urgency | "Got it — I want to keep us moving on this." |
| 2. Frame the cost discipline as protection for the owner | "I owe you transparency on cost. I'll have a price to you by end of day tomorrow before we order materials." |
| 3. Provide a fast rough order of magnitude same-day | "Rough number is $4–6K. Final number after I get the electrician's quote in the morning." |
| 4. Use email confirmation when verbal | "Per our conversation, proceeding with adding the island circuits at NTE $5,500, formal CO to follow within 48 hours." |
| 5. For truly emergent (safety, weather): use a **field directive** | A short standardized form: scope, T&M, signed by owner that day. Convert to formal CO later. |
| 6. Cumulative CO log presented at every OAC meeting | Owner sees the running total — no surprises at close-out. |

### 9.6 Cumulative CO tracking

Always present the owner with one single summary of changes:

| CO # | Description | Amount | Days | Status | Date approved |
|---|---|---|---|---|---|
| 001 | Add deck off master | $14,800 | 4 | Approved | 3/12 |
| 002 | Upgrade kitchen cabinets to walnut | $22,500 | 0 | Approved | 4/2 |
| 003 | Replace rotted subfloor at bath 2 | $3,400 | 2 | Approved | 4/15 |
| 004 | Allowance reconciliation — tile | ($1,200) | 0 | Pending | — |
| | **Cumulative CO impact** | **$39,500** | **+6 days** | | |
| | Original contract | $1,701,800 | | | |
| | **Revised contract value** | **$1,741,300** | | | |
| | **Revised substantial completion** | + 6 days = 4/26 → 5/2 | | | |

---

## 10. Closeout Financial Management

### 10.1 Final billing & retainage release

Sequence:

1. **Substantial completion** — work is fit for owner occupancy, items remaining are punch list. Issue notice of substantial completion.
2. **Final punch list** — single comprehensive list, agreed with owner, dated.
3. **Punch completion** — typically 30–60 days.
4. **Notice of Completion** — owner records with the county (CA: required to shorten lien filing deadline to 60 days). Even if owner doesn't record, your lien deadline becomes 90 days from work end.
5. **Final pay application** — includes:
   - Final draw for work not yet billed
   - Release of retainage
   - All approved COs reconciled
   - All allowances reconciled
   - **Conditional final lien waivers from all subs**, and from GC
6. **Owner payment** — typically 30 days after substantial completion + punch.
7. **Unconditional final lien waivers** issued by GC and all subs once payment clears.
8. **Warranty period begins** — usually 1 year from substantial completion.

### 10.2 Lien waivers at closeout

| When | What to collect from each sub |
|---|---|
| With final pay app submission | Conditional Waiver and Release on Final Payment |
| After their final payment clears (you've paid them) | Unconditional Waiver and Release on Final Payment |
| In your hand before issuing owner the final unconditional waiver | All sub unconditional finals |

**Risk to manage:** owner pays you, you sign unconditional final to owner, but you haven't paid all subs yet. Now you've waived your lien rights but a sub can still lien the property — and the owner will look to you. **Sequence is critical**: get subs' unconditional finals before signing yours to the owner. ([Schorr Law conditional vs. unconditional][schorr])

### 10.3 Warranty period costs

Budget a **warranty reserve** at bid time, typically **0.5–1.5% of contract value**:

| Project type | Warranty reserve |
|---|---|
| New construction, well-known subs | 0.5–0.75% |
| Custom home, high-end finishes | 1.0–1.5% |
| Remodel with unknowns | 1.0–2.0% |
| Production / spec home | 0.5–1.0% |

Track warranty costs by job in your accounting system. Most callbacks cluster around:
- First rainy season (roof leaks, window leaks, drainage)
- First HVAC season change (balancing, controls)
- Wood movement (cabinet doors, hardwood gaps, drywall cracks)

If you're using the warranty reserve up regularly, your sub selection or QC is the problem — fix upstream, not at the callback.

### 10.4 Job cost post-mortem

Within 30 days of project close, run a **lessons learned** meeting with super, PM, and (if possible) lead subs. Output:

| Section | Content |
|---|---|
| **Final cost vs. budget by cost code** | Variances explained; flag codes with >5% variance |
| **Productivity actuals vs. estimate** | Update your productivity database for next job |
| **Scope gaps discovered** | Add to bid checklist for next project |
| **Sub performance scorecard** | Update A/B/C sub list |
| **CO cumulative analysis** | What % of original contract were COs? What drove them? |
| **Schedule actual vs. plan** | Where did we slip? Owner-caused vs. self? |
| **Final OH&P recovery** | Did we earn the profit we bid? |
| **Warranty exposure** | What's likely to come back? Set the reserve. |

**The post-mortem becomes the first input to the next estimate.** A GC who runs this discipline for 5 jobs will out-estimate one who doesn't, for the rest of their career.

---

## 11. Quick Reference: Numbers to Memorize

| Item | Number |
|---|---|
| Residential GC overhead, typical | 10–15% |
| Residential GC profit, net, typical | 5–12% |
| Markup vs. margin | 25% markup ≈ 20% margin |
| General conditions, typical % of direct cost | 8–12% |
| California down payment cap (home improvement) | Lesser of 10% or $1,000 |
| California preliminary notice deadline | 20 days from first furnishing |
| California mechanics lien deadline (private, no NOC) | 90 days from completion |
| California mechanics lien deadline (after NOC) | 60 days from NOC recording |
| Retainage, typical California residential | 5–10% |
| Workers' comp burden, CA carpentry | 8–18% of payroll |
| Total labor burden, CA residential | 35–55% |
| Waste factor, lumber | 5–10% |
| Waste factor, drywall | 10–12% |
| Waste factor, tile field | 10% |
| Waste factor, tile diagonal | 15% |
| Waste factor, concrete slab | 5–10% |
| Working capital needed, typical | 15–20% of largest job |
| Warranty reserve, typical | 0.5–1.5% of contract |
| Change order markup on sub COs, typical | 15–25% |
| Bid hours minimum, $1M custom home | 40 hours |

---

## 12. Sources & Further Reading

- [Siana Marketing — General Contractor Profit Margin: 2026 Industry Data & Benchmarks][siana]
- [Levelset — Average Contractor O&P for California Residential][levelset]
- [Bridgit — General Conditions Construction Cost Estimating Guide][bridgit]
- [SmartBarrel — General Conditions: The Hidden Costs That Kill Your Bids][smbar]
- [Construction Bids AI — Construction Labor Productivity Rates Guide][cbai]
- [BuildItCalc — Material Waste & Overage Calculator][bldc]
- [National Calculator Authority — Construction Material Waste Factor Calculator][nca]
- [Levelset — California 20-Day Preliminary Notice Guide & FAQs][lvprelim]
- [Handle — California Preliminary Notice for Private Works][handle-prelim]
- [CNS Lien — California Mechanics Lien Deadlines][cnslien]
- [CSLB — Conditional and Unconditional Waiver and Release Forms][cslb-waiver]
- [Schorr Law — Conditional & Unconditional Lien Waiver Forms in California][schorr]
- [getbuilt — Conditional vs Unconditional Lien Waivers][getbuilt]
- [Contractor's Licensing Schools — $1,000 Rule: California Down Payment Laws][cslb-bp]
- [Procore — Construction Draw Schedules][procore-draw]
- [ABL Funding — Residential Construction Draw Schedule Template][abl]
- [AIA Contract Documents — A-Series Owner/Contractor Agreements][aiaguide]

[siana]: https://www.sianamarketing.com/resources/general-contractor-profit-margin
[levelset]: https://www.levelset.com/payment-help/question/what-is-the-average-contractors-op-for-residential-construction-in-california/
[bridgit]: https://gobridgit.com/blog/general-conditions-construction-cost-estimating/
[smbar]: https://smartbarrel.io/blog/how-general-conditions-impact-construction-bids-and-project-success/
[cbai]: https://constructionbids.ai/blog/construction-labor-productivity-rates-bidding-guide
[bldc]: https://www.builditcalc.com/material-waste-calculator.html
[nca]: https://nationalcalculatorauthority.com/construction-material-waste-factor-calculator
[lvprelim]: https://www.levelset.com/preliminary-notice/california-preliminary-notice-faqs/
[handle-prelim]: https://www.handle.com/california-preliminary-notice/
[cnslien]: https://cnslien.com/2025/03/19/california-mechanics-lien-deadlines-what-you-need-to-know/
[cslb-waiver]: https://www.cslb.ca.gov/consumers/legal_issues_for_consumers/mechanics_lien/conditional_and_unconditional_waiver_release_form.aspx
[schorr]: https://schorr-law.com/what-is-a-lien-waiver/
[getbuilt]: https://getbuilt.com/blog/conditional-and-unconditional-lien-waivers-what-they-mean-and-when-to-use-them/
[cslb-bp]: https://contractorslicensingschools.com/blog/1000-rule-californias-new-down-payment-laws-every-contractor-must-know/
[procore-draw]: https://www.procore.com/library/construction-draw-schedule
[abl]: https://www.ablfunding.com/blog/residential-construction-draw-schedule-template/
[aiaguide]: https://learn.aiacontracts.com/contract-doc-pages/71126-a-series-ownercontractor-agreements/

---

*End of Module 08. Next-step modules to consider: deeper dives on T&M pricing for service work, GMP contract negotiation tactics, and California-specific subcontractor management law.*
