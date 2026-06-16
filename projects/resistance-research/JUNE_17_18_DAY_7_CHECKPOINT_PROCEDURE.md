---
title: "June 17-18 Day 7 Checkpoint Procedure — Phase 2 Wave 1 T+7 Gate Decision"
created: 2026-06-16
purpose: "Actionable procedure for executing the T+7 gate decision at the June 17-18 checkpoint"
covers_domains: [51, 59, 48]
gate_framework_source: "PHASE_1_COALITION_LEVERAGE_MATRIX.md (Sections 5, 7)"
orchestration_script: "PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py"
status: production-ready
---

# June 17-18 Day 7 Checkpoint — T+7 Gate Decision Procedure

*Resistance Research — June 16, 2026*

---

## SCHEDULING NOTE — Checkpoint Overlap

June 17-18 is a dual critical date: resistance-research Wave 1 T+7 gate **and** the stockbot June 17 retrain execution window (see `PROJECTS.md`, stockbot section and `JUNE_17_RETRAIN_EXECUTION_CHECKLIST.md`). These are independent work streams but they compete for your attention on the same calendar day. Sequence recommendation: complete the stockbot retrain verification first (earlier in the day, fixed time window), then execute the resistance-research checkpoint using this procedure in the afternoon or evening. Both are time-sensitive but the retrain has the harder external deadline. Do not let either slip into June 18 if preventable.

---

## Section 1: Pre-Checkpoint Checklist (June 17 EOD)

Complete all items before running the T+7 assessment. This is the data-gathering phase. The gate decision in Section 2 is only meaningful if the inputs below are accurate.

**1.1 — Confirm Wave 1 sends are logged in the orchestration script**

For each domain you sent during June 16-17, verify that every completed send is recorded:

```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --status
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --status
```

For any send you completed manually that is not yet logged, log it now:

```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-send 1 --time "2026-06-16 HH:MM UTC"
```

Domain 59 sends: AFL-CIO (Send 1), CBPP (Send 2), NWLC (Send 3), MomsRising (Send 4), ITEP (Send 5).
Domain 51 sends: Campaign Legal Center/Chlopak (Send 1), Issue One (Send 2).
Domain 48 sends: Sentencing Project (Wave 1), Prison Policy Initiative (Wave 1) — tracked in DOMAIN_48_EMAIL_TEMPLATE_SET.md; no script support yet (Domain 48 not in orchestration script; log manually in WORKLOG.md).

**1.2 — Inbox review: classify every reply received**

Open your outbound email thread for each domain and check for replies. For every reply:

- STRONG: substantive engagement — asks a follow-up question, requests the full document, offers to share with colleagues, references the research specifically, or signals openness to co-distribution
- MODERATE: acknowledgment, forwarded to correct person, "thanks, I'll take a look," or a non-committal but positive response
- WEAK: auto-reply, out-of-office, generic "thanks"
- NONE: no reply (do not log NONE — it is the default state)

Log each reply immediately:

```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-reply 2 --signal STRONG --summary "CBPP requested one-pager for Senate Finance staff meeting"
```

**1.3 — Log any bounces**

If any email bounced (delivery failure notice in your outbox), log it and send the fallback address before the gate check:

```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-bounce 1 --fallback
```

Critical bounce notes from contact verification:
- Clean Money Action Fund (Domain 51 Wave 2, Send 5): use info@CAclean.org, not cleanmoney.org (unreachable since June 5)
- EPI (Domain 59 Wave 2, Send 6): researchdept@epi.org is unconfirmed — use contact form at epi.org/about/contact if you proceed to Wave 2

**1.4 — Check Gist access counts (qualitative signal)**

Visit each Gist URL and note the view/star count if visible. This is a secondary signal but can indicate passive distribution beyond direct recipients:
- Domain 59: https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba
- Domain 51: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
- Domain 48: https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8

**1.5 — Note the calendar anchor for Domain 59**

Domain 59's urgency frame has been updated (Session 3681) from the Senate Finance markup window (closed June 30) to the OBBBA implementation period (2025-2027 tax years) and 2026 midterm cycle. This means there is no hard cliff for Domain 59 responses — the pressure is continuous, not event-bounded. However, the July 1 Domain 51 California ballot deadline remains a hard external clock. Assess Domain 59 primarily on engagement quality, not speed-to-deadline pressure.

