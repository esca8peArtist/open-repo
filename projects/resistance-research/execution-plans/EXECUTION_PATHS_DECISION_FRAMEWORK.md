---
title: "Phase 1 Distribution — Path Selection Framework"
created: 2026-04-30
session: 686
status: decision-ready
purpose: "One-page decision guide for choosing between Path A, Path A+37, and Path B"
companion_plans:
  - execution-plans/EXECUTION_PLAN_PATH_A.md
  - execution-plans/EXECUTION_PLAN_PATH_A_PLUS_37.md
  - execution-plans/EXECUTION_PLAN_PATH_B.md
---

# Phase 1 Distribution — Path Selection Framework

**Decision status**: All three paths are fully specified and ready to execute. The only remaining input is the user's path choice. Upon selection, the orchestrator executes immediately.

**Recommended path**: A+37 Hybrid. See Section 3 for the decision rule.

---

## 1. Path Comparison Table

| Dimension | Path A | Path A+37 Hybrid | Path B |
|-----------|--------|------------------|--------|
| **Time to Distribution** | 3–4 hours | 3–4h (Phase 1a) + 1–2h (Phase 1b, Day 1–3) | 14–28 days |
| **Domain Count at Launch** | 35 | 34 → 35 (staggered) | 42 |
| **Election Focus** | Domain 37 reaches all contacts simultaneously | Domain 37 goes to 12 election protection specialists with targeted framing | Domain 37 integrated throughout; distribution delayed |
| **April–May 2026 Updates** | All current updates integrated | All current updates integrated | FISA outcome + Iran scenario + circuit vacancies fully added |
| **Spring Legislative Windows** | Fully captured | Fully captured | Partially or fully missed |
| **NVRA August 7 Adoption Cycle** | Organizations have 7+ weeks margin | Organizations have 7+ weeks margin | 3–7 weeks margin (depending on timing) |
| **Complexity** | Single wave | Two waves, 1–3 day separation | Research phase + distribution phase |
| **Primary Use Case** | Rapid, integrated institutional activation | High-leverage election org outreach + general reach | Wait for May 2026 decision clarity before any distribution |
| **Recommended For** | Users with direct election-org relationships who prefer integrated sends | Most users — balances urgency with strategic targeting | Users with specific strategic reasons to delay |
| **Not Recommended If** | You want Domain 37 to reach election-protection specialists with targeted framing | (No disqualifying condition) | Election timing windows are a priority; spring sessions are still open |

---

## 2. Path-Specific Execution Documents

| Path | Execution Plan | Time Estimate | Decision Plan |
|------|---------------|---------------|---------------|
| A | `execution-plans/EXECUTION_PLAN_PATH_A.md` | 3–4 hours total | Execute Blocks 1–7 sequentially on Day 0 |
| A+37 | `execution-plans/EXECUTION_PLAN_PATH_A_PLUS_37.md` | 3–4h (Day 0) + 1–2h (Day 1–3) | Execute Phase 1a Blocks 1–6, then Phase 1b Blocks 7–9 |
| B | `execution-plans/EXECUTION_PLAN_PATH_B.md` | 14–28 days + 3–4h | Execute Phase B-1 (domain maintenance), then B-2 (integration), then B-3 (distribution) |

---

## 3. Decision Guide

**Choose Path A if**:
- You have established direct relationships with Democracy Docket, Campaign Legal Center, and state AG election protection staff — they can receive Domain 37 in a general 35-domain send and route it internally
- You prefer integrated framework coherence over phased sequencing
- Speed is the overriding constraint and you want a single send event
- Your primary channel is Substack publication rather than institutional outreach (general audience framing of the full 35-domain framework is an advantage)

