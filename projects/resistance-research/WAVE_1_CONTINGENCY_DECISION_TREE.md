---
title: "Wave 1 Contingency Decision Tree — Mixed-Signal Outcome Framework"
created: 2026-05-18
status: ACTIVE — reference at May 25 Week 1 checkpoint; earlier checkpoints noted where applicable
scope: "Per-constituency response analysis, impact scoring, Phase 2 sequencing under three scenarios, Tier 2 timing triggers"
audience: "thorn — decision document for Phase 2 path selection based on actual Wave 1 results"
companion_files:
  - WAVE_1_RESPONSE_TRACKING_TEMPLATE.md
  - WAVE_1_DAILY_MONITORING_TEMPLATE.md
  - PHASE_2_LAUNCH_DECISION_TRIGGERS.md
  - PHASE_2_LAUNCH_ROADMAP_POST_WAVE1.md
  - POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md
---

# Wave 1 Contingency Decision Tree

**Primary use date**: May 25 Week 1 checkpoint, after full response window closes  
**Early activation**: May 21 72-hour checkpoint if signals are unambiguous (very strong or very weak)  
**Decision required from user**: Phase 2 scenario selection (STRONG / MODERATE / WEAK path) — no autonomous execution without explicit user approval

---

## PART 1: The Mixed-Signal Problem

Wave 1 sends to 40–45 organizations across five constituencies. The constituencies have different response cycles, different policy relevance windows, and different organizational relationships to the proposal's 40-domain framework. This means you will almost certainly receive mixed signals rather than a clean outcome.

The purpose of this decision tree is to resolve mixed signals into a single actionable path. It does this by:
1. Scoring each constituency independently
2. Weighting constituencies by their Phase 1-to-Phase 2 leverage value
3. Applying a composite score to determine the overall Phase 2 scenario
4. Providing specific Phase 2 domain sequences for each scenario

The framework is conservative: when signals are ambiguous, it favors the lower-leverage scenario to avoid burning Tier 2 contacts before messaging is validated.

---

## PART 2: Per-Constituency Response Scoring

At the May 25 checkpoint, complete this scoring table. Use response data from WAVE_1_RESPONSE_TRACKING_TEMPLATE.md.

### 2.1 Constituency Impact Weights

Not all constituencies carry equal Phase 1-to-Phase 2 leverage. Weights reflect the structural role each constituency plays in the democratic renewal proposal's adoption pathway.

| Constituency | Weight | Why This Weight |
|---|---|---|
| Law Schools (academic institutions) | 30% | Academic legitimation is the primary Phase 2 unlock — law clinics, journals, and testimony pipelines depend on faculty adoption. A response from Goodman (Just Security) or Chenoweth (Harvard) opens cascade adoption across law review and policy journal networks. |
| Think Tanks / Policy Organizations | 30% | Direct policy influence pathway — Brennan Center, Protect Democracy, and Elias Law Group have direct relationships with Democratic legislators, AG coalitions, and election administration networks. A response from this constituency unlocks Phase 2 legislative window distribution. |
| Labor Unions | 20% | Labor federations have member communication infrastructure (newsletters, local chapter briefings) that can scale distribution rapidly. Union adoption also provides the proposal with a working-class legitimacy framing that protects against "elite academic" dismissal. |
| Immigration Legal Aid | 15% | Highest relevance to Domain 42 and related domains. Response from this constituency validates the immigration-specific framing and opens direct-to-community distribution paths that academic and policy org channels cannot reach. |
| Other Academic / Civil Society | 5% | Secondary validation — important for long-term adoption but not a primary Phase 2 lever within the May–August 2026 policy window. |

### 2.2 Per-Constituency Response Score Calculation

For each constituency, calculate a Constituency Response Score (CRS) on a 0–100 scale.

**CRS formula**: (Number of Score 3+ responses / Total sent to constituency) × 100

| Constituency | Sent Count | Score 3+ Responses | CRS (%) | Weight | Weighted Score |
|---|---|---|---|---|---|
| Law Schools | ___ | ___ | ___% | 0.30 | ___ |
| Think Tanks / Policy Orgs | ___ | ___ | ___% | 0.30 | ___ |
| Labor Unions | ___ | ___ | ___% | 0.20 | ___ |
| Immigration Legal Aid | ___ | ___ | ___% | 0.15 | ___ |
| Other Academic / Civil Society | ___ | ___ | ___% | 0.05 | ___ |

