---
title: "Phase 2 Post-Deadline Contingency Activation Framework"
created: "2026-06-29"
session: "General Research Agent — Item 33"
status: "PRODUCTION-READY — dormant until July 1 00:00 UTC trigger"
domains: "51 (Campaign Finance/Dark Money), 48 (Criminal Justice Civic Exclusion)"
hard_deadline: "July 1 2026 00:00 UTC"
activation_trigger: "User posts send-execution timestamp to INBOX.md"
branches: "A (on-time), B (slipped <7 days), C (slipped >7 days)"
---

# Phase 2 Post-Deadline Contingency Activation Framework

**Prepared**: June 29, 2026  
**Dormancy condition**: If sends execute June 29–30, this document has zero operational value. Branch A applies and normal Tier 2 proceeds per PHASE_2_CONTINGENCY_DECISION_TREE.md.  
**Activation condition**: July 1 00:00 UTC arrives without INBOX.md confirmation of send execution → auto-route to Branch B. July 8 00:00 UTC without confirmation → auto-route to Branch C.

---

## How This Document Is Used

1. User executes Domain 51/48 sends and posts timestamp to INBOX.md (e.g., "[resistance-research] Domain 51/48 sends executed 2026-07-03 14:00 UTC")
2. Orchestrator reads timestamp, applies decision tree in PHASE_2_CONTINGENCY_DECISION_TREE.md (companion file), outputs branch assignment
3. User opens this document, navigates to the assigned branch section, executes the pre-staged checklist
4. No further planning required — all contacts, templates, and dates are pre-populated

**Maximum contingency execution time**:
- Branch A: 0h (no contingency activation needed)
- Branch B: 2–3h spread across July 2–10
- Branch C: 4–5h spread across July 8–20, including Saturday–Sunday work if sends execute July 8–9

---

## Branch A: Sends Execute June 29–30 (On-Time)

**Trigger condition**: User posts send confirmation to INBOX.md with timestamp before July 1 00:00 UTC.

**Status**: No contingency activation. Proceed to normal Tier 2.

### Branch A Actions (No Contingency)

- [ ] Post send timestamp to INBOX.md: "[resistance-research] Domain 51/48 sends executed [DATE TIME UTC]"
- [ ] Set T+7 checkpoint reminder: 7 days from send date
- [ ] Follow normal Tier 2 routing per PHASE_2_CONTINGENCY_DECISION_TREE.md
- [ ] Domain 51 T+7 window: July 5–6 (if sent June 28–29)
- [ ] Domain 48 T+7 window: July 5–7 (if sent June 28–30)

### Branch A Tier 2 Timeline (Normal)

| Date | Action | Time |
|------|--------|------|
| June 29–30 | Sends execute | 2.5–3h (per PHASE_2_WAVE_1_EXECUTION_CHECKLIST.md) |
| July 5–6 | Domain 51 T+7: check CLC + Issue One replies | 15 min |
| July 5–7 | Domain 48 T+7: check Sentencing Project + PPI replies | 15 min |
| July 6–8 | Tier 2 activation per signal strength (see PHASE_2_CONTINGENCY_DECISION_TREE.md) | 1.5–3h |
| July 10–15 | Monitor Tier 2 responses; Tier 3 decision gate | 30 min |

**Full T+7 routing**: See PHASE_2_CONTINGENCY_DECISION_TREE.md, STRONG/MODERATE/DRY branches.

---

## Branch B: Sends Execute July 1–7 (Slipped <7 Days)

**Trigger condition**: User posts send confirmation to INBOX.md with timestamp July 1 00:00 UTC – July 7 23:59 UTC.

**Activation**: Orchestrator posts to INBOX.md — "Phase 2 contingency activated (Branch B). See PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md Branch B section."

### Branch B Overview

- **Sends are past the July 1 Domain 51 CA Fair Elections Act messaging lock** but still within actionable advocacy window
- **Domain 48 hard deadline (Virginia Right to Vote Coalition July 15)** is intact or compressed but achievable
- **Corrective action**: Compress Tier 2 window, start Tier 3 5 days early (July 5 vs. July 10–15 normal), overlap Tier 2 + Tier 3 by 5 days
- **Estimated impact retention**: 60–75% of full Branch A value (see PHASE_2_CONTINGENCY_FINANCIAL_MODEL.md)

### Branch B Pre-Execution Checklist (Run Immediately Post-Send)

- [ ] Confirm both Gist URLs are live (incognito browser test):
  - Domain 51: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
  - Domain 48: https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8
