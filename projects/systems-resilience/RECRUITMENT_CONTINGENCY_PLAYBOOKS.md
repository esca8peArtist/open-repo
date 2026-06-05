---
title: "Wave 2 Author Recruitment Contingency Playbooks"
project: systems-resilience
phase: 6
wave: 2
status: PRODUCTION-READY — use June 13–14 during author matching session
created: 2026-06-05
item: 81
purpose: "Five named contingency scenarios (A–E) covering the full outcome space of June 14–15 author matching. Each scenario includes a decision tree, copy-paste notification templates, domain reassignment logic, and timeline impact assessment. Written for project coordinator use during and after the June 14 matching session."
deadline: June 14, 2026 (author matching session)
cross_references:
  - WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md (Item 64 — platform-independent onboarding)
  - PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md (Item 69 — tier A/B/C author list)
  - WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md (Item 78 — quality gates)
  - DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md (Item 79 — 9-contact infrastructure)
  - RECRUITMENT_RESPONSE_TRACKING_AUTOMATION.md (Item 81 companion)
  - WAVE_2_GO_NO_GO_DECISION_GATE_JUNE14.md (Item 81 companion)
---

# Wave 2 Author Recruitment Contingency Playbooks

> **Lead finding**: The highest-probability contingency in Wave 2 recruitment is not total failure but partial success — a mixed-tier roster where 1–2 domains have Tier B authors instead of Tier A, 1 domain has a Tier C author requiring additional onboarding support, and 1 domain has an unresolved backup. This Scenario B outcome (4–5 confirmed authors) is fully recoverable without deferral if the backup activation and scope adjustment decisions are made by June 14 EOD. Scenarios C and D require project lead judgment calls that cannot be pre-made; this playbook pre-stages the decision logic so those calls take minutes, not hours, during the matching session.

---

## How to Use This Document

**Before June 14 (June 13)**: Read all five scenarios. Confirm which scenario best matches your current confirmed roster count. Pre-draft the relevant notification templates.

**During June 14 matching session**: Check confirmed roster count at 14:00 UTC. Route to the appropriate scenario. Use the decision tree to determine Go/No-Go path. Use the notification templates to communicate with confirmed and unconfirmed authors before EOD June 14.

**After June 14**: Log the chosen scenario and path in the PROJECTS.md systems-resilience current focus line. Update the author pairing record in WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md.

**Scenario selection logic**:

```
Count confirmed authors (Tier A or B, status = POSITIVE or CONDITIONAL-resolved) by June 13 EOD:

6 confirmed → Scenario A (Full Success)
4–5 confirmed → Scenario B (1–2 Dropout)
≤3 confirmed → Scenario C (≥3 Dropout)
≥50% Tier A no-response by June 11 → Scenario D (Slow Responder Critical Path) — activate before June 14
Platform unavailable June 15 → Scenario E (Platform Unavailability) — activate immediately on detection
```

Multiple scenarios can apply simultaneously. Scenario D and Scenario E are action triggers that activate before June 14; Scenarios A, B, C are June 14 routing decisions.

---

## Scenario A: Full Success

**Condition**: All Tier A + at least 4/6 Tier B authors confirm by June 13 EOD. Minimum roster: 6 confirmed authors (one per domain), Tier A or B. Platform status: at least one of Nextcloud+Matrix or Google Drive confirmed ready by June 14 14:00 UTC.

### Decision Tree

```
Confirmed authors ≥ 6?
  YES → All 6 domains have confirmed authors?
    YES → All confirmations are POSITIVE (not CONDITIONAL-unresolved)?
      YES → → LAUNCH PATH A (June 20 as planned)
      NO (1–2 CONDITIONAL unresolved) → Resolve CONDITIONALs by June 14 EOD.
               If resolved by EOD → LAUNCH PATH A
               If unresolved → route to Scenario B
  NO → route to Scenario B
```

### What Full Success Looks Like (Objective Criteria)

- 6 rows in `recruitment_tracking_log.csv` with `response_status = POSITIVE`
- All 6 authors are Tier A or Tier B (no Tier C in primary author slots)
- No domain has a CONDITIONAL that depends on scope reduction, compensation negotiation, or start-date change
- Platform status: Nextcloud+Matrix ready OR Google Drive fallback confirmed ready by June 14 14:00 UTC

### Go/No-Go Decision

**Decision**: GO — Launch June 20 as planned.

