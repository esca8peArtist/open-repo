---
title: "ITEM15 — Nutrition & Meal Planning Integration Guide"
project: workout
status: complete
date: 2026-05-07
series-position: master-index
related:
  - comprehensive-plan.md
  - nutrition-01-macro-micronutrient-framework.md
  - nutrition-02-meal-timing-nutrient-timing.md
  - nutrition-03-meal-planning-templates.md
  - nutrition-04-supplementation-guide.md
  - nutrition-05-periodization.md
  - nutrition-06-recovery-optimization.md
  - nutrition-and-tracking.md
sources:
  - "Morton et al. 2018, PMC5867436 — Protein meta-analysis"
  - "ISSN Position Stand — Nutrient Timing, PMC5596471"
  - "Morton et al. 2025, IJSNEM — Nutritional Periodization"
  - "Frontiers in Nutrition 2025 — Dietary supplements systematic review, PMC12498230"
  - "PMC12251028 — Creatine and beta-alanine co-supplementation 2025"
  - "BodySpec — Calisthenics vs Weights for Fat Loss (science-backed)"
---

# ITEM15 — Nutrition & Meal Planning: Integration Guide

**What this document is:** The master integration layer connecting the workout project's training plans to its nutrition series. It answers the question most users will actually ask: *"I am doing the [X] equipment tier at [Y] days/week and my goal is [Z] — what exactly do I eat?"*

**What this document is not:** A standalone nutrition textbook. The six specialist nutrition files already cover the science in depth. This document synthesises their outputs into actionable decision trees, maps them to each training configuration, and provides the implementation sequence a new user needs on Day 1.

**Read this first. Then go deeper in the specialist files.**

---

## Navigation Map — Nutrition Series

| Document | What It Covers | Read When |
|---|---|---|
| **This document** | Decision trees, tier+frequency+goal tables, implementation checklist | First |
| `nutrition-01-macro-micronutrient-framework.md` | Calorie targets, protein/carb/fat science, micronutrients | Setting up your numbers |
| `nutrition-02-meal-timing-nutrient-timing.md` | Pre/intra/post-workout windows, meal frequency, timing by training schedule | Structuring your meals |
| `nutrition-03-meal-planning-templates.md` | Full 7-day meal plans with macro breakdowns and grocery lists | Writing your weekly plan |
| `nutrition-04-supplementation-guide.md` | Evidence tiers for every major supplement, doses, timing, cost | Deciding on supplements |
| `nutrition-05-periodization.md` | How to change nutrition as training phases change | Running a 12-week cycle |
| `nutrition-06-recovery-optimization.md` | Sleep nutrition, injury nutrition, cortisol management | Recovery-focused periods |
| `nutrition-and-tracking.md` | Simple tracking system (no app required), progress metrics | Building the habit |

---

## Section 1 — Nutrition Fundamentals

### The Priority Stack

Before any specific target, the hierarchy of nutritional importance:

1. **Total daily calories** — the master variable for weight change and energy availability
2. **Protein** — the non-negotiable; every other macro adjusts around it
3. **Carbohydrates** — the primary performance fuel; scales with training volume
4. **Fats** — hormonal substrate; maintain a floor, never slash below 0.6 g/kg/day
5. **Micronutrients** — the silent infrastructure; deficiency caps everything above
6. **Meal timing** — amplifier, not foundation
7. **Supplements** — the last 5%, not the first 50%

**If you get #1–3 right 80% of days, you will progress.** Everything else is marginal gain territory. The hierarchy is non-negotiable.

### TDEE Calculation

Total Daily Energy Expenditure is your maintenance calorie level — the point at which body weight is stable.

**Practical estimate:**

> BMR (calories/day) ≈ bodyweight in pounds × 10  
> TDEE = BMR × activity multiplier

| Training Frequency | Activity Multiplier | Example (180 lb / 82 kg person) |
|---|---|---|
| 3 days/week | 1.375 | 1,800 × 1.375 = **~2,475 cal** |
| 4 days/week | 1.55 | 1,800 × 1.55 = **~2,790 cal** |
| 5 days/week | 1.65 | 1,800 × 1.65 = **~2,970 cal** |
| 6 days/week | 1.725 | 1,800 × 1.725 = **~3,105 cal** |

**Important:** These are starting estimates. Individual metabolism varies by 10–15%. Track bodyweight daily for 2 weeks (average each week), then adjust calories by 100–200 if weight is moving in the wrong direction.

**For each goal, adjust from TDEE:**

| Goal | Calorie Adjustment | Rate of Change |
|---|---|---|
| Fat loss | −300 to −500 cal/day | 0.3–0.5 kg/week loss |
| Muscle gain (beginner) | +300 to +500 cal/day | 0.25–0.5 kg/week gain |
| Muscle gain (intermediate+) | +150 to +300 cal/day | 0.1–0.25 kg/week gain |
| Recomposition | ±0 (maintenance) | Weight stable; composition shifts |
| Maintenance | ±0 | Weight stable |

### Macronutrient Ratios

**Protein is always the anchor.** Set protein first, then fill calories with carbs and fats.

| Goal | Protein (g/kg/day) | Carbs (g/kg/day) | Fats (g/kg/day) |
|---|---|---|---|
| Fat loss | 2.2–2.6 (elevated to preserve muscle) | 2.5–4 | 0.6–0.9 |
| Muscle gain | 1.8–2.2 | 5–7 | 0.8–1.2 |
| Recomposition | 2.2–2.6 | 3–4 | 0.8–1.2 |
| Maintenance | 1.6–2.0 | 3–5 | 0.8–1.2 |

*Source: Nutrition 01; targets derived from Morton et al. 2018 meta-analysis (PMC5867436) and subsequent 2024–2025 network meta-analyses confirming the 1.6–2.2 g/kg effective range.*

**Protein quality:** Prioritise complete protein sources with high leucine content (whey, eggs, chicken, beef, Greek yogurt). Plant-based athletes: add 10–15% to protein targets and combine sources for amino acid completeness. See Nutrition 01, Part 1 for the full quality table.

### Micronutrient Priorities for Athletes

