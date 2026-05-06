---
title: "Post-Distribution Impact Tracker — Organizational Adoption & Assessment Gates"
project: cybersecurity-hardening
created: 2026-05-06
version: 3.0
status: ready-for-use
supersedes: v2.0 (individual-level adoption by segment — see post-distribution-impact-tracker-v2.md)
depends-on:
  - tier-1-success-metrics-framework.md
  - tier-1-effectiveness-framework.md
  - tier-1-feedback-collection-protocol.md
  - adoption-tracking-dashboard-spec.md
  - feedback-collection-template.md
---

# Post-Distribution Impact Tracker v3.0
## Organizational Adoption, Assessment Gates, and Tier 2/3 Readiness

**Lead finding**: The most dangerous failure mode after Tier 1 distribution is treating early positive replies as adoption. A reply is a receipt, not a behavior change. This document defines what counts as actual adoption at the organizational level, sets concrete assessment gates at 3, 6, and 12 months, and provides the decision logic for whether Tier 2/3 distribution should replicate the Tier 1 approach or pivot. Nothing in this document should be read until at least one Tier 1 contact has replied — the measurement infrastructure has no value before data exists to enter into it.

**Relationship to prior versions**: v1.0 covered the original 12-organization direct-service cohort (immigration legal aid, community-based organizations, mutual aid networks). v2.0 added individual-level adoption metrics by audience segment (journalists, attorneys, activists, undocumented immigrants) and threat-model-specific outcome signals. This v3.0 document covers the full organizational tracking lifecycle: what adoption means, how to measure it, what the 3/6/12-month gates require, and what each gate's outcome implies for Tier 2/3 strategy. Read v2.0 for individual-segment metrics; read this document for campaign-level assessment and strategic decisions.

**Corpus cohorts tracked here**:
- Cohort A (direct-service): 12 organizations — immigration legal aid (1A), community-based (1B), mutual aid (1C)
- Cohort B (amplifier): 33 organizations — digital rights, academic cybersecurity, researcher communities, journalist organizations

---

## Section 1: Defining "Effective" and "Adopted"

Most impact assessments fail because they never define success concretely. These definitions apply to all organizational tracking in this campaign. They are not aspirational — they are binary pass/fail criteria for assessment gates.

### 1.1 What Counts as "Adopted"

An organization has adopted the corpus when it has taken at least one observable action that required a decision to use this resource, not merely to read it. Reading is not adoption. Forwarding to a colleague is not adoption. Adding to a bookmark list is not adoption.

**Minimum adoption threshold (Stage 3)**: An organization that has done at least ONE of the following:

| Action | Evidence Type | Minimum Quality Required |
|--------|--------------|--------------------------|
| Added the corpus to a client-facing resource page, intake checklist, or published practitioner toolkit | Link or screenshot | Resource publicly accessible or confirmed by organization contact |
| Delivered staff or client training using corpus content as the basis | Training agenda, calendar invite, or self-report | Must reference specific corpus sections, not generic security guidance |
| Changed a client intake form, communication protocol, or organizational policy to reflect corpus recommendations | Document comparison or self-report with specifics | Must reference specific countermeasure (Signal for client comms, data broker opt-outs in intake, etc.) |
| Walked at least one client through any corpus-specific procedure (DROP platform, Signal setup, data broker manual opt-outs) | Self-report from attorney or caseworker | Must be traceable to corpus guidance, not pre-existing practice |
| Cited or referenced corpus content in a published output (brief, newsletter, report, filing, syllabus) | URL or document | Must include a specific claim, term, or procedure from the corpus |

An organization is NOT adopted if:
- It acknowledged receipt without a follow-up action
- It replied "we'll review this" without a subsequent Stage 3 signal by the assessment gate date
- It forwarded the corpus to a colleague without any other observable action
- It expressed positive intent ("this is exactly what we need") without any action within 90 days

### 1.2 What Counts as "Effective"

Effectiveness is measured at two levels: corpus effectiveness (did the guidance produce security posture improvements?) and campaign effectiveness (did the distribution approach reach and convert the target organizations?).

**Corpus effectiveness — minimum definition**: At least one individual who implemented a countermeasure from the corpus experienced a measurable security posture improvement. This is defined as:

