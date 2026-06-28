---
title: "Industrial Construction PM, Scheduling, and Safety — GC Reference Guide"
discipline: Industrial Construction (Mechanical & Electrical)
audience: First-time GC manager / Project Engineer transitioning to PM
tags: [construction, project-management, scheduling, safety, commissioning, industrial, gc]
date: 2026-05-12
---

# Industrial Construction Project Management, Scheduling, and Safety
*A Reference for the General Contractor Managing Mechanical and Electrical Work*

This guide is written for someone stepping into a project management role at a general contractor on an industrial project — refinery, petrochemical, power plant, food and beverage, pharma, water/wastewater, or heavy manufacturing. The "industrial" qualifier matters: you will operate on or adjacent to live process equipment, your client's plant operations and safety culture will dominate your means and methods, and your mechanical and electrical scopes are typically the critical path. This document is dense by design. Treat it as a starting framework, not a substitute for site-specific procedures.

---

## 1. Project Management Fundamentals for Industrial GCs

### 1.1 Project Kickoff

The kickoff is where you protect yourself for the entire project. Anything ambiguous at kickoff becomes a fight later. Drive four artifacts to written agreement in the first two to four weeks:

- **Baseline scope.** Walk the contract, drawings, and specs and produce a one-page scope statement listing inclusions, exclusions, owner-furnished items (OFCI), contractor-furnished items (CFCI), and interface points with other prime contractors. Industrial owners frequently retain process equipment procurement (compressors, reactors, switchgear); your scope is the install, hook-up, and test. Write down who owns each.
- **Baseline schedule.** A Level 3 CPM schedule, resource-loaded if the contract requires it. Submit for owner acceptance. Baseline is sacred — once accepted, all delay analysis runs against it.
- **Baseline budget.** Cost-loaded WBS with cost codes mapped to estimate line items. Lock the contingency, allowances, and management reserve at kickoff and do not bleed into them silently.
- **Communication plan.** Who attends weekly progress meetings, who issues RFIs, who signs change orders, how submittals route, what reporting cadence the owner expects (daily reports, weekly progress, monthly schedule/cost). Distribute an RACI matrix.

Hold an **internal kickoff** (your team, including superintendent and discipline leads) before the **external kickoff** (owner, designer, key subs). The internal kickoff is where you brief risk, contract terms, and your strategy. The external kickoff is where you align expectations.

### 1.2 Organizational Chart and Roles

Industrial jobsites run on a deliberate split between the **office (PM track)** and the **field (superintendent track)**.

| Role | Primary Responsibility | Typical Span |
|---|---|---|
| Project Director / Sr. PM | Contract, owner relationship, P&L | Multi-project or mega-project |
| Project Manager | Scope, schedule, cost, change, procurement, RFIs/submittals | One project |
| Project Engineer | Document control, submittal log, RFI log, support PM | One project |
| Project Controls / Scheduler | CPM updates, EVM, cost reporting | One project or portfolio |
| Superintendent | Field execution, productivity, safety, daily plan | All field work |
| General Foreman / Area Super | Discipline (mech, elec, civil) or area execution | 20–60 craft |
| Foreman | Crew of 4–10 craft | One crew |
| Craft (journeyman/apprentice) | Pipefitter, millwright, ironworker, electrician, instrumentation tech, welder, boilermaker | Self |
| Safety Manager / Safety Officer | JHAs, audits, incident response, training | Site-wide |
| QA/QC Manager | ITPs, NCRs, NDE coordination, turnover | Site-wide |

The PM owns the **contract** with the owner. The superintendent owns the **people and the work**. They must speak daily. A common failure mode for new PMs is to encroach on means and methods — don't. Bring problems to the super, agree on a plan, then communicate to the owner.

### 1.3 Subcontractor Management

Mechanical and electrical work on industrial projects is rarely self-performed end to end. Expect to manage 8–25 subs (pipe fab, pipe erection, structural steel, insulation, painting/coatings, electrical, instrumentation, controls, scaffolding, civil, fireproofing, NDE, etc.).

- **Pre-qualification.** Before bid, qualify on EMR (target ≤ 1.0, hard limit 1.2), OSHA recordables and DART rates (TRIR ideally < 1.5 for industrial), financial capacity, bonding ability, references on similar scope, union/merit shop fit, and PSM facility experience if applicable.
- **Subcontract.** Flow down owner terms, indemnity, insurance (typical: $1M/$2M GL, $1M auto, $1M WC, $5M+ umbrella), retainage (5–10%), schedule, safety requirements, change order process, lien waivers, and OCIP/CCIP enrollment if used.
- **Sub kickoff meeting.** Held before mobilization. Cover scope clarification, schedule integration, manpower curve, submittal list, RFI process, daily reporting, safety orientation, badging, parking/lay-down, and POC list.
- **Daily coordination.** Daily 6:30 a.m. POD (plan of the day) meeting at the trailer or muster point. Each foreman commits to manpower, work fronts, permits needed, and predecessors required. The superintendent resolves conflicts on the spot.
- **Performance management.** Track sub productivity through earned hours vs. actual hours by cost code. A sub trending CPI < 0.85 for three weeks gets a written notice. Document everything; if termination becomes necessary, your file must be airtight.

