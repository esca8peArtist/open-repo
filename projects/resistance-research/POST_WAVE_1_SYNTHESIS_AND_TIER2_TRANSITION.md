---
title: "Post-Wave 1 Impact Synthesis & Tier 2 Transition Framework"
created: 2026-05-17
status: "production-ready for May 20-28 execution"
scope: "May 20–28 post-distribution analysis, Tier 2 readiness assessment, and transition planning"
audience: "thorn (executing Wave 1 distribution May 18–20)"
companion_files:
  - WAVE_1_MONITORING_DASHBOARD.md
  - WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv
  - execution/phase-1-adoption-tracking-automation.md
  - execution/tier-2-distribution-strategy.md
  - execution/tier-2-organizational-contact-list.md
  - PHASE_1_WAVE_1_EXECUTION_DASHBOARD.md
total_time_estimate: "4–6 hours across May 20–28"
---

# Post-Wave 1 Synthesis & Tier 2 Transition Framework

## Overview

After Wave 1 distribution closes (May 20 20:00 UTC), this framework guides the analysis phase (May 20–28). Output: actionable intelligence for Tier 2 launch decision and contact list prioritization.

**Key deliverables**:
1. **Wave 1 Impact Report** — sector-by-sector engagement summary, adoption metrics, unexpected patterns
2. **Tier 2 Candidate Identification** — automated scoring to identify which Batch 1 contacts should escalate to Tier 2
3. **Go/No-Go Decision Framework** — objective criteria for proceeding with Batch 2 vs. pivoting strategy
4. **Tier 2 Wave Planning** — refined contact sequencing, customized messaging, confidence levels

---

## Phase 1: Data Aggregation (May 20–21, ~90 minutes)

### 1.1 Collect Raw Signals (15 minutes)

**Source**: WAVE_1_MONITORING_DASHBOARD.md + email client + Bitly analytics

Pull three data sources:
1. **Daily monitoring dashboard** — copy final state from WAVE_1_MONITORING_DASHBOARD.md SECTION 1 (Daily Tracking Table)
2. **Email reply log** — export all received emails from May 18-20 into a dated folder or spreadsheet
3. **Bitly click analytics** — check https://bitly.com/dashboard for all Gist URLs in Wave 1 emails (baseline view counts from pre-flight + final counts at end of May 20)

**Store in**: `wave-1-raw-signals-[DATE].csv` (date = your analysis date, not send date)

Format:
```
contact_name,org,sector,send_date,status,reply_type,reply_content_summary,reply_date,gist_clicked,gist_clicks,opened_24h,score_assigned
```

### 1.2 Normalize Engagement Scoring (30 minutes)

Use the **Reply Type Classification** from WAVE_1_MONITORING_DASHBOARD.md to assign scores:
- **Integration signal** (5 points) — explicitly mentions using the research in their work
- **Implementation question** (4 points) — asks how to use the framework operationally
- **Referral** (4 points) — connects you to colleagues or new contacts
- **Clarification question** (3 points) — asks for detail on a domain or framing
- **Critique** (3 points) — substantive methodological or factual challenge
- **Acknowledgment only** (1 point) — "thanks, I'll read it" with no follow-up
- **Decline** (0 points) — opted out or said not relevant
- **No reply** (0 points) — silent by end of May 20

**Calculate**:
- `engagement_score = (reply_score × 0.6) + (gist_clicks × 0.2) + (opened_24h × 0.2)`
  - This weights substantive reply quality highest (60%), click behavior second (20%), opens third (20%)
  - Example: Integration signal (5 pts) + 3 Gist clicks + opened = (5×0.6) + (3×0.2) + (1×0.2) = 3.0 + 0.6 + 0.2 = 3.8

Store normalized scores in: `engagement-scores-wave-1.csv`

### 1.3 Validate Completeness (15 minutes)

