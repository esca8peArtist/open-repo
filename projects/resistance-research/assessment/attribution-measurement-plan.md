---
title: "Attribution Measurement Plan — Phase 1 Distribution"
created: "2026-05-05"
session: "778"
status: "production-ready"
distribution_phase: "Phase 1 — all paths (A / A+37 / B)"
measurement_window: "May 2026 – May 2027"
companion: "assessment/phase-1-baseline-metrics.md"
cross_references:
  - post-distribution-impact-measurement-framework.md
  - measurement-and-iteration-framework.md
  - assessment/domain-37-baseline-metrics.md
  - domains/domain-37-baseline-metrics.md
purpose: >
  Defines the methodology for distinguishing "framework caused adoption"
  from "adoption would have happened anyway." Operationalizes four attribution
  tests, sector-specific protocols, time-based attribution windows, and
  failure mode diagnostics.
---

# Attribution Measurement Plan

**May 5, 2026**
**Applies to all distribution paths (A / A+37 / B)**

The central attribution problem: the policy domains this framework addresses are active. Courts are issuing rulings on prosecutorial weaponization, AGs are filing suits on election interference, think tanks are publishing on judicial independence, regardless of whether this framework exists. Any measurement system that counts "Domain 29 activity increased after distribution" without controlling for the ambient activity rate established in `phase-1-baseline-metrics.md` Section 3 will conflate cause and coincidence.

This plan operationalizes a four-test attribution structure that, taken together, can distinguish framework-caused adoption from ambient policy movement with reasonable confidence. No single test is sufficient; all four tests must be applied together, and findings should be treated probabilistically rather than as binary conclusions.

---

## Part 1: Attribution Methodology — Four-Test Structure

The four tests derive from the attribution logic in Session 718's impact analysis and the post-distribution tracking framework documented in `post-distribution-impact-measurement-framework.md`. They are presented here as an integrated methodology with clear implementation protocols.

### Test 1: Vocabulary Marker Test

**Logic**: If an organization adopts the framework's analysis, the most reliable signal is the use of the framework's specific vocabulary — vocabulary that did not exist in that organization's published work before distribution. Generic vocabulary ("election interference," "judicial independence") cannot be attributed to the framework; domain-specific compound phrases that appear in the framework but not in the pre-distribution literature can be attributed to it.

**Strong attribution vocabulary** (these phrases do not appear in the pre-distribution literature in this specific combination; their appearance post-distribution is highly diagnostic):
- "81 percent false positive SAVE" or "24,000 incorrectly flagged" in voter roll context — Domain 37 vocabulary marker
- "22-case retaliatory prosecution pattern" or "prosecutorial weaponization taxonomy" — Domain 29 vocabulary marker
- "Albus cross-jurisdictional election prosecution" combined with election security framing — Domain 37 vocabulary marker
- "law enforcement OLC memo theory" applied to the Venezuela/war powers analysis — Domain 28 vocabulary marker
- "ICE at polling places" combined with "no statutory authority" — Domain 37 vocabulary marker
- "EI-ISAC elimination" combined with "election security coordination void" — Domain 37 vocabulary marker
- "Domain [1-37]" by name and number in policy or legal document — strongest possible marker (no other document uses this taxonomy)

**Weak attribution vocabulary** (these phrases were in pre-distribution literature; their appearance post-distribution is necessary but not sufficient for attribution):
- "democratic backsliding" — ambient; appears in hundreds of pre-distribution documents
- "judicial independence" reform — ambient
- "CISA funding cuts" — ambient (Government Executive, Nextgov covered this in April 2026)
- "prosecutorial weaponization" without the 22-case taxonomy — ambient

**Protocol**: Run the strong attribution vocabulary queries monthly (documented in `phase-1-baseline-metrics.md` Section 1 measurement protocol). Any document that uses three or more strong attribution vocabulary markers is a confirmed adoption event. A document using one marker plus citing the framework by name or Gist URL is a confirmed adoption event. A document using one marker without citation is a possible adoption event — investigate whether the framing emerged independently or post-dates distribution to the source organization.

### Test 2: Structural Convergence Test

