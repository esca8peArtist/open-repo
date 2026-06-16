---
title: "Phase 2 Day 7 Checkpoint Routing Framework"
subtitle: "June 17–18, 2026 — Wave 1–2 Engagement Triage and Phase 2 Dispatch"
created: "2026-06-16"
version: 1.0
status: production-ready
checkpoint_window: "June 17 17:00 UTC — June 18 12:00 UTC"
domains: [51, 59]
waves_evaluated: [Wave 1 (June 14–15), Wave 2 (June 14–15)]
contacts_evaluated: 5
hard_deadlines:
  domain_59: "June 25–30, 2026 (Senate Finance CTC markup window)"
  domain_51: "July 1, 2026 (California Fair Elections Act campaign messaging lock)"
integration_files:
  - "PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md (success metric definitions)"
  - "PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py (orchestration tool + logging)"
  - "PHASE_2_DECISION_MEMO_JUNE_2026.md (prior user decisions on domain sequencing)"
  - "DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md (pre-existing branch logic for D51/D59)"
  - "DOMAIN_51_JUNE_16_DECISION_LOGIC.md (composite score + Tier 2 batch activation)"
  - "DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md (full 10–14h sprint scaffold)"
  - "DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md (Senate Finance express path)"
purpose: >
  Enables 30-minute June 17–18 checkpoint execution. User extracts metrics (30 min),
  cross-references triggers here (5 min), routes to a named Phase 2 action immediately.
  No deliberation required. All routing is pre-decided.
---

# Phase 2 Day 7 Checkpoint Routing Framework

**June 16, 2026 — Pre-Staged for June 17–18 Execution**

**Lead finding**: Waves 1 and 2 (Domain 51: Campaign Legal Center, Issue One, Common Cause CA, LWV California, Clean Money Action Fund; Domain 59 Wave 1: see DOMAIN_59_WAVE_1_EMAIL_EXECUTION_PACKAGE.md) were sent June 14–15. The Day 7 engagement window runs through June 21–22. The checkpoint executes June 17–18 — Day 3–4 of the engagement window — which captures first-responder replies, all Bitly click-throughs from initial open events, and any forwarding signals, while still leaving 8–12 days of runway before both hard deadlines. This framework eliminates the checkpoint-to-action gap: metrics in, routing decision out, execution begins within the same session.

---

## Section 1: Engagement Metric Definitions

*150–200 words. These definitions apply to the June 17–18 checkpoint evaluation. They derive from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Sections 3–5, adapted to Phase 2's smaller contact pool and tighter deadline structure.*

**Reply rate**: Count of substantive replies (Score 3+: explicit engagement, request for more information, forward to colleague, or adoption statement) divided by confirmed-delivered emails in each wave. Do not include hard bounces, OOO-only responses, or Score 1–2 (polite acknowledgment, form response) in the numerator. Denominator is confirmed-delivered count from the orchestration script's send log.

**Forward rate**: Count of confirmed forwarding events — either a reply that states "I've shared this with X" or an unsolicited contact from a party not on the send list who cites a Wave 1–2 contact as the source. Forward events carry a 3x weight relative to standard replies, per PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 3.2. A single forward event from any of the five Wave 1–2 contacts shifts the baseline trajectory upward regardless of reply rate.

**Engagement threshold (composite)**: The combined reply-plus-forward percentage, calculated as: ((Score 3+ reply count + (forward count × 3)) / confirmed-delivered count) × 100. This composite percent is the primary routing input for the decision tree in Section 3.

**Per-contact-tier baselines for Phase 2 waves:**

| Contact Tier | Organizations | Expected Reply Rate (Day 7) | Strong | Moderate | Weak |
|---|---|---|---|---|---|
| Tier 1 — National policy orgs | CLC (Chlopak), Issue One | 40–70% | ≥60% | 30–59% | <30% |
| Tier 1 — California ballot campaign | Common Cause CA, LWV CA, Clean Money Action Fund | 25–50% | ≥45% | 20–44% | <20% |
| Domain 59 Tier 1 — Economic policy | AFL-CIO, CBPP, NWLC (pending send) | 30–60% | ≥50% | 25–49% | <25% |

