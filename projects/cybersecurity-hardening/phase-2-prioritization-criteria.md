---
title: "Phase 2 Prioritization Criteria"
project: cybersecurity-hardening
created: 2026-05-05
status: ready-for-use
depends-on: post-distribution-impact-tracker.md, feedback-collection-protocol.md, tier-1-success-metrics-framework.md
---

# Phase 2 Prioritization Criteria

**Purpose**: Define the evidence thresholds that justify launching Phase 2 expansion, and establish a data-driven framework for deciding which new threat models, organizational hardening guides, and tool-specific deepening efforts are worth building versus which should be deferred.

**Lead finding**: Phase 2 should be triggered by pull, not by a calendar. A launch date set in advance without evidence of Phase 1 adoption is likely to produce content for an audience that hasn't yet materialized. The go/no-go decision framework below defines the minimum evidence threshold before Phase 2 begins, and the prioritization criteria decide *which* Phase 2 content gets built first. Both decisions flow from the feedback data, not from assumptions about what the audience needs.

---

## Section A: Data-Driven Prioritization Framework

### A.1 Three Categories of Phase 2 Content

Phase 2 expansion candidates fall into three categories with different triggering conditions.

**Category 1: Organizational Hardening Guides**

*Triggered by*: ≥3 newsrooms, legal aid organizations, or activist collective contacts explicitly requesting organizational implementation guidance beyond what exists in Tier 2.

These guides translate the individual-level Tier 1-3 recommendations into organizational policy language — institutional security policies, device fleet management, encrypted case management system requirements, incident response procedures. They are not targeted at individuals but at the IT director, general counsel, or security-conscious executive director who received the guide and wants to implement it at the organizational level.

Priority ranking based on adoption evidence:

| Guide | Trigger Threshold | Expected Audience | Lead Signal |
|-------|------------------|-------------------|-------------|
| Newsroom hardening policy template | 3+ newsrooms request organizational implementation guidance | News organization IT staff, security editors | FPF or IRE training inquiry |
| Immigration legal aid clinic data security | 2+ legal aid organizations request case management encryption guidance | IT directors, clinical supervisors | NILC/CLINIC/RAICES inquiry about secure case management |
| Activist collective OpSec documentation | 2+ collectives request shared communication standards | Collective tech leads, security officers | Community follow-up request |
| Law school clinic security | 1+ law school clinic requests guidance on FOIA-protected research workflows | Clinical faculty, clinic directors | Academic Tier 2 follow-up |

**Category 2: New Threat Model Coverage**

*Triggered by*: Feedback identifies a substantially different adversary or context not covered by the current Tier 1-3 threat models, with ≥5 requests from the same audience segment.

New threat model candidates from the task brief and current feedback intelligence:

| Threat Model | Audience | Current Coverage Gap | Trigger Evidence |
|-------------|---------|---------------------|-----------------|
| Domestic violence survivor safety | DV shelter residents, DV advocates | Current guide doesn't address intimate partner surveillance (stalkerware, shared family accounts, location sharing) | DV organizations or advocates requesting tailored guidance |
| Labor organizing under employer surveillance | Union organizers, workers in organizing drives | Employer surveillance of organizing (keyloggers, workplace monitoring, social media surveillance) is distinct from government surveillance | Union requests; labor organizer community feedback |
| Election observer OpSec | Poll workers, election observers in contentious districts | Hostile observers, intimidation tactics, device security at polling locations | Election integrity organization requests |
| Foreign journalist in US | Non-US journalists covering immigration story in US | Different legal exposure (no First Amendment protection, visa vulnerability) | Tier 2 journalism outreach feedback |

Note: Domestic violence is the highest-priority new threat model based on two factors: (1) it is requested by a broad and well-organized field that has documented digital security needs, and (2) the adversary (an intimate partner with pre-existing device access and legal status) is structurally different from the government/data-broker adversary in the current guide, requiring new countermeasures that cannot be adapted from the existing Tier 1-3 structure.

**Category 3: Tool-Specific Deepening**

*Triggered by*: Adoption evidence shows that a specific tool has been adopted but users are hitting second-order implementation problems (scaling, maintenance, recovery) not covered by the current guide.