Four micronutrients cause measurable performance impairment at deficient levels. Everyone training seriously should know their status.

| Micronutrient | Why It Matters | Deficiency Risk | Action |
|---|---|---|---|
| **Iron** | Oxygen transport; VO2 impairment before anaemia appears | High in female athletes (20–40%); moderate in males (3–11%) | Test serum ferritin; supplement only if < 30 ng/mL |
| **Vitamin D** | Muscle contractile function, testosterone, immune modulation | Endemic at northern latitudes and indoor athletes | 2,000–4,000 IU D3/day with fat-containing meal; pair with K2 |
| **Magnesium** | ATP synthesis, muscle relaxation, sleep quality | Athletes consistently underconsume; lost in sweat | 250–400 mg magnesium glycinate before sleep |
| **Zinc** | Protein synthesis, testosterone production, immune function | High sweat-loss athletes; vegetarians | 15–25 mg zinc glycinate if dietary intake is below 11 mg/day |

For the full micronutrient table including B-vitamins, calcium, and electrolytes, see Nutrition 01, Part 4.

### Individual Variation

Nutrition targets are population means. Expect individual variation of ±15% in calorie needs and ±0.3 g/kg in protein requirements.

**Factors that shift requirements upward:**
- Age 40+ (anabolic resistance; increase protein by 0.2–0.3 g/kg)
- High daily non-exercise movement (manual labour, standing jobs)
- Poor sleep (>1 hour below 8 hours/night; increases muscle protein breakdown)
- High training stress (volume peaks in weeks 3–4 of each mesocycle)

**Factors that allow lower intake:**
- Beginner level (neural adaptations dominate; lower MPS requirement)
- Sedentary day jobs with pure training activity
- Consistent 8+ hours sleep (optimal GH release reduces muscle breakdown)

**Food sensitivities and cultural preferences:** The macros matter more than the specific foods. Any whole-food protein source — animal or plant — works if the leucine threshold (2–3 g per meal) is met. Regional staples (rice, dal, plantain, injera, tortillas) all serve equally well as carbohydrate bases. If a food is not listed in a meal plan but fits the macro profile, substitute freely.

### Hydration Strategy

Hydration affects strength performance starting at just 2% bodyweight fluid deficit.

| Context | Target | Notes |
|---|---|---|
| Baseline (non-training) | 35–40 ml/kg/day | Adjust for climate; darker urine = drink more |
| Training sessions < 60 min | 500–750 ml during session | Water is sufficient |
| Training sessions 60–90 min | 750 ml + electrolytes | Add 300–500 mg sodium/hour |
| Sessions > 90 min or in heat | 200–300 ml every 15–20 min | Active sodium replacement mandatory |
| Post-exercise rehydration | 150% of weight lost | 1 kg weight loss = 1.5 L replacement needed |

Do not rely on thirst for performance-critical sessions. By the time thirst is noticeable, performance is already declining.

---

## Section 2 — By Equipment Tier

### How Equipment Tier Affects Nutrition

The equipment tier determines the intensity ceiling and muscle mass recruited per session. Higher tiers recruit more total muscle mass, generate more metabolic stress, and require more calories for recovery. The effect is meaningful but not dramatic — the largest differences are in carbohydrate targets and post-workout recovery nutrition, not in protein targets.

| Tier | Primary Metabolic Demand | Calorie Burn (approx., 60 min session) | Key Nutritional Implication |
|---|---|---|---|
| **Tier 1: No Equipment** | Moderate anaerobic; high skill demand; significant cardiovascular if circuit-based | 300–500 kcal | Lower absolute calorie need; NEAT from incidental movement often larger contributor than session |
| **Tier 2: Resistance Bands** | Moderate-to-high anaerobic; constant band tension increases eccentric demand | 350–550 kcal | Similar to Tier 1 but slightly elevated protein need due to eccentric muscle damage |
| **Tier 3: Full Gym** | High anaerobic; maximum motor unit recruitment via external load; highest glycogen demand | 450–700+ kcal (compound-heavy programs) | Largest carbohydrate requirement; progressive calorie increase as strength increases |

*Note: Bodyweight calisthenics evidence (BodySpec analysis, 2024) shows calorie burn per minute is comparable to moderate-intensity weightlifting, and post-exercise oxygen consumption (EPOC) is slightly higher for full-body calisthenics circuits. The primary difference is that maximum external load potential is capped in Tier 1, limiting long-term hypertrophy potential without progression to harder variations.*

---

### Tier 1 — No Equipment

**Training context from comprehensive-plan.md:** Push-ups, pull-ups (if bar available), calisthenics progressions (planche lean, L-sit, pistol squat), athletic conditioning. Maximum volume without weights. Sessions typically 60–75 minutes.

#### Protein Demand

Protein requirements for bodyweight resistance training are **identical to weight training** once the stimulus is sufficient. The common misconception that bodyweight training needs less protein is incorrect — the muscle damage and MPS response from hard calisthenics (Bulgarian split squats, archer push-ups, Nordic curls) is equivalent to moderate-load barbell work.

**Target:** 1.6–2.0 g/kg/day for muscle building; 2.2–2.4 g/kg/day for fat loss.

The practical challenge in Tier 1 is not the target — it is achieving it on a budget without preparation. Budget protein sources that do not require cooking:
- Canned tuna (170 g can = 34 g protein, ~$1.50)
- Greek yogurt (200 g = 18–20 g protein, ~$0.80)
- Cottage cheese (250 g = 25 g protein, ~$1.20)
- Hard-boiled eggs (batch cook 12 at once; 2 eggs = 12 g protein)
- Whole milk (500 ml = 16 g protein, ~$0.40)

#### Calorie Profiles by Goal

For a reference athlete: 82 kg (180 lb), training 4 days/week, Tier 1.

| Goal | Daily Calorie Target | Protein | Carbs | Fats |
|---|---|---|---|---|
| Fat loss | ~2,100–2,300 cal | 180–196 g (2.2 g/kg) | 164–246 g (2–3 g/kg) | 49–74 g (0.6–0.9 g/kg) |
| Muscle gain | ~2,700–2,900 cal | 148–180 g (1.8–2.2 g/kg) | 328–410 g (4–5 g/kg) | 66–98 g (0.8–1.2 g/kg) |
| Recomposition | ~2,400–2,600 cal | 180–213 g (2.2–2.6 g/kg) | 246–328 g (3–4 g/kg) | 66–98 g (0.8–1.2 g/kg) |

