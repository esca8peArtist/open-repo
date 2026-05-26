---
title: "Phase 1 Wave 1 Synthetic Timeline"
created: 2026-05-26
status: PRODUCTION-READY — complete execution map through Phase 2 sequencing decision
scope: "May 28 through June 30 (Day 30) with Phase 2 gates through July-August"
version: 1.0
companion_files:
  - day-7-14-30-decision-trees.md
  - DOMAIN_56_DISTRIBUTION_STRATEGY.md
  - DOMAIN_39_DISTRIBUTION_STRATEGY.md
  - DOMAIN_39_JUNE1_PRE_PRODUCTION_CHECKLIST.md
  - TOO_EARLY_CONTINGENCY_STAGING_MAY26.md
  - reply-triage-framework.md
  - PHASE_1_WAVE_1_MONITORING_DASHBOARD.md
---

# Phase 1 Wave 1 Synthetic Timeline
## Complete Execution Map — May 28 through Phase 2 Sequencing Decision

**Version 1.0 — May 26, 2026**

---

## Overview

This document maps the complete Phase 1 Wave 1 execution timeline from the May 28 Domain 56 distribution through the June 30 Day 30 checkpoint and the resulting Phase 2 sequencing decision. It identifies every checkpoint, dependency, escalation criterion, and outcome classification gate.

Key dependencies:
- May 28 Domain 56 distribution is the Wave 1 start date
- May 28 synthesis (19:00 UTC) is independent of the distribution — it runs on data from Wave 1 contacts sent May 18-26
- June 1 Domain 39 distribution is the second Wave 1 send — it runs on the HHS rule deadline and is independent of Domain 56 response signals
- Day 7 (June 4-5) is the first formal monitoring checkpoint
- Day 30 (June 27-28) is the Phase 2 gate

---

## Phase 1 Wave 1: Full Timeline

### May 28, 2026 — Distribution Window Opens

**Domain 56 (Civil Service) Tier 2 distribution**

Send window: 08:00 UTC start. All four sends should complete by end of day.

| Send | Organization | Contact | Template | Rationale for Order |
|---|---|---|---|---|
| 1 | Volcker Alliance | volcker@volckeralliance.org | Template 1 | Highest institutional credibility hook; German Berufsbeamtentum + Pendleton Act framing |
| 2 | Democracy Forward | info@democracyforward.org | Template 4 (Democracy Forward para) | Active PEER v. Trump litigation; APA/Loper Bright arguments highest strategic value |
| 3 | CREW | citizensforethics.org/contact | Template 4 (CREW para) | FAQ extension hook; web form |
| 4 | Government Executive | editors@govexec.com | Op-ed pitch | Trade publication; editorial review cycle; different format |

**May 28, 19:00 UTC — Synthesis execution** (independent of distribution):
- Signal log (`post-wave-1-monitoring/wave-1-signal-log-may18-21.md`) must have zero [fill] placeholders before running
- Synthesis script (`synthesis-execution-monitor.py`) classifies Wave 1 batch 1 contacts (Weiser, Elias, Goodman, Chenoweth, Bassin — sent May 18-26)
- Classification: STRONG, MODERATE, WEAK, or TOO_EARLY
- Result logged in `synthesis-execution-log.txt` and posted to CHECKIN.md
- Domain 57/59 pre-production sequencing activated based on result (see "Phase 2 Sequencing" section below)

**Key clarification**: The May 28 synthesis classifies responses from the *earlier* Batch 1 Wave 1 contacts. The Domain 56 Tier 2 sends (today) are a new send batch. These are separate data streams feeding into the same monitoring dashboard.

**Dependencies at May 28**:
- No blockers: Domain 56 Tier 2 sends are path-independent (proceed regardless of synthesis outcome)
- Domain 39 Gist is live (created May 26) — ready for June 1 send
- Synthesis prerequisite: signal log has zero [fill] placeholders (user action required before 19:00 UTC)

---

### May 31, 2026 (Day 3 from May 28) — First Response Check

**Informal checkpoint — not a decision point**

- Check inbox: Any replies to May 28 Domain 56 sends?
- Apply Reply Triage Framework if any replies received (`reply-triage-framework.md`)
- Score each reply (Score 0-5); log in Contacts sheet
- Check Bitly click counts for Domain 56 Gist

