---
title: "Synthesis Outcome — MODERATE Playbook"
created: "2026-05-27"
execution_date: "May 28, 2026 19:15 UTC"
status: "PRE-STAGED — activate only if synthesis returns MODERATE classification"
condition: "QRP >= 1 (exactly 1 Score 3+ reply), OR Gist delta > 10 with zero direct email replies. QRP < 2 and response rate < 40%."
authority: "SYNTHESIS_CONTINGENCY_ROUTING.md (meta-router), SYNTHESIS_OUTCOME_DECISION_TREE.md (full branches)"
---

# SYNTHESIS OUTCOME: MODERATE — Execution Playbook

**Activate this document**: May 28 19:15 UTC, only if synthesis returns MODERATE classification.
**Window**: 19:15–19:45 UTC (30 minutes to route and confirm).
**Domain 56 status**: Already sent or in-progress today — NOT blocked by this outcome. Proceeds as planned.

---

## Section 1 — Outcome Summary

MODERATE means engagement is real but lighter than the STRONG threshold. One Batch 1 contact replied at Score 3 or higher — a substantive response, an internal forward, a follow-up question — but not two. Alternatively, the Gist accumulated more than 10 view-count increases since the May 18 send with zero direct email replies, indicating the document is circulating without converting to direct contact yet.

What this looks like in practice: one think tank or law school contact wrote back with specific domain engagement; or the Gist shows meaningful organic traffic but the inbox is quiet. The argument has credibility with at least one institutional decision-maker. Phase 2 is not blocked. Phase 2 proceeds with scope focus: Domains 56 and 58 launch on schedule; Domains 57 and 59 have a June 10 assessment gate before their launch dates are confirmed.

MODERATE is a workable outcome. The framework has been validated by one institutional contact. That is a credibility anchor for Batch 2 sends, a social proof signal for June 1 Domain 56 emails, and evidence that the argument lands when it reaches the right reader. The strategic adjustment is precision of scope, not retreat.

---

## Section 2 — Immediate Actions (May 28 19:15–19:30)

**Step 1**: Confirm the classification is MODERATE.

Check: `projects/resistance-research/synthesis-execution-output.md` — classification field should read MODERATE. QRP should be exactly 1, or Gist delta should be above 10 with QRP = 0. If classification is borderline (Gist delta is 9–11 with zero replies), accept MODERATE rather than downgrading to WEAK — the routing logic is designed to be conservative at the lower boundary.

**Step 2**: Identify the signal source.

Open the signal log at `post-wave-1-monitoring/wave-1-signal-log-may18-21.md`. Find the contact who produced the Score 3+ reply (or, if Gist-delta-only, note that). Record:
- Contact name and organization:
- Reply score and what they said (brief summary):
- This person/organization is your social proof anchor for Batch 2 sends and Domain 56 June 1 templates.

**Step 3**: Send user notification email (template in SYNTHESIS_CONTINGENCY_ROUTING.md Section 3, Template B).

Subject: `[MODERATE] May 28 Synthesis — Domain 56 send ON SCHEDULE. Phase 2 proceeds. Any concerns?`

The email asks one question: any concerns before proceeding? Default answer is NO, proceed. If no response from user by May 29 08:00 UTC, proceed with MODERATE path as written.

**Step 4**: Log the outcome.

Update CHECKIN.md:
```
## May 28 Synthesis — MODERATE
- Classification: MODERATE
- QRP: [number]
- Signal source: [contact/org that produced Score 3+ or Gist delta > 10]
- Domain 56 sends: [complete / in progress]
- Phase 2 routing: MODERATE path — D56 June 1, D58 July 1, D57/59 gate June 10
- Next gate: June 10 (D57/59 activation decision)
```

---

## Section 3 — Domain 56 Tier 1 Distribution Confirmation (May 28 19:30–20:00)

Domain 56 Tier 2 sends were scheduled for May 28 independent of synthesis outcome. Confirm their status now.

**Verify all 4 sends are logged in DISTRIBUTION_EXECUTION_LOG.md**:
- [ ] Send 1: Volcker Alliance (volcker@volckeralliance.org) — logged with timestamp
- [ ] Send 2: Democracy Forward (info@democracyforward.org) — logged with timestamp
- [ ] Send 3: CREW (citizensforethics.org/contact) — form submission confirmed
- [ ] Send 4: Government Executive (editors@govexec.com) — logged with timestamp