---

## Section 2: T+7 Gate Decision Framework

*Source: PHASE_1_COALITION_LEVERAGE_MATRIX.md, Sections 5 and 7*

Run the automated assessment for each domain after completing Section 1:

```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --t7-check
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --t7-check
```

The script will print a gate decision (FULL ACTIVATION / CONDITIONAL APPROVAL / WEAK THRESHOLD / BELOW THRESHOLD) based on the STRONG reply counts logged in Section 1.2. The gate thresholds are:

**Domain 59 gate thresholds** (5 Wave 1 contacts):
- FULL ACTIVATION: 3+ STRONG signals from AFL-CIO, CBPP, NWLC, MomsRising, ITEP
- CONDITIONAL APPROVAL: 2 STRONG signals
- WEAK THRESHOLD: 1 STRONG signal
- BELOW THRESHOLD: 0 STRONG signals

**Domain 51 gate thresholds** (2 Wave 1 contacts: CLC, Issue One):
- FULL ACTIVATION: 4+ STRONG (includes Wave 2 contacts — only possible if Wave 2 was also executed)
- CONDITIONAL APPROVAL: 2 STRONG signals
- WEAK THRESHOLD: 1 STRONG signal
- BELOW THRESHOLD: 0 STRONG signals

**Domain 48** (no script support): manual assessment. Wave 1 = Sentencing Project + Prison Policy Initiative. STRONG threshold for proceeding to Wave 2 (Brennan Center, Worth Rises, Campaign Legal Center, M4BL): 1 STRONG reply from either organization.

**Cross-domain combined signal** (from PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 5): the gate decision for Phase 2 sequencing beyond Wave 1 is aggregate across domains. If by June 17-18, two or more organizations from CBPP, Georgetown CCF, AFGE, Brennan Center, or Black Mamas Matter Alliance have replied with substantive engagement (STRONG), the transition signal is STRONG across the full Phase 2 program — authorize Tier 2 activation immediately. This is the cross-domain threshold; the per-domain thresholds above govern domain-specific wave sequencing.

**The T+14 checkpoint (July 1) is the primary Phase 2 routing event.** The T+7 checkpoint is an early signal check, not the final decision gate. A BELOW THRESHOLD result at T+7 does not terminate Phase 2 — it triggers the contingency playbooks in Section 4 and extends monitoring to T+14.

---

## Section 3: Tier 2 Activation Routing

Based on the T+7 output from Section 2, follow exactly one of the three paths below.

---

### Path A — STRONG Engagement (2+ STRONG from Wave 1 across any domain combination)

**Immediate action: activate Domain 51 Wave 2 and Domain 59 Tier 2 within 24 hours of checkpoint.**

Domain 51 Wave 2 (California campaign organizations — Common Cause CA, LWV CA, Clean Money Action Fund):
```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --execute wave2
```
Stagger: 90 minutes between sends. Total active time ~45-60 min, clock time ~3 hours.

Domain 59 Tier 2 (conditional on 2+ Tier 1 STRONG — EPI, Demos, NELP, NHLP):
```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --execute wave2
```
Stagger: 45 minutes between sends. Verify EPI email via epi.org/about/contact before send (researchdept@epi.org is unconfirmed).

Domain 48 Wave 2 (Brennan Center, Worth Rises, Campaign Legal Center, M4BL): execute per DOMAIN_48_EMAIL_TEMPLATE_SET.md. Wave 2 sends on June 18-19 per the current execution plan.

**Coalition pre-commitment asks to initiate (per PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 1 and Window analysis):**
- CBPP + AFL-CIO joint CTC statement: if CBPP returned STRONG, send the joint pre-commitment ask referencing the OBBBA implementation window and the CTC midterm framing. Do not reference the June 30 Senate Finance markup — that window is closed.
- Brennan Center Domain 51/56 co-pitch: if you have not yet sent the Domain 56 + Domain 51 combined ask (DOJ Voting Section 30→6 attorney fact anchors both), send now. This is the strongest single-pitch case identified in the leverage matrix.

