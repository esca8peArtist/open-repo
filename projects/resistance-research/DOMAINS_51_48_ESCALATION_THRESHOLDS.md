---
title: "Domains 51/48 Wave 1 — Escalation Thresholds & Response-Rate Decision Rubric"
created: "2026-06-24"
status: "ACTIVE — thresholds trigger based on clock and send count, not subjective assessment"
baseline: "June 24, 2026 04:11 UTC — zero sends confirmed"
scope: "Domain 51 (4 templates, Campaign Finance) + Domain 48 (5 templates, Criminal Justice). Total: 9 sends."
critical_deadline: "June 25 12:00 UTC — if zero sends, ESCALATE. June 27 18:00 UTC — last viable Wave 1 date."
lesson_applied: "SCOTUS Item 21: 'Attention friction > execution friction.' All thresholds below are numeric and time-anchored. No threshold uses words like 'soon,' 'concerning,' or 'consider.' Every trigger has one exact action."
---

# Domains 51/48 Wave 1 — Escalation Thresholds & Response-Rate Decision Rubric

---

## SECTION A: SEND-EXECUTION ESCALATION THRESHOLDS

These thresholds govern when to escalate if Wave 1 sends have not started. They are time-anchored to June 24 baseline (current date).

### Threshold Table — Send Execution

| Clock | Condition | Threshold Level | Action (exact) |
|-------|-----------|-----------------|----------------|
| June 24 12:00 UTC | 0 sends, 0 Gists | WARNING | Post to INBOX.md: "Wave 1 execution pending. Templates at `execution/domain-51-48-wave-1-execution-checklist.md`. Estimated time: 45–60 min. Gist creation adds 10 min per domain." |
| June 24 18:00 UTC | 0 sends | CAUTION | Add to CHECKIN.md: "Domain 51/48 Wave 1: zero sends as of 18:00 UTC June 24. Request user ETA." |
| June 25 12:00 UTC | 0 sends | **ESCALATE** | Write BLOCKED.md entry (template in Section A.1 below). Activate Domain 59 Tier 2 decoupled path. |
| June 25 18:00 UTC | 0 sends | **ESCALATE 2** | Add PROJECTS.md flag: "Domains 51/48 execution risk: Wave 1 48h+ overdue. Phase 2 timeline impact." Evaluate compressed catch-up (see WAVE1_CATCH_UP_PROCEDURES.md). |
| June 26 18:00 UTC | < 4 sends total | **HARD THRESHOLD** | Activate July async path. All remaining sends shift to July 1–7. Document in ORCHESTRATOR_STATE.md: "Domains 51/48 Wave 1 shifted to July async path (execution slipped past June 26 18:00 UTC)." |
| June 27 18:00 UTC | Any sends still outstanding | **DEADLINE CROSSED** | Remaining sends proceed but without "rapid-response" framing. Update templates to remove time-sensitive language ("during the Senate markup window"). June advocacy value still intact; Senate CTC advocacy value is reduced. |

**Key principle**: Each threshold level is determined solely by the clock and the number of sends confirmed. No threshold requires subjective assessment.

---

### Section A.1 — Pre-Written BLOCKED.md Entry (copy-paste at June 25 12:00 UTC)

Copy the text below exactly into BLOCKED.md if zero sends are confirmed at June 25 12:00 UTC:

```
## BLOCKED: Domains 51/48 Wave 1 Execution Overdue
Added: June 25 12:00 UTC
Priority: HIGH (cascades to Domain 59 timing risk)

Status: Wave 1 sends not confirmed as of June 25 12:00 UTC (48h+ past planned June 23 window).

User action required (one of three paths):

PATH A — Execute Wave 1 today (June 25):
  Templates: execution/domain-51-48-wave-1-execution-checklist.md
  Time needed: 45–60 min
  Remaining advocacy value: FULL (DISCLOSE Act markup window still open; Virginia July 15 intact)
  
PATH B — Confirm July async execution:
  Confirm date: July 1–7 for Domains 51/48 sends
  Domain 59 Tier 2 executes independently June 25–30 (no prerequisite)
  Advocacy value: ~85% of same-week value (DISCLOSE Act window may narrow; Virginia still intact)

PATH C — Flag a blocker:
  If any template needs revision or execution is blocked, reply with specific issue
  Orchestrator can revise templates or execution plan within current session

Domain 59 Tier 2 status: INDEPENDENT — not gated on this block. Proceeding on June 25–30 schedule.
```

