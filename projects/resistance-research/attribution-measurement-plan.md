---
title: "Phase 1 Attribution Measurement Plan"
date: 2026-05-05
status: production-ready
session: 780
purpose: >
  Methodology for distinguishing framework causation from co-causation in
  measuring Phase 1 distribution impact. Defines four attribution tests,
  measurement timeline, sector-specific interpretation, Rogers S-curve
  positioning, and counterfactual baseline. Companion to
  phase-1-baseline-metrics.md.
cross_references:
  - phase-1-baseline-metrics.md
  - measurement-and-iteration-framework.md
  - post-distribution-impact-measurement-framework.md
  - domain-37-baseline-metrics.md
---

# Phase 1 Attribution Measurement Plan

**Established: May 5, 2026 — before Phase 1 distribution**

The central attribution problem for any policy framework is this: democratic institutions were already under pressure before the framework existed, lawyers and advocates were already filing cases and publishing analysis, and the causal chain from "framework distributed" to "policy outcome changed" runs through many intervening actors. The question is not whether framework adoption causes good things to happen — it often does not cause them in any simple sense — but whether the framework accelerates, coordinates, or structurally enables outcomes that would have happened more slowly, less efficiently, or not at all.

This plan defines the four tests that will distinguish framework causation from co-causation, the measurement windows at which those tests are applied, how attribution standards differ by sector, where the framework is positioned on Rogers's adoption S-curve at each measurement window, and what the historical record of comparable frameworks suggests the counterfactual baseline should be.

---

## Part I: Four-Test Attribution Framework

Attribution is assessed by running all four tests simultaneously. No single test is sufficient; convergent evidence across two or more tests constitutes credible attribution.

### Test 1: Vocabulary Marker Test

**Definition**: Does the adopting actor use vocabulary, analytical categories, or domain taxonomy that appears in the framework and did not appear in their prior work?

**Operationalization**: Compare the actor's pre-distribution published work against their post-distribution work. Specific vocabulary to track:
- Any use of the phrase "35-domain" or reference to the domain numbering system
- Use of framework-specific domain titles (e.g., "Prosecutorial Weaponization" as a standalone analytical category — a framing that did not appear in major legal publications before Domain 29 was written)
- Citation of the comparative international precedents contained in the framework's domain research (e.g., the German Bundesverfassungsgericht constructive no-confidence provision as a template for U.S. reform — a cross-reference unlikely to appear independently in most domestic legal work)
- Use of the OLC memo "hybrid theory" characterization of the Venezuela operation (Domain 28 analysis) — a specific analytical frame developed in this framework

**Attribution threshold**: If an actor uses two or more vocabulary markers in work published after confirmed contact with the framework, the vocabulary marker test is satisfied.

**Limitation**: Vocabulary can spread through intermediaries (A reads the framework and tells B, who uses the vocabulary without having read the framework). This is still a framework-attributable diffusion event, even if it is two steps removed.

**Not attributable via this test**: Use of general vocabulary ("democratic backsliding," "executive overreach," "rule of law") that was pre-existing in the discourse. Only novel or recombined vocabulary counts.

---

### Test 2: Structural Convergence Test

**Definition**: Does the adopting actor's analytical structure — the way they organize a multi-domain problem — converge with the framework's domain architecture in a way that is unlikely given their prior work?

**Operationalization**: The framework's distinctive structural contribution is organizing the U.S. democracy crisis into discrete, cross-referenced domain categories with international comparative evidence for each. This is different from a general "threats to democracy" inventory. Structural convergence is evidenced when:
- A published piece, amicus brief, or policy report organizes its analysis into domain-parallel categories that parallel the framework's structure
- A litigation strategy memo uses the framework's multi-domain coordination model (linking litigation across Domains 1, 6, 29, and 37 as components of a unified enforcement strategy)
- A law school course restructures around domain-parallel analytical units

**Attribution threshold**: Structural convergence that crosses three or more domains, in work published after confirmed contact, where the actor's prior work did not use comparable domain architecture.