**Domain 51 Wave 3** (national amplifiers — ECU/LAV, Public Citizen, Brennan Center, Democracy 21, OpenSecrets): do not activate at T+7 even if signals are STRONG. Wave 3 activates at T+15 after T+7 signal is confirmed through a second round of sends. This is organizational attention management — do not flood the queue.

---

### Path B — MODERATE Engagement (exactly 1 STRONG across all domains, or 2+ MODERATE with no STRONG)

**Action: delay Tier 2 sends by 3 days; hold Wave 3 until T+14.**

Do not execute Wave 2 sends on June 17-18. Set a calendar reminder for June 20-21 and reassess at that point. If by June 20 the STRONG count has not increased, consult Section 4 contingency playbooks.

During the 3-day delay:
1. Reply promptly to any MODERATE responders to deepen the relationship before the Tier 2 send. If a MODERATE responder named a colleague to contact, reach out to that colleague immediately — this is the "coalition-originated new contact" signal (Threshold 3 in PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 7) and is the single strongest network effect indicator.
2. Check if any sends that have not yet replied are particularly high-probability contacts. CBPP (Domain 59, Send 2, 55-70% response probability) and ITEP (Send 5, 55-70%) are the two highest-probability contacts in the Wave 1 set. If neither has replied by T+7, this is within normal range — academic and policy organizations often reply in 7-14 business days, not 7 calendar days.
3. Execute Domain 48 Wave 2 on its own schedule (June 18-19 per plan) regardless of Domain 51/59 signals. Domain 48 has separate organizational contacts (criminal justice ecosystem) and does not depend on the economic justice coalition engagement metrics.

---

### Path C — WEAK Engagement (0 STRONG signals across all Wave 1 sends at T+7)

**Action: run delivery diagnostic before any further sends. Do not activate Tier 2.**

Zero STRONG signals at T+7 is within the range of normal outcomes — T+7 in calendar days is T+5 in business days, and most organizations acknowledge research materials in 5-15 business days. However, 0 signals requires verification that emails were delivered before concluding that messaging needs adjustment.

Delivery diagnostic sequence:
1. Check your sent folder for each email. Confirm it was not filtered to your own spam or stuck in drafts.
2. For any contact where you have a backup address (Domain 59: AFL-CIO has aflcio.org/contact as form fallback; Domain 51: CLC has info@campaignlegal.org backup), do not resend yet — wait until T+10 before using fallback to avoid appearing as duplicate outreach.
3. Verify Gist URLs resolve correctly from an incognito browser. If a Gist is inaccessible or returns 404, that is a delivery failure affecting all recipients.
4. Do not interpret 0 STRONG at T+7 as messaging failure. See PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 7: "Zero Score 3+ replies from any of the five Tier 1 Phase 1 organizations by Day 14 (June 15): delivery diagnostic required before any further coalition pre-commitment asks." The relevant threshold is Day 14 (T+14), not Day 7.

Hold: do not send coalition pre-commitment asks to CBPP, AFL-CIO, or Brennan Center until T+14 data is available. The risk identified in PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 8, Risk 1 (coalition fatigue from simultaneous asks) applies here — premature follow-up before organizations have processed Wave 1 content will reduce, not increase, engagement probability.

---

## Section 4: Contingency Playbooks

### Contingency A — Wave 1 Response Rate Below 10%

Threshold: 0 replies from 10+ sends across all three domains at T+7.

This is not yet an alarm at T+7, but it warrants a delivery audit. Steps:
1. Run delivery audit per Path C Section 3 above.
2. Check whether the most recent send used the correct email domain. Domain 59: cbpp@cbpp.org (not president@ or named individual addresses). Domain 51: echlopak@campaignlegalcenter.org (not echlopak@campaignlegal.org — these are different domains). Domain 48: sentencingproject.org general inbox.
3. If delivery audit passes (emails sent, Gists resolve, no bounce notices), take no further action at T+7. Resume normal monitoring to T+14.
4. If T+14 still shows 0 replies: reassess subject lines. The research-to-research opening frame ("I'm writing because your organization's work is cited in...") is the documented higher-engagement approach over cold-pitch framing. If the Wave 1 emails did not open with a citation of the receiving organization's own work, that is the most likely cause of low engagement.