**Composite Wave 1 Score**: Sum of Weighted Scores = ___ (0–100)

| Composite Score | Classification |
|---|---|
| 40+ | STRONG |
| 25–39 | MODERATE |
| <25 | WEAK |

---

## PART 3: Mixed-Signal Interpretation Scenarios

These are the most likely mixed-signal combinations and their interpretations. Find the scenario that most closely matches your actual data.

### Scenario A: Law Schools High, Unions Low (e.g., Law Schools >40% CRS, Unions <20% CRS)

**What this means**: The proposal is landing with credentialed researchers but not with member-based organizations. Most likely cause: the framing is too technical or policy-wonk for union communicators to quickly adapt for member audiences, OR union contacts did not receive a sufficiently tailored version of the email that connected the proposal to their specific labor concerns.

**Phase 2 implication**: Prioritize academic and policy org Tier 2 contacts first. Develop a separate union-specific summary document before Tier 2 union outreach. Do not send Tier 2 union contacts the same email template used for Tier 1.

**Domain prioritization**: Lead with Domain 37 (electoral security, high union relevance — voting rights affect members directly) and Domain 39 (healthcare, direct member benefit framing). Delay Domain 57 (multilateral withdrawal) for this constituency — it is the weakest fit for a labor audience.

### Scenario B: Immigration Legal Aid High, Think Tanks Low (e.g., Immigration >40% CRS, Think Tanks <20% CRS)

**What this means**: The proposal is resonating with direct-service organizations but not with policy intermediaries. Most likely cause: think tank contacts did not perceive the proposal as fitting their existing policy agenda, OR the email was caught in institutional filtering/routing.

**Phase 2 implication**: Immigration legal aid contacts are high-quality amplifiers for community-facing distribution. Their engagement validates the proposal's substantive analysis of immigration-related domains. However, the Phase 2 policy window leverage (especially Domain 42 and Domain 56) depends heavily on think tank and legislative intermediaries. Follow up with think tank contacts directly — consider a revised email that explicitly names a policy window (the June 1 HHS rule, the August 2 EU AI Act enforcement date) to make the timing relevance clearer.

**Domain prioritization**: Advance Domain 42 (DEA briefing content) to Tier 2 immigration networks immediately — this is the highest-urgency policy window for this constituency. Domain 39 (healthcare) also has strong immigration legal aid relevance.

### Scenario C: Think Tanks High, Law Schools Low (e.g., Think Tanks >40% CRS, Law Schools <20% CRS)

**What this means**: The proposal is seen as policy-relevant by advocacy intermediaries but has not yet landed with academic validators. This is actually a strong operational signal — policy orgs can begin using the proposal in their existing work while academic validation develops on a slower timeline.

**Phase 2 implication**: Proceed with Phase 2 research on policy-window-urgent domains immediately (Domain 57, Domain 59). Do not wait for academic validation before launching Phase 2. Academic contacts should receive a follow-up email after 10 days from initial send — if they have not replied, a single follow-up is appropriate at the 2-week mark.

**Domain prioritization**: Domain 57 (multilateral withdrawal, August 10 distribution deadline) and Domain 59 (economic precarity, direct policy org audience) should lead Phase 2.

### Scenario D: All Constituencies Low (<20% CRS across all sectors)

**What this means**: Delivery issues, messaging misalignment, or timing problems. Before concluding that the proposal is not resonating, check: Were there widespread soft bounces that may resolve on resend? Did emails land in spam for some recipients? Was the send window (08:00–10:00 UTC) poorly timed for the US east coast morning rush?

**Phase 2 implication**: Do not launch Phase 2 research until a post-mortem diagnosis is complete (see Part 5, Scenario C protocol). A weak response from all constituencies simultaneously suggests a structural issue with the distribution method rather than with the proposal content.

### Scenario E: One High-Score Reply That Changes Everything

**What this means**: A single Score 4 or Score 5 response from a high-weight contact (Goodman, Weiser, Elias, Chenoweth, Bassin) outweighs a lower overall response rate. A public citation by Marc Elias or a Just Security publication request from Ryan Goodman is a STRONG signal even if 90% of the contact list has not replied.

