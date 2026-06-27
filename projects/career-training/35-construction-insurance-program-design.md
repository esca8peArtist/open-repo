---
module: 35
title: "Construction Insurance Program Design: OCIP, Builder's Risk, and Professional Liability"
discipline: ["insurance", "risk-management", "contracts", "financial-management"]
audience: "GCs designing insurance programs and pricing OCIP projects"
status: reference
created: 2026-06-27
tags: [career-training, insurance, OCIP, CCIP, builder's-risk, professional-liability, wrap-up, certificate-of-insurance, coverage-gaps]
estimated-reading-time: 4 hours
---

# Construction Insurance Program Design: OCIP, Builder's Risk, and Professional Liability

> **Purpose.** Module 12 describes insurance types in a business-formation context. This module teaches the field-level insurance literacy GCs need to price projects correctly under wrap-up programs (OCIP/CCIP), read certificates of insurance and identify gaps, understand when builder's risk applies, and know when professional liability is required. A GC who doesn't understand this systematically underbids OCIP work or carries unintended coverage gaps.

> **Distinction from Module 12.** Module 12 covers business-formation insurance basics. This module covers project-specific insurance architecture and the financial impact of insurance decisions on project margin.

---

## Table of Contents

1. [The Insurance Stack on a Construction Project](#1-the-insurance-stack-on-a-construction-project)
2. [Reading and Verifying Certificates of Insurance](#2-reading-and-verifying-certificates-of-insurance)
3. [OCIP and CCIP Programs: Structure and Bidding Impact](#3-ocip-and-ccip-programs-structure-and-bidding-impact)
4. [Builder's Risk Coverage: Structure, Exclusions, and Claims](#4-builders-risk-coverage-structure-exclusions-and-claims)
5. [Professional Liability and Design-Build Risk](#5-professional-liability-and-design-build-risk)
6. [Umbrella and Excess Layers](#6-umbrella-and-excess-layers)
7. [Coverage Gaps and Risk Transfer Strategies](#7-coverage-gaps-and-risk-transfer-strategies)
8. [Insurance Program Audit Checklist](#8-insurance-program-audit-checklist)

---

## 0. Mental Model — Insurance Is Risk Transfer, Not Documentation

Insurance is often treated as a compliance checkbox: get a certificate, submit it to the owner, move on. In reality, insurance is the financial mechanism that determines who pays when something goes wrong. A GC with inadequate insurance or a GC who doesn't understand their insurance is accepting risk that should be transferred to a carrier — and accepting costs that should be borne by others.

The core principle: **Every risk should be borne by the party best positioned to manage it.** For a sub's workers' compensation exposure, the sub is best positioned — they control hiring and safety. For a GC's liability from a sub's defect, the GC typically carries general liability but may transfer a portion back to the sub through subcontract indemnification. The insurance structure should reflect this allocation.

The business impact:
- **Underbidding OCIP work:** Forgetting that subs' bids exclude insurance is a systematic margin leak.
- **Coverage gaps:** A $2M commercial project with an inadequate GL limits creates uninsurable risk.
- **Subcontract administration failure:** Not understanding what OCIP covers means you may require subs to carry duplicate coverage, creating cost friction.

---

## 1. The Insurance Stack on a Construction Project

### 1.1 The Five Core Insurance Types

A typical construction project has five layers of insurance, with different parties responsible for each:

| Type | Coverage | Primary Responsible Party | Typical Limits | Notes |
|---|---|---|---|---|
| **General Liability (GL)** | Bodily injury and property damage caused by the contractor's operations | GC (on residential); Owner/OCIP carrier (on OCIP projects) | $1M–$2M per occurrence; $2M–$4M aggregate | Primary coverage for on-site accidents and damage |
| **Workers' Compensation** | Injury or illness to employees on the job site | Each contractor/sub (own employees) | Statutory per state | No aggregate limit; required by law in all states |
| **Builder's Risk** | Damage to the structure under construction | Owner or GC (typically) | Full replacement value of project | Covers theft, vandalism, collapse, named-peril events |
| **Umbrella / Excess Liability** | Excess coverage above GL and other primary policies | GC or Owner | $1M–$5M+ | Only responds when primary policies are exhausted |
| **Professional Liability / E&O** | Errors and omissions in design or professional consulting services | Design professional or Design-Build GC | $1M–$5M | Only required when contractor is providing design services |

### 1.2 Who Pays for What

**Residential single-family project (typical):**
- GC carries GL (subcontract indemnification flows back to GC)
- Each sub carries workers' comp for their own crew
- Owner carries builder's risk (or requires GC to carry and charge back)
- GC carries umbrella policy (optional but standard)

**Commercial OCIP project (typical):**
- Owner / OCIP carrier carries GL (wrap-up policy replaces individual GC and sub GL)
- Each sub carries workers' comp for their own crew (unless project is CCIP — then wrap-up covers WC too)
- Owner / builder's risk carrier carries builder's risk
- Owner / wrap-up carrier carries umbrella above GL

**Design-build project (any size):**
- GC (as design-builder) carries professional liability / E&O
- Standard GL, builder's risk, workers' comp as above
- Professional liability only applies to the design portion of responsibility

### 1.3 Insurance as a Bid Component

On a standard project (not OCIP), insurance is a direct cost to the GC:
- **GL insurance:** Typically 0.5–1.5% of contract value; included in GC overhead
- **Workers' comp:** Paid by each sub; included in their labor rates
- **Builder's risk:** Typically charged to owner or GC (if charging back); common range $2,000–$10,000+
- **Umbrella:** Optional; typically $300–$800/year if project-specific

These costs are bundled into the GC's bid overhead and profit rates. On an OCIP project, by contrast, the GL component is removed from the GC and sub bids entirely — which changes the math fundamentally.

---

## 2. Reading and Verifying Certificates of Insurance

### 2.1 What a Certificate of Insurance Shows

A Certificate of Insurance (COI) is a one-page document issued by an insurance broker or carrier that confirms that a contractor has active coverage. It is **not** the actual insurance policy; it is a summary.

**Key elements on a COI:**

```
CERTIFICATE OF INSURANCE
[Insurance Broker Header]

PRODUCER: [Broker name and contact]
INSURED: [Contractor name and address]
EFFECTIVE DATE: [When coverage begins]
EXPIRATION DATE: [When coverage expires]

INSURANCE COMPANY(IES) AFFORDING COVERAGE:
Company | Type | Policy # | Limit | Deductible/SIR
[Insurance Co A] | General Liability | [POL-12345] | $1,000,000 per occurrence | $2,500
[Insurance Co B] | Workers' Comp | [POL-54321] | Statutory | $500
[Insurance Co C] | Auto Liability | [POL-99999] | $1,000,000 | $1,000

ADDITIONAL INSURED: [Owner name, if applicable]
- Certificate shows YES or NO and which policies include the owner as additional insured

WAIVER OF SUBROGATION: [YES / NO]

CANCELLATION NOTICE: This certificate is issued as a matter of information only 
and confers no rights upon the certificate holder. In the event of 
cancellation, the insurer will endeavor to provide 10 days' notice.
```

### 2.2 What to Check on Every COI

When a sub submits a COI, verify these elements:

**1. Expiration date** — Is coverage active for the entire project duration? A COI that expires mid-project is a problem.

**2. Policy limits** — Are they adequate for the scope? A plumbing sub with only $300,000 GL coverage on a $2M+ project is under-insured. Standard minimums: $1M per occurrence; $2M aggregate for standard GC; $2M/$4M for larger GCs.

**3. Additional insured endorsement** — Does the COI show the owner/GC as an additional insured on the GL policy? This is critical: if the owner is not an additional insured and a claim arises, the owner has no coverage and may pursue the GC. Language to look for: "Owner is additional insured per endorsement [CG-20-10]" or similar.

**4. Waiver of subrogation** — Does it say YES? A waiver of subrogation prevents the insurance carrier from suing a third party to recover losses. This is typically required by project contracts; if a sub's insurance has subrogation rights, the insurance may pursue the GC even though the sub was responsible.

**5. Deductible/SIR (Self-Insured Retention)** — Is it reasonable? A high deductible ($25,000+) means the sub is retaining significant risk; on a claim, the sub may not have the cash to pay the deductible and complete repairs. Typical acceptable deductible: $2,500–$10,000.

**6. Workers' comp coverage** — Is it listed? Coverage should show "Statutory" and the sub's state. Missing or expired workers' comp is a serious compliance issue.

### 2.3 Red Flags

| Red Flag | What It Means | Action |
|---|---|---|
| COI expires mid-project | Coverage will lapse before work is done | Require sub to obtain renewal or extended COI before expiration |
| Owner not listed as additional insured | Owner has no coverage if sub causes damage | Require endorsement or renegotiate contract terms |
| General Liability only $300K–500K | Insufficient coverage for larger projects | Require sub to increase limits or place additional insured umbrella |
| Workers' comp listed as "Not Applicable" | Sub may not be properly insured | Verify with state labor board; if sub is misclassifying, escalate |
| Deductible $25,000+ | Sub's financial capacity to pay deductible is unclear | Request financial verification or require lower deductible |
| Multiple insurers with gaps in coverage | Coverage may not be continuous across policies | Require consolidated COI and verification of aggregate across all policies |

### 2.4 Obtaining and Managing COIs

**Pre-construction:**
- Require all subs to submit a COI before they are approved.
- Maintain a COI register with expiration dates.

**During construction:**
- 30 days before a COI expires, issue a written notice to the sub: "Your insurance expires on [date]. Please submit a renewal COI by [30 days before expiration]."
- If a sub fails to submit a renewal, do not allow work to continue.

**Example COI tracking spreadsheet:**

| Subcontractor | GL Limit | WC Status | Expiration | Days Until Expiry | Renewal Received? | Additional Insured? |
|---|---|---|---|---|---|---|
| Framing Co. | $1M | Statutory | 9/15/2025 | 78 | No | Yes — CG-20-10 |
| Plumbing Sub | $1M | Statutory | 8/30/2025 | 63 | No | No — ACTION: Request |
| Electrical | $2M | Statutory | 10/1/2025 | 95 | Yes | Yes — CG-20-10 |

---

## 3. OCIP and CCIP Programs: Structure and Bidding Impact

### 3.1 What Is an OCIP?

An **OCIP (Owner Controlled Insurance Program)** is a comprehensive insurance policy carried by the owner that covers the entire project — the owner's work, the GC's work, and all subcontractors' work. It is "owner-controlled" because the owner procures and pays the insurance premium.

**Key difference from standard project:** On a standard project, each sub carries their own GL. On an OCIP project, the owner's insurance covers everyone.

**Who pays the premium:**
- Owner pays the wrap-up insurance premium upfront (typically 2–4% of project value).
- The premium is either included in the project budget or borne by the owner as a project cost outside the construction contract.

**Why owners choose OCIP:**
- **Economies of scale:** One consolidated policy is cheaper per sub than having 20 subs each carry individual GL policies.
- **Claim management:** The owner (through their risk manager or broker) controls claim handling and defense.
- **Reduced sub costs:** Subs don't have to carry GL on this project, so their bids are lower.

### 3.2 The OCIP Bidding Error: Failing to Remove GL from Sub Bids

This is the most common and costly GC error on OCIP projects.

**The problem:** A sub bids a job normally, including their standard GL insurance cost (typically 1–1.5% of their labor). The GC forgets or fails to communicate that the OCIP covers GL, so the sub leaves the insurance cost in their bid. The GC accepts the sub's bid and unknowingly pays twice: once through the OCIP premium and again in the sub's labor rate.

**Example:**
- Electrical sub normally bids electrical rough-in at $85,000 labor + $1,500 GL insurance = $86,500.
- Project has an OCIP that covers all GL (including electrical).
- Sub should bid $85,000 only (no GL cost).
- If GC accepts the $86,500 bid, the GC is paying $1,500 for insurance that's already paid by the OCIP.
- On a $5M project with 15 trades, this error could cost $20,000–$30,000 in duplicate insurance.

**Prevention protocol:**

1. **Notify all subs in the bid package:** "This project is insured under an OCIP. All subcontractors are covered by the owner's general liability policy. Do not include general liability insurance costs in your bid. Your bid should exclude GL."

2. **Pre-bid meeting:** Walk through the OCIP document (or at least the summary) with all subs and explain what's covered. Field questions.

3. **Bid review:** When reviewing sub bids, specifically check the insurance line item. If a sub included GL, call them: "I see you included $X for GL. The OCIP covers this, so please revise your bid to exclude it."

4. **Contract language:** The subcontract should explicitly state: "Contractor shall carry no general liability insurance on this project; all GL coverage is provided under the owner's OCIP per policy [#]. Contractor certifies that GL insurance costs are excluded from this quote."

### 3.3 CCIP — Workers' Compensation Wrap-Up

A **CCIP (Contractor Controlled Insurance Program)** is similar to an OCIP but covers workers' compensation in addition to general liability. The GC (rather than the owner) procures the wrap-up policy.

**When CCIP is used:**
- Projects with high injury risk (heavy concrete, steel, complex MEP).
- Projects where the owner wants to shift insurance procurement to the GC.
- Projects where the GC's insurance broker can provide better pricing than individual sub policies.

**Bidding implications for CCIP:**
- Subs should exclude both GL and WC insurance costs from their bids.
- The GC pays the CCIP premium and factor it into overhead.

**Cost savings from CCIP:**
- Individual sub workers' comp premiums: typically 15–35% of payroll (varies by trade and loss history).
- Consolidated CCIP coverage: typically 8–18% of total payroll (due to economy of scale).
- Potential savings: 5–20% of total labor cost across all subs — substantial on large projects.

### 3.4 Verifying OCIP/CCIP Coverage for Your Scope

Before submitting a bid on an OCIP project, or before allowing a sub to work on a CCIP project, verify exactly what the wrap-up covers:

**Questions to ask:**
1. Does the wrap-up include the GC as the insured, or only the subs?
2. What are the coverage limits per occurrence and aggregate?
3. Are there coverage exclusions (e.g., professional liability, equipment breakdown, etc.)?
4. What is the deductible per claim?
5. Does the policy include contractual liability (coverage for indemnification obligations)?
6. If the GC assumes some risk (e.g., negligence), does the wrap-up cover that exposure?

**Example scenario:** A GC is bidding a commercial fit-out on an OCIP. The OCIP covers GL for all parties, but the certificate notes "excludes professional liability." If the GC is providing any design services (even coordination and layout), the GC must carry a separate E&O policy to cover that exposure. Failure to do so leaves the GC personally liable.

### 3.5 Premium Allocation and Bid Accounting on OCIP Projects

On an OCIP project, the owner pays the wrap-up insurance premium. This cost is typically **2–4% of the project contract value** and is either included in the construction budget or borne by the owner as a separate cost. The GC's bid should reflect this removal of insurance costs.

**Typical bid structure on a $10M commercial OCIP project:**

Standard project (no OCIP):
- Labor: $5M
- Materials: $3M
- Subcontracts: $1.5M
- GC overhead (including GL insurance at 1.2%): $400,000 ($120,000 GL + $280,000 other)
- GC profit (5%): $500,000
- **Total contract value: $10.4M**

OCIP project (same scope, but GC does not carry GL):
- Labor: $5M
- Materials: $3M
- Subcontracts: $1.5M (subs do not include GL)
- GC overhead (excluding GL): $280,000 (GL insurance is $0; other overhead $280,000)
- GC profit (5% of adjusted base): $427,500
- **Total contract value: $10.207M** (approximately $200K less than standard project, reflecting the removal of GL costs from GC and subs)

Owner pays OCIP premium separately: **$300,000–$400,000** (3–4% of $10M).

**Critical distinction for GC economics:**
- On a standard project, the GC includes GL insurance cost in the overhead rate.
- On an OCIP project, the GC should reduce the overhead rate to remove GL, allowing the bid to be lower.
- The owner pays the OCIP premium upfront (not through the construction contract).
- The GC's profit margin should be the same percentage-wise, but the absolute profit is lower because the project cost is lower (no GL costs).

**Bid accounting error to avoid:** Some GCs reduce their overhead rate for OCIP projects to remain "competitive" (trying to undercut other bidders). This is appropriate IF the insurance cost has been removed from subs. However, if subs still include GL costs, the GC is not capturing the cost removal, and the bid is too low.

### 3.6 GC-Provided Insurance Under OCIP (Rare, But Possible)

In some cases, the GC may be required to procure and pay for OCIP insurance on behalf of the owner (unusual, but occurs in design-build or fast-track projects where time is short and the owner trusts the GC to manage insurance procurement).

**If the GC is procuring OCIP:**
1. GC obtains a quote from the wrap-up broker (typically 2–4% of construction cost).
2. GC adds this cost to the bid as a direct cost line item (not part of overhead/profit).
3. GC recovers the premium cost as a pass-through; profit is on the construction work, not the insurance.
4. Owner reimburses the GC for the premium cost from the construction contract draws.

**GC risk on OCIP procurement:**
- If premium increases mid-project due to claims (in some OCIP structures, the premium can adjust if claims exceed projections), the GC may absorb the increase.
- Therefore, GCs should avoid procuring OCIP; let the owner procure and manage it.

### 3.7 Requesting OCIP Documentation Before Bidding

**Minimum documentation to request from the owner/wrap-up broker before bidding:**
1. Certificate of Insurance for the OCIP policy.
2. Copy of the OCIP policy declarations (first 2–3 pages showing coverage limits, deductibles, exclusions).
3. Written confirmation of what is covered (GL, WC if CCIP, umbrella, etc.).
4. Written confirmation that the GC is named as an insured under the OCIP.
5. Confirmation that subs are covered under the OCIP (and therefore should exclude GL from their bids).

**Request in writing:** "Before submitting a bid, we require confirmation that [project name] is covered under a wrap-up insurance program. Please provide (a) Certificate of Insurance, (b) policy declarations showing coverage limits and exclusions, and (c) written confirmation that our company and all subcontractors are insured under the wrap-up. Once we have confirmed the coverage details, we will prepare and submit our bid accordingly."

This protects the GC: if coverage is unclear, the GC can address it before bidding, rather than discovering a coverage gap after contract signature.

---

## 4. Builder's Risk Coverage: Structure, Exclusions, and Claims

### 4.1 What Builder's Risk Covers

**Builder's Risk** (also called "Builders' All-Risk" or BAR) is property insurance covering the building under construction. It covers the structure, installed equipment, and materials on site against damage from specified causes.

**Typical covered perils:**
- Fire and lightning
- Wind and hail
- Explosions
- Theft and vandalism
- Collapse from weight of ice/snow or structural failure
- Water damage (from named perils, not from poor drainage or hydrostatic pressure)
- Aircraft damage
- Riots and civil unrest

**NOT covered:**
- Normal wear and tear
- Poor craftsmanship or defects in workmanship
- Water damage from water ponding, poor grading, inadequate drainage (excludes flood, hydrostatic, seepage)
- Earth movement and earthquakes (separate coverage required in high-risk zones)
- War, terrorism, radiation
- Consequential losses (business interruption, lost revenue)

### 4.2 Builder's Risk Deductible and Valuation

**Deductible structure:**
- Typical deductible: $5,000–$25,000 per claim.
- Wind/hail deductible: Often separate and higher (e.g., 5% of coverage, or $25,000, whichever is greater).
- Earthquake deductible (if coverage is added): Typically 15–25% of coverage.

**Valuation — agreed value vs. replacement cost:**

Most builder's risk policies use "Agreed Value" — the insurer agrees upfront on the value of the project and pays that amount for a total loss, no coinsurance penalty. This requires an accurate valuation at the time of binding.

**Example:** Project contract value is $500,000. The agreed value of the structure under construction is estimated at $350,000 (value of labor and materials in place, excluding profit and overhead). Agreed value is set at $350,000. If a fire destroys the structure when it's 60% complete, the claim value is approximately $210,000 (60% × $350,000), and that's what the policy pays.

**GC responsibility:** Confirm with the owner or their insurance broker that the agreed value is adequate. An under-valued agreed value means under-insurance and partial recovery on a loss.

### 4.3 Coverage Triggers and Exclusions by Phase

**Pre-construction (materials stored on site):**
- Materials delivered to the job site before construction begins are typically covered under builder's risk, but only if they are properly stored and inventoried.
- High-value items (MEP equipment, appliances, structural steel) should be listed separately on the policy.

**During construction (work in progress):**
- Completed work (concrete slab, framed structure, rough MEP) is covered.
- Work must be reasonably secured (open buildings with no security are a risk; some policies exclude open buildings or require 24/7 security).

**Phase-out coverage (near completion):**
- Most policies terminate builder's risk coverage at substantial completion, at which point the owner's standard property insurance takes over.
- Clarify the exact date with the owner — if there is a gap (substantial completion 8/31, but occupancy not until 9/15), coverage must be extended.

### 4.4 Water and Flooding Exclusions — Common Claims Issues

Water damage claims are the most frequent builder's risk disputes. Most policies strictly limit water damage coverage:

**Covered:**
- Damage from a named peril that allows water ingress (e.g., roof damage from wind allows rain to enter).
- Sudden, accidental water damage.

**NOT covered:**
- Water ponding from poor site drainage or grading.
- Water seeping through inadequate waterproofing or flashings (excludes workmanship failure).
- Hydrostatic pressure (water pushing in from below).
- Flood (unless separate flood coverage is added).

**Example dispute:** Heavy rain during construction causes water to pond on the slab and saturate the underslab insulation. The insulation is damaged. Builder's risk denies the claim: "Water ponding is excluded; it's a result of inadequate site drainage, not a named peril." The GC has no recourse unless they purchased separate coverage.

**Best practice:** On projects in climates with heavy rain or on sites with poor drainage, require the owner to:
1. Verify that builder's risk includes "water damage from within the structure" (non-standard endorsement).
2. Consider adding separate coverage for water seepage or hydrostatic pressure.
3. Implement robust site drainage and monitoring during construction.

### 4.5 Filing a Builder's Risk Claim

When a loss occurs (theft, wind damage, fire, etc.):

1. **Mitigate damage immediately** — cover open areas, prevent further water entry, secure the site.
2. **Notify the insurer within 24–48 hours** — delay can be grounds for denial.
3. **Document the loss** — photos of the damage, inventory of damaged items (if theft), weather records (if wind/rain).
4. **Gather estimates** — obtain repair estimates from trades for damaged work.
5. **Submit claim** — provide insurer with notice, documentation, and repair estimates.
6. **Expect adjustment** — the insurer will send an adjuster to inspect the damage and verify the claim amount.
7. **Proceed with repairs** — do not begin repairs without insurer approval unless emergency conditions require immediate action.

**GC role:** Typically, the owner files the builder's risk claim, not the GC. However, the GC should coordinate: provide documentation, assist the adjuster, and keep the owner informed of repair timelines.

---

## 5. Professional Liability and Design-Build Risk

### 5.1 When Professional Liability Is Required

Professional Liability insurance (also called "Errors & Omissions" or E&O) covers losses arising from negligence in the performance of professional services — primarily design services.

**Professional liability is required when the contractor is performing design work:**
- Design-build projects (GC provides the design as well as construction).
- Design-assist projects (GC advises on design, contributes to layout, or coordinates design).
- Projects where the GC is responsible for structural or MEP coordination that constitutes engineering services.

**Professional liability is NOT required when:**
- The GC is building from complete architect/engineer-prepared drawings (traditional design-bid-build).
- The GC is coordinating trades but not designing or engineering systems.

**The risk:** A GC who provides design services without professional liability insurance is accepting unlimited personal liability for design errors. Example: A design-build GC provides structural layout drawings. A slab is poured incorrectly per the layout, and the structure settles. The owner sues for $500,000 in damages. Without E&O, the GC is personally liable.

### 5.2 Coverage Limits and Cost

**Typical professional liability limits on residential design-build projects:** $1M–$2M per claim; $2M–$5M aggregate.

**Commercial projects:** $2M–$5M per claim; $5M–$10M aggregate.

**Cost:** Professional liability is expensive — typically $2,000–$8,000/year for design-build GCs, depending on project volume and loss history.

**Tax treatment:** E&O is a legitimate business expense; it is deductible.

### 5.3 Design Coordination vs. Design-Build Risk

A subtle distinction that affects insurance requirements:

**Design coordination (typically no E&O required):**
- Contractor reviews design drawings for constructability.
- Contractor advises architect on sequencing or feasibility.
- Contractor does not modify, approve, or stamp drawings.
- Architect retains responsibility for design accuracy.

**Design-build (E&O required):**
- Contractor develops design or design standards (structural layout, MEP routing, selections).
- Contractor stamps or certifies design drawings (or causes them to be stamped by an engineer).
- Contractor is responsible if design contains errors.

**Mixed (typically requires E&O):**
- Contractor provides design-assist for specific systems (structural, HVAC layout) but not full design.
- Contractor is responsible for the accuracy of the systems they designed.

**Example:** A residential GC is bidding a design-build project. The GC will provide architectural design (floor plans, elevations, selections) and MEP coordination. The owner's structural engineer will design the structure. In this case:
- The GC should carry professional liability for the architectural/MEP design they provide.
- The structural engineer carries professional liability for structural design.

### 5.4 Professional Liability Claims and Coverage Gaps

Professional liability claims are typically filed after project completion, sometimes years later. Claims often involve:
- Design defects (structural, water infiltration, code non-compliance).
- Failure to identify or coordinate design conflicts.
- Failure to obtain required approvals or permits.

**Coverage limits must be adequate to the project value.** A $3M design-build residential project with only $1M professional liability coverage is under-insured. A $2M claim would exceed the limit, leaving the GC liable for the excess.

**Common claim scenario:**
- Design-build GC provides structural layout; slab is poured per plan.
- Post-occupancy, the slab settles and cracks (design was under-engineered for soil conditions).
- Owner files a professional liability claim against the GC.
- E&O policy responds and covers defense and settlement, up to the policy limit.
- Without E&O, the GC is defending at personal cost and paying any judgment.

---

## 6. Umbrella and Excess Layers

### 6.1 What Umbrella/Excess Coverage Is

An **umbrella policy** (or excess liability policy) is high-limit coverage that sits above primary policies (GL, auto, workers' comp, professional liability) and only responds when a claim exceeds the primary policy limits.

**Example:**
- GC has $1M per occurrence GL.
- Claim arises: $2.5M in damages.
- GL pays $1M.
- Umbrella policy kicks in and pays the next $1M (assuming $1M umbrella limit).
- GC is still liable for $500,000.

**Umbrella limits:** $1M–$5M+ depending on project size and risk profile.

**Cost:** Relatively inexpensive — typically $300–$1,500/year for a $1M umbrella on top of a $1M GL.

### 6.2 When Umbrella Is Critical

Umbrella is essential on:
- Large commercial projects ($5M+) where a single claim could exceed GL limits.
- Projects with high exposure (demolition, structural work, hazardous material handling).
- Design-build projects where design liability could trigger large claims.
- Any project where the GC is accepting indemnification for other parties' negligence.

Umbrella is optional (but recommended) on:
- Residential projects ($200K–$500K) where GL limits are likely sufficient.
- Projects where the GC is minimizing scope and not accepting design responsibility.

### 6.3 Comparing Umbrella Policies

When shopping for umbrella coverage, compare:

| Feature | Importance | What to Look For |
|---|---|---|
| **Drop-down coverage** | High | Does the umbrella respond if primary GL lapses or is canceled? (Drop-down feature fills the gap.) |
| **Duty to defend** | High | Does the umbrella carrier defend the claim, or only reimburse after primary is exhausted? |
| **Sub-limits** | Medium | Are there sub-limits on specific coverages (e.g., pollution, contractual liability)? |
| **Per-claim vs. aggregate** | High | Is there a per-claim limit and an annual aggregate, or unlimited aggregate above the GL? |
| **Exclusions** | High | Does the policy exclude coverage that the GL covers (would create gaps)? |

---

## 7. Coverage Gaps and Risk Transfer Strategies

### 7.1 Common Coverage Gaps

| Gap | Consequence | Solution |
|---|---|---|
| **Contractual liability not covered** | GC assumes indemnification in contracts but insurance won't cover it | Ensure GL policy includes contractual liability endorsement (CG-21-86) |
| **No pollution coverage** | Fuel spill or dust causes third-party damage; not covered | Add pollution liability rider if site has hazmat risk |
| **Inadequate builder's risk valuation** | Total loss yields under-insurance; partial recovery | Confirm agreed value is set to 100% of project value |
| **Umbrella has exclusions GL covers** | A claim falls through the gap | Ensure umbrella and GL are seamless (no conflicting exclusions) |
| **Professional liability limit too low** | E&O claim exceeds policy limit | Match E&O limit to project value |
| **No wrap-up confirmation on OCIP project** | GC believes GL is covered but policy has gaps | Obtain copy of OCIP certificate and limits before bidding |

### 7.2 Contractual Liability and Indemnification

**Contractual liability** is coverage for liability assumed under a contract. Most GC contracts require the GC to indemnify (cover losses caused by) the owner. Without contractual liability coverage, the GC cannot transfer this obligation to insurance.

**Sample contract language requiring indemnification:**

> "Contractor shall indemnify, defend, and hold harmless Owner from and against all claims, damages, and costs arising out of or resulting from Contractor's performance of the Work, including claims arising from Contractor's negligence."

This language means the GC is legally obligated to pay the owner's losses if the GC (or a GC subcontractor) causes damage. Contractual liability coverage reimburses the GC for this obligation.

**Most GL policies include contractual liability by default, but verify:** Ask the GC's broker to confirm that the GL policy includes endorsement CG-21-86 (contractual liability for indemnified contracts).

### 7.3 Risk Transfer Through Subcontracts

The GC can shift certain risks back to subs through subcontract language:

**Example subcontract indemnification clause:**

> "Subcontractor shall indemnify Contractor against all claims, damages, and costs arising out of Subcontractor's performance of the Work or Subcontractor's negligence, except to the extent the claim is caused solely by Contractor's negligence."

This obligates the sub to carry insurance (GL and workers' comp) and to indemnify the GC for losses caused by the sub. The sub's insurance backs up this indemnification.

**Best practice:** Ensure all subcontracts include:
1. Indemnification clause (sub indemnifies GC).
2. Insurance requirement (sub carries GL and WC with GC as additional insured on GL).
3. Waiver of subrogation (sub's insurer won't sue GC).

This creates a clear chain: sub causes damage → GC covered under sub's insurance → if claim is large, GC's umbrella responds.

---

## 8. Insurance Program Audit Checklist

Use this checklist to verify your project's insurance program before construction begins:

**General Liability:**
- [ ] GC has GL coverage for the project (or project is under OCIP/CCIP).
- [ ] GL limits are adequate for project value (minimum $1M per occurrence; $2M aggregate for residential; higher for commercial).
- [ ] GL policy includes contractual liability (endorsement CG-21-86 or equivalent).
- [ ] GL policy includes waiver of subrogation.
- [ ] All subs carry GL with GC as additional insured (endorsement CG-20-10 or 20-11).
- [ ] GL policy is active and will remain active through project completion + cleanup period.

**Builder's Risk:**
- [ ] Owner has builder's risk coverage (or GC is required to carry and charge back).
- [ ] Agreed value is set to 100% of estimated project value (structure + installed materials).
- [ ] Coverage includes named perils (fire, wind, theft, vandalism, collapse).
- [ ] Deductible is reasonable and understood ($5K–$25K typical).
- [ ] Builder's risk will be in force through substantial completion (date confirmed).
- [ ] Water damage exclusions are understood; additional coverage obtained if site has drainage risk.

**Workers' Compensation:**
- [ ] All subs carrying workers' comp for their own employees.
- [ ] COI from each sub shows statutory WC coverage active.
- [ ] Workers' comp COI coverage extends through project completion.
- [ ] GC carries WC for any direct GC employees on site.

**Professional Liability / E&O:**
- [ ] If project is design-build or design-assist: GC has professional liability/E&O.
- [ ] E&O limits are adequate to project value (minimum $1M–$2M residential; $2M–$5M commercial).
- [ ] E&O coverage includes design services (confirm coverage scope with broker).

**Umbrella:**
- [ ] If project value > $2M or has high-risk scope: GC has umbrella coverage ($1M–$5M).
- [ ] Umbrella has drop-down coverage (responds if primary GL lapses).
- [ ] Umbrella covers same perils as primary policies (no gap coverage).

**OCIP/CCIP (if applicable):**
- [ ] Copy of OCIP/CCIP certificate obtained and reviewed.
- [ ] OCIP/CCIP coverage limits adequate for project scope.
- [ ] OCIP/CCIP coverage for GC and all subs confirmed.
- [ ] All subs notified that GL/WC excluded from their bids (OCIP/CCIP covers).
- [ ] Sub bids reviewed to verify GL and WC costs removed.
- [ ] Certificate of Insurance from wrap-up carrier obtained.

**General Verification:**
- [ ] Master insurance spreadsheet created listing all policies, limits, expiration dates.
- [ ] All COIs received from subs; maintained in project file.
- [ ] Insurance expiration dates 30+ days out flagged for renewal follow-up.
- [ ] Insurance broker (GC's) briefed on project scope and risk profile.
- [ ] Owner notified of any coverage gaps or limitations.

---

---

## Case Study 1: OCIP Bidding Disaster — GC Pays Insurance Twice

**Project context:**
- $8.5M commercial office building renovation, 18-month schedule.
- Owner established an OCIP (Owner Controlled Insurance Program) covering all GL costs.
- Owner contracted with a wrap-up broker who procured a $200,000 annual premium for all general contractors and subcontractors' GL coverage.

**The GC's error:**
The GC bid the project using their standard overhead structure, which includes a 1.2% GL insurance cost premium baked into all labor rates and material markup.

- Electrical sub normally bid at $380,000 labor rate, which includes $5,700 in GL insurance costs.
- Mechanical sub normally bid at $520,000 labor rate, which includes $7,800 in GL insurance costs.
- Framing subcontractor normally bid $420,000 labor, which includes $6,300 in GL insurance costs.
- [15 major subs total]
- **Total GL costs baked into sub bids: ~$95,000.**

The GC failed to communicate to subs that the OCIP was covering GL. Subs submitted normal bids including their standard GL costs.

**What the GC received:**
- Electrical: $385,700 (labor $380,000 + GL $5,700)
- Mechanical: $527,800 (labor $520,000 + GL $7,800)
- [14 other subs, all including GL costs]
- **Total sub costs: $8,455,000 (including ~$95,000 of unnecessary GL cost)**

**What the GC should have paid:**
- Electrical: $380,000 (GL covered by OCIP)
- Mechanical: $520,000 (GL covered by OCIP)
- [Other subs at base labor rates, excluding GL]
- **Total sub costs: $8,360,000 (~$95,000 less)**

**The bottom line:**
- Owner paid the OCIP premium: $200,000
- GC paid $95,000 to subs for GL coverage that the OCIP already covered
- **Total cost to cover GL: $295,000 (instead of $200,000)**
- **GC's loss: $95,000 in margin**

On an $8.5M project, a $95,000 loss is approximately 1.1% of contract value — enough to swing a project from profitable to marginally profitable or break-even.

**How this happened:**
1. The GC received the OCIP certificate but did not carefully review it or communicate coverage details to subs.
2. The GC's standard bid process was to request bids from subs without specifically instructing them to exclude GL costs.
3. The GC's estimator did not create a "GL exclusion" instruction to accompany the bid request.
4. Subs submitted standard bids without asking whether GL was covered.

**How to prevent this:**
1. **Pre-bid meeting:** Before bidding on OCIP projects, hold a pre-bid meeting with all subs. Walk through the OCIP coverage and explicitly state: "This project is covered under an OCIP. All general liability insurance costs are covered by the owner's wrap-up policy. Do not include GL in your bid."
2. **Bid package instruction:** Include a written instruction in the bid package: "Contractor shall carry no general liability insurance on this project. All GL coverage is provided under the owner's OCIP per policy [#]. Contractor certifies that GL insurance costs are EXCLUDED from this quote."
3. **Bid review checklist:** When reviewing sub bids, specifically check for GL costs. If a sub included GL, call them and require a revised bid.
4. **Subcontract language:** The subcontract must state: "Contractor shall not carry general liability insurance on this project. All GL coverage is provided by the owner's OCIP. Contractor's price is calculated assuming no GL insurance cost."

**Outcome:**
The GC absorbed the $95,000 loss. The project was otherwise successful, but the margin hit meant the GC earned only 2% net profit on $8.5M in contract value — a below-market return.

**Lesson learned:**
OCIP projects require explicit communication with subs about GL exclusion. A single sentence added to the bid package ("GL excluded — OCIP covers") would have prevented this $95,000 loss.

---

## Case Study 2: Coverage Gap and the Uninsured Subcontractor — Builder's Risk Claim Denial

**Project context:**
- $1.2M residential new build, 5-month schedule.
- Owner carries builder's risk policy with $1.2M agreed value.
- Project in progress, approximately 60% complete (roofing on, windows installed, drywall in progress).

**The incident:**
Heavy rain event (2-inch rainfall in 4 hours) occurs during the drywall phase. Due to incomplete roof flashings and open window openings (not yet fully sealed), water ingresses into the second-floor master bedroom and guest room, saturating drywall, insulation, and subflooring.

Estimated water damage repair cost: $45,000 (replace saturated materials, dry and remediate mold risk).

**Builder's risk claim attempt:**
GC files claim with owner's builder's risk carrier, providing photos and repair estimates. Carrier's adjuster inspects and issues a coverage determination: **"Claim DENIED — water infiltration resulting from incomplete construction / poor workmanship is not a covered peril under the policy. The policy excludes water damage arising from defects in construction or inadequate waterproofing."**

Carrier position: The water ingress was not from a sudden, accidental named peril (like a falling tree branch damaging the roof); it was from incomplete construction (roof flashings not complete; windows not fully sealed).

**Dispute:**
GC contends: "The window sealant was scheduled for week 3 of the drywall phase. The rain occurred during week 1 of drywall. The rain was a named peril (unexpected weather); we were not yet at the stage of final waterproofing."

Carrier contends: "Incomplete roof and window perimeters during this phase of construction is a normal risk of the project. Builder's risk covers sudden, accidental damage from external causes — not damage from the natural progression of incomplete construction during active trades."

**Legal position:**
The insurance contract language is clear: "Builder's risk covers damage to the insured property from external named perils (fire, wind, theft, vandalism, etc.) not arising from defects in workmanship or incomplete construction."

The carrier's interpretation is within the policy terms. The GC has no recovery path through builder's risk.

**Cost allocation:**
- GC must remediate the damage (contract obligation to deliver completed work).
- GC must absorb the $45,000 repair cost.
- GC has no insurance recovery.
- GC could potentially backcharge the roofing sub (if the flashing delay was sub-caused) or the window sub, but this requires proving the delay was the sub's responsibility, not GC schedule management.

**Prevention:**
1. **Understand builder's risk exclusions.** GC should have understood that water damage from incomplete construction is commonly excluded.
2. **Implement site protection during active phases.** Temporary coverings on open window frames and incomplete roof penetrations during heavy rain forecasts prevent water ingress.
3. **Advance builder's risk coverage if weather risk is high.** In climates with frequent heavy rain, GC should request that owner add "water damage from inclement weather during construction" to the builder's risk policy (non-standard endorsement, may increase premium).
4. **Coordinate weather and construction sequencing.** The GC should have scheduled roofing flashing completion and window sealing before anticipated rain events, or implemented temporary weather protection.

**Lesson learned:**
Builder's risk is not a catch-all for weather damage. Water damage is the most litigated coverage in builder's risk, and most policies strictly exclude water damage from incomplete work. GCs must either (a) understand the exclusions and plan around them, or (b) request coverage endorsements before construction starts.

---

## Case Study 3: Professional Liability E&O Claim — Design-Build Structural Defect

**Project context:**
- $2.8M design-build residential project (6-unit townhome complex).
- GC provided architectural design, structural layout, and MEP coordination.
- Owner's structural engineer designed the load-bearing walls and foundation system.
- GC did not carry professional liability / E&O insurance.

**The defect:**
Eighteen months after substantial completion, one of the townhomes (unit 4) begins to show visible cracks in the living room wall and the master bedroom window frame. The owner hires a structural engineer to investigate.

Engineer's report: "The structure is settling unevenly. The settlement is consistent with inadequate foundation design or site preparation. The adjacent units are not settling, suggesting this is unit-specific. Probable cause: inadequate compaction of soil beneath the unit 4 foundation, or design not accounting for a non-uniform soils condition at unit 4 location."

The owner demands that the GC repair the structure. The GC's response: "This is a foundation/structural design issue. We followed the structural engineer's drawings. The engineer is responsible."

The owner is not satisfied and retains a construction defect attorney. The attorney sends a demand letter: "We believe the GC's failure to adequately investigate and prepare the soil at unit 4 location (which is a GC responsibility, not engineering responsibility) resulted in the settling. We are claiming $180,000 in structural repair costs plus $50,000 in diminished value of the property."

**Litigation begins:**
The owner files a lawsuit against the GC for breach of warranty and negligence in construction. The GC's insurance broker is contacted. The GC's GL policy does not cover "defects in design" — that's what professional liability/E&O covers. The GL policy denies coverage.

The GC now must defend itself at personal cost:
- Legal fees for attorney: $30,000–$50,000
- Expert structural engineer for defense: $15,000–$25,000
- Depositions and discovery: $10,000+
- Potential settlement or judgment: $180,000–$230,000 (depending on settlement negotiations or trial outcome)

**Total exposure: $235,000–$305,000, entirely at the GC's cost, because the GC did not carry professional liability insurance.**

**Professional liability insurance would have:**
- Provided a defense (attorney paid by E&O carrier)
- Covered the claim up to the policy limit (typically $1M–$2M on a $2.8M project)
- Covered legal fees and expert costs

**Cost of E&O insurance the GC should have carried:**
- Annual premium for a design-build contractor: $3,000–$6,000 per year
- Duration of project: 1 year (design) + 1 year (construction) = 2 years
- Total E&O cost: $6,000–$12,000

**Lesson learned:**
A GC providing any design services (including layout and structural coordination) must carry professional liability/E&O insurance. The cost of insurance ($6,000–$12,000) is minimal compared to the exposure ($235,000–$305,000+). This is a non-negotiable risk transfer requirement on design-build projects.

---

## Case Study 4: Umbrella Policy Saves the Day — Catastrophic Claim Exceeds GL Limit

**Project context:**
- $1.8M commercial interior renovation, 16-week schedule.
- GC carries:
  - General Liability: $1M per occurrence; $2M aggregate
  - Umbrella: $2M per claim (GC maintained this policy despite it not being contractually required)

**The incident:**
During the drywall and finish phase, an electrical short in a HVAC junction box (not in the scope of work, but existing building system) causes a fire in the wall cavity. The fire is contained to one section of the building, but requires:
- Complete replacement of interior finishes (drywall, flooring, paint) in 4,000 sq ft
- HVAC system replacement (damaged by fire)
- Code upgrade work required for post-fire re-occupancy (emergency lighting, sprinkler additions)
- Business interruption loss (tenant business shut down for 3 weeks)

**Total claim: $2.8M**

**Insurance response:**
The owner sues the GC, alleging that GC's failure to identify the electrical hazard in the existing building system (pre-existing, not GC's work) created the fire risk.

GC's GL carrier pays the first $1M (per occurrence limit). The claim remains at $2.8M.

GC's Umbrella policy responds and pays the next $1.8M (up to the $2M umbrella limit).

Total insurance recovery: $2.8M (with $200K remaining exposure above umbrella limit).

**If the GC had NOT carried umbrella:**
- GL pays: $1M
- GC out-of-pocket: $1.8M
- This would bankrupt a mid-size GC.

**Cost of umbrella insurance:**
- Annual premium: $800–$1,200 for a $2M umbrella on top of a $1M GL
- GC carried it for 5 years (this was one project among many): Total cost $4,000–$6,000

**Lesson learned:**
A single catastrophic claim can exceed GL limits. Umbrella insurance is inexpensive relative to the exposure. Every GC bidding projects over $500K should carry umbrella coverage.

---

## Case Study 5: Contractual Liability Endorsement Saves Subcontractor Indemnification

**Project context:**
- $600,000 residential new build
- Roofing subcontractor (bid: $45,000) installs a roof that subsequently fails during a rainstorm 6 months post-occupancy.
- Homeowner claims water damage of $35,000 (interior water damage to drywall, finishes, and personal property).
- GC's contract with owner requires GC to indemnify owner for any defects in work: "Contractor shall indemnify and defend Owner against all claims arising from Contractor's performance or failure to perform the Work."

**GC's subcontract with roofer:**
The GC's subcontract includes: "Roofer shall indemnify Contractor against all claims arising from Roofer's performance of the Work, except to the extent the claim is caused solely by Contractor's negligence."

**The problem:**
The homeowner sues the owner, claiming water damage. The owner immediately turns to the GC under the GC-Owner indemnification clause. The GC then turns to the roofer under the GC-Roofer indemnification clause.

The roofer's GL policy (if it includes the GC as additional insured) should cover the indemnification obligation. However, if the roofer's GL policy does NOT include a **contractual liability** endorsement, the GL policy will not cover the indemnification obligation.

Without contractual liability coverage, the roofer's GL denies coverage, and the GC must pay the $35,000 claim directly.

**GC's GL policy response:**
The GC's own GL policy includes contractual liability (endorsement CG-21-86, standard on most GL policies). The GC's GL can cover the indemnification obligation to the owner, BUT the GC's GL is being used to cover the sub's responsibility, which erodes the GC's own GL limits.

**If the roofer's GL had contractual liability:**
- Homeowner sues owner.
- Owner claims indemnification from GC.
- GC claims indemnification from roofer.
- Roofer's GL (with contractual liability and GC as additional insured) covers the $35,000 claim.
- GC's GL is protected; the roofer's GL covers the roofer's responsibility.

**Prevention:**
On every subcontract, require:
1. Sub carries GL with GC as additional insured (endorsement CG-20-10 or 20-11).
2. Sub's GL includes contractual liability (endorsement CG-21-86).
3. Sub's GL includes waiver of subrogation.
4. Certificate of Insurance submitted before work begins.

**Lesson learned:**
Contractual liability endorsement on sub GL policies is critical. A GC should check every COI to verify that the sub's GL includes contractual liability (CG-21-86 or equivalent). If not, request it before allowing the sub to work.

---

**Cross-reference:** Module 12 (GC Business Setup) for insurance basics and business-level coverage; Module 13 (Construction Law) for indemnification and risk allocation in contracts; Module 29 (Dispute Resolution) for claim procedures and litigation insurance; Module 32 (Change Orders) for coverage on OCIP/CCIP projects.

**Key resources:**
- Insurance Services Office (ISO) — standard GL endorsements and forms
- American Institute of Architects (AIA) — risk allocation in AIA contracts
- AGC (Associated General Contractors) — OCIP/CCIP guidance documents
- Your project insurance broker — tailored guidance on specific projects and coverage questions