**Logic**: If an organization adopts the framework's analytical structure — not merely its vocabulary, but the way it organizes a set of facts, the specific mechanisms it identifies, the comparative evidence it uses — that structural convergence is strong evidence of adoption even without explicit citation. Policy documents routinely incorporate analytical frameworks without attribution.

**What structural convergence looks like**:
- An AG brief that organizes its election interference argument around exactly five mechanisms (matching Domain 37's five-mechanism taxonomy) where prior AG filings used different categorizations
- A law review article that uses the same comparative constitutional framework (parallel court-stacking examples from Hungary, Turkey, and Israel with the same years and methodological frame as Domain 6) without attribution
- A think tank report that uses the Domain 29 three-category retaliatory prosecution taxonomy (opposition prosecution, protest suppression, institutional dismantling) where the think tank's prior publications used different categorizations

**Protocol**: For each confirmed strong-vocabulary adoption event (from Test 1), read the surrounding document for structural convergence markers. Assess whether the organizational logic of the document mirrors the framework's domain structure. Code each event as: vocabulary-only, vocabulary-plus-structure, or structure-without-vocabulary. The last category requires closest scrutiny — it may indicate independent parallel development (which is itself evidence of the framework's analytical validity) or silent adoption (which is operationally equivalent to attribution for measurement purposes).

**Structural convergence is not plagiarism — it is success**. The goal of the framework is to shape institutional analysis, not to receive citation credit. An AG brief that silently adopts Domain 37's five-mechanism structure and uses it to win an injunction against the DOJ voter roll program is the highest-value outcome in this measurement system.

### Test 3: Timing-and-Contact Test

**Logic**: The causal chain from distribution to adoption has a temporal signature. Organizations that received the framework and subsequently published analysis that uses framework vocabulary or structure are presumptively attribution events. Organizations that published similar analysis without having received the framework are ambient events.

**The causal test**: For any suspected adoption event (from Tests 1 or 2), determine:
1. Was this organization in the distribution sequence?
2. If yes, when did it receive the framework?
3. What is the time elapsed between receipt and the observed adoption signal?
4. Is the time elapsed consistent with the realistic adoption timeline for this sector? (State AGs: 4–8 weeks; think tanks: 6–10 weeks; law schools: 8–16 weeks; media: 2–4 weeks)
5. Did anyone at the organization confirm (in a response email or conversation) that they received and read the materials?

**Protocol**: Maintain a contact log that records the date each organization received materials and the date any adoption signal was observed. Calculate the elapsed time. Events where the elapsed time falls within the sector's realistic adoption timeline AND the organization is in the distribution list AND the document uses strong attribution vocabulary constitute confirmed attribution events. Events where any one of these three conditions is not met are possible attribution events requiring additional investigation.

**The contact-log is the most important attribution document in this system.** Date-stamp every outreach event. Without this log, the timing-and-contact test is impossible to run.

### Test 4: Counterfactual Baseline Test

**Logic**: The most rigorous attribution test asks whether the observed adoption would have occurred without the framework. For most outcomes, this cannot be tested directly. The pre-distribution baseline established in `phase-1-baseline-metrics.md` Section 3 is the closest approximation — if Domain 37 activity was tracking at 12–18 events/month before distribution, and it increases to 20–28 events/month after distribution (a 40–60% increase), some portion of that increase may be attributable to the framework, but the counterfactual question — how many of those events would have occurred without the framework — remains open.

**Two counterfactual proxies**:

*Proxy 1 — Control group comparison*: Identify domains with comparable activity levels and comparable external policy environments that were NOT specifically targeted in the distribution sequence. If Domain 29 (prosecutorial weaponization) receives heavy distribution targeting and shows a 50% activity increase, while Domain 20 (Economic Concentration / Antitrust) receives minimal targeting and shows a 10% activity increase over the same period, the differential increase is attributable evidence. It is not proof — both domains may have had different external drivers — but the comparison narrows the attributable range.

Control group candidate domains (low-distribution-priority, comparable policy activity level):
- Domain 20 (Economic Concentration / Antitrust) — active but not a primary distribution target
- Domain 4 (Digital Government Infrastructure) — lower policy activity, not targeted at Tier 1 contacts
- Domain 22 (Reparations / Racial Justice) — important but not a primary Tier 1 sector match