**No contingency needed.** Proceed to standard onboarding:
- June 15: Send onboarding package to all 6 confirmed authors (WAVE_2_GENERIC_ONBOARDING_TEMPLATE.md, filled and personalized)
- June 15: Finalize peer review pairing assignments (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md, June 14 matching session output)
- June 17: T+3 check-in for Tier B authors (optional for Tier A)
- June 20: Sprint start — T+0 kickoff messages from all authors

### Notification Template A-1: Launch Confirmation to All Authors

```
Subject: Wave 2 Confirmed — June 20 Sprint Start, Your Onboarding Materials

Hi [Author First Name],

Great news: all six Wave 2 author slots are confirmed. We're on track for a June 20 
sprint start.

Here is your onboarding package:

1. Your domain scope document (attached — [Domain Name], [Tier] track)
2. Your annotated bibliography (attached — [XX] pre-vetted sources, green/amber/red rated)
3. Platform access: [Platform name and URL, or Google Drive link]
4. Your peer reviewer: [Peer Reviewer Name], [Domain XX], [contact handle/email]
5. Wave 1+2 corpus: [URL]

Please confirm receipt and platform access by June 17.

Sprint timeline:
- June 20 (T+0): Post your kickoff message in your domain workspace
- June 27 (T+7): 50% draft checkpoint (Sections 1–2 narrative-complete, all headings present)
- July 4 (T+14): Full draft (all sections, citations verified)
- July 4–7 (T+14–17): Peer review exchange
- July 11 (T+21): Revised draft
- July 15 (T+25): Project lead final review
- August 20 (T+60): Production-ready document

Questions before June 20? Use your platform workspace for routine questions. 
Email [PROJECT LEAD EMAIL] for anything blocking.

Welcome aboard — this is going to be a strong sprint.

[Project Lead Name]
```

---

## Scenario B: 1–2 Author Dropout

**Condition**: 1–2 Tier A authors have gone dark or declined, but the core author pool (at minimum 4 confirmed authors from Tiers A+B across 4+ domains) remains intact. At least 4 of the 6 domains have confirmed Tier A or B authors.

### Decision Tree

```
4–5 confirmed Tier A/B authors by June 13 EOD?
  YES (5 confirmed, 1 gap) →
    Identify which domain has the gap.
    Is a named Tier B backup available for that domain?
      YES → Contact backup (Template B-1 below). June 14 activation.
             If backup confirms by June 14 EOD → LAUNCH PATH B (June 20, reduced roster)
             If backup does not confirm by June 14 EOD → defer that domain to Wave 3
      NO → Assess whether the gap domain is optional or required:
             Domain 65 (optional) → Defer to Wave 3. Proceed with 5-domain launch.
             Domain 61 (conditional) → Defer or reduce scope. Proceed with 5-domain launch.
             Domains 60/62/63/64 (required) → Activate any available Tier C backup.
               Tier C confirmed? → LAUNCH PATH B with Tier C for that domain (lower scope)
               No Tier C → route to Scenario C assessment
  YES (4 confirmed, 2 gaps) →
    Are both gap domains optional/conditional (65, 61)?
      YES → Defer both to Wave 3. Launch 4 required domains June 20 (PATH B).
      NO (one or both gaps are in required domains 60/62/63/64) →
        For each required-domain gap:
          Tier B backup available → activate (Template B-1)
          No backup → route to Scenario C
```

### Tier C Backup Protocol (When Tier B Unavailable)

Tier C authors are appropriate for a reduced-scope launch only. Assign Tier C to optional or conditional domains first (65, 61) before assigning Tier C to core domains (60, 62, 63, 64). Tier C authors produce 2,500–3,500 word documents (vs. 6,000–10,000 for Tier A/B); the publication is labelled as a "community primer" rather than a full research guide.

**Reduced scope for Tier C assignment**:
- Word count: 2,500–3,500 (not 6,000–10,000)
- Citations: 25 minimum (not 40+)
- Sections: 4 required (Foundation, Landscape, Pathways, Summary) — skip Implementation deep-dive
- Timeline: Same June 20 start, August 20 target
- Peer review: Assign two reviewers per WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md Part 4

### Domain Reassignment Logic

**If 1 gap domain is identified**:

| Gap Domain | Reassignment Decision |
|-----------|----------------------|
| Domain 65 (Institutional Learning) | Defer to Wave 3 (August). Non-critical for June 20 launch. Note in onboarding communications: "Domain 65 primer targeted for Wave 3 release August 20." |
| Domain 61 (Intergenerational Knowledge) | Defer to Wave 3 OR assign Tier C backup if available. This domain has the most tractable scope reduction. |
| Domain 60 (International Coordination) | Required. Activate Tier B backup. If no Tier B: reduce scope to co-authored primer with Tier C + orchestrator content synthesis. |
| Domain 62 (Infrastructure Interdependencies) | Required. Activate Tier B backup. No Tier C path — this domain requires practitioner expertise that Tier C authors rarely have. If no Tier B → Scenario C assessment. |
| Domain 63 (Ecosystem Restoration) | Required. Activate Tier B backup. Tier C path possible but requires project lead spot-check of technical claims. |
| Domain 64 (Community Economic Resilience) | Required. Activate Tier B backup. Tier C path possible with additional editorial support. |

**If 2 gap domains are identified**:
- If both are optional/conditional (65, 61): Defer both. 4-domain launch.
- If one is required: Apply single-gap logic to required domain; defer optional/conditional.
- If both are required: Route to Scenario C.

### Timeline Impact Assessment

| Scenario B Configuration | June 20 Launch | Wave 3 Domains | Quality Gate Risk |
|--------------------------|----------------|----------------|-------------------|
| 5 confirmed + 1 Tier B backup (day-of) | On schedule | 0 | Low |
| 5 confirmed + 1 Tier C backup | On schedule | 0 | Medium — extra peer review |
| 5 confirmed + 1 deferred domain | On schedule | 1 (Domain 65) | Low |
| 4 confirmed + 2 deferred domains | On schedule | 2 (65, 61) | Low |
| 4 confirmed + 1 required backup + 1 deferred | On schedule | 1 | Medium |

**Day 7 check (June 27)**: If Scenario B launch included a Tier C author or a backup author onboarded June 14–15 (compressed timeline): check T+7 checkpoint carefully. If Day 7 checkpoint shows ≥15% behind schedule for any author → activate Tier-3 editorial support protocol (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md Part 5) immediately. Do not wait for T+14.

### Notification Template B-1: Tier B Backup Activation (June 13–14)

```
Subject: Wave 2 Author — Domain [XX] Opening, June 20 Start (48h Confirmation Window)

Hi [Backup Author First Name],

We have a confirmed opening for the [Domain Name] Wave 2 author slot. Our primary 
candidate has not confirmed by our deadline, and we'd like to offer you the position 
based on your background in [specific area].

What this involves:
- Domain: [Domain Name] — [one-sentence scope]
- Tier: [B or C] — [word count target]: [XX,XXX]–[XX,XXX] words | [XX]+ citations | 
  [X]–[X] hrs/week for 8 weeks
- Platform: [Platform name] — OR Google Drive (your choice, both supported)
- Timeline: Onboarding June 15, sprint start June 20, final delivery August 20
- Peer reviewer: Assigned June 14 — you'll review one other author's work; one author 
  reviews yours
- Attribution: CC-BY 4.0 open license, your byline as primary author

I need a confirmation by [DATE, June 14 or 15] at [17:00 UTC] to finalize the roster 
before our June 14 author matching session.

If you're available: reply "confirmed" and I'll send your full onboarding package 
(scope document, annotated bibliography, platform access) within the hour.

If you're not available for this wave: no problem — I'll note you for Wave 3 (August).

Thanks for considering this on short notice,
[Project Lead Name]
[Email]
```

### Notification Template B-2: Domain Deferral Announcement (to confirmed authors)

```
Subject: Wave 2 Roster Update — [Domain XX] deferred to Wave 3; your sprint unchanged

Hi [Confirmed Author First Name],

Quick update on the Wave 2 roster before your June 20 sprint start:

Domain [XX] ([Domain Name]) will be deferred to Wave 3 (August launch) due to 
unavailability of the recruited author for this sprint. This does not affect your 
domain assignment, your timeline, or your peer reviewer pairing.

Your sprint is fully on track:
- June 20: T+0 kickoff (unchanged)
- June 27: T+7 checkpoint (unchanged)
- August 20: Delivery (unchanged)
- Peer reviewer: [Name], Domain [XX] (unchanged)

The Wave 3 cohort targeting August 20 will include Domain [XX] and potentially 
one additional domain from the Wave 3 candidate pool.

No action needed from you — just wanted to keep you informed on the full roster.

Looking forward to June 20,
[Project Lead Name]
```

