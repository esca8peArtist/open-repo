---
title: "Phase 2 Monitoring Checkpoints — Domains 37, 42, 51, 54"
created: "2026-05-27"
version: "1.0"
status: "PRODUCTION-READY"
scope: "Day 2, Day 7, Day 14 checkpoints per domain; Tier 2 promotion criteria; feedback integration windows; success signals; failure escalation"
audience: "Orchestrator — execute checkpoints autonomously; flag user-decision items in CHECKIN.md"
---

# Phase 2 Monitoring Checkpoints
## Domains 37, 42, 51, 54 — Engagement Tracking and Escalation

**Checkpoints are the operational mechanism.** Distribution sends open the window. Checkpoints tell you whether the window is producing signal. Escalation decisions at each checkpoint are pre-determined — no user decision is needed at Day 2 or Day 7 unless a contact produces a Score 5 signal. Day 14 requires user review for Tier 2 expansion.

---

## How to Run a Checkpoint

1. Open the tracking spreadsheet (per PHASE_2_CONTACT_LIST_MANAGEMENT.md Part 2 template specification)
2. Count: total Tier 1 contacts sent vs. total replies received as of checkpoint date
3. Calculate: response rate = replies / delivered contacts
4. Score each reply using the 5-point scale (PHASE_2_CONTACT_LIST_MANAGEMENT.md Part 3)
5. Compare against the thresholds in this document
6. Execute the prescribed action
7. If action requires user input: write to CHECKIN.md under "Needs Your Input"

Checkpoint cadence: Day 2, Day 7, Day 14 from the domain's distribution send date. Days are calendar days (weekends count).

---

## Domain 51 — Campaign Finance / Dark Money

**Distribution send date (STRONG)**: May 31
**Distribution send date (MODERATE)**: May 31

### Day 2 Checkpoint: June 2

**What to check**:
- Total replies received (including auto-replies / OOO — note separately, do not count toward engagement rate)
- Gist URL view count: compare to Gist view count at time of send (delta = new views)
- Any bounce notifications from the sending account

**Thresholds**:

| Signal | Threshold | Interpretation |
|--------|-----------|---------------|
| 2+ substantive replies | Score 2+ from 2 of 5 contacts | Strong early signal — send Domain 37 on June 2 as scheduled |
| 1 substantive reply | Score 2+ from 1 of 5 contacts | Normal early signal — proceed to Domain 37 on schedule |
| 0 replies + Gist delta 5+ | No direct replies but Gist active | Passive engagement — send Domain 37 on schedule; note for Day 7 |
| 0 replies + Gist delta 0–1 | No signal of any kind | Normal (academic/advocacy response cycle is 5–7 days) — proceed on schedule, do not intervene |
| 1+ bounce notification | Delivery problem | Re-verify bounced contact email immediately; resend to corrected address within 24 hours |

**Day 2 actions**: Record in tracking spreadsheet. No escalation triggered at Day 2 unless there is a bounce or a Score 5 signal (Score 5 = flag immediately in CHECKIN.md).

---

### Day 7 Checkpoint: June 7

**What to check**: Full engagement count; categorize replies by type (PHASE_2_CONTACT_LIST_MANAGEMENT.md Part 4 — implementation, critique, request, adoption, question).

**Thresholds**:

| Response Rate | Action |
|--------------|--------|
| 60%+ (3+ of 5 replied, at least 2 at Score 3+) | Excellent — use engagement as social proof for Domains 37, 42, 54 templates. No Tier 2 activation needed. Proceed to Day 14. |
| 40–59% (2 of 5 replied, at least 1 at Score 3+) | On target — proceed on schedule. Note which specific finding resonated for personalization in subsequent domains. |
| 20–39% (1 of 5 replied at Score 3+) | Below target — activate Domain 51 Tier 2 contacts (Karen Hobert Flynn, Fred Wertheimer) on June 8. Do not revise templates. |
| <20% (0 Score 3+ replies from all 5 contacts) | Below floor — confirm delivery (self-test), review subject lines for spam triggers, activate Tier 2 on June 8. If Gist delta is 10+, treat as Score 2 passive engagement and note. |

**If <20% at Day 7**: Before activating Tier 2, run a 5-minute delivery audit:
1. Send a test email from the same account to your own inbox
2. Check spam folder — if test lands in spam, halt Domain 51 Tier 2 send until delivery is fixed
3. If delivery confirmed, check whether any contacts are on vacation / OOO (OOO auto-reply counts as delivered but not as engaged)

---

### Day 14 Checkpoint: June 14