- A journalist who moved source communications from unencrypted SMS/email to Signal, reducing SIGINT collection surface
- An undocumented individual whose data broker records were removed via manual opt-out or DROP platform, reducing their Palantir ELITE address confidence score
- An immigration attorney whose client communications now occur via Signal with disappearing messages, reducing subpoena attack surface
- An activist who deployed Rayhunter and detected IMSI catcher presence, enabling informed decision to leave their device at home

Note: Security posture improvement cannot be verified by comparing incident rates before and after hardening. The absence of an ICE encounter is not attributable to hardening without a counterfactual. Proxy measures (confirmed implementation of countermeasures that remove specific attack surfaces) are the only measurable proxy for effectiveness. Do not claim incident prevention; claim attack surface reduction.

**Campaign effectiveness — minimum definition**: Across both cohorts combined, at least 15% of organizations reached Stage 3 (adopted) by the 6-month gate, with at least one organization from each cohort type and at least one organization that has distributed the corpus to its own network.

---

## Section 2: Organization Adoption Stage Definitions

These stages apply to every organization in both cohorts. Track the current stage for each organization in the CSV tracker.

| Stage | Name | Definition | Observable Evidence |
|-------|------|-----------|---------------------|
| 0 | Received | Corpus was sent; no reply | Date-sent field populated |
| 1 | Acknowledged | Organization confirmed receipt or clicked the Gist link | Reply logged, or Bitly click from organization domain |
| 2 | Reviewed | Someone at the organization read the corpus beyond the opening section | Reply references specific section, term, or claim; asks an implementation question |
| 3 | Partial Adoption | Organization took at least one action using corpus content | See Stage 3 criteria in Section 1.1 above |
| 4 | Full Adoption | Organization has integrated the corpus into sustained practice | Multiple Stage 3 actions; corpus referenced in more than one context; ongoing implementation |
| 5 | Multiplier | Organization has actively distributed the corpus to its own network without prompting | Referral contacts generated; corpus appears in organization's own communications; affiliate outreach confirmed |

**Critical distinction between Stage 2 and Stage 3**: An organization that replies "we've reviewed this and it's very relevant to our work" is Stage 2 until it takes an action. Stage 2 can persist indefinitely without becoming Stage 3 without an external prompt (follow-up email, direct ask) or internal organizational decision. The 90-day follow-up protocol exists specifically to create the external prompt that moves Stage 2 organizations to Stage 3.

---

## Section 3: Assessment Gate — Month 3 (Day 90)

**Assessment date**: Day 90 from first Tier 1 send, approximately August 2026

**Primary question**: Has the corpus produced enough adoption signals to justify Tier 2 launch?

### 3.1 Required Data to Complete This Assessment

Before the Day 90 assessment, the following must be collected:
- The 90-day follow-up email sent to all Stage 1+ contacts (per `tier-1-feedback-collection-protocol.md`)
- Responses logged in the CSV tracker with Stage-of-adoption field updated
- Gist view count recorded
- Any social media or citation monitoring results logged
- Any referral contacts from Question 3 of the 30-day follow-up documented

### 3.2 Day 90 Pass/Fail Criteria

**Gate 1 — Distribution Completion**

| Criterion | Pass | Conditional | Fail |
|-----------|------|-------------|------|
| Cohort A sends completed (12 orgs) | 10+ of 12 contacted | 8-9 contacted | Fewer than 8 contacted |
| Cohort B sends completed (33 orgs) | 28+ of 33 contacted | 20-27 contacted | Fewer than 20 contacted |

Gate 1 does not require response — only that sends were completed. If Gate 1 fails because sends were never completed, assess only what has been sent and note that the Day 90 assessment is incomplete.

**Gate 2 — Engagement Quality**

| Cohort | Pass Threshold | Conditional | Fail |
|--------|---------------|-------------|------|
| Cohort A reply rate | ≥35% of sends (4+ of 12) | 25-34% | Below 25% |
| Cohort A Stage 2+ rate among replies | ≥50% of replies | 30-49% | Below 30% |
| Cohort B reply rate | ≥25% of sends (8+ of 33) | 15-24% | Below 15% |
| Cohort B Stage 1+ rate among replies | ≥50% of replies | 30-49% | Below 30% |