- [ ] Log exact send timestamps in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md and DOMAIN_48_DISTRIBUTION_EXECUTION_LOG.md
- [ ] Calculate Branch B Tier 2 and Tier 3 target dates using table below
- [ ] Set calendar reminders for all date-anchored actions below

### Branch B Date Calculation Table

Replace [SEND_DATE] with actual execution date:

| Action | Normal (Branch A) | Branch B Formula | Example: July 3 send |
|--------|------------------|------------------|----------------------|
| Domain 51 T+7 check | 7 days post-send | [SEND_DATE] + 7 | July 10 |
| Domain 48 T+7 check | 7 days post-send | [SEND_DATE] + 7 | July 10 |
| Tier 2 activation gate | T+7 | T+7 (same, compressed) | July 10 |
| Tier 2 sends (high-urgency 8) | July 6–8 (Branch A) | [SEND_DATE] + 2 (accelerated) | July 5 |
| Tier 3 start (early) | July 10–15 normal | [SEND_DATE] + 2 (skip gap) | July 5 |
| Tier 2/3 overlap window | None (Branch A) | July 5–10 | July 5–10 |
| Virginia July 15 deadline | July 1–10 ACLU VA send | July 8–12 (compressed) | July 8–12 |

### Branch B Contact Priority — Domain 51 (8 High-Urgency Contacts)

Send in this order. Do not wait for responses between sends — stagger 90 minutes per send or send on consecutive days.

| Priority | Organization | Contact | Email | Template Modification |
|----------|---|---|---|---|
| 1 | Campaign Legal Center | Erin Chlopak | echlopak@campaignlegalcenter.org | Subject: "URGENT — Constitutional architecture research on Citizens United — CA Fair Elections window closed July 1 — national implications live" |
| 2 | Issue One | General inbox | info@issueone.org | Subject: "Dark money architecture research — post-July 1 national window, FEC collapse documentation" |
| 3 | True North Research | Lisa Graves | info@truenorthresearch.org | Cold framing, no CA deadline hook. Use: "Dark money constitutional architecture — FEC enforcement collapse — delivered [DELIVERY_DATE]" |
| 4 | Democracy 21 | Fred Wertheimer | fwertheimer@democracy21.org | Lead with Wertheimer's work cited in Domain 51: "I am sharing research that cites your McCutcheon dissent framing as foundational" |
| 5 | Common Cause CA | Outreach team | outreach@commoncauseca.org | Remove CA Fair Elections Act language (window closed July 1). Use: "Post-deadline federal campaign finance advocacy context — [DELIVERY_DATE]" |
| 6 | League of Women Voters CA | Policy team | ca@lwv.org | Same as Common Cause CA — remove CA-specific deadline hook, use federal framing |
| 7 | Clean Money Action Fund | Research inbox | info@cleanmoneyaction.org | Use research-collaboration framing: "Analysis of disclosure law enforcement gaps — relevant to your 2026 state measure work" |
| 8 | End Citizens United | Research team | info@endcitizensunited.org | National amplification framing: "Federal dark money research delivered [DELIVERY_DATE] — coalition context for ECU advocacy" |

**Template modification rule for Branch B — [DELIVERY_DATE] and [URGENCY_LEVEL] fills**:
- [DELIVERY_DATE] = actual send date (e.g., "July 3, 2026")
- [URGENCY_LEVEL] = "post-July 1 window — federal advocacy timeline intact"

### Branch B Contact Priority — Domain 48 (8 High-Urgency Contacts)

| Priority | Organization | Contact | Email | Template Modification |
|----------|---|---|---|---|
| 1 | Sentencing Project | Nicole D. Porter | nporter@sentencingproject.org | Add: "Delivered [DELIVERY_DATE] — Virginia July 15 coalition window still reachable" |
| 2 | Prison Policy Initiative | Peter Wagner | info@prisonpolicy.org | Same Virginia window note. Use PPI-specific variant per PHASE_2_WAVE_1_EXECUTION_CHECKLIST.md |
| 3 | Brennan Center (Voting Rights) | Sean Morales-Doyle | brennancenter.org/about/contact (web form) | Accelerate: route form to Morales-Doyle specifically; note July 15 Virginia deadline in opening |
| 4 | Fines and Fees Justice Center | Joanna Weiss | info@finesandfeesjusticecenter.org | Lead with LFO-as-poll-tax argument; note Alabama SB 24 October 1 deadline |
| 5 | Worth Rises | Bianca Tylek | info@worthrises.org | Policy escalation framing; note [DELIVERY_DATE] |
| 6 | Campaign Legal Center (Restore Your Vote) | Blair Bowie | info@campaignlegal.org | Note: different address from Domain 51 CLC send. Virginia July 15 hook |
| 7 | NAACP Legal Defense Fund | Janai Nelson | info@naacpldf.org | Tier 2 contact — activate early in Branch B given compressed Tier 2 window. Cite Sentencing Project if SP replied |
| 8 | ACLU of Virginia | Mary Bauer | acluva@acluva.org | Virginia July 15 deadline is the hook. Send July 8–12 (latest viable date for July 15 integration) |