---

## SECTION B: RESPONSE-RATE DECISION RUBRIC

These thresholds govern what to do once sends are confirmed and replies begin arriving. Response-rate thresholds are numeric and domain-specific.

### B.1 — When to Apply This Rubric

Apply response-rate logic **only after at least 3 sends have been confirmed** across either domain. Minimum data window before applying thresholds:

| Sends Out | Minimum Wait Before Rate Assessment |
|-----------|-------------------------------------|
| 1–2 sends | Wait 5 days (insufficient sample) |
| 3–5 sends | Wait 4 days |
| 6–9 sends | Wait 3 days (meaningful data at Day 3) |

First meaningful rate check: **June 27** (if any sends went out June 24–25).

---

### B.2 — Domain 51 Response Rate Thresholds

Domain 51 has 4 Tier A sends: Campaign Legal Center, Common Cause, End Citizens United, Issue One.

| Rate (by June 30) | Interpretation | Wave 2 Action |
|-------------------|----------------|---------------|
| **< 20%** (0 of 4) | No engagement. Template framing likely off-target for recipients. | Revise templates before Wave 2. Focus revision on: (1) more specific advocacy ask tied to Senate markup timeline, (2) shorter email (reduce from ~480w to ~300w), (3) different subject line framing. Revision time: 1–2 hours. Re-test with 1 contact before full Wave 2 launch. |
| **20–40%** (1 of 4) | Single engagement. Messaging reaches some but not all. | Minor refinement — adapt the language from the reply that worked into all templates. Wave 2 proceeds with refined set. Refinement time: 30–45 min. |
| **40–60%** (2 of 4) | Strong. Multiple organizations engaged. | Proceed with Wave 2 as-is. Templates proven. Expand to Tier B (Arizona, Massachusetts, Montana state ballot campaigns). |
| **> 60%** (3–4 of 4) | Excellent. Near-complete engagement. | Accelerate Wave 2. Add 20+ Tier B contacts immediately. Prioritize Arizona Prop 130 and Massachusetts Fair Elections Act campaigns (closest November ballot measures). |

**Special escalation**: If Campaign Legal Center (Template 1) and Common Cause (Template 2) both fail to respond by **July 10**, escalate to secondary contacts:
- CLC secondary: Sean McElwee (smcelwee@campaignlegalcenter.org)
- Common Cause secondary: Ben Barber (bbarber@commoncause.org)
- Also escalate to: Whitehouse Senate staff + Brennan Center (per Domain 51 distribution-execution-roadmap.md contingency)

---

### B.3 — Domain 48 Response Rate Thresholds

Domain 48 has 5 Tier 1 sends: Sentencing Project, Prison Policy Initiative, ACLU Voting Rights, M4BL Policy Table, Fair Elections Center.

| Rate (by June 30) | Interpretation | Wave 2 Action |
|-------------------|----------------|---------------|
| **< 20%** (0–1 of 5) | No engagement. May indicate off-target framing for criminal justice audience. | Revise templates before Wave 2. Focus revision on: (1) lead with the Virginia November 3 argument (most time-urgent), (2) shorten (reduce from ~490w to ~320w), (3) more specific ask (request 20-min call rather than open-ended feedback). Revision time: 1–2 hours. |
| **20–40%** (1–2 of 5) | Partial engagement. | Minor refinement — adopt the framing from the reply that worked. Wave 2 proceeds with refined templates. |
| **40–60%** (2–3 of 5) | Strong engagement. | Proceed to Wave 2 as-is. Templates proven. Move to Tier 2 (Brennan Center, NAACP LDF, Campaign Legal Center, Worth Rises, ACLU-VA). |
| **> 60%** (3–5 of 5) | Excellent engagement. | Accelerate Wave 2 + Tier 3 (broader coalitions). Launch Wave 2 immediately (July 7–10) with expanded contact list. |

**Hard deadline escalations for Domain 48** (Virginia July 15 absolute):
- **July 7**: If M4BL or Fair Elections Center have not replied, escalate immediately. Contact by phone or web form. Do not wait for email reply.
- **July 10**: If Sentencing Project or PPI have not replied, escalate to secondary contacts (Marc Mauer / Peter Wagner). Include "Virginia July 15 deadline" in subject line of follow-up.
- **July 15**: Virginia ballot measure materials integration deadline. Any engagement secured before this date has full value.