**Gate 3 — Adoption Signal Presence**

At least THREE of the following signals must be present by Day 90:

- [ ] At least 1 Cohort A organization is at Stage 3 (confirmed adoption action)
- [ ] At least 1 Cohort A organization has explicitly referenced corpus content when working with a client (e.g., walked through DROP platform)
- [ ] At least 1 Cohort B organization has circulated corpus within their network unprompted
- [ ] At least 1 Cohort B organization has confirmed curriculum or resource list inclusion
- [ ] Referral factor ≥ 1.5 across both cohorts combined (total relationships generated / initial sends)
- [ ] A corpus-specific term (ELITE address confidence score, DROP platform AB 60 pathway) has appeared in any organizational communication outside the original distribution

**Gate 4 — Feedback Quality**

Structured feedback (via 90-day email survey or direct exchange) collected from at least 6 organizations covering:
- At least one gap identified and documented
- At least one threat model accuracy assessment (confirmed / partially accurate / inconsistent)
- At least one format barrier identified

**Gate 5 — Threat Model Integrity**

No Category (c) wrong-threat-model feedback received that has been confirmed by primary source documentation. If confirmed Category (c) feedback exists, it must be resolved before proceeding to Tier 2.

### 3.3 Day 90 Decision Logic

| Gate Pattern | Decision | Action |
|---|---|---|
| All 5 gates pass | Proceed to Tier 2 launch | Schedule sends; incorporate feedback |
| Gates 1, 2, 4, 5 pass; Gate 3 = 2 of 6 signals | Conditional proceed | Wait 21 days for third signal; if no third signal by Day 111, proceed with framing adjusted to available social proof |
| Gate 2 fails (reply rate below threshold) | Hold; diagnose | Apply routing and deliverability diagnostics before concluding content failure |
| Gate 5 fails (confirmed Category c) | Hold; update | Update threat model; wait minimum 14 days for re-verification before Tier 2 |
| Gate 3 = 1 signal only | Conditional hold | Identify highest-potential contacts; direct outreach for Stage 3 conversion; re-assess at Day 105 |
| Fewer than 4 total feedback responses | Partial hold | Send targeted follow-up to Stage 2+ contacts; wait 14 days before deciding |

**What Day 90 does not tell you**: Day 90 tells you whether Tier 2 distribution is safe to launch, not whether the corpus has succeeded. Organizational integration (curriculum, policy, practice change) typically requires 90–180 days post-adoption-signal. A Day 90 pass means the corpus is gaining traction. It does not mean it has changed how any organization operates.

---

## Section 4: Assessment Gate — Month 6 (Day 180)

**Assessment date**: Day 180 from first Tier 1 send, approximately November 2026

**Primary question**: Has organizational adoption translated into measurable practice changes, and are there enough adoption patterns to inform Tier 2/3 framing?

### 4.1 Required Data to Complete This Assessment

- The 180-day follow-up email sent to all Stage 3+ contacts
- Case study interview completed or scheduled for at least 1 Stage 3+ organization
- Gist view count delta documented
- Overton.io quarterly search completed (August search)
- Any legal filing, policy document, or public output citations identified
- Tier 2 launch results (if Tier 2 launched at Day 90): first 90-day data from Tier 2 cohort

### 4.2 Day 180 Pass/Fail Criteria

**Practice Change Threshold**

At least 5 organizations across both cohorts at Stage 3 or above by Day 180. This represents approximately 11% of the combined 45-organization send list — calibrated against the realistic benchmark of 3–5 sustained adoptions within 18 months documented in `tier-1-success-metrics-framework.md`.

| Metric | Pass | Conditional | Fail |
|--------|------|-------------|------|
| Organizations at Stage 3+ | 5+ of 45 total sent | 3-4 of 45 | 0-2 of 45 |
| Organizations at Stage 4+ (sustained adoption) | 1+ | 1 is sufficient | 0 |
| External citations (published output, resource list, filing) | 1+ | 1 is sufficient | 0 |
| Case study interview completed | 1 | 1 is sufficient | 0 |