| Tool | Deepening Topic | Trigger Evidence |
|------|----------------|-----------------|
| Signal | Group administration at scale (journalist collective chat, 20+ member activist group, attorney-client messaging at volume) | 3+ requests for Signal group management guidance |
| Tails OS | Recovery and reinstallation after hardware failure; Tails on less-common hardware (ARM-based laptops, older MacBooks) | 5+ Tails installation failure help desk reports on specific hardware |
| Monero | Privacy best practices (CipherTrace/Chainalysis detection avoidance, exchange-free acquisition); wallet backup and recovery | 3+ activist requests for Monero privacy deepening |
| VeraCrypt | Container recovery; cross-platform container portability; plausible deniability configuration | 3+ attorney or journalist requests for encrypted storage troubleshooting |
| California DROP platform | Non-California residents (interstate data broker exposure, states without DROP equivalents); DROP audit and verification | 3+ requests from non-California users asking about DROP equivalents |

### A.2 Geographic Adaptation as Phase 2 Trigger

Immigration enforcement landscapes, sanctuary city policies, and state-level privacy law vary significantly by state. Phase 2 geographic adaptation is triggered when feedback shows meaningful regional variation in what's working and what's not.

**Priority adaptation scenarios**:

- **Texas**: No state privacy law equivalent to the California DELETE Act; no DROP equivalent; anti-sanctuary-city enforcement infrastructure; high-volume immigration enforcement. Texas-specific guide needs: alternative data broker opt-out pathways (manual-only), address masking strategies without DROP, local legal aid resources under state restrictions. Trigger: ≥5 Texas-based feedback submissions citing California-specific guidance as inapplicable.

- **New York**: Strong state privacy protections; NYC sanctuary city policy with recent legal challenges; NYPD Intelligence Bureau operates with significant surveillance infrastructure. Trigger: ≥3 NYC journalist or activist feedback submissions requesting state-specific guidance.

- **Arizona, Georgia, Michigan, Pennsylvania, Wisconsin**: States with contentious election environments and documented hostile relationships between state-level political actors and activist or immigration communities. Trigger: Feedback from activists or immigration attorneys in these states citing specific local enforcement threats not addressed by the current guide.

**Implementation principle**: Geographic adaptation should produce additive supplements, not replacements. A Texas supplement to Part 0 (manual opt-out process for users without DROP access) does not require a full Texas-specific corpus — it's a 2-3 page addendum to the existing guide.

---

## Section B: Go/No-Go Decision Framework for Phase 2 Launch

### B.1 Launch Criteria (All Must Be Met)

Phase 2 launch requires ALL of the following at the Month 6 assessment gate:

| Criterion | Minimum Threshold | Strong Signal | Data Source |
|-----------|------------------|---------------|-------------|
| Individual adoption: Tier 1 guide downloads | ≥1,000 cumulative views | ≥2,500 views | Gist traffic dashboard |
| Individual adoption: Tier 2-3 guide downloads | ≥500 cumulative views | ≥1,500 views | Gist traffic dashboard |
| Organizational adoption: Stage 2+ engagement | ≥3 Tier 1 organizations reached internal discussion or higher | ≥6 organizations | Email tracker |
| Individual testimonials | ≥1 per week average over 4-week period | ≥3/week | Feedback email and form |
| Feedback volume: Form responses | ≥100 total submissions | ≥300 submissions | Google Form export |
| Gap consensus | Top 3 gaps mentioned by ≥30% of respondents | ≥50% | Monthly synthesis |
| No critical open Errors/Bugs | All Error/Bug issues resolved or actively managed | — | GitHub issues / help desk |

If any criterion is below the minimum threshold at Month 6, do not launch Phase 2. Instead, diagnose the failure mode (using the Section E framework in `post-distribution-impact-tracker.md`) and address the root cause before reassessing.

### B.2 Stop Criteria (Any Sufficient to Halt Phase 2 Launch)

**Do NOT launch Phase 2 if**:

1. **Individual adoption has stalled**: Fewer than 500 combined guide views in Month 3, and no upward trajectory. This indicates a distribution or messaging failure that Phase 2 content will not fix. Address the distribution problem first.

2. **Zero organizational engagement by Month 3**: No Tier 1 organizational contact has reached Stage 1 engagement (read beyond the subject line). This indicates the guide is not reaching organizations at all — either the contacts are wrong, or the corpus is being filtered before review.

3. **Feedback is less than 50% actionable**: If more than half of all feedback submissions are either out-of-scope requests or contradictory (e.g., "make this simpler" and "add more technical depth" in equal proportions), the user base is not cohesive enough to guide Phase 2 content decisions. This indicates the guide is reaching the wrong audience, or has been shared into communities for whom it was not designed.