**Day 3 escalation trigger**: Any Score 5 reply received at Day 3 triggers immediate Phase 2 pre-activation (do not wait for Day 7 or Day 30).

**Preparation for Domain 39**: May 31 is also the preparation day for Domain 39 sends.
- Fill email templates: replace `[Gist URL — insert before send]` with `https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b`
- Fill `[YOUR_NAME]` and `[YOUR_CONTACT_INFO]` in all 5 templates
- Run HHS status check: search "OBBBA Medicaid work requirements HHS rule June 2026" — if rule is blocked by injunction, the urgency framing shifts (rule still drops; distribution still proceeds)
- Verify Georgetown CCF address is `childhealth@georgetown.edu` (NOT ccf@georgetown.edu)
- Verify Brennan Center address is `kennardl@brennan.law.nyu.edu` (voting rights desk, NOT general inbox)

If Domain 39 prep is complete by May 31 evening, you are ready for the May 30 pre-deadline sends (Georgetown CCF and NHeLP were targeted for May 30 — if not yet sent, send by June 1 morning).

---

### June 1, 2026 — Domain 39 (Healthcare) Distribution Window

**HHS deadline trigger**: HHS must issue the interim final rule on OBBBA Medicaid work requirements by June 1, 2026. Organizations that receive the Domain 39 analysis before the rule drops can frame it as a democracy event, not just a health policy change.

**Domain 39 Tier 1 sends** (targeting May 30-June 1):

| Send | Organization | Email | Send Target | Notes |
|---|---|---|---|---|
| 1 | Georgetown Center for Children and Families | childhealth@georgetown.edu (CC: Catherine.Hope@Georgetown.edu) | May 30 | Disability exemption gap + NVRA Section 7 |
| 2 | National Health Law Program | info@healthlaw.org | May 30 | APA standing + rural hospital turnout penalty |
| 3 | Brennan Center for Justice | kennardl@brennan.law.nyu.edu | June 1 | NVRA Section 7 private right of action; timed to rule publication |
| 4 | Institute for Responsive Government | info@responsivegov.org | June 1-2 | NVRA-Medicaid AVR research extension |
| 5 | Black Mamas Matter Alliance | info@blackmamasmatter.org | June 2-3 | Maternal mortality as civic capacity loss; coalition framing |

**Domain 39 Gist URL**: `https://gist.github.com/esca8peArtist/131e8a94c955b973b87f7fb87d0f594b`
**Source document**: `domain-39-healthcare-access-democratic-infrastructure.md` (7,200 words, 47 citations)
**Full send guide**: `DOMAIN_39_JUNE1_PRE_PRODUCTION_CHECKLIST.md` Steps 4-5

**Dependency**: Domain 39 sends are path-independent. They proceed regardless of Domain 56 response signals, May 28 synthesis outcome, or Day 7 checkpoint result. The June 1 HHS rule deadline is a non-negotiable external anchor.

**If STRONG signal arrives from Domain 56 before June 1**: Include 1-2 quotes from Domain 56 Score 4-5 replies as social proof in Domain 39 Tier 2 and Tier 3 sends. Do not delay Tier 1 sends waiting for social proof to accumulate.

---

### June 4-5, 2026 — Day 7 Checkpoint

**Formal checkpoint. Run the Day 7 decision tree from `day-7-14-30-decision-trees.md`.**

**Data to pull** (from Google Sheets dashboard):
- Total Bitly clicks for Domain 56 Gist (Gist Views sheet, Week 1 column)
- Total reply count (Contacts sheet, non-empty Reply_Date column)
- Bounce count (Contacts sheet, Delivery_Status = "Bounced")

**Decision tree** (abbreviated — full tree in `day-7-14-30-decision-trees.md`):

| Condition | Determination | Action | Next checkpoint |
|---|---|---|---|
| 3+ bounces | CONTACT_VERIFY | Fix email addresses; resend to corrected list; restart Day 7 clock | Restart Day 7 |
| 15+ clicks AND 2+ replies | HOLD | No action — proceed normally | Day 30 (skip Day 14) |
| 5-14 clicks OR 0-1 replies | MONITOR | Recheck at Day 14 | Day 14 (June 11-12) |
| 0-4 clicks (confirmed delivery) | ESCALATE | Delivery diagnostic within 24h | Restart Day 7 if re-send |