**What to check**: Final Tier 1 engagement tally; Gist cumulative views; any Tier 2 activation results (if Tier 2 was activated on Day 7–8).

**Thresholds and decisions**:

| Situation | Decision | Action |
|-----------|----------|--------|
| 2+ Score 3+ replies total (any Tier) | PROCEED to Tier 2 full expansion | In Phase 2b Tier 2 expansion week, include Domain 51 in the social proof narrative for all outreach |
| 1 Score 3+ reply (any Tier) | PARTIAL — use for Domain 37 and 54 social proof; no additional Domain 51 outreach | Note the specific organization and finding for use in Domain 54 opening paragraph |
| 0 Score 3+ replies, Gist delta 20+ | PASSIVE SIGNAL — delay Domain 51 Tier 2; investigate whether Gist views are from legitimate organizational sources | If Gist traffic is from targeted organizations: treat as Score 2 aggregate signal and hold for June 15 assessment |
| 0 Score 3+ replies, Gist delta 0–5 | NON-SIGNAL — Domain 51 outreach has not engaged this audience | Flag in CHECKIN.md: "Domain 51 produced no substantive engagement at Day 14. User review recommended before Phase 2b Tier 2 expansion." |

**User decision required at Day 14**: If 0 Score 3+ replies from Domain 51, user needs to decide whether to proceed with Domain 51 Tier 2 or hold and focus resources on the more engaged domains (37 or 54, which will have sent by then and may have better signal).

---

## Domain 37 — Federal Executive Interference in 2026 Midterms

**Distribution send date (STRONG)**: June 2
**Distribution send date (MODERATE)**: June 5

### Day 2 Checkpoint: June 4 (STRONG) / June 7 (MODERATE)

**What to check**: Delivery confirmation, initial replies, Gist delta.

**Thresholds**:

| Signal | Threshold | Action |
|--------|-----------|--------|
| Any Score 3+ reply | 1+ of 5 contacts at Score 3+ | Flag immediately: which organization, which finding resonated? Use in Domain 42 template subject line. |
| 1–2 replies at Score 1–2 | Acknowledgment only | Normal — proceed to Day 7 |
| 0 replies | No signal yet | Normal for election law orgs (7-day cycle common) — proceed to Day 7 |
| Bounce from Marc Elias / Democracy Docket | Contact form used, may not have routing | Re-verify contact — use Democracy Docket staff directory rather than general form |

**Note on re-contact logic**: Wendy Weiser and Marc Elias are Phase 1 Batch 1 contacts. Domain 37 is a targeted follow-up using domain-specific framing, not a cold send. If either of them replies to Domain 37 with a Score 3+ response that specifically mentions Phase 1 engagement, this is a STRONG upgrade signal — flag immediately in CHECKIN.md.

---

### Day 7 Checkpoint: June 9 (STRONG) / June 12 (MODERATE)

**Thresholds**:

| Response Rate | Action |
|--------------|--------|
| 40%+ (2+ of 5 at Score 2+) | On target — note which findings engaged; use in Domain 54 framing (domain shares the civic exclusion architecture argument) |
| 20–39% (1 of 5 at Score 3+) | Acceptable — activate Justin Levitt (Loyola) and Rick Hasen (UCLA) as Tier 2 on Day 8. Election law academic contacts have 10-day response cycles. |
| <20% AND Gist delta 10+ | Passive engagement detected — wait until Day 14 before Tier 2 activation |
| <20% AND Gist delta 0–3 | Below floor — Tier 2 activation on Day 8. Also: do any of the 5 Tier 1 contacts have 2026 midterm election coverage underway? If yes, re-verify email is reaching the right person within the org. |

**Failure escalation**: If Domain 37 gets <20% engagement rate at Day 7, the following changes apply for Domain 42 and Domain 54:

- Domain 42 (Phase 2b) proceeds unchanged — different audience, different signals
- Domain 54: add one additional Tier 1 contact (NAACP Legal Defense Fund escalation) to compensate for any Domain 37 audience crossover gap
- Domain 37 Tier 2 activation (Levitt, Hasen, Lakin) sends on Day 8 with adjusted subject line: move from "2026 midterm interference analysis" framing to "election protection coalition infrastructure" framing — less presidential-campaign focused, more coalition building focused

---

### Day 14 Checkpoint: June 16 (STRONG) / June 19 (MODERATE)

**Success signal at Day 14**: At least 1 organization (any Tier) has cited Domain 37 findings in a public document or has confirmed distribution to their internal networks. This is a Score 4 adoption signal and constitutes the "network multiplier" success signal for Domain 37.