4. **Top gaps conflict with core design principles**: If the most common feedback request is "make Signal less private" or "help me avoid this guide and use regular email," the guide has reached an audience that does not share its foundational threat assumptions. This is an audience mismatch, not a content gap. Do not adjust core security principles to accommodate this feedback.

5. **Legal or safety incident associated with a guide recommendation**: If any guide step is associated with harm to a user — either because the countermeasure failed in a documented way, or because following the guide created a new risk — halt Phase 2, audit the affected section, and revise before any further distribution.

### B.3 Phase 2 Content Sequencing Decision Tree

When Phase 2 go/no-go is approved, use the following decision tree to sequence content production:

```
Step 1: Are there active organizational hardening requests (≥3 organizations)?
  YES → Begin with the most-requested organizational guide
  NO → Continue to Step 2

Step 2: Is there gap consensus (≥40% of respondents cite the same gap)?
  YES → Identify whether gap is a guide revision (quick win) or new content
    If guide revision → update current guide first; this is not Phase 2 content
    If new content → begin with the consensus-gap content area
  NO → Continue to Step 3

Step 3: Is there a regional adaptation request from a priority state (TX, NY, AZ, GA, MI, PA, WI)?
  YES → Produce the geographic supplement for the highest-feedback state
  NO → Continue to Step 4

Step 4: Is there a new threat model request with ≥5 submissions?
  YES → Evaluate against the threat model rubric (Section B.4 below)
  NO → Hold Phase 2 until more data accumulates; do not produce content for speculative needs
```

### B.4 New Threat Model Evaluation Rubric

Before committing to a new threat model document, score the candidate against four criteria (1-5 scale):

| Criterion | Scoring Guidance |
|-----------|-----------------|
| **Adversary distinctness**: Is this adversary structurally different from the current Tier 1-3 adversaries? | 5 = completely new adversary type; 3 = overlapping with existing; 1 = same adversary, minor variation |
| **Countermeasure distinctness**: Does addressing this threat model require new countermeasures not in the current guide? | 5 = new countermeasures required; 3 = adapts existing; 1 = existing guide covers it |
| **Audience size**: Is the target audience large enough to justify a dedicated document? | 5 = national audience of ≥10,000 potential users; 3 = regional/niche; 1 = fewer than 500 users |
| **Feedback demand**: How many feedback submissions requested this threat model? | 5 = ≥10 explicit requests; 3 = 5-9 requests; 1 = 1-4 requests |

**Score interpretation**: Total 16-20 → build immediately; 10-15 → build in Phase 2 queue; below 10 → defer indefinitely.

Example scoring for domestic violence survivor threat model:
- Adversary distinctness: 5 (intimate partner surveillance is structurally distinct — pre-authorized device access, shared accounts, no government involvement)
- Countermeasure distinctness: 5 (stalkerware removal, account separation, emergency device protocols are not in current guide)
- Audience size: 5 (estimated 10+ million DV survivors in US; DV organizations are a well-organized distribution network)
- Feedback demand: dependent on actual feedback data; if 8+ requests received → total score 23 → build immediately

---

## Section C: Success Metrics for Phase 2 Decision

### C.1 Quantitative Thresholds Summary

| Metric | Phase 2 Launch Trigger | Phase 2 Content Priority Trigger |
|--------|----------------------|----------------------------------|
| Guide views | ≥1,000 total | ≥2,500 total |
| Form responses | ≥100 total | ≥300 total; top gap at ≥40% |
| Org Stage 2+ adoption | ≥3 organizations | ≥6 organizations |
| Testimonials | ≥1/week | ≥3/week |
| Org policy citation | ≥1 document | ≥3 documents |
| Newsroom policy requests | ≥3 | Triggers Category 1 build |
| New threat model requests | N/A | ≥5 from same segment |
| Regional adaptation requests | N/A | ≥5 from same state |

### C.2 Qualitative Signals That Carry Veto Weight

Some qualitative signals override the quantitative thresholds — they are either strong accelerators or hard stops regardless of the numbers.

