---
title: "Phase 2 Activation Routing Matrix — Day 7 Checkpoint Output to Domain Execution"
subtitle: "Domains 51, 59, 48, 49-50, 57 — Timing, Resource Allocation, Pre-Staged Templates"
created: 2026-06-17
purpose: >
  Maps each engagement strength outcome (STRONG / MODERATE / WEAK) to a specific
  domain activation sequence, timing schedule, and resource allocation scenario.
  The input is the composite signal per domain from the Day 7 checkpoint.
  The output is a deterministic activation queue with no ambiguity.
domains_active: [51, 59, 48]
domains_queued: [49, 50, 57]
hard_deadlines:
  domain_59: "June 25-30 (Senate Finance CTC markup)"
  domain_51: "July 1 (California Fair Elections Act ballot lock)"
  domain_48: "July 15 (Virginia Right to Vote Coalition integration)"
  domains_49_57: "July 1 (Phase 2 Batch 2 gate)"
input_from: "DAY_7_CHECKPOINT_EXECUTION_DECISION_FRAMEWORK.md (Section 3, Branch selection)"
companion_docs:
  - "DAY_7_CHECKPOINT_EXECUTION_DECISION_FRAMEWORK.md"
  - "DAY_7_CHECKPOINT_MEASUREMENT_DASHBOARD_TEMPLATE.md"
  - "DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md"
  - "DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md"
  - "DOMAINS_49_50_PARALLEL_EXECUTION_ORCHESTRATION.md"
  - "PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py"
status: production-ready
confidence: 90%
---

# Phase 2 Activation Routing Matrix

*Resistance Research — Phase 2 Domain Sequencing*
*June 17, 2026 — Day 7 Checkpoint Dispatch Layer*

**Lead finding**: The three active domains (51, 59, 48) each have independent deadline clocks and independent Tier 2 activation thresholds. Domain 59's Senate Finance override makes it the only domain that activates Tier 2 regardless of signal strength. Domains 51 and 48 gate on engagement signal. Domains 49-50 and 57 gate on the July 1 T+14 coalition transition signal. This matrix maps all combinations.

---

## Section 1: Domain Status at June 17 Checkpoint

| Domain | Topic | Sent | Replies (STRONG / MOD) | Days to Deadline | Clock Status |
|--------|-------|------|------------------------|-----------------|--------------|
| 59 | Economic Precarity / CTC | 5/5 Wave 1 (June 9-11) | 0 STRONG / 2 MOD | 8-13 (Senate markup) | T+8, past Day 7 |
| 51 | Campaign Finance / Dark Money | 0/5 staged | 0 / 0 | 14 (California ballot) | Clock not started |
| 48 | Criminal Justice / Civic Exclusion | 0/6 staged | 0 / 0 | 28 (Virginia coalition) | Clock not started |
| 49 | Environmental Justice / Redistricting | Research complete | n/a | Queued post-July 1 | Queued |
| 50 | Voting Rights Architecture | Research complete | n/a | Queued post-July 1 | Queued |
| 57 | Multilateral Withdrawal / Executive Authority | Research complete | n/a | Queued; UNGA Aug 10 | Queued |

---

## Section 2: Domain 59 — Activation Routing

Domain 59 is the time-critical domain. The Senate Finance CTC markup window (June 25-30) is hard. The activation sequence is partially forced regardless of engagement signal.

### Signal → Activation Table (Domain 59)

| Signal at T+7 | Tier 2 Action | Timing | Research Sprint | Command |
|---------------|--------------|--------|-----------------|---------|
| **STRONG** (2+ STRONG from 5 Wave 1 contacts) | Activate all 4 Tier 2 contacts immediately (EPI, Demos, NELP, NHLP) | Same day as STRONG determination | Full sprint: Zones 1-2 (Senate brief supplement, 4-5h) | `--activate-tier2 59 STRONG` |
| **MODERATE** (1 STRONG or 3+ MODERATE) | Activate EPI + Demos (highest alignment); NELP + NHLP at T+10 | June 20-21 (2-3 day delay from checkpoint) | Zones 1-2 research sprint | `--activate-tier2 59 MODERATE` |
| **WEAK** (0 STRONG, 0-2 MOD) | Senate markup override: activate EPI + Demos regardless | June 20-21 (forced, not gated on signal) | No sprint; distribute from existing 44-citation document | `--activate-tier2 59 WEAK` |
| **DIAGNOSTIC** (<80% delivery) | Resolve bounces first; then apply WEAK rule for confirmed-delivery contacts | After bounce resolution | No sprint | Fix bounces → `--activate-tier2 59 WEAK` |