**Phase 2 implication**: Activate STRONG scenario (see Part 4) regardless of aggregate CRS, because a high-credibility public endorsement generates momentum that substitutes for breadth of initial response. Flag this in the completion log as a High-Value Signal and notify orchestrator immediately.

---

## PART 4: Phase 2 Domain Prioritization by Scenario

### STRONG Response Path (Composite Score 40+)

**Trigger**: Activate immediately upon confirmation at May 25 checkpoint, or earlier if Score 4+ signals arrive from multiple constituencies before May 21.

**Immediate actions (Week of May 25)**:
- Commission Phase 2 research on Domain 57 (multilateral withdrawal) — August 10 distribution deadline is load-bearing. Domain 57 research takes 2–3 sessions; starting May 25 gives 10 weeks before the August 10 deadline.
- Commission Phase 2 research on Domain 59 (economic precarity) — highest general-audience relevance, broadens the proposal's reach beyond specialist audiences.
- Begin Tier 2 pre-contact list construction (Week of May 25). First Tier 2 sends should go out May 26–28.

**Domain sequence (STRONG)**:
1. Domain 57 (multilateral withdrawal) — research weeks May 25–June 7
2. Domain 59 (economic precarity) — research weeks June 1–14 (parallel with Domain 57 where possible)
3. Domain 38 (AI regulatory capture) — research weeks June 8–21 (highest relevance to August 2 EU AI Act enforcement deadline)
4. Domain 39 (healthcare access) — research weeks June 15–28 (June 1 HHS rule creates urgency framing)
5. Domain 40 (surveillance capitalism) — research weeks June 22–July 5

**Tier 2 timing (STRONG)**: First Tier 2 outreach batch — May 26–28, 2026. Include explicit reference to Tier 1 engagement signals in Tier 2 outreach email (social proof framing: "following engagement from [Goodman/Weiser/etc.]").

### MODERATE Response Path (Composite Score 25–39)

**Trigger**: Activate at May 25 checkpoint if composite score falls in the 25–39 range.

**Immediate actions (Week of May 25)**:
- Commission Phase 2 research on electoral security + healthcare only (fastest policy leverage windows before November 2026 midterms and June 1 HHS rule).
- Hold Domain 57 and Domain 59 research pending additional validation data.
- Follow up with non-responding Tier 1 contacts from highest-weight constituencies (Law Schools, Think Tanks) — single follow-up email at 2-week mark (June 1–2).

**Domain sequence (MODERATE)**:
1. Domain 37 supplement (electoral security deep-dive) — highest midterm relevance, already has existing research base
2. Domain 39 (healthcare access) — June 1 HHS rule creates immediate framing opportunity
3. Domain 57 (multilateral withdrawal) — begin June 8 if follow-up responses are positive; delay to June 15 if follow-up responses remain sparse
4. Domain 59 (economic precarity) — begin June 15
5. Domains 38/40 — begin July based on response evolution

**Tier 2 timing (MODERATE)**: Tier 2 pre-contact begins Week of June 1 (not May 25). First Tier 2 sends go out June 1–3. This gives an additional week for Tier 1 follow-up responses to provide social proof for Tier 2 outreach.

### WEAK Response Path (Composite Score <25)

**Trigger**: Activate at May 21 72-hour checkpoint if signals are already clearly weak (zero replies, zero Gist view delta above baseline), or at May 25 checkpoint if composite score is below 25.

**Immediate actions (week of May 21–25)**:
- Do NOT proceed with Phase 2 research or Tier 2 outreach.
- Conduct a structured post-mortem of Wave 1 (see below).
- Make Phase 2 launch decision no earlier than June 1, after post-mortem diagnosis and messaging revision.

**Post-mortem questions to answer before June 1 launch**:
1. Delivery verification: Did emails land in spam? Check by sending a test email to yourself at the same institutional domains that bounced or went silent. Academic email servers (.edu) frequently have aggressive spam filters.
2. Timing verification: Were sends appropriately timed? US east-coast academics are most inbox-active Tuesday–Thursday, 14:00–18:00 UTC. If sends were Monday morning US time, resend on Wednesday afternoon.
3. Messaging audit: Does the subject line signal relevance? Does the opening paragraph address a concrete issue the contact is known to work on? Compare the templates that produced bounces or silence against the templates used in any responses received.
4. Contact quality: Were the contact addresses verified? Check the PHASE_1_CONTACT_VERIFICATION.json against current organizational directories.