**Choose Path A+37 if** (recommended):
- Your election protection contacts are not already personal relationships — targeted Domain 37 framing creates a stronger first impression than general distribution
- You want Domain 37 to reach election specialists with subject lines and body copy keyed to their specific litigation dockets (Democracy Docket case list, ACLU VRA Section 11(b), Protect Democracy HSGP analysis)
- You want the institutional momentum of a general Phase 1a send to compound Phase 1b's credibility — even a 24-hour gap between sends allows the election protection outreach to feel sequenced rather than cold
- The May 30 DOJ consent decree deadline and August 7 NVRA quiet period are high-priority advocacy windows you want to reach election protection organizations with actionable lead time

**Choose Path B if**:
- You have a strategic reason to delay not visible in the research record (pending publication partnership, specific contact timing, personal availability)
- Your primary audience is Senate Judiciary staffers or FISA-specialized litigators who would specifically flag post-May 1 currency gaps
- You want the framework to incorporate the definitive Iran WPR outcome and FISA 702 final vote before any contact sees it
- Comprehensiveness matters more than timing for your distribution goal

**Path B is not recommended if** the following are true (any one is sufficient):
- Spring legislative sessions are still open and ICE-at-polls model legislation could still be introduced
- You want organizations to be positioned before the May 30 DOJ consent decree deadline
- The 6–8 week institutional adoption cycle matters for the August 7 NVRA quiet period
- You can tolerate sending the current version (current through April 29) and updating contacts with post-May developments via a brief follow-up email

---

## 4. What Happens After You Decide

The orchestrator executes immediately upon receiving your path selection. No additional decisions are required before Batch 1 is sent.

**You will need to provide** (user-specific, not available in the research record):
- `{{YOUR_NAME}}` — your name for email sign-off
- `{{YOUR_CONTACT_INFO}}` — your email address, website, or phone for sign-off
- For each Batch 1 email: one recent publication from the contact's institution (5–10 minutes of research per contact, e.g., visit justsecurity.org and pick the most relevant recent article for Ryan Goodman)

**Everything else is already prepared**:
- All 6 canonical Gists are live (Session 678)
- All 5 Batch 1 email templates are ready with `{{placeholder}}` fields
- All URL replacements are mapped in `DISTRIBUTION_GIST_URLS.md`
- Batch 1 contacts are position-verified as of April 29, 2026
- Domain 37 contact list (12 election protection orgs) is in `DOMAIN_37_SEQUENCING_PLAN.md`

---

## 5. Risk Register by Path

| Risk | Path A | Path A+37 | Path B |
|------|--------|-----------|--------|
| Domain 37 reaches general audience without election-specialist framing | Yes — by design | Mitigated — Domain 37 sent with targeted framing | No — Domain 37 sent to all contacts at launch with updated content |
| Spring legislative session windows missed | No | No | High risk if Path B takes >14 days |
| August 7 NVRA adoption cycle compressed | No (7+ weeks) | No (7+ weeks) | Possible if Path B takes >21 days |
| FISA/Iran content not updated before contacts see it | Yes — non-blocking (current through April 29) | Yes — non-blocking | No — updates fully integrated |
| Two-wave complexity and tracking overhead | No | Minor — two send events, 1–3 days apart | No — single send event after research phase |
| Post-May 1 developments make existing domains look stale | Low risk — framework designed for monthly iteration | Low risk | None — framework is updated before launch |

---

## 6. Immediate Execution Command

When you have decided, communicate your path selection in one of the following forms:

- "Execute Path A" → Agent runs `EXECUTION_PLAN_PATH_A.md` Blocks 1–7
- "Execute Path A+37" → Agent runs `EXECUTION_PLAN_PATH_A_PLUS_37.md` Phase 1a Blocks 1–6, then Phase 1b Blocks 7–9
- "Execute Path B" → Agent begins Phase B-1 domain maintenance in priority sequence

No further clarification will be needed. All three plans are fully specified.

---

*This document is a decision aid only. The operative plans are in the three `EXECUTION_PLAN_*.md` files in this directory. For deeper analysis of path trade-offs, see `DISTRIBUTION_PATH_ANALYSIS.md`.*