### Contingency B — Bounces Above 20%

Threshold: 2 or more bounces from 10 sends (20%+ bounce rate).

Immediately log all bounces using `--log-bounce`:
```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-bounce [SEND_NUM]
```

For each bounce, check the script output for available fallback addresses. All Domain 59 and Domain 51 contacts have been verified as of June 10-11, 2026. A post-June-10 bounce on a previously verified address usually indicates:
- Personnel change (executive director or program lead departed after verification date)
- IT change at the organization (email system migration)
- Catch-all inbox disabled

Action by contact:
- AFL-CIO (Send 1, feedback@aflcio.org bounced): use aflcio.org/contact web form as primary; include "For the Legislative Affairs team / Jody Calemine" as first line of body
- CBPP (Send 2, cbpp@cbpp.org bounced): check cbpp.org contact page for current inbox; this is the highest-priority bounce to resolve
- Clean Money Action Fund (Domain 51 Wave 2, Send 5): already known — use info@CAclean.org only, not cleanmoney.org
- Any Domain 51 contact: fallback addresses documented in script config; run `--domain 51 --log-bounce [NUM] --fallback` after using backup address

Do not attempt to find personal email addresses through OSINT for any contact where the organizational inbox has bounced. Use form submissions as fallback. If both primary and fallback are unavailable, note the gap in WORKLOG.md and move on — do not let a single-contact bounce delay the rest of the wave.

### Contingency C — Key Organizations Non-Responsive

The two most critical non-responses to monitor at T+7 are CBPP (Domain 59) and Campaign Legal Center (Domain 51), because both are the primary coalition anchor organizations for their respective domains.

**If CBPP (Domain 59, Send 2) has not replied by T+14 (July 1):**
Per PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 7: "Domain 59 zero CBPP engagement by June 20: CTC markup window is closing; shift immediately to warm-introduction path (identify CBPP policy team personal connections) rather than cold re-contact." The June 30 markup window is now past, so the urgency framing has shifted to OBBBA implementation (2025-2027 tax years). Updated action: if CBPP has not replied by T+14, do not cold-resend. Instead, check if any other Domain 59 respondent (NWLC, ITEP, MomsRising) can provide a warm introduction to the CBPP economic security team. This is the only high-probability path to CBPP engagement after an initial non-response.

**If Campaign Legal Center (Domain 51, Send 1) has not replied by T+14:**
CLC is the anchor for the Domain 51 FEC enforcement and Citizens United framing. Non-response at T+14 most likely reflects routing — the email may be at info@campaignlegal.org (general) rather than having reached Erin Chlopak (Senior Director, Campaign Finance) directly. Action: send to echlopak@campaignlegalcenter.org directly with a two-sentence note referencing the July 1 California Fair Elections Act ballot deadline and the Domain 51 Gist. This is the only verified direct-contact path that bypasses the general inbox.

**If all 5 Domain 59 Wave 1 contacts are non-responsive at T+14:**
This warrants a messaging assessment. Review whether the OBBBA implementation urgency frame (Session 3681 update) is actually landing as urgent to economic policy organizations that are already deeply engaged in OBBBA tracking from their own angle. If these organizations are receiving dozens of OBBBA-related communications daily, the research-to-research framing (citing their own published work in the opening) is the primary differentiator. If the opening line did not specifically cite their work, the next send should open with their specific finding.

---

## Section 5: Post-Checkpoint Next Steps

### If STRONG — Immediate Activation Timeline

Execute within 24 hours of confirming STRONG signal (June 17-18 checkpoint):

Day 0 (checkpoint day): run `--t7-check` for Domain 59 and Domain 51. Confirm STRONG threshold met.

Day 1 (June 18-19): execute Domain 59 Tier 2 (Wave 2: EPI, Demos, NELP, NHLP — 4 contacts, 45-minute stagger). Execute Domain 51 Wave 2 (Common Cause CA, LWV CA, Clean Money — 3 contacts, 90-minute stagger). Total June 18-19 active time: approximately 90 minutes.