---

## Scenario C: Three or More Author Dropouts

**Condition**: 3 or more confirmed authors have gone dark or declined by June 13 EOD, leaving fewer than 4 confirmed Tier A/B authors for the June 20 launch.

This scenario has two response paths. The Go/No-Go decision between them is made by the project lead at the June 14 matching session using the criteria below.

### Decision Tree

```
Confirmed Tier A/B authors ≤ 3 as of June 13 EOD?
  YES →
    Can domains 60, 62, 63, AND 64 (4 required domains) be staffed with confirmed authors?
      YES → 4-domain launch is viable.
              All 4 required domains staffed AND June 20 timeline maintained?
                YES → Response Path 1: Launch 4 required domains June 20. Defer 65 and 61 to Wave 3.
                NO (one required domain still unconfirmed) → Route to Response Path 2 assessment.
      NO (1+ required domains have no confirmed author) →
        Response Path 2: Consolidate OR defer.
        Can 5 remaining domains form 3 co-authored units?
          YES → Assess consolidation: see domain groupings below.
                 Co-author pairing confirmed by June 14? → Consolidated launch June 20 (PATH B)
                 Co-author pairing not confirmed? → Defer entire Wave 2 to July 15 (PATH C)
          NO (insufficient roster for co-authorship consolidation) → Defer entire Wave 2 to July 15 (PATH C)
```

### Response Path 1: Defer Domain 65 to Wave 3, Launch 4 Required Domains June 20

**Trigger**: Domains 60, 62, 63, 64 all have confirmed Tier A/B authors. Domains 65 and/or 61 lack confirmed authors.

**Action**:
- Confirm the 4 required domains' authors are ready for June 20 start
- Formally defer Domain 65 to Wave 3 (August 20 launch)
- Formally defer Domain 61 to Wave 3 if unconfirmed (or reduce to Tier C track if a backup is available)
- Notify all confirmed authors with Template C-1

**This is still a successful Wave 2 launch** — 4 of 6 domains is within Path B criteria (WAVE_2_GO_NO_GO_DECISION_GATE_JUNE14.md). Do not frame this as a failure in communications.

### Response Path 2: Consolidate into 3 Co-Authored Units

**Trigger**: One or more required domains (60, 62, 63, 64) lack a confirmed sole author. At least 3 confirmed authors are available.

**Consolidation groupings** (based on domain adjacency from WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md Part 1):

| Unit | Domains | Rationale | New scope |
|------|---------|-----------|-----------|
| Unit 1: Governance + Learning | 60 + 65 | International coordination and institutional learning share governance theory | Co-author writes governance layer; second author writes learning and adaptation layer |
| Unit 2: Material Systems | 62 + 63 | Infrastructure interdependencies and ecosystem restoration share material-systems-under-constraint framing | Co-author writes infrastructure resilience layer; second author writes ecological restoration layer |
| Unit 3: Economic + Intergenerational | 64 + 61 | Community economic resilience and intergenerational knowledge transmission share cooperative and community-of-practice theory | Co-author writes economic systems layer; second author writes skill transmission and knowledge architecture layer |

**Co-authored document structure**: Each consolidated unit produces one document (12,000–18,000 words) with two named authors, clear section authorship attribution, and a unified introduction and summary written by the project lead.

**Risk**: Scope and coherence management across two authors is the primary coordination cost. Each co-author pair needs a 45-minute scope alignment call before June 20.

**Timeline impact**: Co-authored units have a July 11 full draft deadline (vs. July 4 for solo authors) to account for the coordination overhead. August 20 final delivery is unchanged.

**Viability condition**: This path requires 3 confirmed authors who (a) are willing to co-author and (b) have overlapping availability for a June 15–17 scope alignment call. If any confirmed author declines co-authorship, route to PATH C (full deferral).

### Go/No-Go for Scenario C: Core 4 Domains Check

**The single binary question** (answered at June 14 14:00 UTC):

> Can domains 60, 62, 63, and 64 each have at least one confirmed Tier A, B, or active Tier C author by June 14 EOD?

| Answer | Decision | Next step |
|--------|----------|-----------|
| YES — all 4 core domains staffed | PATH A or B — launch June 20 | Use Response Path 1 (defer 65, optionally 61) |
| YES — via co-authorship consolidation | PATH B — launch June 20 (consolidated) | Use Response Path 2 (3 co-authored units) |
| NO — <4 confirmed even with all available backups | PATH C — defer to July 15 | Send Template C-3 (full deferral). Begin extended recruitment window. |