*Proxy 2 — Natural experiment: hard deadline domains vs. optional domains*: Domains 19f, 25, and 37 have hard external deadlines (May 1 WPR non-compliance, June 12 FISA expiration, November 3 Election Day). These domains will show policy activity spikes independent of the framework as their deadlines approach. If the framework matters, it should show up as quality differences — is the policy response more analytically sophisticated, more specifically targeted to the documented mechanisms, more legally precise — rather than merely as activity volume increases. Compare the analytical structure of policy responses in hard-deadline domains versus optional domains; if hard-deadline domains show both higher volume AND higher analytical sophistication while optional domains show only modest volume increases with similar analytical quality, that pattern is consistent with framework adoption rather than ambient deadline-driven activity.

**Protocol**: At Month 3 and Month 6, run a structured comparison of policy activity across (a) primary distribution target domains, (b) secondary target domains, and (c) control group domains. Calculate the ratio of framework-vocabulary citations per unit of policy activity. If primary targets show 10:1 ratio (10 vocabulary-marker events per 100 policy activity events) while control domains show 0.5:1, that differential is attributable to the framework.

---

## Part 2: Sector-Specific Attribution Protocols

Each sector has distinct institutional logic, distinct adoption timelines, and distinct evidence signals. Generic vocabulary monitoring is insufficient; each sector requires a tailored detection protocol.

### State Attorneys General

**Baseline established**: 22-AG coalition active on election interference; 0 AGs currently using framework vocabulary as of May 5, 2026.

**What adoption looks like**:
- Supplemental brief or amicus filing in an active case (Callais v. Landry appellate track; DOJ voter roll suits; 24-state election EO challenge) that uses Domain 37's specific five-mechanism taxonomy or Domain 29's retaliatory prosecution taxonomy
- NAAG coalition letter that uses framework vocabulary in describing the constitutional basis for state election sovereignty (Domain 33's simultaneous six-state action map, or Domain 37's pre-certification legal framework)
- State AG press release announcing new litigation that cites the framework's legal theory for a mechanism not previously covered in AG coalition strategy (e.g., Section 3 enforcement of Domain 37's Olsen/Albus/Harvilicz analysis)

**What does NOT constitute attribution to this framework** (ambient AG activity):
- Filing new suits on election interference generically without using framework vocabulary
- Coalition letters using standard anti-commandeering or Article II election clause arguments without the framework's specific application to 2026 mechanics
- Any AG action that was publicly announced as imminent before distribution date

**PACER monitoring protocol**: Run the following CourtListener / RECAP keyword searches monthly:
- `"five mechanisms" election interference`
- `"SAVE" "false positive" "81" voter`
- `"Albus" election jurisdiction`
- `"ICE" "polling place" "no authority"`
- `"EI-ISAC" election security coordination`

**Attribution confirmation threshold**: Two of the five domain-specific vocabulary markers appearing in a single brief, combined with filing date post-distribution by an organization in the contact sequence, constitutes a confirmed AG adoption event.

### Law Schools and Legal Academia

**Baseline established**: 0 law school publications or clinic materials using framework vocabulary as of May 5, 2026.

