---
title: "Veterinary Knowledge Platform Architecture"
project: systems-resilience
phase: 5
wave: 3
document_type: operational-architecture
status: production-ready
created: 2026-05-21
extends: SYSTEMS_RESILIENCE_VETERINARY_CARE_RESEARCH.md
---

# Veterinary Knowledge Platform Architecture
## Content Structure, Decision Trees, and Implementation Checklist

> **Purpose**: Define the content architecture, decision trees, and implementation pathway for a community veterinary knowledge platform — the shared protocols, species guides, emergency decision trees, and case documentation system that makes distributed care both safe and improvable over time.

---

## Lead Finding

A community veterinary knowledge platform's most critical function is not storing information — it is preventing the two most dangerous errors in distributed veterinary care: under-escalation (managing at home when veterinary intervention is needed) and over-escalation (transporting animals in states where transport itself is lethal). All content architecture decisions should serve this primary function. The platform must be usable by a community animal health worker at 2 a.m. with no internet access, no veterinarian on call, and an animal in distress.

This means: offline-capable, decision-tree-first, species-specific, and triage-anchored.

---

## Part 1: Platform Architecture Overview

### The Four Content Layers

The platform has four distinct content layers, each serving a different user at a different moment in a care episode:

**Layer 1: Emergency Decision Trees** (used at moment of crisis — first 5 minutes)
Pre-determines the escalation decision before clinical reasoning is required. These are binary trees that take observable inputs (is the animal standing? is it breathing with open-mouth? is it eating?) and output a single action: call now / transport now / monitor every 2 hours / manage at home. No medical knowledge required. These are the first thing a new CAHW learns and the last thing ever removed from the platform.

**Layer 2: Condition-Specific Protocols** (used during home management — first 30–120 minutes)
After the triage decision is "manage at home," the handler needs step-by-step procedures. Bloat treatment protocol. Dystocia assessment and initial correction. Wound care. Each protocol has: materials list, step-by-step instructions, decision nodes (stop and escalate if X), expected outcome if proceeding correctly.

**Layer 3: Preventive Care Reference** (used in planning — routine, scheduled)
Vaccination schedules, biosecurity checklists, seasonal disease calendars, nutrition guidelines, parasite management protocols (FAMACHA scoring). Used by livestock-keeping households for scheduled management, not emergency response.

**Layer 4: Case Documentation and Peer Learning** (used after the episode)
Every care episode handled within the network is documented — diagnosis, intervention, outcome, escalation decision. The hub DVM reviews and provides structured feedback. Over time, this generates a local case library that improves triage accuracy for the specific species mix, disease pressures, and seasonal patterns of the community. This is the platform's long-term value engine.

---

### Platform Format Requirements

**Non-negotiable**: Offline functionality. A platform that requires internet access to function fails exactly when it is most needed — during extended disruption, in dead zones (which characterize most USDA-designated shortage areas), and during on-farm emergencies in barns without cell signal. All Tier 1 Emergency Decision Trees and Tier 2 Condition-Specific Protocols must be available offline.

**Practical formats for offline access**:
- Printed laminated reference cards (single-sheet, one tree per species per emergency type) — the most reliable offline format; zero infrastructure dependency
- Downloaded mobile app with local storage (iOS/Android) — best for households with smartphones; requires pre-crisis download
- PDF booklet stored on a device or printed — backup format for full protocol library

**Digital platform options** (internet-dependent, for reference):
- MSD/Merck Veterinary Manual Online: the most comprehensive freely available veterinary reference; covers all species; drug interactions, dosing, and differential diagnosis
- VetGeni AI platform: clinical documentation and drug database for licensed practitioners
- Veterinary clinical decision support tools (scoping review by PMC11184142 identified six animal health CDS tools as of 2024; Bayesian algorithm-based systems are the most validated approach for differential diagnosis in low-resource settings)

---

## Part 2: Emergency Decision Trees

### Design Principles

Each decision tree must satisfy three criteria:

1. **Observable inputs only**: Every branch point is based on something the handler can directly observe without equipment (except thermometer). "Is the left flank distended?" is observable. "What is the serum calcium level?" is not.