### Domain Reassignment Logic for Scenario C

**Required domains (60, 62, 63, 64)**: Exhaust all backup options before deferring. Sequence:
1. Named Tier B backup (from PHASE_6_AUTHOR_RECRUITMENT_TRACKING.md)
2. Tier C backup if Tier B unavailable (reduced scope)
3. Orchestrator co-author for reduced-scope primer (project lead commits 20–25 hours)
4. Only defer if all 3 options are unavailable or declined

**Optional domain (65)**: Defer to Wave 3 without exhausting backups if roster is already under stress. Domain 65 (Institutional Learning) is the most theory-dense domain and tolerates a Wave 3 release without timeline damage to the Wave 2 corpus.

**Conditional domain (61)**: Defer to Wave 3 if roster is tight, or reduce to Tier C primer if a capable backup is available. Domain 61 (Intergenerational Knowledge) has the most tractable scope-reduction path.

### Notification Template C-1: 4-Domain Launch Announcement

```
Subject: Wave 2 Launch Update — 4 Domains June 20, 2 Domains to Wave 3

Hi [Confirmed Author First Name],

I want to update you on the Wave 2 roster before your sprint starts June 20.

We are launching Wave 2 with 4 domains on June 20:
- Domain [XX]: [Domain Name] — [Author Name]
- Domain [XX]: [Domain Name] — [Author Name]
- Domain [XX]: [Domain Name] — [Author Name]
- Domain [XX]: [Domain Name] — [Author Name]

Domains [XX] and [XX] ([Domain Names]) have been deferred to Wave 3 (August 20 launch) 
due to author availability constraints. The quality gate standard remains unchanged — 
we are launching with the authors who are confirmed and prepared, not rushing incomplete 
author recruitment.

Your sprint is fully unchanged:
- June 20: T+0 kickoff
- August 20: Final delivery
- Peer reviewer: [Name], Domain [XX]

Wave 3 is targeted for an August 20 publication date with an extended recruitment window 
starting June 20. The two deferred domains will benefit from a fuller recruitment 
process and should produce stronger documents for it.

See you June 20,
[Project Lead Name]
```

### Notification Template C-2: Co-Authorship Consolidation Proposal

```
Subject: Wave 2 Co-Authorship Proposal — Domains [XX] + [XX] (48h Response)

Hi [Author First Name],

Given our author roster, I'd like to propose a co-authorship structure for Wave 2 
that I think will actually produce a stronger document than a solo effort.

The proposal: You and [Co-Author Name] co-author a single unified document covering 
[Domain XX: Domain Name] + [Domain XX: Domain Name]. These two domains share 
[specific conceptual link — e.g., "governance theory and institutional learning"], 
and a unified treatment would eliminate the awkward cross-domain bridges that two 
separate documents would need to manage.

What this means in practice:
- You own sections [X, Y, Z] (your primary domain)
- [Co-Author Name] owns sections [A, B, C] (their primary domain)
- Shared sections (introduction, Zone 5 application, summary) are written together 
  or with project lead support
- Timeline: Full draft by July 11 (one week later than solo track, to account for 
  coordination); August 20 delivery unchanged
- Attribution: Both named as primary co-authors, section-level attribution noted

We would need a 45-minute scope alignment call June 15–17. I can organize it 
around your availability.

Would you be willing to proceed on this basis? Please let me know by [DATE, 48h] 
so we can finalize the June 14 roster.

[Project Lead Name]
```

### Notification Template C-3: Full Deferral to July 15

```
Subject: Wave 2 Deferred to July 15 — Next Steps and New Timeline

Hi [Author Name],

After completing our June 14 author matching session, we do not have a minimum viable 
roster to launch Wave 2 on June 20. We are deferring the Wave 2 launch to July 15, 2026.

This decision reflects our quality gate standard (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md): 
we will not launch with fewer than 4 confirmed authors, and we will not compress onboarding 
in ways that compromise the practitioner utility of the final documents.

What this means for you:

If you have confirmed for Wave 2:
Your authorship commitment is preserved. Your revised sprint timeline:
- July 1: Revised onboarding package delivery
- July 7: Author confirmation deadline (re-confirm or release)
- July 15: Sprint start (T+0)
- August 22: T+7 checkpoint
- September 5: T+21 full draft
- October 5: Final delivery

The extended timeline gives us 4 weeks for a more thorough recruitment process and 
more onboarding preparation time for the authors we do have.

If you need to withdraw due to July timing: please let me know by June 20 so we can 
plan the July recruitment accordingly.

I'll send a full revised timeline and July onboarding package by June 21.

Thank you for your patience and continued interest in this project,
[Project Lead Name]
```

