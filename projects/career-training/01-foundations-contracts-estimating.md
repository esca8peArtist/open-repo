---
title: "Industrial GC Foundations: Role, Contracts, and Estimating"
module: 01
discipline: ["mechanical", "electrical", "contracts", "estimating"]
audience: "First-time industrial general contractor (construction-experienced)"
status: "reference"
tags: [career-training, general-contracting, industrial-construction, contracts, estimating, bonds, EPC, GMP]
created: 2026-05-12
---

# Module 01 — Foundations: Role, Contracts, and Estimating for the Industrial General Contractor

> **Scope.** This is the foundation module for a general contractor moving into industrial work — manufacturing plants, refineries, power plants, warehouses with process loads, and heavy industrial facilities. The emphasis throughout is **mechanical and electrical**, which together typically represent 50–75% of installed cost on an industrial project. This document assumes you already have construction experience; it does not re-explain RFI workflow or basic scheduling.

---

## 1. What a General Contractor Does on Industrial Projects

### 1.1 Role definition — three roles that get confused

| Role | Who they work for | Risk position | Typical fee structure |
|---|---|---|---|
| **General Contractor (GC) / Prime** | Owner, under a prime contract | Holds construction risk, signs the bond, signs subcontracts | Lump sum, GMP, or cost-plus with fee |
| **Specialty Subcontractor** | The GC (or sometimes the owner directly as a "prime sub") | Holds risk only for its trade scope | Lump sum or unit price for that trade |
| **Owner's Representative / PMC** | Owner only | No construction risk — advisory and oversight | Hourly, monthly retainer, or % of installed cost |

The distinction matters because industrial owners frequently blur it. An "EPCM" (Engineering, Procurement, Construction *Management*) firm looks like a GC on the org chart but is actually an owner's rep — it holds no construction subcontracts and bears no schedule/budget risk. A true GC signs the trade contracts and is on the hook if a piping sub goes bankrupt.

### 1.2 Prime-contract responsibilities vs. subcontract management

As the prime, you have **two contractual fronts** running in parallel:

**Upstream (Owner ↔ GC, the "Prime Contract")**
- Single point of accountability for schedule, budget, quality, and safety
- Direct liability for liquidated damages, warranty, and performance guarantees
- You hold the performance and payment bonds (see §2.7)
- You sign permits, file notices, and carry the controlling insurance policies (typically OCIP/CCIP rolls some of this back to the owner)
- You manage the formal RFI / submittal / change-order workflow with the design team

**Downstream (GC ↔ Subs, the "Subcontracts")**
- Solicit, level, and award trade packages (mechanical, electrical, I&C, civil, etc.)
- Flow down prime-contract obligations where applicable (see §2.6)
- Administer pay applications, lien waivers, and retainage
- Coordinate sequencing across trades — the GC owns the *interfaces*, not the trades themselves
- Enforce safety program, drug testing, site-specific training, and badging

You are essentially running a **risk-transfer business**: the owner pushes risk to you, you push as much as the law allows down to subs, and you keep the residual risk priced into your fee.

### 1.3 Typical industrial GC scope of work

An industrial GC is rarely self-performing all of this — but is *managing* all of it:

| Discipline | Typical scope items |
|---|---|
| **Civil / Site** | Mass and structural excavation, foundations, pile caps, underground utilities, paving, stormwater, secondary containment |
| **Structural** | Pipe racks, equipment supports, structural steel, platforms, stairs, grating, anchor bolts, grout |
| **Mechanical / Piping** | Process piping (ASME B31.1, B31.3), equipment setting (pumps, compressors, vessels, heat exchangers), pipe supports, insulation, NDE, hydro/pneumatic testing |
| **Electrical (Power)** | Substations, switchgear, MCCs, transformers, conduit and cable tray, power cable pull and terminate, grounding, lightning protection, cathodic protection |
| **Instrumentation & Controls (I&C)** | Field instruments, junction boxes, instrument tubing, signal/control cable, panel work, loop checks, integration to DCS/PLC |
| **Fire Protection** | NFPA-compliant deluge, foam, clean agent, hydrants, monitors, detection (with separate FM/UL-approved installers) |
| **HVAC** | Process ventilation, classified-area HVAC (Class I Div 1/2), pressurization for control rooms, dust collection ducts |
| **Coatings / Insulation** | Surface prep, primer/intermediate/topcoat systems, hot/cold insulation, jacketing, fireproofing (intumescent and cementitious) |
| **Commissioning support** | Mechanical completion punch lists, loop checks, energizations, hand-over packages, vendor support coordination |

The GC's value-add is not doing any one of these well — it is **sequencing all of them** through a constrained, often live, industrial site.

### 1.4 How industrial GC work differs from commercial construction

This is the section first-time industrial GCs underestimate. The differences are not stylistic — they change how you bid, schedule, and staff.