#### Sample Budget-Friendly Meal Plan — Tier 1 Muscle Gain (1-Day Example)

**Daily target:** ~2,750 cal | 160 g protein | 375 g carbs | 80 g fat  
**Daily food cost:** ~$5.50–7.00

| Meal | Foods | Cal | Protein | Carbs | Fat |
|---|---|---|---|---|---|
| Breakfast | 3 whole eggs + 100 g oats (dry) + 200 ml whole milk + 1 banana | 720 | 38 g | 110 g | 22 g |
| Lunch | 2 cans tuna (340 g total) + 200 g cooked white rice + 1 tbsp olive oil + lemon | 680 | 74 g | 43 g | 15 g |
| Pre-workout snack | 250 g Greek yogurt + 1 tbsp honey + 30 g oats | 380 | 22 g | 55 g | 7 g |
| Post-workout | 500 ml whole milk + 1 banana + 30 g peanut butter | 540 | 22 g | 68 g | 22 g |
| Dinner | 3 whole eggs + 200 g sweet potato + 100 g spinach + 1 tbsp olive oil | 430 | 24 g | 45 g | 22 g |
| **Total** | | **2,750** | **180 g** | **321 g** | **88 g** |

*Add 2 slices whole grain toast (+160 cal, 28 g carbs) if carbs fall short. Increase milk to 750 ml for easy calorie top-up.*

**Vegan Tier 1 adaptation:** Replace eggs and milk with tofu (250 g = 20 g protein) + soy milk (300 ml = 10 g protein). Replace tuna with tempeh (200 g = 38 g protein). Add pea+rice protein powder (1 scoop = 25 g protein) to hit the daily protein target. Total cost difference: approximately +$1.50–2.00/day.

---

### Tier 2 — Resistance Bands

**Training context:** Bands add constant tension and an eccentric loading profile different from both bodyweight and free weights. Band exercises include pull-aparts, banded push-ups, band pull-throughs, banded squats and hip thrusts. The primary nutritional implication is slightly elevated muscle protein breakdown from the eccentric component — meaning protein targets nudge toward the upper end of ranges.

#### Protein Requirements

Eccentric-emphasis training (bands under stretch create high eccentric load on the return phase) produces measurable increases in delayed-onset muscle soreness and muscle protein breakdown markers. Studies consistently show that eccentric-dominant training increases protein utilisation by 10–15% compared to concentric-only work.

**Target:** 1.8–2.2 g/kg/day (muscle gain); 2.2–2.6 g/kg/day (fat loss or recomposition).

#### Calorie Targets by Training Frequency

For an 82 kg reference athlete with Tier 2 training:

| Frequency | Estimated TDEE | Muscle Gain (+300 cal) | Fat Loss (−400 cal) | Recomposition |
|---|---|---|---|---|
| 3 days/week | ~2,400 cal | ~2,700 cal | ~2,000 cal | ~2,400 cal |
| 4 days/week | ~2,750 cal | ~3,050 cal | ~2,350 cal | ~2,750 cal |
| 5 days/week | ~2,950 cal | ~3,250 cal | ~2,550 cal | ~2,950 cal |
| 6 days/week | ~3,100 cal | ~3,400 cal | ~2,700 cal | ~3,100 cal |

#### Sample Meal Plan — Tier 2, 4 Days/Week, Muscle Gain (1-Day, Training Day)

**Daily target:** ~3,050 cal | 172 g protein | 420 g carbs | 95 g fat

| Meal | Foods | Cal | Protein | Carbs | Fat |
|---|---|---|---|---|---|
| Breakfast | 4 eggs scrambled + 80 g oats + 200 ml milk + banana | 800 | 44 g | 99 g | 28 g |
| Pre-workout | 150 g chicken breast + 150 g cooked white rice | 440 | 52 g | 43 g | 3 g |
| Post-workout | Whey shake (35 g) + 500 ml sports drink + banana | 440 | 33 g | 78 g | 1 g |
| Lunch | 180 g ground beef (90% lean) + 150 g cooked pasta + marinara | 570 | 43 g | 50 g | 18 g |
| Snack | 200 g Greek yogurt + 25 g almonds | 300 | 21 g | 9 g | 19 g |
| Dinner | 150 g salmon + 200 g sweet potato + broccoli + olive oil | 500 | 34 g | 50 g | 15 g |
| Evening | 250 g cottage cheese | 218 | 25 g | 9 g | 9 g |
| **Total** | | **3,268** | **252 g** | **338 g** | **93 g** |

*Adjust portions down by 10–15% on rest days (reduce carbs; keep protein constant).*

**Weekly grocery estimate:** $68–80/week at standard prices; $42–50 on the budget swap plan from Nutrition 03.

---

### Tier 3 — Full Gym

**Training context from comprehensive-plan.md:** Barbell compounds (squat, bench, deadlift, row, overhead press), dumbbell accessories, cable work, machine work. Maximum external load progression. Sessions 65–75 minutes for 4-day plans; 65+ minutes for 5–6 day plans.

#### Key Nutritional Drivers

1. **Progressive calorie increase as strength increases.** As the barbell gets heavier, more muscle mass is recruited per session, and glycogen demand rises. A lifter squatting 60 kg burns meaningfully fewer calories than one squatting 140 kg over an equivalent set-and-rep scheme. Expect to recalculate TDEE every 8–12 weeks.

2. **Optimal protein timing.** With Tier 3's higher session intensity and systemic protein turnover, the post-workout window matters slightly more. A study (Frontiers in Nutrition, 2025 systematic review) confirms protein within 2 hours of resistance training increases MPS regardless of exact timing — but for Tier 3 athletes, a dedicated post-workout protein dose of 30–40 g with carbohydrates is a meaningful performance tool, not just a nice-to-have.

