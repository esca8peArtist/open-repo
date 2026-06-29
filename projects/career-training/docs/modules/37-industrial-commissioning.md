---
module: 37
title: "Industrial Commissioning: Functional Testing, Mechanical Handoff, and Owner Training"
discipline: ["commissioning", "mechanical-systems", "testing", "project-closeout", "operations-handoff"]
audience: "Industrial GCs and mechanical/electrical specialty subs transitioning to prime GC roles"
status: reference
created: 2026-06-28
tags: [career-training, commissioning, functional-testing, pre-functional-testing, deficiency-management, owner-training, system-acceptance, ashrae, industrial]
estimated-reading-time: 4 hours
---

# Industrial Commissioning: Functional Testing, Mechanical Handoff, and Owner Training

> **Purpose.** Module 02 mentions "commissioning support" as part of field execution. The actual commissioning workflow—pre-functional checklists, functional performance testing, deficiency tracking and resolution, system startup sequences, owner training documentation, and final acceptance—is not taught anywhere in the curriculum. This module teaches the operational discipline that separates GCs whose projects reach final payment with satisfied operations teams from those who leave behind deferred punch lists, warranty disputes, and owner dissatisfaction.

> **Distinction from Module 02.** Module 02 covers general field execution and handoff basics. This module teaches the systematic commissioning process that industrial and commercial mechanical systems require to transition safely and effectively from the GC's construction phase to the owner's operations phase.

---

## Table of Contents

