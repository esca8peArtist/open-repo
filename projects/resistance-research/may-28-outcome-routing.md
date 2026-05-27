---
title: "May 28 Outcome Routing — Decision Tree"
created: "2026-05-27"
execution_time: "19:15 UTC May 28, 2026 (immediately after synthesis)"
status: "PRODUCTION-READY"
authority: "SYNTHESIS_OUTCOME_DECISION_TREE.md (full sub-paths); post-synthesis-contingency-execution-playbooks.md (full playbooks)"
companion_files:
  - synthesis-execution-monitor-checkpoint.md
  - user-notification-templates.md
  - SYNTHESIS_OUTCOME_ACTIVATION_CHECKLIST.md
  - contingency-activation-status.md (generated at runtime)
---

# May 28 Outcome Routing — Decision Tree

**How to use**: After synthesis runs at 19:00 UTC, identify your classification from the terminal output. Navigate to the matching IF block below. Execute every THEN item that applies. Each item is a concrete action, file to open, or command to run — not a description of what to think about.

All five outcomes are covered. TOO_EARLY has a forced resolution rule on May 28 — it cannot extend further.

---

## IF OUTCOME = STRONG

**Condition**: QRP >= 2 with response rate >= 40%, OR any contact scored Score 5 (published citation, formal collaboration offer, brief integration request).

**THEN — Tonight (May 28, 19:15–21:00 UTC)**:

1. Identify the highest-scoring contact from the signal log. Record: name, organization, reply content summary. This becomes the social proof anchor for all June 1 emails.

2. Update Domain 56 June 1 email templates before bed tonight. Open `projects/resistance-research/execution/domain-56-email-template.md`. In every template, add to the opening paragraph: "Following substantive engagement from [ORGANIZATION] on the democratic-design framework..." — insert the contact's organization name. This update must happen before June 1.

3. Confirm Domain 39 May 30 sends are staged:
   - Georgetown CCF: childhealth@georgetown.edu (verified active — NOT ccf@georgetown.edu)
   - NHeLP: info@healthlaw.org
   These send regardless of outcome. STRONG means they go with full momentum framing.

4. Confirm Domain 58 Gist creation is in queue. Trump v. Barbara ruling has no date but expected late June / early July. Pre-ruling distribution to tribal law contacts begins June 15. This is path-independent but STRONG activates it earliest.

5. Update CHECKIN.md using the STRONG template in `user-notification-templates.md`.

6. Commit CHECKIN.md to master.

**THEN — Phase 2 Domain Sequencing (STRONG path)**:

| Date | Action | File |
|------|--------|------|
| May 28 (tonight) | Domain 56 templates updated with social proof | execution/domain-56-email-template.md |
| May 30 | Domain 39 Tier 1 sends (Georgetown CCF, NHeLP) | DOMAIN_39_DISTRIBUTION_STRATEGY.md |
| June 1 | Domain 39 Tier 2 (Brennan Center, IRG); Domain 56 4 sends | DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md |
| June 2-3 | Domain 39 Tier 3 (Black Mamas Matter) | DOMAIN_39_DISTRIBUTION_STRATEGY.md |
| June 10 | Domain 57 research launch | DOMAINS_57_59_PRODUCTION_ROADMAP.md |
| June 15 | Domain 59 research launch (parallel with 57); Tier 2 activation | post-synthesis-contingency-execution-playbooks.md |
| June 15 | Domain 58 pre-ruling tribal law distribution | DOMAIN_58_DISTRIBUTION_BRIDGE.md |
| August 1 | Domain 59 distribution target | — |
| August 10 | Domain 57 distribution target | — |

**Next user decision gate**: June 10 (Domain 57 research status check — confirm on-track or flag blockers).

**Risk flags to monitor**:
- Domain 59 OBBBA data dependency: HHS June 1 interim final rule. If rule delayed, Section 2 of Domain 59 uses preliminary CRS projections as fallback.
- Protected writing blocks required: Flag weeks of June 15 and July 6-20 in calendar now.

---

## IF OUTCOME = MODERATE

**Condition**: QRP >= 1 from at least one Score 3+ reply, OR Gist delta > 10 with zero direct replies. At least one institutional contact confirmed engagement.

**THEN — Tonight (May 28, 19:15–21:00 UTC)**:

1. Identify the single MODERATE-signaling contact (highest score in signal log). This is the social proof anchor.

2. Update Domain 56 June 1 templates with that organization's name — same procedure as STRONG. Social proof from one organization is still social proof. If Gist-only signal (no direct reply), use: "Following significant research engagement from the academic and legal communities..." (no named organization needed).

3. Confirm Domain 39 May 30 sends are staged (same contacts as STRONG — path-independent).

4. Add a June 10 assessment gate to your calendar. At June 10, Batch 2 response data will determine whether Domains 57 and 59 launch immediately or defer to August. This is the only pending user decision before June 10.