**Note**: Day 7 metrics combine Domain 56 Tier 2 sends (May 28) with any Tier 1 domain sends that preceded them. If prior Batch 1 Wave 1 contacts (Weiser, Elias, etc.) replied before Day 7, those replies count toward the Day 7 reply total.

**Outcome classification note**: Day 7 is NOT a Phase 2 gate — it is a delivery and engagement confirmation checkpoint. Even a Day 7 ESCALATE determination does not affect Phase 2 planning; it triggers a delivery diagnostic and possible re-send. Phase 2 activation decisions are made at Day 30.

**Expected outcome at Day 7**: Based on the profile of the Tier 2 contacts (institutional organizations with 5-10 day response cycles), Day 7 MONITOR or HOLD is the most likely result. ESCALATE is possible only if the Gist link is broken or emails went to spam.

---

### June 11-12, 2026 — Day 14 Micro-Checkpoint (conditional)

**Applies only if Day 7 determination was MONITOR.**

**Data to pull**: Cumulative Bitly clicks since Day 0.

| Cumulative clicks | Determination | Action | Next |
|---|---|---|---|
| 25+ | Escalate to HOLD | No action; continue to Day 30 | Day 30 |
| 10-24 | CONTINUE_MONITOR | Apply Modification 2 (framing revision); plan Day 45 re-send | Day 30 |
| < 10 | FAILURE_IMMINENT | Contact Tier 1 directly (phone/video); resend to corrected list; new Bitly links | Day 30 with contingency active |

If Day 7 was HOLD, skip Day 14 entirely and go directly to Day 30.

---

### June 27-28, 2026 — Day 30 Checkpoint (Phase 2 Gate)

**This is the primary Phase 2 sequencing decision point. Run the Day 30 decision tree from `day-7-14-30-decision-trees.md`.**

**Data to pull** (from Google Sheets dashboard):
- (A) Score 3+ reply rate: (count of Score 3+ replies) / (count of delivered emails) — expressed as percentage
- (B) Constituencies passing strong threshold: count of constituencies with 3+ Score 3+ replies (out of 7)
- (C) Cross-organizational referrals: count of confirmed or probable cross-org references
- (D) Confirmed adoption signals: count with Verification_Status = "Confirmed" in Adoptions sheet
- (E) Week 3-4 Bitly clicks: were Bitly clicks zero in both Week 3 AND Week 4? (YES/NO)

**Check order**: FAILURE first, then STRONG, MODERATE, WEAK, ASSESS. First match wins.

### Day 30 Outcome Classification Gates

---

**FAILURE** (most severe — check first):
- Condition: A<10% AND C=0 AND D=0 AND E=YES (both weeks 3-4 zero Bitly clicks)
- All four conditions must be simultaneously true
- Action: User decision required within 48h. Present three options: (1) CONTINUE with 90-day extension; (2) PIVOT to public-channel only; (3) CLOSE Phase 1 and move to Phase 2
- Domain 39 sends regardless (healthcare deadline is non-negotiable)
- Phase 2 sequencing: User decides within 48h

---

**STRONG**:
- Condition: A>=50% AND B>=4 AND C>=3 AND D>=2
- Action (within 24h): Domain 39 sends by end of Day 1 (if not already sent); Domain 56 Wave 2 law school sends begin Day 1-2; Tier 2 pre-briefing begins; social proof quotes from Score 4-5 replies prepared
- Phase 2 sequencing: Full activation immediately. See "Phase 2 Sequencing: STRONG" below.

---

**MODERATE**:
- Condition: A 20-49% OR B>=3 OR C>=1 OR D>=1 (but not meeting STRONG threshold)
- Action: Domain 39 sends within 24h; Domain 56 distribution to law school Tier 2 held until Day 37; Phase 1 monitoring extended through Day 60; Tier 2 expansion staged but not sent
- Phase 2 sequencing: Partial activation. See "Phase 2 Sequencing: MODERATE" below.

---