**Current state June 17**: WEAK / BELOW THRESHOLD. Script output June 17 03:19 UTC confirmed forced Tier 2 activation for June 20-21 due to Senate markup pressure. No STRONG threshold required for this activation.

### Domain 59 Tier 2 Contact Queue

Execute in order. 45-minute stagger between sends.

| Priority | Organization | Contact / Address | Send Window | Template Source |
|----------|-------------|-------------------|-------------|-----------------|
| 1 | Economic Policy Institute | researchdept@epi.org (UNCONFIRMED — verify at epi.org/about/contact before send) | June 20 (T+1 from reassessment) | `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 2 |
| 2 | Demos | info@demos.org (confirmed; note: Taifa Smith Butler is current President, not Chiraag Bains who departed 2021) | June 20 (T+45 min after EPI) | `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 2 |
| 3 | National Employment Law Project | info@nelp.org | June 20 (T+90 min after EPI) | `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 2 |
| 4 | National Housing Law Project | info@nhlp.org | June 21 (next day, if capacity allows) | `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 2 |

**EPI email address warning**: researchdept@epi.org is listed in the contact verification files as unconfirmed. Before sending, visit epi.org/about/contact and use the web form if the direct address is not confirmed.

### Domain 59 Phase 2 Batch 2 Gate (Domain 49-50 integration)

Domain 59's economic precarity research is an analytical input to Domains 49 (Environmental Justice / Redistricting) and 50 (Voting Rights Architecture). The Phase 2 Batch 2 activation logic requires at least one Domain 59 Tier 1 organization (CBPP, ITEP, MomsRising, NWLC, AFL-CIO) to have engaged at STRONG before Domain 49-50 co-distribution with economic justice organizations begins. As of June 17, this gate is not yet cleared — 2 MODERATE replies do not qualify.

---

## Section 3: Domain 51 — Activation Routing

Domain 51 is gated on the July 1 California Fair Elections Act deadline. Wave 1 has not yet been sent. The routing matrix governs what happens at Domain 51's T+7 (approximately June 24-25 if Wave 1 goes out June 17-18).

### Signal → Activation Table (Domain 51)

| Signal at T+7 (~June 24-25) | Tier 2 Action | Timing | Research Sprint | Command |
|-----------------------------|--------------|--------|-----------------|---------|
| **STRONG** (2+ STRONG from 5 Wave 1-2 contacts) | Activate all 13 Tier 2 contacts in 3 waves (initial 3 → secondary 5 → extended 5) | Same day as STRONG | Zones 1-2 (FEC enforcement addendum, 4-5h) | `--activate-tier2 51 STRONG` |
| **MODERATE** (1 STRONG, or any CLC reply) | Activate initial 3 Tier 2 contacts; secondary 5 at T+14 | June 25-26 (checkpoint + 1 day) | Zones 1-2 research sprint | `--activate-tier2 51 MODERATE` |
| **WEAK** (0 STRONG, 0-1 MODERATE) | Hold Tier 1 expansion until T+14 (July 1); activate initial 3 only on July 1 | July 1 | No sprint until T+14 signal | Hold until `--activate-tier2 51 WEAK` on July 1 |
| **DIAGNOSTIC** (<80% delivery) | Resolve bounces, then apply WEAK rule | After bounce resolution | No sprint | Fix bounces first |

**Special rule — CLC as automatic MODERATE elevator**: Any reply from Erin Chlopak (echlopak@campaignlegalcenter.org) or the Campaign Legal Center general inbox automatically elevates Domain 51 to MODERATE, regardless of reply quality. CLC's campaign finance constitutional team is the highest-value Domain 51 relationship. Even a boilerplate acknowledgment from CLC is a relationship confirmation that authorizes Tier 1 expansion.

### Domain 51 Tier 2 Contact Queue

**Initial 3 (activate on MODERATE signal)**:

| Priority | Organization | Contact / Address | Send Window | Template Source |
|----------|-------------|-------------------|-------------|-----------------|
| 1 | True North Research | info@truenorthresearch.org | Day 1 after checkpoint | `DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md` Zone 3 |
| 2 | Montana I-194 Campaign | Via Ballotpedia Montana I-194 2026 campaign contact | Day 1 | `DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md` Zone 4 |
| 3 | Michigan Clean Elections Coalition | Via michiganadvance.com contact | Day 1-2 | `DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md` Zone 4 |

**Secondary 5 (activate 7 days after initial 3, or on STRONG signal immediately)**:

| Priority | Organization | Contact / Address | Alignment |
|----------|-------------|-------------------|-----------|
| 4 | New Mexico Common Cause | commoncause.org/new-mexico | State ballot + DISCLOSE Act alignment |
| 5 | Issue One ReFormers Caucus | issueone.org/about/reformers-caucus | Bipartisan reform network |
| 6 | ACLU Voting Rights Project | slakin@aclu.org (Sophia Lin Lakin) | Citizens United constitutional challenge |
| 7 | UCLA Election Law Center | rhasen@law.ucla.edu (Rick Hasen) | Academic credentialing |
| 8 | Loyola Law School | jlevitt@lls.edu (Justin Levitt) | Academic credentialing |

**Extended 5 (activate on STRONG signal only, or at July 1 T+14 if MODERATE with 2+ STRONG total)**:

| Priority | Organization | Contact / Address | Alignment |
|----------|-------------|-------------------|-----------|
| 9 | End Citizens United / Let America Vote | info@endcitizensunited.org | Direct mission alignment |
| 10 | Public Citizen | cholman@citizen.org (Craig Holman) | DISCLOSE Act advocacy |
| 11 | Brennan Center | ghoshs@brennan.law.nyu.edu (Saurav Ghosh) | Campaign finance constitutional team |
| 12 | Democracy 21 | fwertheimer@democracy21.org (Fred Wertheimer) | Clean election legislation |
| 13 | OpenSecrets | info@opensecrets.org | Dark money data credentialing |

### Domain 51 Resource Allocation Scenarios

**Full execution (STRONG signal)**: 30-35 researcher-hours over 7 days. Sends all 13 Tier 2 contacts in 3 waves. Includes 10-14h research sprint across all 5 zones. Produces Zone 1 FEC enforcement addendum (2,000 words, statute-risk case list) and Zone 2 Crypto/AI PAC architecture analysis (2,500 words). Both feed directly into Senate DISCLOSE Act testimony readiness and California ballot campaign materials.

**Selective execution (MODERATE signal)**: 10-12 researcher-hours over 4-5 days. Sends initial 3 + secondary 5 Tier 2 contacts. Research sprint limited to Zones 1-2 (7-8h). Produces Zone 1 addendum only. Adequate for California July 1 deadline.

**Diagnostic / minimum execution (WEAK signal)**: 2-3 researcher-hours. No research sprint. Activates initial 3 Tier 2 contacts on July 1 with existing 65-citation research document. Adequate for maintaining organizational relationships until T+14 signal arrives.

---

## Section 4: Domain 48 — Activation Routing

Domain 48 is the least time-pressured of the three active domains at this checkpoint. The Virginia July 15 deadline is 28 days away. The routing is driven primarily by signal quality rather than deadline urgency.

### Signal → Activation Table (Domain 48)

| Signal at T+7 (~June 24-25) | Tier 2 Action | Timing | Template Source |
|-----------------------------|--------------|--------|-----------------|
| **STRONG** (2+ STRONG from 6 Wave 1-2 contacts) | Activate NAACP LDF + FFJC immediately; ACLU VA on June 27-28 | Same day as STRONG | `PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md` |
| **MODERATE** (1 STRONG from Wave 1-2) | Activate FFJC only; hold LDF for June 27 checkpoint | June 25-26 | `PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md` |
| **WEAK** (0 STRONG) | ACLU Virginia contingency path only (acluva@acluva.org — Mary Bauer) | July 1 T+14 | Contingency template |

**Priority contact rationale**:
- Sentencing Project (nporter@sentencingproject.org) replied first in Domain 48 ecosystem historically — their "Locked Out" data is the primary empirical source for the document. A response from Nicole Porter is the single most predictive signal of Domain 48 coalition viability.
- Prison Policy Initiative (info@prisonpolicy.org) — jury exclusion and housing barrier research is primary source for Sections 2.2 and 2.5. Their engagement validates the democratic design extension argument.
- If both Sentencing Project and PPI remain non-responsive at T+14, the likely cause is routing — these organizations receive substantial research inbound. Follow-up should personalize to their specific published finding that is cited in the domain document.

### Domain 48 Tier 2 Contact Queue

| Priority | Organization | Contact / Address | Activate Condition |
|----------|-------------|-------------------|--------------------|
| 1 | NAACP Legal Defense Fund | info@naacpldf.org (Janai Nelson) | 2+ STRONG from Wave 1-2 |
| 2 | Fines and Fees Justice Center | info@finesandfeesjusticecenter.org (Joanna Weiss) | 1+ STRONG from Wave 1-2 |
| 3 | ACLU of Virginia | acluva@acluva.org (Mary Bauer) | Contingency if M4BL unresponsive, or June 27 checkpoint |
| 4 | PPI follow-up | Wendy Sawyer or Leah Wang for data validation | If Wave 1 PPI produced MODERATE engagement |