**Sector Coverage Threshold**

At least one Stage 3+ adoption from each of the following sectors:
- [ ] Immigration legal aid (Cohort A, Tier 1A) — direct-service with undocumented clients
- [ ] Community-based organization (Cohort A, Tier 1B) — community education infrastructure
- [ ] Digital rights organization (Cohort B, Sector A) — amplifier and public validation function
- [ ] Journalist organization (Cohort B, Sector D) — practitioner protection and public coverage function

Full sector coverage by Day 180 means the corpus has proven it can serve structurally different organizational missions. Absence of a full sector coverage means Tier 3 framing should weight toward the sectors where adoption succeeded.

**Feedback Integration Threshold**

At least two concrete corpus revisions made in response to Tier 1 feedback, documented in a changelog. This is not a pass/fail criterion for launching Tier 2/3 — it is a quality marker. A corpus that received no feedback actionable enough to drive revision is a corpus that either reached too few organizations or did not reach them deeply enough.

### 4.3 Day 180 Decision Logic for Tier 2/3

**If Day 180 threshold met with sector coverage**: Tier 2 distribution can proceed with high confidence. The framing should lead with the sectors that showed adoption and reference the specific adoption type ("Organizations providing direct legal services to undocumented clients have implemented...").

**If Day 180 threshold met but missing sector coverage**: Proceed with Tier 2/3 but weight outreach toward the sectors where adoption has been confirmed. Do not claim multi-sector adoption in Tier 2 cover messages if the evidence only covers two sectors.

**If Day 180 threshold not met (fewer than 3 Stage 3+ adoptions)**: Tier 3 distribution should be delayed. Investigate whether the shortfall is a content problem (corpus does not meet organizational needs), a channel problem (outreach did not reach the right contacts), or a timing problem (organizations needed 180+ days to convert). Each root cause requires a different response.

---

## Section 5: Assessment Gate — Month 12 (Day 365)

**Assessment date**: Day 365 from first Tier 1 send, approximately May 2027

**Primary question**: Is the corpus sustaining, deepening, or fading? What evidence exists of actual security posture improvement in the populations served?

### 5.1 Required Data to Complete This Assessment

- Google Scholar and Overton.io search results (November and February runs)
- CourtListener and PACER search for "Palantir ELITE" and corpus-specific terms in any filings
- Gist view trajectory over the full 12 months
- Case study interviews completed (target: 2)
- Any near-miss narratives collected via anonymous feedback channel
- DROP platform effectiveness check (November 2026 earliest, for DROP enrollments before August 1, 2026)
- Any news coverage or independent publication citing corpus content

### 5.2 Day 365 Indicators

These are not pass/fail — they are diagnostic indicators for calibrating the corpus's long-term impact and informing ongoing iteration.

**Diffusion indicators (is the corpus spreading beyond direct outreach?)**

| Indicator | Strong | Moderate | Weak |
|-----------|--------|----------|------|
| Gist view trajectory | Month 12 views significantly higher than Month 6 (organic growth continues) | Flat but sustained (~20-50 views/month) | Declining from early peak |
| Attribution-confirmed citations | 3+ from corpus-specific content markers | 1-2 | 0 |
| Academic preprint or working paper citation | 1+ | Informal citation (course reading list, syllabus) | 0 |
| Independent republication (corpus linked in another resource without prompting) | 2+ | 1 | 0 |
| Legal filing citation | 1+ | N/A | 0 |

**Impact depth indicators (is the corpus changing how organizations actually operate?)**

| Indicator | Strong | Moderate | Weak |
|-----------|--------|----------|------|
| Organizations at Stage 4 (sustained, not just initial adoption) | 3+ | 1-2 | 0 |
| Organizations at Stage 5 (multiplier — distributing to their own networks) | 1+ | N/A | 0 |
| DROP platform enrollment reports from California legal aid organizations | 2+ orgs reporting client completions | 1 org | 0 |
| Near-miss narratives received (anonymous channel) | 1+ | N/A | 0 |
| Journalist-to-journalist training using corpus | 1 documented case | Informal sharing | 0 |

**Failure-mode detection (is the corpus stagnating or becoming outdated?)**

