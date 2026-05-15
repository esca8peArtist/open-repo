---
title: "User Decisions Required for Tier 1 Phase 1 Launch"
project: cybersecurity-hardening
created: 2026-05-15
status: awaiting-user-decision
phase: Phase 1 — Pre-Launch Authorization
decision-owner: Anya
launch-target: June 1, 2026
estimated-decision-time: 30–60 minutes
---

# User Decisions Required for Tier 1 Phase 1 Launch

**Status**: Everything is prepared and production-ready. This document lists what only the user can decide before outreach begins.

**Estimated time to work through this document and make all decisions**: 30–60 minutes.

**After decisions are made**: The agent can complete any remaining prep tasks (Gist updates, document revisions) within 60–90 minutes. User can then launch on any chosen date.

---

## Summary: What Is Ready vs. What Needs a Decision

| Category | Status |
|---------|--------|
| Corpus (Gist) | Published and verified accessible |
| Email templates (Senate, think tank, law school, civil rights) | Complete — personalization hooks ready |
| Email templates (Tier 1A immigration legal aid: NILC, CLINIC, RAICES, ILRC, NLG) | Complete — full personalized drafts in TIER1_OUTREACH_PREPARED.md |
| Contact list (25 contacts) | 5 Tier 1A national organizations fully verified; 20 research methodology documented; Senate/think tank/law school contacts identified and ready for verification |
| Pre-flight checklist | Complete — 10 sections, 45–60 min to execute |
| Execution calendar | Complete — full day-by-day schedule June 1–21 |
| Contingency protocols | Complete — A, B, C, D fully documented |
| **Day 1 send date** | **DECISION REQUIRED** |
| **Which contact track to launch first** | **DECISION REQUIRED** |
| **Corpus accuracy flags (3 items)** | **DECISION REQUIRED** |
| **Escalation authorization if reply rate falls below threshold** | **DECISION REQUIRED** |

---

## Decision 1: Day 1 Send Date

**What the agent recommends**: June 1, 2026 (Monday). This is the date in the Execution Calendar and all pre-launch prep is calibrated to a May 31 Day 0 / June 1 Day 1 schedule.

**Why June 1**: Monday sends to Senate staff and think tanks have strong engagement windows. The June 12 Section 702 FISA reauthorization deadline creates a natural time-anchor for Week 2 follow-ups that would not be available if launch is delayed to mid-June or later.

**If you want to launch earlier**: The earliest practical date is this week (week of May 19–23) given that contact verification needs 5–7 days and infrastructure setup needs 2–3 days. The June 12 FISA anchor would still be usable for follow-ups.

**If you want to launch later**: Any delay past June 7 forfeits the FISA reauthorization anchor for Week 1 contacts. After June 15, the Section 702 hook becomes stale. July 1 is the next natural window (post-FISA, new legislative cycle), but Phase 1 response collection compresses against the July 26 quarterly review date.

**Your decision**:
- [ ] Launch June 1, 2026 as planned
- [ ] Launch earlier: [date] — I understand the pre-launch window needs to compress accordingly
- [ ] Launch later: [date] — I understand the FISA timing anchor becomes unavailable
- [ ] Not ready to decide — I need to review [specific documents] first

---

## Decision 2: Which Contact Track to Launch First

**Background**: Two distinct outreach tracks are prepared and ready:

**Track A: Policy/Institutional Track** (PHASE_1_EXECUTION_CALENDAR.md)
- 25 contacts: Senate staff (8), think tanks (10), law school clinics (7), civil rights organizations (2)
- Wave 1 = Senate staff, Waves 2–3 = think tanks and law schools
- Goal: Policy adoption, legislative documentation, and institutional credibility
- Timeline: June 1–21 active sends; June 7/15/19 gate checkpoints
- Success metric: Briefing meetings scheduled (3+ by Day 14)

**Track B: Grassroots/Direct-Need Track** (TIER1_OUTREACH_PREPARED.md + TIER1_DISTRIBUTION_PREP.md)
- 25 contacts: Immigration legal aid — NILC, CLINIC, RAICES, ILRC, NLG (national) + 20 regional organizations
- Wave 1 = 5 national immigration legal aid organizations; Waves 2–3 = community organizations and mutual aid networks
- Goal: Direct distribution to populations facing active ELITE targeting
- Timeline: 6–7 weeks total; Weeks 1, 2, 3 for each tier
- Success metric: Response rate 10%+ by end of Week 2; corpus forwarded to client networks

**The agent has prepared both tracks fully.** You do not have to choose one and abandon the other — they can run in parallel. However, parallel tracks require more daily attention (two sets of contacts to monitor and respond to).