---

## Section 5: Domains 49-50 and 57 — Queued Activation

These three domains have completed research but have not yet entered the distribution phase. They activate based on the July 1 T+14 coalition transition gate and the Phase 2 Batch 2 signal from Domains 51, 59, and 48.

### Domain 49 — Environmental Justice / Redistricting

**Gate condition**: Two or more organizations from {CBPP, Georgetown CCF, AFGE, Brennan Center, Black Mamas Matter Alliance} have replied STRONG to Phase 1-2 active domains by July 1. This is the cross-domain STRONG threshold from `PHASE_1_COALITION_LEVERAGE_MATRIX.md` Section 5.

**If gate clears (July 1)**: Activate `DOMAIN_49_EXECUTION_PREFLIGHT.md`. Priority contacts: NAACP LDF + Democracy Docket + Campaign Legal Center (Redistricting/VRA team). Timeline: July 1-15. The Callais redistricting cascade (Louisiana signed May 30, 2026) and Alabama, Tennessee, South Carolina redistricting litigation are the urgency frame.

**If gate does not clear (July 1 WEAK across all domains)**: Hold Domain 49 activation. The VRA redistricting coalition requires at least one STRONG organizational relationship established first — cold outreach on Domain 49 before any prior domain has generated STRONG engagement would reduce response probability.

**Key urgency factor**: Redistricting cascade litigation windows close state by state through August 2026. Each week of delay reduces the window for Domain 49 research to influence active litigation. July 1-15 is the priority window.

### Domain 50 — Voting Rights Architecture

**Gate condition**: Same as Domain 49 — two or more cross-domain STRONG signals by July 1.

**Sequencing note**: Domain 50 activates 5-7 days after Domain 49 per `DOMAINS_49_50_PARALLEL_EXECUTION_ORCHESTRATION.md`. They share organizational contacts (NAACP LDF, Democracy Docket, CLC) and must be staggered to avoid contact fatigue. Domain 49 leads; Domain 50 follows with a distinct angle (constitutional framework vs. litigation tactics).

**If gate clears**: July 5-15 activation window. Domain 50 contacts receive the Voting Rights Architecture analysis as a companion to the Domain 49 redistricting brief. The combined send positions the two documents as a research series, not a volume flood.

**If gate does not clear**: Domain 50 holds alongside Domain 49. No independent activation.

### Domain 57 — Multilateral Withdrawal / Executive Authority

**Gate condition**: Different from Domains 49-50. Domain 57 has an independent deadline: the UN General Assembly session opens in September, with the UNGA high-level segment around August 10. The international law coalition (ASIL, Council on Foreign Relations, Stimson Center) is most receptive during June-July before the UNGA prep cycle closes.

**Activation trigger for Domain 57**: Does not require cross-domain STRONG signal. Activate independently based on the UNGA calendar:
- June 30 - July 10: Optimal send window. ASIL members and CFR senior fellows are completing pre-UNGA analysis; Domain 57's treaty withdrawal and executive authority research is directly relevant to their briefing cycle.
- After July 15: Window narrows. Organizations transition to active UNGA preparation and are less receptive to new research introductions.
- `domain-57-distribution-runbook.md` and `DOMAIN_57_GIST_URL.txt` are production-ready.

**Resource requirement**: Domain 57 activation requires only the distribution execution (1-2 hours). No additional research sprint needed — the existing research document is complete. This is the lowest-cost Batch 2 activation.

---

## Section 6: Resource Allocation Scenarios

### Full Execution (STRONG signal across 2+ domains)

Available from July 1 if the Day 7-14 cycle produces strong engagement.

| Time Period | Activity | Hours Required | Domains |
|-------------|----------|---------------|---------|
| June 17-21 | D59 Tier 2 activation (Senate forced) | 2-3 | 59 |
| June 20-24 | D59 research sprint Zones 1-2 | 5-7 | 59 |
| June 25-26 | D51 Tier 1 national expansion | 1-2 | 51 |
| June 26-29 | D51 research sprint Zones 1-2 | 5-7 | 51 |
| June 25-27 | D48 Tier 2 NAACP LDF + FFJC | 1 | 48 |
| July 1-10 | D49 environmental justice distribution | 3-4 | 49 |
| July 5-15 | D50 voting rights architecture distribution | 3-4 | 50 |
| July 1-10 | D57 multilateral withdrawal distribution | 1-2 | 57 |
| **Total** | **Full Phase 2 execution** | **~25 hours over 28 days** | **All** |

### Selective Execution (MODERATE signal, 1 STRONG per domain)