**WEAK**:
- Condition: A<20% AND B<2 AND C=0 AND D=0 (but not meeting FAILURE threshold)
- Action: Three modifications activated:
  - Modification 1 (Stakeholder substitution by Day 37): Replace 30% of non-responding Tier 1 with Tier 1.5 contacts
  - Modification 2 (Framing revision by Day 35): Shift to single-domain operational resource framing
  - Modification 3 (Channel shift by Day 45): Move 50% effort to network intermediaries
- Domain 39 sends regardless
- Phase 2 sequencing: Deferred to Day 90 checkpoint. See "Phase 2 Sequencing: WEAK" below.

---

**ASSESS** (partial signals):
- Condition: Some of A/B/C/D above zero but below MODERATE threshold (A 10-19% with B>=1 or C>=1 or D>=1)
- Action: Domain 39 sends only; Phase 1 extended to Day 60; prepare both contingency and normal Phase 2 options in parallel; wait for Day 60 with fuller data
- Phase 2 sequencing: Hold until Day 60 (July 27-28). Both paths prepared in parallel.

---

### Pre-Day-30 Score 5 / Score 4 Cluster Override

If a Score 5 event (implementation signal) is received at ANY point before Day 30:
- Trigger immediate Phase 2 pre-activation (do not wait for Day 30)
- Domain 39 distribution within 48h
- Update CHECKIN.md "Needs Your Input"
- Source: `day-7-14-30-decision-trees.md` — "Pre-Day-30 Rapid-Response Signals" section

If two or more Score 4 events occur within 14 days:
- Treat as pre-Day-30 STRONG signal
- Execute STRONG protocol
- Do not wait for Day 30 checkpoint

---

## Phase 2 Sequencing (Activated at Day 30)

### STRONG Outcome Sequencing

**Domain 39 distribution**: Day 1 of Phase 2 activation (June 28-29) — all 5 emails sent with social proof from Domain 56 Score 4-5 replies included in Tier 2/3 covers

**Domain 56 Wave 2 (law school Tier 2)**: Day 1-2 of activation — use Score 4-5 replies from Tier 1 as social proof anchor

**Domain 57 (Multilateral Withdrawal) pre-production**: June 15 research launch hold — begin research; distribution target August 10 (six weeks before UNGA 81)

**Domain 59 (Economic Precarity)**: June 15 parallel research launch (alongside Domain 57)

**Tier 2 pre-contact list preparation**: All four constituencies — immigration legal aid, law schools, unions, think tanks — Stage outreach materials for Week 5 (June 22-28) sends

**Signal from synthesis**: STRONG outcome suggests the democratic-design framing is resonating. Accelerate cadence.

---

### MODERATE Outcome Sequencing

**Domain 39 distribution**: Same as STRONG — Day 1 (non-negotiable healthcare deadline)

**Domain 56 Wave 2**: Hold to Day 37 (July 4-5) — assess additional Tier 1 responses before expanding

**Domain 57 pre-production**: June 10 research start; distribution target remains August 10

**Domain 59 pre-production**: July 1 secondary research start

**Tier 2 expansion**: Plan but do not send until Day 37 assessment shows upward trajectory

**Extended monitoring**: Phase 1 monitoring continues through Day 60

---

### WEAK Outcome Sequencing

**Domain 39 distribution**: Day 1 (non-negotiable)

**Domain 56 Wave 2**: Hold to Day 60 checkpoint (July 27-28) — do not expand until failure recovery shows improvement

**Domain 57 pre-production**: Deferred — start August 1 (not June 15); distribution target TBD

**Domain 59 pre-production**: Deferred — start July 15; distribution target TBD

**Alternative domain sequencing**: Per `TOO_EARLY_CONTINGENCY_STAGING_MAY26.md` WEAK-specific actions:
- Domain 38 (AI Regulatory Capture): June 3 research start; June 30 distribution target
- Domain 40 (Surveillance Capitalism): June 22 research start; July 15 target
- These are audience-diversification plays while Phase 1 failure recovery runs

**90-day extension**: Phase 1 extended to Day 90 checkpoint (August 26)

---

### ASSESS Outcome Sequencing

**Domain 39**: Day 1 (non-negotiable)
**All other domains**: Prepare both STRONG and WEAK sequencing in parallel — do not commit until Day 60 checkpoint provides more data
**Day 60 decision point**: July 27-28

