---
title: "Tier 1 Effectiveness Measurement Framework"
project: cybersecurity-hardening
created: 2026-05-05
revised: 2026-05-05
status: production-ready
cohort-size: 33
sectors: [digital-rights, academic-cybersecurity, researcher-communities, journalists]
depends-on:
  - tier-1-success-metrics-framework.md
  - tier-1-feedback-collection-protocol.md
  - post-distribution-impact-tracker.md
---

# Tier 1 Effectiveness Measurement Framework

**Lead finding**: The most important early signal is not how many organizations acknowledged receipt — it is whether the corpus generated a question. A question means someone read past the subject line and encountered something they needed to act on. An acknowledgment without a question is Stage 0. A question is Stage 1. The framework lives or dies at the boundary between those two.

**Cohort**: 33 organizations across four sectors: digital rights organizations, academic cybersecurity programs, researcher communities, and journalist organizations.

---

## 1. What "Success" Means for Each Sector

Success is not uniform across the four Tier 1 sectors. Digital rights organizations, academic cybersecurity programs, researcher communities, and journalist organizations have different institutional rhythms, different output expectations, and different observable adoption signals. Applying a single adoption rate threshold misreads the signal in both directions.

**Sector distribution (approximate)**: ~12 digital rights organizations, ~8 academic programs, ~7 researcher communities, ~6 journalist organizations. Total: 33.

**Note on prior sector taxonomy**: Earlier planning documents used a 1A/1B/1C taxonomy (immigration legal aid, community-based organizations, mutual aid networks) corresponding to a smaller 12-organization direct-service cohort. That cohort is a separate campaign layer. This framework applies to the current 33-organization amplifier cohort. Do not mix thresholds across cohorts.

### Behavioral Thresholds: Read, Understood, Implemented

Before defining sector-specific success, define the behavioral chain the corpus is trying to trigger. All three steps must occur for the corpus to have achieved its purpose. Each is separately observable.

**Read** — Someone at the organization reviewed the corpus beyond the subject line and Gist preview.

Observable indicators (any one sufficient):
- Reply references a specific section, term, or claim from the corpus body
- Reply asks a question that could only arise from reading (e.g., "What happens if a client already submitted a DROP request before the broker processing deadline?")
- Bitly click followed by a reply within 72 hours (indicates the click was a genuine read, not a browser preview)

**Understood** — The reader has internalized the threat model's logic and the countermeasures' purpose, not just their steps.

Observable indicators (any one sufficient):
- Reply describes the ELITE risk in the organization's own language ("So ICE is building targeting scores from commercial databases without subpoenas?")
- Reply identifies the corpus's most distinctive contribution relative to other resources ("We haven't seen the DROP platform documented this specifically anywhere else")
- Reply asks a question that extends the threat model to their specific population ("Does the address confidence scoring affect clients at shelter addresses?")
- Vocabulary migration: organization uses corpus-origin terms in a public output within 60 days

**Implemented** — The organization or its clients have taken at least one action described in the corpus.

Observable indicators (any one sufficient):
- Organization confirms guiding clients through Part 0 data broker opt-outs (self-report at Day 90 follow-up)
- Organization confirms walking California clients through the AB 60 → DROP platform pathway
- Corpus appears on an organization's resource page, intranet, or practitioner toolkit
- Organization schedules or conducts a workshop using the corpus as the basis

### Sector-Specific Success Definitions

**Sector A: Digital Rights Organizations**
(EFF, CDT, Access Now, Privacy International, EPIC, STOP, Tor Project, Fight for the Future, Mozilla Foundation, Restore the Fourth, CDD, Demand Progress — ~12 organizations)

Digital rights organizations receive a high volume of threat model submissions and security research. Their adoption signal is publication or citation, not internal use. Success is measured at the "Understood" level by Day 30 (they can describe the ELITE threat model accurately) and at the "Implemented" level by Day 90 (they publish, cite, or share the corpus with their own audience).

| Timeframe | Minimum Success | Strong Signal | Outstanding |
|-----------|----------------|---------------|-------------|
| Day 30 | ≥3 of 12 organizations at "Read" level | ≥5 at "Read"; ≥1 at "Understood" | ≥1 org circulates internally to policy team |
| Day 90 | ≥2 organizations at "Understood" | ≥1 citation, link, or publication recommendation | EFF or CDT links to corpus in any output |
| Day 180 | ≥1 corpus citation in a published policy output | ≥3 organizations have shared externally | Corpus incorporated in a published surveillance threat brief |