### 1.4 Owner / Client Management

Industrial owners (operators, EPCs, EPCMs) are sophisticated and contract-driven. Manage them through documentation, not relationships alone.

- **RFIs (Requests for Information).** Use a controlled log with RFI #, date submitted, response-required date, status, and impact (cost/schedule). Industrial RFIs often surface drawing conflicts, missing tie-in details, or material substitutions. Respond windows are typically 5–10 working days; if late, document the impact in a notification letter — this is the basis of a future delay claim.
- **Submittals.** Shop drawings, equipment cut sheets, weld procedure specs (WPS) and procedure qualification records (PQR), welder qualifications, mill certs, paint specs, MOC (management of change) documentation, and red-line as-builts. The submittal log is a living document; track Submitted → Under Review → Approved/Approved as Noted/Revise and Resubmit.
- **Progress reporting.** Daily Construction Reports (manpower, equipment, weather, work performed, delays, visitors). Weekly progress report with three-week look-ahead. Monthly report with CPM update, EVM (CPI/SPI), cost narrative, safety stats, photos, and forecast.
- **Change orders.** See 1.7. Owner trust is built or destroyed in change order handling.

### 1.5 Document Control

This is where projects bleed money silently. Run a single source of truth — typically Procore, Aconex, BIM 360 / ACC, Bluebeam Studio, or InEight. Practices:

- **Drawing register.** Every drawing has a current revision. When Rev B supersedes Rev A, A is stamped "Superseded" and pulled from the field. A single bad revision in the field is how you build the wrong thing.
- **Spec control.** Same as drawings. Keep a controlled "Issued for Construction" (IFC) set in the trailer.
- **RFI, submittal, NCR, and change order logs.** All numbered, all dated, all routed.
- **Field markups.** Foremen mark deviations on a controlled redline set as work progresses — this feeds the as-built deliverable.
- **Transmittals.** Every formal document exchange goes through a transmittal log. If it isn't transmitted, it didn't happen.

### 1.6 Cost Control and Earned Value Management

Industrial projects live and die by EVM. The PMI / AACE framework:

- **PV (Planned Value)** — budgeted cost of work scheduled to date (BCWS)
- **EV (Earned Value)** — budgeted cost of work performed (BCWP)
- **AC (Actual Cost)** — actual cost of work performed (ACWP)
- **CV (Cost Variance)** = EV − AC. Negative = over budget.
- **SV (Schedule Variance)** = EV − PV. Negative = behind schedule.
- **CPI** = EV / AC. < 1.0 = losing money. 0.95 is yellow, 0.90 is red.
- **SPI** = EV / PV. < 1.0 = behind schedule.
- **EAC (Estimate at Completion)** = BAC / CPI (most common formula) or AC + (BAC − EV) / (CPI × SPI) for combined-performance forecast.
- **VAC (Variance at Completion)** = BAC − EAC.

Run a **cost code structure** aligned to your WBS — typical industrial uses an expanded MasterFormat or a custom code (e.g., 04-1500-PIPE-ERECT-AREA-200). Each labor hour, material PO, and sub invoice gets coded. **Weekly cost reports** to the PM include budgeted hours, earned hours, actual hours, % complete, CPI, SPI, and projected at completion (PAC) by cost code. Foremen estimate physical % complete at the end of each week — not hours burned, *work installed*.

A refinery project with 150 work packages and a $450M baseline can fail or succeed on EVM discipline alone. Monthly cadence for owner reporting, weekly internal, and biweekly for high-risk packages above ~$10M.

### 1.7 Change Order Management

A change order is the contractually authorized adjustment to scope, price, or time. Workflow:

1. **Trigger.** Owner directive, RFI response that adds scope, differing site condition, design error, force majeure.
2. **Notification.** Written notice to owner within contract timeframe (often 7–14 days from event). Miss this and you waive the claim.
3. **Pricing.** Build T&M or lump-sum estimate by cost code. Include labor (including fringes, burdens, taxes), material (with tax), equipment, sub costs, and markups.
4. **Markups.** Typical industrial GC markup stack:
   - Self-performed work: 10–15% overhead + 10% profit = ~21–26% compound
   - Subcontracted work: 5–10% overhead and profit combined
   - Bond: actual rate (0.7–1.5%)
   - Insurance: actual rate or 1–2%