3. **Intra-workout carbohydrates for sessions > 60 minutes.** Full gym compound programs with 5–6 exercises easily run 70–90 minutes. Once session duration exceeds 60 minutes at high intensity, glycogen depletion impairs performance within the session. 30–60 g fast carbohydrates intra-workout (sports drink, banana, raisins) prevents the performance decline that occurs when glycogen drops below 50% saturation.

#### Calorie Targets by Frequency and Goal

For an 82 kg reference athlete with Tier 3 training:

| Frequency | Estimated TDEE | Muscle Gain | Fat Loss | Recomposition |
|---|---|---|---|---|
| 3 days/week | ~2,550 cal | ~2,850 cal | ~2,150 cal | ~2,550 cal |
| 4 days/week | ~2,900 cal | ~3,200 cal | ~2,450 cal | ~2,900 cal |
| 5 days/week | ~3,100 cal | ~3,400 cal | ~2,600 cal | ~3,100 cal |
| 6 days/week | ~3,300 cal | ~3,600–3,800 cal | ~2,750 cal | ~3,300 cal |

*Heavy compound lifters at 6 days/week with significant muscle mass may have TDEEs of 3,500–4,000+. These estimates assume average recreational athletic output.*

#### Sample Meal Plan — Tier 3, 5 Days/Week, Muscle Gain (1-Day, Training Day)

**Daily target:** ~3,400 cal | 180 g protein | 470 g carbs | 100 g fat

| Meal | Foods | Cal | Protein | Carbs | Fat |
|---|---|---|---|---|---|
| Breakfast | 4 eggs + 100 g oats + 300 ml milk + 1 tbsp honey + banana | 970 | 50 g | 138 g | 30 g |
| Pre-workout | 180 g chicken breast + 200 g cooked white rice + 1/2 tbsp olive oil | 580 | 63 g | 57 g | 10 g |
| Intra-workout | 500 ml sports drink | 130 | 0 g | 32 g | 0 g |
| Post-workout | Whey shake (35 g) + banana + 300 ml sports drink | 380 | 33 g | 59 g | 1 g |
| Lunch | 200 g ground beef + 200 g cooked rice + mixed veg | 620 | 45 g | 58 g | 20 g |
| Snack | 250 g Greek yogurt + 30 g walnuts + 1 tbsp honey | 430 | 22 g | 26 g | 28 g |
| Dinner | 200 g sirloin steak + 200 g sweet potato + broccoli + olive oil | 610 | 48 g | 45 g | 20 g |
| Evening | 300 g cottage cheese | 261 | 30 g | 11 g | 10 g |
| **Total** | | **3,981** | **291 g** | **426 g** | **119 g** |

*This is a high-volume day. Scale down protein to 180 g and carbs to 420 g for exact targets. On rest days: remove intra-workout, sports drink, and reduce rice to 150 g. Increase dietary fats slightly.*

---

## Section 3 — By Goal

### Fat Loss

**Defining the deficit correctly.** The evidence-supported deficit for most recreational athletes is 300–500 cal/day below TDEE, producing 0.3–0.5 kg/week loss. Larger deficits accelerate fat loss but accelerate lean mass loss proportionally. Athletes who want to preserve training performance should not exceed 500 cal/day deficit.

**Protein is elevated in deficit, not reduced.** Counterintuitively, fat loss phases require the *highest* protein intake: 2.2–2.6 g/kg/day. This is strongly supported by the ISSN position on protein and exercise (PMC5477153) and multiple deficit studies showing that protein above 2.0 g/kg substantially preserves lean mass and strength during caloric restriction.

**Nutrient density matters more during a deficit.** With fewer total calories, the cost of micronutrient-poor food choices is higher. Priority foods during a cut:
- Lean proteins: chicken breast, egg whites, white fish, Greek yogurt, cottage cheese
- High-fibre vegetables: broccoli, spinach, cauliflower, cucumber (low calorie, high satiety)
- Moderate-GI carbs: oats, sweet potato, legumes (satiety via fibre + resistant starch)
- Fruit: berries, apples (high fibre, moderate sugar, high micronutrient density)

**Adherence strategies.** The most common failure mode in a deficit is not metabolic — it is behavioural. Hunger management:
- Eat protein at every meal (30–40 g per meal reduces postprandial hunger hormones)
- Prioritise food volume over calorie density (100 g chicken has 165 cal; 100 g almonds has 580 cal)
- Keep dietary fat at the floor (0.6–0.8 g/kg) — do not eliminate, as fat slows gastric emptying and reduces hunger

**12-week fat loss nutrition timeline:**

| Weeks | Deficit | Training Phase | Key Adjustments |
|---|---|---|---|
| 1–2 | −200 cal (ramp-in) | Full intensity | Establish protein habit; measure baseline weight |
| 3–8 | −400 to −500 cal | Full intensity | Main cut; deload at week 5–6 |
| 9–10 | −400 cal | Reduced volume (deload) | Maintain protein; reduce carbs 15–20% |
| 11–12 | −200 cal (ramp-out) | Return to full intensity | Refeed to maintenance; assess body composition |

After 12 weeks, take a 2–4 week maintenance break before continuing. Hormonal adaptation (reduced T3, increased ghrelin) makes extended cuts progressively less effective and harder to sustain.

---

### Muscle Gain (Clean Bulk)

**Surplus sizing.** The most common error in a muscle gain phase is eating too large a surplus. A beginner (< 1 year training) can use 300–500 cal/day above TDEE. An intermediate (1–3 years) should not exceed 200–350 cal/day. An advanced lifter (3+ years) rarely needs more than 100–200 cal/day — the rate of muscle gain is simply slower, and a larger surplus produces predominantly fat.

**Protein targets.** 1.8–2.2 g/kg/day is the evidence-supported range for hypertrophy (Morton et al. 2018; updated 2024 meta-analyses confirm gains plateau near 2.0 g/kg for most, with marginal returns to 2.4 g/kg in some populations). Higher-end targets (2.2 g/kg) are useful for older athletes (40+) or those with poor sleep or high training stress.