Timeline note: Digital rights organizations with publishing operations (EFF, CDT, Privacy International) may take 60–90 days to formally publish a piece citing new research — their review process is deliberate. However, informal sharing within the organization (staff Slack, internal security briefings) happens within 1–2 weeks of reading. The informal sharing signal may be invisible; look for domain-specific follow-up questions as a proxy.

**Sector B: Academic Cybersecurity Programs**
(CMU CyLab, UC Berkeley CLTC, MIT CSAIL, UW Security Lab, and similar — ~8 programs)

Academic adoption follows a different timeline: individual faculty engage first, curriculum integration or research citation comes months later. Success is measured at "Understood" level (faculty can describe the corpus's contribution to existing knowledge) and at "Implemented" level when the corpus enters a syllabus, reading list, or published research citation.

| Timeframe | Minimum Success | Strong Signal | Outstanding |
|-----------|----------------|---------------|-------------|
| Day 30 | ≥2 of 8 programs at "Read" level | ≥3 at "Read"; faculty follow-up question received | Corpus shared with a research group internally |
| Day 90 | ≥1 faculty engagement at "Understood" level | ≥1 program indicates curriculum interest | Course syllabus or reading list inclusion |
| Day 180 | ≥1 research citation or thesis reference | ≥2 programs integrating corpus materials | Published academic paper or conference presentation citing corpus |

Timeline note: Academic institutions move on semester timelines. A corpus shared in May 2026 can plausibly reach a Fall 2026 syllabus if a faculty member is convinced by August. The academic adoption signal to watch is a question from a faculty researcher about methodology, sourcing, or extension — this signals they are considering using the corpus in their own work.

**Sector C: Researcher Communities**
(Independent security researchers, digital forensics practitioners, privacy engineers, civil society technologists — ~7 communities/individuals)

Researcher communities have the fastest adoption speed for technical content and the strongest norm of sharing within trusted networks. Success is measured at "Understood" and "Implemented" levels simultaneously — researchers who understand the corpus will implement its recommendations and share it in their networks without prompting.

| Timeframe | Minimum Success | Strong Signal | Outstanding |
|-----------|----------------|---------------|-------------|
| Day 7 | ≥2 of 7 contacts at "Read" level | ≥3 at "Read"; ≥1 domain-specific question | Corpus shared in a researcher Signal group or mailing list |
| Day 30 | ≥2 contacts at "Understood" | Technical critique or extension request received | Corpus appears in a researcher-operated resource list |
| Day 90 | ≥1 contact at "Implemented" (recommends to their network) | Corpus forked, extended, or cited in a researcher's own project | Formal audit, technical review, or verification published |

Timeline note: Security researcher communities have horizontal sharing norms similar to mutual aid networks — high trust, fast propagation. The key trust node in each community is a 1–3 person authority figure whose recommendation carries the whole community. Identify which researcher contacts have that trust-node role before sending; their engagement or non-engagement explains most of the variance in this sector's outcomes.

**Sector D: Journalist Organizations**
(FPF, IRE, RCFP, and individual security-beat journalists at major outlets — ~6 organizations)

Journalist adoption is measured differently from other sectors. "Implemented" for journalists means: (1) using the corpus's OPSEC guidance with their own sources, or (2) citing the corpus in reporting on ICE surveillance or ELITE, or (3) distributing the corpus through their own journalist security training infrastructure.

| Timeframe | Minimum Success | Strong Signal | Outstanding |
|-----------|----------------|---------------|-------------|
| Day 14 | ≥1 of 6 organizations at "Read" level | ≥2 at "Read" | A beat journalist requests permission to cite the ELITE threat model |
| Day 30 | ≥2 organizations at "Read" | ≥1 organization incorporates into journalist security training | Published article cites corpus as source |
| Day 90 | ≥1 organization at "Understood" | ≥2 organizations at "Understood"; corpus in a journalist training toolkit | Corpus cited in published investigative journalism on Palantir/ICE |

Timeline note: Journalist adoption has two distinct failure modes. First: the corpus is treated as a tip that requires reporter verification before use — in this case, engagement may not be visible until publication. Second: security editors want to recommend the corpus internally but cannot do so without confirmation that the underlying threat model is vetted. The legal-practitioner confirmation signal (Section 3, Signal 4) is specifically designed to address this bottleneck.

---

## 2. Quantified Success Targets

These are the campaign-level success thresholds — not per-organization, but across the full 33-organization Tier 1 cohort. Percentages are given alongside raw counts because the cohort is large enough for percentages to be meaningful.

### Day 30 Thresholds

| Metric | Below Threshold | On Track | Strong |
|--------|----------------|----------|--------|
| Reply rate (any reply) | <15% (fewer than 5 of 33) | 25–35% (8–12 of 33) | ≥40% (13+ of 33) |
| Stage 1+ rate among replies | <30% of replies | 50–60% of replies | ≥70% of replies |
| Referral factor | 0 new contacts | ≥4 new warm contacts | ≥8 new warm contacts |
| Bitly incremental clicks | <20 beyond initial opens | 35–60 | 80+ |
| Sector coverage (≥1 reply per sector) | 0–1 sectors covered | 2–3 sectors covered | All 4 sectors have ≥1 Stage 1+ reply |

### Day 90 Thresholds

| Metric | Below Threshold | On Track | Strong |
|--------|----------------|----------|--------|
| Organizations at "Implemented" | 0 | ≥4 of 33 (12%) | ≥8 of 33 (24%) |
| Organizations at "Understood" | <4 | ≥8 of 33 (24%) | ≥12 of 33 (36%) |
| External citations (published output, link, resource list) | 0 | ≥2 documented | ≥5 documented |
| Named gaps in feedback | 0 | ≥3 distinct gaps logged | ≥6 gaps with sector attribution |
| Referral factor | <1.0 | ≥1.5 (50 total contacts) | ≥2.0 (66 total contacts) |
| Vocabulary migration events | 0 | ≥2 documented | ≥5 documented |
| Threat model accuracy confirmations | 0 | ≥2 | ≥4 from practitioners with operational visibility |

### Day 180 Thresholds

| Metric | Below Threshold | On Track | Strong |
|--------|----------------|----------|--------|
| Organizations with changed internal practice or publication | 0 | ≥5 of 33 (15%) | ≥10 of 33 (30%) |
| Self-reported adoption rate | <10% of org contacts confirm use | ≥20% confirm use | ≥30% confirm use |
| Institutional citations (published brief, syllabus, training curriculum, toolkit) | 0 | ≥3 | ≥7 |
| Phase 3 referrals generated (contacts for next distribution tier) | <5 | ≥15 | ≥30 |
| Journalist coverage or citation | 0 | ≥1 published piece | ≥3 published pieces or mentions |

**Calibration note on the 20% target**: "40%+ of recipients report framework matches threat model" (one recommended Phase 2 criterion) translates to ≥13 of 33 organizations confirming threat model accuracy. A more conservative threshold — ≥7 confirmations (21%) — is "On Track" and sufficient for a Phase 2 launch if threat model integrity checks pass. Do not wait for the Strong threshold before launching Phase 2; the 40% bar is aspirational, not required.

**Calibration note on domain-specific adoption signals**: "5+ Domain XY adoption requests" — at 33 organizations, 5 domain-specific requests (15% of cohort) in a single request category is a strong indicator that a missing section is required before Phase 2. Track not just that requests came in, but which domain (device hardening, messaging, DROP platform, post-detention scenarios) they cluster in.

---

## 3. Early Adopter Signal Detection

Early adopter behavior in the first 30 days is the strongest available predictor of Phase 2 adoption success. The following signals, when present, predict that the corpus will achieve wide adoption within 6 months. When absent, they predict stall.

### Signal 1: Vocabulary Migration (Days 1–30)

Public outputs from a Tier 1 contact use terminology that originated in the corpus. Monitor for:

- "address confidence score" in any organizational communication
- "DELETE Act DROP platform" paired with immigration context
- "Tier 1 threat level" used in a security briefing
- "data broker opt-out" specifically contextualized for undocumented people (not just generic privacy advice)

**Phase 2 readiness prediction**: If ≥2 Tier 1 contacts use corpus-origin vocabulary in their own communications by Day 45, Phase 2 distribution to digital rights organizations will land with high credibility. These organizations vet sources rigorously — vocabulary migration signals that the corpus has been tested in operational practice, not just read.

**If absent at Day 60**: Vocabulary migration being absent at Day 60 predicts with high reliability that formal institutional integration will not occur by Month 6. The corpus is being held at "awareness" rather than "understanding." This is typically a routing failure (program staff never saw it) or a format failure (it was bookmarked rather than read).

### Signal 2: Unprompted Secondary Distribution (Days 7–21)

A Tier 1 contact shares the corpus without being prompted to do so. Signs:
- A referral from someone not in the initial send list who cites a Tier 1 organization as the source
- A Gist view spike correlating with no action from the sender
- A reply stating "I've already shared this with [colleague/partner org]" before being asked
- The corpus appearing in a Signal group, Slack channel, or social post not seeded by the sender

**Phase 2 readiness prediction**: If 2+ organizations forward the corpus unprompted in the first 21 days, the S-curve has started. Phase 2 can launch with social proof framing: "Organizations working directly with affected communities have already been distributing this." If requesting permission to name organizations, do so at the Day 30 follow-up.

**High-value scenario**: CLINIC (400+ affiliated programs nationally) forwarding to its affiliate network within 30 days would represent a Phase 2 readiness signal in itself — one send effectively constituting a Phase 2 distribution.

### Signal 3: Domain-Specific Requests (Days 7–30)

A contact asks for more information on a specific section or scenario. High-signal request forms:
- "Can you tell me more about the DROP platform pathway for clients without ID?" (operational test)
- "Does this cover [specific scenario]?" where the scenario is a real client situation
- "Is there a version we could print for clients without internet access?" (deployment signal)
- "Our clients are mostly on phones — is there a mobile version?" (barrier signal with high-value fix)

**Phase 2 readiness prediction**: Domain-specific requests mean the corpus is being tested against real operational need. This is a Stage 1 signal with Stage 2 predictive value. Organizations that ask specific questions are more likely to implement within 60 days than organizations that reply with general approval.

**Critical interpretation note**: A request for device-hardening elaboration indicates a recipient with higher technical security culture (more likely to be a mutual aid network or an organization with in-house security capacity). A request for messaging app guidance indicates a recipient at an earlier stage of security adoption. A request for DROP platform guidance indicates a California-based organization with direct-service clients. Log the domain of every specific request — it drives both Phase 2 message framing and guide revision priority.

### Signal 4: Legal or Practitioner Credential Engagement (Days 14–45)

A legal or policy professional engages with the sourcing or legal framework of the threat model. Signs:
- An attorney asks which FOIA requests or court filings document the ELITE capabilities
- A paralegal asks whether the opt-out procedures satisfy a specific state statute
- An organization requests the threat model for use in litigation or regulatory comment

**Phase 2 readiness prediction**: Legal credentialing engagement from even one Tier 1A organization is a strong signal for Phase 2 distribution to journalists and academic programs. Journalists need to be able to cite the source; academics need to be able to teach it. Legal practitioner validation answers the credibility question that would otherwise require weeks of Tier 2 vetting.

---

## 4. Timeline Expectations by Phase

### Days 0–30: Access and Readiness

**Primary question**: Did the corpus reach the right people?

The primary failure mode in this phase is not low engagement — it is the corpus being routed to communications staff rather than program staff. Communications staff acknowledge and file; program staff ask questions.

**Expected event sequence**:
- Days 1–3: First Bitly clicks (immediate after send)
- Days 3–7: First replies from mutual aid networks (1C) and fast-moving community orgs (1B)
- Days 7–14: First replies from legal aid organizations (1A)
- Day 7: Week 1 follow-up sent to non-responders (subject line variant)
- Days 14–21: Follow-up wave; first referral contacts generated
- Days 21–30: 30-day assessment; Day 30 follow-up email sent

**Phase gate**: ≥8 of 33 organizations at "Read" level by Day 30. Zero replies by Day 10 is a deliverability emergency, not a content failure — verify spam filter status and contact addresses before drawing any conclusions about corpus quality. At 33 organizations, even 5 replies by Day 10 is a reasonable early signal for a cold outreach campaign of this type.

**What does not belong in this phase**: Protocol changes, curriculum integration, or institutional policy adoption. Any organization that shows Stage 3+ signals in the first 30 days is unusual — log it, but do not use it to set revised Phase 2 timelines.

### Days 30–90: Vocabulary Adoption

**Primary question**: Is the corpus shaping how organizations think about the threat, even before formal adoption?

Vocabulary adoption is the leading indicator of eventual institutional integration. The resistance-research adoption framework shows that vocabulary migration at 30–90 days predicts institutional integration at 6–12 months with higher reliability than engagement rates alone.

**Expected event sequence**:
- Weeks 5–8: First observable use of corpus language in organizational communications
- Weeks 6–10: Organizations that showed Stage 1 engagement begin internal circulation (Stage 2)
- Day 60: Mid-cycle assessment; compare sector engagement rates; identify stalled contacts
- Days 84–90: 90-day follow-up sent; structured feedback collected via `recipient-feedback-template.md`

**Phase gate**: ≥2 documented vocabulary migration events AND ≥8 organizations at "Understood" level by Day 90.

**Intervention trigger**: If Day 60 assessment shows zero vocabulary migration and reply rate below 25%, apply the routing diagnostic in Section 5 before concluding content failure.

### Days 90–180: Practice Changes

**Primary question**: Have organizations changed what they actually do?

Observable practice changes — intake checklist updates, communication protocols, client education programs — are the Stage 3+ signals that constitute genuine adoption.

**Expected event sequence**:
- Months 3–4: Organizations that showed Stage 2 signals become Stage 3 (partial implementation)
- Month 4–5: First case study eligible organizations emerge; case study interview window opens
- Month 6: 6-month reassessment; Phase 2 (Tier 2 distribution) decision review

**Phase gate**: ≥5 of 33 organizations at "Implemented" level by Day 180, with at least one external citation (published output, toolkit, or institutional resource list) and at least one confirmed adoption from each of Sectors A–D.

**The highest-confidence signal in this entire framework for the 33-organization amplifier cohort**: A Sector A digital rights organization (EFF, CDT, Privacy International) publishing any output that cites the ELITE threat model with attribution to the corpus. This signal constitutes public institutional validation by organizations whose credibility is recognized by policymakers, journalists, and technical communities simultaneously. A single EFF citation changes the corpus's standing in every subsequent distribution context.

**The highest-consequence signal in the broader project**: Any legal organization (from the prior direct-service cohort) reporting that it walked a client through the AB 60 → DELETE Act DROP platform pathway. This signal is a direct chain from corpus to reduced ELITE targeting risk for a specific undocumented person. No other metric in any distribution tier reaches that level of consequence. Track it separately from the 33-organization amplifier cohort metrics.

---

## 5. Feedback Triage

Feedback from Tier 1 contacts falls into one of four categories, each with a distinct response protocol. The most common error is treating a category (c) wrong-threat-model problem as a category (a) wording fix — it produces cosmetic revisions that do not address the real issue.

### Category (a): Minor Wording Fix

**Definition**: The guide's logic is sound and the threat model is accurate, but specific language or instructions are unclear, outdated, or missing a step.

**Distinguishing test**: If you fixed the specific wording or step, would the feedback reporter say "that's all I needed"? If yes, this is category (a).

**Signal patterns**:
- "The DROP platform signup screen looks different than described in Step 3"
- "The VeraCrypt version number in the screenshot is outdated"
- "You're missing a step between [X] and [Y] in the Signal hardening section"
- "The phrase 'address confidence score' appears in Section 2 without being defined first"

**Response**: Fix in the live Gist immediately. No Tier 2 launch delay. Document the fix in a running changelog at the top of the guide. Note the improvement in Tier 2 outreach as evidence of active iteration.

**Timeline**: Fix within 48 hours of confirmation.

### Category (b): Missing Section

**Definition**: The guide's existing content is correct, but a real scenario or population is not addressed and that gap is preventing adoption.

**Distinguishing test**: The feedback describes a use case that the corpus does not cover, but the corpus's existing threat model would correctly analyze that use case if extended. The gap is scope, not accuracy.

**Signal patterns**:
- "We work with elderly clients who don't have smartphones — there's nothing here for them"
- "Our clients are mixed-status families — the guide assumes individuals, not families with different legal statuses"
- "There's no guidance for what to do if a client has already been detained and their device may have been searched"
- "Our clients use shared devices at public library computers — none of these steps apply"

**Response**: Document the missing scenario. Prioritize for the next version based on frequency (if 2+ organizations report the same gap, it is required before Tier 2 launch). If the missing scenario is post-detention or device-compromised, consult a digital security expert before adding guidance — these are higher-stakes scenarios where incorrect advice causes real harm.

**Timeline**: Assess priority within 7 days of Day 90 feedback aggregation. Required fixes before Tier 2: any gap cited by 2+ organizations, plus any gap specific to California DROP platform procedures.

### Category (c): Wrong Threat Model

**Definition**: The guide's description of the threat — what the surveillance system does, what data it accesses, how targeting decisions are made — does not match what organizations actually observe on the ground.

**Distinguishing test**: The feedback describes specific cases where the corpus's predictions did not hold, or where the actual threat vector was different from what the guide describes. This is not a clarity problem. It is a factual accuracy problem.

**Signal patterns**:
- "The attorneys in our network say clients are mostly being found through employer records and school records, not commercial data broker databases — Part 0 wouldn't have helped those cases"
- "We've had clients who completed all the data broker opt-outs and were still located within 30 days — the ELITE system must have other sources we don't know about"
- "The guide says DMV records are a primary source, but our state DMV has a policy explicitly blocking ICE data sharing — that section is misleading for our clients"
- "We have a client whose case showed that ICE was using utility records, which aren't covered anywhere in the threat model"

**Response**: This is the highest-severity feedback category. Do not launch Phase 2 (Tier 2 distribution) until this is resolved. Steps:
1. Request specifics: ask the reporting organization for any case documentation they can share (even anonymized) that supports the alternative threat vector
2. Cross-check against primary sources: verify whether the new threat vector is documented in any court filing, FOIA disclosure, or government contract the corpus has not yet analyzed
3. If the new threat vector is confirmed by primary source: update the threat model section, note the update explicitly, and revise Part 0 recommendations to address the additional vector
4. If the new threat vector is anecdotal without primary source confirmation: add a "Known gaps and limitations" section noting that the corpus documents confirmed data sources as of its publication date and that operational patterns may vary by jurisdiction

**Phase 2 hold condition**: Any confirmed factual inaccuracy in the threat model requires updating before Tier 2 distribution. Digital rights organizations and academic programs will subject the threat model to higher scrutiny than direct-service organizations. An error that passes undetected in Tier 1 will not survive Tier 2 vetting.

### Category (d): Framework Isn't Landing

**Definition**: Feedback indicates the corpus is not activating the intended audience — not because of a specific content problem, but because the corpus's framing, format, or entry point does not fit how these organizations process information and prioritize action.

**Distinguishing test**: Multiple organizations express positive intentions ("this looks useful") but zero behavior change. The gap is not a specific content error or missing section — it is that the corpus is not prompting action. If you could not fix this with a single content change, this is category (d).

**Signal patterns**:
- Reply rate below 15% after 30 days with no deliverability or routing explanation
- All replies at Stage 0 (generic acknowledgment, no specific engagement) across multiple organizations
- Referral factor of 0 at Day 45 (no secondary distribution)
- Day 60 check shows zero vocabulary migration across all 12 contacts
- Multiple organizations say "we'll get to it when things calm down" — without any follow-through after 60 days

**Diagnostic sequence before concluding category (d)**:
1. Was the corpus routed to program staff or only communications staff? If communications staff: re-send to program contacts. This resolves category (d) pattern without being category (d).
2. Did the subject line land in spam? Verify. If yes: test a new subject line. Not category (d).
3. Is there a concurrent crisis absorbing staff capacity? (Major enforcement wave, organizational leadership change.) If yes: re-engage after 30 days. Not category (d).
4. Is the entry point wrong for the audience? Tier 1B and 1C audiences may need to lead with Part 0 (immediate action) rather than the threat model (analytical framing). If organizations are routing the corpus as a "reference document" rather than an "action document," the corpus leads with the wrong section for those audiences.

**If diagnostics are clear and category (d) pattern persists**:
- The corpus is too long for a first-touch ask for Tier 1B and 1C. Produce a standalone 2-page Part 0 document as a new entry point. Send the 2-page version first; link to the full corpus for interested recipients.
- Consider whether the outreach framing positioned the corpus as an analytical resource rather than an operational one. For direct-service organizations, operational framing ("your clients can take these steps today") is more activating than analytical framing ("here is what the surveillance infrastructure does").

**Phase 2 hold condition**: If fewer than 6 of 33 organizations show Stage 1+ engagement by Day 90 after all diagnostics have been addressed, hold Phase 2 launch. Phase 2 outreach will invoke Tier 1 social proof — that proof must exist before it can be invoked. Launching Phase 2 without Tier 1 social proof weakens every subsequent distribution tier. At 33 organizations, 6 Stage 1+ engagements is 18% — a low bar set deliberately to account for the outreach dynamics of technical organizations that are skeptical of unsolicited security research. If even this threshold is not met, the corpus's framing is the problem, not its content.

---

## 6. Go/No-Go Decision Tree for Phase 2

The following decision tree synthesizes the 90-day assessment into an explicit Phase 2 launch decision. Assess at Day 90 from the first Tier 1 send.

```
PHASE 2 (TIER 2 DISTRIBUTION) GO/NO-GO ASSESSMENT
Assessment Date: [Day 90 from first Tier 1 send]
Cohort: 33 organizations (Sectors A–D: digital rights, academic, researcher, journalist)

GATE 1 — BASIC DISTRIBUTION CONFIRMATION
Did at least 28 of 33 named Tier 1 organizations receive the corpus?
  YES → proceed to Gate 2
  NO → complete remaining sends before assessing; delay Gate 2 by [N] weeks

GATE 2 — ENGAGEMENT QUALITY
Of the organizations that replied, are at least 50% at Stage 1 or above ("Read" level)?
  YES → proceed to Gate 3
  NO (but ≥25% replied, i.e., ≥8 of 33) → run routing diagnostic (Section 5, category (d))
     → re-send to corrected program-level contacts
     → re-assess after 2 weeks
     → if still below 50% Stage 1+: classify as category (d); apply format interventions
  NO (below 15% replied, i.e., fewer than 5 of 33) → deliverability failure or category (d)
     → check spam filters; verify contacts; test subject line variant
     → if corrected contacts still produce <15% reply rate: HOLD Phase 2

GATE 3 — ADOPTION SIGNAL (at least 2 of the following, from at least 2 different sectors)
  [ ] A Sector A organization has linked to or cited the corpus in any published output
  [ ] A Sector B academic program has requested citation details or course use permission
  [ ] A Sector C researcher has shared the corpus in their own network (unprompted)
  [ ] A Sector D journalist organization has incorporated corpus into journalist security training
  [ ] Any organization has requested an updated version, translation, or adapted format
  [ ] A referral contact generated from the cohort has engaged substantively at Stage 1+
  [ ] Corpus appeared in an organizational newsletter, resource list, or public post not seeded by sender

  2 or more boxes checked, from ≥2 sectors → proceed to Gate 4
  1 box checked, 1 sector only → conditional hold; wait 21 days for second signal
                               → if no second signal: apply sector-specific triage before proceeding
  0 boxes checked → hold Phase 2 until Gate 3 criterion is met, max Day 120
                  → at Day 120 with 0 Gate 3 signals: category (d) confirmed; 
                    revise entry point and re-engage 5 highest-potential contacts

GATE 4 — FEEDBACK INTEGRATION
Have the following been answered by at least 6 Tier 1 contacts (from ≥2 sectors)?
  [ ] Which section was most relevant? (identifies framing for Phase 2)
  [ ] What barriers prevented or delayed implementation? (drives format decisions)
  [ ] Is the threat model sourced well enough to cite publicly? (credibility assessment)
  [ ] Is there anyone else who should have this? (builds Phase 2 contact list)

  All four answered from ≥6 contacts → proceed to Phase 2 launch decision
  Three answered from ≥4 contacts → proceed with noted gap
  Fewer than 4 contacts responded → send targeted follow-up to highest-Stage contacts; 
                                    wait max 14 days before proceeding with available data

GATE 5 — THREAT MODEL INTEGRITY
Has any category (c) wrong-threat-model feedback been received?
  NO → proceed to Phase 2 launch decision
  YES, confirmed by primary source → update threat model; delay Phase 2 minimum 14 days 
                                    from update completion
  YES, anecdotal only → add "Known gaps and limitations" section; proceed with 
                        disclosure language

PHASE 2 LAUNCH DECISION

  All 5 gates pass → LAUNCH Phase 2 sends

  Gates 1, 2, 4, 5 pass; Gate 3 = 1 signal, 1 sector only → CONDITIONAL HOLD
    Wait for second Gate 3 signal from a different sector, maximum 21 additional days
    If no second signal by Day 111: proceed with available Gate 3 signal; note in Phase 2 framing
    Phase 2 outreach should lead with the sector where adoption is confirmed

  Gate 2 fails → HOLD
    Diagnose routing vs. deliverability vs. category (d) framework failure
    Apply corrected contacts or format interventions
    Re-assess at Day 105

  Gate 5 fails (category c confirmed) → HOLD
    Update threat model before any Phase 2 distribution
    Minimum 14-day hold from update completion for Tier 1 feedback on revision

  Condition C (overwhelming demand) detected — signals:
    ≥5 organizations at Stage 1+ by Day 14, OR
    ≥3 unprompted secondary distributions in first 21 days, OR
    ≥1 major Sector A publication (EFF, CDT, Privacy International) before Day 30
  → ACCELERATE
    Confirm organizational permission to cite adoption signals
    Produce standalone summary document for Phase 2 framing
    Launch Phase 2 immediately with named social proof where permitted
```

---

## 7. Phase 2 Readiness: What Each Sector Signal Predicts

The Tier 1 signals do not equally predict Phase 2 success. Phase 2 outreach will be to a broader public or policymaker audience — and the Tier 1 cohort's adoption patterns determine what social proof is available and how credible it will be.

### If Sector A (digital rights) adopts: Phase 2 readiness very high for policy audiences

A digital rights organization publishing or formally linking to the corpus constitutes institutional validation. EFF or CDT endorsement, in particular, is a credibility signal that travels across the entire civil liberties and policy community. For Phase 2 outreach to policymakers, legislative staff, and broader civil society coalitions: a single EFF or CDT citation is sufficient social proof to frame Phase 2 outreach as "already validated by leading digital rights organizations."

### If Sector B (academic) adopts: Phase 2 readiness high for research and technical audiences

An academic program incorporating the corpus into a syllabus or citing it in research signals that the corpus has passed the scrutiny of experts with direct knowledge of the technical landscape. For Phase 2 outreach to technical policy audiences, regulatory agencies, or think tanks: academic adoption is the specific social proof that separates "advocacy document" from "research-grounded analysis." Cite specific institution types, not individual names, unless permission is obtained.

### If Sector C (researchers) adopt: Phase 2 readiness high for technical and practitioner audiences

Researcher community adoption — especially if any technical critique or extension was incorporated — is the social proof that the corpus can withstand expert scrutiny. For Phase 2 outreach to any technical audience: "security researchers reviewed the threat model and raised questions that have been incorporated" is a stronger credibility signal than "no critiques received," because it shows active engagement, not just passive acknowledgment.

### If Sector D (journalists) adopt: Phase 2 readiness very high for public and media audiences

A journalist organization integrating the corpus into their security training, or a published piece citing it, constitutes the broadest possible social proof. Journalism coverage creates a public record that amplifies every subsequent outreach. For Phase 2 outreach to wider audiences: a link to published journalism citing the corpus is more compelling than any first-party claim about the corpus's value.

### If recipients report threat model inaccuracy: Phase 2 readiness conditional

Any Tier 1 recipient reporting that the threat model does not match documented evidence requires resolution before Phase 2. The 33-organization Tier 1 cohort has significant technical and legal sophistication — if the threat model survives their scrutiny, it will survive Phase 2. If it does not, Phase 2 amplification of an inaccurate threat model causes reputational harm that is difficult to reverse. The Phase 2 hold in Gate 5 exists specifically to catch this before it compounds.

### Cross-sector adoption pattern: the strongest Phase 2 signal

If at least two sectors show Stage 1+ engagement by Day 45 — particularly if Sector A and Sector D both show signals — the corpus has demonstrated the ability to bridge technical audiences and communications-focused audiences simultaneously. This cross-sector adoption pattern is the strongest available predictor of sustained Phase 2 success across heterogeneous audiences.

---

## 8. Failure Mode Taxonomy

These failure modes are distinct and require different responses. Misdiagnosing one as another is the most common cause of unnecessary framework revision.

| Failure Mode | Symptoms | Root Cause | Correct Response | Wrong Response |
|---|---|---|---|---|
| Routing failure | Replies arrive but uniformly Stage 0 (generic acknowledgments, no content questions) | Corpus reached communications staff, not program staff | Research correct program-level contact; re-send with routing note | Revise corpus content |
| Deliverability failure | Zero replies, zero Bitly clicks after 14 days | Spam filter, wrong address, or organizational chaos | Test alternate email; try Signal for 1B/1C; verify contact info | Revise corpus content |
| Format mismatch | Positive intent but "we'll read it when we have time" language, no follow-through | Gist URL does not fit organizational resource-sharing workflow | Produce PDF; create standalone Part 0; re-send in adapted format | Revise threat model |
| Audience mismatch | Active engagement from unexpected sectors; target sectors unresponsive | Corpus's technical depth fits security-aware organizations, not high-volume direct-service organizations | Lead with Part 0 for 1B/1C; reserve full corpus for 1A | Simplify the threat model |
| Content gap (category b) | Positive intent expressed; specific requests for missing scenarios recurring | Corpus does not address this population's actual situation | Document gap; add to next version; re-engage with updated material | Add more technical depth |
| Wrong threat model (category c) | Ground-level feedback contradicts threat model's claims about how ICE locates targets | Threat model based on documentation that is incomplete or jurisdiction-specific | Verify against primary sources; update if confirmed; add limitations section | Ignore until more reports come in |
| Framework isn't landing (category d) | Low engagement across all sectors after routing, deliverability, and timing diagnostics clear | Core framing does not resonate with organizational self-understanding of mission | Reframe entry point; lead with Part 0; test operational vs. analytical framing | Revise corpus structure |

---

*Framework complete. Calibrated for 33-organization amplifier cohort (Sectors A–D: digital rights, academic, researcher communities, journalists). Read alongside `tier-1-success-metrics-framework.md` (per-organization tracking tables) and `tier-1-feedback-collection-protocol.md` (follow-up email templates). The Phase 2 decision tree in Section 6 is the operative synthesis. The failure mode taxonomy in Section 8 is the diagnostic key for any signal pattern that does not match expectations.*

*The prior 12-organization direct-service cohort (1A immigration legal aid, 1B community-based, 1C mutual aid) uses the sector-specific thresholds from the earlier version of this document. Do not mix cohorts when assessing campaign-level thresholds.*

*Last revised: 2026-05-05*