2. **Conservative bias**: When evidence is ambiguous, the tree routes toward escalation rather than home management. The cost of an unnecessary call is low; the cost of delayed escalation is high.

3. **Species-specific**: A single generic tree covering all species creates dangerous errors. Bloat protocols for goats differ from bloat protocols for cattle. Respiratory distress presentation differs between chickens and ruminants. Each species gets its own tree.

---

### Tree 1: Ruminant (Goat/Sheep) — Is This an Emergency?

```
START: Animal is showing abnormal behavior or you found it in distress.

STEP 1: Can the animal stand and bear weight on all four limbs?
  NO  → EMERGENCY: Call veterinarian now. Do not leave the animal alone.
  YES → Go to Step 2

STEP 2: Is the animal's left flank visibly distended (bloated on the left side)?
  YES → URGENT: See Bloat Protocol (Layer 2). Call vet if no improvement in 20 min.
  NO  → Go to Step 3

STEP 3: Is the animal breathing with its mouth open (at rest, not after exercise)?
  YES → EMERGENCY: Respiratory emergency. Minimize movement. Call vet now.
  NO  → Go to Step 4

STEP 4: Is the animal showing any of these: staggering, circling, apparent blindness,
        head tilted back or to one side, muscle tremors or facial twitching?
  YES → EMERGENCY: Neurological signs. Call vet immediately.
         (Differential: Polioencephalomalacia, Listeria, Hypocalcemia — narrow treatment
          window for all three)
  NO  → Go to Step 5

STEP 5: Is the rectal temperature above 104°F or below 101°F?
  ABOVE 104°F → URGENT: Systemic infection likely. Document fever. If animal is eating:
                 monitor every 2 hours and call vet within 4 hours. If not eating: call now.
  BELOW 101°F → URGENT: Hypothermia or shock. Warm the animal. Call vet.
  NORMAL (101–104°F) → Go to Step 6

STEP 6: Is this a pregnant or recently-kidded doe showing any of these:
         anorexia, lethargy, teeth grinding, wobbling, or apparent blindness?
  YES → EMERGENCY: Pregnancy toxemia or Hypocalcemia. Call vet. Begin oral
         propylene glycol (150 ml twice daily) if propylene glycol is available
         and animal can swallow. This is a treatment window, not a cure.
  NO  → Go to Step 7

STEP 7: Is the animal eating and drinking?
  YES → Monitor closely. Document observations every 2 hours. Call vet if
         not improving within 12 hours or if condition changes.
  NO  → URGENT: Anorexia plus any other symptom = call vet within 2 hours.
         Anorexia alone (otherwise normal) = call vet within 4–6 hours.

END
```

---

### Tree 2: Poultry (Chickens) — Is This an Emergency?

```
START: Bird is separated from the flock, appears unwell, or was found on the ground.

STEP 1: Is the bird breathing with its neck extended or mouth open at rest?
  YES → EMERGENCY: Respiratory emergency or Newcastle disease.
         Isolate immediately. Call vet. Do NOT move bird into main flock.
  NO  → Go to Step 2

STEP 2: Are multiple birds in the flock showing similar symptoms?
  YES → BIOSECURITY ALERT: Isolate all affected birds. Do not move
         birds in or out. Document clinical signs. Call vet or USDA APHIS
         (1-866-536-7593 for reportable disease concerns).
  NO  → Go to Step 3

STEP 3: Is the bird showing neurological signs (circling, falling, head twisting,
        star-gazing, paralysis)?
  YES → EMERGENCY: Newcastle disease, Marek's disease, or vitamin deficiency.
         Isolate immediately. Call vet.
  NO  → Go to Step 4

STEP 4: Is the comb and wattles blue or purple (cyanotic)?
  YES → EMERGENCY: Circulatory collapse. Bird likely cannot be saved.
         Humane euthanasia should be considered immediately.
  NO  → Go to Step 5

STEP 5: Is the hen straining with tail pumping and no egg produced in 24+ hours?
  YES → URGENT: Egg binding. See Egg Binding Protocol (Layer 2).
  NO  → Go to Step 6

STEP 6: Is a vent prolapse visible (pink/red tissue protruding from vent)?
  YES → URGENT: Isolate bird from flock (others will peck it). Warm water soak,
         lubricate, gentle manual reduction. Call vet if not resolved in 1 hour.
  NO  → Go to Step 7

STEP 7: Is the bird eating, drinking, and maintaining position in the pecking order?
  YES → Monitor closely. Separate if being bullied. Check for mites/lice.
  NO  → Treat as URGENT. Support care (warmth, electrolytes). Call vet within 4 hours.

END
```