These baselines are grounded in the Phase 1 per-constituency thresholds (PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 4): law school and civil rights targets showed 25–50% Day 30 reply rates; operational advocacy organizations at the program director level (Chlopak at CLC, Kemp at Common Cause CA) show higher first-contact probability because the email is targeted to their direct program area rather than to a general inbox.

**Expected ranges across all five Wave 1–2 contacts:**
- Strong engagement: 3 or more Score 3+ replies (60%+ composite)
- Moderate engagement: 1–2 Score 3+ replies, OR any Score 4–5 reply (20–59% composite)
- Weak engagement: 0 Score 3+ replies with confirmed delivery (0–19% composite)

---

## Section 2: Tier 2 Activation Triggers

*200–300 words. Specific threshold crossings that unlock each Tier 2 action. "Tier 2" in this context means: (a) Tier 2 deep leverage contacts within Domain 51 and 59 (the next distribution wave), (b) Tier 2 leverage in CLC domain (expanded national contacts), and (c) additional domain activation (Domains 48, 57, 59 express path) per DOMAIN_51_JUNE_16_DECISION_LOGIC.md and the PHASE_2_DECISION_MEMO_JUNE_2026.md sequencing decisions.*

### Trigger Matrix: What Unlocks What

**Trigger A — Domain 59 Senate Finance Express Path (non-negotiable)**
- Condition: Senate Finance markup still active at finance.senate.gov (verify at checkpoint)
- Activates: Domain 59 express path regardless of all other engagement metrics
- Contacts: AFL-CIO (feedback@aflcio.org), CBPP (cbpp@cbpp.org), NWLC (info@nwlc.org)
- Timing: Execute same day as checkpoint, within the checkpoint session
- Source: DAY_7_CHECKPOINT_ROUTING_DECISION_TREE.md "Critical rule" — this trigger does not require any prior engagement signal; it is calendar-driven

**Trigger B — Domain 51 CLC Deep Leverage (reply-dependent)**
- Condition: Erin Chlopak (CLC) replies at Score 3+ AND/OR Issue One replies at Score 3+
- Activates: Domain 51 Tier 1 expansion: OpenSecrets (info@opensecrets.org), Democracy 21 (fwertheimer@democracy21.org), Public Citizen (cholman@citizen.org)
- Timing: Within 24 hours of checkpoint if trigger met
- If Issue One replies specifically: Send Domain 51 cross-domain note citing FEC enforcement collapse + 42-point civic participation gap (D59) — template in DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md Section 4.1

**Trigger C — Domain 48 Batch Activation (composite-score-dependent)**
- Condition: Composite engagement score ≥ 8/10 (per DOMAIN_51_JUNE_16_DECISION_LOGIC.md Section 2)
- Activates: Domain 48 (Criminal Justice / Civic Exclusion) distribution — pre-staged contacts in DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md
- Timing: June 18–20 (2-day stagger after Domain 51 Tier 1 expansion)
- Rationale: Domain 48's dark-money-to-criminal-justice-funding-pipeline argument directly extends Domain 51's FEC collapse analysis

**Trigger D — Domain 57 Parallel Activation (composite-score-dependent)**
- Condition: Composite engagement score ≥ 8/10, AND Domain 48 activation confirmed above
- Activates: Domain 57 (Multilateral Withdrawal) distribution — Gist live at DOMAIN_57_GIST_URL.txt
- Timing: June 20–22 (4–6 day stagger after Domain 48 per DOMAIN_51_JUNE_16_DECISION_LOGIC.md Section 3.1)
- Contacts: Human Rights Watch, Amnesty International USA, Council on Foreign Relations, Senate Foreign Relations Committee staff, Freedom House

