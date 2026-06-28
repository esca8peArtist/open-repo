---
module: 33
title: "Quality Assurance and Quality Control Procedures"
discipline: ["quality-control", "inspections", "documentation", "warranty"]
audience: "GCs reducing warranty claims and improving project quality"
status: reference
created: 2026-05-13
tags: [career-training, QA/QC, inspections, punch-list, warranty, non-conformance, quality-documentation]
estimated-reading-time: 4 hours
---

# Quality Assurance and Quality Control Procedures

> **Purpose.** Quality failures in construction have a compounding cost structure: a defect caught during framing costs $200 to fix; caught during drywall it costs $2,000; found at closeout it costs $8,000; discovered by the owner after occupancy it costs $20,000 and a referral network. This module provides a systematic QC framework — from program structure through post-closeout warranty — that GCs can implement on any project without a dedicated quality manager.

> **Distinction between QA and QC.** Quality Assurance (QA) is the system — the program, the standards, the procedures. Quality Control (QC) is the execution — the actual inspections, tests, and documentation. Both are required. A QA program that isn't executed is a document. QC without a defined standard is guesswork.

---

## Table of Contents

1. [QC Program Structure](#1-qc-program-structure)
2. [Inspection Protocols by Trade](#2-inspection-protocols-by-trade)
3. [Testing Requirements and Acceptance Criteria](#3-testing-requirements-and-acceptance-criteria)
4. [Non-Conformance Procedures and Corrective Actions](#4-non-conformance-procedures-and-corrective-actions)
5. [Final Inspection and Punch-List Management](#5-final-inspection-and-punch-list-management)
6. [Warranty Claims and Post-Closeout Customer Communication](#6-warranty-claims-and-post-closeout-customer-communication)
7. [Quality Documentation for Liability Protection](#7-quality-documentation-for-liability-protection)
8. [Inspection Checklist Templates](#8-inspection-checklist-templates)

---

## 0. Mental Model — Quality Is a System, Not an Attitude

Every GC will tell you they care about quality. The ones who actually deliver it consistently have one thing the others lack: **a system**. Not a feeling. Not an intention. A documented sequence of checks, inspections, and sign-offs that happens on every project regardless of schedule pressure, budget strain, or the superintendent's mood on a given Friday.

The business case for systematic QC is straightforward:

**Cost of a warranty claim on a residential project (typical):**
- Rework labor and materials: $5,000–$40,000
- Subcontractor call-back (paid or argued): $2,000–$15,000
- GC management time: 20–40 hours × $75–$150/hr = $1,500–$6,000
- Owner relationship damage: lost referrals, lost repeat business
- Insurance premium impact if claim-filed
- Potential litigation: $20,000–$200,000+

**Cost of a systematic QC program on a $500,000 project:**
- Superintendent time for documented inspections: 15–25 hours/month × project duration
- Third-party testing fees: $1,500–$5,000
- Documentation system: $0 (template adoption) to $300/month (software)

**The math is not subtle.** One prevented warranty call pays for an entire project's QC program. The GCs with the lowest warranty claim rates are not luckier — they built a system.

---

## 1. QC Program Structure

### 1.1 The Three Layers of Quality Control

A complete QC program operates at three levels simultaneously:

**Layer 1 — Contractor Self-Inspection**
The GC's own superintendent inspects work before calling for any external inspection. No work should be submitted for official inspection without first passing the GC's internal check.

**Layer 2 — Owner/Architect Observation**
The owner or architect observes completed work at defined milestones — typically the same inspection points as AHJ inspections plus any project-specific quality checkpoints.

**Layer 3 — Third-Party and AHJ Inspections**
Authority Having Jurisdiction (building department) inspections, plus any third-party special inspections required by the permit (structural, soils, concrete, welding, etc.).

All three layers run in sequence for each milestone. Skipping Layer 1 (contractor self-inspection) is the most common failure — and it virtually guarantees that AHJ inspections will fail, which doubles the schedule impact of any problem.

### 1.2 The QC Plan Document

Every project of $250,000 or more should have a written QC Plan — a one-to-three-page document produced before construction begins that defines:

1. **QC Inspection Points** — the specific milestones at which inspections occur.
2. **Who inspects** — GC superintendent, sub foreman, or third-party special inspector.
3. **What standard applies** — California Building Code section, specification section, manufacturer instruction, or industry standard.
4. **Documentation required** — what form is filled out, what photos are taken, where they're filed.
5. **Acceptance criteria** — what passes vs. what requires correction.
6. **Non-conformance procedure** — what happens when something fails inspection.

**Sample QC Inspection Points for a residential new build:**

| Milestone | Inspection Type | Layer | Documentation |
|---|---|---|---|
| Foundation excavation | Soils / compaction | L2/L3 | Geotechnical letter or special inspector report |
| Rebar before concrete pour | Reinforcing steel | L1/L3 | Photo log; special inspector report if required |
| Foundation concrete pour | Concrete placement | L1 | Cylinder test samples; placement log |
| Underslab plumbing | Plumbing rough | L1/L3 | AHJ inspection card; photo log |
| Foundation walls | Form and pour | L1 | Photo before pour; cylinder tests |
| Framing pre-cover | Framing (full) | L1/L2/L3 | GC framing checklist; AHJ framing inspection |
| Shear walls | Nailing and hold-downs | L1/L3 | Nailing photo log; special inspector sign-off if required |
| Rough plumbing | All DWV and supply | L1/L3 | AHJ rough plumbing inspection card |
| Rough electrical | Panel, wiring, boxes | L1/L3 | AHJ rough electrical inspection card |
| HVAC rough | Duct layout, equipment | L1/L3 | AHJ mechanical rough inspection card |
| Insulation | R-value and coverage | L1/L3 | AHJ insulation inspection card; photo log |
| Drywall | Type, installation pattern | L1 | Photo log; per spec |
| Windows and waterproofing | Flashing, sealant | L1 | Photo log (critical pre-cover element) |
| Roofing | Underlayment before shingles | L1 | Photo log |
| Finish electrical | Device installation | L1 | Photo log; fixture list |
| Finish plumbing | Fixture installation; final pressure test | L1/L3 | Test log; AHJ final plumbing |
| Final building | Overall final inspection | L1/L2/L3 | AHJ final inspection; GC punch list completion |

### 1.3 Scheduling AHJ Inspections

Building department inspections must be scheduled in advance — typically 24–72 hours. In many California jurisdictions, inspections are scarce: a failed inspection means waiting another 24–72 hours for a reinspection, plus the cost of correcting the defect and the schedule impact.

**Best practice:** Never call for an AHJ inspection until Layer 1 (GC self-inspection) is complete and you are confident the work will pass. A failed AHJ inspection is a symptom of a failed internal QC process.

**AHJ inspection log — maintain per project:**

| Inspection | Date Requested | Date Inspected | Inspector Name | Result | Corrections Required | Reinspection Date | Final Result |
|---|---|---|---|---|---|---|---|
| Foundation | Mar 12 | Mar 13 | J. Smith | Pass | — | — | Pass |
| Framing | Apr 2 | Apr 4 | J. Smith | Fail | Missing hurricane tie at RR-14 | Apr 6 | Pass |
| Rough plumbing | Apr 8 | Apr 9 | M. Jones | Pass | — | — | Pass |

Track all failed inspections and their corrections. This log demonstrates due diligence and provides a factual record if an owner later claims persistent quality problems.

---

## 2. Inspection Protocols by Trade

### 2.1 Framing Inspection Protocol

Framing is the highest-consequence inspection because errors in framing are expensive to correct once concealed. A failed framing inspection after drywall is a catastrophic cost event.

**Pre-cover framing checklist (before calling for AHJ inspection):**

**Foundation and Sill:**
- [ ] Sill plate treated lumber where required (within 6" of concrete or where noted)
- [ ] Anchor bolts as shown on plans — spacing, distance from corners
- [ ] Foundation vents per code (1 sq ft per 150 sq ft of crawl space; or per mechanical ventilation design)

**Wall Framing:**
- [ ] Stud spacing as specified (16" or 24" OC per plans and engineering)
- [ ] Header sizes as specified by engineer or per table
- [ ] King studs and trimmers at all openings — both sides
- [ ] Corner framing complete (3-stud corners or engineered alternative)
- [ ] Fire blocking installed at required locations (at each floor level, in concealed spaces > 10 feet vertical, at top of wall cavities)
- [ ] Draftstops in attic and concealed spaces per California Building Code §718

**Shear Walls:**
- [ ] Shear wall locations per structural drawings
- [ ] Sheathing type and thickness per schedule
- [ ] Nailing schedule — nail size, spacing at panel edges and field — photograph critical panels before sheathing is continued
- [ ] Hold-down hardware installed and properly fastened — photograph each hold-down anchor
- [ ] Blocking at panel edges

**Roof Framing:**
- [ ] Rafter or truss spacing per plan
- [ ] Ridge board or structural ridge beam as specified
- [ ] Collar ties or ridge straps as required
- [ ] Hurricane ties / rafter ties at each rafter-to-top-plate connection (required in California's high-wind and seismic zones — verify requirement with local AHJ)
- [ ] Blocking at bearing points and at gable ends
- [ ] Attic access opening per code (minimum 22" × 30"; clearance above hatch)

### 2.2 Rough Electrical Inspection Protocol

**Box placement and mounting:**
- [ ] Outlet boxes at correct height (standard: 12" to center; GFCI per NEC/CEC requirements)
- [ ] Switch boxes at correct height (standard: 48" to center)
- [ ] Box fill calculation complete — no overcrowded boxes (NEC Article 314)
- [ ] Boxes secured to studs or blocking

**Wiring:**
- [ ] Wire type correct for application (NM cable in dry locations; MC or conduit where required)
- [ ] Wire protected at notches (nail plates per CEC/NEC §300.4)
- [ ] Wire secured within 12" of box and at max 4.5' intervals (NM cable per NEC §334.30)
- [ ] Minimum 6" of free conductor at each box
- [ ] Correct wire gauge for circuit ampacity
- [ ] Ground wire continuous

**Panel:**
- [ ] Panel location per plan; clearances per NEC §110.26 (36" in front; 30" wide; 6.5' headroom)
- [ ] Breaker sizes as designed; no double-tapping
- [ ] Neutral and ground separated at main panel; bonded at service entrance
- [ ] Arc fault circuit interrupter (AFCI) breakers installed where required (bedrooms, living areas — CEC/NEC 210.12)
- [ ] GFCI circuit breakers or devices where required (bathrooms, kitchens, garages, outdoors, crawlspaces — NEC 210.8)

### 2.3 Rough Plumbing Inspection Protocol

**DWV (Drain, Waste, Vent) System:**
- [ ] Pipe material and grade as specified (ABS, PVC, cast iron per local AHJ preference)
- [ ] Slope: drain pipes 1/4" per foot minimum; no negative slope anywhere
- [ ] Clean-out locations per code (within 5' of building exterior; at each change of direction > 45°; at top of each stack)
- [ ] Vent stack penetrations through roof — proper flashing
- [ ] P-traps at every fixture location; no S-traps (prohibited by CPC)
- [ ] Air admittance valves — only where permitted by local AHJ (not universally accepted in California)
- [ ] Pressure test: 5 PSI air or water test on DWV for 15 minutes with no pressure drop

**Supply Piping:**
- [ ] Pipe material per specification (copper, CPVC, PEX — verify local code acceptance)
- [ ] Isolation valves at each fixture group and at each toilet and appliance
- [ ] Expansion tank installed on water heater where required (closed systems)
- [ ] Water hammer arrestors at washing machine and dishwasher connections
- [ ] Pressure test: 100 PSI for 30 minutes on water supply with no pressure drop

**Water Heater:**
- [ ] T&P (temperature and pressure) relief valve installed; discharge pipe to within 6" of floor
- [ ] Seismic strapping — California requires two-point strapping on all residential water heaters

### 2.4 Concrete Inspection Protocol

**Pre-pour inspection:**
- [ ] Rebar size, spacing, and coverage (minimum 3" clear to earth; 1.5" interior minimum) match structural drawings
- [ ] Rebar laps per structural engineer's specifications
- [ ] Sleeves, conduit, and embedded items placed correctly
- [ ] Form dimensions match design; forms clean and properly oiled/released
- [ ] Subgrade compacted and tested (proctor density test if required by soils report)
- [ ] Special inspector on site if required by permit

**During pour:**
- [ ] Slump test at point of delivery — maximum slump per specification (typically 4" for structural concrete)
- [ ] Concrete cylinder samples taken — minimum 2 cylinders per 50 CY or one set per truck if small pour
- [ ] Vibration for consolidation — avoid over-vibrating
- [ ] No addition of water at the truck on site without engineer's authorization
- [ ] Pour continuous without cold joints unless designed

**Post-pour:**
- [ ] Curing compound applied or wet cure maintained per specification
- [ ] Temperature monitoring if cold weather
- [ ] Cylinder test results tracked; 28-day strength confirms design strength

### 2.5 Finish Work Inspection Protocol

**Drywall:**
- [ ] Board type correct for location (Type X in fire-rated assemblies; moisture-resistant in bathrooms)
- [ ] Fastener spacing per manufacturer and code (8" OC on edges, 12" OC in field for walls)
- [ ] No butt joints over doors/windows unless blocked
- [ ] Corner bead straight; no voids at mud joints
- [ ] Three-coat finish for smooth walls; two-coat minimum for textured

**Tile:**
- [ ] Substrate: cement board or tile backer in wet areas; no drywall directly in showers
- [ ] Waterproof membrane in shower areas: verify installation per manufacturer instructions before tile
- [ ] Thin-set type and coverage: 95% back-butter coverage in wet areas per ANSI A108 standards
- [ ] Grout joint size consistent; full grout coverage; no hollow-sounding tiles after installation
- [ ] Caulk at changes of plane (floor-to-wall, wall-to-tub, wall-to-counter) — never grout at changes of plane

**Paint and Finishes:**
- [ ] Surface preparation: all holes filled; surface sanded; primer coat applied
- [ ] Sheen level per specification (eggshell, satin, semi-gloss in wet areas)
- [ ] Coverage: no roller marks, lap marks, or holidays (missed areas)
- [ ] Trim painting: clean edges, no bleeding onto walls; consistent caulk lines
- [ ] Review at different light angles (oblique natural light reveals most paint defects)

---

## 3. Testing Requirements and Acceptance Criteria

### 3.1 Mandatory Tests by Phase

| Test | When | Acceptance Criteria | Who Performs |
|---|---|---|---|
| Soil compaction (Proctor density) | Before foundation, before slab | Per geotechnical report; typically 90–95% maximum dry density | Geotechnical or special inspection firm |
| Concrete cylinder break (28-day) | Each significant pour | Fc specified (typically 2,500–4,000 PSI residential; higher commercial) | Testing lab from cylinders taken at pour |
| DWV pressure test | Before concealment | 5 PSI air or water; no drop over 15 minutes | GC or plumbing sub |
| Water supply pressure test | Before concealment | 100 PSI; no drop over 30 minutes | GC or plumbing sub |
| HVAC duct leakage test (California Title 24) | Before insulation conceals ducts | Per Title 24 — leakage < 6% of system air flow | HERS rater (required for Title 24 compliance) |
| Blower door test (California Title 24) | Near final, before closeout | Per Title 24 energy model | HERS rater |
| GFCI/AFCI breaker test | At final electrical | 100% of GFCI/AFCI outlets and breakers tested with tester | GC or electrician |
| Structural special inspections | Per IBC/CBC and permit | Per structural engineer's inspection program | DSA-approved special inspector (if required) |

**California-specific testing:** California Title 24 energy compliance requires HERS (Home Energy Rating System) verification for duct leakage and building envelope infiltration. Budget approximately $800–$1,500 for a HERS rater on residential projects. Failure to obtain the HERS verification prevents final permit sign-off.

### 3.2 Special Inspections — California Requirements

California Building Code (CBC) Section 1705 requires **special inspections** for the following work types when indicated on the permit:

| Work Type | When Special Inspection is Required |
|---|---|
| Concrete — high-strength | Fc > 5,000 PSI |
| Concrete — all new residential over 2 stories | Per CBC §1705.3 |
| Reinforcing steel | In seismic design categories D, E, F |
| Structural steel — welding | All structural steel connections |
| Structural masonry | All structural masonry |
| Driven piles / drilled piers | All deep foundations |
| Shotcrete | All applications |
| Seismic force-resisting systems | In SDC D, E, F |

The **Statement of Special Inspections** must be submitted with the permit. The approved special inspection agency conducts inspections during construction and provides a final statement of compliance.

**GC responsibility:** Coordinate the special inspector's schedule so they are on site when the work requiring inspection is occurring. A special inspector who arrives after the work is concealed has no value. Log every special inspector visit in the daily report.

---

## 4. Non-Conformance Procedures and Corrective Actions

### 4.1 What Is a Non-Conformance

A **non-conformance** is any condition where the installed work does not meet the contract documents, the applicable code, or the manufacturer's installation requirements. Non-conformances range from minor (paint touch-up) to major (incorrect rebar in poured concrete).

The GC must have a defined, systematic response to non-conformances. An ad hoc, case-by-case response leads to inconsistency, missed corrections, and documentation gaps that cause later disputes.

### 4.2 Non-Conformance Report (NCR) Process

**Step 1 — Identify and Document.** When a non-conformance is found (by GC, AHJ, owner, or third-party inspector), issue a **Non-Conformance Report** within 24 hours:

```
NON-CONFORMANCE REPORT
Project: __________________ NCR No.: _____ Date: _______
Location: _____________________ (building grid, room number)
Identified by: _________________ (inspector name/title)
Work affected: _________________

DESCRIPTION OF NON-CONFORMANCE:
[Specific description of what does not conform and why]

REFERENCE: CBC Section ___ / Specification Section ___ / Drawing ___ / 
           Manufacturer instruction ___

PHOTOS: Attached (Exhibit A)

DISPOSITION OPTIONS:
[ ] Repair/Rework — correct to specification
[ ] Replace — remove and reinstall correctly
[ ] Accept as-is — if Owner/Architect agrees non-conformance has no 
    functional or structural impact (requires written acceptance)
[ ] Other engineering resolution — engineer's written approval of 
    alternate compliance

REQUIRED ACTION: ______________________________________________
ACTION ASSIGNED TO: _______________ DUE DATE: _______________
VERIFICATION OF COMPLETION: ________ by: ___________________
```

**Step 2 — Disposition.** One of four dispositions applies:
- **Repair/rework:** Sub corrects the work to specification. GC verifies.
- **Replace:** Work is removed and reinstalled correctly.
- **Accept as-is with written approval:** Only appropriate when the non-conformance is confirmed by the engineer or architect to have no structural, safety, or code compliance impact. Get the acceptance in writing — always.
- **Engineering resolution:** Engineer of record approves an alternate means of compliance.

**Step 3 — Verify Correction.** After the sub claims correction, the GC superintendent re-inspects. Photograph the corrected condition. Close the NCR with the verification date and inspector's name.

**Step 4 — Track.** Maintain an NCR log throughout the project. Review open NCRs weekly until all are closed.

### 4.3 Handling the Sub Who Resists Correction

A sub who is told to rework their work is losing money — the rework costs them labor without additional payment. Some resistance is natural. The GC's response should be firm, systematic, and documented.

**Sequence:**
1. Identify the non-conformance in writing (NCR).
2. Direct the sub to correct within a defined timeframe (24–72 hours for safety-related; 5 business days for cosmetic).
3. If the sub does not correct within the timeframe, issue a **written performance notice** (see Module 30, Section 4.2).
4. If the sub continues to resist, the GC may correct the work with another sub or GC forces and **backcharge** the cost to the non-conforming sub.
5. Document every step. The backcharge is only collectible if the paper trail is complete.

**The "close enough" trap:** Never accept work that doesn't meet specification simply because correcting it is inconvenient. If you accept defective work from a sub today, you own that defect for the life of the building. When the homeowner calls in year 3 about a leak at the window you "accepted" from the window sub, you pay — not the sub.

---

## 5. Final Inspection and Punch-List Management

### 5.1 The Pre-Final Walkthrough

Before the owner walkthrough or AHJ final inspection, conduct a **GC pre-final inspection** — a room-by-room, system-by-system review of the entire project. This is the last quality gate before the project transfers to the owner.

Assign a PM or senior superintendent who was not involved in the daily field work — fresh eyes catch things the team has become blind to.

**Pre-final inspection approach:**
- Walk each room in sequence with a clipboard or mobile app.
- Check all four directions in each room (walls, ceiling, floor).
- Test every device: switches, outlets (GFCI test), plumbing fixtures, HVAC operation, doors and hardware.
- Review all exterior elements: roofing, flashing, siding, exterior doors and windows, flatwork and drainage.

### 5.2 Generating and Managing the Punch List

A **punch list** is the written record of all incomplete or defective items identified during final inspection. It is a working document, not an accusation — it is the GC's tool for completing the project.

**Punch list best practices:**

1. **Location-coded items.** Each punch list item should include exact location (Room 204, north wall; Master bath, toilet compartment; SW corner of garage).
2. **Photo for each item.** Attach a photo to each punch list item. This eliminates ambiguity ("what exactly is wrong with the paint in the hallway?").
3. **Trade assignment.** Each item is assigned to the responsible trade. The sub knows which items are theirs.
4. **Due date.** Each item has a due date — typically 5–10 business days.
5. **Digital format.** Use a punch list app (Procore punch list, Buildertrend, or even a Google Sheet shared with all subs) — paper punch lists get lost; digital lists can be sorted, filtered, and tracked in real time.

**Punch list stages:**
- **Owner punch list:** Items the owner/architect identifies during their walkthrough.
- **GC punch list:** Items the GC identified in the pre-final inspection.
- **Consolidated punch list:** Both combined; de-duplicated; assigned.

**Managing the punch list to close:**

The punch list can become a project-ending drag if not managed aggressively. Common failure patterns:
- Items sit for weeks because no one owns them.
- The punch list keeps growing as the owner adds new items.
- The GC waits for all items to be done before calling for final inspection — when the work could be certified complete sooner.

**Counter-strategies:**
- Assign a PM specifically to punch list management for the last 2–4 weeks of a project.
- Issue a final punch list closure date — after this date, new items are warranty work, not punch list.
- Withhold sub final payment until their punch items are complete.

### 5.3 Certificate of Substantial Completion

**Substantial completion** is the date when the work is sufficiently complete that the owner can occupy and use the project for its intended purpose, even if minor items remain.

This date matters for:
- Warranty start dates (typically begin at substantial completion).
- Contractor's final payment trigger (typically on substantial completion or certificate of occupancy).
- Lien deadlines (see Module 13).

Issue a formal **Certificate of Substantial Completion** (AIA G704 or similar) signed by the contractor, owner, and architect (if applicable). Attach the punch list as Exhibit A. This document is the legal boundary between the construction phase and the warranty phase.

---

## 6. Warranty Claims and Post-Closeout Customer Communication

### 6.1 California Warranty Standards

**Express warranty:** The warranty your contract provides. California residential construction typically warrants workmanship for 1 year from substantial completion. Manufacturer warranties on materials and equipment are passed through.

**Statutory implied warranties (California Civil Code §900–945.5 — SB 800):**
California's Right to Repair Act (SB 800, 2002) creates specific statutory standards for new residential construction (single-family and multi-unit up to 4 stories):

| Category | Statutory Period |
|---|---|
| Fit and finish (paint, tile, carpeting, cabinet surfaces) | 1 year |
| Plumbing and sewer systems | 4 years |
| Electrical systems | 4 years |
| Other systems (structural, mechanical) | 4 years |
| Soil and foundation settling causing structure damage | 10 years |
| Structural defects (load-bearing components) | 10 years |
| Water infiltration and waterproofing | 10 years |

**SB 800 pre-litigation process:** Before an owner can file a lawsuit for construction defects in new residential construction, they must follow SB 800's Notice and Opportunity to Repair process:
1. Owner provides written notice of the defect.
2. Contractor has 14 days to acknowledge.
3. Contractor has 35 days to inspect.
4. Contractor has 30 days after inspection to offer to repair or compensate.
5. Owner must accept or reject the offer before suing.

Failure to follow this process can result in the owner's lawsuit being stayed. As the contractor, **you must respond to written defect notices within the statutory periods** — missing these deadlines can prejudice your rights in subsequent litigation.

### 6.2 Warranty Response Procedure

**When a warranty claim arrives:**

1. **Acknowledge in writing within 5 business days.** Even if you dispute the claim, acknowledge receipt and state you will inspect. Ignoring warranty claims is the fastest path to a lawsuit.

2. **Inspect promptly.** Schedule the inspection within 2 weeks of the claim. Bring your superintendent and potentially the responsible sub-foreman.

3. **Document the inspection.** Photos of the claimed defect condition; measurements; comparison to specification.

4. **Determine responsibility:**
   - Is this a workmanship defect? (Your obligation.)
   - Is this a material failure? (Manufacturer's warranty — you facilitate, they pay.)
   - Is this owner abuse or modification? (Not your warranty obligation.)
   - Is this normal settling or movement within acceptable parameters? (May not be a defect.)

5. **Respond in writing within a reasonable time** — 10–14 business days — with your determination and, if repair is warranted, a proposed schedule.

6. **Repair promptly once authorized.** Every week of delay in repairing a warranty item increases owner frustration and legal exposure.

7. **Document the repair.** Photos before and after. Written confirmation that the owner accepts the repair.

### 6.3 Post-Closeout Customer Communication

The GC who disappears after the certificate of occupancy is a GC who will never get a referral from that project.

**Best practice post-closeout communication:**

| Timing | Action | Purpose |
|---|---|---|
| Move-in day | Deliver owner's manual binder | Establishes professionalism; provides all warranty documents |
| 30 days post-occupancy | Follow-up call or email | Catch early issues before they become frustrations |
| 11 months post-occupancy | Written reminder of 1-year warranty expiration | Invites owner to submit any final warranty items before expiration; demonstrates good faith |
| 18 months | Check-in | Touch point for referral generation |
| Annual | Holiday or appreciation contact | Relationship maintenance |

**The owner's manual binder** (deliver at substantial completion):
- Copy of the signed contract
- All warranty certificates (HVAC, roofing, windows, appliances)
- Equipment manuals (HVAC, water heater, appliances)
- Paint colors with Benjamin Moore / Sherwin Williams codes
- Tile and material supplier contact information (for future additions)
- Plumbing valve locations
- Electrical panel directory
- GC contact information and warranty claim procedure

This binder costs the GC $20 and an hour of PM time. Its value in referral generation over the next 10 years is immeasurable.

---

## 7. Quality Documentation for Liability Protection

### 7.1 Documentation as Your Defense

In California, latent construction defect claims can be brought up to **10 years after substantial completion** (CCP §337.15). A lawsuit filed 8 years after closeout is not uncommon on multi-million-dollar projects. Your defense in that lawsuit is your project documentation: daily logs, inspection records, photos, third-party inspection reports, and certified test results.

**A GC whose records show:**
- Systematic pre-cover inspections with photos
- Third-party special inspection reports
- Passed AHJ inspections at every stage
- Concrete cylinder test results confirming design strength
- HERS verification for Title 24 compliance

...has a fundamentally different litigation posture than a GC whose records consist of a permit card and some photos of the finished product.

### 7.2 Critical Pre-Cover Documentation

The most important photos in any construction project are the ones taken immediately before concealment:

| Concealment Event | What to Photograph Extensively |
|---|---|
| Drywall over rough MEP | All pipe and wire runs; labels on wires; all junction boxes; HVAC duct connections |
| Concrete over rebar/underslab | Rebar layout with tape measure visible; all embedded items; special inspector on site |
| Backfill over underground | Pipe type and depth; bedding material; compaction; sleeve locations |
| Siding over housewrap/flashing | All window flashings; all penetration flashings; housewrap laps; tape at penetrations |
| Roofing over underlayment | Underlayment laps; all flashings (valley, step, counter, base); ice and water shield if used |
| Insulation over framing | Insulation type, thickness, and coverage; thermal bridging details |

"Extensive" means 20–40 photos per milestone on a typical room, not 2–3. Storage is cheap. A photo that proves the flashing was correctly installed in 2026 is priceless in 2031 when the litigation subpoena arrives.

### 7.3 Document Retention Schedule

| Document Type | Retention Period | Format |
|---|---|---|
| Daily logs | 12 years | Digital (cloud backup) |
| Inspection photos | 12 years | Cloud (organized by date and location) |
| AHJ inspection cards | 12 years | Scan originals; retain physical |
| Special inspection reports | 12 years | Digital |
| Test results (concrete, compaction) | 12 years | Digital |
| Punch list and NCR logs | 12 years | Digital |
| Warranty claims and correspondence | 12 years after claim resolved | Digital |
| Subcontract documents | 12 years | Digital |
| As-built drawings | 12 years | Digital (PDF) |
| Owner's manual binder | Retain a copy | Digital |

**12-year standard:** The 10-year latent defect period plus 2 years of buffer. After 12 years from substantial completion, California's statute of repose (CCP §337.15) bars new construction defect claims (with limited exceptions for fraudulent concealment).

---

## 8. Inspection Checklist Templates

### 8.1 Pre-Framing-Inspection Self-Check Checklist

Use before calling AHJ for framing inspection:

**Foundation / Sill:**
- [ ] Sill bolts at max 6' OC, within 12" of each end, with washers
- [ ] Sill plate PT lumber where required; correct species/treatment (AWPA UC4B for soil contact)
- [ ] All anchor bolts as shown; nothing added without engineer review

**Walls:**
- [ ] Stud spacing per plan (16" or 24" OC)
- [ ] Double top plate with lap joints offset minimum 24"
- [ ] All headers correct size per plan; installed with crown up
- [ ] King studs and jack studs (trimmers) both sides of each opening
- [ ] Fire blocking installed at horizontal concealed spaces, at each floor, and at 10' vertical intervals
- [ ] Shear wall panels correct type and nailed per schedule — photo taken

**Roof:**
- [ ] Rafter or truss at correct spacing; all bearing points secured
- [ ] Hurricane straps or equivalent at all rafter-to-wall connections
- [ ] Ridge beam or board correct size
- [ ] Blocking at gable ends and at all bearing points

**Pre-call confirmation:** GC superintendent has walked all areas. [ ] Pass — ready for AHJ inspection.

---

### 8.2 Punch List Item Template (per item)

```
PUNCH LIST — [Project] — Item #_____

Location: __________________ (room name, orientation, grid reference)
Trade responsible: ______________
Description: __________________________________________
Photo: Attached Y / N — Exhibit #____
Standard not met: CBC §___ / Specification §___ / Owner selection ___
Priority: [ ] Safety  [ ] Code  [ ] Contract  [ ] Cosmetic
Required correction: ______________________________________
Assigned to: _________________ Due date: _________________
Verified complete: Y / N   Verified by: _______ Date: _______
```

---

### 8.3 Warranty Response Letter Template

```
[Date]

To: [Owner Name]
Re: [Project Address]
Subject: Warranty Inspection — [Brief description of claim]

Thank you for notifying us of the [issue described] at your property. 
We take all warranty matters seriously and will respond promptly.

We will schedule an inspection visit within the next [10] business 
days. Our superintendent [Name] will contact you directly to arrange 
a mutually convenient time.

Following inspection, we will provide you with a written determination 
within [14] business days, including our proposed course of action if 
a warranty repair is required.

Our warranty covers [describe scope] through [date — 1 year from 
substantial completion]. This matter is within that period and will 
be addressed accordingly.

Please do not make any repairs to the affected area prior to our 
inspection, as this may affect our ability to assess the condition 
and determine the appropriate remedy.

Sincerely,
[Name, Title, Company]
[Phone, Email]
```

---

**Cross-reference:** Module 07 (Residential GC: Scope, Trades, and People Management) for day-to-day field management; Module 21 (Project Closeout, Punch List, and Warranty) for the formal closeout sequence; Module 13 (Construction Law and Lien Rights) for warranty period legal framework and SB 800; Module 24 (Reading Construction Specifications) for specification compliance interpretation.

**Key California resources:**
- California Building Standards Code (CBC 2022): bsc.ca.gov
- California Title 24 Energy Standards: energy.ca.gov/title-24
- California SB 800 Right to Repair Act: Civil Code §895–945.5
- California HERS program: energy.ca.gov/programs-and-topics/programs/home-energy-rating-system-hers-program