5. Update CHECKIN.md using the MODERATE template in `user-notification-templates.md`.

6. Commit CHECKIN.md to master.

**THEN — Phase 2 Domain Sequencing (MODERATE path)**:

| Date | Action | Note |
|------|--------|------|
| May 30 | Domain 39 Tier 1 sends | Path-independent |
| June 1 | Domain 56 4 sends with social proof framing | Use identified org as anchor |
| June 1 | Domain 39 Tier 2 sends | Path-independent |
| June 2-3 | Domain 39 Tier 3 send | Path-independent |
| June 10 | Assessment gate: launch Domains 57 + 59 OR defer to August | Requires Batch 2 data |
| July 1 | Domain 58 distribution (Trump v. Barbara ruling-contingent) | Monitoring begins June 15 |
| August 10 (if deferred) | Domain 57 distribution | Post-gate decision |
| August 1 (if deferred) | Domain 59 distribution | Post-gate decision |

**At the June 10 gate**: IF Batch 2 has produced 2+ Score 3+ replies, THEN launch Domain 57 research on the MODERATE timeline (June 10 start, Aug 10 completion) and Domain 59 (July 1 start, Aug 1 completion). IF Batch 2 is still at zero Score 3+ replies, THEN defer both to August and proceed with WEAK path remediation for Phase 1.

**Next user decision gate**: June 10. No decision required before then.

---

## IF OUTCOME = WEAK

**Condition**: QRP = 0 (zero Score 3+ replies), Gist delta <= 5, and delivery self-test confirmed inbox placement (not spam).

**THEN — Step 1 (before anything else): select root cause mode**

The router will suggest a mode from the four below. Confirm or override:

- **Mode 1 — Messaging**: 4-5 contacts replied at Score 1-2 but no Gist depth. Interpretation: contacts read the subject line but the value proposition did not land. Path: Domain 37 targeted amplification (B path — lead with a single high-relevance domain, not the full framework).
- **Mode 2 — Timing**: 1-2 late replies arrived; Gist delta 3-5. Interpretation: window was not fully closed at synthesis time. Path: Batch 2 expansion on standard schedule (A path — extend the wave rather than pivot).
- **Mode 3 — Stakeholder**: 2+ bounces or verified undeliverable addresses. Interpretation: contact quality issue, not message quality. Path: Batch 2 with contact re-verification (A path with contact swap).
- **Mode 4 — Substance**: 0-1 replies; Gist delta 0-1; delivery confirmed. Interpretation: message never prompted action — either framing is wrong or contacts have changed context. Path: narrative bridge documents before next wave (C path).

Record selected mode in CHECKIN.md before doing anything else with email or templates.

**THEN — Tonight (May 28, 19:15–21:00 UTC)**:

1. Log mode selection in CHECKIN.md.
2. Confirm Domain 56 June 1 distribution proceeds as planned — use framework utility framing (no social proof available). The democratic-design argument stands independently.
3. Confirm Domain 39 May 30 sends proceed — these are path-independent and have an external deadline (June 1 HHS interim Medicaid rule).
4. Do not revise any email templates tonight. The mode diagnosis determines what to revise; acting before the diagnosis risks doubling down on the wrong problem.
5. Update CHECKIN.md using WEAK template in `user-notification-templates.md`.
6. Commit CHECKIN.md to master.

**THEN — Phase 2 Domain Sequencing (WEAK path)**:

| Date | Action | Note |
|------|--------|------|
| May 30 | Domain 39 Tier 1 sends | Path-independent; proceeds regardless |
| June 1 | Domain 56 4 sends — framework utility framing | No social proof; standalone argument |
| June 1 | Domain 39 Tier 2 sends | Path-independent |
| June 3-7 | Phase 1 follow-up per selected mode (A / B / C) | See post-synthesis-contingency-execution-playbooks.md WEAK section |
| June 10 | Assessment gate: if Batch 2 produced 2+ Score 3+ → uplift to MODERATE timeline for 57/59 | Key recovery trigger |
| July 1 | Domain 58 distribution OR within 5 days of Trump v. Barbara ruling | Proceeds regardless of Phase 1 |
| August 1 | Domain 59 research launch (deferred from June) | Post-gate decision |
| August 10 | Domain 57 research launch (deferred from June) | Post-gate decision |

**Reframing note**: Phase 1 was validation scope-check, not proof-of-concept. Domains 39, 56, and 58 have independent external deadlines (June 1 HHS, June 1-30 H.R. 492 markup window, Trump v. Barbara ruling) that generate distribution events regardless of Phase 1 engagement amplitude. WEAK Phase 1 is a signal to diagnose and adjust — it is not a project failure.

**Next user decision gate**: June 5 (Batch 3 activation gate — requires Batch 2 response data). No decision required before June 5 unless you want to override the mode diagnosis tonight.

---