**Trigger E — Wave 1–2 Retry (weak-signal contingency)**
- Condition: 0 Score 3+ replies AND delivery rate ≥ 80% (confirmed delivery, no engagement)
- Activates: Retry protocol — contact substitution per PHASE_2_TIER_2_CONTACT_STRATEGY.md
- Timing: Day 14 (June 28–29), with modified subject lines and single-domain framing
- Does not delay Domain 59 express path (Trigger A always fires independent of this)

**Escalation threshold (Tier 2 vs. retry decision point):**
- Metrics above 20% composite → selective Tier 2 activation (Trigger B + Trigger A)
- Metrics above 50% composite → full acceleration (Triggers A + B + C + D)
- Metrics below 20% with confirmed delivery → retry Wave 1–2 framing (Trigger E)
- Metrics below 20% with delivery failure → diagnostic before any retry (Section 5 FAILURE contingency)

---

## Section 3: Decision Tree

*Input: Wave 1 + Wave 2 engagement metrics from the orchestration script log and email inbox audit. Output: specific Phase 2 routing. Pre-flight checks run first; branch determination follows.*

---

### Pre-Flight (5 minutes — complete before entering branches)

Pull these values from the orchestration script and email inbox before running the tree:

```
uv run python /home/awank/dev/SuperClaude_Framework/projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --t7-check
uv run python /home/awank/dev/SuperClaude_Framework/projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --t7-check
```

Record:

| Metric | Value | Source |
|---|---|---|
| D51 confirmed deliveries | ___ / 5 | Script --t7-check output |
| D51 hard bounces | ___ | Script --t7-check output |
| D59 confirmed deliveries | ___ / [n] | Script --t7-check output |
| Score 3+ replies (D51) | ___ | Email inbox audit |
| Score 3+ replies (D59) | ___ | Email inbox audit |
| Any Score 4–5 reply | YES / NO | Email inbox |
| Gist clicks — Domain 51 | ___ (total Day 1–7) | Bitly dashboard |
| Gist clicks — Domain 59 | ___ (total Day 1–7) | Bitly dashboard |
| Forward events confirmed | ___ | Email inbox / referral contact |
| Composite engagement % | ___% | ((Score 3+ + forwards×3) / delivered) × 100 |
| Senate Finance markup | ACTIVE / PASSED / STALLED | finance.senate.gov |
| California ballot status | ON BALLOT / REMOVED | ballotpedia.org |

Delivery check: if confirmed deliveries < 80% of sends (more than 1 bounce per 5 sends), run delivery diagnostic from POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md Section 7.1 before entering the branches below.

---

### Branch Determination

Apply the first test that matches:

```
IF composite engagement % >= 50% (3+ Score 3+ replies or equivalent with forwards)
    → STRONG branch (Section 3A)

ELSE IF composite engagement % is 20-49% (1-2 Score 3+ replies, OR any Score 4-5)
    → MODERATE branch (Section 3B)

ELSE IF composite engagement % < 20% AND delivery confirmed >= 80%
    → WEAK branch (Section 3C)

ELSE IF composite engagement % < 20% AND delivery < 80%
    → DIAGNOSTIC branch (Section 3D)
```

**Regardless of branch: check Senate Finance markup status. If ACTIVE, Domain 59 express path fires immediately (Trigger A) in every branch.**

---

### 3A: STRONG Branch (composite >= 50%)

*Precedent from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 5: Phase 1's strong Day 30 threshold was 50%+ for Tier 1 operational organizations. Achieving this at Day 3–7 of a Phase 2 send indicates messaging-to-audience alignment above projections and warrants immediate acceleration.*

**What this means operationally**: Three or more substantive replies from five contacts in seven days is a 60% substantive reply rate. This is above the upper bound of expected cold advocacy email performance in this sector (Phase 1 Tier 1 expected: 25–50% at Day 30; achieved here at Day 7). Activate everything.

**Routing: FULL ACCELERATION**

