---
title: "Phase 1 Rapid-Response Decision Trees — Day 7, Follow-Up Dispatch, Week 2"
created: 2026-05-31
version: 1.0
status: production-ready
scope: >
  Three standalone 1-page decision trees for Day 7–14 rapid-response execution.
  Timestamp-keyed. All branches terminate in a named action — no judgment required.
companion_files:
  - PHASE_1_RAPID_RESPONSE_OPERATIONAL_GUIDE.md
  - PHASE_1_RAPID_RESPONSE_SHEETS_TEMPLATES.md
  - PHASE_1_RAPID_RESPONSE_COMMAND_CARD.md
  - day-7-14-30-decision-trees.md
---

# Phase 1 Rapid-Response Decision Trees

**Version 1.0 — May 31, 2026**

Three trees. One per decision point. Each terminates in a named action with a named next step.
Use the Quick-Reference Command Card (PHASE_1_RAPID_RESPONSE_COMMAND_CARD.md) to pull the input metrics before running these trees.

---

## Decision Tree 1: Day 7 Gate

**Timestamp**: June 8, 2026, 08:00 UTC
**Input data required**: Pull from Sector_Engagement tab (Template A) + Contacts tab + Gist_Views tab
**Time to run**: 5 minutes after data is pulled

```
START: Open Sector_Engagement tab. Read Column H (Signal_Band) for all 6 sectors.
       Read Contacts tab Summary Block: Overall reply rate.
       Read Gist_Views tab: Cumulative_Clicks (Column J, most recent row).

Collect three values:
  (A) Cumulative Bitly clicks to date
  (B) Overall reply rate (any reply / delivered)
  (C) Count of sectors showing "WEAK" or "DEFINITE WEAK" or "PROBABLE WEAK" in Column H

──────────────────────────────────────────────────────────────────────────────

GATE 0: DELIVERY CHECK (run before any signal analysis)
│
├── Bounced count >= 3?
│   (Check Contacts tab: COUNTIF(I:I,"Bounced"))
│
│   YES → DETERMINATION: CONTACT_VERIFY
│         Immediate action: Pull Contacts tab, filter Delivery_Status = "Bounced"
│         Correct email addresses (verify on each org's website)
│         Resend to corrected list within 24 hours
│         Restart Day 7 clock (new Day 7 = resend date + 7 days)
│         Log in CHECKIN.md: "Contact verification re-send — [date]"
│         DONE — do not proceed to Gate 1 today
│
│   NO → Proceed to Gate 1

──────────────────────────────────────────────────────────────────────────────

GATE 1: CLICK VOLUME
│
├── (A) Cumulative clicks < 5?
│
│   YES → DETERMINATION: PAUSE
│         This indicates a delivery or link failure, not engagement failure.
│
│         Diagnostic sequence (complete in order, stop when cause found):
│         1. Click bit.ly/drp-d39 in incognito browser → does the Gist load?
│            NO → Link is broken. Create new Bitly link. Resend to all contacts.
│            YES → Link is working. Continue to step 2.
│         2. Forward the June 1 sent email to a personal test address.
│            Does it arrive in spam?
│            YES → Deliverability problem. Contact 2-3 Tier 1 contacts via
│                  LinkedIn or contact form to confirm receipt.
│            NO → Continue to step 3.
│         3. Open Gmail Sent folder. Are all June 1 emails present?
│            NO → Some emails were not sent. Identify which and resend.
│            YES → Delivery confirmed but zero engagement. Apply Playbook C.
│
│         Log in CHECKIN.md: "Day 7 PAUSE — diagnostic in progress — [date]"
│         DONE — reassess after diagnostic within 24 hours
│
│   NO → Proceed to Gate 2

──────────────────────────────────────────────────────────────────────────────

GATE 2: ENGAGEMENT RATE
│
├── (B) Overall reply rate >= 30%?
│
│   YES → Proceed to Gate 3 (STRONG candidate)
│
│   NO → (B) Overall reply rate 15-29%?
│
│        YES → Proceed to Gate 3 (MODERATE candidate)
│
│        NO → (B) Overall reply rate < 15%?
│             (C) WEAK sector count >= 4?
│
│             BOTH YES → DETERMINATION: REBASE
│                        Apply Section 4 Playbook C immediately.
│                        Dispatch all six sector follow-up templates within 6 hours.
│                        Log in CHECKIN.md: "Day 7 REBASE — [date]"
│                        Next decision point: Day 9 review (June 10)
│
│             ONE OR NEITHER → DETERMINATION: HOLD with weak-sector follow-up
│                              Proceed to Gate 3 for the HOLD/ESCALATE decision.
│                              Dispatch follow-up templates for WEAK sectors only.

──────────────────────────────────────────────────────────────────────────────

GATE 3: SIGNAL QUALITY
│
├── Any Score 5 (Implementation Signal) received?
│   (Check Replies tab: COUNTIF(F:F,">=5") > 0)
│
│   YES → DETERMINATION: ESCALATE — PHASE 2 PRE-ACTIVATION
│         Action: Apply Playbook A immediately.
│         Extract social proof quote from Score 5 reply.
│         Prepare Tier 2 Domain 39 contact list.
│         Log in CHECKIN.md: "Day 7 ESCALATE — Score 5 from [Org] — [date]"
│         DONE
│
│   NO → Continue
│
├── Any Score 4 (Partnership Request) received?
│   (Check Replies tab: COUNTIF(F:F,"=4") > 0)
│
│   YES → DETERMINATION: ESCALATE — PHASE 2 PRE-ACTIVATION (lighter weight)
│         Action: Apply Playbook A, Steps 1-4.
│         Log partnership request in Adoptions tab as "Probable" signal.
│         Respond to Score 4 contact within 24 hours.
│         If 2+ Score 4 replies: activate full Phase 2 pre-activation immediately.
│         Log in CHECKIN.md: "Day 7 ESCALATE — Score 4 from [Org] — [date]"
│         DONE
│
│   NO → Continue
│
├── Overall reply rate >= 30% AND (A) clicks >= 25?
│
│   YES → DETERMINATION: HOLD (on track)
│         Continue standard cadence through Day 30.
│         No follow-up dispatch needed unless specific sectors are WEAK.
│         Log in CHECKIN.md: "Day 7 HOLD — on track — [date]"
│         Next checkpoint: Day 30 (June 30)
│
│   NO → Overall reply rate 15-29% AND clicks 10-24?
│
│        YES → DETERMINATION: HOLD with monitoring
│              Dispatch follow-up templates for any WEAK sectors.
│              Set Day 14 checkpoint (June 15).
│              Log in CHECKIN.md: "Day 7 HOLD — monitoring — [date]"
│              Next checkpoint: Day 14 (June 15)
│
│        NO → DETERMINATION: REBASE (if not already set at Gate 2)
│             Apply Playbook C. Dispatch all sector templates within 6 hours.
│             Log in CHECKIN.md: "Day 7 REBASE — [date]"
│             Next checkpoint: Day 9 review (June 10)
```