**Carbohydrates are the mass-gain lever.** When adding calories in a surplus, the extra calories should come from carbohydrates — not fat. Fat has a hormonal floor (0.6 g/kg) but no meaningful upper performance benefit above 1.2 g/kg. Adding carbs fuels training volume, supports glycogen replenishment, and drives insulin-mediated nutrient partitioning toward muscle.

**Training frequency and nutrient partitioning.** Higher training frequencies (5–6 days/week) improve nutrient partitioning during a surplus — more days of elevated muscle protein synthesis means more of the caloric surplus is directed toward muscle rather than fat. This is the primary nutritional argument for 5–6 day programs during an active building phase.

**12-week muscle gain timeline:**

| Weeks | Surplus | Expected Gain | Key Adjustments |
|---|---|---|---|
| 1–4 | +300 cal | 0.3–0.4 kg/week (mostly glycogen + neural) | Establish eating rhythm; do not expect scale to move fast |
| 5–10 | +300–400 cal | 0.2–0.3 kg/week (lean mass + some fat) | Peak training volume; do not diet; protein at upper end |
| 11–12 | +200 cal (ramp-down) | Deload and assessment | Reduce surplus during deload; assess body composition trend |

---

### Recomposition (Simultaneous Fat Loss + Muscle Gain)

Body recomposition was long considered impossible in trained individuals. A 2024 editorial in Frontiers in Nutrition and supporting RCTs now confirm it is achievable with specific conditions.

**Conditions required:**
1. **Protein at 2.2–2.6 g/kg/day** — the most important variable
2. **Calories near maintenance** (±200 cal, not a meaningful surplus or deficit)
3. **Heavy resistance training 3–5 days/week** (the anabolic stimulus is the "surplus" at the muscle level)

**Who can recompose effectively:**
- Beginners (< 12 months training) at any calorie level — the beginner stimulus is powerful enough to drive simultaneous gain and loss
- Athletes returning after a training break (muscle memory accelerates lean mass recovery)
- Intermediate athletes with high protein intake and consistent heavy training

**Who should not expect recomposition:**
- Advanced athletes (3+ years training, near genetic ceiling) — marginal results; a dedicated bulk-cut cycle is more efficient
- Athletes in a large deficit (> 500 cal/day) — too much lean mass loss to call it recomposition

**Practical recomposition nutrition:**
- Calories: TDEE (no surplus, no deficit)
- Protein: 2.2 g/kg minimum (e.g., 82 kg athlete = 180 g/day)
- Carbs: 3–4 g/kg (adequate for training; not excess)
- Fats: 0.8–1.0 g/kg
- Timeline: 12–24 weeks minimum; body composition changes slowly and scale weight may not move

---

### Maintenance

Maintenance nutrition is the underrated goal. Athletes maintaining a training effect while travelling, in a life-stress period, or between structured phases need a simple, sustainable framework.

**Calorie stability.** Track bodyweight weekly average. If it drifts > 1 kg in either direction over 3 weeks, adjust calories by 150–200 and reassess.

**The performance shift.** In maintenance phases, the nutrition focus shifts from mass or composition change to **performance and energy**. This means:
- Carbohydrate targets based on training schedule, not calorie goals (pre-workout and post-workout carbs remain non-negotiable even when total calories are neutral)
- Micronutrient investment (when not chasing rapid composition change, it pays to improve food quality)
- Recovery nutrition (Nutrition 06 is most relevant during extended maintenance phases)

**Minimum effective protein:** 1.6 g/kg/day during maintenance. Athletes who let protein slip below this threshold during maintenance periods lose meaningful lean mass over months.

---

## Section 4 — Meal Planning Templates

### How to Use the Templates

The full 7-day meal plans with day-by-day macro breakdowns are in `nutrition-03-meal-planning-templates.md`. That file contains:

- **Plan A:** Hypertrophy/muscle gain (7-day, 2,800 cal reference)
- **Plan B:** Strength-focused (7-day, 2,600 cal reference)
- **Plan C:** Conditioning/maintenance (7-day, 2,200 cal reference)

Each plan includes: full macro breakdown per meal, grocery list with cost estimates ($65–75/week standard, $40–45/week budget), vegan adaptations, and batch cooking guidance.

**Scaling the templates to your parameters:**

All templates use an 82 kg (180 lb) reference athlete. To scale:
- **Protein:** Multiply your bodyweight (kg) × your g/kg target → this is your daily protein gram total
- **Calories:** Use the TDEE table in Section 1 above, then adjust for your goal
- **Carbs and fats:** Adjust proportionally to hit calorie target after protein is fixed

**Macro calculator (simple formula):**

```
Step 1: TDEE = (bodyweight in lbs × 10) × activity multiplier
Step 2: Protein = bodyweight (kg) × protein target (g/kg)
Step 3: Protein calories = protein (g) × 4
Step 4: Remaining calories = TDEE ± goal adjustment − protein calories
Step 5: Carbs = 60% of remaining calories ÷ 4
Step 6: Fats = 40% of remaining calories ÷ 9
```

*Example: 75 kg athlete, 5 days/week, muscle gain.*  
TDEE = 165 lbs × 10 × 1.65 = 2,723 cal. Goal: +350 cal = 3,073 cal.  
Protein: 75 × 2.0 = 150 g (600 cal). Remaining: 2,473 cal.  
Carbs: 2,473 × 0.60 ÷ 4 = **370 g**. Fats: 2,473 × 0.40 ÷ 9 = **110 g**.

**Flexibility guidelines for eating out:**
- Prioritise protein first: ask for extra protein, double the meat, add eggs
- Estimate carbs as a moderate portion (1 cup rice = ~50 g carbs)
- Do not obsess over fats in restaurants — assume +20–30 g above what's visible
- One meal off target does not break a week of good nutrition; consistency over days matters more than perfection at each meal

**Regional food availability:** All templates can be built around local staples. High-protein staples across cuisines: legumes + grains (South Asian, African, Latin American), fish (coastal regions, East Asian), tofu + tempeh (East/Southeast Asian), dairy (European, North American). Any whole-food carbohydrate staple — rice, plantain, yam, injera, corn tortilla — works as the carb base.

---

## Section 5 — Supplement Strategy