5. **Negotiation.** Owner reviews, often counter-prices. Hold your number with backup documentation.
6. **Documentation.** Executed change order signed by both parties. Update budget, schedule, and EVM baseline ("rebaselining" on approved changes only).

Track **change order log** with proposed COs (PCOs), change order requests (CORs), and executed COs. Owners are sensitive to change; surprises destroy trust. Communicate verbally before the paperwork arrives.

### 1.8 Procurement and Material Management

Industrial procurement is dominated by **long-lead equipment (LLE)**:

| Item | Typical Lead Time |
|---|---|
| Major rotating equipment (large compressors, turbines) | 12–24 months |
| Heat exchangers, pressure vessels (ASME U-stamp) | 9–18 months |
| Switchgear (5kV+), MV transformers | 12–20 months |
| MCCs, large VFDs | 6–12 months |
| Large-bore alloy / stainless pipe | 4–9 months |
| Specialty valves (control, ESD) | 6–12 months |
| Cable tray, conduit, building wire (bulk) | 6–16 weeks |

Identify LLE within the first 30 days. Build a **procurement schedule** linked to the CPM with milestones: PO award, vendor drawings, FAT, ship, on site, ready for install. Assign an **expediter** to LLE; they call the vendor weekly and visit the fab shop on critical items. On site, run a **lay-down yard** with bar-coded material control. Lost material on a refinery turnaround can sink a critical path in a day.

---

## 2. Scheduling

### 2.1 Critical Path Method (CPM)

CPM is the backbone of industrial scheduling. The critical path is the longest chain of dependent activities with zero float — delay any of them and the project end date moves.

Building a CPM schedule:

1. Decompose scope into a **WBS** (see 2.2).
2. Define **activities** at a resolution of 1–20 working days each. Smaller for short-duration scopes, larger for outer years on multi-year projects.
3. Assign **durations** based on quantities × productivity rates (e.g., 0.6 manhours/LF for 2" CS pipe in pipe rack).
4. Define **logic / relationships**: Finish-to-Start (FS) is default, Start-to-Start (SS) and Finish-to-Finish (FF) with lags for parallel work. Avoid SF.
5. Run the **forward pass** to compute Early Start (ES) and Early Finish (EF), then the **backward pass** for Late Start (LS) and Late Finish (LF). Total Float (TF) = LF − EF. Critical path = activities with TF = 0 (or negative).
6. Reading the schedule: critical path activities are usually highlighted (red bars in P6). Look at TF — anything < 10 days needs daily attention. Anything with negative float means you're already late.

**Activity ID conventions** matter. Use prefixes like `M-200-FAB` (mechanical, area 200, fabrication), `E-300-TERM` (electrical, area 300, terminations), `C-100-FND` (civil, area 100, foundations). This makes the schedule readable in a glance and supports filtering and reporting.

### 2.2 Work Breakdown Structure (WBS) for Industrial Projects

A common WBS pattern:

```
Level 1: Project
Level 2: Area / Unit (e.g., Crude Unit, Cooling Tower, Substation 7)
Level 3: System (e.g., Reactor Feed, 4160V Distribution)
Level 4: Discipline (Civil, Steel, Mech, E&I, Insulation, Paint)
Level 5: Phase (Fab, Erect, Test, Turnover)
Level 6: Work Package (Iso 1234-001, Cable Schedule 480V-MCC-3)
```

Tie cost codes to WBS so a single click rolls up cost and schedule by area, system, or discipline. This is what makes EVM tractable.

### 2.3 Three-Week Look-Ahead and Daily Planning

CPM is for forecasting and contract management. **Three-week look-aheads** are for execution.

- Issued weekly by the superintendent / general foreman.
- Each activity shows crew, manpower, predecessors required (drawings IFC, materials on site, permits pulled, scaffold built), and any constraints.
- Reviewed at the **weekly POD (Plan of the Day)** with foremen.
- Drives **daily work plans / Pre-Task Plans (PTPs)** issued each morning at toolbox talks.

Last Planner System / Lean Construction principles work well here: weekly work plans with **Percent Plan Complete (PPC)** tracked — aim for > 80%. Below that, root-cause the misses (manpower, materials, info, prerequisites, weather, safety, other).

### 2.4 Resource-Loaded Schedules

Owners on large industrial projects (especially DOE, federal, EPC contracts) require resource-loaded schedules in P6. Each activity carries:

- Labor hours by craft (pipefitter, electrician, etc.)
- Equipment (crane hours)
- Cost

Resource histograms show **manpower curves** — when you'll peak crew (e.g., 280 craft in month 14). This drives badging, parking, lay-down sizing, sanitary facilities, and bus schedules. Industrial sites are crew-density constrained — exceed your work-front capacity and productivity collapses (the "stacking of trades" curse).

### 2.5 Schedule Delay Analysis

Disputes about who caused delay are settled with documented analysis. Common methods (AACE Recommended Practice 29R-03):

- **As-planned vs. as-built.** Overlay baseline on actual. Simple but crude.
- **Impacted as-planned.** Insert delay events into baseline; show new completion.
- **Collapsed as-built (but-for).** Remove delay events from as-built; show what would have happened.
- **Time impact analysis (TIA).** Insert delay fragnet into a contemporaneous schedule update; rerun CPM. Industry standard for prospective delay claims.
- **Windows analysis.** Split project into windows (monthly typically); analyze critical path movement in each.

**Concurrent delay** — when both owner and contractor cause delay in the same time window — typically results in time extension without compensable damages. **Float consumption** rules differ by contract: some say "float belongs to the project" (whoever uses it first), others give it to the owner. Read your contract.

### 2.6 Recovery Schedules

When you're > 10% behind, the owner will demand a recovery plan:

- **Re-sequence** non-critical work to free up critical-path crews.
- **Add resources** to critical-path activities (watch the Brooks' Law trap — adding bodies to a late task can slow it).
- **Shift work** — go to 10s, 6-10s, double shifts, or 24/7. Productivity drops ~5–15% on 2nd shift, ~20–30% on extended OT after 4 weeks (MCAA productivity loss factors).
- **Premium overtime.** Track cost separately for potential recovery.
- **Re-engineer.** Modularize, prefab off-site, change construction method.

### 2.7 Milestone Schedules

Owner-facing summary at Level 1 or 2 with 15–40 key dates: NTP, IFC drawings, major equipment deliveries, foundations complete, steel erection complete, mechanical completion by system, energization, hydrotest complete, ready for commissioning, RFSU (ready for startup), substantial completion, final completion. Update monthly.

### 2.8 Primavera P6 vs. MS Project

| Feature | Primavera P6 | MS Project |
|---|---|---|
| Industrial / EPC standard | Yes (de facto) | Rare |
| Resource loading and leveling | Excellent | Adequate |
| Multi-project / enterprise | Native (EPS, OBS) | Limited |
| User interface | Steep learning curve | Friendlier |
| Cost | $$$$ (per-seat or cloud) | $ |
| Integration with EVM/cost systems | Strong (Unifier, Ecosys) | Weak |
| Typical use | Refineries, power, infrastructure | Small commercial, internal |

If you're going to a refinery, power, midstream, or large EPC environment, **learn P6**. Take an Oracle University class or an industry course. MS Project is fine for small fast-track projects but won't satisfy an industrial owner's controls organization.

### 2.9 Tie-In and Outage Planning

The hardest scheduling problem on a brownfield industrial project is the **tie-in window** — the period when plant operations shuts down (turnaround / TAR) and you can cut into live systems. Outages are budgeted in days and measured in millions of dollars of lost production per day.

- Tie-in scopes are sequenced backward from the cutover date with hour-level granularity.
- Pre-fab everything possible — bring tie-in spools complete with WPS-qualified welds, tested upstream.
- Stage all material, tools, and rigging in advance.
- Run a **tie-in walkdown** with operations 30 days, 14 days, and 48 hours before.
- Build a **tie-in matrix**: each tie-in has a number, location, isolation boundary, LOTO points, blinds list, blind installer, removal sequence, hydro requirements, and reinstatement responsibility.
- Track **TAR hour-by-hour** in a war room. A 14-day TAR has zero room to slip.

---

## 3. Safety Management on Industrial Jobsites

Industrial safety is not a paperwork exercise. Operating plants kill people — your job is to send everyone home every day. The frameworks below are the floor, not the ceiling.

### 3.1 OSHA 29 CFR 1926 — Construction Standards (Primary)

For construction work — including additions, alterations, demolition, painting — 1926 applies. Key subparts for industrial mechanical/electrical:

| Subpart | Topic | Key References |
|---|---|---|
| C | General Safety & Health | 1926.20–.35 |
| D | Occupational Health | Hazcom, IH |
| E | PPE | 1926.95–.107 |
| K | Electrical | 1926.400–.449 (including LOTO at 1926.417) |
| L | Scaffolds | 1926.450–.454 (4 ft trigger height) |
| M | Fall Protection | 1926.500–.503 (6 ft trigger height) |
| N | Cranes, Derricks, Hoists | 1926.1400 series (CDAC standard) |
| O | Motor Vehicles, Mechanized Equipment | 1926.600 series |
| P | Excavations | 1926.650–.652 (5 ft protective system trigger) |
| Q | Concrete and Masonry | 1926.700 series |
| R | Steel Erection | 1926.750–.761 (15 ft fall arrest on iron) |
| V | Power Transmission | High-voltage work |
| AA | Confined Spaces in Construction | 1926.1200 series (replaces general industry deference) |
| Z | Toxic Substances | Silica (1926.1153), lead, asbestos |

Fall protection above 6 feet, fall arrest or restraint required. Excavation protection required at 5 feet (or by competent person below). Scaffolds require competent-person erection and tagging. **Confined Space in Construction (Subpart AA, 2015)** introduced permit-required confined space rules specifically for construction — separate entry supervisor, attendant, entrant, rescue plan, atmospheric testing (O₂ 19.5–23.5%, LEL < 10%, H₂S < 10 ppm, CO < 25 ppm typical).

### 3.2 OSHA 29 CFR 1910 — General Industry (When It Applies)

1910 applies when you are performing **maintenance** rather than construction, when working as a contractor inside operating units, or when host employer standards govern (multi-employer site doctrine). Practical implication: during a plant turnaround, you may be cited under either 1910 or 1926 depending on the nature of the task. Key 1910 standards you'll touch:

- **1910.119 — Process Safety Management (PSM).** Applies to facilities with covered highly hazardous chemicals above threshold quantities. Drives MOC, PSSR (pre-startup safety review), and contractor selection.
- **1910.146 — Permit-Required Confined Spaces (general industry).** Host facility's CSE procedures may apply.
- **1910.147 — Control of Hazardous Energy (LOTO).** Often used as the standard even on construction work because host plant procedures dominate.
- **1910.269 — Electric Power Generation, Transmission, Distribution.** When working on utility-owned equipment.
- **1910.1200 — Hazard Communication.** SDSs, labels, training.

The **multi-employer citation policy** means OSHA can cite the GC as a "controlling employer" for hazards exposed to *any* employee on site, even your sub's workers. Inspect everyone.

### 3.3 Site-Specific Safety Plan (SSSP) and JHA/JSA

Every industrial project requires a written SSSP, approved by the owner before mobilization. Contents:

- Project description, organizational chart, emergency response plan, muster points, evacuation routes
- Hazard analysis by phase (sitework, structural, mechanical, electrical, commissioning)
- Required permits and procedures
- Subcontractor safety expectations and oversight protocol
- Training matrix (OSHA 10/30, site-specific orientation, refreshers)

**Job Hazard Analysis (JHA)** — sometimes called JSA — is a task-level breakdown:

1. Break task into steps
2. Identify hazards at each step (energy types, materials, environment, ergonomics)
3. Define controls per hierarchy: **Elimination → Substitution → Engineering → Administrative → PPE**
4. Reviewed and signed by crew before work, posted at work front

Daily **Pre-Task Plan (PTP)** is a JHA refresh customized to today's actual conditions, weather, crew, and adjacent work.

### 3.4 Permit-to-Work Systems

Operating plants run on permits. The GC's site safety officer typically coordinates daily permit pulls with plant operations.

- **Hot Work Permit.** Required for welding, grinding, cutting, torch work, anywhere fire could ignite flammables. Pre-task gas test, fire watch present, watch held 30–60 min after work (firewatch hold), combustibles cleared 35 ft, fire extinguisher staged.
- **Confined Space Entry (CSE) Permit.** Atmospheric tests, attendant assigned, rescue plan, communication, blinds/LOTO verified, permit posted at entrance.
- **Lockout/Tagout (LOTO).** Energy isolation: electrical, hydraulic, pneumatic, steam, process fluid, gravity, stored energy. Each affected worker applies their own lock. Verify zero-energy state before work. Group LOTO via a lockbox is common for large crews.
- **Line Break / Vessel Entry.** Process line cuts require draining, depressurization, flushing/purging, blinding, and a written line-break permit naming the blind location and signed by operations.
- **Excavation Permit.** Underground utility clearance (one-call, ground-penetrating radar, hand-dig within tolerance), competent person daily inspection, soil classification, protective system.
- **Working at Heights / Scaffold Permit.** Some sites; especially for mobile elevated work platforms (MEWPs).
- **Energized Electrical Work (NFPA 70E).** Arc-flash hazard analysis, PPE category, energized work permit signed by host facility.

### 3.5 Process Safety for Operating Plants

If the host plant is PSM-covered (refineries, petrochemical, large chlorine, ammonia, some grain), your work falls under their PSM program:

- **MOC (Management of Change).** Any deviation from existing plant configuration requires an MOC — even temporary scaffolding over a relief device line. MOCs route through plant engineering, operations, and safety before work proceeds.
- **PSSR (Pre-Startup Safety Review).** Before reintroducing process to a modified or new unit, a PSSR confirms construction matches drawings, P&IDs are red-lined as-built, training is complete, procedures exist, safety systems are tested. The GC typically owns the construction-side checklist.
- **HAZOP awareness.** The HAZard and OPerability study is the owner's design-stage hazard review. As a GC you don't run HAZOPs, but you should know whether your scope was HAZOP'd and whether your install matches the HAZOP outcome. Field deviations that affect process safety must be MOC'd.

### 3.6 Incident Reporting and Recordkeeping

- **Near-miss program.** Anonymous reporting, no-blame, rewarded. Industrial best-practice ratio: 600 near-misses : 30 first aid : 10 recordable : 1 lost time : 1 fatality (Heinrich/Bird). If near-miss reports are low, your reporting culture is broken, not your safety performance.
- **OSHA 300 / 300A logs.** Recordables tracked on the 300 log; annual summary posted Feb 1–Apr 30 on the 300A.
- **EMR (Experience Modification Rate).** Workers' comp insurance multiplier based on three-year loss history. Industrial owners prequalify subs at EMR ≤ 1.0; many won't allow > 1.2.
- **TRIR (Total Recordable Incident Rate)** = (recordables × 200,000) / hours worked. Target < 1.0 on best-in-class industrial.
- **DART (Days Away, Restricted, Transferred)** = subset of TRIR. Target < 0.5.
- **Reportable events.** Fatality → 8 hours to OSHA. Inpatient hospitalization, amputation, loss of eye → 24 hours.

### 3.7 Subcontractor Safety Oversight

- Daily safety walks by the GC safety officer, signed off in a log
- Weekly all-hands safety meeting (toolbox talk on a chosen topic)
- Monthly safety committee with sub representation
- **Stop-Work Authority** — anyone, including the most junior apprentice, can halt work without retaliation. Train it, advertise it, reward use of it.
- Pre-task plans collected daily and audited
- Behavior-based safety observation programs (STOP, SafeStart) when contractually required

### 3.8 Industrial Hygiene

- **Asbestos.** Pre-existing in older plants (insulation, gaskets, transite). Surveyed before demo; abated by licensed contractor; air monitoring per 1926.1101.
- **Lead paint.** Common on older structural steel and process equipment. 1926.62 triggers exposure assessment, respirator, hygiene facilities.
- **Silica.** 1926.1153 (Table 1 controls or exposure assessment); cutting concrete and masonry is prevalent.
- **H₂S.** Refineries, sour gas, wastewater. Continuous personal monitors, fixed-area monitors, escape SCBA, evacuation drills. Action level often 5 ppm, evacuation 10 ppm.
- **Benzene, hexavalent chromium, welding fume, NORM** (naturally occurring radioactive material in scale) — site-specific assessments required.
- **PPE baseline (industrial).** Hard hat, ANSI Z87 safety glasses, FR coveralls (NFPA 2112 / ASTM F1506 ≥ 8 cal/cm² Arc Rating typical), leather gloves with task-specific overgloves, steel-toe boots, hearing protection in posted areas, H₂S monitor where applicable, fall protection harness when working at height.

### 3.9 Crane and Rigging Safety

OSHA 1926 Subpart CC (1926.1400–.1442). Key practices:

- **Operator certification.** NCCCO or equivalent.
- **Annual third-party inspection** plus monthly documented inspection plus daily pre-shift walkaround.
- **Lift plans for every lift.** Standard lift plans (cookie-cutter) for routine work; **engineered critical lift plans** when:
  - Load > 75% of crane capacity at the radius
  - Tandem (two-crane) lifts
  - Lifts over occupied buildings, pipe racks with live process, control rooms
  - Personnel platforms (1926.1431)
  - Blind picks
- **Critical lift plan content.** Crane make/model, configuration (boom length, jib, counterweight), rated capacity at radius, load weight + rigging weight, ground bearing pressure, outrigger pad design, swing path, communication plan, weather limits, all riggers/operator/signal person named.
- **Rigging hardware inspection.** Slings tagged with capacity, inspected each shift for damage. Removed from service for cuts, kinks, heat damage, missing tags.
- **Pre-lift meeting** mandatory for multi-crane or critical lifts. Everyone signs.
- **Ground conditions.** GC is responsible for adequate ground per 1926.1402 — crane mat design where bearing pressure exceeds soil capacity. Get a geotech opinion on soft ground or near excavations.

---

## 4. Quality Control and Commissioning

### 4.1 Inspection and Test Plans (ITPs)

An ITP is a system-by-system or component-by-component matrix listing every inspection and test required, the standard, the responsible party, the hold/witness points, and the acceptance criteria.

Example row (welding):
| # | Activity | Standard | Frequency | Acceptance | Responsibility | H/W/M/R |
|---|---|---|---|---|---|---|
| 12 | Visual weld inspection | AWS D1.1 | 100% | Per code | CWI | M |
| 13 | RT (radiography) | ASME B31.3 | 10% random | Per code | NDE sub | W |
| 14 | Hydrotest | ASME B31.3 | Each system | 1.5× design pressure × 10 min hold | GC | H |

**H/W/M/R** = Hold point (work stops until inspector witnesses), Witness, Monitor, Review-only.

The PM and QC manager build the ITP register from the specs, get it approved by the owner and any third-party inspectors (often AI — Authorized Inspector for ASME work, or insurance-required inspectors), and run the project against it.

### 4.2 Non-Conformance Reports (NCRs)

When work does not meet specification, raise an NCR:

1. Identify and quarantine
2. Disposition options: **Use-as-is, Rework, Repair (with engineering approval), Reject/Replace**
3. Engineer/owner reviews disposition
4. Root cause analysis (5 Whys or fishbone) for systemic issues
5. Corrective and preventive action (CAPA)
6. Close-out signed by QC and owner

NCRs are a leading indicator of QC health — too few suggests inspection gaps, too many suggests workmanship problems. Trend by sub and by cost code.

### 4.3 Third-Party Inspection

Owner-paid or insurance-required inspectors witness critical activities:

- **NDE (Non-Destructive Examination)** — VT (visual), MT (magnetic particle), PT (dye penetrant), UT (ultrasonic), RT (radiographic), PMI (positive material ID), hardness testing, ferrite testing. ASNT SNT-TC-1A Level II/III certified technicians.
- **Authorized Inspector (AI)** for ASME Section I (boilers), Section VIII (pressure vessels), B31.3 (process piping). Stamps the manufacturer's data report. National Board commissioned.
- **Hydrostatic test witnessing.** Pressure held per code, pressure decay limits, calibrated gauge. Pneumatic test in lieu of hydro is permitted only with engineered exclusion zones.
- **Factory Acceptance Test (FAT).** Witness equipment performance at the vendor shop before ship — large rotating equipment, switchgear, MCCs, control panels, packaged systems. Saves enormous field rework.
- **Site Acceptance Test (SAT).** Performance verification after installation, before commissioning.

### 4.4 Punch Lists

The punch list is the running record of work that is *substantially* complete but has minor defects.

- **A-items** — must be completed before mechanical completion / system turnover (anything affecting safety, code, function, performance).
- **B-items** — may be completed after MC but before substantial completion (cosmetic, accessibility, documentation, minor leaks).
- **C-items** — sometimes used for final cleanup, painting touch-up, post-startup access work.

Walk the system with the owner's representative, log items in a controlled tracker (Procore, Field, BlueBeam), assign responsibility and due date, retest, sign off. Aged punch is the death of a project — track it weekly.

### 4.5 Pre-Commissioning vs. Commissioning vs. Startup

The boundary between construction and operations is the most contentious phase. Understand the four phases:

| Phase | Activities | Lead | GC Role |
|---|---|---|---|
| Construction | Install, weld, terminate | GC | Owner |
| Pre-Commissioning | Flushing, cleaning, blowing, pickling, drying, point-to-point loop check, motor solo run, instrument calibration, hydrotest, megger, hi-pot | GC (often) | Lead |
| Commissioning | System energization, no-load testing, function testing with utilities (water, air, N₂), control loop tuning, alarm and trip testing | Commissioning team (owner or 3rd party) | Support, provide labor |
| Startup | Introduce process fluids, ramp to rated capacity, performance test runs | Operations | Standby support, warranty |

**Mechanical Completion (MC)** is the formal handoff between Construction and Commissioning, system by system. The system has been built per drawings, tested at the cold-loop level, punch list down to A=0 / B-minor. The MC certificate transfers care, custody, and control for that system.

**Substantial Completion** is later — the project (or contracted scope) is capable of beneficial use. Triggers the warranty period, releases most retainage, ends liquidated damages exposure.

**Final Completion** comes after the punch list is fully cleared and all turnover documents are accepted.

### 4.6 Systems Turnover Documentation

The **turnover package (TOP)** is the formal deliverable that proves the system was built correctly and is ready for the owner. A complete TOP for a piping/mechanical system typically includes:

- ITP with all signed inspection records
- Mill test reports (MTRs) and material certificates of compliance
- Welder qualifications (WPQ) and weld procedure specs (WPS/PQR)
- Weld map / weld log with NDE results indexed by weld number
- Hydrotest packages (test boundary sketch, gauge calibration cert, chart, signed test record)
- PMI reports for alloy systems
- NCR log (closed)
- Punch list (closed A-items)
- Red-line drawings showing as-built deviations
- Equipment data sheets and serial numbers

Electrical systems add: megger results, hi-pot results, cable schedules with terminations verified, torque records, relay setting sheets, breaker test records, ground continuity records, arc-flash labels installed.

Beyond the technical turnover package, the GC delivers:

- **As-built drawings** — clean CAD update from field redlines.
- **O&M (Operations & Maintenance) Manuals** — vendor manuals, spare parts lists, lubrication schedules, recommended PM intervals, troubleshooting guides. Bound (physical and electronic), indexed.
- **Training records** — owner operators and maintenance trained per spec.
- **Warranty letters** — vendor warranties consolidated with effective dates.
- **Final lien waivers** from all subs and suppliers.

Build the turnover package **as you go**, not at the end. Owners increasingly tie progress payments to TOP completion percentages — a piping system at 95% installed but with 0% turnover documentation may be 50% billable.

---

## Closing Notes

Three habits separate good industrial PMs from struggling ones:

1. **Write everything down, on the day it happens.** Daily logs, RFIs, notifications. The project that has good documentation wins the disputes.
2. **Walk the job every day.** You cannot manage from the trailer. Walk with the superintendent, talk to foremen, look at the work.
3. **Treat safety as a leading metric, not a lagging one.** Near-misses, observations, JHA quality, permit compliance — these predict the outcome. Recordables only tell you what already went wrong.

Industrial construction is unforgiving. Process plants are operated by people whose livelihoods depend on uptime, whose safety depends on your install quality, and whose patience for excuses is zero. Show up early, document obsessively, respect operations, and protect your craft. The rest is detail.

---

## Sources

- [OSHA 29 CFR 1926 (Construction Standards)](https://www.osha.gov/laws-regs/regulations/standardnumber/1926)
- [OSHA 29 CFR 1910 (General Industry Standards)](https://www.osha.gov/laws-regs/regulations/standardnumber/1910)
- [OSHA Standard Interpretation — Application of 1910 and 1926 to Operating Plant Services](https://www.osha.gov/laws-regs/standardinterpretations/1991-02-19)
- [OSHA 1926.1400 — Cranes and Derricks in Construction (Scope)](https://www.osha.gov/laws-regs/regulations/standardnumber/1926/1926.1400)
- [OSHA Cranes, Derricks and Hoist Safety Standards](https://www.osha.gov/cranes-derricks/standards)
- [Comparing OSHA General Industry 1910 vs Construction 1926](https://osha-safety-training.net/blogs/news/comparing-osha-general-industry-1910-vs-construction-1926-printed-regulation-manuals-for-compliance-managers)
- [Construction vs. General Industry Standards (Safety Resources)](https://www.safetyresources.com/safety-blog/construction-vs-general-industry-standards)
- [Key OSHA Standards for Oil and Gas Facilities](https://osha-safety-training.net/blogs/news/key-osha-standards-and-compliance-for-oil-and-gas-facilities-a-comprehensive-guide)
- [Crane Lift Plan (NSSGA)](https://www.nssga.org/sites/default/files/2023-01/Crane_Lift_Plan.pdf)
- [Mechanical Completion, Substantial Completion, Final Completion — Commissioning & Assurance Academy](https://commissioningandstartup.com/mechanical-completion-substantial-completion-final-completion/)
- [The True Meaning of Mechanical Completion — Audubon Companies](https://auduboncompanies.com/the-true-meaning-of-mechanical-completion/)
- [Earned Value Method (EVM) for Construction Projects — MDPI Buildings](https://www.mdpi.com/2075-5309/12/3/301)
- [Earned Value in Construction — Gather Insights](https://www.gatherinsights.com/en/earned-value)
- [Differences of EVM Practices in Construction — PMI](https://www.pmi.org/learning/library/differences-earned-value-management-practices-construction-5790)
- [Best Practices for Primavera P6 CPM Scheduling — Leopard Project Controls](https://consultleopard.com/best-practices-for-primavera-p6-cpm-scheduling/)
- [Oracle Primavera P6 EPPM](https://www.oracle.com/construction-engineering/primavera-p6/)
- [Introduction to CPM Scheduling using Primavera P6 (NYSDOT Manual)](https://www.dot.ny.gov/main/business-center/contractors/construction-division/construction-repository/NYSDOT_P6CLIENT_Training_Manual.pdf)
- AACE International Recommended Practice 29R-03 — Forensic Schedule Analysis
- NFPA 70E — Standard for Electrical Safety in the Workplace
- ASME B31.3 — Process Piping Code
- AWS D1.1 — Structural Welding Code
- MCAA Bulletin — Factors Affecting Labor Productivity