Checklist:
- [ ] All 5 Batch 1 contacts have rows in engagement-scores-wave-1.csv
- [ ] All email replies are accounted for (count in raw signals = count in emails received)
- [ ] No duplicate rows (sort by contact_name, scan for repeats)
- [ ] Gist click counts match Bitly dashboard (spot-check 3 URLs)
- [ ] All scores fall in range [0.0–5.0]

**If incomplete**: Flag specific missing data. Do not proceed to Phase 2 until complete.

---

## Phase 2: Sector & Engagement Trend Analysis (May 21–22, ~120 minutes)

### 2.1 Sector-Level Aggregation (30 minutes)

Create a summary table from normalized engagement scores:

```
sector | num_contacted | num_replied | reply_rate | avg_engagement_score | max_score | integration_signals | implementation_questions
Law School | 2 | 1 | 50% | 2.4 | 3.8 | 0 | 1
Policy Org | 2 | 2 | 100% | 3.1 | 4.2 | 1 | 1
Immigration Legal | 1 | 1 | 100% | 4.8 | 4.8 | 1 | 0
```

**Metrics calculated**:
- **Reply rate** = (contacts_with_replies / total_contacts) × 100
- **Avg engagement score** = mean of all engagement scores in sector
- **Max score** = highest individual engagement score in sector
- **Integration signals** = count of contacts with score ≥5
- **Implementation questions** = count of response type "Implementation"

### 2.2 Expected Baselines (reference only, no action)

From prior research (policy brief RCTs, policymaker outreach):
- **Policy-to-policymaker outreach**: 30–40% reply rate typical, 2.1 avg engagement score
- **Academic-to-academic**: 25–35% reply rate, 2.3 avg engagement score
- **Legal-to-legal**: 40–50% reply rate, 2.8 avg engagement score
- **High engagement threshold** (Tier 2 candidate): score ≥3.5

*Note: Wave 1 is intentionally small (5 contacts) for qualitative feedback on framing. Statistical significance requires 20+ contacts per sector. Sector trends from May 20–21 are directional, not predictive.*

### 2.3 Pattern Recognition (30 minutes)

Manually scan replies for recurring themes:

| Theme | Count | Example | Implication |
|-------|-------|---------|------------|
| Asks about implementation in [domain] | ? | "How do I use this in immigration law?" | Sector-specific framing works — prioritize in Tier 2 |
| Requests more detail on [domain] | ? | "Can you expand on the voting systems section?" | Gaps in existing documentation — add to Phase 2 research or provide citations |
| Objects to framing of [domain] | ? | "This oversimplifies the trade-offs in X" | Either update framing or note as ideological divergence for Tier 2 candidate assessment |
| Mentions forwarding to colleagues | ? | "Sending this to our legal team" | High-value signal for organizational multiplier — track for Tier 2 escalation |
| References use in upcoming project | ? | "We're doing this analysis for [X] project" | Direct adoption signal — highest priority for Tier 2 |

**Output**: `wave-1-theme-log.md` (informal notes, 200–300 words) summarizing what you learned about messaging effectiveness.

### 2.4 Unexpected Patterns (30 minutes)

Flag anything that surprises:
- Contact did NOT reply despite prior relationship → check email address validity, institutional role change
- Contact replied negatively to a domain you expected to resonate → note for Tier 2 customization
- Multiple contacts asked same question → indicates messaging gap, update email template for Batch 2
- No Gist clicks but email opened → content preview in email reader worked; actual reading may not have happened

Document in `wave-1-anomalies.md` (short form, one anomaly per section).

---

## Phase 3: Tier 2 Candidate Identification (May 22–23, ~90 minutes)

### 3.1 Automated Scoring (30 minutes)

For each Batch 1 contact, calculate **Tier 2 readiness score**:

```
tier_2_score = 
  (engagement_score × 0.5) +           # primary: substantive engagement quality
  (integration_signal × 2.0) +         # bonus: they're already using the material
  (implementation_question × 1.5) +    # bonus: they want to operationalize
  (referral × 1.5) +                   # bonus: they connected you to others
  (sector_alignment × 0.5)             # bonus: sector matches Tier 2 strategy
```