- **MEP is the project, not a finish trade.** In commercial work, the building shell drives schedule; MEP fills in. In industrial work, the *process equipment and its piping/wiring* is the building's reason to exist. The structural steel exists to hold a column up; the column drives the schedule.
- **Codes are different and stricter.** ASME B31.3 (process piping), NFPA 70 / NEC Article 500 (hazardous locations), NFPA 70E (arc flash), API 650/653 (tanks), ASME Section VIII (pressure vessels), OSHA 1910.119 PSM (Process Safety Management). Commercial IBC/IMC knowledge is necessary but nowhere near sufficient.
- **Welder qualification and weld procedures.** Every production welder needs a WPQ to the appropriate WPS; the GC (or its piping sub) maintains the records. Owner or AI (Authorized Inspector) audits them.
- **NDE and testing are deliverables, not afterthoughts.** Radiography, PT, MT, UT, hydrotest packages, and pneumatic tests are line items, with formal turnover packages.
- **Brownfield work dominates.** Most industrial work is on operating sites. That means tie-ins under outage windows, hot work permits, LOTO (Lockout/Tagout), confined-space programs, line-break procedures, and SIMOPS (Simultaneous Operations) management. None of this exists on a greenfield commercial build.
- **Productivity is lower.** Industrial labor productivity is routinely 50–70% of commercial benchmarks because of PPE, permits, congestion, and elevations. Pricing this wrong is the single most common way new industrial GCs lose money (see §3.4).
- **Owner technical staff are involved daily.** A commercial owner sees the building at substantial completion; an industrial owner has operations, maintenance, and reliability engineers walking the job every day, often with the authority to redirect work.
- **Vendor-supplied equipment dominates the cost basis.** A $50M project may include $20M of owner-furnished or vendor-engineered equipment (compressors, heat exchangers, control systems). The GC's scope is to *receive, set, align, hook up, and commission* these — not to procure them. The procurement risk model is therefore inverted.

---

## 2. Contract Types and Legal Foundations

### 2.1 Lump Sum (Fixed Price)

A single price for a defined scope. The contractor bears all cost-overrun risk; the owner bears scope-creep risk.

- **Use when:** Scope is well-defined, drawings are issued for construction (IFC), conditions are predictable
- **Watch for:** Aggressive owner-friendly clauses that convert "lump sum" into "lump sum plus everything we forgot" — see *exclusions* discipline in §3.2
- **Margin profile:** Highest upside if you execute well; bid-or-die downside

### 2.2 Unit Price

Price per defined unit (LF of conduit, CY of concrete, DI of weld). Final contract value = unit price × actual installed quantity.

- **Use when:** Quantities are uncertain but unit conditions are stable (e.g., site work, underground utilities, repetitive piping)
- **Watch for:** The owner's right to *vary* quantities; many contracts allow ±15–25% variation at the same unit price before renegotiation triggers
- **Industrial relevance:** Common for tank cleaning, pipeline replacement, multi-unit refinery turnarounds

### 2.3 Cost-Plus

Owner reimburses actual costs plus a fee. Three common forms:

| Variant | Fee structure | Contractor incentive |
|---|---|---|
| **CPFF** (Cost Plus Fixed Fee) | Flat dollar fee, regardless of cost | Stay on schedule; cost doesn't affect fee |
| **CPIF** (Cost Plus Incentive Fee) | Base fee + share of savings (or penalty for overrun) against a target | Aligned to target — most common on industrial |
| **CPPC** (Cost Plus Percentage of Cost) | Fee = % of actual cost | Generally disfavored — *illegal* on US federal work (FAR 16.102(c)) because it perversely rewards cost growth |

CPIF with a target cost and a sharing ratio (commonly 70/30 owner/contractor on savings) is the workhorse of large industrial work where scope is evolving.

### 2.4 Time and Materials (T&M)

Hourly labor rates × hours, plus material cost × markup, plus equipment rates. Used for emergencies, undefined scopes, and small change-order work.

- **Use when:** Scope cannot be defined in advance (turnaround discovery work, breakdowns)
- **Owner protections:** "Not-to-exceed" caps, daily timesheet signoff, audit rights
- **GC discipline required:** Foreman discipline on coding hours, signed daily reports, immediate material receipts — losing the documentation game on T&M is a path to disputed invoices and 90+ day receivables

### 2.5 GMP (Guaranteed Maximum Price)

A hybrid: the contractor reimbursed at cost up to a ceiling, with shared savings below the ceiling. Above the ceiling, the contractor eats the overrun.

- **Common with CMAR delivery** (see §2.6)
- **Critical mechanics:** What is included in the "cost"? What contingencies sit *inside* vs. *outside* the GMP? How is shared savings calculated and timed?
- **Open-book accounting:** Owner has full audit rights into actual cost; the GC must run "open-book" project accounting

### 2.6 EPC, EPCM, Design-Build, Design-Bid-Build, CMAR

These are **delivery methods** — how design and construction are organized — and they sit on top of the **contract type** (lump sum, GMP, etc.).