| Signal | Action Required |
|--------|-----------------|
| No views after Month 9 (organic traffic has stopped) | Consider re-distribution with updated framing; reach out to Stage 4 organizations for endorsement |
| Version notes show no revisions since launch | Conduct quarterly tool audit; at least one corpus element will have changed in 12 months |
| DROP platform effectiveness feedback negative (data not being removed as promised) | Update guidance with realistic expectations; add California CPPA complaint procedure |
| Academic or legal practitioner reports threat model is outdated | Priority revision; new FOIA requests and contract searches; update before any further distribution |

### 5.3 12-Month Strategic Decision: Replicate or Pivot

The 12-month assessment answers the question the task brief poses: should Tier 2/3 messaging replicate the Tier 1 approach or pivot?

**Replicate if**:
- At least 3 sectors showed Stage 3+ adoption
- The adoption pattern matches the approach (technical depth, primary-source threat model, graduated tier structure resonated)
- Feedback identified gaps in scope (missing populations, missing procedures) but not gaps in framing (the approach itself was not the barrier)
- Referral factor ≥ 1.5 (the corpus is spreading through networks, not just through direct sends)

**Partial pivot if**:
- One or two sectors adopted well but the others did not engage
- Feedback identified a format barrier (Gist vs. PDF, length, language) that is addressable without changing the core approach
- Early adoption concentrated in technical audiences (researchers, digital rights) but not in direct-service audiences (legal aid, community-based)
- A specific threat model claim was found inaccurate and has been corrected; framing adjustment needed to acknowledge the correction

**Full pivot if**:
- Fewer than 3 Stage 3+ adoptions in 12 months across both cohorts (45 organizations)
- Category (c) wrong-threat-model feedback confirmed that the core framing of the ELITE threat is incorrect or jurisdiction-specific
- Feedback converges on a different entry point or format (the corpus should have been a 1-page handout, not a 10,000-word guide)
- Organizations report that the threat model does not match their clients' actual enforcement experiences

**Full pivot does not mean the research was wasted**. It means the distribution format or threat model framing needs a structural revision before Tier 2/3 can succeed. The primary-source documentation of ELITE, DROP platform, and data broker pipelines retains value regardless of format or framing. A pivot should preserve the sourcing while restructuring the presentation.

---

## Section 6: KPIs Summary Table

The following table consolidates all key performance indicators across the three assessment gates. It is the single-page reference for evaluating campaign performance.

| KPI | 3-Month Target | 6-Month Target | 12-Month Target | Data Source |
|-----|---------------|----------------|-----------------|-------------|
| Total organizations at Stage 3+ | ≥3 of 45 | ≥5 of 45 | ≥8 of 45 | CSV tracker |
| Organizations at Stage 4+ (sustained) | 0 required | ≥1 | ≥3 | CSV tracker |
| Organizations at Stage 5 (multiplier) | 0 required | 0 required | ≥1 | CSV tracker |
| Sector coverage at Stage 3+ | 2+ sectors | 3+ sectors | All 4 sectors | CSV tracker |
| External citations (published) | 0 required | ≥1 | ≥3 | Google Alerts, Overton |
| Referral factor | ≥1.2 | ≥1.5 | ≥2.0 | CSV tracker referral count |
| Gist view count | 300+ | 600+ | 1,000+ | Gist traffic log |
| Feedback responses collected | ≥6 | ≥10 | ≥15 cumulative | CSV tracker |
| Corpus revisions made | ≥1 | ≥2 | ≥4 (quarterly cadence) | Gist changelog |
| Confirmed threat model accuracy | ≥1 practitioner confirmation | ≥3 | ≥5 | Feedback logs |
| DROP enrollment reports (CA) | N/A (August 1 deadline) | 0 required until Nov 2026 | ≥2 legal aid orgs | 90/180-day follow-up |
| Near-miss narratives | N/A | 0 required | ≥1 | Anonymous feedback channel |
| Academic/policy citations | 0 required | 0 required | ≥1 preprint or syllabus | Google Scholar, Overton |
| Legal filing citations | 0 required | 0 required | 0 required (1 = exceptional) | CourtListener |