### Day 7 Determination Summary

| Determination | Triggers | Next Action | Next Checkpoint |
|---------------|---------|-------------|-----------------|
| CONTACT_VERIFY | 3+ bounces | Fix emails, resend | Restart (resend + 7 days) |
| PAUSE | Clicks < 5 | Delivery diagnostic | 24 hours after diagnostic |
| ESCALATE | Score 4+ reply | Playbook A — Phase 2 prep | Day 14 (lower priority) |
| HOLD | Rate >= 30%, clicks >= 25 | Standard cadence | Day 30 (June 30) |
| HOLD + monitoring | Rate 15-29%, clicks 10-24 | Dispatch WEAK templates | Day 14 (June 15) |
| REBASE | Rate < 15%, 4+ WEAK sectors | Playbook C — all 6 templates | Day 9 review (June 10) |

---

## Decision Tree 2: Follow-Up Dispatch

**Timestamp**: June 8–9, 2026 (within 12 hours of Day 7 Gate determination)
**Applies when**: Day 7 determination is HOLD+monitoring or REBASE
**Does not apply when**: ESCALATE (Playbook A is active), CONTACT_VERIFY (re-send in progress), or PAUSE (diagnostic in progress)
**Input**: Sector_Engagement tab Column H (Signal_Band), Column J (Template_To_Use)
**Time to run**: 20 minutes (including email preparation)