---

### Tree 3: Dogs/Cats — Is This an Emergency?

```
START: Animal is behaving abnormally, injured, or ill.

STEP 1: Are the gums pale, white, blue, or purple? (Check by pulling back the lip)
  YES → EMERGENCY: Shock, anemia, or respiratory failure.
         Transport to emergency vet immediately. Do not delay.
  NO  → Go to Step 2

STEP 2: Is the animal having a seizure, or is it unresponsive/unconscious?
  YES → EMERGENCY: Do not restrain during seizure. Keep away from hazards.
         Time the seizure. Transport immediately after seizure ends.
  NO  → Go to Step 3

STEP 3: Is there severe, uncontrolled bleeding that does not stop within 5 minutes
        of direct firm pressure?
  YES → EMERGENCY: Continue pressure. If limb: apply tourniquet above wound.
         Transport immediately.
  NO  → Go to Step 4

STEP 4: Is a dog (especially large-breed or deep-chested) showing rapid abdominal
        distension plus unproductive retching/gagging?
  YES → EMERGENCY: GDV (bloat/volvulus). Fatal without surgery within hours.
         Transport immediately. Do not delay for any reason.
  NO  → Go to Step 5

STEP 5: Is a male cat straining to urinate with little or no urine output?
  YES → EMERGENCY: Urethral obstruction. Fatal within 24–72 hours.
         Transport immediately.
  NO  → Go to Step 6

STEP 6: Do you suspect the animal ate something poisonous in the last 2 hours?
  YES → URGENT: Call ASPCA Animal Poison Control (888-426-4435, 24/7, $95 fee)
         before inducing vomiting. Do not induce vomiting without guidance.
  NO  → Go to Step 7

STEP 7: Is the animal eating, drinking, and responding to you normally?
  YES → Monitor. Seek care within 24–48 hours for minor symptoms.
  NO  → Treat as URGENT. Seek veterinary consultation (telehealth as option if
         available) within 4 hours.

END
```

---

## Part 3: Condition-Specific Protocols (Layer 2)

### Protocol Library Structure

Each Layer 2 protocol follows a standard format for consistency and rapid reading under stress:

```
PROTOCOL: [Condition Name] — [Species]
TRIAGE CATEGORY: Emergency / Urgent / Home-Management
SUPPLIES NEEDED: [itemized list from household supply cache]
TIME WINDOW: [how long before the condition becomes critical]
STEP-BY-STEP:
  1. [Action]
  2. [Action]
  DECISION NODE: If [X], stop and call vet. If [Y], continue.
  3. [Action]
EXPECTED OUTCOME: [what should happen if proceeding correctly]
STOP AND CALL IF: [conditions that indicate home management is failing]
```

### Minimum Viable Protocol Library (Priority Order)

The following protocols must exist before network operations begin. They represent the highest-frequency and highest-stakes conditions across the network's likely species mix.

**Priority 1 — Must have before any CAHW is trained:**
1. Ruminant Bloat (Goat/Sheep) — free gas and frothy
2. Ruminant Dystocia (Goat/Sheep) — birth assistance
3. Poultry Egg Binding
4. Wound Care (all species) — lacerations, puncture wounds
5. Oral Medication Administration (all species)
6. Subcutaneous and Intramuscular Injection Technique (all species)
7. Goat Urinary Obstruction — RECOGNITION ONLY (escalation protocol — no home treatment)
8. Hypocalcemia (Goat/Sheep) — early stage home treatment and escalation threshold