**Note on M4BL**: Movement for Black Lives (info@m4bl.org) is deferred from Branch B Priority 8 to allow ACLU VA prioritization. Activate M4BL in Branch B week 2 if Virginia window still active.

### Branch B Tier 3 Early Start (July 5 vs. Normal July 10–15)

Skip the normal 5-day gap between Tier 2 and Tier 3. Begin Tier 3 domain activation July 5 regardless of Tier 2 signal if sends executed July 1–4.

**Tier 3 targets (activate July 5–8)**:
- Volcker Alliance: policy.director@volckeralliance.org — cross-domain Democracy Program framing
- Democracy Forward: contact@democracyforward.org — litigation-adjacent framing
- CREW (Citizens for Responsibility and Ethics): info@citizensforethics.org — enforcement accountability framing
- Government Executive: editors@govexec.com — research amplification framing

**Tier 3 template modification**: Use [URGENCY_LEVEL] = "mid-legislative-session advocacy context — Domain 51/48 distributed [DELIVERY_DATE]"

### Branch B Escalation Trigger

**If 0 replies within 72 hours of Tier 2 send (Branch B only)**:
- Do not wait for T+7. Move immediately to Tier 3 activation.
- Rationale: The compressed window (5 fewer days vs. Branch A) means waiting T+7 in Branch B sacrifices the remaining advocacy window.
- Action: Post to INBOX.md — "[resistance-research] Branch B escalation triggered — 0 replies at T+72h — activating Tier 3 early per Branch B protocol"

### Branch B Day-by-Day Execution Map

| Day | Action | Time Required |
|-----|--------|---------------|
| Send day (July 1–7) | Execute sends per PHASE_2_WAVE_1_EXECUTION_CHECKLIST.md | 2.5–3h |
| Send day + 1 | Confirm delivery (no hard bounces); begin Domain 51 Tier 2 Priority 1–4 sends | 45–60 min |
| Send day + 2 | Domain 51 Tier 2 Priority 5–8; Domain 48 Tier 2 Priority 1–4 | 45–60 min |
| Send day + 2 (if July 1–4 send) | Begin Tier 3 early (Volcker, Democracy Forward) | 30–45 min |
| Send day + 3 | Domain 48 Tier 2 Priority 5–8; monitor Domain 51 replies | 30–45 min |
| Send day + 5 | 72h escalation check — if 0 replies, activate remaining Tier 3 | 30 min |
| July 8–12 | ACLU of Virginia send (calendar-driven Virginia July 15 anchor) | 20 min |
| July 10 | T+7 checkpoint — assess signal strength, route per PHASE_2_CONTINGENCY_DECISION_TREE.md | 20 min |
| **Total** | | **2–3h spread across 8–10 days** |

---

## Branch C: Sends Execute July 8+ (Slipped >7 Days)

**Trigger condition**: July 8 00:00 UTC arrives without INBOX.md confirmation, OR user posts confirmation with timestamp July 8 00:00 UTC or later.

**Activation**: Orchestrator posts to INBOX.md — "Phase 2 contingency activated (Branch C). Emergency protocol. See PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md Branch C section."

### Branch C Overview

- **Domain 51 CA deadline is 7+ days past** — California Fair Elections Act window closed permanently; shift to federal campaign finance framing only
- **Domain 48 Virginia July 15 window is at risk** — only reachable if sends execute by July 11; beyond July 11, Virginia coalition integration is not achievable in the current cycle
- **Congressional early recess risk**: July 15+ enters "informal recess" period — Hill staff attention drops significantly until September (formal recess is August 4–September 7)
- **Full contingency activated**: Mid-legislative-window rapid-response protocol; skip Tier 2/Tier 3 overlap; focus on August 1 post-Summer Recess momentum point
- **Estimated impact retention**: 40–50% of full Branch A value (see PHASE_2_CONTINGENCY_FINANCIAL_MODEL.md)
- **Saturday–Sunday work required** if sends execute July 8–9 (weekend execution to catch pre-recess window before July 14–15)

### Branch C Critical Decision Points