**Note on the legal filing citation**: This is included because it represents the highest-consequence attribution of the corpus to a specific legal outcome. It is not required for any assessment gate. A single legal filing that cites the ELITE documentation would constitute extraordinary campaign-level success. Track it because it is worth tracking, not because its absence is a failure.

---

## Section 7: Incident Prevention Metrics — Proxy Framework

Because effectiveness is primarily a non-event, the proxy measurement strategy is documented here for reference across all three assessment gates.

### 7.1 Attack Surface Reduction as the Primary Proxy

Security posture improvement cannot be directly measured. Attack surface reduction can be. The following attack surfaces are targeted by corpus countermeasures, and their reduction is verifiable:

| Attack Surface | Countermeasure | Verifiable Reduction |
|---------------|---------------|---------------------|
| Commercial data broker records in ELITE database | Data broker manual opt-out or DROP enrollment | Self-report of completed opt-outs; broker removal confirmations |
| SIGINT collection via unencrypted SMS/email | Signal adoption | Self-report: "I now communicate with sources via Signal" |
| ICE home visit via high-confidence address score | Address masking (mail forwarding, P.O. box) | Self-report: "I have moved my address records to a forwarding service" |
| Device seizure during traffic stop | Full-disk encryption + auto-reboot | Self-report: device encrypted; auto-reboot configured |
| Financial surveillance via Venmo/PayPal | Monero or cash | Self-report: "I have stopped using Venmo for political contributions" |
| IMSI catcher at protests | Rayhunter deployment or leaving phone at home | Rayhunter detection log or self-report |

**Attribution protocol**: When an organization or individual reports a countermeasure implementation, log it with an attribution confidence level:
- **High**: References a corpus-specific term or procedure (DROP platform, ELITE address confidence score, Rayhunter)
- **Medium**: Implementation aligns with corpus guidance but could have been learned elsewhere (Signal adoption, data broker opt-out)
- **Low**: General security improvement with no specific corpus link

### 7.2 Near-Miss Narrative Collection Protocol

Near-miss narratives are self-reported stories of cases where hardening appears to have prevented or reduced harm. They cannot be verified. They are the highest-value qualitative signal in the entire tracking framework because they establish a plausible mechanism from corpus implementation to prevented harm.

**Collection channels**:
1. Anonymous Signal number (if established): +1 [number] with the message "OpSec feedback"
2. Anonymous feedback form (linked in the corpus itself): Google Form or Tally with no required identifying fields
3. 90-day and 180-day follow-up email: "Has anyone at your organization used this with a client who subsequently avoided an adverse outcome?"

**Logging protocol**: Log all near-miss narratives with:
- Date received
- Channel (anonymous / org follow-up)
- Audience segment (journalist / attorney / activist / undocumented)
- Countermeasure referenced (which corpus element was implemented)
- Outcome described (what adverse event was avoided or reduced)
- Attribution confidence (did the person specifically reference the corpus?)

**What to do with near-miss narratives**: They are not publishable claims. They are internal signals that tell you whether the corpus is reaching people who face real threats and are using it in real situations. One near-miss narrative from a journalist whose source was protected because they switched to Signal is more meaningful than 100 acknowledgment emails from organizations that said "this looks useful."

---

## Section 8: Connecting Tier 1 Outcomes to Tier 2/3 Design

The Tier 1 assessment gates produce five categories of intelligence that directly drive Tier 2/3 design. This section maps each intelligence category to a specific Tier 2/3 decision.

### 8.1 Adoption Pattern → Tier 2 Audience Sequencing

If Tier 1 adoption concentrated in legal aid organizations (Cohort A), lead Tier 2 with the legal community angle: the corpus has been reviewed by immigration legal aid organizations and is being used in client intake. This framing resonates with the next tier of legal and policy audiences (state bar associations, law school clinics, legislative staff).

If Tier 1 adoption concentrated in digital rights organizations (Cohort B, Sector A), lead Tier 2 with the research validation angle: the corpus has been reviewed by organizations specializing in surveillance policy. This framing resonates with technical and policy audiences.

If adoption is cross-sector, lead Tier 2 with multi-sector framing: the corpus has been adopted by organizations across legal services, digital rights, journalism, and academic research. This is the strongest possible Tier 2 opening.