```
START: Open Sector_Engagement tab.
       For each sector row, read Signal_Band (Column H).

FOR EACH SECTOR:

──────────────────────────────────────────────────────────────────────────────

SECTOR: LAW SCHOOL
│
├── Signal_Band = "DEFINITE WEAK" or "PROBABLE WEAK"?
│   YES → Dispatch Template 1 — Law Schools
│         Subject: Following up — election law clinic resource, [domain reference]
│         Talking points:
│           - Law school review timelines are expected; this is a proactive re-reach
│           - Frame as clinic resource, not framework pitch
│           - Offer two-page executive summary (bit.ly/drp-summary) as faster read
│           - Offer clinic-formatted brief if that lowers activation threshold
│           - CC 4.0 — can adapt without asking
│         Send time: Within 12 hours of Day 7 (by 20:00 UTC June 8)
│
│   Signal_Band = "POSSIBLE WEAK"?
│   YES → Watch 48 hours. If still POSSIBLE WEAK by June 10: dispatch Template 1.
│         Set a reminder for June 10 08:00 UTC.
│
│   Signal_Band = "MODERATE" or "STRONG"?
│   → No follow-up needed. Log "No action — [MODERATE/STRONG]" in Column K.

──────────────────────────────────────────────────────────────────────────────

SECTOR: IMMIGRATION LEGAL
│
├── Signal_Band = "DEFINITE WEAK" or "PROBABLE WEAK"?
│   YES → FIRST: Run delivery diagnostic before sending follow-up.
│         Immigration Legal is expected to have the fastest reply rate (Days 1-5).
│         WEAK at Day 7 in this sector indicates delivery failure more likely than
│         disengagement.
│         Diagnostic: Check if June 1 sent emails are in Sent folder. If confirmed
│         sent, proceed to Template 2.
│         Dispatch Template 2 — Immigration Legal
│         Subject: Domain 39 follow-up — Ninth Circuit brief timing and NVRA enforcement
│         Talking points:
│           - NVRA Section 7 enforcement argument (Pathway 2) — privately enforceable
│           - Strengthens APA challenges beyond healthcare domain
│           - Offer brief-format excerpt for their active Ninth Circuit work
│           - Emphasize January 1, 2027 work requirement effective date timeline
│
│   Signal_Band = "POSSIBLE WEAK"?
│   YES → Dispatch Template 2 immediately (do not wait 48 hours for this sector).
│         Immigration Legal POSSIBLE WEAK at Day 7 warrants earlier intervention
│         than other sectors.
│
│   Signal_Band = "MODERATE" or "STRONG"?
│   → No follow-up needed.

──────────────────────────────────────────────────────────────────────────────

SECTOR: CIVIL RIGHTS
│
├── Signal_Band = "DEFINITE WEAK" or "PROBABLE WEAK"?
│   YES → Dispatch Template 3 — Civil Rights
│         Subject: SPLC indictment context — Domain 39 + prosecution deterrence
│         Talking points:
│           - Frame around active federal prosecution pattern (SPLC, DOJ capture)
│           - Democratic participation argument strengthens pre-litigation submissions
│           - Harder for courts to narrow than benefits-access frame
│           - Offer condensed litigation strategy memo if preparing for July-Aug advocacy
│           - January 2027 work requirement effective date: litigation window now
│
│   Signal_Band = "POSSIBLE WEAK"?
│   YES → Watch 48 hours. Civil Rights organizations often have email routing delays.
│         If no improvement by June 10: dispatch Template 3.
│
│   Signal_Band = "MODERATE" or "STRONG"?
│   → No follow-up needed.

──────────────────────────────────────────────────────────────────────────────

SECTOR: ACADEMIC
│
├── Signal_Band = "DEFINITE WEAK" or "PROBABLE WEAK"?
│   YES → Dispatch Template 4 — Academic (but use lighter touch)
│         Subject: Following up — democratic infrastructure argument for your [research]
│         Talking points:
│           - Academic review cycles: 10-21 days is normal, this is a proactive note
│           - Five causal pathways are disaggregatable — each can be cited independently
│           - Offer supplementary citation list for whichever pathway intersects their work
│           - CC 4.0, cite freely
│           - No ask for a response; just surfacing the pathway-specific resource
│         Note: Academic WEAK at Day 7 is not alarming. Send Template 4 June 10
│         (Day 9) rather than June 8 to allow the standard review cycle to play out.
│
│   Signal_Band = "POSSIBLE WEAK"?
│   YES → Watch until June 10. If still POSSIBLE WEAK, send Template 4 on June 10.
│
│   Signal_Band = "MODERATE" or "STRONG"?
│   → No follow-up needed.

──────────────────────────────────────────────────────────────────────────────

SECTOR: FAITH NETWORKS
│
├── Signal_Band = "DEFINITE WEAK" or "PROBABLE WEAK"?
│   YES → Dispatch Template 5 — Faith Networks
│         Subject: Healthcare and civic participation — following up
│         Talking points:
│           - Rural hospital closures: 3.8pp turnout decline per APSR 2025
│           - Medicaid offices as statutory voter registration sites (NVRA)
│           - Civic capacity argument: preventable mortality = diminished political voice
│           - Framing connects healthcare advocacy to voting rights work
│           - Lead with congregational application, not litigation angle
│           - Offer to discuss congregational implementation
│
│   Signal_Band = "POSSIBLE WEAK"?
│   YES → Watch 48 hours. Faith networks have broad broadcast pattern with slow
│         individual response — a single engaged faith leader can trigger wide
│         amplification. Do not mistake slow individual response for disengagement.
│
│   Signal_Band = "MODERATE" or "STRONG"?
│   → No follow-up needed.

──────────────────────────────────────────────────────────────────────────────

SECTOR: LABOR
│
├── Signal_Band = "DEFINITE WEAK" or "PROBABLE WEAK"?
│   YES → Dispatch Template 6 — Labor
│         Subject: Following up — worker health and organizing capacity, Domain 39
│         Talking points:
│           - Medical debt depletes cognitive bandwidth for civic and union participation
│           - CFPB medical debt rule (blocked by Trump administration) — context
│           - OBBBA work requirements effective January 1, 2027: organizing impact
│           - Democratic infrastructure frame: healthcare = conditions for self-governance
│           - Offer labor-specific excerpt for November election cycle materials
│         Note: Labor contacts often need authorization before replying. If you have
│         a named individual contact (not a general union address), send to them directly.
│         Do not send to general union email for the follow-up.
│
│   Signal_Band = "POSSIBLE WEAK"?
│   YES → Watch 48 hours. If still POSSIBLE WEAK by June 10, dispatch Template 6
│         to the specific named contact, not the general organizational address.
│
│   Signal_Band = "MODERATE" or "STRONG"?
│   → No follow-up needed.

──────────────────────────────────────────────────────────────────────────────

AFTER ALL SIX SECTORS:

Log follow-up dispatch in CHECKIN.md:
  "Follow-up dispatch complete — June 8 [time] UTC
   Sectors dispatched: [list]
   Sectors watched (48h): [list]
   Sectors no action (MODERATE/STRONG): [list]"

Set calendar reminder for June 10 at 08:00 UTC to review watched sectors.
```

