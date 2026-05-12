---
title: "Reading and Interpreting Construction Specifications"
module: 24
discipline: ["specifications", "CSI", "MasterFormat", "quality-control", "contracts"]
audience: "Residential GC — field-experienced but unfamiliar with formal project specifications"
status: "reference"
tags: [career-training, specifications, CSI, MasterFormat, Division01, submittals, quality-control, contracts]
created: 2026-05-12
---

# Reading and Interpreting Construction Specifications

> **Bottom line up front:** Drawings show **where** and **what**. Specifications define **how**, **with what**, **to what standard**, and **with what proof**. Both are part of the contract. Both are legally binding. If you have built homes for years using only drawings and a handshake conversation with the architect, you have been doing half the reading. The other half — the spec book — is where most quality disputes, change-order arguments, and back-charges actually live. This guide makes you fluent enough to scope, bid, manage subs, and defend your work using the spec.

---

## 1. Why Specifications Matter to the GC

### 1.1 Specs vs. Drawings — Two Halves of the Same Instruction

| Drawings show | Specifications define |
|---|---|
| Geometry — location, dimensions, elevations | Material — product, grade, manufacturer, standard |
| Quantity — how many, how big | Quality — performance level, acceptable tolerances |
| Relationships — what connects to what | Method — how it gets installed, in what order, by whom |
| Visual configuration | Verification — testing, inspections, submittals, warranties |
| The "noun" of the project | The "adjective and verb" of the project |