**Limitation**: This test is harder to satisfy and carries more weight when it is satisfied. Most citations will satisfy Test 1 (vocabulary) without fully satisfying Test 2 (structure). Full structural adoption by a single institution constitutes a high-confidence attribution event.

---

### Test 3: Timing-and-Contact Test

**Definition**: Is there a documented contact event (email sent, link shared, conversation confirmed) followed within a reasonable causal window by an outcome, where the timing is unlikely to be coincidental?

**Operationalization**:
- **Step 1**: Confirm and timestamp all distribution contacts (DISTRIBUTION_EXECUTION_LOG.md)
- **Step 2**: Document subsequent outcomes (citations, brief filings, policy statements) with their publication dates
- **Step 3**: Apply a causal window appropriate to the sector (see Part III: Sector-Specific Attribution)
- **Step 4**: Calculate whether the outcome falls within the causal window for that sector

**Causal windows by sector**:
- AG policy counsel: 4-8 weeks from contact to internal memo incorporation; 8-16 weeks to external filing
- Think tank researcher: 2-6 weeks from contact to blog post; 3-12 months to formal publication
- Law school faculty: 2-8 weeks from contact to syllabi revision; 6-18 months to academic publication
- Journalist: 1-2 weeks from contact to article; attribution signal requires vocabulary marker as corroboration

**Attribution threshold**: Contact documented before outcome; outcome falls within sector-appropriate causal window; no evidence of independent discovery before contact.

**Limitation**: Timing alone is never sufficient — it must be combined with Test 1 or Test 2. A think tank publishing similar analysis 8 weeks after contact satisfies timing but requires vocabulary convergence to move from "plausible" to "credible" attribution.

---

### Test 4: Counterfactual Baseline Test

**Definition**: Would the outcome have occurred anyway, at roughly the same time and with roughly the same structure, absent the framework?

**Operationalization**: This is the most demanding test and is largely answered by historical comparison rather than direct observation. The question is whether the framework accelerates or structures outcomes that were already in the baseline trend.

Three categories of outcome:

**Category A — Baseline-driven outcomes (not framework-attributable)**:
Outcomes that were clearly on the baseline trajectory before distribution. Examples:
- New multistate AG coalition lawsuit filed on voting rights — this is in the normal churn rate documented in phase-1-baseline-metrics.md Metric 3. Unless vocabulary markers or structural convergence are present, this is baseline.
- Brennan Center publishes a report on election interference — this is Brennan Center's core function and would occur absent the framework.
- Just Security publishes an analysis of war powers — this is their regular publication cadence.

**Category B — Accelerated outcomes (weakly framework-attributable)**:
Outcomes that were probably coming eventually but appear to arrive earlier, with greater coordination, or with more comprehensive evidence, following framework contact. Attribution is "co-causation with acceleration." Examples:
- AG coalition letter that uses Domain 37 CISA evidence arrives 60 days after AG contact, while comparable coalition letters on this specific sub-issue had not appeared in the prior 90 days.
- A law review note on prosecutorial weaponization is submitted after faculty contact, and the note cites Domain 29 evidence not previously compiled in this form.

**Category C — Framework-enabled outcomes (strongly attributable)**:
Outcomes that would not plausibly have occurred on the baseline trajectory — outcomes that require the framework's specific analytical structure or evidence compilation to occur. Examples:
- A litigant files an amicus brief in a war powers case citing the OLC memo "hybrid theory" analysis from Domain 28 — a piece of evidence that required deep document research not done elsewhere.
- An AG office incorporates the Domain 37 seven-baseline metrics into its election security legal strategy — a specific, non-obvious structural contribution.
- A Senate hearing incorporates the framework's comparative international evidence for a specific reform domain.

**Attribution standard**: Category C outcomes satisfy the counterfactual test. Category B outcomes are credible co-causation. Category A outcomes are not attributable to the framework absent corroborating evidence from Tests 1-3.