### The Honest Priority Framework

The supplement industry generates over $50B/year in revenue. Most of that revenue is from products with weak or no evidence. This section covers what the evidence actually supports, what has conditional support, what to avoid, and how to allocate a limited budget.

**Ground rule:** Supplements cannot compensate for inadequate calories, poor protein intake, or insufficient sleep. They are amplifiers for an already-functional nutrition base.

---

### Tier 1 — Strong Evidence, Most Athletes Benefit

**Creatine Monohydrate**
- **Effect size:** +5–10% strength (1RM) over 4–12 weeks; +1.3–2.3 kg lean mass over 8 weeks vs. training alone (PMC10180745); +10–15% repeated sprint capacity
- **Dose:** 3–5 g/day indefinitely (no loading required; loading just saturates faster). Creatine monohydrate only — HCl and "buffered" forms have more expensive pricing and no superior evidence.
- **Timing:** Does not matter significantly. Take with any meal.
- **Cost:** ~$0.10–0.20/day (200 g bag lasts 40–65 days at 3–5 g/day)
- **Who benefits most:** Vegans (zero dietary creatine from plant foods); athletes 40+ (natural creatine stores decline with age); high-frequency athletes (recovery acceleration)
- **Updated 2025 evidence:** PMC12251028 confirms creatine + training combination enhances high-intensity exercise performance, particularly anaerobic power — the effect is robust and consistent across populations.

**Protein Powder (Whey or Plant-Based)**
- Not essential if whole-food protein targets are being met — but a practical tool for athletes who struggle to hit 160+ g protein from food alone
- **Whey:** 25–30 g protein per scoop, high DIAAS score, complete amino acid profile; concentrate is cheaper than isolate with minor practical difference
- **Plant-based:** Pea+rice blend (not single-source pea) provides comparable amino acid profile; look for 25+ g protein per serving and 2.5+ g leucine
- **Cost:** $1.00–1.50/serving whey concentrate; $1.50–2.00/serving plant blend
- **Dose:** Use to fill the gap between dietary protein and daily target; typically 1–2 scoops/day

**Vitamin D3**
- Endemic deficiency in indoor athletes and those at northern latitudes (above 40°N latitude in winter, synthesising vitamin D from sunlight is essentially impossible)
- **Effect:** Meta-analysis (MDPI Nutrients, 2024) confirms D3 supplementation improves lower-limb muscle strength in deficient athletes; immune support is also well-established
- **Dose:** 2,000–4,000 IU/day with a fat-containing meal; pair with 100–200 mcg vitamin K2 for optimal calcium partitioning
- **Cost:** ~$0.05–0.10/day; one of the most cost-effective supplements available

**Caffeine**
- Well-established ergogenic at 3–6 mg/kg bodyweight 30–60 minutes before training
- Improves strength output, endurance, and reduces rate of perceived exertion
- **Practical note:** Tolerance develops with daily use; cycle off 1 week/month or reserve for hard sessions. Black coffee (80–100 mg per 250 ml cup) is an equally effective and cheaper alternative to pre-workout products.
- **Cost:** Coffee is $0.10–0.30/serving; caffeine tablets are $0.05–0.10/serving

---

### Tier 2 — Conditional Evidence, Worth Considering

**Beta-Alanine**
- Increases muscle carnosine, which buffers hydrogen ions during high-intensity glycolytic work. Practical benefit is specific to activities lasting 1–4 minutes at near-maximal intensity.
- **Who benefits:** Athletes doing HIIT circuits, conditioning finishers, or any activity with repeated 60–180 second high-intensity bouts. Athletes doing primarily strength training (1–5 rep sets with full rest) see minimal benefit.
- **Dose:** 3.2–6.4 g/day; split doses to reduce paraesthesia (tingling sensation). Requires 4 weeks of loading to see effect.
- **Updated 2025 evidence:** PMC12251028 confirms the creatine + beta-alanine combination enhances anaerobic power and repeated-bout performance more than either alone. Relevant for Tier 3 athletes running conditioning finishers.
- **Cost:** ~$0.30–0.50/day

**Citrulline Malate**
- Enhances nitric oxide production, increasing blood flow and nutrient delivery to working muscle. May reduce DOMS by 30–40% and modestly improve repeated-sprint capacity.
- **Evidence quality:** Frontiers in Nutrition 2025 systematic review notes citrulline acts as a "facilitator of training and recovery" rather than a direct driver of morphological change. Honest framing: real but modest effect.
- **Dose:** 6–8 g taken 60 minutes before training
- **Who benefits:** High-volume athletes (5–6 days/week) seeking better session-to-session recovery; athletes with high DOMS sensitivity

**Omega-3 (EPA+DHA)**
- Reduces exercise-induced muscle damage markers (CK, DOMS), modestly improves protein synthesis rate, and has strong cardiovascular evidence
- **Dose:** 1–2 g combined EPA+DHA daily. Fish oil or algae-based (vegan)
- **Who benefits:** Athletes not eating fatty fish 2–3×/week (most people). Particularly valuable during high-volume training blocks when muscle damage is highest.
- **Cost:** ~$0.15–0.30/day for standard fish oil; $0.40–0.60/day for algae-based

---

### Avoid — Marketing Without Meaningful Evidence

| Supplement | Claim | Reality |
|---|---|---|
| BCAAs (branched-chain amino acids) | Muscle growth, recovery | BCAAs are a subset of protein. If you hit protein targets from whole foods or protein powder, BCAAs are fully redundant — you are already getting them. |
| Proprietary pre-workout blends | Energy, pump, performance | Usually a combination of caffeine (get separately), beta-alanine (get separately), and proprietary "blends" that exempt them from dosage disclosure. Buy the ingredients individually. |
| Testosterone boosters | Natural T increase | No over-the-counter supplement meaningfully raises testosterone. Clinical evidence for marketed ingredients (ashwagandha, tribulus, ZMA) is weak and context-specific. |
| Glutamine | Muscle recovery | The body synthesises glutamine endogenously; supplementation is redundant in athletes eating adequate protein. Evidence for performance benefit is essentially absent. |
| HMB (beta-hydroxy beta-methylbutyrate) | Anti-catabolic | One or two early studies showed effects in untrained subjects. Subsequent trials in trained athletes showed no meaningful benefit vs. protein-matched controls. |
| Fat burners (thermogenics) | Accelerated fat loss | Largely caffeine + synephrine at doses that create cardiovascular risk. Fat loss is determined by caloric deficit; no supplement changes the fundamental equation. |

