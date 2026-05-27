---
title: "Synthesis Contingency Routing — May 28 Meta-Router"
created: "2026-05-27"
execution_date: "May 28, 2026 19:15 UTC"
status: "PRODUCTION-READY — read this first at 19:15 UTC after synthesis completes"
scope: "Routes May 28 synthesis outcome to correct playbook and pre-written user communication. One decision: which outcome? Then navigate to the correct playbook."
---

# Synthesis Contingency Routing
## May 28 Meta-Router — Read at 19:15 UTC

This is the first document you open after the synthesis runs at 19:00 UTC. Read your outcome classification. Navigate to the correct playbook. Send the pre-written communication. You have 30 minutes (19:15–19:45 UTC).

**Domain 56 May 28 sends**: Already complete or in progress today. NOT dependent on synthesis outcome. If sends are pending, complete them today — independently of whatever the synthesis shows.

---

## Section 1 — Outcome Classification Reference

The synthesis script (`synthesis-execution-monitor.py`) classifies based on the Quality Reply Points (QRP) formula from `MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md`. The five possible outputs:

### STRONG
- **Condition**: QRP >= 2 (two or more Batch 1 contacts replied at Score 3+), AND substantive response rate >= 40% — OR any single Score 5 signal (published citation, formal collaboration offer)
- **What it means**: The framework reached institutional decision-makers and produced verified engagement. At least two contacts engaged substantively. One Score 5 signal overrides all other conditions regardless of QRP.
- **Phase 2 impact**: All four domains (56, 57, 58, 59) launch on the full parallel schedule. Domain 56 June 1, Domain 39 May 30, Domain 58 ruling-contingent, Domain 57 June 10, Domain 59 June 15.
- **User decision required**: Approve parallel launch vs. staggered (default: parallel). Due May 29 08:00 UTC.
- **Playbook**: `SYNTHESIS_OUTCOME_STRONG_PLAYBOOK.md`

### MODERATE
- **Condition**: QRP = 1 (exactly one Score 3+ reply) — OR Gist delta > 10 with zero direct email replies. QRP must be below 2 (otherwise STRONG).
- **What it means**: Real engagement from one institutional contact or meaningful organic Gist traffic. Framework has credibility. Phase 2 proceeds with focus.
- **Phase 2 impact**: Domain 56 June 1, Domain 39 May 30, Domain 58 ruling-contingent proceed on schedule. Domains 57 and 59 have a June 10 gate before launch dates are confirmed.
- **User decision required**: Any concerns? (default: no, proceed). Due May 29 08:00 UTC.
- **Playbook**: `SYNTHESIS_OUTCOME_MODERATE_PLAYBOOK.md`

### WEAK
- **Condition**: QRP = 0 (no Score 3+ replies from any Batch 1 contact), Gist delta <= 5, AND delivery self-test confirmed inbox (not spam).
- **What it means**: No institutional engagement signals. Cause is unknown — could be timing, messaging, stakeholder, or substance. Root cause diagnosis determines Phase 1 follow-up path.
- **Phase 2 impact**: Domain 56 June 1, Domain 39 May 30, Domain 58 ruling-contingent proceed regardless. Domains 57/59 deferred — June 10 gate determines August or earlier. Phase 1 remediation begins.
- **User decision required**: Option (a) proceed cautiously OR option (b) delay Phase 2 scope to June 1 with May 29–31 additional outreach. Due May 29 noon.
- **Playbook**: `SYNTHESIS_OUTCOME_WEAK_PLAYBOOK.md`

### TOO_EARLY
- **Condition**: Zero replies from all five Batch 1 contacts AND zero or minimal Gist delta AND at least one contact's standard response window is still open (law schools: Day 7 from May 18 send = May 25; if May 28 is the final extension, this gate closes tonight).
- **What it means**: Timing snapshot only. Not a content failure. The window has not yet fully closed for all contacts. May 28 is the absolute final gate — there is no further wait.
- **Phase 2 impact**: NONE until reclassified tonight. Apply QRP formula one final time. Any Score 3+ = MODERATE. Any Score 5 = STRONG. Zero signals + delivery confirmed = WEAK immediately.
- **User decision required**: Tonight — reclassify and re-run router. No wait available past May 28.
- **Action**: Re-run `synthesis-outcome-router.py --outcome WEAK` (or MODERATE/STRONG) after final assessment. Then navigate to the matching playbook.