---

## Scenario D: Slow Responder Critical Path

**Condition**: 50% or more of Tier A authors have not responded by June 11 (Day 3 post-send), even though none have explicitly declined. This is the "going dark" scenario — not rejection, but silence that makes the timeline non-viable if activation is delayed.

**This scenario activates before June 14.** Do not wait for the matching session to act on Scenario D.

### Decision Tree

```
June 11 08:00 UTC monitor check:
  Tier A response rate < 50% (≥3 of 6 Tier A have status = SENT/OPENED/NO_RESPONSE)?
    YES → Scenario D activated immediately.
    NO → Continue standard monitoring. Check again June 12.

Scenario D activated:
  Action 1: Send Template B (re-engagement) to ALL non-responding Tier A simultaneously (not sequentially).
  Action 2: Contact Tier B backups for ALL non-responding Tier A domains SIMULTANEOUSLY.
             Use Template B-1 (backup activation). State: "We are running parallel tracks."
  Action 3: Email project lead: "Scenario D activated [timestamp]. Tier B parallel recruitment live 
             for [X] domains. Expect response by June 12 EOD."

June 12 EOD assessment:
  Re-engagement responses received from ≥ original Tier A count?
    YES → Combine Tier A confirmations + any Tier B confirmations. If total ≥ 6 → Scenario A.
           If total 4–5 → Scenario B.
    NO → Count confirmed Tier B activations.
           If Tier B activations ≥ 4 → Proceed as Scenario B (Tier B roster instead of Tier A).
           If total confirmed < 4 → Scenario C assessment.
```

### Parallel Recruitment Protocol

When Scenario D activates, Tier A re-engagement and Tier B activation happen simultaneously. This is not a violation of the standard sequential process — the timeline no longer permits sequential activation.

**Parallel track management**:
- Log both contacts in `recruitment_tracking_log.csv` (Tier A original and Tier B backup)
- If both respond positively: confirm Tier A (preferred). Release Tier B with Template D-3 (below).
- If only Tier A responds: confirm Tier A. Inform Tier B backup that slot is filled (Template D-3).
- If only Tier B responds: confirm Tier B. Continue one additional re-engagement attempt with Tier A.
- If neither responds by June 12 EOD: move to Scenario C assessment for that domain.

### Escalation to Project Lead (Template D-1)

```
Subject: Scenario D Activated — Tier B Parallel Recruitment Live (June 11)

[Project Lead Name],

Scenario D (≥50% Tier A no-response by Day 3) activated as of [timestamp] UTC.

Current status:
- Tier A responses received: [X]/[total] (expected: [total])
- Tier A no-response (status: SENT/OPENED after 3 days): [domains]
- Tier B parallel activation started: [timestamp]
- Domains with parallel recruitment active: [domain list]

Actions taken:
1. Re-engagement emails (Template B) sent to: [author names/domains]
2. Tier B backup contacts sent (Template B-1) to: [backup names/domains]

Decision needed from you:
- Can onboarding happen June 13–14 instead of June 15 if we confirm Tier B authors by June 12?
  (This compresses onboarding by 1 day but keeps June 20 sprint start intact.)
- If yes: I will schedule onboarding package delivery for June 13 and confirm with Tier B authors.
- If no: Target onboarding June 15; accept 1-day sprint slip (T+0 = June 21).

Please confirm by June 12 12:00 UTC.

[Coordinator Name]
```

### Timeline Impact Assessment

| Scenario D Outcome | June 20 Launch | Quality Risk | Mitigation |
|-------------------|----------------|--------------|------------|
| Tier A re-engages June 12 → 6 confirmed | On schedule | Low | Standard onboarding June 15 |
| Tier B confirms June 12 → 4–5 confirmed | On schedule | Medium (Tier B mix) | Compressed onboarding June 13–14; extra T+3 check-in |
| Only 3 confirmed by June 12 | At risk — Scenario C | High | Go/No-Go at June 14 matching session |
| <3 confirmed by June 12 | PATH C likely | — | See Scenario C, full deferral path |

