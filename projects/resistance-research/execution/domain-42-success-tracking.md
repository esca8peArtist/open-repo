---
title: "Domain 42 Success Tracking — DEA-1362 Hearing Outreach Measurement Protocol"
created: 2026-05-09
status: production-ready
deadline: "May 24, 2026 (electronic) / May 28, 2026 (Federal Register)"
scope: "Measurement protocol, weekly checkpoints, contingency decision paths, and post-hearing tracking for Domain 42 Phase 1 outreach"
word_count: ~900
companion_files:
  - execution/domain-42-phase-1-outreach-prioritization.md
  - execution/domain-42-wave-contacts.csv
  - execution/domain-42-outreach-sequencing.md
  - WORKLOG.md
---

# Domain 42 Success Tracking
## Measurement Protocol, Weekly Checkpoints, and Contingency Paths

---

## Response Classification Protocol

Every contact response is classified into one of four commitment tiers. Classification happens at first response — update the Yes/No/Maybe column in `domain-42-wave-contacts.csv` immediately.

**COM — Committed to File**: Explicit written statement that the organization will file a participation notice for DEA-1362 before May 24. Does not need to reference Domain 42. Any statement of intent to file is COM. Action: reply within 24 hours with the submission guide (`domain-42-may-28-dea-submission-guide.md`) and offer to answer procedural questions. Log date and contact name in WORKLOG.md.

**REQ — Reviewing / Requested Materials**: Organization has requested additional materials, is routing internally, or acknowledged the briefing without declining. "Forwarding to our policy team" is REQ. Action: send requested materials immediately; add to follow-up calendar for May 15. Target: 60% of REQ contacts convert to COM if follow-up is prompt.

**BRIEF — Briefing Materials Only**: Organization wants the research but has not indicated filing intent. Action: send materials with a one-sentence deadline reminder embedded. Maximum one additional follow-up on May 18. Downstream value still present — BRIEF contacts may cite Domain 42 in future work or share with their network.

**DEC — Declined**: Explicit statement that the organization will not participate or cannot act within the deadline window. Action: log and close. Do not follow up. One DEC is not a critical path failure.

**NO-REPLY**: No response within 5 days of send. Action: trigger one follow-up per the schedule below. Log as NO-REPLY until response or follow-up deadline passes.

---

## Primary Metrics — May 9 Through May 24

| Metric | Minimum Viable | Target | Stretch | How to Measure |
|--------|:--------------:|:------:|:-------:|----------------|
| Organizations requesting Domain 42 briefing materials after initial send | 2 | 4 | 7 | Count REQ + COM responses across all waves |
| Organizations explicitly committing to DEA hearing participation (COM) | 2 | 4 | 6 | Count COM responses in wave-contacts.csv |
| Secondary contacts reached through network amplification | 5 | 15 | 30 | Count named forwards reported by Wave 1 contacts; SSDP chapter network forwards |
| Participation notices submitted by May 25 (3-day buffer before May 28) | 1 | 3 | 5 | Email confirmations from committed organizations; DEA-1362 docket check |

**The counterfactual tracking rule**: DPA and NORML filing participation notices represents the baseline — they would file regardless of this outreach. Track two separate counts in WORKLOG.md: (1) total organizations that file, (2) organizations whose filing is directly attributable to Domain 42 outreach (counterfactual organizations: ACLU, Sentencing Project, LEAP, NAACP LDF, any state AG). The counterfactual count is the Domain 42-specific contribution to the hearing record.

**The May 25 buffer**: Target having all known participation notice filings confirmed by May 25 — three days before the May 28 Federal Register deadline. This gives a buffer for organizations that encounter submission difficulties and allows final confirmation against the docket before the window closes. Organizations that have not confirmed filing by May 25 should receive a single final check-in: "Have you been able to submit to nprm@dea.gov? Happy to confirm the filing procedure if useful."

---

## Weekly Checkpoints

### Checkpoint 1 — May 11 (48 Hours After Wave 1)

**Check**: How many Wave 1 contacts (DPA, NORML, ACLU, Sentencing Project, LEAP) have responded?

**Threshold to proceed with Wave 2 unchanged**: At least 1 substantive response (COM or REQ) from the 5 Wave 1 contacts.

**If 0 responses at 48 hours**: Do not delay Wave 2 — proceed on schedule. But add one sentence to each Wave 2 send: "I wanted to make sure [Organization] had this before the DEA deadline — [Organization A] and similar groups are reviewing the briefing now." This maintains forward momentum without fabricating confirmation.

**Social proof check**: If DPA or NORML has responded positively (COM or REQ), activate the social proof sentence for all remaining Wave 2 sends. See outreach sequencing protocol in `domain-42-outreach-sequencing.md`.

**Log in WORKLOG.md**: Response count, classification, any notable content from responses, send dates for Wave 2.

### Checkpoint 2 — May 14 (After Wave 2 Complete)

**Check**: What is the running COM count? How many REQ contacts need follow-up?