---

## Part II: Measurement Timeline

All measurements are taken against the Day 0 baselines established in phase-1-baseline-metrics.md. Measurement windows are fixed ex ante and are not extended retroactively.

### Window 1: Day 0-30 — Access Period Monitoring

**What is being measured**: Whether the framework reached its targets and generated initial engagement.

**Key measurements**:
- Email delivery and open rates (against 2% failure threshold; 12-18% success threshold)
- Reply rates and nature of replies (substantive engagement vs. acknowledgment vs. decline)
- Confirmed routing events (contact confirms they shared with litigation team, co-author, or colleague)
- Any early Tier A media citations (would indicate unusual early-adopter signal)

**Attribution assessment**: No outcome attribution in this window. This window establishes whether the distribution infrastructure worked. Attribution tests are premature — causation cannot run from a document received 3 weeks ago to a published piece.

**What a strong Day 30 looks like**: 10-15 confirmed engagements; 2-4 AG offices with confirmed routing; 1-2 think tank contacts requesting domain-specific follow-up; 0 citations (expected).

**What a weak Day 30 looks like**: 0-3 engagements; email deliverability issues; no routing events. See phase-1-baseline-metrics.md Metric 5 for failure threshold triggers.

---

### Window 2: Month 2-3 — Vocabulary Adoption Monitoring

**What is being measured**: Whether framework vocabulary is beginning to appear in the discourse of early adopters.

**Key measurements**:
- Systematic search of all Tier A and B sources for vocabulary markers (Test 1)
- Follow-up contacts to any Day 30 engagers: "Has the framework been useful? Has it influenced any specific work product?"
- Monitoring of PACER for amicus briefs in the highest-relevance active cases (Domain 37 election cases, Domain 28 war powers, Domain 6 independent agency removal)
- Conference presentation mentions (April-May 2026 season; September 2026 season)

**Attribution assessment**: First attribution claims possible but should be held to high standard. A Tier A publication that uses vocabulary markers and was confirmed to have received the framework constitutes credible early attribution. A think tank blog post by a confirmed contact that uses domain-parallel structure constitutes credible early attribution.

**Target**: 2-5 cumulative vocabulary-marker citations; 1-3 confirmed routing events to secondary audiences; 1 conference mention.

---

### Window 3: Month 4-6 — Substantive Adoption Monitoring

**What is being measured**: Whether the framework's analytical structure is being incorporated into institutional work products.

**Key measurements**:
- Amicus briefs filed in pending Domain-area cases (PACER search by case docket)
- Think tank publication citations (all Tier B sources reviewed)
- Law school syllabi updates (direct faculty contact follow-up; indirect signals from course listings)
- AG coalition letters or press releases using domain analysis
- Congressional testimony citing framework evidence

**Attribution assessment**: Full four-test attribution assessment for any outcome that appears in this window. An AG amicus brief that satisfies Tests 1, 3, and 4 is a Category B-C attribution event. A law review note in submission that satisfies Tests 2 and 3 is a Category B event. Document every attribution finding in DISTRIBUTION_EXECUTION_LOG.md.

**Target**: 5-15 cumulative citations across Tier A, B, C; 1-2 confirmed institutional adoption events (syllabi, brief, coalition letter); 0-1 Category C attribution events.

---

### Window 4: Month 7-12 — Diffusion Pattern Monitoring

**What is being measured**: Whether adoption is following an S-curve or has plateaued; which sectors are leading; where secondary diffusion (adopter to new adopter) is occurring.

**Key measurements**:
- All prior measurements continued at monthly cadence
- First law review article in production that cites framework (submission date is proxy for awareness date)
- Second-order diffusion: does a law review note cite a think tank piece that cites the framework? Does an AG amicus brief cite a Brennan Center report that uses domain language?
- Phase 2 go/no-go decision: at Month 9-12, assess whether Phase 1 evidence base justifies Phase 2 distribution expansion