Day 3-5 (June 20-22): reply to all STRONG and MODERATE Wave 1 respondents. Offer the one-page summary for internal distribution. This is the relationship-deepening window before the coalition pre-commitment ask.

Day 6-7 (June 23-24): coalition pre-commitment asks. If CBPP (Domain 59) returned STRONG: send the joint CBPP + AFL-CIO CTC statement pre-commitment ask anchored to the 2026 midterm GOTV cycle. If Brennan Center (Domain 51 Wave 3 contact) has been warmed through Domain 56 or Domain 51: send the Domain 56 + Domain 51 co-pitch.

Day 15 (July 1): T+14 checkpoint. Run `--all-domains-status`. Assess Domain 51 Wave 3 activation (national amplifiers: ECU/LAV, Public Citizen, Democracy 21, OpenSecrets). Wave 3 requires 2+ STRONG from Wave 1+2 combined. This is also the California Fair Elections Act ballot deadline — ensure Domain 51 Gist remains accessible and CA contacts have received materials in time.

```
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --all-domains-status
```

Domain 48 Wave 2 (June 18-19, per plan) is independent of Domain 51/59 gate decisions. Execute on schedule regardless of STRONG/MODERATE/WEAK outcome for other domains.

### If MODERATE — Delay and Deepen

Execute Wave 2 sends on June 20-21 (3-day delay). During the delay:
- Reply to any MODERATE respondents with a follow-up that includes the one-pager offer and a concrete single ask (share this link with your policy team / add your name to a joint statement)
- Set T+14 July 1 as the next formal assessment date
- Domain 48 Wave 2 proceeds on schedule (June 18-19) — no hold

T+14 July 1 gate thresholds (from PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 5): if by July 1, exactly one organization has replied with substantive engagement across all domains, proceed with calendar-deadline domains only (Domain 49 redistricting, Domain 51 California July 1, Domain 57 UNGA August 10). Hold Domain 50 and Domain 54 until the July 1 Day 30 checkpoint provides more data.

### If WEAK (Path C) — Retreat Path

Do not execute any Tier 2 or Wave 2 sends until T+14 data resolves the ambiguity.

The retreat path is not distribution termination — it is a 7-day hold to determine whether T+7 silence is a delivery issue, a timing issue, or a messaging issue. Per the coalition relationship maturity cycle documented in PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 5: organizations require 30-45 days from first contact to meaningful advocacy coordination readiness. A T+7 WEAK signal places you at Day 7 of a 30-45 day cycle. This is not a failure — it is the expected state for roughly half of all first-contact sends.

If T+14 also returns WEAK or BELOW THRESHOLD: consult the Failure Thresholds and escalation criteria in PHASE_1_COALITION_LEVERAGE_MATRIX.md, Section 7 before deciding whether to continue with current messaging or redesign the outreach frame.

---

## Quick Reference — Command Set for June 17-18

```bash
# Pre-checkpoint: verify all sends are logged
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --status
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --status

# Log any sends not yet recorded
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-send 1 --time "2026-06-16 14:05 UTC"

# Log replies as you review inbox
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-reply 2 --signal STRONG --summary "one sentence description"

# Log bounces
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --log-bounce 1 --fallback

# Run the T+7 gate assessment
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --t7-check
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --t7-check

# Combined status view
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --all-domains-status

# Confirm activation sequence before executing Wave 2
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --sequence-check

# Execute Wave 2 (only after STRONG/CONDITIONAL gate confirmed)
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 59 --execute wave2
uv run python projects/resistance-research/PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py --domain 51 --execute wave2
```

All commands run from the repository root. State persists to `projects/resistance-research/phase-1-adoption/data/wave_orchestration_state_d51.json` and `wave_orchestration_state_d59.json`. WORKLOG entries written automatically to `projects/resistance-research/WORKLOG.md`.

---

*Framework sources: PHASE_1_COALITION_LEVERAGE_MATRIX.md (Sections 5, 7, 8); PHASE_2_MULTI_DOMAIN_WAVE_ORCHESTRATION_SCRIPT.py (t7_gate config, cmd_t7_check, cmd_log_reply); PROJECTS.md (resistance-research current focus, June 17-18 checkpoint spec).*