**Critical path assessment**:
- If running COM count is 0: Focus entirely on ACLU and Sentencing Project. Both received Wave 1 sends; if neither has responded substantively, send one targeted follow-up to each, subject line: `[Organization] — following up, Domain 42 DEA-1362 briefing, 10 days to electronic deadline (May 24)`. Secondary contact for each: check organizational directory for the Criminal Law Reform Project director (ACLU) and Research Director (Sentencing Project).
- If running COM count is 1 (DPA or NORML only): Activate LEAP and SSDP as referral nodes. Ask explicitly: "If you have a working relationship with DPA or NORML's federal policy staff, an introduction would be the most valuable thing you can do — the DEA electronic deadline is May 24."
- If running COM count is 2 or more: Proceed to Wave 3 AG outreach on standard schedule. Concentrate support on confirmed filers.

**Wave 3 go/no-go**: Assess whether AG outreach is viable given current timeline. If it is May 14 or earlier, proceed with California and Colorado AG sends. If it is May 15 or later, drop Michigan and Washington AG sends.

**Log in WORKLOG.md**: Running COM/REQ/BRIEF/DEC counts by wave, follow-up triggers activated, Wave 3 send decisions.

### Checkpoint 3 — May 18 (Hard Stop Day)

**This is the final day for any new outreach.** No new organizational contact after May 18.

**Check**: What is the final contact count by status? Have all REQ contacts been followed up?

**Final follow-up sweep**: Send one final abbreviated reminder (3 sentences maximum) to all contacts that have not responded and have not declined. Subject line: `One week to DEA hearing participation deadline (May 28) — Domain 42 briefing still available`. Include the corrected deadline language (May 24 electronic) in the body.

**Transition to filing support**: Shift mode from outreach to filing support. All COM organizations receive active support: offer to review their participation notice language before submission, confirm the docket number and submission email, walk through the filing procedure from `domain-42-may-28-dea-submission-guide.md`.

**Log in WORKLOG.md**: Final status counts, names of committed organizations, any follow-up threads still open.

### Checkpoint 4 — May 25 (3-Day Buffer Check)

**Check**: How many participation notices have been confirmed submitted?

**Contact all COM organizations**: One-sentence check-in: "Have you been able to submit to nprm@dea.gov? Happy to help with anything." Log the filing confirmation date and docket confirmation (if the DEA sends one) in WORKLOG.md.

**If minimum viable outcome (1 submission confirmed) is not met by May 25**: Review the COM list. If organizations that committed have not yet filed, escalate the support offer — walk through the filing procedure in a phone or video call if they are willing. The May 28 deadline is firm.

---

## Downstream Metrics — June 22 Through July 15

| Metric | How to Measure | Target Date |
|--------|---------------|------------|
| Organizations selected as DEA designated participants (from the Domain 42-briefed list) | DEA-1362 docket — June 22 notification | June 22 |
| Organizations excluded despite filing (document the exclusion list) | Compare filed notice list against designated participant list | June 22 |
| Domain 42 Section 3 language appearing in any written hearing submissions | DEA-1362 docket for written testimony post-June 29 | July 15 |
| Organizations sharing Domain 42 through membership communications before June 29 | Monitor DPA, NORML, ACLU newsletter archives | June 29 |
| Media coverage using "regulatory capture" or "democratic exclusion" framing of the hearing | Google Alert: "DEA rescheduling democratic exclusion" + "DEA regulatory capture hearing" | Ongoing |

**The exclusion documentation protocol**: If Domain 42-briefed organizations file participation notices and are excluded by the DEA (the 2024 pattern: 160+ requestors, 25 selected, disproportionately anti-reform), document the exclusion list in WORKLOG.md as affirmative evidence for Domain 42 Section 2. A selection outcome that excludes NORML, ACLU, and the Sentencing Project while admitting pharmaceutical industry representatives is itself a data point for the regulatory capture argument. Log: organization name, date of participation notice filing, DEA response date, selection decision.

---

## Contingency Decision Paths

**If no COM by May 13 (DPA and NORML have not responded substantively)**:
1. Escalate to secondary contacts: DPA Executive Director (Maria McFarland Sanchez-Moreno); NORML Executive Director (Erik Altieri) or legal committee chair. Find via organizational staff directories.
2. Redirect emphasis to ACLU and Sentencing Project — their filing is more analytically valuable than a DPA or NORML filing because they would not file without this outreach.
3. Activate LEAP and SSDP as referral nodes (see Section 4, Contingency B, in `domain-42-phase-1-outreach-prioritization.md`).

**If the DEA freezes or cancels the June 29 hearing (Section 591 congressional rider is the most likely mechanism)**:
Organizations that have already filed participation notices by May 24 retain administrative standing for any reconstituted proceeding. The filings and any exclusion decisions remain in the public record and are usable for subsequent legislative advocacy. Distribute Domain 42 to the secondary academic and Substack audience post-May 28 for longer-term policy framing. The democratic design argument does not expire with the DEA hearing deadline.

**If minimum viable outcome is not achieved (fewer than 2 COM by May 24)**:
The Domain 42 research document retains independent value. Distribute to law school clinics, the general Substack audience, and state-level drug policy reform organizations as background material for non-hearing drug policy work. The CC-BY 4.0 license permits free adaptation and use without further outreach from this project. Log the outcome in WORKLOG.md as a Phase 1 data point — the measurement protocol is itself evidence of what the outreach attempted, regardless of uptake.

---

*Created May 9, 2026. This document is the operational measurement counterpart to domain-42-phase-1-outreach-prioritization.md. All outcome logging goes to WORKLOG.md. Post-June 29: check DEA-1362 docket at regulations.gov for published testimony and participant lists.*