**Accelerators** (advance Phase 2 timeline regardless of quantitative threshold):
- A major newsroom (NYT, WaPo, The Intercept, ProPublica) requests the corpus for journalist training use
- A Tier 1 immigration legal organization (NILC, CLINIC, RAICES) publishes a policy document citing the corpus
- The Palantir ELITE documentation in the corpus is cited in a legal filing (even as background research)
- A law school clinic adopts the corpus for clinical training in an immigration or civil rights context
- A major security conference (DEF CON, CCC, USENIX Security) accepts a talk based on the corpus threat model

**Hard stops** (halt Phase 2 regardless of quantitative threshold):
- A guide step produces a documented safety failure (user followed guide, tool failed in a critical moment)
- The corpus is publicly associated with facilitating obstruction of justice or another legal risk to the author
- A central tool (Signal, Tails OS) announces a major security vulnerability in its current version
- The Palantir ELITE documentation in the corpus is challenged as legally inaccurate by an authoritative source

### C.3 18-Month Institutional Impact Targets

The Phase 2 decision also incorporates the 18-month targets from `tier-1-success-metrics-framework.md` Section 5. These are not Phase 2 triggers but indicators that the distribution infrastructure is working correctly:

- 3-5 documented sustained adoptions (Stage 4) among Tier 1 organizations
- 1+ peer-reviewed or conference paper citation in security or immigration law context
- Organizations that received the corpus have collectively reached ≥500 individuals through training or referral
- Framework referenced in 1+ legal filing, legislative testimony, or published civil rights position paper

If the 18-month review shows that these institutional impact targets have not been met, Phase 2 expansion should pause while the organizational distribution infrastructure is diagnosed and repaired. Building more content for an audience that is not yet consistently reached does not solve a distribution problem.

---

## Section D: Phase 2 Build-Out Sequence

Based on the prioritization framework, the recommended Phase 2 sequence (contingent on feedback data validating each trigger) is:

**Sequence 1 (Months 7-9, if triggers met)**:
- Organizational hardening template for immigration legal aid clinics (most direct connection to Tier 1 organizational outreach)
- Texas geographic supplement (most urgent regional adaptation given enforcement environment and lack of DROP equivalent)

**Sequence 2 (Months 10-12, if triggers met)**:
- Newsroom hardening policy template (contingent on 3+ newsroom requests)
- Domestic violence survivor threat model (contingent on DV organization feedback; scores highest on rubric)

**Sequence 3 (Months 13-18, if triggers met)**:
- Labor organizing threat model (contingent on 5+ union/organizer requests)
- Signal group administration deepening (contingent on 3+ scale requests)
- New York geographic supplement (if NY-specific feedback volume warrants)

**Do not build** without trigger evidence:
- Monero deepening (build only if activists adopt Monero at meaningful scale — current US adoption is 18% of crypto users for any privacy coin, not specifically Monero)
- Election observer OpSec (build only if election integrity organizations make direct requests — too narrow to justify without demand evidence)
- Speculative international adaptations (no evidence base yet)

---

*Document complete. The Phase 2 decision is made at the Month 6 assessment gate using the criteria in Section B. Content sequence follows the decision tree in Section B.3 based on actual feedback data from `feedback-collection-protocol.md` Section 3 and the per-organization tracking data from `tier-1-success-metrics-framework.md`. Do not build Phase 2 content in anticipation of feedback; build in response to it.*

**Sources**:
- Domestic violence survivor digital security needs: [EFF Street Level Surveillance — stalkerware](https://sls.eff.org/)
- Monero adoption US statistics: [Privacy coins regulatory environment 2025](https://coinlaw.io/privacy-coins-vs-regulatory-compliance-statistics/)
- Chainalysis Reactor 3.0 detection improvement: [TRM Labs Monero traceability research](https://www.trmlabs.com/resources/blog/the-rise-of-monero-traceability-challenges-and-research-review)
- Section 702 three-year renewal (no warrant requirement): internal project tracking (see surveillance-tracking.md, CHECKIN.md)
- SAFETAG adoption evidence (audit alone is insufficient): [Internews SAFETAG evaluation](https://greaterinternetfreedom.org/success_stories/evaluation-findings-safetag-audits-increase-digital-security-of-organizations-and-lead-to-changes-in-attitude-and-behavior/)
- Freedom of the Press Foundation journalist training scale: [FPF Digital Security Education](https://freedom.press/digisec/)
- California DELETE Act DROP enforcement penalties: [CPPA DROP regulations](https://cppa.ca.gov/regulations/drop.html)