---

## Decision Tree 3: Week 2 Adjustment

**Timestamp**: June 15, 2026 (Day 14 checkpoint)
**Applies only when**: Day 7 determination was HOLD+monitoring, REBASE, or if WEAK sectors were flagged for 48h watch on June 8 and remain unresolved
**Does not apply when**: Day 7 was ESCALATE or PAUSE (those paths have their own continuation)
**Input**: Same four metrics as Day 7 + rebase actions log from Checkpoints tab
**Time to run**: 30 minutes

```
START: Pull same four values as Day 7.
       Also check: did rebase follow-ups (Template 1-6 dispatched June 8-10) generate any replies?

Collect five values:
  (A) Cumulative Bitly clicks to date
  (B) Overall reply rate (any reply / delivered)
  (C) Count of sectors still showing WEAK signal (run Template A formulas again)
  (D) Any new Score 3+ replies since Day 7? (count from Replies tab, filter by date)
  (E) Did rebased sectors (those that received follow-up templates) reply?
      (Check: for each sector that received Template 1-6, is there any reply logged
       in the Replies tab dated June 8 or later for a contact in that sector?)

──────────────────────────────────────────────────────────────────────────────

BRANCH 1: PHASE 2 TRIGGER
│
├── (A) >= 25 cumulative clicks AND (B) >= 25% reply rate AND (D) >= 3 new Score 3+ replies?
│
│   YES → DETERMINATION: PHASE 2 TRIGGER — DO NOT WAIT FOR DAY 30
│         Phase 1 is demonstrating sufficient engagement velocity to pre-activate Phase 2.
│
│         Immediate actions:
│         1. Update Phase2_Readiness tab (Template D) — check all three threshold rows.
│            If all three say "THRESHOLD MET": Phase 2 is triggered.
│         2. Pull social proof: collect 2-3 direct quotes from Score 4+ replies.
│         3. Prepare Domain 39 Tier 2 contact list (organizations adjacent to
│            Score 4+ Tier 1 replies — peer organizations, referred contacts).
│         4. Draft Tier 2 follow-on email using original Domain 39 template structure,
│            adding the social proof quotes.
│         5. Send Tier 2 email within 48 hours of this determination.
│
│         Log in CHECKIN.md: "Day 14 PHASE 2 TRIGGER — [date] — Tier 2 initiated"
│         Next checkpoint: Day 30 (June 30) — now tracks Tier 2 adoption

──────────────────────────────────────────────────────────────────────────────

BRANCH 2: CONTINUE STANDARD PHASE 1
│
├── (A) >= 25 clicks AND (B) 15-24% reply rate AND (C) <= 2 sectors still WEAK?
│
│   YES → DETERMINATION: CONTINUE STANDARD
│         Phase 1 is performing within acceptable range. No additional intervention
│         needed. Continue monitoring cadence to Day 30.
│
│         Actions:
│         1. Log CONTINUE determination in Checkpoints tab and CHECKIN.md.
│         2. Respond to any outstanding Score 3 replies (integration questions,
│            methodology critiques). Apply reply-triage-framework.md.
│         3. For the <= 2 sectors still WEAK: this is the final follow-up opportunity
│            before Day 30. Apply Modification 2 framing shift to those sectors:
│            shift from "35-domain framework" to "single-domain operational resource."
│            Use the Modification 2 framing in Section 4 Playbook C.
│         4. Set Day 30 checkpoint reminder: June 30 at 08:00 UTC.
│
│         Log in CHECKIN.md: "Day 14 CONTINUE — [date] — Modification 2 applied to: [list]"
│         Next checkpoint: Day 30 (June 30)

──────────────────────────────────────────────────────────────────────────────

BRANCH 3: REBASE EXTENDED
│
├── (A) 10-24 clicks AND (B) 8-14% reply rate AND (C) >= 3 sectors still WEAK?
│
│   YES → DETERMINATION: REBASE EXTENDED
│         The Day 7 rebase actions did not produce sufficient recovery. Escalate
│         to Modification 1 (stakeholder substitution) for WEAK sectors.
│
│         Actions:
│         1. Log REBASE EXTENDED in Checkpoints tab and CHECKIN.md.
│         2. For each sector still WEAK: identify Tier 1.5 contacts
│            (alternatives to the original Tier 1 contacts who have not replied).
│            Tier 1.5 examples:
│            - Law Schools: clinic directors instead of school deans
│            - Immigration Legal: state chapter leads instead of national directors
│            - Civil Rights: regional chapter directors instead of national staff
│            - Academic: department chairs instead of full professors
│            - Faith: regional coordinators instead of national denominational leadership
│            - Labor: local union officers instead of international union staff
│         3. Prepare contact verification for Tier 1.5 contacts (email addresses).
│         4. Draft Tier 1.5 outreach using same templates as original Tier 1
│            but with Modification 2 framing shift for each sector.
│         5. Send Tier 1.5 outreach by June 19 (Day 18).
│
│         Log in CHECKIN.md: "Day 14 REBASE EXTENDED — Modification 1 active — [date]"
│         Next checkpoint: Day 30 (June 30) — includes Tier 1.5 results

──────────────────────────────────────────────────────────────────────────────

BRANCH 4: FAILURE IMMINENT
│
├── (A) < 10 cumulative clicks AND (B) < 8% reply rate AND (E) = NO (rebased sectors did not reply)?
│
│   YES → DETERMINATION: FAILURE IMMINENT
│         Standard email channel has failed to generate signal. Direct contact
│         required before Day 30.
│
│         Actions (complete within 48 hours):
│         1. Log FAILURE IMMINENT in Checkpoints tab and CHECKIN.md
│            under "Needs Your Input."
│         2. Contact 2-3 highest-priority Tier 1 contacts directly via a second
│            channel (LinkedIn DM, organization contact form, or personal referral).
│            Script: "Hi [Name], I sent a framework on healthcare and democratic
│            participation on June 1. Did you receive it? I want to make sure it
│            reached you — happy to resend or discuss if you have any questions."
│         3. Create new Bitly links (old ones may be broken or untracked).
│            Test all links in incognito browser.
│         4. Run the full failure recovery protocol from day-7-14-30-decision-trees.md:
│            FAILURE pathway — all three modifications active.
│         5. Do NOT close Phase 1. Continue to Day 30 with modified approach.
│
│         Log in CHECKIN.md under "Needs Your Input":
│           "Day 14 FAILURE IMMINENT — Direct contact required — [date]
│            Contacts to reach: [list top 2-3 Tier 1 names]
│            Action window: June 15-17"
│         Next checkpoint: Day 30 (June 30) — reassess with direct contact results

──────────────────────────────────────────────────────────────────────────────

NONE OF THE ABOVE (ambiguous signal — some metrics above threshold, some below):
│
└── DETERMINATION: ASSESS — HOLD AND MONITOR
    One or more conditions from Branches 1-4 are partially met but not definitively.
    This typically occurs when: clicks are moderate (10-24) but reply rate is good
    (15%+), or clicks are strong but sectors are still WEAK.
    
    Actions:
    - Respond to all outstanding replies (no backlogs at Day 14)
    - For sectors still WEAK: apply final Modification 2 framing follow-up
    - Continue standard cadence to Day 30 without additional escalation
    - Log in CHECKIN.md: "Day 14 ASSESS — [date] — proceeding to Day 30"
    - Next checkpoint: Day 30 (June 30)
```