Where:
- `engagement_score` = from Phase 1 (0–5)
- `integration_signal` = 1 if reply type includes "Integration signal", else 0
- `implementation_question` = 1 if reply type includes "Implementation", else 0
- `referral` = 1 if reply mentions forwarding or connecting to colleague, else 0
- `sector_alignment` = 0.5 if contact's sector (law, policy, immigration legal) matches Tier 2 strategy, else 0

**Example**:
- Contact: Ryan Goodman (Just Security, law school)
- engagement_score = 3.8
- integration_signal = 1 (mentioned using in an upcoming brief)
- implementation_question = 1 (asked about implementation in his domain)
- referral = 0
- sector_alignment = 0.5
- **tier_2_score = (3.8 × 0.5) + (1 × 2.0) + (1 × 1.5) + 0 + (0.5) = 1.9 + 2.0 + 1.5 + 0.5 = 5.9**

**Tier 2 Candidate Thresholds**:
- **Definite candidate** (score ≥5.0) — escalate immediately to Tier 2 Wave 1
- **Probable candidate** (score 3.5–4.9) — escalate to Tier 2 Wave 1 with customized outreach
- **Possible candidate** (score 2.0–3.4) — monitor for follow-up engagement; escalate to Tier 2 Wave 2
- **Not yet** (score <2.0) — return to Batch 2 or broader Tier 1 distribution; reassess in 2 weeks

### 3.2 Tier 2 Candidate List (30 minutes)

Create preliminary Tier 2 candidate list:

```
contact_name | org | sector | engagement_score | tier_2_score | candidate_threshold | tier_2_wave | custom_messaging_angle
Ryan Goodman | Just Security | Law | 3.8 | 5.9 | Definite | Wave 1 | Brief collaboration in elections domain
[...]
```