**Priority 2 — Build within first 3 months of network operation:**
9. Coccidiosis management — young animals
10. Respiratory illness triage — ruminants and poultry
11. Diarrhea/Scours — young ruminants (oral electrolytes, dehydration assessment)
12. Pregnancy toxemia — propylene glycol protocol
13. FAMACHA scoring — goat/sheep parasite assessment
14. Fecal egg count interpretation
15. Vaccination administration and anaphylaxis response

**Priority 3 — Build within first year:**
16. Dog/Cat wound care
17. Dog/Cat dietary indiscretion (vomiting/diarrhea)
18. Rabbit GI stasis — recognition and initial management
19. Swine erysipelas — recognition and escalation
20. End-of-life assessment (HHHHHMM scale for companion animals)

---

## Part 4: Species-Specific Care Guides

### Content Structure for Each Species Guide

A species guide is a 4–6 page reference document covering:

1. **Normal baselines**: Temperature, heart rate, respiratory rate, normal daily food/water intake, normal fecal/urine output, normal behavior patterns
2. **Seasonal health calendar**: Month-by-month disease risk profile for Zone 5 context
3. **Vaccination schedule**: Which vaccines, which months, OTC vs. prescription
4. **Common conditions**: Top 5–8 conditions by frequency, with brief recognition and response notes (linking to full Layer 2 protocols)
5. **When this species is "fine" vs. "sick"**: Behavioral baselines that distinguish normal variation from clinical illness — this is the daily observation framework

### Species Guides Required for Zone 5 Homestead Network

| Species | Priority | Key Diseases to Cover |
|---|---|---|
| Chickens (layers/meat) | 1 | Marek's, AI biosecurity, Coccidiosis, Respiratory complex, Egg binding, Pasty butt (chicks) |
| Meat/Dairy Goats | 1 | Enterotoxemia, CAE, CL, Bloat, Urinary calculi, Dystocia, Hypocalcemia, Barber Pole Worm |
| Dogs | 1 | GDV, Parvovirus, Trauma, Toxin ingestion, Urinary obstruction (cats) |
| Cats | 1 | FLUTD/urinary obstruction, Respiratory (URI), Toxin exposure, Dental |
| Rabbits | 2 | GI stasis, Pasteurellosis, RHDV2 biosecurity, Heat stress |
| Pigs (small-scale) | 2 | Erysipelas, Swine flu biosecurity, Mange, Internal parasites |
| Laying hens (supplement to chickens guide) | 2 | Vent prolapse, Egg binding, Molting management |
| Sheep | 3 | Enterotoxemia (same as goats), Footrot, Pregnancy toxemia, Barber Pole Worm |
| Poultry (turkeys/ducks) | 3 | Blackhead (turkeys), Aspergillosis, Wet pox |
| Aquaculture (pond fish) | 3 | Bacterial gill disease, Parasites (Ich), Oxygen depletion |
| Native wildlife (injured) | 3 | Recognition only + wildlife rehabilitator referral network |

---

## Part 5: Contraindication Management

### The Drug Safety Reference Layer

Veterinary drug contraindications are species-specific in ways that differ dramatically from human medicine. The most dangerous drug errors in lay veterinary care come from one of three patterns:

**Pattern 1: Human medication given to animals**
- Ibuprofen/NSAIDs (Advil, Motrin): toxic to dogs and cats; causes gastrointestinal ulcers, kidney failure
- Acetaminophen (Tylenol): causes methemoglobinemia and liver failure in cats; toxic to dogs at high doses
- Xylitol (in sugar-free products): causes severe hypoglycemia and liver failure in dogs
- Permethrin (topical insecticide): safe for dogs and horses; fatal to cats even in small doses

**Pattern 2: Livestock medication given to wrong livestock species**
- Ivermectin (certain formulations): safe for cattle and pigs at label dose; certain dog breeds (collies, shelties, and others with MDR1 gene mutation) are highly sensitive — can cause fatal neurological toxicity
- Poloxalene (bloat prevention): effective for cattle; use in goats requires dose adjustment
- Monensin (ionophore feed additive): safe for cattle and poultry; TOXIC to horses at any dose; moderately toxic to goats
- Lasalocid: safe for cattle; toxic to horses and dogs

