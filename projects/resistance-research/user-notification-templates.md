---
title: "User Notification Templates — May 28 Synthesis Result"
created: "2026-05-27"
purpose: "Copy-paste notification messages for each synthesis outcome. Zero drafting at synthesis time."
scope: "Slack/Discord messages + CHECKIN.md entries for all 5 outcomes"
status: "PRODUCTION-READY"
companion_files:
  - may-28-outcome-routing.md
  - synthesis-execution-monitor-checkpoint.md
  - SYNTHESIS_OUTCOME_NOTIFICATION_TEMPLATES.md (full CHECKIN.md blocks)
---

# User Notification Templates — May 28 Synthesis

**How to use**: After synthesis runs at 19:15 UTC and the router completes, find the section matching your outcome below. Fill all fields marked in [BRACKETS] — sources for each field are listed. Copy the Slack/Discord block and paste it into your channel immediately. Copy the CHECKIN.md block into CHECKIN.md and commit. Total time: under 5 minutes.

For full CHECKIN.md blocks with complete Phase 2 schedules, see `SYNTHESIS_OUTCOME_NOTIFICATION_TEMPLATES.md` (existing file). The templates below are condensed for speed — use them when you want the result communicated immediately without assembling a long document.

---

## Field Reference (fill these before copying any template)

| Field | Where to find it |
|-------|-----------------|
| [TIME] | Current UTC time when you are posting |
| [QRP] | Terminal output from synthesis-execution-monitor.py — "Quality Reply Points:" row |
| [CONTACT] | Signal log — contact row with highest score |
| [ORG] | Signal log — organization column for [CONTACT] |
| [SCORE] | Signal log — score column for [CONTACT] |
| [REPLY_SUMMARY] | Signal log — key_content column for [CONTACT], or one sentence from memory |
| [GIST_DELTA] | Signal log — Gist views column, May 18–28 delta total |
| [REPLIES_COUNT] | Count of contacts with Score 3+ in signal log |
| [MODE] | Your mode selection: Mode 1 / 2 / 3 / 4 (WEAK outcome only) |
| [PATH] | Remediation path: A / B / C (WEAK outcome only) |

---

## STRONG Outcome

**Slack/Discord — STRONG**

```
SYNTHESIS COMPLETE — STRONG

[REPLIES_COUNT]/5 contacts at Score 3+. [QRP] QRP. [GIST_DELTA] Gist views (May 18–28).
Top signal: [CONTACT] at [ORG] — Score [SCORE] — "[REPLY_SUMMARY]"

Phase 2 launching in parallel:
- Domain 56: June 1 (4 sends, social proof framing — [ORG] named)
- Domain 39: May 30 Tier 1 + June 1 Tier 2 + June 2-3 Tier 3
- Domain 57 + 59: June 10/15 research sprint
- Domain 58: June 15 pre-ruling dist. + immediate after Trump v. Barbara

No user decisions needed until June 10.
Posted: [TIME] UTC
```

**Recommended next action to include in message**: "Domain 56 template update needed tonight — inserting [ORG] as social proof anchor before June 1 send."

---

## MODERATE Outcome

**Slack/Discord — MODERATE**

```
SYNTHESIS COMPLETE — MODERATE

[ORG] produced Score [SCORE] signal. [QRP] QRP total. [GIST_DELTA] Gist views.

Proceeding:
- Domain 56: June 1 with [ORG] social proof framing
- Domain 39: May 30 Tier 1 + June 1 Tier 2 (path-independent)
- Domain 58 prep: begins now (ruling-contingent distribution)
- Domains 57 + 59: June 10 assessment gate (launch or defer to Aug)

Next decision: June 10 (Batch 2 data in, launch 57/59 or hold).
Posted: [TIME] UTC
```

**Recommended next action**: "Updating Domain 56 templates now with [ORG] as social proof anchor."

---

## WEAK Outcome

**Slack/Discord — WEAK**

```
SYNTHESIS COMPLETE — WEAK

[QRP] QRP. Zero Score 3+ replies. [GIST_DELTA] Gist views (May 18–28).
Root cause: [MODE] — [one sentence rationale]
Remediation: Path [PATH]

Still executing:
- Domain 56: June 1 (framework framing — no social proof)
- Domain 39: May 30 + June 1 (path-independent)
- Domain 58: July 1 + Trump v. Barbara hard trigger
- Domains 57/59: deferred to August

No content revisions until mode confirmed.
Next gate: June 5 (Batch 3 decision).
Posted: [TIME] UTC
```

**Recommended next action**: "Mode confirmed as [MODE]. No template edits tonight — diagnosis first."

---

## TOO_EARLY Outcome (forced resolution)

**Slack/Discord — TOO_EARLY resolved**

```
SYNTHESIS — TOO_EARLY FINAL GATE

Day 10. Final inbox check complete.
[DESCRIBE RESULT: "Zero replies confirmed" OR "Score [X] reply from [CONTACT] found — reclassifying to [OUTCOME]"]

[IF RECLASSIFYING]: Rerunning router now with --outcome [OUTCOME]. Navigate to [OUTCOME] section.

[IF CONFIRMING WEAK]: Reclassifying WEAK. Zero signals, delivery confirmed.
All autonomous prep continues. Phase 1 closes.
Posted: [TIME] UTC
```

**Note**: If you are reclassifying, post a second notification after the router reruns, using the STRONG, MODERATE, or WEAK template above.

---

## DELIVERY_PROBLEM Outcome

**Slack/Discord — DELIVERY_PROBLEM**

```
SYNTHESIS — DELIVERY_PROBLEM

Test email confirmed in spam folder.
Root cause: [one sentence — e.g., "Gmail free account triggering commercial filter"]
Fix selected: [Fix A / Fix B / Fix C]

All batch sends PAUSED.
Domain 39 May 30 sends EXEMPT — proceeding from alternate account.
Domain 56: shifts June 1 → June 10.
Batch 1 resend: May 30 from fixed account.
Reclassification: June 6 (7 days post-resend).

Implementing fix now.
Posted: [TIME] UTC
```

**Recommended next action**: "Sending test email from alternate account now to verify Fix A works."

---

## CHECKIN.md Header Block (use for all outcomes)

Add this as the header in CHECKIN.md before pasting the full block from `SYNTHESIS_OUTCOME_NOTIFICATION_TEMPLATES.md`:

```
## May 28 Synthesis Complete — [OUTCOME]
*Posted: [TIME] UTC, May 28, 2026*
*Synthesis executed: synthesis-execution-monitor.py + synthesis-outcome-router.py*
*Authority: contingency-activation-status.md (immediate actions) + may-28-outcome-routing.md (decision tree)*
```

---

*Created: May 27, 2026. For full CHECKIN.md blocks with complete Phase 2 schedules, see SYNTHESIS_OUTCOME_NOTIFICATION_TEMPLATES.md. These templates are condensed for immediate speed-of-notification use.*