1. [What Commissioning Is and Why It Matters](#1-what-commissioning-is-and-why-it-matters)
2. [Pre-Functional Testing: Installation Verification](#2-pre-functional-testing-installation-verification)
3. [Functional Performance Testing: Does It Work as Designed?](#3-functional-performance-testing-does-it-work-as-designed)
4. [The Deficiency Log: Discovery Through Closure](#4-the-deficiency-log-discovery-through-closure)
5. [Owner Training and Documentation](#5-owner-training-and-documentation)
6. [Final Acceptance and Payment](#6-final-acceptance-and-payment)
7. [ASHRAE and Regulatory Context](#7-ashrae-and-regulatory-context)

---

## 0. Mental Model — Commissioning Is the Bridge Between Construction and Operations

Most GCs view commissioning as a checkbox at the end of the project: "Get the system running, hand over the keys, move to the next job." This approach leaves the owner's operations team with systems they don't understand, defects they'll discover later, and warranty disputes that damage the GC's reputation.

**Real commissioning** is the systematic handoff process that verifies the system works as designed, trains the owner's operations staff to operate it safely, and resolves defects before the GC loses access. The business case:

- **Final payment protection:** Most industrial and commercial contracts tie retainage release to commissioning completion. A GC that doesn't complete commissioning doesn't get paid.
- **Warranty reduction:** Systems started correctly under supervision rarely produce warranty callbacks. Systems started carelessly produce emergency calls at 2:00 AM.
- **Owner relationship:** The operations team who trains with the GC becomes the GC's repeat-business advocate. The operations team who discovers problems after the GC leaves becomes the GC's critic.
- **Regulatory compliance:** Systems that pass a formal commissioning process are defensible if a regulator or insurance claim examines them later.

The discipline required: Pre-functional checklists, functional performance tests, documented deficiency tracking, hands-on owner training, and final acceptance sign-off. This module teaches all five.

---

## 1. What Commissioning Is and Why It Matters

### 1.1 Commissioning Defined

Commissioning is the process of verifying that building systems are installed in accordance with the design intent and that they perform as designed. ASHRAE Guideline 0-2021 defines it as "the process of achieving, verifying, and documenting that all building systems perform interactively according to the design intent and the owner's operational needs."

Three key elements:
1. **Verification:** Systems are installed correctly and completely.
2. **Testing:** Systems operate per the design engineer's specifications and control sequences.
3. **Documentation and training:** The owner receives a complete technical package and hands-on training from the system operators who will run it.

### 1.2 The GC's Role vs. the Commissioning Agent's Role

On a project with a dedicated commissioning agent (common on larger industrial and institutional projects), roles are distributed:

- **Commissioning agent:** Independent third party who oversees the entire process, reviews test results, signs off on the system.
- **Mechanical/electrical contractor:** Executes the pre-functional tests and most of the functional tests (with the commissioning agent witnessing and approving).
- **Design engineer:** Provides the test procedures, defines pass/fail criteria, may be present during critical testing (especially startup sequences).
- **GC:** Ensures all parties perform their roles, manages schedules and access, coordinates the commissioning agenda with the owner.

On a smaller project without a dedicated commissioning agent, the GC often assumes the commissioning agent role, or the mechanical contractor provides commissioning services. Regardless of the structure, the GC is accountable for ensuring commissioning is completed before final payment is released.

### 1.3 Why Commissioning Matters for Final Payment

Most industrial and commercial contracts explicitly condition final retainage release on commissioning completion. Example contract language:

> "Final payment shall not be due until (a) the project is substantially complete; (b) all systems have passed functional performance testing; (c) all commissioning deficiencies have been resolved and accepted by the design professional; (d) the owner has received training documentation and the owner's operators have been trained on all critical systems; and (e) the commissioning agent (if applicable) has issued a written Commissioning Completion Certificate."

A GC that does not complete commissioning literally cannot collect final payment. The retainage may be 5–10% of the contract value; on a $2M industrial project, retainage is often $100,000–$200,000. Missing commissioning holds that money indefinitely.

### 1.4 ASHRAE Guideline 0 — The Industry Standard

ASHRAE (American Society of Heating, Refrigerating and Air-Conditioning Engineers) publishes Guideline 0, which establishes the standard commissioning process. While ASHRAE 0 is technically guidance (not code), many architectural specifications and industrial owner standards reference it explicitly. Understanding the basic framework ensures the GC can speak credibly with commissioning agents and design engineers.

The ASHRAE process includes:
- **Planning phase:** Commissioning authority identified; scope defined; testing procedures outlined.
- **Design phase:** Commissioning requirements incorporated into construction documents; specifications updated to include commissioning requirements.
- **Construction phase:** Pre-functional tests verify installation; functional performance tests verify operation.
- **Acceptance phase:** Systems accepted by owner operations team; training completed; documentation delivered.

For most GCs, the relevant phases are construction and acceptance. This module focuses on those phases.

---

## 2. Pre-Functional Testing: Installation Verification

### 2.1 What Pre-Functional Testing Verifies

A pre-functional test (PFT) is not a performance test. It's an installation verification checklist that confirms the system is complete, clean, and ready for performance testing. Think of it as "are all the components installed and in place?" not "does it work correctly?"

Typical PFT verification points:
- All components (fans, pumps, motors, dampers, sensors) are physically present.
- All electrical connections are complete and labeled per drawings.
- All mechanical connections (bolts, welds, flange gaskets) are complete and tight.
- Systems are clean (no construction debris, no dirt in ducts or pipes).
- All startup prerequisites are met (fluids filled, filters installed, electrical panels energized).
- Safety interlocks and emergency shutdown systems are operable (tested for mechanical function, not electrical logic).
- All instrumentation (thermometers, gauges, pressure indicators) is installed and readable.

### 2.2 PFT Checklist Structure by System Type

**HVAC Systems:**
- Air handling units: motors installed, belts set to correct tension, dampers free and movable, filters installed
- Ductwork: sealed, insulated (if specified), all connections complete, no visible damage
- VAV boxes and terminal units: physically installed, strapped, dampers operable
- Thermostats and sensors: installed in correct locations, accessible and readable
- Refrigerant lines: brazed connections pressure-tested, insulation intact
- Exhaust fans: installed, accessible, damper operable

**Plumbing Systems:**
- Pressure test certificates available (confirms rough piping passed hydrostatic test)
- All insulation installed on hot water and chilled water lines
- Strainers installed upstream of sensitive equipment (pumps, boilers)
- Pressure relief valves installed and set to design pressure (can be verified visually; final functional test confirms opening pressure)
- Traps primed (water fill at fixture level)
- All connections made up and free of leaks (visual inspection under light load)

**Electrical Systems:**
- All branch circuits labeled per one-line diagram
- Breakers installed and in "off" position
- Grounding continuity verified (megger test or continuity meter)
- All equipment grounding straps installed and tight
- Cable tray and conduit properly supported and bonded
- Emergency systems (generator, UPS) fuel supply confirmed available

**Process Piping (industrial):**
- Hydrostatic test certificates available (rough piping passed)
- All insulation installed
- All flanged connections made up, bolted to spec torque
- System flushed and debris removed (flushing certificates available)
- Non-destructive examination (NDE) completed per spec (X-rays, ultrasonic thickness on critical welds)

### 2.3 Who Executes PFT and Documentation

The installing contractor (the mechanical, electrical, or plumbing sub) typically executes the PFT. A commissioning agent (if present) or the GC witnesses key steps and verifies completion. The PFT is not a pass/fail test; it's a checklist. Items that fail are corrected and rechecked before moving to functional performance testing.

**PFT Documentation:**
A simple form listing each verification point, marked "pass" or "fail," signed by the responsible contractor and the GC (or commissioning agent). The PFT becomes part of the operations and maintenance (O&M) package delivered to the owner at closeout.

### 2.4 What Happens When PFT Fails

PFT failures are common and expected. Examples:
- A valve is installed backward (happens more than once per year in typical industrial projects).
- Electrical breaker labeling is incomplete.
- Insulation is missing on a 3-inch hot water line.
- A strainer is installed in the wrong location.

The process: deficiency is identified on the PFT checklist, the responsible contractor corrects it, the GC or commissioning agent re-verifies, and the PFT item is marked "pass." The project does not proceed to functional performance testing until all PFT items pass.

---

## 3. Functional Performance Testing: Does It Work as Designed?

### 3.1 The Difference Between PFT and FPT

**Pre-Functional Testing** answers: "Is it installed?"

**Functional Performance Testing** answers: "Does it work as designed?"

PFT is a visual/mechanical checklist. FPT involves operating the system and measuring performance against the design engineer's specifications.

### 3.2 FPT Procedures by System Type

**HVAC Systems:**
- Air balancing: measure actual airflow at each VAV box outlet, compare to design airflow, adjust dampers until design flow is achieved
- Setpoint verification: set the thermostat to setpoint (say, 72°F heating); verify that system initiates heating; measure discharge air temperature to confirm it's heating (not cooling)
- Control sequence verification: confirm the control logic operates as designed (example: if outdoor air temperature drops below 55°F, economizer damper closes and heating engages)
- Alarm testing: trigger an alarm condition (temperature sensor failure, filter differential pressure high, etc.) and confirm the control system responds correctly (raises alarm, shuts down equipment if appropriate)
- Equipment startup: run the system for 1–4 hours and observe for abnormal noise, vibration, or temperature/pressure conditions

**Process Piping and Mechanical Systems:**
- Pressure hold: close isolation valves, pressurize the system to design pressure (or test pressure if specified), measure pressure decay over 30 minutes or 1 hour (confirms no leaks, no slow weeping)
- Flow testing: with the system running, measure flow at inlet and outlet; confirm flow is within ±5% of design flow
- Relief valve testing: pressurize the system; confirm the relief valve opens at its set pressure (within ±5%); confirm it closes and holds downstream pressure without weeping (slow drip)
- Temperature monitoring: if the system should maintain a certain temperature (chilled water at 45°F, hot water at 180°F), operate the system for 30 minutes and confirm temperature regulation

**Electrical Systems:**
- Load bank testing: connect a temporary load bank (dummy electrical load) to the system; verify the generator can sustain rated load without dropping voltage
- UPS failover testing: operate the system from battery only; confirm it can sustain load for the design duration (typically 5–15 minutes)
- Bus transfer testing: simulate a loss of primary power; confirm the bus transfer switch transfers load to backup power (typically a generator) within the design time (typically 250 ms or less)
- Generator transfer and sync testing: start the generator and confirm it synchronizes with the utility grid and accepts load in the correct sequence (this is a critical step and should be supervised by the commissioning engineer)

### 3.3 FPT Pass, Conditional Pass, and Fail Criteria

**Pass:** The system meets the design specification. Example: discharge air temperature is 55°F ± 2°F, per design spec.

**Conditional Pass:** The system is functional but outside the design specification by a minor amount that does not impair safety or performance. Example: discharge air temperature is 58°F when design is 55°F ± 2°F. The measurement is slightly high but is close enough that the system is acceptable without correction. A conditional pass is typically acceptable if the design professional agrees.

**Fail:** The system does not meet the design specification and cannot be accepted without correction. Example: the system will not reach design pressure; relief valve does not hold pressure. This triggers a deficiency that must be corrected and retested.

### 3.4 The Owner's Role in FPT

The owner's operations staff (the people who will operate the system after the GC leaves) should witness functional performance testing. This is their first live exposure to the system. The questions they ask during testing ("What does that gauge measure?" "What should I do if the temperature alarm goes off?" "How often do we clean the filter?") become the focus of training after testing is complete.

### 3.5 Seasonality and Deferred Testing

Some systems cannot be fully tested in non-design conditions. An HVAC heating system cannot be tested in cooling mode during summer. A rooftop chiller cannot be tested in freezing outdoor air conditions.

Contract language typically addresses this:
> "Heating mode functional performance testing may be deferred until outdoor air temperature falls below 50°F. The owner accepts the system for provisional occupancy pending completion of deferred testing. The GC shall complete deferred heating-mode testing during the first appropriate season (projected January–March) and shall notify the owner of completion."

This is called "provisional acceptance" or "conditional acceptance." The owner gets occupancy; the GC retains the right to complete testing when conditions allow.

---

## 4. The Deficiency Log: Discovery Through Closure

### 4.1 The Deficiency Log Format

A deficiency log is a simple table that tracks every issue discovered during PFT and FPT from discovery through resolution and final acceptance. At minimum, it contains:

- **Deficiency number:** Unique identifier (Deficiency 37.1, 37.2, etc.)
- **System:** Which system (HVAC, Chilled Water, Electrical)
- **Description:** What the problem is (narrative, enough detail that someone reading it without being present understands what went wrong)
- **Severity:** Critical, Major, or Minor
- **Responsible party:** Sub responsible for correction
- **Target resolution date:** When the GC expects the correction to be complete
- **Resolution description:** How it was fixed (only filled in after correction)
- **Retest date:** When it was retested
- **Accepted by:** Commissioning agent or design professional signature/initials

### 4.2 Severity Classification

**Critical deficiency:** System cannot be operated safely, or operation would damage equipment. Examples: cooling system cannot reach design pressure (risk of compressor damage); electrical interlock fails (risk of personnel electrocution). Critical deficiencies must be resolved before the owner takes occupancy or uses the system.

**Major deficiency:** System is functional but operates outside design parameters. Examples: chilled water temperature drifts ±3°F instead of ±1°F as designed; fan outlet airflow is 10% below design. Major deficiencies are noted and tracked but do not prevent provisional occupancy. They must be resolved within an agreed timeframe (typically 5–10 business days).

**Minor deficiency:** Aesthetic or non-operational issue. Examples: a pressure gauge is not labeled; the equipment manual is not in the binder; the owner training checklist has incomplete signatures. Minor deficiencies are resolved before final payment but do not affect system operation.

### 4.3 Managing Deficiency Resolution from Subs

The GC's role is critical here. The GC tracks the deficiency log, ensures the responsible sub understands the issue and the deadline, verifies the resolution when the sub claims it's complete, and routes for retest. The commissioning agent or design professional typically approves the resolution.

**Typical sequence:**
1. Deficiency identified during FPT (e.g., "Chilled water supply temperature 48°F; design 45°F ± 1°F").
2. GC enters deficiency on log, severity "Major," responsible party "MEP Contractor — Chilled Water," target resolution 3 days.
3. GC calls the MEP contractor and explains: "Chilled water is running warm. This is a Major deficiency. We need it corrected by Thursday so we can retest."
4. MEP contractor troubleshoots: discovers the chiller is not fully loaded (it's not running hard enough). Adjusts the chiller setpoint down by 3°F.
5. MEP contractor notifies GC: "Chilled water deficiency corrected. Setpoint adjusted; current temperature 45.2°F."
6. GC schedules retest; commissioning agent or design engineer witnesses retest; confirms 45.2°F is within design tolerance.
7. GC updates deficiency log: "Resolution: Adjusted chiller setpoint per MEP contractor recommendation. Retest 3/15; result 45.2°F (within spec). Accepted by commissioning agent."

### 4.4 The Deficiency Closeout Meeting

When all PFT and FPT testing is complete and all deficiencies are resolved, the GC hosts a deficiency closeout meeting. Attendees: GC, mechanical/electrical contractors, commissioning agent (if applicable), design engineer (if required by contract), and owner operations staff.

Agenda:
1. Review the completed deficiency log.
2. Confirm all critical and major deficiencies are resolved and accepted.
3. Confirm all minor deficiencies are scheduled for closeout.
4. Obtain signatures on the deficiency log closure document.

This meeting is brief (30 minutes) but important—it's the formal acknowledgment that commissioning defects have been addressed.

---

## 5. Owner Training and Documentation

### 5.1 What Owner Training Must Cover

Owner training is hands-on instruction for the operations staff who will operate and maintain the system after the GC leaves. It covers:

**Design intent:** Why the system works the way it does. Example: "This chiller uses an economizer—when outside air temperature drops below 55°F, the chiller cycles off and we use free cooling from the outdoor air. This saves energy in shoulder seasons."

**Normal operating parameters:** Typical values the operators should expect to see. Example: "Chilled water supply should be 45°F ± 1°F during normal operation. Hot water supply should be 180°F ± 3°F. If you see temperatures outside these ranges, that's an alarm condition."

**Startup and shutdown sequences:** Step-by-step procedures the operators execute. Example: "To start the chilled water system: (1) open the isolation ball valves at the chiller inlet and outlet (red handles, turn counterclockwise 90°); (2) check the expansion tank pressure gauge—should be 20 psi; (3) turn the chiller keyswitch to 'on'; (4) wait 30 seconds for the low-pressure safety to clear; (5) observe the outlet thermometer—temperature should drop within 2 minutes; if not, check for alarm conditions."

**Alarm identification and response:** What each alarm means and what to do. Example: "If the chiller refrigerant-pressure alarm sounds, this means refrigerant pressure fell below 40 psi. Immediate action: (1) turn the chiller off; (2) call the service contractor; do not restart the chiller without checking with the contractor first."

**Emergency shutdown:** How to safely shut down the system in an emergency. Example: "In an emergency (fire, uncontrolled leakage), turn the red emergency stop button on the control panel (located next to the chiller). This closes all isolation valves and shuts down the chiller."

**Routine maintenance intervals:** How often, and by whom, the system needs maintenance. Example: "Chiller air-cooled condenser requires cleaning every 6 months (more frequently if operated in dusty environments). Filter replacement every 3 months or when pressure differential exceeds 0.5 inches of water column."

### 5.2 Training Format Options

**In-person hands-on (best):** The commissioning engineer or the mechanical contractor brings the system to steady-state operating condition, and the owner operators watch and take notes. The GC can pause and ask questions: "What if the setpoint drifts 2°F? How do you adjust it?" The operators hear the equipment running; they see the normal sounds and feel of the system.

**Video recording (good for ongoing reference):** A 15–30 minute video of the system starting up, running at normal conditions, and performing a controlled shutdown. Operators can replay it as a refresher. Video does not replace hands-on training but supplements it.

**Written O&M manuals (required, not sufficient alone):** The equipment manufacturer provides operation manuals. These are reference documents, not training. An operator who has never seen the equipment running will not understand the manual.

**Best practice:** In-person training for 2–4 hours (hands-on, system running, questions answered) supplemented by video recording and written O&M manuals.

### 5.3 Training Package Logistics

**Before training:**
- Identify which owner staff will attend (typically 2–4 operations personnel, possibly the facilities manager or owner PM).
- Confirm their availability and schedule the training session (should occur in the last week before the owner takes occupancy, when the systems are running and stable).
- Draft a training agenda by system: HVAC system training (1 hour), chilled water system (1 hour), emergency procedures (30 minutes), etc.
- Prepare handouts: system schematic showing key setpoints and parameters, alarm codes and responses, maintenance intervals and contact info for service contractors.

**During training:**
- Bring the systems to normal operating condition.
- Walk operators through the startup sequence.
- Explain normal operating parameters and show where to read them on the control panel.
- Trigger an alarm or simulate an abnormal condition ("The supply temperature just dropped to 40°F; what would you do?").
- Have operators practice the shutdown sequence.
- Distribute handouts and O&M manuals.

**After training:**
- Require each attendee to sign a training attendance form (name, date, systems covered, signature). This confirms they received training and can limit future warranty claims based on "operator error."
- Offer a follow-up session if an operator was unable to attend the primary training.

### 5.4 The Training Sign-Off

A training sign-off document should be part of the final commissioning package:

> "The undersigned operations personnel have received comprehensive training on the HVAC, chilled water, and hot water systems. We understand the normal operating parameters, startup/shutdown procedures, alarm responses, and emergency procedures. We acknowledge receipt of the Operations and Maintenance Manuals and have confirmed contact information for after-hours service support."

Signature lines for each operator. This protects the GC: if an operator later claims "I didn't know the system worked that way," the sign-off contradicts that claim.

---

## 6. Final Acceptance and Payment

### 6.1 The Final Commissioning Package

The commissioning package delivered to the owner at substantial completion includes:

- **Pre-functional test checklists:** All completed PFT forms, signed.
- **Functional performance test reports:** All FPT procedures executed, results recorded, pass/fail/conditional pass documented.
- **Deficiency log:** All deficiencies identified, resolved, and closed out, with sign-off by commissioning agent or design professional.
- **Training attendance records:** Signed forms confirming all operations staff received training.
- **As-built drawings:** Updated mechanical, electrical, and plumbing drawings showing final installed configuration.
- **Operations and maintenance manuals:** Original equipment manufacturer manuals, organized by system.
- **Warranty documentation:** Warranties from equipment manufacturers, warranty period start/end dates.
- **Attic stock schedule:** A schedule of spare parts, filters, belts, refrigerant, etc., that the owner should keep on hand (common for industrial facilities).
- **Commissioning Completion Certificate:** Issued by the commissioning agent (if applicable) or design professional, confirming all commissioning requirements have been satisfied.

### 6.2 Relationship Between Commissioning Acceptance and Final Payment

Most industrial and commercial contracts explicitly condition final retainage release on delivery of this package and sign-off by the design professional or owner. Contract language is typically strict:

> "Final payment shall not be due until the architect has issued a Commissioning Completion Certificate and the owner has received and accepted the complete commissioning package as described in Section 2.7."

A GC cannot collect retainage without this. The GC must proactively ensure all elements of the commissioning package are assembled and delivered before requesting final payment.

### 6.3 Partial Acceptance

Sometimes the owner takes occupancy before commissioning is completely finished. Example: a multi-building industrial facility completes commissioning on Building A but Building B systems are still being tested.

In this case, the contract may allow "partial acceptance." A partial acceptance document describes which systems/building areas have passed commissioning and are accepted, and which are deferred. Retainage is released proportionally:
- Building A passed commissioning (50% of contract): 50% of retainage released.
- Building B pending commissioning: 50% of retainage held until Building B commissioning is complete.

The partial acceptance document must clearly state the owner cannot hold the GC liable for "deemed acceptance" of deferred systems. Without this clause, the owner might later claim "you didn't tell me the chiller had a problem, so I accept it as-is" — even though commissioning wasn't complete.

### 6.4 First-Year Performance Period

Some contracts include a 12-month performance period after commissioning. During this period, the owner may request warranty service if a system fails or underperforms. The GC must understand what triggers a warranty call (defect in materials or workmanship) versus what triggers a change order (owner request or operating error).

Example:
- **Warranty call:** 6 months after commissioning, the chiller fails to reach design temperature. Investigation shows a refrigerant leak (defect in brazing). The GC covers the repair cost.
- **Change order, not warranty:** The owner requests that the chiller operate at 43°F instead of 45°F. This is an operational change, not a defect. The MEP contractor adjusts the setpoint; the GC charges a small service fee if the contract requires it.

Clear documentation of what's warranty-covered prevents disputes during the performance period.

---

## 7. ASHRAE and Regulatory Context

### 7.1 When ASHRAE Guideline 0 Applies

ASHRAE Guideline 0 is a voluntary industry standard, not code. However:
- Many architectural specifications require "commissioning per ASHRAE Guideline 0."
- Many large industrial and institutional owners require ASHRAE 0 commissioning.
- Insurance companies and lenders increasingly reference ASHRAE 0 as the industry standard of care.

When your contract says "commissioning shall be performed per ASHRAE Guideline 0," you are bound to follow the Guideline's framework. If your contract doesn't mention ASHRAE, you can still reference it as the industry standard if a dispute arises over whether commissioning was adequate.

### 7.2 LEED Commissioning Requirements

LEED-certified projects have commissioning requirements:
- **LEED EA Prerequisite 1 (Fundamental Commissioning):** Basic commissioning as described above (PFT, FPT, deficiency resolution, training, documentation).
- **LEED EA Credit 3 (Enhanced Commissioning):** Adds requirements for continuous commissioning testing over the first year of operation (the owner continues to monitor and optimize systems post-handoff).

If your project is LEED, the contract will specify these requirements. Enhanced Commissioning extends beyond the GC's typical retainage period but may impact the training and documentation deliverables.

### 7.3 California Title 24 Commissioning

California's Title 24 Part 6 (Energy Code) requires commissioning for commercial HVAC systems:
- All HVAC equipment must undergo functional performance testing before occupancy.
- Test results must be documented and submitted to the local building department.
- Commissioning documentation is part of the final building permit closeout.

This is enforced by the building department at final inspection. A GC that does not complete Title 24 commissioning cannot obtain a final occupancy permit—which means the owner cannot legally occupy the building. This requirement is absolute on any California commercial project.

---

## Case Study 1: The Premature System Startup

**Project context:**
- 145,000 sq ft industrial manufacturing facility, $18M construction contract.
- Primary mechanical system: 500-ton centrifugal chiller serving the main production floor.
- Contract includes 4-week commissioning phase with a commissioning agent.
- Scheduled commissioning: June 1–30; owner occupancy: July 1.

**The problem:**
May 28 (3 days before scheduled PFT): The owner's operations manager, impatient with a 2-week construction delay that was resolved by accelerating schedule work, decides to start up the chiller "for testing" without waiting for the GC's formal pre-functional test or the commissioning agent's approval.

The operations manager views this as a preliminary check: "I just want to see if it actually runs."

The chiller runs for 3 days without incident. On day 4, bearing noise increases; by day 5, the main bearing begins to smoke. A bearing failure occurs. Emergency shutdown and inspection reveal: the bearing lubrication system was not fully charged (part of the PFT is confirming lube oil level and flow), and oil starvation caused bearing damage. Repair cost: $85,000 (bearing replacement, internal inspection for secondary damage, lubrication system flushing and recharge).

**Who is responsible?**
The owner's operations manager operated the system outside the commissioning protocol. The contract clause states:

> "The chiller shall not be operated for any purpose until the commissioning agent has completed the pre-functional test, confirmed all components are installed correctly, and issued written authorization to proceed with startup testing."

**The GC's position:** "The owner's unauthorized startup voided the startup warranty. The bearing failure is due to the owner's violation of the commissioning protocol, specifically operating without PFT completion. The mechanical contractor's warranty covers defects in design and workmanship, not damage caused by unauthorized operation outside commissioning procedures."

**The owner's position:** "The bearing is a warranty item. If it was defective, you should have caught it during your commissioning."

**What documentation does the GC need?**
1. Written commissioning schedule showing PFT scheduled for June 1.
2. Email correspondence where the GC (or commissioning agent) specifically instructed the owner not to operate the chiller before PFT completion.
3. The commissioning protocol document (part of the contract documents) requiring PFT before startup.
4. Photographs or video of the control panel showing the chiller keyswitch was in "off" position before May 28 (proves it was not authorized to run).
5. Bearing failure analysis report from the bearing manufacturer or a bearing specialist, confirming the failure was consistent with lube-oil starvation (not a manufacturing defect).

**The GC's response:**
The GC immediately issues a written notice to the owner:

> "NOTICE OF UNAUTHORIZED EQUIPMENT OPERATION — We have been informed that the chiller was started and operated for 3 days without completing the required pre-functional test and without commissioning agent authorization. Per the contract commissioning protocol, equipment operation is prohibited until PFT completion. The bearing failure that occurred appears to be related to inadequate lubrication system verification at startup — verification that occurs during PFT. The GC does not warrant equipment damaged by unauthorized operation. We recommend the owner contact the mechanical contractor's insurance carrier to discuss coverage for this loss. The commissioning schedule resumes on June 1 per the original timeline."

**Actual outcome:**
The owner's insurance claim is filed against their general liability policy (for the losses they incurred on the rework and schedule delay). The insurance company denies the claim because the damage was caused by the owner's violation of the commissioning protocol, not by a defect in materials or workmanship. The owner absorbs the $85,000 cost.

**Key lessons:**
1. **Document the commissioning schedule early.** Email the owner and the commissioning agent before construction is complete: "Commissioning begins June 1. Equipment operation is prohibited before PFT completion."
2. **Control access to equipment.** If possible, the GC should lock out critical equipment (remove the chiller keyswitch, place a chain lock on the pump isolation valves) until PFT is scheduled. This prevents unauthorized startup.
3. **Include commissioning protocol in the contract conditions.** Make it a contractual obligation that equipment operation requires written PFT approval, not a suggested best practice.
4. **When unauthorized operation occurs, document it immediately.** Take photographs, note the date/time, and send a written notice to the owner. Do not attempt to fix the problem or reimburse the owner—document and escalate.

---

## Case Study 2: The Incomplete Training Package

**Project context:**
- 78,000 sq ft laboratory facility, $12M construction contract.
- Complex HVAC with multiple control zones, demand-controlled ventilation (DCV), and energy recovery ventilation (ERV).
- Owner is a research institution with in-house facilities staff (6 technicians).
- Commissioning includes 2 days of on-site owner training.

**The problem:**
Functional performance testing is complete; deficiencies are resolved. The GC schedules the owner training for the last Friday before occupancy (substantial completion is Monday).

Training attendees: 4 of the 6 facilities technicians. Two technicians are unavailable (one is on vacation; one is assigned to another building emergency).

Training covers: normal startup procedure, setpoint adjustments, alarm responses, and routine filter changes. The 4 attending technicians sign the training attendance form.

Two weeks post-occupancy: The facilities manager calls the GC with a problem: "The demand-controlled ventilation isn't working correctly. When occupancy is low, the CO2-based ventilation cutback isn't happening. We're running at full ventilation when no one's here. Can you come fix this?"

Investigation shows: the DCV setpoint was not explained during training (the two missing technicians who would have been responsible for DCV didn't attend training). The facilities manager adjusted the setpoint incorrectly to try to fix the problem, and now the system is not responding to CO2 changes.

The owner claims this is a deficiency that should have been caught during commissioning. The GC claims the training was completed as contracted, and the owner's operational error is not a warranty issue.

**Contract language:**
> "Training shall be provided to the owner's designated facilities personnel. The GC shall confirm attendees are the personnel responsible for the specific systems covered in training. Training sign-off indicates the attendees are competent to operate and maintain the systems."

**What does the training sign-off form say?**
The form used by the GC's commissioning contractor stated:
> "The undersigned personnel have received training on all systems and are competent to operate them."

It did not identify which person is responsible for which system. The signature line was generic; it did not require "DCV responsibilities assigned to [name]."

**The GC's exposure:**
The GC's training sign-off says the owner's personnel were trained. But the facilities manager claims the training was inadequate because the responsible person didn't attend. The GC's generic training form doesn't protect them.

**The owner's position:**
"Your training package was incomplete. The person responsible for DCV wasn't there. When we tried to operate the system post-occupancy, we discovered we didn't know how to use the DCV controls. That's your problem—you should have trained the right person."

**What should the GC have done?**
Before scheduling training:
1. Meet with the owner and ask: "Which staff member is responsible for each system?" (e.g., "Who manages the HVAC controls? Who manages the ERV system? Who manages the DCV?")
2. Confirm those specific individuals will attend training.
3. If a key person is unavailable, reschedule training rather than proceeding without them.
4. In the training sign-off form, identify each person by name and system: "John Smith (DCV controls), Mary Lee (General HVAC), etc."
5. Document that each person confirmed their understanding of their system's specific responsibilities.

**The GC's response to the owner's complaint:**
The GC can point to the training attendance form and note that the two missing technicians were not listed as responsible for DCV. However, the generic training form created ambiguity. The GC should:
1. Acknowledge: "We note that two facilities staff did not attend the training. We recommend a follow-up training session for the staff members responsible for DCV controls."
2. Offer a follow-up: Schedule a 1-hour DCV-focused training with the correct technicians at no cost.
3. Assist with correction: Have the commissioning agent review the DCV setpoint adjustment the owner made and confirm the system is reset correctly.

**Key lessons:**
1. **Confirm attendees before training.** Require the owner to identify which staff members are responsible for which systems, and confirm they will attend.
2. **Use a detailed training sign-off form.** Instead of generic signatures, require: "I, [name], confirm I have received training on [specific systems] and I am responsible for operating and maintaining [specific systems]."
3. **Reschedule if key staff are absent.** Don't complete training without the responsible operators present.
4. **Document system-specific responsibilities post-training.** After training, follow up with a written memo: "Per the training of June 14, John Smith is responsible for DCV controls. His responsibilities include monthly setpoint verification and annual DCV sensor calibration."
5. **Offer follow-up training for absences.** It's far cheaper to offer a free 1-hour follow-up training session than to dispute a warranty claim over inadequate training.

---

## Summary and Key Takeaways

Commissioning is the bridge between construction and operations. A GC that treats commissioning as a checkbox at the end of the project leaves money on the table (retainage held, disputes over warranty calls) and reputation damage (the operations team that discovers problems post-handoff becomes a critic, not a repeat-business advocate).

The discipline required is not complex, but it is systematic:

1. **Pre-functional testing** confirms installation is complete and correct.
2. **Functional performance testing** confirms operation meets design intent.
3. **Deficiency tracking** ensures every issue is documented, corrected, and retested.
4. **Owner training** prepares the operations team to run the system safely and effectively.
5. **Final acceptance** releases retainage and closes the project.

GCs who execute this discipline collect final payment on time, minimize warranty disputes, and build relationships with operations teams that lead to repeat business and referrals.

---

**Cross-reference:** Module 02 (Field Execution and System Startup) for general closeout procedures; Module 03 (Project Management and Safety) for industrial project planning context; Module 35 (Construction Insurance) for warranty and defect coverage; Module 29 (Dispute Resolution and Claims) for managing commissioning disputes.

**Key resources:**
- ASHRAE Guideline 0-2021: The Commissioning Process
- ASHRAE Guideline 1: HVAC&R Technical Requirements for Commissioning
- California Title 24 Part 6: Commissioning requirements for commercial HVAC
- LEED v4.1: Commissioning requirements for EA Prerequisite 1 and EA Credit 3