---

### Budget Allocation

**$30–40/month baseline (strong evidence only):**
- Creatine monohydrate: $8–12/month
- Vitamin D3 + K2: $5–8/month
- Protein powder (if needed to hit targets): $15–25/month for 15–20 servings

**$50–70/month (add conditionals):**
- All baseline above, plus omega-3 fish oil: $8–12/month
- Caffeine tablets (if not using coffee): $3–5/month
- Beta-alanine (if doing HIIT): $10–15/month

**Testing whether a supplement works for you:** Run any new supplement for minimum 8 weeks at the proper dose before assessing. Track training volume (sets × reps × weight) and subjective recovery weekly. If no measurable improvement in either metric after 8 weeks, the supplement is not producing meaningful benefit for your individual physiology.

---

## Section 6 — Periodization Nutrition

### The Core Principle

Apply different nutritional strategies to different training phases the way you apply different sets and rep ranges. Static nutrition on a dynamic training program is sub-optimal by definition.

From Nutrition 05: *"A fixed 2,800 cal/day plan applied across a hypertrophy block, a deload week, a conditioning phase, and an active rest week will consistently overfeed in some periods and underfeed in others."*

### Phase-by-Phase Nutrition Adjustments

**Phase 1 (Weeks 1–4, all tiers): Neural Adaptation**

The first training block is dominated by nervous system adaptation, not muscle hypertrophy. Protein requirements are not yet at their maximum, and caloric needs are lower than they will be in later phases.

- Calories: TDEE + 200–300 (conservative surplus; the adaptation is neural, not hypertrophic)
- Protein: Lower end of target range (1.6–1.8 g/kg)
- Carbs: Moderate (4–5 g/kg)
- Priority: Build the nutrition habit — meal timing, protein distribution, hydration. Do not stress perfect macro hitting; aim for correct order of magnitude.

**Phase 2 (Weeks 5–12, all tiers): Hypertrophy Block**

This is peak training volume. Glycogen demand is highest. Protein synthesis is running maximally. Do not diet during this phase.

- Calories: TDEE + 300–500 (full surplus for beginners; +200–350 for intermediates)
- Protein: Upper end of target range (2.0–2.2 g/kg)
- Carbs: Upper bound (5–7 g/kg); prioritise peri-workout window
- Priority: Maximize recovery; do not let carbs fall below target on heavy training days

**Deload Weeks (every 4th week or as prescribed in comprehensive-plan.md)**

- Calories: TDEE (maintenance; do not cut calories during a deload)
- Protein: Maintain at full target — muscle protein breakdown remains elevated for 48–72 hours after the last hard session. Protein during rest days and deloads is protective, not wasteful.
- Carbs: Lower bound for the goal (3–4 g/kg); training volume is reduced
- Priority: Recovery nutrition (Nutrition 06), sleep, micronutrients

**Strength-Focused Blocks (if using the strength variation in comprehensive-plan.md)**

- Lower rep ranges, longer rest periods, lower total volume per session
- Calorie needs are slightly lower than hypertrophy blocks (less total work done)
- Protein maintained at full target
- Carbs: 3–5 g/kg (reduced from hypertrophy phase; glycogen demand is lower)
- Emphasis: Micronutrient sufficiency for connective tissue health (collagen, vitamin C, vitamin D)

**Conditioning-Heavy Periods**

- Significant additional cardiorespiratory demand beyond resistance training
- Increase carbs by 1–2 g/kg to match glycolytic demand
- Sodium replacement becomes critical (high sweat volume during sustained conditioning)
- Do not add conditioning volume without adding carbs to match it — performance will degrade week-over-week

### Carbohydrate Timing Within the Week (Microcycle)

Within any training week, carbs should shift with training demands:

| Day Type | Carb Target (as % of weekly high) | Practical Example (82 kg, hypertrophy) |
|---|---|---|
| Heavy compound day (squat, deadlift, bench) | 100% | 410–574 g (5–7 g/kg) |
| Moderate volume day | 75–80% | 300–380 g |
| Skill/technique day (low glycogen demand) | 60–70% | 250–320 g |
| Rest day | 40–50% | 164–246 g (2–3 g/kg) |

**Protein remains constant across all days.** Do not reduce protein on rest days.

### 12-Week Periodized Nutrition Calendar Template

This pairs with the 12-week program structure in `comprehensive-plan.md`.

| Week | Phase | Calories | Protein | Carbs | Key Focus |
|---|---|---|---|---|---|
| 1–2 | Phase 1 adaptation | TDEE + 200 | 1.6 g/kg | 4 g/kg | Build eating habits |
| 3–4 | Phase 1 peak | TDEE + 300 | 1.8 g/kg | 5 g/kg | Increase portions with training volume |
| 5 | Deload | TDEE | 1.8 g/kg | 3 g/kg | Maintain protein; pull back carbs |
| 6–8 | Phase 2 hypertrophy | TDEE + 350–400 | 2.0–2.2 g/kg | 6–7 g/kg | Maximize recovery; no dieting |
| 9–10 | Phase 2 peak | TDEE + 400 | 2.2 g/kg | 6–7 g/kg | Highest glycogen demand of the cycle |
| 11 | Deload | TDEE | 2.0 g/kg | 3–4 g/kg | Recovery; sleep focus |
| 12 | Assessment | TDEE | 1.8 g/kg | 4–5 g/kg | Baseline re-test; prepare next phase |

For a fat loss goal: subtract 400 cal from the above calorie column each week; increase protein by 0.2–0.4 g/kg.  
For recomposition: hold calories at TDEE throughout; protein at 2.2 g/kg from Week 1.

---

## Section 7 — Implementation Checklist

The most common failure mode is not choosing the wrong nutrition plan — it is failing to build the execution habit in the first three weeks. This checklist is sequenced to build the habit before adding complexity.