**Pattern 3: Drug interactions**
- Organophosphate insecticides + cholinesterase-inhibiting drugs: additive toxicity
- Sulfonamides + procaine penicillin: antagonistic combination — procaine breaks down to para-aminobenzoic acid which antagonizes sulfonamides
- Flunixin (Banamine) + nephrotoxic antibiotics (gentamicin, neomycin): combined renal toxicity risk

### Contraindication Quick-Reference Card Format

The network's contraindication reference should be a laminated single-page card organized by species column:

```
NEVER give to [SPECIES]:
- CATS: Permethrin, Ibuprofen, Acetaminophen, Aspirin (any dose), Certain flea treatments
- DOGS: Xylitol, Grapes/Raisins, Macadamia nuts, Onion/Garlic (all forms)
- HORSES: Monensin, Lasalocid, Any cattle ionophore feed additive
- GOATS: Copper supplements (sheep only — goats tolerate; sheep do NOT tolerate excess copper)
- SHEEP: Copper supplements at cattle dosing levels — causes cumulative liver damage
- ALL SPECIES: Never give human NSAIDs without species-specific guidance
```

### Drug Database Access for the Network

**Free, authoritative, internet-dependent:**
- MSD/Merck Veterinary Manual Drug Library: https://www.msdvetmanual.com/pharmacology
- FARAD (Food Animal Residue Avoidance Databank): withdrawal times for food animals on extra-label drug use. Critical for food safety: if an animal received medication and will enter the food chain, withdrawal time must be respected. https://farad.org/

**For hub practitioners (licensed):**
- VetGeni drug database (AI-assisted)
- Plumb's Veterinary Drug Handbook (physical copy at hub; standard reference)

**Offline backup**: Plumb's Veterinary Drug Handbook (current edition, ~$80–$120) should be a required purchase for every hub clinic and strongly recommended for satellite CVTs. This is the single most important offline drug reference.

---

## Part 6: Case Documentation and Peer Learning System

### Why Documentation Matters for Distributed Networks

The value of documentation in a distributed veterinary network compounds over time. A CAHW who correctly diagnoses early-stage pregnancy toxemia generates a case record; the hub DVM reviews it, confirms the diagnosis, and the case enters the local case library. The next CAHW who encounters similar signs can compare against that documented case. After 200 cases, the local case library reflects the actual disease pressures, seasonal patterns, and species mix of the specific community — something no generic reference can provide.

East Africa CAHW networks that implemented case documentation showed improved triage accuracy over time (PMC5776010 — the Ethiopian smartphone surveillance app study documented improved accuracy and timeliness from lay practitioner reporting). The principle applies: structured documentation improves the skill of the person documenting and the network's collective knowledge.

### Minimum Viable Documentation System

**Case record fields (paper or digital)**:

```
DATE: _______________
CAHW NAME: _______________
SPECIES/INDIVIDUAL ANIMAL ID: _______________
CHIEF COMPLAINT (observed behavior): _______________
VITAL SIGNS (temp, HR, RR if measured): _______________
TRIAGE DECISION: [ ] Emergency call [ ] Urgent monitor [ ] Home management
ACTIONS TAKEN: _______________
OUTCOME (24-hour follow-up): _______________
HUB DVM REVIEW: [ ] Confirmed appropriate [ ] Would have escalated [ ] Notes: ___
```

**The hub DVM review is non-optional.** Without feedback, documentation becomes a rote task with no learning value. The hub DVM should commit to reviewing all submitted cases within 48 hours and providing structured feedback to the CAHW. In a network of 15 CAHWs each handling 2–3 cases per month, this is 30–45 case reviews per month for the DVM — roughly 3–5 hours if reviews average 5–8 minutes per case.

### Digital Documentation Options

**For internet-connected networks**: A shared spreadsheet (Google Sheets, shared with hub DVM), a simple practice management tool, or a custom form system (Google Forms → Google Sheets pipeline requires no software cost).