---

## Timeline Summary Table

| Date | Event | Domain | Determination needed | Dependencies |
|---|---|---|---|---|
| May 28, 08:00 UTC | Domain 56 Tier 2 distribution | Civil Service | None — proceed | Gist live; templates filled with name/contact |
| May 28, 19:00 UTC | May 28 synthesis execution | Wave 1 batch 1 (Weiser et al.) | STRONG / MODERATE / WEAK / TOO_EARLY | Signal log has zero [fill] placeholders |
| May 30 | Domain 39 Tier 1 pre-deadline sends | Healthcare | None — proceed | Gist live; templates filled; HHS status checked |
| June 1 | Domain 39 Tier 2 send (Brennan Center) | Healthcare | None — proceed | HHS rule published or pending |
| June 2-3 | Domain 39 Tier 3 sends | Healthcare | None — proceed | Tier 1 response check |
| June 4-5 | Day 7 checkpoint | Domain 56 + 39 combined | HOLD / MONITOR / ESCALATE / CONTACT_VERIFY | Dashboard with clicks + replies |
| June 11-12 | Day 14 micro-checkpoint | All | (if Day 7 = MONITOR only) | Cumulative click count |
| June 27-28 | Day 30 checkpoint (Phase 2 gate) | All | STRONG / MODERATE / WEAK / ASSESS / FAILURE | Four metrics: A/B/C/D |
| June 28-29 | Domain 39 Tier 2/3 sends (if STRONG or MODERATE) | Healthcare | Activated by Day 30 | Score 4-5 quotes from Domain 56 for social proof |
| July 4-5 (Day 37) | Domain 56 Wave 2 law school sends (if MODERATE) | Civil Service | Conditional on Day 30 MODERATE | Tier 1 response trend |
| July 27-28 | Day 60 checkpoint | All | MOVEMENT / PARTIAL / BELOW_TARGET | Full Phase 1 dataset |
| August 10 | Domain 57 distribution target (STRONG/MODERATE) | Multilateral Withdrawal | Research complete | UNGA 81 six-week window |

---

## Escalation Criteria Summary

**Immediate escalation** (do not wait for next checkpoint):
- Any Score 5 reply (implementation signal) at any point → Phase 2 pre-activation
- Two or more Score 4 replies within 14 days → Early STRONG signal
- 3+ bounced addresses → CONTACT_VERIFY (same-day action)

**Day 30 escalation thresholds** (Phase 2 gate conditions):
- STRONG: A>=50% AND B>=4 AND C>=3 AND D>=2 → Full Phase 2 immediate
- FAILURE: A<10% AND C=0 AND D=0 AND Weeks 3-4 Bitly=0 → User decision required 48h

**June 1 non-negotiable**: Domain 39 sends proceed regardless of any monitoring outcome, synthesis result, or Phase 1 signal state. The HHS rule deadline is an external anchor that overrides all Phase 1 signal logic.

---

## Outcome Classification Gates at Each Checkpoint

| Checkpoint | Gate question | Pass condition | Fail condition |
|---|---|---|---|
| Day 7 | Is delivery confirmed and minimum engagement happening? | 15+ clicks OR 2+ replies, 0-2 bounces | 3+ bounces (re-verify) OR 0-4 clicks (delivery diagnostic) |
| Day 14 (if triggered) | Is engagement recovering from low Day 7? | 25+ cumulative clicks | < 10 cumulative clicks (FAILURE_IMMINENT) |
| Day 30 | Is Phase 1 on track for STRONG/MODERATE? | A>=20% OR B>=3 OR C>=1 OR D>=1 (at minimum MODERATE) | All four metrics below threshold (WEAK/FAILURE) |
| Day 60 | Has Phase 1 achieved movement-scale impact? | Multiple confirmed adoptions; cross-org referrals visible | Below targets after extended timeline |
| Pre-Day-30 Score 5 override | Early adoption signal | Any Score 5 reply | N/A — override always passes to Phase 2 |

---

*Synthetic timeline created: May 26, 2026. Phase 1 Wave 1 execution map complete through Phase 2 sequencing decision. All dates are calendar days from May 28 Domain 56 send unless otherwise noted.*