**1-day slip risk**: If Tier B authors are confirmed June 12 and onboarding compresses to June 13–14 instead of June 15, the T+7 checkpoint (June 27) becomes T+6 (June 26). This is a minor schedule adjustment, not a quality risk. Notify affected Tier B authors of the compressed onboarding timeline with Template D-2.

### Template D-2: Compressed Onboarding Notification

```
Subject: Wave 2 Onboarding Package — Earlier Delivery (June 13 instead of June 15)

Hi [Author First Name],

Good news: you've been confirmed for the Wave 2 author roster.

Due to a slightly compressed confirmation timeline, I'm sending your onboarding 
package on June 13 (two days earlier than the standard June 15 date). This gives 
you more preparation time before the June 20 sprint start — not less.

Your onboarding package is attached:
1. Domain scope document ([Domain Name])
2. Annotated bibliography ([XX] sources)
3. Platform access: [instructions]
4. Peer reviewer: [Name], Domain [XX]

Please confirm receipt and platform access by June 16. Sprint starts June 20 as planned.

No changes to your timeline, word count target, or deliverables.

Looking forward to working with you,
[Project Lead Name]
```

### Template D-3: Releasing a Parallel-Recruited Author (Tier A Confirms)

```
Subject: Wave 2 — Slot Filled, Thank You

Hi [Backup Author First Name],

Thank you for your quick response to our Wave 2 opening for Domain [XX].

I'm writing to let you know that our primary author for this domain has confirmed 
availability, so the slot is now filled. I want to thank you for your willingness 
to step in on short notice — it's genuinely helpful to know the project has a 
community of people willing to engage this way.

I'll keep your contact information for Wave 3 (August launch), which will have 
openings in domains [XX] and potentially others.

Thanks again,
[Project Lead Name]
```

---

## Scenario E: Platform Unavailability

**Condition**: As of June 15 (the day before sprint start), Nextcloud + Matrix infrastructure is not confirmed ready. This could mean: server unreachable, Matrix federation issues, author access not provisioned, or Tailscale VPN connectivity problem for external authors.

**This scenario has a pre-built resolution (Item 64) that requires zero decision-making.** The Google Drive fallback is production-ready. The only action is notification.

### Decision Tree

```
June 14 14:00 UTC: Confirm Nextcloud+Matrix status.
  Platform confirmed ready (all 6 author folders provisioned, Matrix rooms live)?
    YES → Standard onboarding. No Scenario E action needed.
    NO →
      Is this a temporary outage (ETA for resolution within 24 hours)?
        YES → Delay onboarding package delivery by 24 hours. Notify authors (Template E-1).
               Monitor June 15 08:00 UTC for resolution.
               June 15 still unresolved → Activate Google Drive fallback (Template E-2).
        NO (>24 hours ETA or unknown) → Activate Google Drive fallback immediately (Template E-2).
                                         No further assessment needed.
```

### Platform Status Check (June 14 14:00 UTC)

**Nextcloud check** (run on raspby1):
```bash
curl -s -o /dev/null -w "%{http_code}" https://100.70.184.84/nextcloud/status.php
# Expected: 200. Anything else → platform issue.
```

**Matrix check**:
```bash
curl -s -o /dev/null -w "%{http_code}" https://100.70.184.84/_matrix/client/versions
# Expected: 200. Anything else → Matrix issue.
```

**Author folder check** (sample):
```bash
# Verify one author's folder is provisioned
# Log in to Nextcloud admin and confirm Phase5-Wave2-[Domain]/ exists for each author
```

**Resolution threshold**: If any of the three checks fail and the cause is not clear within 2 hours of investigation → activate Google Drive fallback. Do not wait for a root cause fix.

### Google Drive Fallback Activation

The Google Drive fallback (Item 64, JUNE_5_15_CONTINGENCY_OFFLINE_ONBOARDING.md) is production-ready. Activation steps:

1. Create a Google Drive folder structure: `Wave 2 Phase 6 / [Domain Name] / [Author Name]/`
2. Upload scope document, annotated bibliography, and DRAFT-[domain].md template to each author's folder
3. Set sharing permissions: "Anyone with link can edit" — OR use author's Gmail for direct share
4. Send Template E-2 with Google Drive links
5. Timeline impact: Zero. Google Drive fallback is functionally equivalent to Nextcloud for document collaboration.