| Delivery Method | Design holder | Construction holder | Owner risk | Schedule speed |
|---|---|---|---|---|
| **Design-Bid-Build (DBB)** | Owner (via A/E) | GC (separate) | High — owner owns design adequacy | Slowest |
| **Construction Manager at Risk (CMAR)** | Owner (via A/E) | CM converts to GC under GMP | Medium | Faster — overlap design and procurement |
| **Design-Build (DB)** | Single entity | Same entity | Lower — single point of responsibility | Fast |
| **EPC** | Single entity (full design) | Same entity | Lowest — performance guarantee on plant output | Fast, but disciplined |
| **EPCM** | Single entity for E + CM | *Owner holds trade contracts* | High — looks like EPC but isn't | Variable |

Two industrial-specific notes:

- **EPC** is the dominant delivery method on greenfield process plants because the owner wants a single-point throat to choke and a performance guarantee (turnkey, with a heat-rate or throughput warranty). The lump-sum EPC contract is high-risk for the contractor and is priced accordingly — EPC contingencies of 8–15% of contract value are normal.
- **EPCM** is dominant on mining, oil & gas, and brownfield petrochemical work. Despite the "C" looking like "Construction," it is **Construction Management** — the EPCM firm is an agent, not a constructor. As an industrial GC, you may be a trade contractor under an EPCM firm, in which case your contract is *with the owner directly* and the EPCM firm is an intermediary you take direction from but who does not pay you.

### 2.7 Key contract clauses — what to negotiate

These clauses are where projects are won or lost long before they break ground:

**Indemnification.** Who defends and pays when someone gets hurt or property is damaged? Look for:
- *Comparative* (each party pays for what they caused) vs. *broad-form* indemnity (you pay for everything, even owner's negligence) — broad-form is unenforceable in many states (e.g., anti-indemnity statutes in TX, CA, IL) but still gets drafted in
- "Negligence-trigger" language — you only indemnify *to the extent of* your negligence
- Insurance-backed indemnity — your CGL must cover the contractual liability you've signed up for

**Liquidated Damages (LDs).** Pre-agreed dollar amount per day of delay against a milestone. Industrial LDs are often *substantial* — $25k–$500k/day on power and refining work, sometimes higher.
- Negotiate a **cap** (commonly 10–20% of contract value, sometimes capped at the contractor's fee)
- Negotiate **excusable delay** events (force majeure, owner-caused, differing site conditions)
- Distinguish *delay LDs* from *performance LDs* (the latter apply when plant output doesn't meet guarantee — EPC-specific)
- "Sole and exclusive remedy" language for LDs is contractor-favorable — it prevents stacking LDs on top of actual damages

**Force Majeure.** Excusable events that suspend performance.
- A *list-based* clause (named events: hurricane, war, pandemic, strike) is safer than open-ended language
- Most clauses give **time relief only**, not money — read carefully
- "No damages for delay" clauses, when stacked with force majeure, can leave you absorbing weeks of standby costs

**Change Order Provisions.** The single most important clause for cash flow.
- Notice requirements (often 7–14 days, sometimes as short as 48 hours)
- Pricing methodology (T&M? agreed unit rates? cost-plus with capped fee?)
- "Pending change order" rights — can you proceed with work while pricing is negotiated, or must you stop?
- Constructive change doctrine — when owner direction effectively changes the work without a formal CO

**Retainage.** Owner withholds a percentage of each payment (commonly 5–10%) until completion.
- Negotiate **stepped reduction** at 50% completion
- Negotiate **early release of retainage on stored equipment**
- Federal projects: 10% until 50%, then can drop to 0% per FAR if performance is satisfactory
- Many states cap retainage by statute (e.g., California: 5%)

**Payment Terms.** Industry standard is net-30 from approved pay app, but industrial owners frequently push net-45 or net-60. Combined with 60-day pay-app cycle this means *the GC is financing the owner for 90+ days*.
- Negotiate **interest on late payment** (8–12% annual is typical)
- Statutory prompt-pay laws exist in most states for public work and many for private — know yours

**Dispute Resolution.** Step-up clauses: senior-management negotiation → mediation → arbitration or litigation.
- AAA Construction Industry Rules are common for arbitration
- Venue and choice-of-law matter — getting dragged to the owner's home state for arbitration is expensive
- Waiver of consequential damages should be mutual

### 2.8 AIA vs. EJCDC vs. ConsensusDocs vs. Owner-Proprietary

These are **standard contract families**. Industrial work uses all four, plus heavily-modified owner proprietary forms.

| Family | Authored by | Tilt | Common use |
|---|---|---|---|
| **AIA** | American Institute of Architects | Architect-favorable; treats architect as owner's representative | Commercial, institutional, some light industrial |
| **EJCDC** | Engineers Joint Contract Documents Committee (ACEC + NSPE + ASCE) | Engineer-favorable; better-suited to engineered systems | Utility, water/wastewater, light industrial |
| **ConsensusDocs** | 40+ industry associations including AGC | Most contractor-balanced of the three; removes designer from administration role | Increasingly used on private work, especially design-build |
| **Owner-Proprietary** | Owner's law firm | Owner-favorable, often aggressive | Heavy industrial — refining, chemical, power, mining (most large industrial owners insist on their own form) |

Key behavioral difference: **ConsensusDocs** does not treat the design professional as the owner's agent during construction — observation and approval fall directly on the owner. **AIA** and **EJCDC** vest the design professional with that role. On a process plant where the EPC engineer is also designing equipment they procured, this distinction has real consequences.

**Practical reality on industrial work:** Plan to receive a heavily-modified owner-proprietary form, marked up by an oil-and-gas or power-industry law firm. Your job (often with your construction attorney) is to redline back to something closer to a balanced position. Expect to *negotiate* — not accept — indemnity, LD caps, warranty, and consequential damages waivers.

### 2.9 Flow-Down Clauses

A flow-down clause in your subcontract says: "Subcontractor assumes toward Contractor all obligations Contractor assumes toward Owner, as applicable to Subcontractor's work."

**What actually flows through generic flow-down language (per most case law):**
- Scope, quality, schedule, technical specifications
- Safety and site rules
- General performance standards

**What courts (notably in New York and several other jurisdictions) have held does NOT flow through generic language and must be *specifically called out* in the subcontract:**
- Indemnification provisions
- Insurance requirements (especially additional-insured status)
- Dispute resolution / forum selection / arbitration clauses
- "Pay-when-paid" / "pay-if-paid" provisions
- "No damages for delay" provisions
- Liquidated damages

**Drafting practice:** Use a hybrid — a general flow-down clause **plus** specific re-statement of the critical risk-transfer provisions. If you want the LD clause to apply to your piping sub, *write it into the subcontract*; don't rely on incorporation by reference.

### 2.10 Bonds

A surety bond is a three-party instrument: **principal** (you), **obligee** (owner or, for payment bonds, the subs/suppliers), and **surety** (the bonding company).

| Bond | Purpose | When required | Typical amount |
|---|---|---|---|
| **Bid Bond** | Guarantees you will sign the contract and provide P&P bonds if awarded | With bid, on most public and many private industrial jobs | 5–10% of bid (sometimes "bid security" via certified check) |
| **Performance Bond** | Guarantees you will complete the project per contract | At contract execution, federal jobs >$150k (Miller Act), most states' Little Miller Acts for state public work | 100% of contract value (sometimes 50% on private) |
| **Payment Bond** | Guarantees you will pay subs and suppliers | Same triggers as performance bond | 100% of contract value (Miller Act); some private owners require less |

**Miller Act (40 U.S.C. ch. 31, subch. III).** On federal construction contracts exceeding $150,000 (per FAR 28.102), the prime must provide both performance and payment bonds. Subcontractors cannot lien federal property (sovereign immunity), so the payment bond is their *only* recourse — and it gives them a Miller Act claim with a 90-day notice and 1-year suit window.

**How to get bonded.** Sureties underwrite based on the "Three C's": Character, Capacity, Capital.
- **Character:** Personal and corporate references, history of completing projects
- **Capacity:** Track record of similar size/type work — sureties typically allow single-job aggregate at 5–10× working capital and 10–20× equity
- **Capital:** Audited financial statements (work-in-progress schedule, balance sheet, P&L) — sureties want a CPA-prepared, percentage-of-completion (POC) WIP schedule
- **Premium:** ~0.5% to 3% of contract value, scaled to risk profile

**Building bonding capacity** is one of the strategic levers of a new industrial GC. Maintaining strong CPA-audited financials, low debt-to-equity, and a clean claims history with your surety expands the size of jobs you can chase.

---

## 3. Estimating and Bidding

### 3.1 Reading and interpreting bid packages

Two solicitation types dominate:

**IFB / ITB (Invitation for Bid / Invitation to Bid).** Sealed-bid, lowest responsive/responsible bidder wins. Specifications are fully defined. No negotiation on price after submission. Dominant on public-sector industrial work (municipal water/wastewater, public power, federal). Your job: get the price right and document responsiveness.

**RFP (Request for Proposal).** Multi-factor evaluation — price, technical approach, schedule, experience, key personnel. Negotiation allowed. Dominant on private industrial work. Your job: tell a credible technical story *and* be competitive on price.

**The bid package — typical components:**
1. Cover letter / instructions to bidders (deadlines, submittal format)
2. Bid form (line items you fill in)
3. Sample contract (with redlines highlighted, or stating "non-negotiable")
4. General Conditions and Special Conditions (read these *first* — risk lives here)
5. Technical specifications (CSI MasterFormat divisions, or owner-specific structure)
6. Drawings (issued for bid — IFB drawings, not IFC)
7. Geotechnical and environmental reports
8. Reference standards (codes, owner specs, vendor specs)
9. Existing conditions / record drawings (for brownfield)
10. Addenda (incorporate each one in writing)

**First-day reading discipline:**
- Read the **General and Special Conditions** before you look at a drawing. The commercial risk profile is set here.
- Identify the **delivery method, contract type, and LD structure** in the first 30 minutes.
- Identify any **owner-furnished equipment** list — this radically changes scope.
- Find the **schedule milestones** and outage/tie-in windows — these often define whether the job is biddable at all.

### 3.2 Scope review and exclusions

The discipline of **listing what you are NOT including** is more important than listing what you are.

Typical industrial exclusions (and why):

| Exclusion | Reason |
|---|---|
| Owner-furnished equipment (OFE) procurement | Owner buys directly — but check who pays freight, unloading, storage, set, and warranty |
| Permitting and impact fees | Owner usually retains — but you may be on the hook for trade-specific permits |
| Hazmat abatement | Specialty subcontractor and separate licensing |
| Soft excavation / dewatering beyond X feet | Differing site condition risk |
| Rock excavation | Unit price separately |
| Process commissioning and start-up | Owner / vendor scope |
| Operator training | Owner / vendor scope |
| Builder's risk insurance | Usually owner-procured on industrial |
| Sales tax on OFE | Often owner direct purchase to capture exemption |
| Spare parts | Vendor scope |
| Special tools and lifting fixtures | Vendor scope |

Write exclusions in the bid letter explicitly. Implicit exclusions disappear in litigation.

### 3.3 Quantity takeoff — mechanical and electrical

**Piping takeoff** is done by line, broken into:
- Pipe linear footage by size, schedule, and material (CS, SS, alloy, lined)
- Fittings by type and size (elbows, tees, reducers, caps)
- Valves by type, size, class
- Flanges, gaskets, stud bolts (FG&S sets)
- Welds — counted as **diameter-inches (DI)** — the workload metric for welding labor; DI = nominal pipe size × number of welds
- Supports (count + weight) and concrete/grouting where applicable
- NDE: % radiography by service, hydrotest packages
- Insulation by LF + size + thickness + service temperature
- Painting by surface area, coating system

**Equipment takeoff:**
- Tag list with weight, dimensions, anchor pattern, and lift requirements
- For each: receive/inspect, set, level, grout, hook up
- Pre-alignment and final alignment for rotating equipment
- Crane sizing — a single 200-ton lift can drive a week of mobilization cost

**Electrical takeoff:**
- Conduit by size, type (RMC, IMC, EMT, RGS, PVC-coated for hazardous), and run path
- Cable tray by size and type (ladder, solid bottom, ventilated)
- Wire by size and type (THHN, XHHW, MV cable, instrument cable) — separate measurements for power, control, instrument, and fiber
- Boxes, fittings, supports, seals (Class I Div 1/2 seal-offs are labor-intensive)
- Lighting fixtures by type, mounting, and hazardous-area rating
- Major gear: substations, switchgear lineups, MCCs, transformers, generators
- Grounding: counterpoise, ground rods, exothermic welds, equipment bonds
- Terminations — count each cable end; megger, hi-pot, and continuity testing

**I&C takeoff:**
- Instruments by tag (DP, PT, TT, LT, valves, analyzers)
- Junction boxes
- Instrument tubing by LF, OD, material
- Cable from field to JB to marshalling to DCS — count each segment
- Loop count for loop check labor

**Quantity tools.** Industrial estimators use Accubid, ConEst, RSMeans, and increasingly model-based takeoff from Navisworks, SmartPlant Construction, or Revit/CADWorx. A skilled piping estimator can hand-take-off about 1,500–3,000 DI per day; modeled takeoff at 5–10× that — but only if the model is reliable, which on bid-stage industrial it usually is not.

### 3.4 Labor productivity factors

**Labor units** are the heart of industrial estimating. A labor unit is "hours per unit installed" (e.g., 0.55 hrs/LF of 4" CS pipe, schedule 40, ground-level, normal access). Industry standard sources: **NECA Manual of Labor Units** (electrical), **MCAA labor units** (mechanical), **PHCC**, **RSMeans**, and proprietary contractor databases.

**Productivity adjustment factors (PFs)** are applied as multipliers to base labor units. Typical ranges on industrial work:

| Factor | Typical multiplier | Notes |
|---|---|---|
| Elevation (working above grade) | 1.05 – 1.40 | Increases with height and lift dependency |
| Hazardous area (Class I Div 1/2) | 1.10 – 1.25 | Permits, seals, sparking tools |
| PPE level (FRC, FRA, SCBA) | 1.05 – 1.30 | Heat stress and movement restriction |
| Confined space entry | 1.20 – 1.50 | Permit, attendant, rescue standby |
| Hot work permit area | 1.10 – 1.20 | Fire watch, gas test, permit cycle |
| Overtime (sustained >50 hr/wk) | 1.10 – 1.30 productivity loss | Diminishing returns — Bureau of Labor data |
| Stacking of trades / congestion | 1.10 – 1.40 | Multiple crews in same area |
| Weather (heat >95°F or cold <32°F) | 1.10 – 1.25 | Cycling work/rest, gloves |
| Shift work (2nd / 3rd shift) | 1.10 – 1.20 | Lighting, supervision, fatigue |
| Brownfield vs. greenfield | 1.20 – 1.60 | Permits, SIMOPS, congestion |
| Outage / turnaround work | 1.30 – 1.80 | Schedule pressure, congestion, working off design |

These compound multiplicatively. A brownfield, elevated, Class I Div 1 task with FRC and confined space entry can easily run at PF 2.0 — meaning your base labor unit doubles. **Forgetting to compound PFs is the #1 cause of lost-money industrial bids.**

### 3.5 Material pricing and escalation

- Get **firm quotes** from at least two suppliers per major commodity (pipe, valves, wire, cable, gear)
- Set a **quote validity period** that aligns with your bid acceptance period plus a buffer — 60–90 days is typical
- Long-lead equipment quotes need **price firm through delivery** — switchgear and transformers in 2024-2026 have 50–80 week lead times
- Negotiate **escalation clauses** in your contract — most commonly tied to PPI indices (BLS Producer Price Index, specific commodity series) — for projects longer than 12 months or with deferred starts
- Account for **freight, taxes, fuel surcharges, and warehousing** separately — don't bury in unit material cost

### 3.6 Subcontractor solicitation and bid leveling

**Solicitation:**
- Issue your sub bid package early — 3 weeks minimum before your prime bid date
- Pre-qualify subs on EMR (Experience Modification Rate), safety stats, bonding capacity, similar-project experience
- For each trade, target 3+ competitive bids
- Hold a sub pre-bid call to align scope and Q&A

**Leveling** (sometimes called "bid tabulation"):
- Normalize bids to **identical scope** — strip out inclusions/exclusions, alternates, and clarifications
- Build a leveling spreadsheet with one column per bidder, one row per scope item
- Adjust each bid to the *same* baseline before comparing
- Identify **scope gaps** — items no bidder included — these become GC self-perform or "scope holds"
- Watch for **unbalanced bids** (low base, inflated unit prices on overage items) — these are common gaming on unit-price work

A low bid that is missing 8% of scope is not a low bid; it is a setup for a change-order war. Disciplined leveling is the difference between a clean award and chasing margin all year.

### 3.7 Overhead and profit markup

**Direct cost** = labor + materials + equipment + subcontractors (the "hard cost")

**Indirect cost / Job overhead** = project-specific overhead: supervision, project management, site office, temp utilities, safety, QA/QC, small tools, consumables, travel, per diem. On industrial, this routinely runs **8–15% of direct cost.**

**General overhead / Home office overhead** = company-wide costs spread across projects: executive salaries, accounting, BD, office rent, IT. Typically **3–8%** of direct cost depending on volume.

**Fee / Profit** = what you take to the bottom line. Industrial GC fee ranges:
- Lump sum competitive bid: 3–7%
- GMP / negotiated: 4–8%
- Cost-plus with target: 5–10% (often with incentive)
- EPC: 8–15% (reflecting the higher risk)

A simple rule of thumb on competitive industrial work: total markup on direct cost = ~15–25% (covering job overhead + GO + fee). The **markup-vs.-margin trap**: a 20% markup on cost = 16.7% margin on revenue. To net a 20% margin on revenue, mark up cost by 25%.

### 3.8 Bid bond requirements

If the bid package requires a bid bond:
- Notify your surety early — they need to know what you're chasing
- Bid bonds run 5–10% of bid amount
- The "bid spread" question — if you're the low bidder and the second bidder is 20% higher, the surety may decline to issue the performance bond, fearing a math error
- Your surety underwriter has the right to approve the *job*, not just the *bond* — get them comfortable with industrial scopes early

### 3.9 Common estimating pitfalls — the industrial-specific list

1. **Under-pricing access.** A pump set 40 feet in the air over an operating unit is not the same labor as the same pump in a greenfield shop. Walk the site. Take photos. Add lift hours.
2. **Missing outage and tie-in constraints.** "Hot tap" or "tie-in during scheduled outage" buried in spec language can mean the difference between 16 hours and 16 days of work. Identify every tie-in. Confirm outage windows in writing.
3. **Underestimating permit cycle time.** Hot work, confined space, line break, energized work — each permit can consume 30–90 minutes of crew time per occurrence. On a tightly-permitted refinery, that's 10–15% direct labor loss.
4. **Ignoring SIMOPS and stacking.** When you're working alongside operations, maintenance, vendor reps, and other contractors, productivity collapses. Bid it.
5. **Missing escalation on long-lead.** A 60-week switchgear order placed in month 2 of a 24-month project delivers in month 16 at whatever the market is then — without an escalation clause you eat it.
6. **Misreading the LD clause.** A daily LD that is unlimited or stacks with performance LDs can wipe out the project margin in two weeks of delay.
7. **Assuming the prime can be negotiated.** Some owner-proprietary forms are genuinely non-negotiable. Build the risk into the price or no-bid.
8. **No contingency on brownfield discovery.** If you're touching existing infrastructure, carry 5–10% scope contingency for "discovered" conditions even on a lump sum — and negotiate a change-order mechanism that gives you a fighting chance to recover when they happen.
9. **Single-source critical commodity.** If only one vendor's pump fits the spec, you have no leverage. Identify these and negotiate price-firm + delivery commitments.
10. **Forgetting commissioning support hours.** Even if commissioning is "owner scope," vendors and operations will pull on your crews for support hours. Carry a separate line item.
11. **Undersizing the QA/QC and document control budget.** Industrial work generates 10–100× the document load of commercial — turnover packages can run thousands of pages per system. Staff for it.
12. **Wishful productivity assumptions.** Bidding industrial labor at commercial productivity is the most expensive single mistake you can make. Use industrial labor units. Apply PFs honestly. Validate with your own historical job data as you build it.

---

## 4. Recommended Next Steps for the New Industrial GC

- **Build a labor-unit library.** Buy NECA and MCAA manuals; capture your own actual hours per unit on every job you close. Within two years, your proprietary database becomes a competitive moat.
- **Get a construction attorney on retainer.** Specifically one who works on owner-proprietary EPC forms. A two-hour redline on the prime contract is the cheapest insurance you will ever buy.
- **Build a surety relationship.** Quarterly meetings with your bond underwriter, audited financials, clean WIP. Bonding capacity scales with relationship.
- **Pre-qualify your sub base.** Maintain a list of 3+ bonded subs per major trade in each region you work. Update annually.
- **Walk every site before bidding.** Mandatory pre-bid site visits exist for a reason. Skip one and you will price the drawing, not the project.

---

## Sources and Further Reading

**Role and scope of industrial general contractors**
- [What is General Contracting: Top 5 Benefits — NRG Consulting](https://www.nrgconsultingltd.com/post/what-is-general-contracting-complete-guide)
- [General Contractor Responsibilities Explained — Diamond Contractors](https://diamondcontractors.com/what-are-the-responsibilities-of-a-general-contractor/)
- [PMC Scope of Work (refinery) — Scribd document](https://www.scribd.com/document/94885541/PMC-Scope-of-Work)

**Delivery methods (EPC, Design-Build, CMAR, DBB)**
- [EPC vs Design-Build: What's Right for Industrial Projects — PLC Construction](https://www.plcconstruction.com/epc-vs-design-build-whats-right-for-industrial-projects/)
- [Choosing the right construction delivery method — JE Dunn](https://jedunn.com/blog/choosing-the-right-construction-delivery-method/)
- [Design-Build vs. CMAR — Finfrock](https://finfrock.com/design-build-vs-cmar/)
- [Comparing 5 Project Delivery Methods — Gordian](https://www.gordian.com/resources/comparing-5-project-delivery-methods/)
- [6 Construction Project Delivery Methods Compared — Procore](https://www.procore.com/library/construction-project-delivery-methods)
- [CMAR vs Design-Build — Mastt](https://www.mastt.com/blogs/cmar-vs-design-build)

**Contract types — lump sum, cost-plus, GMP, unit price, T&M**
- [Construction Contract Types — Procore Library](https://www.procore.com/library/construction-contract-types)
- [Understanding Construction Contract Types — Levvigo](https://www.levvigo.com/blog/understanding-construction-contract-types-lump-sum-cost-plus-unit-price-and-gmp)
- [4 Types of Construction Contracts — AIA Contract Documents](https://learn.aiacontracts.com/articles/183501-four-common-construction-contracts-you-need-to-understand/)
- [GMP vs Lump Sum — Superlegal](https://www.superlegal.ai/blog/gmp-contract-vs-lump-sum/)
- [Construction Contract Types — ABC PDF](https://www.abc.org/Portals/1/Documents/Membership%20Docs/MemberDiscountDocs/ContractTypes.pdf)
- [Lump Sum Contracts: Advantages, Disadvantages — NetSuite](https://www.netsuite.com/portal/resource/articles/accounting/lump-sum-contracts.shtml)

**Standard contract forms (AIA, EJCDC, ConsensusDocs)**
- [Construction Contracts Book: Analysis of AIA, ConsensusDocs, and EJCDC — ABA](https://www.americanbar.org/products/inv/book/400620307/)
- [ConsensusDocs / AIA Comparison Chart](https://www.consensusdocs.org/resources/comparison-chart/)
- [The New AIA and ConsensusDocs — NSPE](https://www.nspe.org/sites/default/files/resources/pdfs/Construction.pdf)
- [Construction Contracts: Key Differences — AGC of Minnesota](https://agcmn-c5.s3.us-east-2.amazonaws.com/5416/4195/4128/11_1345_MR4_Smith.pdf)

**Flow-down clauses and contract clauses**
- [What GCs Should Know About Flow-Down Clauses — Construction Dive](https://www.constructiondive.com/news/construction-flow-down-clauses-legal/743346/)
- [Incorporation by Reference and Flow Down Obligations — ConsensusDocs](https://www.consensusdocs.org/incorporation-by-reference-and-flow-down-obligations/)
- [Understanding Subcontract Terms and Flow-Through Clauses — Winstead](https://m.winstead.com/portalresource/lookup/wosid/cp-base-4-197504/overrideFile.name=/Understanding%20Subcontract%20Terms%20and%20Flow-Through%20Clauses.pdf)
- [Problematic Construction Contract Clauses: Flow Down — Long International](https://www.long-intl.com/blog/flow-down/)
- [Liquidated Damages in Construction — Kegler Brown](https://www.keglerbrown.com/publications/liquidated-damages-construction-guide)
- [Force Majeure in Construction Contracts & Claims — Long International](https://www.long-intl.com/blog/force-majeure/)
- [Force Majeure in Construction: 5 Steps — Sirion](https://www.sirion.ai/library/contract-clauses/force-majeure-construction/)

**Bonds and the Miller Act**
- [Subpart 28.1 — Bonds and Other Financial Protections — Acquisition.gov (FAR)](https://www.acquisition.gov/far/subpart-28.1)
- [The Miller Act | Federal Bonding Requirements — Grit Insurance](https://gritinsurance.com/bonds-surety/bond-education-center/contractor-guide-to-surety-bonding/the-miller-act/)
- [Miller Act Bonding: Requirements and Waiver — ConsensusDocs](https://www.consensusdocs.org/news/miller-act-bonding-requirements-and-waiver/)
- [Miller Act Payment Bond Claims — American Bar Association](https://www.americanbar.org/groups/construction_industry/publications/under_construction/2022/winter2022/miller-act-payment-bond-claims/)
- [Miller Act brochure — GSA](https://www.gsa.gov/system/files/miller_brochure.pdf)
- [Miller Act — Wikipedia](https://en.wikipedia.org/wiki/Miller_Act)

**Estimating, takeoff, and labor productivity**
- [Mechanical Estimating Manual: Sheet Metal, Piping (Pita)](http://www.iqytechnicalcollege.com/BAE%20690-Mechanical%20Estimating.pdf)
- [Labor Factors — Electrical Estimating 101](https://electricalestimating101.com/labor-factors/)
- [Electrical Cost Estimation: Contractor's Guide — Bids Analytics](https://bidsanalytics.com/how-to-estimate-electrical-construction-costs-a-contractors-blueprint/)
- [How to Do a Construction Takeoff for Electrical Estimators — Drawer.ai](https://drawer.ai/blog/how-to-do-a-construction-takeoff-for-electrical-estimators)
- [Commercial Electrical Estimating Guide — RSMeans](https://www.rsmeans.com/resources/commercial-electrical-estimating)
- [Calculate Electrical Labor Cost Accurately — Champion Fiberglass](https://championfiberglass.com/how-to-calculate-electrical-labor-cost/)
- [Why Accurate Industrial Takeoff Services Matter — Digital Estimating](https://digitalestimating.com/accurate-industrial-takeoff-services-matter-for-us-contractors/)

**Bidding (IFB vs. RFP) and procurement**
- [What's the Difference Between an RFP vs IFB? — BidNet](https://www.bidnetdirect.com/resources/articles/whats-the-difference-between-rfp-vs-ifb)
- [Understanding ITBs in Construction — Zebel](https://zebel.io/invitation-to-bid-in-construction/)
- [Construction Bids: ITB vs RFP — ProfitDig](https://profitdig.com/blog/construction-bids-the-differences-between-an-invitation-to-bid-vs-request-for-proposal/)
- [The ABCs of IFBs, ITBs, RFPs, RFQs, and RFIs — UNC Coates' Canons](https://canons.sog.unc.edu/blog/2010/09/01/the-abcs-of-ifbs-itbs-rfps-rfqs-and-rfis/)

**Overhead, profit, and markup**
- [Pricing the Job: Overhead, Markup, Profit — Building Advisor](https://buildingadvisor.com/project-management/bidding/pricing-the-job-overhead-markup/)
- [Typical Contractor Overhead and Profit — Planyard](https://planyard.com/blog/typical-contractor-overhead-and-profit-explained)
- [Contractor Overhead & Profit Formulas — Buildfolio](https://build-folio.com/contractor-guides/contractor-overhead-profit-guide/)
- [Markup on Subs — Markup and Profit](https://www.markupandprofit.com/articles/markup-on-subs/)

---

> **Next module:** *02 — Mechanical Systems for the Industrial GC: process piping, equipment, HVAC, fire protection.*