| Time Period | Activity | Hours Required | Domains |
|-------------|----------|---------------|---------|
| June 17-21 | D59 forced Tier 2 (2 of 4 contacts) | 1 | 59 |
| June 25-26 | D51 initial 3 Tier 2 contacts | 1 | 51 |
| June 25-26 | D51 Zones 1-2 sprint | 4-5 | 51 |
| June 27-28 | D48 FFJC only | 0.5 | 48 |
| July 5-10 | D57 distribution (calendar-gated, not signal-gated) | 1-2 | 57 |
| July 1-15 | D49 + D50 gated on T+14 signal | 6-8 (if gate clears) | 49, 50 |
| **Total** | **Selective Phase 2** | **~14-18 hours over 28 days** | **Most** |

### Diagnostic / Minimum Execution (WEAK signal, 0 STRONG across all domains)

| Time Period | Activity | Hours Required | Domains |
|-------------|----------|---------------|---------|
| June 17-21 | D59 forced Tier 2 (Senate override) | 1 | 59 |
| June 25 | D51 initial 3 Tier 2 contacts only | 0.5 | 51 |
| July 1-5 | D48 ACLU Virginia contingency | 0.5 | 48 |
| July 5-10 | D57 distribution (calendar-gated) | 1-2 | 57 |
| July 15 | Reassess D49 + D50 with 28-day accumulated signal | 1 | 49, 50 |
| **Total** | **Minimum Phase 2 maintenance** | **~5-6 hours** | **Limited** |

---

## Section 7: Pre-Staged Scripts and Templates Per Domain

### Domain 59 — Active Send Templates

All templates in `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md`. Pre-staged for the Senate Finance markup window. Key elements already written:
- Subject line: "Economic precarity + democratic participation — CTC refundability research for Senate Finance markup"
- Opening: cites recipient organization's own analysis of the income-voter participation relationship
- Gist URL: `https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba` (confirmed HTTP 200)
- Sender fills: [YOUR_NAME], [YOUR_CONTACT_INFO]
- Frame update for post-markup scenario: `DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md` Part 7, Contingency 1

### Domain 51 — Active Send Templates

Wave 1 templates in `DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md`. Wave 2 templates in `DOMAIN_51_WAVE_2_EMAIL_EXECUTION_PACKAGE.md`.
- Email 1: echlopak@campaignlegalcenter.org — Subject: "Constitutional architecture research on Citizens United — Hawaii/Montana model + FEC collapse analysis"
- Email 2: info@issueone.org — Subject: "Dark money architecture research — FEC collapse documentation + state ballot measure analysis"
- Emails 3-5 (Wave 2 California contacts): in `DOMAIN_51_WAVE_2_EMAIL_EXECUTION_PACKAGE.md`
- Gist URL: `https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372` (confirmed HTTP 200)
- Tier 1 national expansion templates (OpenSecrets, Democracy 21, Public Citizen): `DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md` Zone 3

### Domain 48 — Active Send Templates

Templates in `DOMAIN_48_EMAIL_TEMPLATE_SET.md`. Template A with organization-specific variants.
- Send 1: nporter@sentencingproject.org — Template A, Sentencing Project variant (cite "Locked Out" report)
- Send 2: info@prisonpolicy.org — Template A, PPI variant (cite jury exclusion synthesis)
- Gist URL: `https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8` (confirmed HTTP 200)
- Sender fills: {{YOUR_NAME}}, {{YOUR_CONTACT_INFO}} ({{ORG_NAME}} and {{DECISION_MAKER}} are resolved per contact list)
- Tier 2 templates (NAACP LDF, FFJC, ACLU VA): `PHASE_2_TIER_2_ACTIVATION_PROTOCOLS.md`

### Domain 57 — Distribution Templates

Templates in `domain-57-distribution-runbook.md`. Gist: `DOMAIN_57_GIST_URL.txt`.
- Calendar trigger: June 30 - July 10 (UNGA pre-session)
- No signal gate required — activate independently on calendar

### Domains 49-50 — Queued Templates

Both runbooks production-ready:
- `DOMAIN_49_RESEARCH_EXECUTION_RUNBOOK.md`
- `DOMAIN_50_RESEARCH_EXECUTION_RUNBOOK.md`
- Orchestration: `DOMAINS_49_50_PARALLEL_EXECUTION_ORCHESTRATION.md`
- Contact list: activate only after July 1 gate clears; do not cold-send before prior-domain STRONG signal established

---

*Matrix prepared June 17, 2026. All Gist URLs verified HTTP 200 as of June 17 03:19 UTC. Contact addresses verified June 5-16, 2026. Script commands reference `PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py` (1,900 lines, all three domains supported).*