**Domain sequence (WEAK)**: Determined after post-mortem, not pre-specified. The post-mortem output determines which domains to lead with in a revised Phase 2 launch.

**Tier 2 timing (WEAK)**: Tier 2 contacts are NOT reached out to until Phase 1 post-mortem is complete and at least one Tier 1 response validates revised messaging. Target: June 8–15, conditional on post-mortem completion.

---

## PART 5: Decision Matrix — IF [Pattern] THEN [Action]

| If This Is True | Then Do This | Rationale |
|---|---|---|
| ≥1 Score 4+ response from law school or think tank by May 21 | Activate STRONG path immediately, do not wait for May 25 checkpoint | A high-value signal this early is a leading indicator of broader adoption |
| 0 substantive replies but Gist delta >10 by May 21 | Classify as borderline MODERATE, follow up with clicked-but-silent contacts first | Click data suggests interest that hasn't converted to reply — a follow-up email referencing a specific policy deadline may convert |
| ≥3 hard bounces from think tank or law school contacts | Before classifying as WEAK, investigate bounce causes and resend to verified addresses | High-weight constituency bounces bias the composite score unfairly if they are deliverability failures rather than disengagement |
| Any ADOPTION_SIGNAL category response from any constituency | Immediately draft a follow-up email (within 24 hours) — do not wait for the next monitoring checkpoint | Adoption-signal responses have a conversion window; delay loses momentum |
| PARTISAN_PUSHBACK from ≥2 contacts | Schedule messaging calibration session — do not dismiss as noise | Two independent pushback responses suggest a framing issue in the specific template used for that constituency |
| Responses only from immigration legal aid, zero from law schools or think tanks | Advance Domain 42 immediately; hold Phase 2 academic distribution pending Tier 1 law school/think tank follow-up | Immigration legal aid engagement is valuable but does not substitute for academic or policy org validation for Phase 2 amplification |
| More than 5 OOO messages with return dates after June 1 | Do not count those contacts in the May 25 composite score — recheck at June 8 | OOO return-date data is useful: it tells you exactly when to follow up with absent contacts |

---

## PART 6: Tier 2 Pre-Contact Timing Triggers

Tier 2 pre-contact should only begin when at least one of the following trigger conditions is met. Do not begin Tier 2 outreach as a default action at a fixed date — anchor it to actual Phase 1 signal strength.

### Trigger A: STRONG Phase 1 (immediate Tier 2 activation)
**Condition**: Composite CRS ≥40 at May 25 checkpoint, OR Score 4+ response from ≥2 Tier 1 high-weight contacts before May 25.  
**Tier 2 pre-contact start**: May 26–28, 2026.  
**Tier 2 framing**: Lead with Tier 1 social proof — name the responding organizations (if they consented to public mention) or describe the response level without naming individuals.

### Trigger B: MODERATE Phase 1 (delayed Tier 2 activation)
**Condition**: Composite CRS 25–39 at May 25 checkpoint.  
**Tier 2 pre-contact start**: June 1–3, 2026.  
**Tier 2 framing**: Lead with the policy window urgency (June 1 HHS rule, August 10 Domain 57 deadline, November midterms) rather than social proof — you do not yet have strong social proof to offer.

### Trigger C: WEAK Phase 1 (conditional Tier 2 activation)
**Condition**: Composite CRS <25 at May 25 checkpoint.  
**Tier 2 pre-contact start**: Conditional — not before June 8, and only after post-mortem is complete and messaging revision is drafted.  
**Tier 2 framing**: If launching post-post-mortem, lead with new framing rather than the original proposal framing. The weak response is information that the original framing needs adjustment.

### Trigger D: High-Value Signal Override (immediate Tier 2 regardless of overall CRS)
**Condition**: Score 5 adoption signal from any Tier 1 contact before May 25 (public citation, briefing invitation, formal collaboration proposal).  
**Tier 2 pre-contact start**: Immediately upon confirmation of Signal, regardless of composite CRS.  
**Tier 2 framing**: Lead explicitly with the adoption signal — a public endorsement from a credentialed source is the most powerful Tier 2 acquisition lever available.