**Attribution assessment**: At 12 months, conduct systematic four-test attribution review of all identified outcomes. Produce a Phase 1 Impact Assessment document that maps each outcome to its attribution category (A, B, or C) and its test satisfaction profile.

**Target**: 10-30 cumulative citations; 2-5 institutional adoption events; 1-2 second-order diffusion events (adopter A introduces framework to adopter B); 0-2 Category C attribution events.

---

## Part III: Sector-Specific Attribution

Attribution standards differ by sector because the causal mechanisms and outcome types differ. The same citation event has different evidentiary weight depending on who produced it.

### State Attorneys General

**Mechanism**: Framework reaches AG policy counsel through direct outreach or NAAG network. Policy counsel routes relevant domain to litigation team. Litigation team incorporates evidence into pending filing, new complaint, or amicus brief.

**Attribution interpretation**: AG citations carry the highest institutional weight but are the hardest to track. AG briefs do not announce their research sources; an amicus brief that uses Domain 37 CISA evidence without attribution to the framework is still a framework-attributable event if Tests 1 and 3 are satisfied.

**Key signals**:
- PACER search for briefs in Domain-relevant cases (Democracy Docket flags these)
- NAAG coalition letters (public; searchable)
- AG press releases using framework vocabulary

**Attribution ceiling**: Even a single amicus brief in the SAVE Act litigation (31 pending cases) that uses domain-specific analysis constitutes a high-value institutional adoption event. AG filings create public record.

**Caution**: AGs are institutionally resistant to endorsing external frameworks by name. "The analysis in [cite]" is unlikely; "courts have recognized" citing domain evidence without attribution is the realistic adoption form. Do not confuse non-attribution with non-adoption.

---

### Law Schools

**Mechanism**: Faculty member receives framework, routes to clinic students as a research resource, assigns in course, or incorporates evidence into their own scholarship. Law review editors may independently discover framework through faculty contact and solicit a note or comment.

**Attribution interpretation**: Law school citations carry high permanence (especially law review citations) but have a long lag. A faculty member who finds Domain 6 useful for a course in September 2026 will not produce a citable law review article until 2027 at the earliest. The near-term signals are behavioral: faculty forward to colleagues, students cite in clinic memos, syllabi update.

**Key signals**:
- Direct faculty confirmation (most reliable; follow-up email at Month 3)
- Student clinic memos citing framework (these rarely become public; ask for confirmation)
- SSRN working paper posting
- Law review submission (long lag; most significant)

**Attribution calibration**: Law school adoption is most meaningful for Phase 2 and Phase 3 impact, not Phase 1. A course assignment in Fall 2026 semester seeds a class of 20 law students who will carry the framework's analytical categories into their careers over the following decade. This is the mechanism by which the Model Penal Code spread in the 1960s-1980s and the mechanism by which ABA Model Rules achieved 50-state adoption over 20 years.

---

### Think Tanks

**Mechanism**: Researcher receives framework; finds domain analysis useful for a report already in progress; incorporates evidence or adopts vocabulary; publishes report or blog post.

**Attribution interpretation**: Think tank citations are the fastest and most trackable. Just Security publishes in days; Brennan Center publishes in weeks to months. Vocabulary marker test is most useful here because think tank writing is published and searchable.

**Key signals**:
- Publication by confirmed contact within 90 days of distribution (Test 3 satisfied)
- Vocabulary markers in the publication (Test 1 corroboration)
- Request for additional domain-specific materials (pre-publication signal)

**Attribution calibration**: Think tank citations are medium-weight individually but create citation chain infrastructure. A Brennan Center report that uses Domain 29 analysis, subsequently cited by five law review notes, creates a five-citation diffusion event from a single adoption.

---

### Journalists

**Mechanism**: Framework reaches journalist through direct outreach or through a source who read it. Journalist uses domain analysis as background research; specific figures, timelines, or frameworks appear in article.