- [ ] Domain 59 express path TODAY (Trigger A): AFL-CIO, CBPP, NWLC — 45 minutes active. Templates in DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 1. Log to domain-59-send-log-june1.md.
- [ ] Domain 51 Tier 1 expansion within 24 hours (Trigger B): OpenSecrets, Democracy 21, Public Citizen — 30 minutes active. Templates in DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md Part 2.
- [ ] Domain 51 full research sprint authorized (Days 1–5): DOMAIN_51_RAPID_ACTIVATION_RUNBOOK.md Zones 1–5, 10–14 hours total.
- [ ] Domain 59 full research sprint authorized (Days 1–5, parallel with D51): DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Parts 3–6.
- [ ] Domain 48 activation June 18–20 (Trigger C): Contacts from DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md.
- [ ] Domain 57 activation June 20–22 (Trigger D): Gist at DOMAIN_57_GIST_URL.txt.
- [ ] Cross-domain synthesis note Day 2: Target CBPP or AFL-CIO after first D59 reply. Template DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md Section 4.1.
- [ ] Update CHECKIN.md: "Day 7 checkpoint STRONG (composite __%). Full acceleration authorized. D59 express June 17, D51 Tier 1 expansion June 18, D48 June 18–20, D57 June 20–22."

**Resource requirement**: 22–30 researcher-hours over 5 days per PHASE_2_RESOURCE_ALLOCATION_CONTINGENCY_MATRIX.md Row 1.

---

### 3B: MODERATE Branch (composite 20–49%)

*Precedent from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 5: Phase 1's moderate Day 30 threshold was 30–49% overall reply rate with at least 3 of 7 constituencies at strong threshold. The MODERATE branch provides selective activation: Domain 59's Senate Finance urgency overrides Domain 51 sequencing logic when capacity is constrained.*

**What this means operationally**: One or two substantive replies from five contacts confirms the research is finding receptive readers, the messaging is not generating active rejection, and at least one organizational context is aligned. This is the expected outcome for a cold Phase 2 send at Day 7.

**Routing: SELECTIVE ACTIVATION — Option A (default, capacity-conservative)**

- [ ] Domain 59 express path TODAY (Trigger A, non-negotiable): AFL-CIO, CBPP, NWLC — 45 minutes. Templates in DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 1.
- [ ] Domain 51 Tier 1 expansion within 48 hours (first 2 contacts only): OpenSecrets (highest reply probability), Democracy 21 (clean DISCLOSE Act argument). Defer Public Citizen and state sends to Day 14. 20 minutes active.
- [ ] No research sprints in Option A. Both domains distribute from existing research documents (D51: 65 citations, 6,800 words; D59: 44 citations, existing Gist).
- [ ] Hold Domain 48 pending Day 14 engagement reassessment.
- [ ] Hold Domain 57 pending Day 14 engagement reassessment.
- [ ] Update CHECKIN.md: "Day 7 checkpoint MODERATE (composite __%). D59 express firing today. D51 first 2 Tier 1 expansion contacts June 18. D48/D57 reassess June 28–29."

**Option B (use when capacity allows 10–12h over 4–5 days AND at least one domain received a reply):**

- [ ] Same as Option A PLUS authorize full D51 or D59 research sprint for the domain that received the reply.
- [ ] Second domain sprint holds pending Day 14 signal from the first sprint's expanded contacts.
- [ ] Total additional time: 10–14 hours over 4–5 days.

**If Issue One replied specifically (contact-specific trigger)**: Send cross-domain note — FEC enforcement collapse + 42-point civic participation gap synthesis. Template at DOMAINS_51_59_SEQUENTIAL_ACTIVATION_TIMING.md Section 4.1. This is a high-leverage follow-up; Issue One's reach (TIME100, Washingtonian 500 policy network) turns one reply into a potential multiplier event.

**Resource requirement**: 65 minutes (Option A) or 10–15 hours over 4–5 days (Option B).

---

### 3C: WEAK Branch (composite < 20%, delivery confirmed)