### 8.2 Gap Inventory → Tier 2/3 Content Updates

The Day 90 feedback aggregation will produce a ranked list of content gaps. The top two gaps that were cited by ≥2 organizations are required updates before Tier 2 distribution. Gaps cited by one organization are Phase 2 enhancements. Gaps that suggest structural problems with the threat model are Category (c) holds.

**Content update priority order for Tier 2**:
1. Confirmed Category (c) corrections: any factual error in the threat model, no matter who reported it
2. DROP platform procedural gaps: the highest-consequence section for California-based undocumented clients
3. Missing population sections cited by ≥2 organizations
4. Language gaps: Spanish-language Part 0 is the highest-priority translation if ≥2 organizations cited it
5. Format gaps: PDF version if ≥3 organizations cited the Gist format as a distribution barrier

### 8.3 Threat Model Accuracy Confirmation → Tier 2 Credibility Framing

If ≥3 Tier 1 organizations confirm that the ELITE threat model accurately describes what they observe in their clients' cases, this confirmation is the strongest available credibility signal for Tier 2. The framing: "Immigration legal practitioners with direct case experience have confirmed that this threat model accurately describes how ICE targeting operates."

If threat model accuracy is mixed or contested, Tier 2 must include explicit uncertainty language: "The threat model is based on publicly documented Palantir contracts and government data-sharing agreements; some aspects of its operational implementation may vary by jurisdiction."

### 8.4 Referral Network → Tier 2 Contact List

Every referral generated via Question 3 of the 30-day follow-up is a Tier 2 warm contact. Warm contacts from Tier 1 referrals should be the first sends in any Tier 2 wave — their prior relationship with a Tier 1 organization means they are already oriented toward the corpus's mission.

Build the Tier 2 contact list in the following priority order:
1. Warm referrals from Tier 1 Question 3 responses
2. Organizations at the same tier as successful Tier 1 adopters (sector-matched outreach)
3. Organizations listed in existing Tier 2 planning documents (tier-2-sector-contact-lists.md, tier-2-outreach-email-templates.md)
4. Cold contacts in sectors where Tier 1 showed no adoption (these require revised framing before sending)

### 8.5 Barrier Profile → Tier 2/3 Approach Adjustment

The most common Tier 1 barrier(s) identified through 90-day feedback determine whether Tier 2/3 should replicate the approach or adjust it.

| Barrier | Adjustment Required |
|---------|-------------------|
| Format (Gist URL) | Produce PDF before Tier 2; lead with PDF in all sends |
| Length | Produce standalone 2-page Part 0 summary; use as Tier 2 entry point |
| Sourcing credibility | Produce sourcing reference appendix; submit to peer review or seek endorsement |
| Language (Spanish gap) | Translate Part 0 before Tier 2 sends to community-based organizations |
| Technical complexity | Produce quick-start videos for highest-friction steps (Tails, VeraCrypt, DROP enrollment) |
| Threat model uncertainty | Add explicit epistemics annotations ("confirmed in X contract" vs. "inferred from X filing") |

---

## Section 9: Privacy and Data Handling for Impact Tracking

### 9.1 Protecting Feedback Sources

The feedback tracking infrastructure contains identifying information about organizations and contacts who discussed security vulnerabilities with vulnerable populations. Handle with appropriate care.

**Storage requirements**:
- CSV tracker stored in a location accessible only to the campaign operator (not shared storage, not public repository)
- If stored in Google Sheets: access restricted to one account; sharing disabled
- If stored locally: on a device with full-disk encryption enabled

**What not to log**:
- Client case details shared by organizations during follow-up calls
- Staff security vulnerabilities disclosed during interviews
- Organizational capacity information that could harm the organization if disclosed
- Near-miss narrative details that could identify a specific undocumented individual

**Anonymization for external reporting**: All external reporting (to Tier 2 contacts, in any public-facing document) must anonymize organizational names unless explicit permission has been granted. Log permission status in the CSV tracker `citation_permission` field.

### 9.2 Safe Feedback Channel Design

Anonymous feedback channels (for undocumented immigrants and activists) must not log IP addresses, require account creation, or retain identifying metadata.