**Attribution interpretation**: Journalistic citations are fastest but least durable (not indexed in academic databases; not PACER-accessible; often not attributed by name). The attribution test requires that: (a) contact is confirmed before publication (Test 3); and (b) article contains specific data points or analytical frames that are unique to the framework (Test 1).

**Key signals**:
- Article uses specific baseline numbers from phase-1-baseline-metrics.md or domain-37-baseline-metrics.md
- Article uses domain-specific framing (e.g., "five-vector interference strategy" if that framing is adopted from Domain 37)
- Journalist requests background interview or documents after receiving framework

**Attribution calibration**: Journalistic citation is lowest-weight for academic or policy purposes but highest-weight for public discourse. An Atlantic article that uses Domain 37 evidence reaches 1-2 million readers; a law review article that uses the same evidence reaches 200. Both matter; they matter differently.

---

## Part IV: Rogers S-Curve Application

The framework's expected position on Rogers's adoption S-curve at each measurement window, based on the baseline metrics and historical comparable diffusion patterns.

### Rogers Adopter Categories (Reference)

| Category | Share of Total Population | Characteristics |
|----------|--------------------------|----------------|
| Innovators | 2.5% | Risk-tolerant; early discovery; low credibility threshold |
| Early Adopters | 13.5% | Opinion leaders; credibility gatekeepers; produce the testimonials that drive early majority |
| Early Majority | 34% | Deliberate; adopt when peer adoption provides social proof |
| Late Majority | 34% | Skeptical; adopt under peer pressure or structural necessity |
| Laggards | 16% | Tradition-bound; last to adopt if ever |

Applied to the framework's institutional target universe of 103 Tier 1-2 institutions:

| Adopter Category | N (of 103) | Expected Adoption Window |
|-----------------|-----------|-------------------------|
| Innovators | 3 | Month 1-2 |
| Early Adopters | 14 | Month 2-6 |
| Early Majority | 35 | Month 6-18 |
| Late Majority | 35 | Month 18-36 |
| Laggards | 16 | Month 36+ or never |

### S-Curve Position by Measurement Window

**Day 0-30**: Pre-diffusion. Framework in distribution phase; no S-curve position yet established. The 10-15 Day 30 engagement targets represent potential innovators, not confirmed adopters.

**Month 2-3**: Innovator phase. If 2-5 citations appear and 1-2 confirmed adoption events occur, we are in the innovator adoption band. This is exactly where the framework should be. Innovators do not produce the S-curve inflection point; they produce the credibility signals (testimonials, published citations) that Early Adopters require before adopting.

**Month 4-6**: Early Adopter recruitment phase. The 5-15 cumulative citation target represents movement into early adopter territory. The key variable is whether any Early Adopter institution (Brennan Center, a T14 law school clinic, a Senate Judiciary staff contact) produces a public adoption signal — because that signal is what triggers early majority interest.

**Month 7-12**: Early Adopter consolidation / Early Majority threshold. If by Month 12 the framework has 10-30 citations and 3-5 confirmed institutional adoption events, it is in the early-to-early-majority transition. This is the inflection point of the S-curve — the point after which diffusion accelerates without active promotion. Most policy frameworks that reach 20+ citations from institutional sources within 12 months achieve S-curve inflection by Month 18-24.

**Month 13-24 (Phase 2 window)**: Early Majority adoption. S-curve inflection if early adopter signals were strong. Phase 2 distribution should be timed to coincide with early majority onset — distributing before S-curve inflection is premature; distributing after is reactive.

### Inflection Point Prerequisites

Based on the Rogers literature and policy framework diffusion case studies, S-curve inflection requires three conditions to be met simultaneously:
1. At least one high-credibility institution (Brennan Center, Harvard Law, a state AG coalition) has publicly adopted or cited the framework
2. The framework is available in a format that early majority institutions can engage (short executive summary, domain one-pagers, Substack archive)
3. At least one "observable adoption" event has occurred that early majority actors can see and evaluate as a social proof signal