**What adoption looks like**:
- Law review article or student note that cites the framework by name or Gist URL, or that uses the framework's domain structure to organize its analysis
- Law clinic course syllabus that includes the framework document as assigned reading (typically detectable only through direct contact confirmation or student posts on public forums)
- Law review symposium invitation that frames its theme using framework domain taxonomy
- Amicus brief filed by a law school clinic (Georgetown ICAP, Harvard DROL, BU Legislative, Stanford Immigrants' Rights) that uses framework vocabulary in its constitutional argument

**Fastest law school adoption pathways** (from `post-distribution-impact-measurement-framework.md` Part I):
- Domain 6 (Judicial Independence) — dense existing constitutional law infrastructure; comparative methodology is standard format
- Domain 28 (War Powers / Venezuela) — Just Security publication as academic vector; national security law faculty
- Domain 29 (Prosecutorial Weaponization) — live cases with law school clinic dockets; SPLC case creates direct organizational incentive
- Domain 37 (Election Interference) — voting rights faculty; Brennan Center relationships create rapid entry point

**Westlaw / Lexis monitoring protocol** (quarterly, institutional access required):
- `"democratic renewal proposal"` — framework citation
- `"35-domain" /10 (framework OR proposal OR research)` — structural reference
- `"SAVE" /3 "false positive" /5 voter 2026` — Domain 37 vocabulary marker
- `"Albus" /5 "cross-jurisdictional" election` — Domain 37 specific marker

**Attribution confirmation threshold**: Any law review article or clinic brief published after distribution date that uses the framework by name or uses two or more strong attribution vocabulary markers from the same domain chapter. Note author affiliation, date, and how the framework influenced the analytical structure.

### Think Tanks and Policy Organizations

**Baseline established**: 0 think tank publications using framework vocabulary as of May 5, 2026. Brennan Center, Brookings, CAP, Just Security, Protect Democracy, EPI all documented in pre-distribution state in `phase-1-baseline-metrics.md` Section 1.

**What adoption looks like**:
- Brennan Center election protection publication that uses Domain 37's five-mechanism structure to frame the federal election interference threat (the Brennan Center's current "Fight to Protect the Midterms" series uses different framing — any shift to Domain 37's taxonomy is an adoption signal)
- Just Security piece on Venezuela/war powers that cites the OLC memo analysis from Domain 28 (Just Security already covers the Venezuela operation; adoption is signaled by use of the framework's specific OLC memo internal-contradiction analysis, not general war powers coverage)
- EPI publication on labor rights that incorporates Domain 17's sectoral bargaining analysis or co-determination framework (EPI already covers these topics; adoption is signaled by use of the framework's specific comparative international evidence base — the German Mitbestimmung or Swedish model evidence)
- Protect Democracy retaliatory action publication that incorporates Domain 29's three-category taxonomy (opposition prosecution, protest suppression, institutional dismantling) in place of its current case-by-case documentation approach

**Domain 37 as fastest think tank entry point**: The seven quantified baselines in `domains/domain-37-baseline-metrics.md` are directly usable in think tank publications and will not age rapidly. Think tanks will adopt Domain 37 evidence first because it provides data they cannot generate quickly themselves. Any Brennan Center or Protect Democracy publication that cites the DOJ voter roll case count (24 + DC), the election denier appointment headcount (11+), or the CISA election security budget figures in the specific quantified format documented in Domain 37's baselines is a presumptive adoption event.

**Web monitoring protocol** (set as Google News alerts):
- `site:brennancenter.org "five mechanisms" OR "SAVE false positive" OR "EI-ISAC"`
- `site:justsecurity.org "OLC memo" Venezuela "internal contradiction" 2026`
- `site:protectdemocracy.org "three categories" prosecution OR "22 cases" retaliatory`
- `site:epi.org "co-determination" OR "sectoral bargaining" Germany model`

**Attribution confirmation threshold**: Think tank publication post-distribution that uses strong attribution vocabulary from the relevant domain AND was published by an organization in the distribution sequence. The threshold is lower than for AGs (one strong vocabulary marker is sufficient for think tanks, given that think tanks cite sources more readily and attributably than litigation filings).

### Academic Researchers

**Baseline established**: 0 academic citations of framework vocabulary in SSRN or Google Scholar as of April 30, 2026.

**What adoption looks like**:
- SSRN preprint or conference paper that cites the framework by Gist URL or by name ("Democratic Renewal Proposal, 35-domain framework")
- Conference presentation (APSA, law society annual meetings, PolSci regional meetings) that uses domain taxonomy as its analytical frame
- Co-author inquiry from a researcher who encountered the framework and wants to develop one domain into a journal article
- Citation in a forthcoming book chapter (detectable only via Google Scholar after publication)

**Realistic timeline for academic citations**: 6–18 months from distribution to publication (GPPI "Whose Bright Idea Was That" 2023 review of think tank citation timelines; the policy-to-academic pipeline operates at publication cycle speed). The Phase 1 measurement window should not expect more than 1–3 confirmed academic citations; 5+ would be exceptional. Month 6-12 is the realistic window for initial academic visibility; Month 12-24 for meaningful citation depth.

**Google Scholar alert protocol**:
- `"democratic renewal proposal"` — should return 0 pre-distribution; any post-distribution hits are adoption events
- `"35-domain democratic"` — same
- `author citations to framework Gist URL` (manually trackable via GitHub Gist view statistics)

**Attribution confirmation threshold**: Any SSRN or Google Scholar indexed paper published after distribution date that cites the framework by name or URL. Note author, institution, domain cited, and how the citation is used (supportive, critical, or as background).

### Media and Journalism

**Baseline established**: 0 framework-specific media citations; 40–60 ambient election interference articles/month; 15–25 prosecutorial weaponization articles/month as of April 2026.

**What adoption looks like**:
- National or specialist outlet article that cites the framework document directly (links to Gist) or quotes from it
- Journalist who uses domain-specific vocabulary in coverage that post-dates their receipt of framework materials
- Op-ed by a Batch 1-3 contact (Goodman, Weiser, Chenoweth, Bassin, Elias) that references the framework in the context of their domain expertise
- Letters from an American, Popular Information, or similar high-reach newsletter that introduces the framework to their subscriber base

**Organic vs. planted citation distinction**: This sector requires distinguishing citations that result from direct outreach (planted) from citations by journalists who discovered the framework through organic search, academic citation, or referral from an organization that adopted it (organic). Organic citations have higher signal value for establishing the framework's credibility in the broader policy ecosystem. Track source of each media citation: Was this journalist in the media outreach sequence? Did they contact us first? Did they encounter the framework through an organization that adopted it (third-order signal)?

**Google News monitoring protocol** (set as alerts on distribution day):
- `"democratic renewal proposal"` — should return 0 pre-distribution; any hit is an adoption event
- `"35-domain" democratic framework` — same
- `"Domain 37" election 2026` — same
- `"SAVE false positive" "81" voter 2026` — high-specificity vocabulary marker; pre-distribution baseline is 2–4/month

**Attribution confirmation threshold**: Any media article post-distribution that links to the framework Gist, quotes from it, or uses three or more strong attribution vocabulary markers. Note outlet, author, date, framing (favorable/neutral/critical), and whether the journalist was in the media outreach sequence.

---

## Part 3: Time-Based Attribution Windows

Attribution signals have different weights depending on when they appear relative to distribution date. Early adoption signals are more directly attributable (less time for ambient causes to explain the adoption); late adoption signals require more scrutiny of the causal pathway.

### Window 1: Weeks 1-2 Post-Distribution (Vocabulary Awareness Phase)

**What is observable**: Open rates, initial replies, Gist views, first-round contact log entries.

**What is attributable in this window**: Only email engagement signals. Any institutional output (publications, briefs, citations) that appears within 2 weeks of distribution was almost certainly in production before distribution; it cannot be attributed to the framework.

**Exception**: A Just Security piece can be published within 48–96 hours. If a Just Security editor receives Domain 28 materials on Day 1 and publishes a piece on Day 4 that uses framework-specific vocabulary, that is a confirmed near-instant adoption event. Just Security is the only organization in the distribution list with a fast enough publication cycle to produce attributable output in Week 1-2.

**Measurement action**: Log all email opens, replies, and Gist views. Record first substantive response date per organization. Do not claim any institutional output in this window as an attribution event without confirming (a) the organization received materials before the publication was submitted, and (b) the publication uses strong attribution vocabulary.

### Window 2: Weeks 3-4 Post-Distribution (Engagement Phase)

**What is observable**: Pattern of substantive responses, domain-specific questions, requests for additional materials, referral offers.

**What is attributable in this window**: Email engagement depth. Institutional outputs from Very fast-cycle organizations (Just Security, active litigation teams that file within days of receipt). State AG supplemental brief filings where the brief was filed within 3-4 weeks of receipt and uses strong attribution vocabulary.

**Measurement action**: Assess reply pattern by sector. Are replies generic (acknowledgment) or substantive (domain-specific questions, operational asks)? The ratio of substantive to acknowledgment responses is the primary Week 3-4 attribution signal — it indicates whether the framework is being read operationally or filed away.

**Attribution threshold for this window**: An AG brief with strong attribution vocabulary filed within 3-4 weeks of distribution is a confirmed attribution event if (a) the AG office is in the distribution sequence and (b) the brief uses mechanisms not present in the AG's prior filings.

### Window 3: Month 2-3 Post-Distribution (Substantive Adoption Phase)

**What is observable**: Think tank publications, law review submissions, organizational policy memos, additional AG filings, media citations from recipients.

**What is attributable in this window**: Institutional outputs from think tanks (6-10 week production cycle), advocacy organizations (2-3 month campaign integration), and early academic pre-prints. This is the window when the primary attribution tests (Tests 1-4 in Part 1 of this document) become fully operational.

**Measurement action**: Monthly policy momentum count per domain (documented in `phase-1-baseline-metrics.md` Section 3 protocol). Monthly vocabulary marker search (Section 1 protocol). Monthly contact log review for new second-order signals (has any Batch 1-3 contact referred a new organization to the framework?).

**Attribution threshold for this window**: Think tank publication using strong attribution vocabulary from a domain where the think tank is in the distribution sequence, published 6-12 weeks after receipt. State AG brief using framework structure in a filing against a federal defendant on election, prosecutorial, or war powers grounds. These are the highest-probability attribution events in Month 2-3.

### Window 4: Month 4-6 Post-Distribution (Diffusion Phase)

**What is observable**: Citations from organizations NOT in the original distribution sequence. Law review articles. Organic media citations. Organizations contacting us (rather than us contacting them) requesting the framework.

**What is attributable in this window**: Second-order diffusion — evidence that organizations outside the original distribution list are using the framework because a Tier 1 adopter shared it with them. This is the most important adoption signal in the entire measurement system, because it indicates the framework has achieved self-sustaining circulation.

**Measurement action**: For any adoption event from an organization not in the distribution sequence, investigate the causal pathway: How did they encounter the framework? Was it through a Tier 1 adopter (strong evidence of cascade)? Through organic search (evidence of public visibility)? Through an academic citation (evidence of credibility establishment)?

**Attribution threshold**: Any adoption event from an organization not in the distribution sequence that can be traced to a Tier 1 adopter via the "who referred you?" question in the contact log. This confirms the cascade model and is the most rigorous evidence that the framework is generating independent institutional momentum.

### Window 5: Month 6-12 Post-Distribution (Institutionalization Phase)

**What is observable**: Framework vocabulary appearing in testimony, legislation, or court opinions. Academic citations in published (not just preprint) articles. Organizational strategy documents referencing the framework. Follow-on frameworks or analyses that build explicitly on the proposal.

**What is attributable**: The framework is now part of the institutional vocabulary of the policy area. Attribution at this stage is diffuse — the framework has become one of many inputs to institutional discourse — but the vocabulary marker test still applies. Any policy document that uses the specific compound vocabulary established in Part 1, Test 1, was shaped (directly or through the cascade) by this framework.

**Measurement action**: Overton.io policy citation database search (register now; set reminder at Month 4, 8, and 12 per `post-distribution-impact-measurement-framework.md` Part II). PACER amicus brief search for framework vocabulary. Congress.gov full-text testimony search for domain-specific vocabulary.

---

## Part 4: Failure Mode Diagnostics

**Core question**: If Phase 1 adoption stalls, is the failure in the delivery layer, the engagement layer, or the adoption layer? These three failure modes have different fixes, and misdiagnosing one as another wastes resources.

### Delivery vs. Engagement Failure Diagnostic

If Week 3-4 signals are weak, run this diagnostic before assuming engagement failure:

**Delivery check**:
- Is the email open rate below 25%? (If yes: deliverability failure — fix email platform, verify addresses, switch to LinkedIn InMail)
- Are Gist views below 100 after 14 days? (If yes: the Gist URLs are not being clicked — either the email is not being opened, or the CTA is unclear — rewrite the ask)
- Are there zero replies of any kind from Batch 1 after 7 days? (If yes: confirm emails were actually sent from a deliverable address; verify one address manually)

**Engagement check**:
- Is the open rate above 35% but the reply rate below 3%? (If yes: engagement failure — the document was opened but the ask was not compelling — tighten the ask to one domain-specific question)
- Are replies all acknowledgment-only with no domain specificity? (If yes: the recipients are being polite but the framework is not operationally relevant to their current work — create domain-specific memos for their active dockets)
- Are Gist views above 200 but zero downstream citations? (If yes: the framework is being read but not shared — the document may be perceived as too long or too general — create a five-page executive summary optimized for institutional distribution)

### Adoption Failure by Sector

If Month 3 signals are weak despite strong Week 3-4 engagement, investigate by sector:

**If AGs are silent**: Is it delivery failure (no AG office received materials)? Or adoption failure (received but not operationally useful)? Fix: Identify whether any AG policy counsel explicitly responded; if not, secure a warm introduction from a law school clinic contact (Georgetown ICAP, Harvard DROL) who has existing AG relationships. The cold-to-warm conversion multiplier is 3-5x.

**If think tanks are silent**: Is the framework arriving as competition (another organization in "our" space) rather than as a tool (something we can use for our work)? Fix: Reframe the outreach as "I would like your feedback on whether this analysis is accurate" rather than "I want to share this research with you." Think tank research directors respond to peer feedback requests; they do not respond to unsolicited research submissions.

**If law schools are silent**: The academic cycle is slow. Law school silence at Month 3 is expected; at Month 6 it is meaningful. If Month 6 is still silent: contact course directors directly with a specific ask — "Would one chapter of this proposal work as a seminar reading for [specific course]?" The ask must be framed around their course needs, not the framework's breadth.

**If adoption is sector-specific** (e.g., strong in AGs, weak in think tanks): Investigate whether the issue is domain-alignment or format-alignment. AGs work in briefs; the framework's constitutional argument structure maps onto brief format naturally. Think tanks work in policy memos; the framework's domain chapters are not policy memo format. Fix: Translate the three highest-relevance domains into think tank brief format (executive summary + evidence + policy recommendations in <8 pages) and resubmit to think tank contacts with a format note.

**If adoption is issue-specific** (clusters by domain topic, not sector): This is the most informative failure mode because it tells you which topics have reached their institutional audiences and which have not. If Domains 28-29 (war powers, prosecutorial weaponization) are generating strong adoption while Domain 31 (healthcare / Medicaid) is not, the issue may be audience mismatch — the healthcare policy community is not in the current Tier 1 contact list. Fix: Identify the healthcare policy community's specific Tier 1 institutions (Urban Institute, CBPP, Families USA) and create a healthcare-specific distribution sequence.

### Quick Pivot: Day 45 Decision Tree

If Day 45 shows zero domain-specific adoptions (no brief, no publication, no citation using strong vocabulary markers):

1. Verify delivery (are emails reaching inboxes? Are Gist URLs working?). If delivery is broken, fix and re-send before drawing any conclusions.

2. If delivery is working: Create domain-specific memos for the top 3 high-relevance domains (Domain 29 for SPLC and prosecutorial weaponization orgs; Domain 37 for election protection orgs; Domain 6 for judicial independence orgs). Format as policy memos, not proposal chapters. 2-4 pages maximum.

3. Re-initiate contact with Batch 1 recipients with a specific operational ask: "The [domain name] analysis I shared maps directly onto your [current filing / pending publication / upcoming testimony]. Would a shorter version oriented specifically for [that purpose] be useful?"

4. If Day 60 shows zero domain-specific adoptions after the operational ask: Initiate the bridge-node strategy. Contact Erica Chenoweth (Harvard Kennedy School) and Ryan Goodman (Just Security) with a direct request to publish a piece using one domain chapter. Their publications create the social proof that makes all subsequent outreach to other institutions 3-5x more effective.

The Day 45 pivot is not a failure declaration. It is a mid-course correction in response to data. The 90-day window remains the primary assessment point; Day 45 is the last opportunity for in-flight adjustments that can materially affect Month 3 outcomes.

---

*Companion document: `assessment/phase-1-baseline-metrics.md`*
*Measurement framework: `post-distribution-impact-measurement-framework.md`*
*Domain 37 baselines: `assessment/domain-37-baseline-metrics.md` and `domains/domain-37-baseline-metrics.md`*
*Contact log: `BATCH_1_CONTACT_LOG.md` and `DISTRIBUTION_EXECUTION_LOG.md`*
*Attribution baselines locked: May 5, 2026*
*First attribution review: 30 days post-distribution launch*
*Full attribution assessment: 90 days post-distribution launch (Month 3)*