**For offline-first networks**: Paper case forms organized in a binder at each satellite location; collected and scanned/photographed for hub DVM review monthly; retained in chronological file at hub.

**Confidentiality**: Case records contain individual animal health data and household information. They should be treated as private records — not shared publicly without owner consent. Network governance documents should specify data ownership (network vs. individual household) and retention policy.

---

## Part 7: Implementation Checklist

### Phase 1: Minimum Viable Platform (Before Network Launch)

- [ ] Emergency Decision Trees completed for all species in network (minimum: ruminants, poultry, dogs/cats)
- [ ] All Priority 1 Layer 2 protocols written and reviewed by hub DVM
- [ ] Normal baselines reference card created for each species
- [ ] Contraindication quick-reference card printed and laminated for each CAHW
- [ ] Hub DVM has reviewed and approved all emergency content
- [ ] Offline format confirmed: printed laminated cards at each satellite location AND PDF downloaded on all CAHW smartphones
- [ ] Case documentation form designed and printed (50 copies per CAHW starting stock)
- [ ] Hub DVM review commitment confirmed (48-hour response standard)
- [ ] ASPCA Animal Poison Control number (888-426-4435) on every reference card
- [ ] USDA APHIS reportable disease hotline (1-866-536-7593) on every reference card

### Phase 2: Full Platform (Within First 6 Months)

- [ ] All Priority 2 protocols completed
- [ ] All species guides completed for network's species mix
- [ ] Contraindication reference expanded to cover all drugs in network supply cache
- [ ] Drug withdrawal time reference (FARAD) available to hub
- [ ] Case library initialized with first 20+ documented cases
- [ ] Hub DVM review feedback loop operational (48-hour target met consistently)
- [ ] Platform reviewed and updated after every significant seasonal disease event
- [ ] 6-month protocol review scheduled with hub DVM and 2+ CAHWs

### Phase 3: Continuous Improvement (Ongoing, Quarterly)

- [ ] Quarterly case review: what conditions are most frequent? Are protocols adequate?
- [ ] Annual protocol review with hub DVM: update based on new AVMA/AAVMC guidance
- [ ] FAMACHA scoring accuracy audit (annual, for networks with ruminants)
- [ ] Vaccination schedule update based on USDA APHIS and CFSPH current recommendations
- [ ] New CAHW onboarding review: does the platform serve new learners well?
- [ ] Emerging disease alerts: USDA APHIS disease alerts integrated into seasonal updates

---

## Sources

- MSD/Merck Veterinary Manual. https://www.msdvetmanual.com/
- PMC11184142, Expanding access to veterinary CDS tools in resource-limited settings. https://pmc.ncbi.nlm.nih.gov/articles/PMC11184142/
- Frontiers in Veterinary Science, CDS tools scoping review. https://www.frontiersin.org/journals/veterinary-science/articles/10.3389/fvets.2024.1349188/full
- PMC5776010, Ethiopian smartphone app for livestock disease surveillance. https://pmc.ncbi.nlm.nih.gov/articles/PMC5776010/
- FARAD, Food Animal Residue Avoidance Databank. https://farad.org/
- Virginia Cooperative Extension, APSC-169, Monitoring Livestock Vital Signs. https://www.pubs.ext.vt.edu/APSC/APSC-169/APSC-169.html
- University of Missouri VHC, Recognizing a Medical Emergency in Small Ruminants. https://vhc.missouri.edu/food-animal-hospital/recognizing-a-medical-emergency-in-small-ruminants/
- ASPCA, Animal Poison Control. https://www.aspca.org/pet-care/animal-poison-control
- USDA APHIS, reportable diseases. https://www.aphis.usda.gov/livestock-poultry-disease
- WOAH CAHW competency guidelines (11 modules). https://www.woah.org/app/uploads/2024/09/woah-competency-and-curriculum-guidelines-for-cahws-071024.pdf
- PMC10044252, HHHHHMM Scale validation. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10044252/
- VetGeni AI platform. https://www.vetgeni.com/veterinary-ai

---

*Phase 5 Wave 3 — Knowledge Platform Architecture*
*Prepared: 2026-05-21 | Status: Production-ready*