### Week 2 Determination Summary

| Determination | Key Inputs | Core Action | Next Checkpoint |
|---------------|-----------|-------------|-----------------|
| PHASE 2 TRIGGER | Clicks >= 25, Rate >= 25%, 3+ new Score 3+ | Activate Tier 2 within 48h | Day 30 tracks Tier 2 |
| CONTINUE STANDARD | Clicks >= 25, Rate 15-24%, <= 2 WEAK | Modification 2 for remaining WEAK sectors | Day 30 (June 30) |
| REBASE EXTENDED | Clicks 10-24, Rate 8-14%, 3+ WEAK | Modification 1 (Tier 1.5 contacts) | Day 30 (June 30) |
| FAILURE IMMINENT | Clicks < 10, Rate < 8%, no rebase response | Direct contact + all 3 modifications | Day 30 (June 30) |
| ASSESS | Mixed signals — some above, some below threshold | Respond to backlogs + Modification 2 | Day 30 (June 30) |

---

## Cross-Tree Summary: June 8–30 Decision Timeline

| Date | Tree | Input | Output Options |
|------|------|-------|---------------|
| June 8 08:00 UTC | Tree 1: Day 7 Gate | Clicks, reply rate, sector bands | ESCALATE / HOLD / PAUSE / REBASE / CONTACT_VERIFY |
| June 8-9 | Tree 2: Follow-Up Dispatch | Sector Signal_Band per sector | Template 1-6 dispatched or 48h watch set |
| June 10 | Tree 2 continued | POSSIBLE WEAK sectors re-checked | Dispatch or release |
| June 15 08:00 UTC | Tree 3: Week 2 Adjustment | Clicks, reply rate, sectors, rebase results | PHASE 2 TRIGGER / CONTINUE / REBASE EXTENDED / FAILURE IMMINENT / ASSESS |
| June 30 08:00 UTC | Tree from day-7-14-30-decision-trees.md | Full four-metric pull | STRONG / MODERATE / WEAK / ASSESS / FAILURE |

---

**Status**: Production-ready. Use Tree 1 starting June 8. Tree 2 immediately after Tree 1. Tree 3 on June 15.