**If all 4 are sent**: Domain 56 May 28 workstream is complete. Note in distribution-log.md: "MODERATE synthesis outcome confirmed. Domain 56 May 28 sends complete. June 1 advocacy window on schedule."

**If 1–3 sends are complete**: Complete remaining sends before end of day. MODERATE outcome does not affect the send order — proceed as scheduled.

**If 0 sends are complete**: Execute sends immediately per `DOMAIN_56_TIER_2_DISTRIBUTION_MAY28_CHECKLIST.md`. Do not hold sends for Phase 2 routing — they are independent.

**June 1 template update (required for MODERATE path)**:

Before the June 1 Domain 56 sends, update email templates to insert the MODERATE social proof signal. In each template's opening paragraph, replace the generic introduction with: "Following substantive engagement from [Organization from signal log]..." — this is the one concrete social proof anchor the MODERATE outcome provides. It is not as broad as STRONG social proof, but it is a real institutional reference. Use it precisely in the June 1 templates.

---

## Section 4 — Phase 2 Contingency (May 29–June 10)

Under MODERATE, Phase 2 proceeds with domain focus rather than full parallel launch.

**Domains proceeding on schedule (no gate needed)**:
- Domain 56: June 1 distribution — proceeds regardless (H.R. 492 advocacy window is external)
- Domain 39: May 30 Tier 1 sends (Georgetown CCF at childhealth@georgetown.edu, NHeLP at info@healthlaw.org) — proceeds regardless
- Domain 58: Ruling-contingent; Gist + templates complete; distribution within 5 days of Trump v. Barbara ruling or July 1 fallback

**Domains with June 10 gate**:
- Domain 57 (Multilateral Withdrawal): Research launch remains June 10 under MODERATE. At June 10, confirm research is on track; confirm August 10 distribution target. Under MODERATE, Domain 57's outreach framing uses the constitutional asymmetry argument rather than social proof momentum ("this analysis documents how US withdrawal posture differs structurally from all other OECD members — a gap in the comparative law literature"). The MODERATE signal is not broad enough to anchor cold outreach to international law faculty with institutional momentum framing.
- Domain 59 (Economic Precarity): Under MODERATE, deferred to July 1 research launch (vs. June 15 under STRONG). The June 10 gate confirms this: if Batch 2 has produced 2+ additional Score 3+ replies by June 10, advance to June 15. If Batch 2 reply rate is still building, hold to July 1. Default is July 1.

**May 30 manual signal review** (orchestrator task):

Run a quick signal check on May 30: has any additional Batch 2 contact replied at Score 3+? If yes, log it. By June 10, the combined Batch 1 + Batch 2 signal profile will determine whether Domains 57 and 59 launch on the June 15 (near-STRONG) or July 1 (MODERATE) schedule.

---

## Section 5 — User Decision Window

User has a 24-hour window (May 28 19:15 UTC through May 29 19:15 UTC) to request any adjustment.

**Default decision** (no response required):
- Domain 56 June 1 distribution proceeds
- Domain 39 May 30 sends proceed
- Domain 57 research launch June 10 proceeds
- Domain 59 research launch July 1 (default; may advance to June 15 at June 10 gate if Batch 2 signals are strong)

**User can request**:
- Advance Domain 59 to June 15 now (if they believe MODERATE underestimates engagement)
- Delay Domain 57 beyond June 10 (if capacity is constrained)
- Add the MODERATE-signal organization to the Domain 56 June 1 template social proof reference (confirm which contact to name)

**If no response by May 29 19:15 UTC**: Proceed with all defaults. Post confirmation in CHECKIN.md: "MODERATE path defaults confirmed. Proceeding to Phase 2 MODERATE schedule."

**Next user decision required**: June 10 — Domain 57 research status check; Domain 57/59 launch date confirmation (June 15 vs. July 1). No action needed before June 10.

---

*Pre-staged: May 27, 2026. Activate: May 28 19:15 UTC if synthesis returns MODERATE.*
*Do not activate if synthesis returns STRONG, WEAK, TOO_EARLY, or DELIVERY_PROBLEM.*
*Meta-router: SYNTHESIS_CONTINGENCY_ROUTING.md*