**1. Virginia July 15 gate (assess immediately on Branch C activation)**:
- If sends execute July 8–11: ACLU of Virginia contact is still viable. Send immediately on execution day — do not stagger. Virginia coalition materials deadline July 15 is now 4–7 days away.
- If sends execute July 12+: Virginia July 15 window is closed. Remove ACLU VA from active contact list. Flag for next cycle (November 2026 ballot measure window reopens September).

**2. Domain 51 CA reframe**:
- California Fair Elections Act messaging infrastructure lock was July 1. All CA-specific language in templates is now outdated.
- Replace all CA-specific language with federal dark money framework framing.
- Common Cause CA, LWV CA, and Clean Money Action Fund emails must use: "Post-deadline federal campaign finance advocacy context" rather than any CA-specific deadline hook.

**3. August 1 redirect**:
- Congress returns from Summer Recess approximately August 5–7. The August 1–7 window is the highest-value advocacy window in Branch C.
- All Tier 3 sends should target the August 1–7 window, not immediate July execution. Exception: Sentencing Project, PPI, and Fines and Fees Justice Center (policy research orgs, not Hill-adjacent — send immediately regardless of recess).

### Branch C Pre-Execution Checklist (Run Immediately Post-Send)

- [ ] Assess Virginia July 15 gate: sends executed by July 11? Yes → ACLU VA immediate contact. No → skip.
- [ ] Rewrite all CA-specific template language to federal framing (see template modifications below)
- [ ] Identify Saturday–Sunday contact (if executing July 8–9): Hill-adjacent contacts will not be read until Monday July 14; send to research orgs immediately, schedule Hill-adjacent sends for Monday July 14 08:00 local time
- [ ] Log send timestamp in both execution log files
- [ ] Notify Domains 49–50 stakeholders (parallel emergency email — see Section below)

### Branch C Contact Priority — 6-Contact Emergency Protocol

These 6 contacts represent the highest-value, lowest-deadline-risk contacts. Execute in this order within 48 hours of send execution.

| Priority | Organization | Contact | Email | Branch C Framing | Notes |
|----------|---|---|---|---|---|
| 1 | Sentencing Project | Nicole D. Porter | nporter@sentencingproject.org | "Criminal justice civic exclusion synthesis — delivered [DELIVERY_DATE] — Virginia coalition window [OPEN/CLOSED per July 11 gate]" | Research org — not Hill-adjacent, send immediately including weekends |
| 2 | Fines and Fees Justice Center | Joanna Weiss | info@finesandfeesjusticecenter.org | "LFO civil rights analysis delivered [DELIVERY_DATE] — Alabama SB 24 October 1 deadline still actionable" | LFO framing survives Branch C — Alabama deadline is October, not July |
| 3 | True North Research | Lisa Graves | info@truenorthresearch.org | "Dark money constitutional architecture — federal campaign finance research — delivered [DELIVERY_DATE]" | Cold contact, no CA hook needed — use federal framing |
| 4 | Democracy 21 | Fred Wertheimer | fwertheimer@democracy21.org | "McCutcheon-era dark money documentation — research citing your work — delivered [DELIVERY_DATE]" | Cite Wertheimer's work as anchor — research-to-cited-source is warmest available approach |
| 5 | NAACP Legal Defense Fund | Janai Nelson | info@naacpldf.org | "Felony disenfranchisement constitutional architecture — delivered [DELIVERY_DATE] — August advocacy context" | Shift framing to August pre-term SCOTUS window; Readmission Act theory is not recess-dependent |
| 6 | Prison Policy Initiative | Peter Wagner | info@prisonpolicy.org | "Criminal justice civic exclusion synthesis — built on PPI's research — delivered [DELIVERY_DATE]" | PPI variant per PHASE_2_WAVE_1_EXECUTION_CHECKLIST.md; add note about August recess advocacy window |

### Branch C Deferred Contact List (Activate August 1–7, Post-Recess)

These contacts should NOT receive emails in the July 12–31 window if sends execute July 12+. Schedule for August 1–7.

| Organization | Email | Why Deferred | August Framing |
|---|---|---|---|
| Campaign Legal Center | echlopak@campaignlegalcenter.org | Hill-adjacent — recess reduces staff attention | "Constitutional campaign finance analysis — pre-fall term advocacy context" |
| Issue One | info@issueone.org | Legislative window dependent | "Dark money architecture research — fall 2026 legislative context" |
| Brennan Center (Voting Rights) | brennancenter.org/about/contact | Litigation-adjacent; recess period | "Civic exclusion synthesis — fall term SCOTUS context" |
| End Citizens United | info@endcitizensunited.org | Campaign finance advocacy — August cycle context | "Federal dark money research — fall 2026 campaign finance advocacy" |
| ACLU of Virginia | acluva@acluva.org | Virginia July 15 window closed if July 12+ | "November 2026 ballot measure research context — delivered [DELIVERY_DATE]" |