A drawing shows a 2x6 exterior wall with R-21 insulation. The spec tells you:
- The species and grade of the 2x6 (SPF #2 vs. Doug Fir #1)
- Maximum moisture content at installation (often 19% for framing)
- Whether the studs must be kiln-dried, FSC-certified, or fire-treated
- The exact insulation product class (unfaced batt, faced batt, mineral wool, dense-pack cellulose)
- The ASTM standard the insulation must meet
- How it gets installed (friction fit, no compression, vapor retarder side)
- Who inspects it before drywall closes it in

**You cannot bid, build, or defend the wall using drawings alone.**

### 1.2 Legal Weight — "I Didn't Read the Spec" Is Not a Defense

In a standard AIA A101 / A201 contract (and most modified residential agreements), the **Contract Documents** typically include:

1. Agreement (the contract itself)
2. General Conditions (often AIA A201)
3. Supplementary Conditions
4. **Specifications**
5. **Drawings**
6. Addenda issued before execution
7. Modifications issued after execution (change orders, ASIs, etc.)

All seven are equally binding. Courts and arbitrators treat the spec as part of the contract you signed. If the spec says "all sealants shall be Class 25 per ASTM C920," and you installed Class 12, you breached the contract — even if the drawings did not mention sealant class. **Constructive notice is presumed.** You are deemed to know what is in the documents you signed.

The corollary: when you sign the contract, you should know what you signed up for. The hour you spend reading the spec before signing is the cheapest hour you will spend on the job.

### 1.3 How Specs Affect Cost

Specs frequently contain hidden cost drivers that do not appear on drawings:

| Cost driver hiding in the spec | Typical impact |
|---|---|
| Higher-grade concrete (4000 PSI vs. 3000) | 8–15% on concrete |
| Air-entrained concrete for exterior flatwork | 5–10% premium |
| Special inspections paid by contractor | $1,500–$8,000 per discipline |
| Concrete cylinder testing (1 set per 50 CY or 5,000 SF) | $50–$120 per set, multiple sets per pour |
| Mock-ups (masonry panel, full bathroom, exterior assembly) | $1,500–$25,000 |
| Submittal preparation by subs (shop drawings) | Built into sub price — but expedites can be GC cost |
| Performance bond / payment bond | 0.5–2% of contract |
| Specified products with single source (e.g., "Marvin Ultimate only") | Variable; can be 20–40% over builder-grade |
| Level 5 drywall finish | 30–60% over Level 4 |
| Cleaning, protection, dumpsters, temp utilities | 1–3% of project, often missed |
| Field-applied air-barrier with mandated testing | $2–$6 per SF of exterior wall |
| Closeout: O&M manuals, training, attic stock | Several days of PM time |

**If you missed it in the spec, you absorb the difference.** This is the single most common bid mistake made by GCs moving from custom-build word-of-mouth work into formally specified projects.

### 1.4 Quality Disputes — The Spec Is the Reference Document

When the architect walks the job and says "that's not what we specified," your three possible responses are:

1. **"You're right, we'll fix it."** (You owe the rework.)
2. **"The spec says X, we installed X. Show me where it says otherwise."** (You owe nothing.)
3. **"The spec is ambiguous between X and Y. Let's RFI it."** (Open question — possibly a change order.)

You can only give responses 2 and 3 if **you actually know what the spec says.** If you do not, your only honest response is #1, and you eat the cost. Most GCs lose quality disputes not because they were wrong, but because they could not cite the spec back at the architect with confidence.

### 1.5 Conflicts Between Drawings and Specs

Drawings and specs disagree more often than you'd think — different people draft them, sometimes months apart, with imperfect coordination. The contract documents typically include an **order of precedence** clause. Common variants:

| Precedence rule | What it means |
|---|---|
| "Most restrictive governs" (most common in residential) | If the spec requires R-30 and the drawing notes R-21, you owe R-30 |
| Specifications govern drawings | Spec wins on conflict |
| Drawings govern specifications | Drawing wins (rare in modern contracts) |
| Detailed drawings govern general drawings; large-scale governs small-scale | For drawing-to-drawing conflicts |
| Written dimensions govern scaled dimensions | Never scale drawings |

**Always find and read the order-of-precedence clause** — it is usually in the General Conditions (A201 §1.2) or Supplementary Conditions, sometimes echoed in Division 01.

When you find a conflict during the project, **issue an RFI immediately.** Do not unilaterally pick the cheaper interpretation — even if "most restrictive governs" is not in your contract, the architect can argue you knew of the conflict and chose to ignore it. RFI it, get a written answer, and price the delta as a change if applicable.

---

## 2. CSI MasterFormat — The Organizing System

### 2.1 History and Purpose

The **Construction Specifications Institute (CSI)** and **Construction Specifications Canada (CSC)** jointly publish **MasterFormat** — the dominant numbering system for North American construction specifications since 1963. The current 50-division structure (Divisions 00–49) was introduced in 2004, replacing the older 16-division format. Most residential specs you encounter today follow this system, even if loosely.

**Why a standardized system matters:**
- Subcontractors know where to find their scope without reading the whole book.
- Estimators can map costs to standard cost codes (often the same numbers).
- Specs from different architects on different projects are organized the same way.
- The numbering is the index — Section 09 91 23 always means "Interior Painting" regardless of project.

### 2.2 Structure — Levels of Hierarchy

MasterFormat numbers use a six-digit format, organized hierarchically:

```
09 91 23
│  │  │
│  │  └── Level 3: specific work result (e.g., Interior Painting)
│  └───── Level 2: family of work (e.g., Painting)
└──────── Level 1: Division (e.g., 09 Finishes)
```

| Level | Example | Meaning |
|---|---|---|
| Level 1 (Division) | **09** Finishes | The major work category |
| Level 2 | **09 90** Painting and Coating | The family within the division |
| Level 3 | **09 91 23** Interior Painting | The specific work result |
| Level 4 (optional) | **09 91 23.13** Wood Surface Interior Painting | Further refinement, rarely used in residential |

### 2.3 The 50 Divisions — Quick Reference

| Group | Divisions | Coverage |
|---|---|---|
| Procurement & Contracting | 00 | Bidding, contracts, conditions |
| General Requirements | 01 | Project-wide requirements |
| Facility Construction Subgroup | 02–14 | Site, structure, enclosure, interiors |
| Facility Services Subgroup | 21–28 | Fire suppression, plumbing, HVAC, electrical, communications, security |
| Site & Infrastructure Subgroup | 31–35 | Earthwork, exterior improvements, utilities |
| Process Equipment Subgroup | 40–49 | Industrial — generally not used in residential |

### 2.4 Key Divisions for the Residential GC

| Division | Title | What's in it for a residential GC |
|---|---|---|
| **00** | Procurement & Contracting Requirements | Invitation to bid, instructions to bidders, bid form, contract form (often AIA A101 or A105 for residential), General Conditions (A201), Supplementary Conditions, bond and insurance requirements |
| **01** | **General Requirements** | The GC's operating manual — submittals, RFIs, change orders, payment, schedule, safety, temporary facilities, closeout. **Read this completely, every project.** |
| **02** | Existing Conditions | Site survey, geotechnical report references, hazmat (asbestos, lead) abatement, selective demolition |
| **03** | Concrete | Footings, foundations, slabs, mix designs, rebar, formwork, curing |
| **04** | Masonry | CMU foundation, brick veneer, stone, mortar, flashing, ties |
| **05** | Metals | Structural steel, steel joists, ornamental rails, light-gauge framing (sometimes) |
| **06** | Wood, Plastics, and Composites | Rough framing, sheathing, engineered lumber (LVL, PSL, I-joists), finish carpentry, millwork, cabinets, countertops |
| **07** | **Thermal & Moisture Protection** | Insulation, WRB, air barriers, roofing, flashing, sealants, firestopping. **Heavy concentration of moisture-failure liability lives here.** |
| **08** | Openings | Doors (wood, metal, glass), windows, skylights, frames, hardware, glazing, garage doors |
| **09** | Finishes | Drywall, plaster, tile, stone, wood floors, resilient flooring, carpet, paint, acoustic ceilings |
| **10** | Specialties | Bath accessories, fireplace surrounds, lockers, mailboxes, address numbers, signage, partitions |
| **11** | Equipment | Residential appliances (ranges, refrigerators, washers, dryers), pool equipment, garage equipment |
| **12** | Furnishings | Window treatments, built-in seating, manufactured casework (sometimes) |
| **13** | Special Construction | Saunas, swimming pools, integrated assemblies |
| **14** | Conveying Equipment | Residential elevators, dumbwaiters |
| **21** | Fire Suppression | Residential sprinklers (NFPA 13D for one- and two-family) |
| **22** | **Plumbing** | DWV, supply, fixtures, water heaters, gas piping |
| **23** | **HVAC** | Equipment, ductwork, controls, ventilation, refrigerant piping |
| **26** | **Electrical** | Service, branch circuits, devices, lighting, panelboards |
| **27** | Communications | Structured cabling, AV pre-wire |
| **28** | Electronic Safety & Security | Alarm, access control, surveillance |
| **31** | Earthwork | Excavation, fill, compaction, shoring, erosion control |
| **32** | Exterior Improvements | Paving, curbs, fencing, retaining walls, planting, irrigation |
| **33** | Utilities | Site water, sewer, storm, electrical service to building |

### 2.5 Navigating an Unfamiliar Spec

Five-step routine when handed a new spec book:

1. **Open the Table of Contents.** Skim the section numbers. Note which divisions are present and which are missing — missing divisions often mean owner-direct, or scoped to a different prime contractor.
2. **Read Division 00 first.** Bid form, contract form, supplementary conditions, bond/insurance — these set the financial and legal frame.
3. **Read Division 01 completely.** Every section. Yes, all of it. This is where the project-specific procedures live.
4. **Skim Part 1 of every other section in your scope.** Part 1 tells you what is being specified, what submittals are required, and what references apply. You can defer Parts 2 and 3 to bid finalization.
5. **Cross-reference sections to drawings.** Most spec sections include a "Related Sections" clause that points to adjacent sections. Use the spec section number on the drawing keynotes (e.g., "Roofing per 07 31 13") to land in the right spec section.

---

## 3. Division 01 — General Requirements in Depth

### 3.1 Why Division 01 Is the Most Important Section to Read

Division 01 applies **to every other division.** Every requirement in Division 01 modifies every product and execution section in the book. It is also the section most often **modified by the specific project** (vs. boilerplate sections from a master spec system like ARCOM/SpecLink). If the owner has a quirk — special billing format, mandated subcontractors, specific safety protocols, weekly photo submissions — it is in Division 01.

Read it cover to cover. Twice. The first time to understand the rules; the second time to extract a checklist of things you must do.

### 3.2 Major Division 01 Sections — Reference Table

| Section | Title | What it controls | Key things to extract |
|---|---|---|---|
| **01 10 00** | Summary | Project description, work covered, phasing, owner-furnished items, work sequencing, owner occupancy during construction | Scope you may have missed; items "by Owner" you do **not** install; sequence constraints (e.g., owner moves in second floor while you finish first) |
| **01 20 00** | Price and Payment Procedures | Schedule of values format, application for payment (often AIA G702/G703), retainage rate, stored material billing rules, allowances, alternates, unit prices | Retainage percentage, how to bill stored material (insurance, storage location, bill of sale), allowance carry amounts, alternate pricing requirements |
| **01 25 00** | Substitution Procedures | How to request a substitution to specified products, what documentation, time limits, fees | Cutoff date (often "no substitutions accepted after 30 days post-NTP"); required submittal package; whether you pay redesign costs if substitution requires it |
| **01 26 00** | Contract Modification Procedures | Field orders, construction change directives (CCDs), change order process, documentation requirements, overhead and profit markups | OH&P % on changes (often 10% OH + 5% P for self-performed, 5% on sub change orders); time-and-materials documentation rules; CCD vs. CO distinction |
| **01 29 00** | Payment Procedures | Detailed billing rules (sometimes merged with 01 20 00) | Same as 01 20 00 |
| **01 30 00** | Administrative Requirements | RFI process and form, meetings required, submittal procedures, document control, project record documents | RFI response time (typical 7–10 business days — but you must request in writing); pre-construction meeting attendees; OAC meeting frequency; pre-installation conference list |
| **01 31 19** | Project Meetings | Pre-construction, OAC (Owner-Architect-Contractor), pre-installation conferences | Who attends, who chairs, minutes responsibility |
| **01 32 00** | Construction Progress Documentation | Schedule format (CPM, bar chart), updates, photographs, daily reports | Whether a full CPM is required; update frequency; photo requirements (digital, geo-tagged, weekly) |
| **01 33 00** | Submittal Procedures | Format, transmittal form, review timeline, resubmittal procedure | Architect review time (typical 14 days); coordination drawings; sample required quantities (often 3 — one for record, one for architect, one for owner) |
| **01 40 00** | Quality Requirements | Referenced standards (ASTM, ACI, ANSI, NFPA, ICC, etc.), testing agencies, special inspections, mock-ups, manufacturer's field services | Which tests are paid by whom (testing of failed work is **always** GC cost); special inspector hire (often by Owner, but coordinated by GC); mock-up retention or demolition |
| **01 42 00** | References | Cited standards — list of every standard referenced anywhere in the spec | Cross-check against your subs' capability |
| **01 45 00** | Quality Control | Manufacturer's instructions, field samples, mock-ups, in-place sampling | When you can demolish a mock-up; whether mock-ups stay as benchmark |
| **01 50 00** | Temporary Facilities and Controls | Temporary utilities (power, water, sanitary, internet), barriers, fencing, signage, dust control, fire protection, security | Who pays utilities during construction; fence height and material; required project sign; whether owner provides connection points |
| **01 56 00** | Temporary Barriers and Enclosures | Construction fencing, dust partitions during occupied renovations, weather closures | Especially critical on occupied renovations |
| **01 60 00** | Product Requirements | Delivery, storage, handling, project conditions, substitutions (cross-references 01 25 00), warranties | Storage temp/humidity for materials (drywall, wood flooring); manufacturer warranty pass-through to owner |
| **01 70 00** | Execution Requirements | Examination of substrates, preparation, installation, cutting and patching, cleaning, demonstration and training, closeout | Acceptance of prior work before starting; cutting/patching responsibility (you cut, original installer patches? or you cut and patch?); broom-clean vs. final cleaning standard |
| **01 73 29** | Cutting and Patching | Detailed cutting and patching rules | Often forbids cutting structural members without engineer approval |
| **01 74 00** | Cleaning and Waste Management | Daily cleanup, final cleaning, waste sorting/recycling | LEED projects: recycling % required; haul tickets retained |
| **01 77 00** | Closeout Procedures | Substantial completion, final completion, punch list process | Required documents at SC; sequence (request walk → punch issued → corrections → final walk → SC certificate) |
| **01 78 00** | Closeout Submittals | O&M manuals, warranties, record documents (as-builts), spare parts, attic stock, training | Volume of closeout — start collecting **during** construction, not at the end |
| **01 79 00** | Demonstration and Training | Owner training on systems | Hours required per system; video recording requirements |

### 3.3 What "Or Equal" Actually Means

A common Part 2 phrase: "Acceptable products: ABC Brand Model 123, or equal."

In practice, "or equal" is governed by Section 01 25 00 Substitution Procedures, and it is almost never as easy as it sounds:

- **You must submit a formal substitution request,** usually on the architect's form, before a deadline (often 30 days after NTP).
- You must show **the proposed product equals or exceeds every specified attribute** — not just price.
- You bear the burden of proof, and **the architect has sole discretion** to accept or reject. Their decision is generally not arbitrable.
- If the substitution requires redesign or coordination changes, **you pay for them.**
- "Or equal" is **not** an open invitation. Two trusted brands listed by name + "or equal" usually means "we are willing to consider one more brand if you can prove it."

When a sub tells you "I always use Brand X, it's equal," your answer is: "Submit the substitution request with full data, before the deadline. Until approved, you're installing the specified product."

---

## 4. Three-Part Section Format — Understanding Any Spec Section

Every CSI-formatted section follows the same structure. Once you can read one section, you can read them all.

### 4.1 The Structure

| Part | Title | Contents |
|---|---|---|
| Part 1 | General | Scope, related sections, references, definitions, submittals, quality assurance, delivery/storage, project conditions, warranty, maintenance materials |
| Part 2 | Products | Manufacturers, materials, equipment, components, accessories, mixes, fabrication, finishes, source quality control |
| Part 3 | Execution | Examination, preparation, installation, field quality control, cleaning, protection, schedules |

### 4.2 Part 1 — General

**What to look for:**

- **1.01 Section Includes** — what work is described in this section. Critical for scoping: a section titled "Gypsum Board Assemblies" might include cold-formed framing studs, not just board.
- **1.02 Related Sections** — adjacent sections. If 09 21 16 says "see 06 10 00 for wood blocking in walls," the blocking is **not in your drywall sub's scope** — it's in your framing sub's scope. Many missed-scope disputes turn on this clause.
- **1.03 References** — list of cited standards (e.g., ASTM C1396 for gypsum board, GA-216 for installation). These are **incorporated by reference** — they are part of the contract even though they are not bound in the spec book. You can read them at the standards organization's website, sometimes for a fee.
- **1.04 Submittals** — what you must submit before installation: product data, shop drawings, samples, mock-ups, certifications, test reports. Each line costs money and time; ignore at your peril.
- **1.05 Quality Assurance** — installer qualifications (e.g., "minimum 5 years experience installing this product"), manufacturer qualifications, mock-up requirements, pre-installation conference requirements.
- **1.06 Delivery, Storage, Handling** — site storage conditions; many products void warranty if stored improperly (drywall must be stacked flat off the floor; wood flooring must acclimate at design humidity).
- **1.07 Project / Site Conditions** — environmental conditions required before installation (e.g., interior at 65°F before painting).
- **1.08 Warranty** — product warranty pass-through and special extended warranties (e.g., 20-year manufacturer roofing warranty).

### 4.3 Part 2 — Products — The Four Specification Methods

Spec writers can specify a product in four ways, each with different flexibility:

| Method | What it looks like | Your flexibility | Risk |
|---|---|---|---|
| **Proprietary (closed)** | "Provide Marvin Ultimate Casement, Model CWN..." | None. You install exactly this product. | Single-source pricing exposure. |
| **Semi-proprietary (or equal)** | "Marvin Ultimate, Andersen 400 Series, or approved equal" | Limited. Listed products are pre-approved; alternatives require substitution request. | Architect can reject alternatives. |
| **Performance** | "Casement window with U-factor ≤ 0.28, SHGC ≤ 0.30, AAMA AW-PG40, air infiltration ≤ 0.10 cfm/sf at 1.57 psf..." | Wide. Any product meeting all performance criteria is acceptable. | You must prove performance with data sheets / test reports. |
| **Prescriptive / Descriptive** | "Casement window, aluminum-clad wood, 1-3/4 inch sash, dual-pane low-E argon-filled glass, ..." | Moderate. Any product meeting all descriptive criteria works, but interpretation is contested. | Subjective compliance — architect can argue you missed a sub-criterion. |

**Practical implication for bidding:**
- Proprietary = bid the named product, no exceptions. Get a quote, lock the price.
- Semi-proprietary = bid the cheapest listed product unless the architect has indicated a preference.
- Performance = bid the cheapest product that documentably meets performance. Get the cut sheet ready for submittal.
- Descriptive = bid carefully. Read every word — every adjective is a requirement.

### 4.4 Part 3 — Execution

**What to look for:**

- **3.01 Examination** — required inspection of conditions before installation. "Installer's acceptance of substrate constitutes acceptance of conditions." Translation: if your tile sub starts setting tile over a substrate, they implicitly accepted that substrate. If it cracks later, that's their problem. **Train subs to document substrate problems in writing before starting.**
- **3.02 Preparation** — required prep work (priming, moisture barrier, leveling, etc.).
- **3.03 Installation** — the actual method. References to manufacturer instructions ("install per manufacturer's printed instructions") incorporate those instructions as contract requirements. Print the instructions and keep them onsite.
- **3.04 Field Quality Control** — testing during installation (e.g., infiltration testing on air barriers; thermography on insulation).
- **3.05 Adjusting** — final tuning (e.g., door hardware adjustment after settling).
- **3.06 Cleaning** — installer's cleanup obligation.
- **3.07 Protection** — protection of installed work until substantial completion.
- **3.08 Schedules** — applicable schedules (e.g., paint schedule, door schedule), sometimes referenced from drawings.

---

## 5. Reading Specifications for Bidding

### 5.1 Bid Checklist — Spec Sections to Read Carefully Before Pricing

| Read carefully | Why |
|---|---|
| Division 00 in full | Bond, insurance, liquidated damages, payment retainage — direct cost and risk |
| Division 01 in full | GC-borne items (testing, temp facilities, cleaning, closeout) that drawings never show |
| Part 1 of every section in your scope | Submittals, references, QA — sets the burden of proof |
| Part 2 of products with proprietary or single-source items | Lock pricing early; long lead times |
| Part 3 of high-risk execution sections (concrete, waterproofing, roofing, air barrier) | Where field testing, mock-ups, and inspections create real cost |
| Allowances and alternates schedule | These directly affect your bid number |
| Unit price schedule | Pricing if quantities change |

### 5.2 Spec-Driven Cost Items That Aren't on Drawings

Things the spec demands that you must price even though they appear nowhere on the drawings:

| Hidden cost item | Where it hides |
|---|---|
| Concrete cylinder testing (1 set / 50 CY or each pour < 50 CY) | 03 30 00 Part 1.04 + Division 01 testing |
| Soils compaction testing | 31 23 00 + Division 01 |
| Special inspections (structural, anchorage, welding) | IBC Chapter 17 referenced in 01 40 00 — usually owner pays the inspector, but **GC pays for any re-inspection of failed work** |
| Mock-ups (brick panel, full bathroom, exterior wall section) | Individual sections + Division 01 |
| Shop drawings for engineered components (truss, stairs, railings, cabinets) | Sub's cost, usually, but expedite fees are GC's |
| Product samples (typically 3 per material) | Section Part 1 |
| Pre-installation conferences (often 6–12 of them) | 01 31 19 + individual sections |
| Substantial completion punch list management | 01 77 00 |
| Closeout submittal preparation (O&M manuals, warranties, record drawings) | 01 78 00 — often 40–80 hours of PM time |
| Owner training sessions | 01 79 00 |
| Final cleaning (often by professional cleaning subcontractor) | 01 74 00 |
| Construction waste recycling and reporting | 01 74 19 |
| Project sign | 01 58 13 |
| Temporary utilities (power consumption, water, dumpster, port-a-johns) | 01 50 00 |
| Commissioning of HVAC / building systems | Division 01 + 23 08 00 |
| Extended warranties (roofing 20-yr NDL, window 10-yr, etc.) | Section Part 1.08 |
| Attic stock (spare tile, paint, flooring — typically 2–5%) | Section Part 1.09 |

**Rule of thumb:** Add 2–4% of contract value as "Division 01 contingency" if you have not read Division 01 carefully and priced it line by line.

### 5.3 "By Owner" and "By Others" — Scope Exclusions

Section 01 10 00 Summary typically lists:

- **Owner-Furnished, Owner-Installed (OFOI)** — owner buys and installs. Not your problem, but coordinate access.
- **Owner-Furnished, Contractor-Installed (OFCI)** — owner buys, you install. **Confirm**: receiving and inspection responsibility, warranty pass-through, what you do if delivery is late.
- **Not in Contract (NIC)** — outside your scope entirely.
- **By Others** — vague; clarify by RFI.

Common residential OFOI / NIC items: appliances, audio-visual equipment, window treatments, furniture, smart-home programming, low-voltage racks, art lighting.

### 5.4 Addenda — Pre-Bid Modifications

Before bid submission, the architect may issue **addenda** modifying the spec or drawings. Each addendum is numbered (Addendum 1, 2, 3...). You must:

1. Acknowledge each addendum on the bid form.
2. Incorporate each addendum's changes into your bid.
3. After contract execution, addenda become part of the contract documents.

**Failure to acknowledge an addendum may invalidate your bid or, worse, bind you to the changes without having priced them.**

---

## 6. Common Residential Spec Sections — What to Look For

Below: scope items most likely to bite the residential GC. For each, the key things to extract during your spec read.

### 6.1 03 30 00 Cast-in-Place Concrete

| Look for | Why it matters |
|---|---|
| Compressive strength (f'c): 2500 / 3000 / 4000 / 5000 PSI | Drives mix cost; 4000+ PSI requires more cement |
| Maximum water/cement ratio | Affects strength and durability; lower w/c = more expensive |
| Air content (5–7% typical for exterior) | Air-entrained mix is for freeze-thaw — interior slabs typically not entrained because air weakens slab |
| Slump limits | High-slump for pumping/finishing; low-slump for structural |
| Aggregate size | 3/8" pump mix vs. 3/4" structural |
| Admixtures (fly ash, plasticizers, accelerators) | Mix cost and schedule |
| Curing method (7-day wet cure, curing compound, curing blanket) | Curing compound on slabs you want polished or epoxied can prevent adhesion — match curing to finish |
| Cylinder testing frequency (typically 1 set of 4 per 50 CY or per day's pour, whichever more frequent) | Testing cost; GC schedules testing agency |
| Cold weather provisions (50°F minimum, heated enclosures, accelerators) | Winter pours: significant cost |
| Hot weather provisions (retarders, sub-grade cooling, fog spraying) | Summer pours in hot climates |
| Reinforcement: grade (60 ksi typical), epoxy-coated vs. black, lap length, cover | Wrong cover = inspector rejection |
| Tolerances (F-numbers for floors — Ff/Fl, FF50/FL30 typical residential) | Polished concrete or large-format tile demands high flatness |

### 6.2 06 10 00 Rough Carpentry

| Look for | Why it matters |
|---|---|
| Species and grade (e.g., Doug Fir #2 or better, SPF #2, SYP #2) | Cost and span tables differ |
| Moisture content at installation (typically 19% max for framing) | Wet lumber shrinks → drywall cracks → callback |
| Treatment for ground contact / weather (CCA, ACQ, MCA — and required fasteners for treated lumber: HDG or stainless) | Untreated below-grade fails; standard fasteners corrode in modern ACQ |
| Engineered lumber: brand and grade (LVL, PSL, LSL, glulam) | Substitution requires structural engineer approval |
| Sheathing: type, thickness, exposure rating (CDX, OSB, exterior glue), span rating | Wrong sheathing = re-do |
| Fastener type, size, spacing (nails for shear walls — 8d common at 4" o.c. edge, 12" field, typical) | Shear wall fastening is non-negotiable — re-inspection |
| Hangers and connectors (Simpson catalog numbers, equivalent only with engineer's stamp) | "Equivalent" must be ICC-ES approved — not all are |
| Blocking and bracing (fire blocking per code, shear blocking per drawings) | Inspector kicks per IRC R602.8 |
| Wood I-joist and truss layout: who provides shop drawings | Truss design submittal needs engineer-signed; layout sheet is fabricator's |

### 6.3 07 21 00 Insulation

| Look for | Why it matters |
|---|---|
| R-value AND product type | R-21 batt and R-21 dense-pack cellulose perform differently in cold |
| Product subtype: unfaced/faced batt, mineral wool, blown cellulose, blown fiberglass, closed-cell SPF, open-cell SPF, rigid (XPS, EPS, polyiso) | Each has different vapor permeance, fire rating, fastening |
| ASTM compliance (C665 for blanket; C1015 for blown; C578 for XPS/EPS; C1289 for polyiso) | Required for code compliance |
| Vapor retarder class (Class I: poly; Class II: kraft, vapor-retarder paint; Class III: latex paint on drywall) | Climate zone determines required class; wrong VR = condensation |
| Continuous exterior insulation (R-5 or R-10 typical) | Special detailing at fasteners, windows, roof edge |
| Air barrier compatibility | Some insulation is also an air barrier (closed-cell SPF); some is not (batt) |
| Fire and smoke ratings (Class A flame spread / smoke developed ≤ 25/50 for exposed in attics) | Inspector requirement |
| Installer certifications (e.g., spray foam installer cards; some manufacturers require certified installers for warranty) | If sub isn't certified, warranty void |

### 6.4 07 27 00 Air Barriers

| Look for | Why it matters |
|---|---|
| Continuous air barrier requirement: walls only, or walls + roof + floor (the "6-sided box") | Affects detailing at every transition |
| Material type: fluid-applied (Prosoco R-Guard, Henry Air-Bloc), self-adhered membrane (Henry Blueskin, Grace Vycor), mechanically attached sheet (Tyvek CommercialWrap), or proprietary integrated sheathing (ZIP System with tape) | Each requires different prep, application, and warranty paperwork |
| Performance requirement: ASTM E2178 (material air permeance < 0.004 cfm/sf) and ASTM E2357 (assembly air leakage < 0.04 cfm/sf at 1.57 psf) | If testing fails, you re-do |
| Whole-building blower-door test: required ACH50 target (IRC requires ≤ 5 ACH50 for new construction in many climate zones; performance specs may require ≤ 3 ACH50) | Failing blower door pre-drywall is fixable; failing at substantial completion is not |
| Transitions: WRB-to-window flashing tape, WRB-to-roof underlayment, WRB-to-foundation | Most air leakage is at transitions, not field |
| Manufacturer compatibility list | Mixing brands (Henry sheet over Prosoco fluid) can void both warranties |

### 6.5 07 31 13 Asphalt Shingle Roofing

| Look for | Why it matters |
|---|---|
| Shingle class / weight (architectural vs. 3-tab vs. premium designer) | Cost and warranty period |
| Wind rating (ASTM D3161 Class F = 110 mph; ASTM D7158 Class H = 150 mph) | Coastal projects often spec Class H |
| UL 2390 / ASTM D3161 / ASTM D7158 compliance | Code-mandated in high-wind areas |
| Algae resistance (ASTM D3462) | Owner-driven aesthetic spec, especially in humid climates |
| Underlayment: synthetic vs. #30 felt vs. self-adhered (full coverage in high-wind) | Synthetic now standard; full ice-and-water in some zones |
| Ice and water shield extent: minimum 24" inside warm wall, valleys, around penetrations, sometimes whole low-slope sections | Code-driven (IRC R905.1.2) |
| Drip edge: required at eaves and rakes per IRC; gauge and material specified | Easy to miss on small jobs |
| Valley type: open (metal-lined), closed-cut, woven | Different labor and material |
| Fastener type and pattern (galvanized 1-1/4" min, 4–6 nails per shingle depending on wind zone) | High-wind areas require 6-nail; warranty void with fewer |
| Starter strip and ridge cap product (specified vs. cut-shingle improvised) | Manufacturer warranty often requires matching products |
| Manufacturer's enhanced warranty (e.g., GAF Golden Pledge — requires certified installer + complete system) | Big selling point; requires certified roofer |

### 6.6 07 62 00 Sheet Metal Flashing and Trim

| Look for | Why it matters |
|---|---|
| Material: galvanized steel (G90 min), aluminum (.024–.040 typical), copper (16 oz / 20 oz), stainless | Galvanic incompatibility (copper near aluminum/galv) causes corrosion |
| Minimum gauge or thickness | Below-spec gauge dents, fails wind |
| Lap requirements (typically 4" minimum, sealed) | Leaks at laps if undersized |
| Sealant type (typically ASTM C920 Class 25 or 50, urethane or silicone) | Wrong sealant fails in UV or movement |
| Integration with WRB (lapped over, not under, in shingle fashion) | Backwards lapping = leak |
| Drip edge profile, kick-out flashings at roof-wall intersections, head flashings at windows/doors | Missing kick-out flashings cause sidewall rot — #1 residential failure |
| Cleat spacing and fastener type | Wind-uplift performance |

### 6.7 08 14 00 Interior Wood Doors

| Look for | Why it matters |
|---|---|
| Species and cut (paint-grade vs. stain-grade; rotary, plain-sliced, quarter-sawn, rift) | Stain-grade much pricier |
| Grade (per WDMA I.S.1A: Premium / Custom / Economy) | Premium is for high-end |
| Core type: hollow (HC), solid particleboard (SCB / PB), staved lumber (SLC), mineral (for fire-rated) | Solid core resists sound; required where STC-rated |
| Fire rating (20/45/60/90 min) — required by drawings or code at attached garage, between dwelling units | Wrong core = code fail |
| Construction: flush vs. stile-and-rail (5-panel, Shaker, etc.) | Different fabricators, different cost |
| Prefit / premachined / prefinished | Pre-machined is faster install; prefinished avoids site-finish |
| Warranty (typical 1-year, lifetime against delamination for premium) | Replace early failures |

### 6.8 08 51 13 Aluminum Windows (and 08 52 13 Wood, 08 53 13 Vinyl)

| Look for | Why it matters |
|---|---|
| AAMA / WDMA performance class (R, LC, CW, AW) and performance grade (PG — e.g., AW-PG50 means architectural window, 50 psf design pressure) | Coastal / high-wind projects require higher PG |
| U-factor (whole-window NFRC) | Energy code compliance |
| SHGC (Solar Heat Gain Coefficient) | Climate-driven; varies wall-to-wall in some climate zones |
| VT (Visible Transmittance) | Daylighting |
| Air infiltration (cfm/sf at 1.57 psf — typically ≤ 0.30) | Cold drafts in winter if poor |
| Water penetration test pressure (typically 15% of design pressure, min 2.86 psf) | Driving rain resistance |
| Operating type (casement, awning, double-hung, sliding, fixed) | Drawings tell you this; spec confirms hardware |
| Glazing: dual-pane vs. triple-pane, low-E coating (which surface — #2 vs. #3), argon vs. krypton, warm-edge spacer | Each affects U-factor and cost |
| Frame: aluminum thermally broken vs. aluminum-clad wood vs. fiberglass vs. vinyl | Cost, aesthetics, durability |
| Screen type (full, half, retractable) and color | Owner detail |
| Hardware finish | Owner detail |
| Manufacturer warranty (often 10-yr glass, 20-yr frame) | Pass through to owner |

### 6.9 09 21 16 Gypsum Board Assemblies

| Look for | Why it matters |
|---|---|
| Board type and thickness: 1/2" standard, 5/8" Type X (fire-rated), 1/2" mold-resistant, cement board, glass-mat exterior sheathing | Type X required at garages (residential per IRC R302.6), between units, at certain ceiling assemblies |
| Fastener type and pattern (screws, typically Type W for wood / Type S for steel; spacing 12" o.c. on ceilings, 16" on walls per GA-216) | Tight pattern reduces nail pops; wrong screw strips |
| Resilient channel / sound channels where STC-rated | Easy to omit during framing — coordinate early |
| Corner bead type (metal, paper-faced metal, vinyl, no-coat) | Quality and durability differ |
| **Joint treatment finish level (GA-214):** | Critical — drives labor cost dramatically |
| → Level 0: no taping (temporary) | |
| → Level 1: tape embedded in joints (above ceilings, plenum) | |
| → Level 2: tape + skim on joints and fasteners (garages, storage) | |
| → Level 3: two coats over Level 2 (heavy texture finish) | |
| → Level 4: three coats over Level 2 (flat paint, light texture — **residential standard**) | |
| → Level 5: skim coat over entire surface (gloss/semi-gloss paint, raking light, high-end residential) | |
| Control joints (every 30 ft typical, at room-to-corridor transitions, ceiling-to-wall) | Cracks without them |
| Sound-attenuation blanket in cavity (often called out here even though it's insulation) | Required for STC-rated walls |

### 6.10 09 30 00 Tiling

| Look for | Why it matters |
|---|---|
| Tile type (ceramic, porcelain, natural stone) and grade (Standard / Second / Decorative) per ANSI A137.1 | Porcelain ≠ ceramic; different cutting and setting |
| Setting material per ANSI A118: A118.1 dryset, A118.4 latex-modified, A118.11 polymer-modified, A118.15 improved modified for porcelain/large-format | Wrong thinset on porcelain = delamination |
| Grout type per ANSI A118: cement (A118.6 / A118.7) vs. epoxy (A118.3) | Epoxy is stain-proof but harder to install |
| Grout width and color | Detail |
| Backer board: cement board (ANSI A118.9), foam (Wedi, Schluter Kerdi-Board), glass-mat | Backer for wet vs. dry differs |
| Waterproofing: ANSI A118.10 surface-applied (Schluter Kerdi, RedGard, Hydro Ban) — at showers, tub surrounds, floors | Code requires waterproofing at showers; failure = leak |
| Crack isolation membrane (ANSI A118.12) at concrete floors with shrinkage cracks | Prevents telegraphing |
| Movement joints (TCNA EJ171) at floor-to-wall, every 20–25 ft of field, around penetrations | Missing movement joints = popped tile |
| TCNA Handbook detail reference (e.g., TCNA F125 for interior floor over concrete) | Architect cites the detail; you build to it |
| Installer qualifications (often Certified Tile Installer or NTCA member required for high-end) | Subbed appropriately |

### 6.11 09 90 00 Paints and Coatings

| Look for | Why it matters |
|---|---|
| Surface preparation requirements (SSPC standards for metal; sanding/cleaning for wood; primer-sealer for new drywall) | Skipped prep = adhesion failure |
| Primer requirements (latex vs. oil; stain-blocking; bonding) | Type-Y substrate needs Type-Y primer |
| Number of coats (typically primer + 2 finish; sometimes primer + 3 on dark / saturated colors) | Two coats minimum on most surfaces |
| Sheen level (flat, matte, eggshell, satin, semi-gloss, gloss) per room | Walls vs. trim |
| Acceptable products (often listed by manufacturer: Sherwin-Williams, Benjamin Moore, PPG) and specific product line (premium vs. contractor-grade) | Premium lines cost ~30% more |
| Dry film thickness (DFT) and wet film thickness (WFT) — more common in commercial but appears on coatings over metal / exterior | Field-measured with mil gauge |
| VOC limits (some jurisdictions require ≤ 50 g/L) | Compliance and indoor air quality |
| Color schedule (referenced from drawings or spec) | Confirm before ordering |
| Touch-up paint provided to owner (typically 1 quart per color) | Closeout submittal |

### 6.12 22 10 00 Plumbing Piping

| Look for | Why it matters |
|---|---|
| Pipe material by system: cold/hot supply (Type L copper, PEX-A, PEX-B, CPVC), DWV (PVC, ABS, cast iron), gas (black steel, CSST, copper) | Different code allowances by jurisdiction |
| Joining method: solder vs. ProPress vs. SharkBite (often disallowed in spec), PEX crimp vs. expansion | Spec often forbids push-fit |
| Pressure test requirement (typically 100 psi hold for 15 min on supply; 5 psi air test on DWV) | Required before cover |
| Slope requirements (1/4" per foot for 3" and smaller DWV; 1/8" per foot for 4" and larger per UPC/IPC) | Inspector check |
| Insulation (1/2" on cold lines in unconditioned space; 1" on hot supply for energy code; full insulation on exposed pipes) | Energy code |
| Hangers and supports: spacing and material (no plastic hangers on metal pipe) | Sag and noise |
| Backflow prevention, water hammer arrestors at quick-close valves (washing machine, dishwasher, ice maker) | Code + comfort |
| Fixture rough-in dimensions and connection types | Coordinate with fixture spec section |

### 6.13 23 00 00 HVAC

(Often split across 23 05 00 Common Work, 23 31 00 Ductwork, 23 81 00 Decentralized HVAC, etc.)

| Look for | Why it matters |
|---|---|
| Equipment model numbers, capacity (BTU/h, tons, SEER, AFUE, HSPF) | Energy code minimums; sizing per Manual J |
| Ductwork material (galvanized steel, flex duct limits, fiberboard) | Some specs ban flex; others limit length |
| Sealing standard (Mastic, UL 181 tape — duct tape banned) | Energy code |
| Insulation R-value on ductwork in unconditioned space (R-8 typical) | Energy code |
| Manual J load calc, Manual D duct design, Manual S equipment selection — required submittals | Often spec-required |
| Refrigerant piping (copper ACR; line set sizing; brazing with nitrogen purge) | Quality install for warranty |
| Commissioning / start-up (manufacturer's authorized startup for warranty) | Many manufacturers void warranty without factory startup |
| Ventilation: ERV/HRV requirement, CFM, balanced air | Code (ASHRAE 62.2) |

### 6.14 26 05 00 Common Work Results for Electrical

| Look for | Why it matters |
|---|---|
| Wire type and insulation (THHN, THWN-2 for wet locations, NM-B for residential, MC for some applications) | Code-specified by use |
| Conduit type (EMT, IMC, RMC, PVC) and where required vs. NM-B in residential | Some specs require conduit in unfinished basements / garages |
| Device ratings (15A vs. 20A receptacles; tamper-resistant TR; weather-resistant WR for exterior; GFCI / AFCI per code) | NEC 406.12 (TR), 210.8 (GFCI), 210.12 (AFCI) |
| Panel manufacturer (often spec'd by name — Square D QO, Eaton CH, Siemens) | Owner preference; matches breakers |
| Service size and feeder size | Often per drawings; spec confirms |
| Grounding and bonding (NEC 250) | Critical safety; inspector check |
| Testing: continuity, megger, GFCI/AFCI function test | Submittal required on some projects |
| Labeling (panel directory, circuit identification, disconnects per NEC 110.22) | Closeout requirement |
| Low-voltage scope: separate spec section (Division 27) | Don't assume electrical sub handles structured cabling |

---

## 7. Submittals — What the Spec Requires

### 7.1 Types of Submittals

| Type | What it is | Typical timing |
|---|---|---|
| **Product Data** | Manufacturer cut sheets, technical specifications, installation instructions. Used to verify the proposed product matches the spec. | Submit early; before ordering. |
| **Shop Drawings** | Contractor-prepared drawings showing how the work will be fabricated and installed (cabinets, stairs, trusses, railings, structural steel). | Submit after design but before fabrication. Long lead. |
| **Samples** | Physical pieces of the actual product (tile, stone, brick, paint chips, finish samples). | Submit before bulk order. Architect picks from samples. |
| **Mock-ups** | Full-size assemblies built onsite or at fabricator (brick panel, exterior wall, full bathroom). | Submit early; once approved becomes the benchmark for the rest. |
| **Test Reports** | Lab reports proving product meets performance specs (concrete cylinder breaks, air-barrier ASTM E2357 tests). | During / after installation. |
| **Certificates** | Manufacturer letters certifying compliance, installer certifications, third-party listings (UL, FM, ICC-ES). | Before installation. |
| **Closeout Submittals** | O&M manuals, warranties, record drawings (as-builts), spare parts, attic stock, training records. | At substantial completion. |

### 7.2 Submittal Process — Step by Step

```
Sub prepares submittal
        ↓
Sub submits to GC
        ↓
GC reviews — verifies completeness, matches spec, coordinates with adjacent work
        ↓
GC stamps and signs (this is meaningful — see 7.3)
        ↓
GC transmits to Architect
        ↓
Architect reviews (typical 14 calendar days)
        ↓
Architect returns with action stamp:
  • Approved / No Exceptions Taken
  • Approved as Noted / Make Corrections Noted
  • Revise and Resubmit
  • Rejected / Not Approved
  • For Information Only
        ↓
GC distributes back to sub
        ↓
If Approved or Approved as Noted: proceed with fabrication/installation
If Revise and Resubmit: sub corrects, cycle repeats
```

### 7.3 The GC's Stamp — What It Means

When you stamp a submittal before forwarding to the architect, you are certifying:

1. You have **reviewed** the submittal.
2. The submittal **complies with the contract documents.**
3. You have **coordinated** the submittal with adjacent work and other submittals.
4. You have **verified field dimensions** (where applicable).

This is not a formality. If you forward an unstamped submittal, the architect will reject it. If you stamp a non-compliant submittal and the architect approves it on the basis of your representation, **you are still responsible for the non-compliance.** Architect approval of submittals does not relieve the contractor from compliance with the contract documents (per AIA A201 §3.12.8).

### 7.4 What "Approved as Noted" Means

The most common return stamp. It means:

- The submittal is approved **subject to the architect's corrections marked on the submittal.**
- You must **incorporate every noted correction.**
- You do **not** need to resubmit; you may proceed with the corrections.
- It is **not** unconditional approval. If you ignore the notes, you breached.

Common error: sub receives "Approved as Noted," sees the word "Approved," and orders the product without correcting. The product arrives wrong. Sub claims architect approved. Architect points to the notes. **You eat the rework.**

**Best practice:** When you receive "Approved as Noted," transmit the marked-up submittal to the sub with a written instruction: "Note architect's corrections on attached submittal. Incorporate before fabrication and confirm in writing within 5 days."

### 7.5 The Submittal Schedule

Division 01 33 00 typically requires the GC to prepare a **submittal schedule** within 30 days of NTP, listing:

- Every submittal required by the spec
- Spec section / submittal title
- Date submittal will be sent to architect
- Date architect's return is needed to maintain schedule
- Lead time after approval to delivery onsite

**Why this matters:** Long-lead items (windows, custom millwork, structural steel, specialty roofing) can be 12–26 weeks from approval to delivery. If you submit at week 12 of a 20-week project, you cannot recover. Your submittal schedule should drive your purchasing schedule, which should drive your overall construction schedule.

**Practical tip:** Build the submittal schedule from a checklist of every Part 1.04 (Submittals) clause in every spec section in your scope. Miss one, and you have a hole in the project.

### 7.6 Substitution Requests as Submittals

Substitution requests are a specialized submittal:

- Use the **architect's specified form** (often in 01 25 00).
- Submit **before the substitution deadline.**
- Include side-by-side comparison: spec'd product vs. proposed product, attribute by attribute.
- Include cut sheets, test reports, and warranty documents.
- Include cost impact (usually a deduct credit if approved).
- Include schedule impact.
- Include contractor's certification that the substitute is equal or better.

The architect can:

- Approve (proceed with proposed product)
- Reject (install specified product)
- Conditionally approve (proceed if conditions met)

The architect's decision is generally final and not arbitrable. Plan accordingly.

---

## 8. Using the Spec to Manage Subs

### 8.1 Flowing Down Spec Requirements to Sub Contracts

**"Sub shall comply with all applicable specification sections" is legally weak.** It is enforceable on paper, but in practice subs will deny having read or understood the spec, and you will be in a "he said, she said" with no way to back-charge.

**Better approach: extract specific requirements.** In every sub contract:

1. **Attach the relevant spec sections as exhibits** (not just reference them).
2. **List specific submittals required by the spec** that the sub must produce, with deadlines.
3. **List specific testing and inspection requirements** and who pays.
4. **List specific warranty and closeout deliverables.**
5. **State that the sub has read and agrees to the attached spec sections.**

Example clause:
> "Subcontractor acknowledges receipt and review of Specification Sections 09 21 16, 09 22 16, and 09 29 00 (Drywall Assemblies), attached as Exhibit B. Subcontractor shall furnish all submittals listed in Section 09 21 16 Part 1.04, including product data for gypsum board, joint compound, fasteners, and corner bead, within 14 days of NTP. All assemblies shall achieve Level 4 finish per GA-214 except as noted on drawings."

When a sub misses Level 4 finish and produces Level 3, the contract clause is your enforcement document.

### 8.2 Pre-Installation Conferences

Division 01 31 19 typically lists required pre-installation conferences. Common examples:

- Concrete (before first pour)
- Roofing (before installation)
- Waterproofing / air barrier (before installation)
- Stucco / EIFS (before lath)
- Tile (before setting)
- Painting (before priming)
- Hardwood flooring (before installation)
- Cabinets (before installation)

**Who attends:**
- GC superintendent and project manager
- Sub foreman and project manager
- Architect
- Owner's representative (sometimes)
- Manufacturer's technical representative (sometimes — often required for warranty)
- Special inspector or testing agency (if applicable)

**What is covered:**
- Review of spec requirements for the work
- Substrate conditions and acceptance
- Coordination with adjacent trades
- Sequencing
- Submittal status
- Mock-up requirements
- Field testing requirements
- Cleanup and protection

**Document the meeting:** Issue meeting minutes within 48 hours. Include decisions made, action items, and attendance. If a sub claims later they "didn't know" about a requirement, the minutes are your proof.

### 8.3 Holding Subs to Spec — When Things Go Wrong

The spec is your enforcement document. The cycle:

1. **Identify the deviation.** "The drywall is Level 3, not Level 4 per 09 21 16."
2. **Notify in writing.** Email or formal NCR (non-conformance report) citing the spec section.
3. **Demand correction.** Set a deadline. Cite the sub contract.
4. **If sub refuses:**
   - Document with photos.
   - Issue 48-hour cure notice per sub contract.
   - If still uncured, hire another sub to correct and back-charge per contract.
5. **Track all costs.** Architect/owner will want to see your enforcement when they ask "why is this Level 3?"

**Avoid:** Verbal back-and-forth, vague emails, accepting "we'll fix it on the next one." Get specifics, in writing, with a deadline.

### 8.4 Quality Control Checklists from Part 3

Convert every Part 3 Execution section into a field checklist for your superintendent. Example, for 09 21 16 drywall:

| Check | Spec ref | Pass / Fail | Notes |
|---|---|---|---|
| Substrate acceptance documented before start | 09 21 16 Part 3.01 | | |
| Board orientation: ceilings perpendicular to framing | 09 21 16 Part 3.03 | | |
| Screw spacing: 12" o.c. ceilings, 16" o.c. walls | 09 21 16 Part 3.03 / GA-216 | | |
| Type X at garage ceiling, garage-house wall | 09 21 16 Part 2.01 | | |
| Fastener heads dimpled, not over-driven | GA-216 | | |
| Mold-resistant board in baths and laundry | 09 21 16 Part 2.01 | | |
| Joint treatment Level 4 throughout (Level 5 at flat ceilings in great room per finish schedule) | 09 21 16 Part 3.04 / 09 91 23 | | |
| Control joints at locations shown on drawings | 09 21 16 Part 3.03 | | |
| Sound attenuation blanket in master bedroom walls (STC-rated) | 09 21 16 / 09 81 00 | | |

The checklist is built once per project, used by the superintendent during installation, signed off at completion, and filed for the closeout package. It is also your defense if the architect challenges the work months later.

---

## 9. Appendix — Quick Reference Cards

### 9.1 Standards Bodies You'll See Cited

| Acronym | Body | What they govern |
|---|---|---|
| ASTM | ASTM International (formerly American Society for Testing and Materials) | Materials testing — concrete, steel, wood, sealants, virtually everything |
| ACI | American Concrete Institute | Concrete mix, placement, reinforcement, curing |
| ANSI | American National Standards Institute | Cross-cutting standards including tile (A108, A118, A137), plumbing fixtures |
| NFPA | National Fire Protection Association | Fire codes (NFPA 13 sprinklers, 70 NEC, 72 fire alarm) |
| ICC | International Code Council | IRC, IBC, IECC, IPC, IMC, IFC |
| AISC | American Institute of Steel Construction | Structural steel |
| AWS | American Welding Society | Welding standards (D1.1 structural steel, D1.2 aluminum) |
| AWI | Architectural Woodwork Institute | Millwork (AWS standards: Custom / Premium / Economy grades) |
| GA | Gypsum Association | Drywall (GA-216 installation, GA-214 finish levels) |
| TCNA | Tile Council of North America | Tile installation handbook |
| NWFA | National Wood Flooring Association | Wood floor installation |
| NFRC | National Fenestration Rating Council | Window/door energy ratings |
| AAMA | American Architectural Manufacturers Association | Windows, doors, curtain wall performance |
| SMACNA | Sheet Metal and Air Conditioning Contractors National Association | HVAC ductwork |
| SSPC | Society for Protective Coatings | Surface prep for coatings |
| UL | Underwriters Laboratories | Fire and safety listings |

### 9.2 Action Stamps — What Each Means

| Stamp | Meaning | What to do |
|---|---|---|
| Approved / No Exceptions Taken / Reviewed | Submittal is acceptable as submitted | Proceed with fabrication/install |
| Approved as Noted / Make Corrections Noted | Acceptable subject to architect's notes | Incorporate notes; proceed |
| Revise and Resubmit | Significant changes required | Revise; resubmit; do not proceed |
| Rejected / Not Approved | Submittal does not meet spec | Start over with a new approach |
| For Information Only / Not Reviewed | No formal review (informational submittals) | Verify whether action is required |

### 9.3 Spec Reading Routine — First Day on a New Project

1. Read the contract / agreement.
2. Read Division 00 General and Supplementary Conditions in full.
3. Read Division 01 completely; extract a one-page checklist of GC obligations.
4. Skim Part 1 of every section in your scope; build the submittal schedule.
5. Identify all proprietary / single-source products; get pricing locked.
6. Identify all required mock-ups, special inspections, and pre-installation conferences; add to schedule.
7. Identify all testing requirements and confirm who pays.
8. Identify allowances, alternates, and unit prices; confirm in contract.
9. Identify long-lead items; start submittals immediately.
10. Distribute relevant spec sections to subs with their contracts as exhibits.

### 9.4 The Ten Things Most Likely to Cost You Money

1. Concrete strength higher than you bid.
2. Special inspections for failed work.
3. Mock-ups you did not budget for.
4. Level 5 drywall finish where you priced Level 4.
5. Mandated single-source windows or appliances.
6. Air-barrier testing that fails and requires re-do.
7. Closeout submittal preparation labor.
8. Temporary facilities (power, water, dumpsters) you assumed the owner would cover.
9. Cutting and patching responsibility ambiguity.
10. Punch list items beyond what you considered reasonable — driven by spec tolerance language.

---

## Closing Note — Becoming Fluent

You will not become fluent by reading this guide. You will become fluent by:

1. Reading Division 01 of your next three projects, cover to cover.
2. Building a submittal schedule from scratch for one project.
3. Sitting in on three pre-installation conferences.
4. Writing one NCR citing a specific spec section to back-charge a sub.
5. Successfully defending one architect challenge by quoting a spec back at them.

The spec is not a hostile document. It is the architect's effort to write down everything they want, in advance, so you can price it and build it. When you treat it as a partner — a checklist of what to do and what to prove — it becomes the cheapest insurance policy on the project. When you treat it as a stack of paper you don't have time to read, it becomes the most expensive thing in your file cabinet.

Read the spec. Bid the spec. Build the spec. Defend the spec. That is the discipline.