**Failure signal at Day 14**: Zero replies from any of the 5 Tier 1 + 5 Tier 2 contacts after 14 days. This is atypical for the election protection community, which is highly activated on 2026 electoral issues.

**If failure at Day 14**:
1. Check: did the NVRA 90-day quiet period concern shift organizational priorities? If election orgs are in quiet period preparation mode, their external communications have contracted.
2. Check: is there a major development in the 23-state mail ballot EO case (scheduled for June 2 hearing at Massachusetts U.S. District Court)? If the hearing produced a ruling that changed the landscape, organizations may be in reactive mode rather than reading incoming research.
3. If neither factor applies: Domain 37 has not engaged this audience through email/Gist. Pivot to Substack/Reddit distribution of Domain 37 content as earned-media channel (no further cold institutional outreach).

---

## Domain 42 Phase 2b — DEA Regulatory Capture (Academic/Legislative Wave)

**Distribution send date (STRONG)**: June 4
**Distribution send date (MODERATE)**: June 6

### Day 2 Checkpoint: June 6 (STRONG) / June 8 (MODERATE)

**Note**: Academic response cycle is 7–14 days, not 3–5 days. Day 2 checkpoint for Domain 42 is informational only — no action triggered unless bounce.

**What to check**:
- Confirm all 5 academic contacts delivered (no bounces)
- Note any immediate replies (unusual for academics but possible for administrative law faculty during active regulatory proceedings)
- Verify Domain 42 Gist URL is still live and accessible: https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab

**Day 2 action**: Record delivery status only. No engagement actions.

---

### Day 7 Checkpoint: June 11 (STRONG) / June 13 (MODERATE)

**Academic engagement norms**: Response rates for academic faculty in 7 days are typically 15–25% even for highly relevant materials during an active regulatory proceeding. Calibrate thresholds accordingly.

**Thresholds**:

| Response Rate | Action |
|--------------|--------|
| 25%+ (1–2 of 5 replied at any score) | On track — academic cycle is slow. Wait for Day 14. |
| 1 reply from Mason Marks specifically | Flag immediately — he is the primary academic source for Domain 42's regulatory capture argument. Any reply from him constitutes a Score 3+ minimum. |
| 0 replies | Normal at Day 7 — extend window to Day 14 without escalation |
| Bounce from any law school contact | Re-verify via law school faculty directory — professor emails frequently change with sabbaticals |

**No Tier 2 activation at Day 7** for Domain 42 academic wave unless there are multiple bounces (indicating the contact list is outdated).

---

### Day 14 Checkpoint: June 18 (STRONG) / June 20 (MODERATE)

**This is the primary Domain 42 checkpoint.** Academic response windows of 14 days are standard.

**Thresholds**:

| Response Rate | Action |
|--------------|--------|
| 20%+ (1+ of 5 replied at Score 2+) | On target — academic engagement at expected rate. Note whether Mason Marks or Zettler replied; these are the highest-value for hearing record amplification. |
| 1 reply requesting the full framework or offering to cite in testimony | Score 4 adoption signal — flag in CHECKIN.md. This contact should receive all related domains. |
| 0 replies from all 5 academic contacts | Activate tax law community contacts (280E specialists) as Tier 2 on Day 15. Different framing — move from "democratic legitimacy" to "regulatory uncertainty for state-legal businesses" |
| 0 replies AND DEA hearing running June 29–July 15 | Time-sensitive — activate SAFER Banking AG contacts (if not already sent) as Tier 2 on Day 14 with explicit DEA hearing-record framing |

**DEA hearing integration**: The June 29 hearing opens during Domain 42's active engagement window. If any Tier 1 contact has not replied by June 25, send a single follow-up with the subject line: "DEA hearing opens June 29 — Domain 42 hearing-record context." This is the last Domain 42 follow-up action.

**Success signal at Day 14**: Any academic contact submitting written comments to the DEA hearing (June 29–July 15) that reference the regulatory capture argument or cite the Yale Law Journal / Regulatory Review framing documented in Domain 42. This would constitute a Score 5 signal — the document influenced a formal federal regulatory proceeding record.

---

## Domain 54 — Criminal Justice / Civic Exclusion

**Distribution send date (STRONG)**: June 6
**Distribution send date (MODERATE)**: June 10–12

### Day 2 Checkpoint: June 8 (STRONG) / June 12–14 (MODERATE)