**Next step**: Merge with execution/tier-2-organizational-contact-list.md (47 organizations, 5 sectors) to identify gaps:
- Which Tier 2 organizations did NOT get Wave 1 contact? (They'll receive Tier 2 outreach directly)
- Which Batch 1 contacts are ready to "bring along" into Tier 2 Wave 1?
- Are there organizational champions who can facilitate Tier 2 introductions?

### 3.3 Decision: Escalate or Defer (30 minutes)

For each Tier 2 candidate, decide:

| Candidate | Decision | Reason | Timeline |
|-----------|----------|--------|----------|
| Definite (score ≥5.0) | Escalate immediately | High engagement + integration signal | Tier 2 Wave 1 (May 25–31) |
| Probable (3.5–4.9) | Escalate with customization | Strong engagement + specific interest area | Tier 2 Wave 1 with custom brief |
| Possible (2.0–3.4) | Monitor + Batch 2 | Medium engagement; wait for follow-up | Re-engage in Batch 2 (May 25) |
| Not yet (<2.0) | Broader Tier 1 expansion | Low engagement; may need different angle | Batch 2 outreach (May 25) or defer |

**Default strategy**: Escalate all Definite + Probable candidates to Tier 2 Wave 1 immediately (exploit momentum). Monitor Possible candidates for 2 weeks before deciding.

---

## Phase 4: Go/No-Go Decision Framework (May 23–24, ~60 minutes)

### 4.1 Objective Criteria (30 minutes)

Proceed to Batch 2 + Tier 2 launch if **ALL** of the following are true:

**Minimum engagement threshold** (MUST PASS):
- [ ] Reply rate ≥25% (at least 2 of 5 Batch 1 contacts replied substantively)
- [ ] Average engagement score ≥2.0 (basic receptiveness across replies)
- [ ] At least one integration signal or implementation question (evidence of practical interest)

**No critical technical failures** (MUST PASS):
- [ ] No Gist URLs returned 404 during Wave 1
- [ ] No email deliverability issues (bounces <5%)
- [ ] No spam complaints received

**Messaging quality** (SHOULD PASS):
- [ ] No sector-wide objections to core framing (isolated critique is OK; systemic rejection is not)
- [ ] Contacts understood the scope of the research (few clarification questions about "what is this?")
- [ ] No major email formatting issues reported

### 4.2 Decision Matrix (15 minutes)

```
Scenario | Engagement | Tech Issues | Messaging | Decision | Next Action
Wave 1 Success | ✓ ✓ | ✓ ✓ | ✓ ✓ | PROCEED | Batch 2 + Tier 2 launch May 25
Moderate Engagement | ✓ | ✓ ✓ | ✓ ✓ | PROCEED WITH CAUTION | Batch 2 only; defer Tier 2 1 week
Low Engagement | ✗ | ✓ ✓ | ✓ ✓ | PIVOT | Extended Batch 2 (double contacts); investigate messaging gaps
Tech Failure | ? | ✗ | ? | HALT | Debug before proceeding
Messaging Failure | ? | ✓ | ✗ | PAUSE & REVISE | Update email templates; retest with small batch
```

### 4.3 Document Decision (15 minutes)

Write a one-page summary in `wave-1-go-no-go-decision.md`:

```markdown
# Wave 1 Go/No-Go Decision — May 24, 2026

## Threshold Assessment

[Check off which criteria were met]

## Recommendation

[PROCEED / PROCEED WITH CAUTION / PIVOT / HALT]

## Rationale

[2–3 sentences explaining the recommendation based on data]

## Next Steps

[Specific actions for May 25+: Batch 2 launch, Tier 2 timeline, messaging updates, etc.]

## Timeline

[Updated schedule for Batch 2 and Tier 2 execution based on decision]
```

---

## Phase 5: Tier 2 Wave Planning & Contact Prioritization (May 25–28, ~60 minutes)

### 5.1 Tier 2 Wave 1 Contact Prioritization (30 minutes)

Once you've identified Tier 2 candidates from Phase 3, prioritize Tier 2 organizations using this scoring matrix:

```
organization | sector | contact_quality | sector_alignment | movement_multiplier | custom_angle | priority_rank
[Org Name] | Labor Union | 2 (verified contact) | 1.0 (full match) | 2.0 (100K members) | Occupational security + union organizing | High
[Org Name] | Immigration Legal | 2 | 1.0 | 1.5 (regional network) | Sanctuary cities + legal access | High
[Org Name] | Civil Rights | 1 (primary role only) | 0.8 (related) | 1.0 (member org) | Digital rights + voting access | Medium
```

**Scoring**:
- `contact_quality` = 2 (verified contact + direct relationship from Wave 1), 1 (primary contact only), 0 (no prior contact)
- `sector_alignment` = 1.0 (core Tier 2 sector), 0.8 (adjacent), 0.5 (broader alignment)
- `movement_multiplier` = organizational reach (member count / network size)
- `custom_angle` = sector-specific messaging hook (from Phase 1 theme analysis)

**Priority assignment**:
1. All Wave 1 Definite candidates (score ≥5.0) — send Tier 2 outreach May 25–26
2. High-priority organizations (score ≥6.0) — send May 26–27
3. Medium-priority organizations (score 4.0–5.9) — send May 27–28
4. Lower-priority organizations — hold for Tier 2 Wave 2 (June 1–14)

### 5.2 Customized Messaging Angles (20 minutes)

Using themes from Phase 2.3, create sector-specific message customizations for Tier 2:

**Template** (copy to `tier-2-wave-1-custom-angles.md`):

```markdown
## Labor Unions — Custom Angle

**Theme from Wave 1**: Contacts asked about occupational security and union organizing implications

**Tier 2 customization**:
- Lead with: "How democratic governance failures compound labor exploitation"
- Emphasize: Domains 51 (campaign finance preventing pro-labor ballot measures), 29 (prosecutorial weaponization of labor organizing), 54 (criminal justice exclusion removing workers from civic participation)
- Offer: Briefing on how to use this framework in union educational materials + legislative advocacy

---

## Immigration Legal Aid — Custom Angle

**Theme from Wave 1**: Contacts asked how to implement in immigration law and policy

**Tier 2 customization**:
- Lead with: "Democratic design failures that fuel immigration restriction"
- Emphasize: Domains 25 (surveillance architecture), 28 (war powers enabling border militarization), 37 (executive interference in judicial/administrative processes), 50 (voter registration access)
- Offer: Dedicated briefing on NVRA implications + VAWA integration opportunities
```

### 5.3 Tier 2 Launch Readiness Checklist (10 minutes)

Before sending first Tier 2 email (May 25):

- [ ] `tier-2-wave-1-custom-angles.md` complete (sector-specific messaging ready)
- [ ] Email templates populated with Tier 2 contact names and organizations
- [ ] Tier 2 contact email addresses verified (spot-check: open org page, confirm current email format)
- [ ] Gists still live and accessible (spot-check: load each URL one more time)
- [ ] Discord or Slack channel set up for Tier 2 response monitoring (separate from Wave 1)
- [ ] `tier-2-wave-1-engagement-scoring-calculator.csv` created (copy Wave 1 template, rename for Tier 2)

---

## Success Metrics & Thresholds (Reference)

Use these to evaluate Wave 1 outcome and adjust Tier 2 strategy:

| Metric | Minimum | Target | Excellent |
|--------|---------|--------|-----------|
| Reply rate | 25% | 40% | 60%+ |
| Avg engagement score | 2.0 | 2.5 | 3.5+ |
| Integration signals | 1 | 2–3 | 4+ |
| Implementation questions | 1 | 2–3 | 4+ |
| Tier 2 candidates identified | 2 | 3–4 | 5 |
| Go/No-Go decision confidence | 70% | 85% | 95%+ |

---

## Timeline

- **May 20–21**: Phase 1 (Data Aggregation) — 90 min
- **May 21–22**: Phase 2 (Sector & Trend Analysis) — 120 min
- **May 22–23**: Phase 3 (Tier 2 Candidate ID) — 90 min
- **May 23–24**: Phase 4 (Go/No-Go Decision) — 60 min
- **May 25–28**: Phase 5 (Tier 2 Wave Planning) — 60 min

**Total**: ~6 hours across May 20–28 (can compress to 4 hours if working daily)

---

## Outputs Produced

By May 28, you will have:

1. ✅ **wave-1-raw-signals-[DATE].csv** — all engagement data normalized
2. ✅ **engagement-scores-wave-1.csv** — normalized engagement scores
3. ✅ **Wave 1 Sector Summary Table** — reply rates and engagement trends by sector
4. ✅ **wave-1-theme-log.md** — pattern analysis and messaging effectiveness assessment
5. ✅ **wave-1-anomalies.md** — unexpected patterns and outliers
6. ✅ **Tier 2 Candidate List** — scored candidates with escalation decision
7. ✅ **wave-1-go-no-go-decision.md** — formal decision document
8. ✅ **tier-2-wave-1-custom-angles.md** — sector-specific messaging for Tier 2
9. ✅ **tier-2-wave-1-engagement-scoring-calculator.csv** — ready for Tier 2 monitoring

---

## Notes

- **Wave 1 is qualitative validation**, not statistical proof. 5 contacts provides signal on messaging framing, not population-level engagement patterns. Tier 2 (20+ organizations per sector) is where you get statistical confidence.

- **Tier 2 decision should not wait for perfect data**. If you hit the "Proceed" threshold by May 24, launch Tier 2 Wave 1 May 25 while still collecting Wave 1 follow-up replies through May 28. Momentum matters.

- **Keep this framework available for post-Tier-1 execution** (weeks 3–4 if using 4-week Tier 1 window). You'll repeat Phase 1–5 for Tier 2, and again for Tier 3.

---

**Last updated**: 2026-05-17  
**Created for**: resistance-research Wave 1 distribution cycle (May 18–June 15)