## IF OUTCOME = TOO_EARLY

**Final gate rule**: May 28 is Day 10. TOO_EARLY cannot extend past tonight. This outcome has one and only one resolution path.

**THEN — Apply the QRP formula one final time (manually, now)**:

Open the signal log and the inbox simultaneously. Check every logged contact:
- Any contact with Score 3+ → QRP contribution of 1.0. If total QRP >= 1 → reclassify MODERATE. Navigate to MODERATE section above.
- Any contact with Score 5 (published citation, formal collaboration) → reclassify STRONG immediately. Navigate to STRONG section above.
- Zero contacts at Score 3+ AND confirmed inbox delivery → reclassify WEAK immediately. Navigate to WEAK section above.

**Command to force reclassification**:

```bash
cd /home/awank/dev/SuperClaude_Framework
uv run python projects/resistance-research/synthesis-outcome-router.py --outcome WEAK
```

Replace WEAK with MODERATE or STRONG if the manual check found qualifying signals.

There is no further wait. The synthesis produces a definitive outcome tonight regardless. All autonomous preparation work (Domain 56 templates, Domain 39 Gist, Domain 58 contact verification) completed during the TOO_EARLY window is still valid — none of it is wasted by reclassifying tonight.

---

## IF OUTCOME = DELIVERY_PROBLEM

**Condition**: Delivery self-test email (sent from your sending account to your own inbox) landed in spam folder.

**THEN — Verify it is not a false positive (do this first, before any other action)**:

1. Check your spam folder again in a fresh browser session.
2. If the test email is now in inbox: this was a temporary spam filter issue. Reclassify as TOO_EARLY (if no other signals) or WEAK (if the filter was present during the May 18 sends). Use `--outcome TOO_EARLY` or `--outcome WEAK` accordingly.
3. If confirmed spam: proceed.

**THEN — Select a fix (pick exactly one)**:

- **Fix A — Switch sending account (15 minutes)**: Send the May 28 synthesis test from a different email account (organizational address, or a clean Gmail not used for bulk outreach). If inbox delivery confirmed from the alternate account, use it for all remaining sends. This is the fastest recovery path.
- **Fix B — Revise email templates (30 minutes)**: Remove all-caps words, reduce link count to one per email, add plain text signature. Resend test from original account. If inbox: templates were the trigger.
- **Fix C — Investigate domain/IP reputation (60 minutes)**: Check MXToolbox.com and Google Postmaster Tools for the sending domain. If flagged: warm-up service or domain switch required. This is the longest path and should only be chosen if Fix A and Fix B both fail.

**THEN — Pauses and exemptions**:

- PAUSE: All batch outreach sends (Batch 1 resends, Batch 2, Domain 56 June 1)
- NOT PAUSED: Domain 39 May 30 sends — these can use the alternate account identified in Fix A and should not be delayed given the June 1 HHS deadline
- NOT PAUSED: Domain 58 preparation — this is research and Gist creation, not outbound email

**THEN — Timeline adjustments**:

| What | Original date | Adjusted date |
|------|--------------|---------------|
| Batch 1 resend | — | May 30 from fixed account |
| Domain 56 sends | June 1 | June 10 (after resend response window) |
| Domain 39 sends | May 30 | May 30 — proceeds from alternate account (unchanged) |
| Reclassification | Tonight | June 6 (7-day window from May 30 resend) |
| Domain 57/59 decision | June 10 | June 15 (shifted by reclassification delay) |

**Next user decision gate**: Tomorrow (May 29) — confirm fix worked by verifying test email landed in inbox. If inbox confirmed: proceed with May 30 Batch 1 resend as scheduled.

---

## Cross-Outcome Rules (Apply to All Outcomes)

**Domain 39 sends are path-independent**: May 30 Tier 1 and June 1 Tier 2 sends happen regardless of synthesis outcome. The only exception is DELIVERY_PROBLEM, where they shift to the fixed sending account. Contacts: Georgetown CCF (childhealth@georgetown.edu), NHeLP (info@healthlaw.org), Brennan Center (kennardl@brennan.law.nyu.edu), IRG (info@responsivegov.org).

**Trump v. Barbara is a hard trigger**: Domain 58 rapid-response distribution activates within 5 days of the ruling regardless of Phase 1 or Phase 2 synthesis outcome. Begin daily SCOTUSblog monitoring at https://www.scotusblog.com/cases/trump-v-barbara/ starting June 15.

**CHECKIN.md must be updated tonight**: Use pre-written templates in `user-notification-templates.md`. Copy the matching outcome block, fill all [BRACKET] fields from signal log and script output, paste into CHECKIN.md, commit before 23:59 UTC.

---

*Created: May 27, 2026. For full sub-path decision branches, see SYNTHESIS_OUTCOME_DECISION_TREE.md. For full playbooks with day-by-day action plans, see post-synthesis-contingency-execution-playbooks.md.*