**Your decision**:
- [ ] Track A only (policy/institutional) — I want institutional adoption and policy impact first
- [ ] Track B only (grassroots/direct-need) — I want the corpus reaching at-risk populations first
- [ ] Both tracks in parallel starting June 1 — I have bandwidth to manage 10 active contacts simultaneously
- [ ] Both tracks sequentially — Track [A/B] first, then Track [B/A] starting in Week 3
- [ ] Not ready to decide — I want to see [specific criteria or information] first

---

## Decision 3: Corpus Accuracy Flags — Three Items Requiring Action or Deferral

Three accuracy gaps were documented in PHASE_1_FLAGS_ASSESSMENT.md (May 7, 2026). Each requires your decision on timing: resolve before launch, resolve concurrently, or defer.

### Flag 1: Mobile Fortify — Field Biometric Deployment (HIGH PRIORITY)

**The issue**: The corpus does not clearly explain that ICE's Mobile Fortify system enables biometric collection at any street encounter — not only at formal checkpoints. The countermeasures are correct; the contextual framing is incomplete.

**Estimated effort**: 15–20 minutes. Add one paragraph to opsec-playbook.md biometric section. Agent can do this.

**Recommendation**: Resolve before launch. This is a 15-minute fix that removes a meaningful gap for Tier 1A audiences (immigration legal aid organizations whose clients face street encounters with ICE agents).

**Your decision**:
- [ ] Resolve before launch — agent should update the Gist before Day 1 sends
- [ ] Resolve concurrently — agent updates Gist within 72 hours of Day 1; send recipients an update note
- [ ] Defer to July 26 quarterly review — I accept the gap for Phase 1 distribution

### Flag 2: DOGE/SSA Litigation Status (MEDIUM PRIORITY)

**The issue**: The corpus states that "at least 15 federal lawsuits were challenging [DOGE SSA data access] as of early 2026." This is now inaccurate — the Fourth Circuit vacated the preliminary injunction in April 2026 and SSA data access is operational. The countermeasures are unchanged; only the litigation framing is outdated.

**Estimated effort**: 10–15 minutes. Update one sentence in threat-model.md. Agent can do this.

**Recommendation**: Defer to July 26 quarterly review. This is a litigation status update, not a capability gap. The underlying countermeasures do not change. If a recipient explicitly asks about DOGE status, provide the updated status verbally and note it for the July revision.

**Your decision**:
- [ ] Resolve before launch — update the framing now
- [ ] Defer to July 26 quarterly review — acceptable at current risk level
- [ ] Defer — provide verbal updates if recipients ask

### Flag 3: Cellebrite Device Seizure / BFU-AFU Distinction (HIGH PRIORITY)

**The issue**: The corpus does not explain the BFU/AFU device state distinction — that a physically confiscated device in After-First-Unlock state is significantly more vulnerable to Cellebrite extraction than a powered-off device. This affects how readers configure GrapheneOS auto-reboot and wipe passphrase settings.

**Estimated effort**: 45–60 minutes. Add a new subsection to implementation-guide.md covering BFU/AFU, wipe passphrase, and auto-reboot configuration. Agent can do this.

**Recommendation**: Resolve before launch. This directly affects device security guidance for high-risk populations (immigration attorneys and activists facing arrest risk) and is a meaningful gap in the current guide.

**Your decision**:
- [ ] Resolve before launch — agent should update the Gist before Day 1 sends
- [ ] Resolve concurrently — agent updates within 72 hours of Day 1
- [ ] Defer to July 26 quarterly review — I accept the gap for Phase 1 distribution

**Combined effort if resolving Flags 1 and 3 before launch**: 60–80 minutes total agent work. Agent can complete both and publish an updated Gist the day you approve.

---

## Decision 4: Escalation Authorization — Low Reply Rate Response

**Background**: The Execution Calendar includes pre-committed contingency protocols. However, two of them require authorization that goes beyond standard email follow-up:

**Contingency A: Phone outreach to Senate offices (activates if fewer than 3 Stage 1+ replies by Day 4)**

If the Week 1 Senate staff outreach generates very low engagement, Contingency A calls for escalated phone calls to the top 3 Senate offices. This is a judgment call that benefits from your authorization:
- Phone calls require more preparation and are more assertive than email follow-up
- If you have any concern about phone outreach to Senate staff specifically, this contingency can be modified to "additional email variants only"

**Your decision**:
- [ ] Authorized — proceed with phone outreach to Senate offices if Contingency A triggers
- [ ] Restricted — email follow-ups only, no phone outreach to Senate offices
- [ ] Case-by-case — confirm with me before calling any Senate office