Phase 1 distribution is designed to achieve condition 2. Early adopter phase (Month 2-6) is where conditions 1 and 3 must be achieved before Phase 2 distribution accelerates.

---

## Part V: Counterfactual Baseline — Historical Precedents

To assess whether the framework's adoption rate is fast, slow, or normal, the following historical precedents provide the relevant comparison class.

### Model Penal Code (1962) — 15-Year Diffusion

**Comparator**: The MPC was drafted by the American Law Institute and promulgated in 1962. It took approximately 15 years for a majority of states to substantially revise their penal codes based on the MPC. By the mid-1970s, more than two-thirds of states had adopted provisions.

**Diffusion mechanism**: The MPC spread through law school curricula (criminal law courses adopted it as the analytical framework within 3-5 years), through ALI member networks (similar to the framework's Tier 2 academic contacts), and through state legislative reform commission adoption.

**Counterfactual implication**: Without the MPC, state criminal law reform would have been slower, more fragmented, and would have lacked a common analytical vocabulary across states. The MPC's contribution was coordination — it gave reformers in each state a shared template rather than requiring each to develop their own from scratch. This is precisely the framework's intended function.

**Calibration for this framework**: The MPC had the ALI's institutional authority, a 10-year drafting process, and a formal promulgation event. This framework lacks those institutional anchors but operates in a faster information environment. Adjusted expectation: 3-7 year diffusion to widespread institutional adoption (vs. 15 years for MPC) is plausible if early adopter phase is successful.

### ABA Model Rules of Professional Conduct (1983) — 20-Year Full Adoption

**Comparator**: The ABA Model Rules were adopted in 1983. By 2003, almost all states had adopted some form of the Model Rules. Full adoption (all states) took 20 years.

**Diffusion mechanism**: Law school ethics courses adopted the Model Rules within 2-3 years (fast academic diffusion). Bar association adoption required state-by-state approval processes. Major law firms shifted to Model Rules compliance within 5-7 years.

**Counterfactual implication**: Without the Model Rules, state professional conduct codes would have continued to diverge, creating coordination problems for multi-state legal practice. The Model Rules' contribution was standardization — a vocabulary and analytical structure that made cross-state legal practice coherent.

**Calibration for this framework**: The ABA had monopoly authority over legal ethics; this framework has no comparable enforcement mechanism. But the framework does not need enforcement-mechanism adoption; it needs citation and analytical adoption. Citation diffusion is faster than institutional adoption — a 5-10 year citation diffusion cycle for academic and think tank sources is realistic.

### Brennan Center Automatic Voter Registration Campaign (2015-2024) — 10-Year Diffusion

**Comparator**: The Brennan Center began actively promoting AVR in 2015. Oregon and California adopted AVR in 2015. By 2024, 24 states and DC had adopted AVR in some form.

**Diffusion mechanism**: The Brennan Center provided the model legislation, the evidence base, and the advocacy infrastructure. State adoption was the outcome. The first two states adopted within months of the Brennan Center's model legislation being published. The most recent adoptions (Pennsylvania 2023, 10 years later) are late-majority events.

**Counterfactual implication**: Without the Brennan Center's coordinated advocacy, AVR diffusion would have been slower and more fragmented. The 10-year diffusion from 0 to 24 states represents a successful policy campaign that still required nearly a decade to reach its current adoption level.

**Calibration for this framework**: This is the closest model to the framework's intended impact path. Like AVR, the framework provides evidence and structure that advocates in multiple institutional contexts can use independently. Unlike AVR, the framework is not tied to a specific legislative proposal — it is an analytical tool. This makes adoption faster (no legislative process required) but impact harder to measure (no binary adoption/non-adoption signal). The 10-year calibration suggests the framework should not expect its full institutional impact to be visible within Phase 1; Phase 1 is seeding the innovator and early adopter segments from which diffusion proceeds.

### Protect Democracy "Authoritarian Playbook" Series (2017-2020)

**Comparator**: Protect Democracy began publishing their series of anti-authoritarian policy frameworks in 2017. By 2019-2020, the series was being cited in academic work, congressional testimony, and major media. The "Presidential Norms Protection Act" framework developed by Protect Democracy was incorporated into actual legislative proposals within 18 months of publication.

**Counterfactual implication**: This is the fastest-diffusing comparable framework, achieving academic and legislative citation within 18-24 months. Key accelerant: Protect Democracy had institutional credibility, a staff team, and media relationships already in place before distribution.

**Calibration for this framework**: 18-24 months to first legislative citation is an optimistic but achievable target if Phase 1 early adopter engagement is strong. The Protect Democracy case also demonstrates that think tank citation (Tier B) precedes legislative citation (Tier 1) by 6-12 months — consistent with the measurement timeline in Part II.

### Without-Framework Counterfactual

Based on these four historical precedents, the baseline counterfactual — what would happen to democratic institutional response to the current crisis absent the framework — is:

- AG coalitions would continue litigating but with less analytical coordination across domain areas
- Think tanks would continue publishing individual domain analyses without a cross-domain synthesis
- Law schools would teach individual constitutional cases without a multi-domain integrative framework
- Policy reform proposals would continue to emerge but without a common vocabulary enabling rapid coordination

**The framework's marginal contribution is not origination of any single element but cross-domain synthesis and vocabulary standardization.** These are coordination goods, not invention goods. They are also the hardest category of contribution to measure directly, because coordination benefits are typically counterfactual (what did not happen because coordination occurred) rather than observable (what happened because the framework existed).

This is why the four attribution tests, particularly Test 4 (counterfactual), are necessary rather than optional. The framework's impact will be systematically underestimated if only positive observable outcomes are counted.

---

## Summary: Attribution Decision Protocol

When a potential Phase 1 impact event is identified, apply the following decision protocol:

1. **Run Test 3 first** (Timing-and-Contact): Is there a documented contact event before the outcome? If no, stop — the outcome is not framework-attributable by this methodology.

2. **If Test 3 is satisfied, run Test 1** (Vocabulary Marker): Does the outcome contain framework-specific vocabulary or evidence not present in the actor's prior work? If yes, attribution is credible. If no, proceed to Test 2.

3. **If Test 1 is ambiguous, run Test 2** (Structural Convergence): Does the outcome's analytical architecture converge with the framework's domain structure? If yes across 3+ domains, attribution is credible.

4. **Always run Test 4** (Counterfactual): Would this have happened anyway, at roughly this time, absent the framework? If yes (Category A), attribute to baseline. If plausibly accelerated (Category B), attribute as co-causation. If framework-enabled (Category C), attribute as primary causation.

5. **Record the attribution finding** in DISTRIBUTION_EXECUTION_LOG.md with: contact timestamp, outcome timestamp, tests satisfied, attribution category (A/B/C), confidence level (low/medium/high).

Attribution findings accumulated across all measurement windows constitute the Phase 1 Impact Assessment at Month 12 and are the primary input for the Phase 2 go/no-go decision.

---

*Sources: Diffusion of Innovations (Rogers, E.M., 1995) ([Stanford overview](https://web.stanford.edu/class/symbsys205/Diffusion%20of%20Innovations.htm)); Brennan Center AVR history and implementation dates ([Brennan Center](https://www.brennancenter.org/our-work/research-reports/history-avr-implementation-dates)); Model Penal Code history ([Wikipedia/ALI](https://en.wikipedia.org/wiki/Model_Penal_Code)); ABA Model Rules history ([ABA](https://www.americanbar.org/groups/professional_responsibility/publications/model_rules_of_professional_conduct/)); Overton policy citation methodology ([Overton](https://www.overton.io/overton-index)); Rogers diffusion applications ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC11247801/)); Advocacy Coalition Framework ([Springer](https://link.springer.com/chapter/10.1007/978-3-031-85554-2_1)).*