*Precedent from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 5 failure recovery: "an unchanged strategy will produce unchanged results." WEAK does not mean failure — it means the Day 7 window has not yet produced a signal, which is within normal variance for a 3-day-old send to high-inbox-volume program directors. The WEAK branch adjusts scope, not urgency.*

**What this means operationally**: Zero substantive replies from five confirmed-delivered contacts over three to seven days. This occurs when contacts are traveling, when inboxes are high-volume (pre-markup congressional schedule), or when subject line framing did not trigger a read. It is not a messaging failure signal until Day 14 with zero opens confirmed via Bitly.

**Routing: RETAIN CORE, DEFER EXPANSION**

- [ ] Domain 59 express path TODAY (Trigger A, non-negotiable): The Senate Finance markup deadline is an immovable external calendar event. Domain 59 sends regardless of Domain 51 engagement signal. AFL-CIO, CBPP, NWLC — templates in DOMAIN_59_RAPID_ACTIVATION_RUNBOOK.md Part 1.
- [ ] Domain 51 expansion to highest-priority contact only: Campaign Legal Center backup contact (info@campaignlegal.org) if no reply from Chlopak; OR OpenSecrets only (one email, highest reply probability, most domain-aligned). Do not expand to full Tier 1 list.
- [ ] Hold Domain 48, Domain 57, all research sprints.
- [ ] Day 14 reassessment scheduled (June 28–29): If no signals by Day 14, execute retry per Trigger E — contact substitution (next-tier-down contacts per PHASE_2_TIER_2_CONTACT_STRATEGY.md) and single-domain framing shift (lead with one domain specific to each recipient's current work rather than full framework overview).
- [ ] Check Bitly clicks: If zero Gist clicks AND zero replies, the issue may be delivery (spam filtering, wrong address) rather than engagement. Cross-reference against bounce logs before scheduling retry.
- [ ] Update CHECKIN.md: "Day 7 checkpoint WEAK (composite __%). D59 express firing today (Senate Finance immovable). D51 single-contact expansion. All other expansion held. Retry assessment June 28–29."

**What WEAK does not mean**: Weak Day 7 does not indicate a failed campaign. PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 5 established that Day 7 minimum viable engagement requires signals from at least 4 of 7 constituencies — the Phase 2 equivalent threshold (signals from at least 2 of 5 contacts) may arrive Day 8–14 as contacts process inbox backlog.

---

### 3D: DIAGNOSTIC Branch (delivery < 80%)

**What this means**: More than one bounce per five sends indicates a delivery integrity problem, not an engagement problem. Do not interpret zero replies as weak engagement until delivery is confirmed.

- [ ] Run POST_WAVE_2_ENGAGEMENT_ANALYSIS_TEMPLATE.md Section 7.1 delivery diagnostic.
- [ ] Identify bounce source: hard bounce (address invalid) vs. soft bounce (delivery delayed).
- [ ] For hard bounces: pull backup addresses from WAVE_1_EMAIL_EXECUTION_PACKAGE.md and WAVE_2_EMAIL_EXECUTION_PACKAGE.md contact tables.
- [ ] Resend to confirmed-valid addresses before entering any engagement branch.
- [ ] Domain 59 express path TODAY regardless (Trigger A): Senate Finance window does not wait for delivery diagnostics. Use confirmed-valid D59 contact addresses only.
- [ ] Reassess engagement branch after resend (48-hour window before re-entering tree).

---

## Section 4: Execution Checklist

*5-step process for June 17–18 checkpoint. Total active time: 35–40 minutes.*

**Step 1 — Pull engagement logs (10 minutes)**

Run both t7-check commands from Section 3 pre-flight. Open email inbox and pull Gmail label counts for phase2-outreach/replies/. Open Bitly dashboard and record 7-day click totals for Domain 51 and Domain 59 Gist short links. Open PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py state files (wave_orchestration_state_d51.json, equivalent for D59) to confirm confirmed-delivered count and log any bounce records.

**Step 2 — Extract and record metrics (5 minutes)**

Fill the pre-flight table in Section 3 with values from Step 1. Calculate composite engagement percentage. Note any Score 4–5 replies, forward events, or Bitly spikes (5+ clicks on a single day within 24–72 hours of send = confirmed delivery + engagement). Record email bounce log findings.

**Step 3 — Cross-reference triggers (5 minutes)**

Apply branch determination logic from Section 3. Identify which triggers fire (A through E). If Senate Finance markup is ACTIVE, Trigger A fires regardless of branch. If Issue One has replied, note the cross-domain note follow-up in the checklist. Record composite score against DOMAIN_51_JUNE_16_DECISION_LOGIC.md thresholds for the Domain 51 batch activation determination (score ≥ 8 unlocks D48 + D57).

**Step 4 — Execute routing (15–20 minutes)**

Follow the branch checklist for your determined branch. Begin with Trigger A (D59 express path) if Senate Finance is active — this is always the first action. Then execute domain-specific triggers in order (B, C, D as capacity allows). Log each send to the orchestration script:

```
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-send 1 --time "[UTC timestamp]"
uv run python PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --log-send 3 --time "[UTC timestamp]"
```

**Step 5 — Document checkpoint decision (5 minutes)**

Update CHECKIN.md with: checkpoint date, branch determined, composite score, specific actions executed, next checkpoint date. Record which triggers fired. If STRONG or MODERATE, note which contacts replied and what they said (this becomes social proof framing for Tier 2 sends). If WEAK or DIAGNOSTIC, note the reassessment window.

**Tools and log references:**
- Engagement logs: PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --t7-check output, wave_orchestration_state_d51.json
- Bounce logs: Gmail sent label / Campaign Monitor dashboard (if used) / orchestration script bounce records
- Reply logs: Gmail phase2-outreach/replies/ labels; DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md
- Bitly: bitly.com dashboard, Domain 51 and Domain 59 short link click reports
- Orchestration script log: WORKLOG.md (auto-appended by script on every --log-send and --log-reply call)

---

## Section 5: Contingency Scenarios

*Three scenarios with specific routing for each. Domain 59 Senate Finance path is non-negotiable in all three.*

---

### Scenario 1: Low Engagement — composite < 20% (Wave 1–2 both weak)

**What happened**: Five contacts received and confirmed-delivered emails. Fewer than one substantive reply was received by Day 7. Bitly shows 0–2 clicks on each Gist.

**Diagnosis before retry**: Distinguish messaging failure from timing failure. High-inbox-volume contacts (program directors, executive directors of national organizations) often process outreach in batch on specific days. Day 3–7 is within their normal processing lag. Check if any Bitly clicks occurred on Day 5–7 — late-breaking clicks indicate the email was read but a reply not yet composed.

**Routing: Retain D59 urgency, retry D51 at Day 14 with adjustments**

- Immediate: Domain 59 express path fires (Trigger A). Three new contacts, Senate Finance framing, no engagement dependency.
- Day 14 retry for Domain 51: Apply three modifications from PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 6.3 failure recovery protocol:
  - Modification 1 — Contact substitution: Replace 1–2 Wave 1–2 contacts with next-tier contacts. Substitute general inbox contacts with program-specific direct contacts (CLC's info@campaignlegal.org → Adav Noti at noti@campaignlegalcenter.org if Chlopak did not open; Issue One general inbox → direct to a named policy staff member if findable).
  - Modification 2 — Framing revision: Shift from full dark money architecture overview to single issue: lead with FEC enforcement collapse (200+ days without quorum, specific pending matters at statute-of-limitations risk) as a standalone, actionable research note. Attach full Gist URL but frame it as supplementary.
  - Modification 3 — Channel addition: Post a condensed Domain 51 summary to a relevant public channel (Just Security, Lawfare, or a Substack the contacts follow) so the next outreach email can reference a published piece rather than a cold Gist link.

**What to hold**: Domain 48, Domain 57, all research sprints. Domain 59 is the active track.

---

### Scenario 2: Moderate Engagement — composite 20–50% (selective response)

**What happened**: One or two of five contacts replied substantively. Bitly shows 3–6 total clicks across both Gists. At least one contact is engaged; others are processing or uninterested.

**Routing: Selective Tier 2 activation for highest-responding contacts**

- Immediate: Domain 59 express path (Trigger A). Domain 51 Tier 1 expansion to first two next-priority contacts (Trigger B, first two contacts only).
- Domain-specific routing for the replying contacts:
  - If CLC (Chlopak) replied: Activate Domain 51 Tier 1 expansion immediately, noting CLC engagement as social proof in OpenSecrets and Democracy 21 emails ("Campaign Legal Center has engaged with this analysis" — social proof framing per PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 6.1).
  - If Common Cause CA or LWV CA replied: Add Montana I-194 state-level follow-up (status of signature qualification), since these California contacts may have state coalition connections to the Montana campaign. Reference DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md for ballot status contingency framing.
  - If Issue One replied (any score): Send cross-domain synthesis note within 24 hours (FEC collapse + civic participation gap). High-multiplier event.
- Hold Domain 48 and Domain 57 activation pending Day 14 signal. Both domains have time: Domain 48 primary distribution window is August 1–15 (Virginia ballot measure), Domain 57 is August 10 UNGA prep. Day 14 reassessment does not threaten either deadline.
- Research sprints: Authorize Domain 59 research sprint only if D59 contacts reply at Step 1 Domain 59 check. Defer D51 full sprint pending second reply confirmation.

**Composite score application**: Apply DOMAIN_51_JUNE_16_DECISION_LOGIC.md composite score. A moderate engagement composite of 5–7/10 routes to MODERATE activation path (Domain 48 + Domain 57 on June 20–22 stagger, not immediate batch). Score below 5 holds both.

---

### Scenario 3: High Engagement — composite > 50% (full acceleration)

**What happened**: Three or more of five contacts replied substantively. Any forward events confirmed. Bitly shows 7+ total clicks. This exceeds Day 7 projections for a cold Phase 2 send in this sector.

**Routing: Immediate acceleration to Tier 2 plus Tier 2.5 prep for urgent domains**

- Immediate: Domain 59 express path (Trigger A). Domain 51 full Tier 1 expansion all three contacts (Trigger B). Both fire the same day as the checkpoint.
- Tier 2.5 prep (begin June 18–19): Domain 48 contact verification (DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md), Domain 57 Gist live-check (DOMAIN_57_GIST_URL.txt), and a cross-domain synthesis note to the strongest-engaging contact referencing the FEC-to-civic-participation causal chain.
- Research sprints: Authorize both D51 and D59 full sprints in parallel (10–14h each, Days 1–5 stagger). D59 sprint produces Senate staff briefing supplement (400-word OBBBA provision mapping). D51 sprint deepens Zone 1 (pending FEC enforcement matters at statute risk) and Zone 2 (crypto/AI PAC 2026 deployment data).
- Domain 48 activation June 18–20 (Trigger C). Domain 57 activation June 20–22 (Trigger D). Both fire without waiting for additional signals — the STRONG engagement signal authorizes the full batch per DOMAIN_51_JUNE_16_DECISION_LOGIC.md Section 3.1.
- Social proof capture: Record the exact reply content (contact name, date, what they said) for use in all subsequent Tier 2 and Tier 3 sends. A 50%+ Day 7 reply rate from national policy organizations is a lead reference for later outreach ("this research has been engaged by Erin Chlopak at Campaign Legal Center / [contact name] at [org]...").
- Update CHECKIN.md: Flag HIGH ENGAGEMENT signal. Note whether any reply included a forward event or adoption signal — these are the leading indicators of the network multiplier effect documented in PHASE_1_IMPACT_EVALUATION_FRAMEWORK.md Section 3.5.