### Notification Template E-1: Platform Delay (24-hour notice)

```
Subject: Wave 2 Onboarding — 24-Hour Delay on Platform Access

Hi [Author First Name],

Quick update: there is a temporary infrastructure issue with the [Nextcloud+Matrix / 
platform] that we're resolving. This does not affect your June 20 sprint start.

Revised onboarding schedule:
- Onboarding package delivery: June 16 (instead of June 15)
- Platform access: June 16
- Sprint start: June 20 (unchanged)
- All checkpoints: Unchanged

I'll send your complete onboarding package — including platform credentials — by 
June 16 12:00 UTC.

No action needed from you until June 16.

[Project Lead Name]
```

### Notification Template E-2: Google Drive Fallback Activation

```
Subject: Wave 2 Onboarding — Google Drive Platform (Updated Instructions)

Hi [Author First Name],

Your Wave 2 onboarding package is ready. We are using Google Drive for document 
collaboration in this sprint (instead of Nextcloud — infrastructure prep is still 
in progress on that side, and we didn't want to delay your onboarding).

Your workspace:
- Scope document: [Google Drive link — view/edit]
- Annotated bibliography: [Google Drive link — view]
- Working draft template: [Google Drive link — edit]
- Peer review exchange: Via your domain email thread (project lead CC'd)

How the Google Drive workflow functions:
1. Open your draft link and begin editing directly in Google Docs (no software install)
2. All communication happens via email or [Matrix/Discourse if available] — same as the 
   standard platform workflow
3. Submit checkpoints by sharing your draft link with project lead via email with 
   subject: "[Domain XX] T+7 checkpoint" (or T+14, etc.)

Timeline: Unchanged. Sprint start June 20. All checkpoints as planned.

Any questions: [PROJECT LEAD EMAIL]

[Project Lead Name]
```

**Timeline impact**: Zero. The Google Drive fallback requires no onboarding adjustment, no scope reduction, and no timeline slip. Scenario E is a communication task, not a decision task.

---

## Cross-Scenario Reference Table

| Confirmed by June 13 | Primary Scenario | Go/No-Go Path | Launch Date |
|---------------------|-----------------|---------------|-------------|
| 6 Tier A/B | A — Full Success | PATH A | June 20 |
| 5 Tier A/B | B — 1 Dropout | PATH B | June 20 (5 domains) |
| 4 Tier A/B | B — 2 Dropouts | PATH B | June 20 (4 domains) |
| 3 Tier A/B + viable co-auth | C — Response Path 2 | PATH B (consolidated) | June 20 |
| 3 Tier A/B, no co-auth | C — Full Deferral | PATH C | July 15 |
| <3 Tier A/B | C — Full Deferral | PATH C | July 15 |
| ≥50% Tier A dark by June 11 | D — Slow Responder | PATH B or C per June 12 EOD count | June 20 or July 15 |
| Platform unavailable June 15 | E — Platform Fallback | PATH A/B/C (unchanged, Google Drive) | June 20 (unchanged) |

---

## Quality Gate Integration

All contingency paths must maintain the quality gate standard from WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md (Item 78). The following quality adjustments apply per path:

| Path | Author Roster | Quality Gate Adjustment |
|------|--------------|------------------------|
| PATH A | 6 Tier A/B | Standard quality gate. 0 FAILs, ≤4 NEEDS-REVISION required. |
| PATH B (Tier B mix) | 4–5 Tier A/B | Standard quality gate. Tier B authors receive 1 additional T+3 check-in. |
| PATH B (Tier C backup) | One Tier C in roster | Tier C authors receive 2 peer reviewers (WAVE_2_PEER_REVIEW_PAIRING_PROTOCOL.md Part 4). Quality gate remains identical but review depth increases. |
| PATH C (deferred) | N/A — no June 20 launch | Quality gate applies to July 15 launch; no adjustment. Extended recruitment window should yield higher-tier authors. |

**The quality gate is not softened under any contingency path.** Documents that do not meet the 20-item peer review standard are not published, regardless of recruitment pressure. The contingency automation manages timeline and roster; it does not authorize publication of below-standard documents.

---

*Item 81 — Wave 2 Author Recruitment Contingency Automation*
*Version 1.0 — June 5, 2026*
*Companion files: RECRUITMENT_RESPONSE_TRACKING_AUTOMATION.md, WAVE_2_GO_NO_GO_DECISION_GATE_JUNE14.md*