**Acceptable options**:
- Tally.so form: does not log IP addresses by default; accessible without account creation
- Google Form with all required fields disabled: functional but metadata stored by Google
- Paper form at legal aid offices: no digital footprint; collected by trusted intermediary
- Anonymous Signal message: to a number not linked to the campaign operator's identity

**Not acceptable**:
- Typeform (logs IP addresses by default)
- JotForm (requires account or Google sign-in)
- Any form service that integrates with a CRM or marketing platform

---

## Section 10: Monitoring Infrastructure Setup Checklist

Complete before the first Tier 1 send. Items that are not set up before distribution cannot be retroactively applied.

**Before Day 1 (distribution launch)**:
- [ ] Google Alert set for: `"Palantir ELITE" immigration`, `"data broker opt-out" undocumented`, corpus Gist URL
- [ ] Google Scholar alert set for: `"Palantir ELITE" immigration`, `"DELETE Act" undocumented`
- [ ] Bitly short link created for Gist URL (for click tracking)
- [ ] CSV tracker populated with all Cohort A and Cohort B organization rows
- [ ] Anonymous feedback channel established (form URL or Signal number)
- [ ] Gist traffic baseline recorded
- [ ] 90-day follow-up email drafted and saved as Gmail draft template

**At Day 30 (first assessment checkpoint)**:
- [ ] Gist view count logged
- [ ] CSV tracker updated with all reply data
- [ ] Stage-of-adoption field updated for all contacted organizations
- [ ] Day 30 follow-up email sent to all contacts (per `tier-1-feedback-collection-protocol.md` template)
- [ ] Referral contacts from Question 3 added to tracker

**At Day 90 (Gate 1)**:
- [ ] 90-day follow-up email sent to all Stage 1+ contacts
- [ ] Structured feedback (survey or interview) collected and logged
- [ ] Gist view count logged (delta from Day 30)
- [ ] Gate 1-5 criteria evaluated (Section 3.2)
- [ ] Tier 2 decision made and documented

**At Day 180 (Gate 2)**:
- [ ] 180-day follow-up sent to Stage 3+ contacts
- [ ] Case study interview conducted or scheduled
- [ ] Overton.io search run
- [ ] Gist view count logged (delta from Day 90)
- [ ] Gate criteria evaluated (Section 4.2)
- [ ] Tier 3 decision made and documented
- [ ] DROP platform effectiveness check (for enrollments before August 1, 2026)

**At Day 365 (Gate 3)**:
- [ ] Annual Overton, Google Scholar, and CourtListener searches run
- [ ] Near-miss narrative log reviewed and aggregated
- [ ] 12-month impact summary produced (per `adoption-tracking-dashboard-spec.md` quarterly template)
- [ ] Replicate/partial pivot/full pivot decision documented (Section 5.3)
- [ ] WORKLOG.md updated with annual summary

---

*Document complete. This is the master assessment framework. For per-organization follow-up email templates, see `tier-1-feedback-collection-protocol.md`. For individual-level adoption metrics by segment (journalists, attorneys, activists, undocumented immigrants), see `post-distribution-impact-tracker.md` v2.0. For passive monitoring infrastructure (Gist traffic, social media, policy database), see `adoption-tracking-dashboard-spec.md`. For the 90-day structured feedback survey, see `feedback-collection-template.md`.*

*Last updated: 2026-05-06*

**Sources cited in this document**:
- Stage adoption model and referral factor methodology: adapted from `post-distribution-impact-tracker.md` v1.0 (session 717)
- Realistic adoption benchmarks (3–5 sustained adoptions in 18 months): `tier-1-success-metrics-framework.md`, Section 5
- Category (c) wrong-threat-model feedback protocol: `tier-1-effectiveness-framework.md`, Section 5
- Near-miss narrative value and collection: `post-distribution-impact-tracker.md` v2.0, Section A-D
- DROP platform timeline (August 1, 2026 broker processing deadline): [California DROP Platform](https://privacy.ca.gov/drop/)
- Privacy-preserving form design: [Tally.so privacy policy](https://tally.so/help/privacy); [EFF Privacy Badger browser detection](https://privacybadger.org/)