### DELIVERY_PROBLEM
- **Condition**: Delivery self-test email (sent from your sending account to your own address) landed in spam.
- **What it means**: The delivery pipe failed. Contacts did not receive the emails. This is infrastructure, not content.
- **Phase 2 impact**: Pause ALL Phase 2 sends except Domain 39 (proceed May 30) and Domain 56 (shifts to June 10 after delivery fix).
- **User decision required**: Tonight — choose Fix A (switch sending account), Fix B (reduce spam triggers), or Fix C (check domain reputation). Confirm fix before Domain 39 May 30 sends.
- **Playbook**: Not a separate playbook file — full instructions in `MAY_28_OUTCOME_DECISION_QUICK_REFERENCE.md` DELIVERY_PROBLEM section.

---

## Section 2 — May 28 Routing Decision Tree

```
19:00 UTC — Synthesis runs
↓
19:15 UTC — Read synthesis-execution-output.md
↓
What is the classification?
│
├── STRONG ──────────────→ SYNTHESIS_OUTCOME_STRONG_PLAYBOOK.md
│                          Send Template A email to user
│                          Domain 56 sends: confirm complete
│                          Phase 2: full parallel launch pending user approve
│                          User decision due: May 29 08:00 UTC
│
├── MODERATE ────────────→ SYNTHESIS_OUTCOME_MODERATE_PLAYBOOK.md
│                          Send Template B email to user
│                          Identify signal source from signal log
│                          Domain 56 sends: confirm complete
│                          Phase 2: D56/39/58 on schedule; D57/59 gate June 10
│                          User decision due: May 29 08:00 UTC
│
├── WEAK ────────────────→ SYNTHESIS_OUTCOME_WEAK_PLAYBOOK.md
│                          Send Template C email to user
│                          Run root cause mode diagnosis (Section 1 of WEAK playbook)
│                          Domain 56 sends: confirm complete regardless
│                          Phase 2: D56/39/58 proceed; D57/59 deferred to August gate
│                          User decision due: May 29 noon (option a or b)
│
├── TOO_EARLY ───────────→ Apply QRP formula one final time (May 28 is the absolute final gate)
│                          Any Score 3+ → reclassify MODERATE → send Template B → MODERATE playbook
│                          Any Score 5 → reclassify STRONG → send Template A → STRONG playbook
│                          Zero signals + delivery confirmed → reclassify WEAK → send Template C → WEAK playbook
│                          Re-run: uv run python synthesis-outcome-router.py --outcome [RESULT]
│                          Send Template D email to user with final classification
│
└── DELIVERY_PROBLEM ────→ DO NOT proceed with Phase 2 sends
                           Send Template E email to user
                           Confirm Domain 39 May 30 proceeds (separate from Phase 1 send infrastructure)
                           Choose Fix A/B/C tonight
                           See MAY_28_OUTCOME_DECISION_QUICK_REFERENCE.md DELIVERY_PROBLEM section
```

**Path-independent regardless of all outcomes**:
- Domain 56 May 28 Tier 2 sends: complete today
- Domain 39 May 30 Tier 1 sends: proceed regardless (Georgetown CCF, NHeLP)
- Domain 58 SCOTUSblog monitoring: continues daily

---

## Section 3 — Communication Templates

Five pre-written email templates. Copy, fill sender name, and send. No editing needed beyond the fields marked [FILL].

---

### Template A — STRONG Outcome

**Subject**: [STRONG] May 28 Synthesis — Phase 2 Full Launch Ready. Approve?

---

The May 28 synthesis returned STRONG classification.

QRP: [FILL from synthesis output]
Signal: [FILL — name of contact/org that produced Score 3+ or Score 5]

What this means: Phase 2 is go-live. All four domains (56, 57, 58, 59) can launch on the parallel schedule.

Domain 56 May 28 sends: [FILL — complete / X of 4 complete]