**Contingency B: Tier 2 timeline deferral (activates if fewer than 2 policy uptake signals by Day 14)**

If Phase 1 adoption is below threshold, Contingency B defers Tier 2 Group B from July 15 to August 1. This is logged internally in WORKLOG.md and does not require user action — but you should be aware that this is a pre-committed protocol and understand the logic before it potentially activates.

**Your decision**:
- [ ] Confirmed — I understand and pre-authorize Contingency B deferral if triggered
- [ ] Flag me before deferring — I want to be consulted before Tier 2 timeline changes

---

## Decision 5: Warm Introduction Outreach (Optional — High Impact)

**Background**: The Execution Calendar recommends that if you have existing professional relationships with any of the 25 contacts (or their colleagues), you send a 1-sentence warm introduction note via that mutual contact on May 29–30. This is estimated to increase Week 1 reply rate by approximately 15%.

**This requires knowing whether such relationships exist** — something only you can determine.

**Your decision**:
- [ ] I have mutual contacts with some organizations — I will send warm introduction notes before May 31
- [ ] I have no relevant mutual contacts — skip this step
- [ ] Uncertain — I will check my network and decide before May 29

---

## Decision 6: Gist Content Finality

**Background**: The corpus (Gist) is published and verified accessible. Before launch, you should confirm that the content reflects your final intended message on these specific points:

1. **Tone and attribution**: The corpus is published under username `esca8peArtist`. Are you comfortable with this attribution for Phase 1 policy outreach to Senate staff and institutional contacts? Some contacts may verify the Gist URL's authorship.

2. **Scope statements**: The corpus states explicitly that it does not protect against targeted investigation with a full government court order — only against bulk commercial surveillance infrastructure. Is this scope limitation still the intended framing?

3. **Spanish translation**: The corpus notes that a Spanish-language version of Part 0 is planned for July 2026. Is this still accurate, and is there anything in the current corpus that should be updated before it reaches Tier 1B community organizations?

**Your decision**:
- [ ] Corpus content is final — no changes needed before Day 1
- [ ] Corpus needs specific updates: [describe changes]
- [ ] I want to review the Gist one more time before approving: [I'll do this by date]

---

## Summary: Decision Record Template

Fill this in when you've made your decisions. Share with the agent to confirm launch authorization.

```
TIER 1 PHASE 1 LAUNCH AUTHORIZATION

Date of this decision: _______________
Decision owner: Anya

Decision 1 — Launch date: _______________
Decision 2 — Contact track: [ ] Track A  [ ] Track B  [ ] Both parallel  [ ] Both sequential: A then B / B then A
Decision 3 — Corpus flags:
  Flag 1 (Mobile Fortify): [ ] Resolve before launch  [ ] Concurrent  [ ] Defer July 26
  Flag 2 (DOGE litigation): [ ] Resolve before launch  [ ] Defer July 26  [ ] Defer + verbal
  Flag 3 (Device seizure): [ ] Resolve before launch  [ ] Concurrent  [ ] Defer July 26
Decision 4a — Phone outreach authorization: [ ] Authorized  [ ] Email only  [ ] Case-by-case
Decision 4b — Contingency B pre-authorization: [ ] Pre-authorized  [ ] Flag before deferring
Decision 5 — Warm introduction outreach: [ ] Yes — I have connections  [ ] No  [ ] Checking
Decision 6 — Corpus content: [ ] Final  [ ] Needs updates: ________________

LAUNCH AUTHORIZED: [ ] YES  [ ] NO — pending: ________________
```

---

## What Happens After You Authorize

Once you fill in the decision record and authorize launch:

1. **Agent completes any corpus updates** (Flags 1 and/or 3 if selected) — 60–80 minutes
2. **Agent publishes updated Gist** and confirms revision notes — 5 minutes
3. **User completes Day 0 pre-launch checklist** (TIER_1_DAY1_EXECUTION_CHECKLIST.md) — 90–120 minutes
4. **User sends Day 1 Wave 1** (5 Senate contacts, 8:30–8:50 AM) — 45–60 minutes

**Total user time from authorization to first send**: Approximately 30–60 minutes of decision time now, plus 90–120 minutes of Day 0 prep, plus 60 minutes Day 1 morning.

**The campaign then runs for 21 days** (June 1–21) at 30–60 minutes per day of monitoring and responding, with three gate checkpoints (June 7, 15, 19) where you assess metrics and make go/caution/stop decisions.

---

*Created: 2026-05-15. Consolidates pending decisions from: TIER1_PHASE1_READINESS_SUMMARY.md, PHASE_1_FLAGS_ASSESSMENT.md, PHASE_1_EXECUTION_CALENDAR.md.*