---

### B.4 — Combined Decision Table (Both Domains)

Use this table for the Wave 2 go/no-go decision on June 28.

| Combined Rate (both domains) | Wave 2 Decision | Timeline |
|------------------------------|-----------------|----------|
| **< 20%** | REVISE + RE-TEST | July 1–3 (revise), July 7 (re-test with 2 contacts), July 14 (Wave 2 if re-test succeeds) |
| **20–39%** | REFINE + PROCEED | June 30 (revise), July 1–2 (Wave 2 launch) |
| **40–59%** | PROCEED AS-IS | July 1–2 (Wave 2 launch, current templates) |
| **> 60%** | ACCELERATE | June 29–30 (Wave 2 launch, expanded contacts) |

**Hard NO-GO condition**: If response rate < 10% AND bounce rate > 30% (email addresses invalid), do NOT launch Wave 2. Escalate to user with: "Contact list needs re-verification. More than 30% of Domain 51/48 Tier 1 emails may be invalid. Request user decision on contact list update before Wave 2."

---

## SECTION C: DOMAIN 59 TIER 2 INDEPENDENT ESCALATION

Domain 59 Tier 2 (EPI, Demos, NELP) does NOT depend on Domains 51/48 Wave 1 completion or response rates. However, it has its own escalation thresholds.

| Threshold | Condition | Action |
|-----------|-----------|--------|
| June 25 12:00 UTC | Domain 59 Tier 2 not started | Reminder: "Domain 59 Tier 2 independent — 3 templates ready. Senate Finance CTC markup window open now. Est. time: 20 min." |
| June 28 18:00 UTC | Domain 59 Tier 2 < 2 sends | CAUTION: Only 2 days remaining in window. Send remaining templates today. |
| June 30 18:00 UTC | Domain 59 Tier 2 < 3 sends | WINDOW CLOSING: Senate Finance CTC advocacy window closes. Send any remaining templates immediately or accept reduced advocacy value for missed sends. |

---

## SECTION D: PHASE 2 CASCADE RISK LOGIC

This section summarizes what cascades if thresholds are crossed, so every escalation decision is made with full awareness of downstream impact.

```
Wave 1 execution slip → CASCADE ANALYSIS

Slip to June 25:
  - Domain 51: DISCLOSE Act markup window still open ✓
  - Domain 48: Virginia July 15 still protected (20+ days buffer) ✓
  - Domain 59 Tier 2: Execute independently, no impact ✓
  - Wave 2 timing: Compressed 1 day but manageable ✓
  - Phase 2 momentum: INTACT

Slip to June 26–27:
  - Domain 51: DISCLOSE Act markup window narrowing (Senate vote July 1 possible) ⚠
  - Domain 48: Virginia July 15 still protected (18+ days buffer) ✓
  - Domain 59 Tier 2: Execute independently, no impact ✓
  - Wave 2 timing: Compressed 2–3 days; July 2–3 launch ⚠
  - Phase 2 momentum: REDUCED but intact

Slip to June 28–30 (compressed catch-up):
  - Domain 51: DISCLOSE Act window may close (Senate vote timing uncertain) ⚠
  - Domain 48: Virginia July 15 still intact (15+ days buffer) ✓
  - Domain 59 Tier 2: Execute independently, no impact ✓
  - Wave 2 timing: July 7–10 launch; 14-day response window preserved ✓
  - Phase 2 momentum: DEGRADED for Domain 51; intact for Domain 48

Slip past July 1 (July async path):
  - Domain 51: Senate markup may have concluded without DISCLOSE Act advocacy; reduced value ⚠⚠
  - Domain 48: Virginia July 15 still intact IF sends happen July 1–7 ✓ (tight)
  - Domain 59 Tier 2: Complete; no impact ✓
  - Wave 2 timing: July 14–21; feasible but later ✓
  - Phase 2 momentum: BROKEN for Domain 51, marginal for Domain 48
```

---

*Created: June 24, 2026 | Item 27 deliverable 2 of 4 | Companion documents: DOMAINS_51_48_WAVE1_DAILY_MONITORING_CHECKLIST.md, WAVE1_CATCH_UP_PROCEDURES.md, DOMAINS_51_48_WAVE1_EXECUTION_STATUS_TRACKER.md*