Proposed next steps (no action needed from you unless you want to change something):
- May 30: Domain 39 Tier 1 sends (Georgetown CCF, NHeLP) — proceeds
- June 1: Domain 39 Tier 2 (Brennan Center, IRG); Domain 56 distribution (H.R. 492 advocacy window)
- June 10: Domain 57 research launch
- June 15: Domain 59 research launch (parallel with D57)
- Late June / July 1: Domain 58 (within 5 days of Trump v. Barbara ruling; July 1 fallback)

One question: Do you approve full parallel Phase 2, or would you prefer a staggered launch (Domains 57/59 start June 15 and July 1 instead)?

Default if no response by May 29 08:00 UTC: proceed with full parallel launch.

---

### Template B — MODERATE Outcome

**Subject**: [MODERATE] May 28 Synthesis — Domain 56 send ON SCHEDULE. Phase 2 proceeds. Any concerns?

---

The May 28 synthesis returned MODERATE classification.

QRP: [FILL from synthesis output]
Signal: [FILL — name of contact/org, or "Gist delta > 10"]

What this means: Real engagement from one institutional contact. Phase 2 proceeds with scope focus.

Domain 56 May 28 sends: [FILL — complete / X of 4 complete]

Planned next steps (no action needed unless you have concerns):
- May 30: Domain 39 Tier 1 sends (Georgetown CCF, NHeLP) — proceeds
- June 1: Domain 39 Tier 2 (Brennan Center, IRG); Domain 56 distribution (standalone utility framing + [FILL signal org] as social proof anchor)
- July 1: Domain 58 (ruling-contingent; earlier if ruling drops before then)
- June 10: Assessment gate — confirm Domain 57/59 launch dates (June 15 vs. July 1)

Any concerns before proceeding? If no response by May 29 08:00 UTC, all of the above proceeds.

---

### Template C — WEAK Outcome

**Subject**: [WEAK] May 28 Synthesis — Domain 56 distribution ON SCHEDULE. Phase 2 DECISION REQUIRED by May 29 noon. Recommend option (a).

---

The May 28 synthesis returned WEAK classification.

QRP: 0
Gist delta: [FILL from synthesis output]
Delivery: confirmed inbox (not a delivery problem)
Root cause diagnosis: Mode [FILL 1/2/3/4] — [FILL brief description]

What this means: No institutional engagement signals from Batch 1 contacts. This is not a research failure. The analysis is sound. The cause is [FILL timing / messaging / stakeholder / substance].

Domain 56 May 28 sends: [FILL — complete / X of 4 complete]

Domain 56 June 1 and Domain 39 May 30 proceed regardless — they are not blocked by this outcome.

I need your decision by May 29 noon:

**(a) Proceed May 30 with Phase 2 caution mode**: D56/39/58 on schedule. Domains 57/59 assessed at June 10 gate — if Batch 2 generates signal by then, they launch; if not, August fallback. Phase 1 follow-up begins today per Mode [FILL] diagnosis.

**(b) Delay Phase 2 scope to June 1**: Use May 29–31 for follow-up outreach to top 5 contacts and signal log gap analysis. Domains 57/59 explicitly deferred to August. D56 June 1 and D39 May 30 still proceed.

My recommendation: **(a)**. Domains 56 and 39 proceed regardless. The June 10 gate gives you a decision point before Domains 57/59 commit to any send. Option (a) keeps all options open with the least irreversible commitment.

If no response by May 29 noon: proceed with option (a).

---

### Template D — TOO_EARLY Final Gate

**Subject**: [TOO_EARLY → FINAL GATE] May 28 synthesis complete. Final classification: [FILL STRONG/MODERATE/WEAK]. Domain 56 sends on schedule.

---

The May 28 synthesis ran the final TOO_EARLY gate (May 28 is the absolute last extension window).

Final classification: [FILL — STRONG / MODERATE / WEAK]
QRP: [FILL]
Delivery: [FILL — inbox confirmed / inconclusive]

Domain 56 May 28 sends: [FILL — complete / X of 4 complete]