### Branch C Parallel Emergency Email — Domains 49–50 Stakeholders

If sends slip to July 8+, send the following notification to Domain 49–50 contacts on execution day to flag the delay and set expectations for July–August research activation.

**Addresses**: Do not send to Domain 49–50 primary contacts (research has not been distributed). This is an internal stakeholder notification to any co-researchers or collaboration-track contacts identified in PHASE_2_COALITION_CONTACT_MATRIX.md Domains 49–50 section.

**Subject**: "Phase 2 research timeline — Domain 49/50 activation shifted to August"

**Body**:
```
Hi [CONTACT],

I wanted to flag a timeline shift in our Phase 2 democratic renewal research distribution. Domains 51 (Campaign Finance) and 48 (Criminal Justice/Civic Exclusion) sends have executed as of [DELIVERY_DATE]. Due to the timing, Domain 49 (Environmental Justice) and Domain 50 (LGBTQ+ Civic Participation) research will activate on the August 1–15 schedule (post-Summer Recess) rather than the original July 1–15 target.

This does not affect the research quality or completeness — both domains are fully production-ready. The August window aligns better with Hill staff attention post-recess, and the Domain 50 August 1 ballot measure certification deadline in 7 states makes August the higher-value distribution window in any case.

I will be in touch with the Domain 49/50 materials in early August.

[YOUR_NAME]
[YOUR_CONTACT_INFO]
```

### Branch C Day-by-Day Execution Map

| Day | Action | Time Required |
|-----|--------|---------------|
| Send day (July 8+) | Execute sends per PHASE_2_WAVE_1_EXECUTION_CHECKLIST.md | 2.5–3h |
| Send day (if Sat–Sun) | Send Priority 1–3 (research orgs, not Hill-adjacent) immediately | 30–45 min |
| Monday post-send | Send Priority 4–6; assess Virginia July 15 gate | 45–60 min |
| Send day + 1–2 | Assess Virginia gate; send ACLU VA if July 11 or earlier | 20–30 min |
| Send day + 2 | Domains 49–50 stakeholder notification emails | 20–30 min |
| Send day + 5 | T+5 check: any replies from Priority 1–6? Route per signal | 15 min |
| July 31 | Pre-August-window prep: refresh templates for August framing | 30 min |
| August 1–7 | Deferred contact list activation (Hill-adjacent, post-recess) | 60–90 min |
| August 1–15 | Domains 49–50 research activation if Branch C signal is MODERATE+ | 3–4h |
| **Total** | | **4–5h spread across July–August** |

### Branch C Template Modifications

**Replacing California deadline language**:

Replace ALL instances of:
- "California Fair Elections Act" → "federal campaign finance disclosure architecture"
- "July 1 deadline" → "post-Citizens United enforcement gap"
- "CA ballot measure window" → "2026 federal campaign finance advocacy cycle"
- "SB 2471 constitutional theory" → "Hawaii-model constitutional theory applicable nationally"

[DELIVERY_DATE] = actual send date  
[URGENCY_LEVEL] = "mid-legislative-session — August pre-term advocacy context"

---

## Summary Comparison Table

| Branch | Trigger | Tier 2 Contact Count | Tier 3 Start | Total Active Time | Virginia July 15 | Impact Retention |
|--------|---------|---------------------|--------------|-------------------|-----------------|-----------------|
| A (on-time) | Sends June 29–30 | 12 (normal) | July 10–15 | 2.5–3h over 2–3 weeks | Fully achievable | 100% |
| B (slipped <7 days) | Sends July 1–7 | 8 (high-urgency) | July 5 (early) | 2–3h over 8–10 days | Achievable if July 11 | 60–75% |
| C (slipped >7 days) | Sends July 8+ | 6 (emergency) | August 1 | 4–5h over 3–4 weeks | At risk; closed if July 12+ | 40–50% |

---

*Created June 29, 2026 (Item 33, Exploration Queue). All contacts sourced from PHASE_2_COALITION_CONTACT_MATRIX.md (verified June 17, 2026). Template language anchored to PHASE_2_WAVE_1_EXECUTION_CHECKLIST.md, DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md, and DOMAIN_48_EMAIL_TEMPLATE_SET.md. Branch decision routing: see PHASE_2_CONTINGENCY_DECISION_TREE.md (Item 33 companion file). Financial impact analysis: see PHASE_2_CONTINGENCY_FINANCIAL_MODEL.md.*