### Week 1 — Measure Before You Manage

- [ ] **Establish your baseline.** Log everything you eat for 3 days (2 weekdays + 1 weekend day) using MyFitnessPal, Cronometer, or a simple written food log. Do not change your eating yet — just observe.
- [ ] **Calculate your numbers.** Using the TDEE formula in Section 1 and your goal, set daily protein, calorie, carb, and fat targets.
- [ ] **Weigh yourself every morning** after waking and before eating. Record the number. Average the week's readings.
- [ ] **Identify your protein gap.** Most people eating ad libitum consume 60–100 g protein/day. Your target is likely 130–200 g. Find the gap and plan which foods will close it.

### Weeks 2–3 — Build the Structure

- [ ] **Set your protein anchors first.** Build each day around 3–4 high-protein meals. Everything else fills in around them.
- [ ] **Write your first grocery list** using one of the plans in Nutrition 03 as a template. Modify for your budget and preferences.
- [ ] **Batch cook once.** Cook 1 kg of protein (chicken breast, ground beef, hard-boiled eggs) and 500 g of a carb source (rice, sweet potato) in one session. This eliminates the "nothing to eat" failure point for 3–4 days.
- [ ] **Start creatine.** 3–5 g/day with any meal. This is the highest-return supplement. No loading required.
- [ ] **Check Vitamin D status.** If you do not get 30+ minutes of midday sun daily, start 2,000–4,000 IU D3 with dinner.

### Week 4 — First Adjustment Checkpoint

- [ ] **Compare Week 1 average bodyweight to Week 4 average bodyweight.** 
  - If weight is moving in the correct direction at the correct rate: hold course.
  - If weight is not moving: adjust calories by 150–200 cal in the appropriate direction.
  - If weight is moving too fast: either the surplus/deficit is too large, or water fluctuations are distorting the signal. Wait one more week before adjusting.
- [ ] **Assess protein compliance.** Are you hitting your protein target most days? If not, identify the specific meal where protein consistently falls short and add a protein source there.
- [ ] **Assess energy levels.** Consistent fatigue during sessions suggests either: insufficient carbohydrate, insufficient overall calories, or poor sleep. Check in order.

### Ongoing Quarterly Reviews

- [ ] **Recalculate TDEE every 8–12 weeks.** As body composition changes, TDEE changes. A lighter person needs fewer calories; a stronger/more muscular person may need more.
- [ ] **Reassess supplement stack** at 3-month intervals. Is each supplement producing a measurable benefit? If not, cut it and redirect the budget.
- [ ] **Check iron status** if performance has declined unexpectedly, especially in female athletes. Serum ferritin < 30 ng/mL is the threshold for supplementation.
- [ ] **Adjust for season/climate.** Summer training in heat increases fluid and sodium requirements meaningfully. Winter at northern latitudes makes Vitamin D supplementation non-optional.

### When to Adjust Mid-Cycle

| Signal | Likely Cause | Action |
|---|---|---|
| Performance declining week-over-week | Energy/carb deficit; insufficient recovery | Increase carbs by 30–50 g on training days; assess sleep |
| Losing strength on a bulk | Deficit is larger than intended; protein too low | Add 200 cal (all carbs); confirm protein target is being hit |
| Gaining weight faster than expected (>0.5 kg/week on a "lean bulk") | Surplus too large | Reduce by 200 cal/day; usually from carbs |
| Constant fatigue + poor mood | Caloric deficit too aggressive; micronutrient gap | Increase to maintenance for 1–2 weeks (diet break); check iron and D |
| Injury | Increased protein and collagen needs | See Nutrition 06 (injury nutrition protocol); increase protein to 2.0–2.5 g/kg |

### Tools

**Free:**
- **Cronometer** (preferred over MyFitnessPal for micronutrient tracking — better database accuracy)
- **MyFitnessPal** (larger food database; better for restaurant estimation)
- **Kitchen scale** (most important tool; measuring in cups is inaccurate by 20–40%)
- **Written food log** (notebook + food label reading; works for anyone resistant to apps)

**Paid (optional):**
- **Registered dietitian** (most valuable for athletes with complex medical histories, eating disorder history, or high competition goals)
- **InBody or DEXA scan** (body composition assessment; more accurate than scale weight for tracking progress; useful at start and every 12 weeks)

---

## Sources

- [Morton et al. 2018 — Protein meta-analysis, PMC5867436](https://pmc.ncbi.nlm.nih.gov/articles/PMC5867436/)
- [ISSN Position Stand — Nutrient Timing, PMC5596471](https://pmc.ncbi.nlm.nih.gov/articles/PMC5596471/)
- [ISSN Position Stand — Protein and Exercise, PMC5477153](https://pmc.ncbi.nlm.nih.gov/articles/PMC5477153/)
- [Morton et al. 2025 — Nutritional Periodization, IJSNEM](https://journals.humankinetics.com/view/journals/ijsnem/36/3/article-p279.xml)
- [Frontiers in Nutrition 2025 — Efficacy of dietary supplements, PMC12498230](https://pmc.ncbi.nlm.nih.gov/articles/PMC12498230/)
- [PMC12251028 — Creatine and beta-alanine co-supplementation 2025](https://pmc.ncbi.nlm.nih.gov/articles/PMC12251028/)
- [Frontiers in Nutrition 2025 — Post-exercise recovery timing](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2025.1567438/full)
- [Frontiers in Nutrition 2024 — Body recomposition editorial](https://www.frontiersin.org/journals/nutrition/articles/10.3389/fnut.2024.1467406/full)
- [BodySpec — Calisthenics vs. Weights for Fat Loss](https://www.bodyspec.com/blog/post/calisthenics_vs_weights_for_fat_loss_a_sciencebacked_comparison)
- [PMC10180745 — Creatine and regional hypertrophy meta-analysis](https://pmc.ncbi.nlm.nih.gov/articles/PMC10180745/)
- [ISSN Position Stand — Beta-Alanine, PMC4501114](https://pmc.ncbi.nlm.nih.gov/articles/PMC4501114/)