Based on this final classification, I am routing to the [FILL STRONG / MODERATE / WEAK] playbook. Please see the corresponding subject-line email I am also sending now.

No wait beyond May 28 is available. The classification resolves tonight.

---

### Template E — DELIVERY_PROBLEM

**Subject**: [DELIVERY_PROBLEM] May 28 synthesis — emails may not have reached recipients. Urgent infrastructure fix required.

---

The May 28 synthesis flagged a DELIVERY_PROBLEM: the delivery self-test email from the sending account landed in spam.

This means the May 18 Batch 1 emails may not have reached recipients' inboxes. This is an infrastructure issue, not a content issue. The framework analysis is not affected.

Domain 56 May 28 sends: [FILL status] — NOTE: If sends have not yet gone out, hold them until delivery is fixed.
Domain 39 May 30 sends: Proceed as planned — Domain 39 is a separate send, not blocked.

Required tonight — choose one fix:
- **Fix A** (15 min): Switch to a different sending account. Send test email from new account to your inbox. If inbox: proceed.
- **Fix B** (30 min): Edit templates to reduce spam triggers (remove ALL CAPS, reduce link count, add plain text signature). Resend self-test.
- **Fix C** (60 min): Check domain/IP reputation at MXToolbox.com. Repair and retest.

What I need from you: confirm which fix you want to apply, or tell me the self-test result if you have already run a new test.

Phase 2 sends are paused until inbox delivery is confirmed. Domain 56 distribution shifts from June 1 to June 10 (wait for Batch 1 resend assessment window).

---

## Quick Contacts Reference (verified May 26, 2026)

**Domain 56 May 28 contacts**:
- Volcker Alliance: volcker@volckeralliance.org
- Democracy Forward: info@democracyforward.org
- CREW: citizensforethics.org/contact (form only)
- Government Executive: editors@govexec.com

**Domain 39 May 30 contacts (Tier 1)**:
- Georgetown CCF: childhealth@georgetown.edu (NOT ccf@georgetown.edu)
- NHeLP: info@healthlaw.org

**Domain 39 June 1 contacts (Tier 2)**:
- Brennan Center: kennardl@brennan.law.nyu.edu
- IRG: info@responsivegov.org

**Domain 56 Gist URL**: `https://gist.github.com/esca8peArtist/8f11e868397921a4e6556b41196d1b1f`

---

## Summary Matrix

| Outcome | Root signal | Domain 56 May 28 | Domain 39 May 30 | Phase 2 path | User decision | Playbook |
|---------|------------|-----------------|-----------------|-------------|--------------|---------|
| STRONG | 2+ Score 3+ or Score 5 | Proceeds | Proceeds | All 4 domains, parallel | By May 29 08:00 UTC | STRONG_PLAYBOOK.md |
| MODERATE | 1 Score 3+, or Gist delta > 10 | Proceeds | Proceeds | D56/39/58 on schedule; D57/59 gate June 10 | By May 29 08:00 UTC | MODERATE_PLAYBOOK.md |
| WEAK | 0 Score 3+, Gist delta <= 5, inbox confirmed | Proceeds | Proceeds | D56/39/58 proceed; D57/59 August | By May 29 noon (a vs. b) | WEAK_PLAYBOOK.md |
| TOO_EARLY | Zero replies, windows still open | Proceeds | Proceeds | Reclassify tonight → matching playbook | Tonight | Reclassify first |
| DELIVERY_PROBLEM | Self-test in spam | Hold if not sent | Proceeds | Pause all Phase 1 sends; fix delivery first | Tonight (Fix A/B/C) | Quick Reference |

---

*Pre-staged: May 27, 2026. Read at: May 28 19:15 UTC, immediately after synthesis completes.*
*Playbook files: SYNTHESIS_OUTCOME_STRONG_PLAYBOOK.md, SYNTHESIS_OUTCOME_MODERATE_PLAYBOOK.md, SYNTHESIS_OUTCOME_WEAK_PLAYBOOK.md*
*Full decision branches: SYNTHESIS_OUTCOME_DECISION_TREE.md*
*Delivery problem details: MAY_28_OUTCOME_DECISION_QUICK_REFERENCE.md*