**What to check**:
- Delivery confirmation (no bounces from Sentencing Project, PPI, M4BL, Worth Rises)
- Any immediate replies from Virginia-specific contacts (Virginia compliance status for King v. O'Bannon due June 1 — organizations monitoring this may reply quickly)
- Gist delta from baseline

**Virginia compliance urgency signal**: If Virginia state compliance with the King v. O'Bannon ruling is disputed or delayed after June 1, Virginia civic organizations will be in active advocacy mode. A Domain 54 distribution arriving during that dispute is highly timely — expect faster-than-average reply rates from Virginia contacts specifically.

**Day 2 action**: Record delivery status; note any Virginia-specific replies for immediate follow-up with Virginia constitutional amendment campaign framing.

---

### Day 7 Checkpoint: June 13 (STRONG) / June 17–19 (MODERATE)

**Thresholds**:

| Response Rate | Action |
|--------------|--------|
| 50%+ (3+ of 6 replied at Score 2+) | Exceptional — Domain 54 is resonating. Note which findings: felony disenfranchisement scale (4 million), jury exclusion (20 million), or the 27% unemployment rate for formerly incarcerated people. Prepare social proof summary for Tier 2 expansion. |
| 35–49% (2 of 6 at Score 2+) | Strong — proceed to Day 14 without Tier 2 activation. Flag strongest reply for social proof. |
| 20–34% (1 of 6 at Score 3+) | Acceptable — Sentencing Project or Prison Policy Institute specifically? These are the primary data-source contacts; even one engagement validates the framework connection. Activate Desmond Meade (Florida Rights Restoration) as Tier 2 on Day 8. |
| <20% AND Virginia contacts silent | Below floor — M4BL and Worth Rises contacts need verification. Grassroots organizations have variable email reliability; contact via secondary channel (contact form, Twitter/X DM) if primary email produced no signal. |

**If Domain 37 produced <20% engagement at Day 7, apply these changes to Domain 54**:
- Add one additional contact to Domain 54 Tier 1: NAACP Legal Defense Fund Democracy program (escalation from Phase 1 contact, different program)
- Add Virginia-specific urgency framing to any follow-up messages (Virginia constitutional amendment November 2026)
- Domain 54 subject line adjustment: if Domain 37 missed on "federal executive interference" framing, test "civic exclusion architecture and the 4 million Americans who cannot vote" — more data-driven, less framing-dependent

---

### Day 14 Checkpoint: June 20 (STRONG) / June 24–26 (MODERATE)

**Success signals at Day 14**:

| Signal | Category | Significance |
|--------|----------|-------------|
| Sentencing Project or Prison Policy Initiative cites Domain 54 findings in a report or publication | Score 4–5 adoption | Highest-value: these organizations set the data standard for criminal justice reform discourse |
| M4BL People's Assembly Project shares Domain 54 with its 100+ member organizations | Score 5 (network multiplier) | Multiplies reach by the 100+ M4BL member network — the largest criminal justice reform organizational infrastructure |
| Virginia organization references Domain 54 in King v. O'Bannon compliance monitoring | Score 4 | Time-sensitive institutional adoption during active enforcement proceeding |
| Worth Rises or National Re-Entry Coalition uses Domain 54 in member materials | Score 3–4 | Community adoption signal; most direct evidence of "reach to affected communities" |

**Failure signal**: Fewer than 2 replies from all 6 Tier 1 contacts at Day 14.

**Failure escalation**: If fewer than 2 replies at Day 14:
1. Activate full Domain 54 Tier 2 (Desmond Meade, Samuel Sinyangwe, NAACP LDF, Brennan Center Criminal Justice) on Day 15
2. Prepare a separate 2-page "Virginia constitutional amendment briefing" — excerpting Domain 54's felony disenfranchisement analysis specifically for the November 2026 Virginia ballot context — and distribute to Virginia civic organizations via a targeted Tier 2 sub-send
3. Flag in CHECKIN.md: "Domain 54 Tier 1 engagement below 2 replies at Day 14. Recommending Tier 2 activation and Virginia standalone briefing."

---

## Cross-Domain Monitoring Synthesis (June 10 Gate)

At June 10, all four Phase 2b domains have sent (under STRONG) and are within their active engagement windows. This is the primary cross-domain synthesis point.

**June 10 synthesis assessment** (30 minutes, autonomous):

1. Tally engagement across all four domains:

| Domain | Contacts Sent | Replies Received | Score 3+ Count | Response Rate |
|--------|--------------|-----------------|---------------|---------------|
| Domain 51 | 5 Tier 1 | ? | ? | ?% |
| Domain 37 | 5 Tier 1 | ? | ? | ?% |
| Domain 42 Phase 2b | 5 Tier 1 | ? | ? | ?% |
| Domain 54 | 6 Tier 1 | ? | ? | ?% |
| COMBINED | 21 | ? | ? | ?% |

2. Apply the combined engagement thresholds from PHASE_2_EXPANSION_TIMELINE.md Part 4:
   - Combined 30%+: Tier 2 full expansion. Proceed to June 15 Tier 2 planning.
   - Combined 15–29%: Partial Tier 2 — activate for strongest domain only.
   - Combined <15%: Hold Tier 2. Flag in CHECKIN.md for user review.

3. Identify the cross-domain resonance pattern:
   - Are the same organizations engaging with multiple Phase 2b domains? (If yes: this is a network hub — prioritize their Tier 3 promotion and use them as social proof for all subsequent outreach)
   - Are specific findings generating cross-domain resonance? (The Citizens United dark money architecture in Domain 51 + the DEA regulatory capture in Domain 42 + the disenfranchisement numbers in Domain 54 should all be resonating with the same civil rights organizations — if they are, this validates the "interlocking mechanisms" argument central to the framework)

4. Write summary to PHASE_2_MONITORING_CHECKPOINTS.md (this file, append below): three sentences: [combined response rate], [strongest domain], [weakest domain]. This is the standing record for June 15 planning.

---

## June 15 Tier 2 Expansion Decision

**Inputs**: June 10 synthesis assessment + Day 14 checkpoint data for Domain 51 (June 14) and Domain 37 (June 16 under STRONG).

**Decision tree**:

```
Combined Phase 2b engagement at June 15:

  4+ Score 3+ replies (from any combination of domains)
    → FULL TIER 2 EXPANSION
    → Activate all Tier 2 contacts across all four domains
    → Use multi-domain social proof framing: "Following engagement from [Org A, Org B, Org C]..."
    → Week 6 (June 22–28) is Tier 2 execution week
    → Estimate: 20–25 Tier 2 sends across all four domains

  2–3 Score 3+ replies
    → SELECTIVE TIER 2 EXPANSION
    → Activate Tier 2 only for the 2 highest-performing domains
    → Use single-domain social proof framing per domain
    → Week 6 partial execution: 10–12 Tier 2 sends

  1 Score 3+ reply
    → HOLD TIER 2, EXTEND TIER 1 WINDOW
    → Send one follow-up to non-responding Tier 1 contacts in the strongest domain
    → Wait until July 1 for Tier 2 decision
    → 1 Score 3+ reply is meaningful but insufficient for multi-domain Tier 2 expansion

  0 Score 3+ replies
    → FLAG IN CHECKIN.md: "Phase 2b produced zero Score 3+ replies at Day 14 across all domains.
       User decision required on whether to continue, pivot messaging, or defer to August."
    → No automated Tier 2 activation
    → Phase 2a (Domains 56/39/57/59) continues on standard schedule regardless
```

**User action required at June 15**: If combined engagement is below 2 Score 3+ replies across all four domains, user needs to decide the Phase 2b direction. Everything else is autonomous execution.

---

## Feedback Integration Windows

**When to collect feedback**: Continuously — every reply is feedback. Log it in the tracking spreadsheet column H.

**When to synthesize feedback**: At each Day 7 checkpoint. The synthesis question is: what specific finding, framing, or reform proposal is generating engagement? This informs the next domain's templates.

**When to apply feedback to the next domain**: Before sending the next domain's Tier 1 wave. Synthesis happens during the 2-day gap between sends.

**Feedback integration examples**:

- If Domain 51 Day 7 reveals that the FEC quorum failure finding (not the Citizens United structural argument) generated the most engagement: lead with the FEC quorum failure in Domain 37 templates (the election administration angle connects directly)
- If Domain 37 Day 7 reveals that CISA election security defunding resonated more than DOJ voter roll litigation: in Domain 54, lead with the voter suppression → civic exclusion pipeline, not the structural democratic design argument
- If Domain 42 produces engagement from a contact who specifically notes the Yale Law Journal regulatory capture argument: in Domain 54, reference the same "regulatory capture of law enforcement agencies" framing — the structural argument is transferable

**What not to do with feedback**: Do not revise domain documents in response to individual replies before the Day 14 checkpoint. Revisions during an active engagement window create version-control problems (contacts who received the original Gist now have a different document than contacts who receive an updated one). Revisions should wait until all four domains have completed their Day 14 checkpoints.

---

*Document created: May 27, 2026. Covers Phase 2b expansion domains (37, 42, 51, 54) monitoring checkpoints and escalation. Standalone — no cross-references required for checkpoint execution.*
