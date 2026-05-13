---
title: "Phase 1 Distribution Readiness — All Three Paths (A / A+37 / B)"
created: 2026-05-13
status: production-ready — path decision pending
scope: >
  Comprehensive pre-decision readiness document. Covers domain inventories,
  Gist structures, contact groups, Week 1–4 timelines, and dependency mapping
  for all three paths. Integrates Domain 42 DEA deadline analysis. Provides
  Path A+37 execution time estimate and pre-launch actions that can be taken
  NOW without a path decision.
reference_sources:
  - PHASE_1_EXECUTION_READINESS.md
  - PHASE_1_DISTRIBUTION_EXECUTION_BLUEPRINT.md
  - execution-plans/EXECUTION_PATHS_DECISION_FRAMEWORK.md
  - execution-plans/EXECUTION_PLAN_PATH_A_PLUS_37.md
  - execution/domain-42-contact-list.md
  - execution/domain-42-may-28-outreach-plan.md
  - execution/phase-1-contact-verification-checklist.md
  - execution/phase-1-gist-creation-playbook.md
  - execution/phase-1-distribution-setup-checklist.md
  - DISTRIBUTION_GIST_URLS.md
---

# Phase 1 Distribution Readiness — All Three Paths

**Prepared**: May 13, 2026  
**Path decision status**: Pending user selection  
**Domain 42 DEA deadline**: May 28, 2026 — INDEPENDENT of path decision (execute regardless)  
**Overall readiness**: APPROVED FOR IMMEDIATE LAUNCH on any path

---

## EXECUTIVE FINDING

Path A+37 can be launched by **May 14, 2026 (Wednesday), with first emails sent by 6:00 PM**, pending only these user actions:

1. Confirm your name and contact information (fills `{{YOUR_NAME}}` / `{{YOUR_CONTACT_INFO}}`)
2. Create the Domain 42 Gist (10 minutes; instructions at `execution/domain-42-gist-creation-steps.md`)
3. For each of the 5 Batch 1 contacts: note one recent publication from their institution (5–10 minutes each)
4. Confirm sending email address and verify it is not blocklisted (`mxtoolbox.com/blacklists.aspx`)

Everything else is staged and ready. Total execution time from path decision to first email send: **3.5–4 hours**.

---

## DELIVERABLE 1: Distribution Readiness Checklist by Path

---

### PATH A — Immediate Full Distribution (35 domains)

**Philosophy**: Single-wave launch. All 35 domains distributed to all contacts. Domain 37 reaches election protection organizations in the same general send as everyone else.

#### Domains Included

Path A distributes the complete 35-domain framework. All Phase 1 core domains plus all Phase 2/3 expansions that are production-ready.

**Core 35 domains (consolidated in main proposal Gist)**:

The main proposal Gist at `https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261` contains all 35 domains. The standalone domain files in `/domains/` provide supplemental depth but are not sent individually in Path A — contacts receive the main proposal link.

**Additionally distributed as standalone Gists** (all 6 already live):

| Document | Gist URL | Purpose |
|----------|----------|---------|
| Democratic Renewal Proposal | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | Primary send artifact |
| Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | 2-page entry point |
| Litigation Tracker 2026 | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | Companion reference |
| First Amendment Suppression | https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c | Companion reference |
| Environmental Rollbacks | https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4 | Companion reference |
| Police Consent Decree | https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731 | Companion reference |

**New Gist required for Path A** (1 Gist, create Day 0):
- Domain 42 standalone Gist (source: `domains/domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md`)
- Zone A/D wrapper instructions: `execution/domain-42-gist-creation-steps.md`
- Estimated creation time: 10 minutes

**Gist zone structure for Domain 42 (all paths)**:
- Zone A: Standalone domain header block (title, framework context, DEA deadline callout)
- Zone B: Context paragraph linking to main proposal Gist
- Zone D: Footer — advocacy windows table (May 28 filing deadline; June 29 hearing; July 15 hearing close; Section 591 congressional block risk)

#### Contact Groups — Path A

| Wave | Tier | Count | Groups | Send Window |
|------|------|-------|--------|-------------|
| Batch 1 | Tier 1 — Top 5 | 5 | Just Security, Brennan Center, Harvard Kennedy School, Protect Democracy, Democracy Docket | Day 0 |
| Batch 2 | Tier 1 remaining | 9 | Think tanks, law schools, policy institutes | Days 6–14 |
| Batch 3 | Tier 1 + Tier 2 | 10 | Labor/civil society, state-level orgs | Days 15–21 |
| Domain 42 sub-batch | Separate track | 10 | Drug policy reform orgs, civil rights orgs, academic, state AGs | May 8–21 (INDEPENDENT) |
| Total Phase 1 | — | 34 | General outreach + Domain 42 parallel track | Days 0–21 |

**Domain 37 routing in Path A**: Domain 37 is embedded in the main proposal. Election protection organizations (Brennan Center, Democracy Docket, Protect Democracy — all in Batch 1) receive it with the same framing as all other contacts. No targeted Domain 37 email.

#### Path A Week 1–4 Timeline

| Period | Actions |
|--------|---------|
| Day 0 (May 14) | Gist verification; template fill; Batch 1 send (5 emails); Domain 42 Category A wave if not yet sent |
| Days 1–5 (May 15–19) | Post Twitter Thread 1; r/law Reddit post; Wave 2 personalization; Domain 42 Category B/C waves |
| Days 6–14 (May 20–28) | Wave 2 send (9 contacts); Domain 42 state AG wave; May 28 DEA deadline |
| Days 15–21 (May 29–June 4) | Wave 3 send (10 contacts); Substack posts 3–4; OSF application deadline (June 4) |

#### Path A Dependencies

**User must provide before Day 0**:
- `{{YOUR_NAME}}` and `{{YOUR_CONTACT_INFO}}` for email sign-offs
- One recent publication per Batch 1 contact (5 contacts × 5–10 min = 30 min)
- Sending email address confirmed and verified not blocklisted
- GitHub logged in as `esca8peArtist` for Domain 42 Gist creation

**Infrastructure already complete (no user action needed)**:
- 6 canonical Gists live and verified (Session 678, April 30)
- All templates filled with Gist URLs via `fill_templates.py`
- All 5 Batch 1 contacts position-verified as of April 29, 2026
- Domain 42 outreach plan fully staged (`execution/domain-42-may-28-outreach-plan.md`)

---

### PATH A+37 HYBRID — Recommended Path

**Philosophy**: Two-wave launch. Phase 1a distributes the 34-domain general framework (excluding Domain 37) to all contacts. Phase 1b distributes Domain 37 as a standalone targeted send to 12 election protection specialists, Days 1–3 after Phase 1a.

#### Domains Included

**Phase 1a (34 domains, Day 0)**: Main proposal Gist minus Domain 37. All 5 Batch 1 contacts receive the `[PATH A+37]` paragraph block noting that Domain 37 is being distributed separately to election protection contacts.

**Phase 1b (Domain 37 standalone, Days 1–3)**: Domain 37 standalone Gist sent to 12 election protection organizations with targeted framing.

**The distinction from Path A**: The main proposal Gist already contains Domain 37. What changes in Path A+37 is not the content available to contacts — it is the framing. Election protection organizations get a separate email leading with Domain 37 and connecting it explicitly to their current active litigation. This creates a higher probability of immediate use than Domain 37 landing mid-document in a 35-domain framework.

**New Gists required for Path A+37** (2 Gists, create Day 0):

| Gist | Source File | Estimated Time | Notes |
|------|------------|----------------|-------|
| Domain 42 standalone | `domains/domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md` | 10 min | Zone A/D structure; required for all paths |
| Domain 37 standalone | `domains/domain-37-federal-executive-interference-2026-midterms.md` | 10 min | Includes Advocacy Windows table (May 30 / June 30 / August 7 / Sept / Oct) as Zone D footer |

**Zone D footer block for Domain 37 Gist** (paste verbatim):
```
---

## Advocacy Windows — 2026 Midterm Timeline

| Date | Window | Action Needed |
|------|--------|---------------|
| May 30, 2026 | DOJ consent decrees finalized or challenged | Legal challenge and public pressure positioning |
| June 30, 2026 | Emergency EO routing window | OMB/legal review challenge opportunity |
| August 7, 2026 | NVRA 90-day quiet period begins | Pre-filed emergency injunction templates required |
| September 2026 | Pre-election litigation positioning | Section 3 disqualifications, voter roll restoration |
| October 2026 | Poll observer deployment | Legal hotline readiness, real-time election monitoring |

*This is a standalone excerpt from Domain 37 of the 35-domain Democratic Renewal Research framework.*
*Full proposal: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261*
```

#### Contact Groups — Path A+37

| Wave | Tier | Count | Groups | Send Window |
|------|------|-------|--------|-------------|
| Phase 1a Batch 1 | Tier 1 — Top 5 | 5 | Just Security, Brennan Center, Harvard Kennedy School, Protect Democracy, Democracy Docket | Day 0 |
| Phase 1b Tier 1 | Election protection specialists | 7 | Brennan Center (Domain 37 follow-up), Democracy Docket (Domain 37 follow-up), Protect Democracy (follow-up), Lawyers' Committee VRP, ACLU Voting Rights Project, States United Democracy Center, Common Cause | Day 1 |
| Phase 1b Tier 2 | State election networks | 5 | Per `DOMAIN_37_SEQUENCING_PLAN.md` Tier 2 contacts | Day 2 |
| General Batch 2 | Tier 1 remaining | 9 | Think tanks, law schools | Days 6–14 |
| General Batch 3 | Tier 1 + Tier 2 | 10 | Labor/civil society, state-level | Days 15–21 |
| Domain 42 sub-batch | Separate parallel track | 10 | Drug policy, civil rights, academic, state AGs | May 8–21 (INDEPENDENT) |
| Total Phase 1 | — | 46 | All tracks combined | Days 0–21 |

**Note on Weiser/Elias/Bassin**: These three contacts appear in both Phase 1a (Batch 1) and Phase 1b. This is by design — two different emails, two different framings. Phase 1b is not a duplicate. Opening framing for Phase 1b: "Following up on the 35-domain framework I sent earlier today / yesterday — I wanted to send Domain 37 directly given your organization's specific work on [active case or litigation]."

#### Path A+37 Week 1–4 Timeline

| Period | Phase 1a Actions | Phase 1b Actions | Domain 42 Track |
|--------|-----------------|-----------------|-----------------|
| Day 0 (May 14) | Gist verification; create Domain 42 + Domain 37 Gists; template fill; Batch 1 send (5 emails) | Prepare 12 Phase 1b emails; check most recent docket update per org | Category A wave if not yet sent (DPA, NORML, ACLU CLR, Sentencing Project, LEAP, SSDP) |
| Day 1 (May 15) | Twitter Thread 1 post; check bounces; begin Wave 2 personalization | Send 7 Tier 1 Phase 1b emails (14:00–16:45, 15-min spacing) | Category B wave: NAACP LDF, Prison Policy Initiative; Category C: Mason Marks |
| Day 2 (May 16) | r/law Reddit post; continue Wave 2 personalization | Send 5 Tier 2 Phase 1b emails | Category C: Ohio State Moritz DEPC; MPP |
| Day 3 (May 17) | Substack Post 1 publishes | Phase 1b complete; log all 12 sends | Category D: State AG wave (CO, CA, MI, WA) |
| Days 4–5 (May 18–19) | Twitter Thread 2; r/PoliticalScience Reddit | Check Phase 1b bounces | Check Wave 1 responses; apply follow-up trigger if needed |
| Days 6–14 (May 20–28) | Wave 2 send (9 contacts); r/electionreform Reddit | Monitor Phase 1b engagement signals; send follow-up to non-responders by Day 10 | May 21: Final Domain 42 reminder wave. May 28: DEA deadline — log who filed |
| Days 15–21 (May 29–June 4) | Wave 3 send (10 contacts); Substack Posts 3–4 | Month 1 assessment — which Phase 1b orgs are engaging Domain 37? | Post-deadline tracking: check DEA-1362 docket for participant list |

#### Path A+37 Dependencies

**User must provide before Day 0**:
- `{{YOUR_NAME}}` and `{{YOUR_CONTACT_INFO}}`
- One recent publication per Batch 1 contact (30 min total)
- One active case/campaign per Phase 1b election protection org (5–10 min per org; 7 Tier 1 orgs = 35–70 min — can be done in parallel with Day 0 setup)
- Sending email address verified not blocklisted

**Infrastructure already complete**:
- 6 canonical Gists live (Session 678)
- Domain 37 file production-ready (`domains/domain-37-federal-executive-interference-2026-midterms.md`, 89 KB, current through May 7)
- Domain 42 file production-ready (`domains/domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md`, 55 KB, current through May 7)
- All Phase 1b subject lines pre-written (`execution-plans/EXECUTION_PLAN_PATH_A_PLUS_37.md` Section 4, Block 8)
- Domain 42 outreach plan fully staged (10 organizations, 3-wave sequence, follow-up protocol)
- `fill_templates.py` script ready to run

---

### PATH B — Research Extension Then Distribution

**Philosophy**: Add 7 Phase 2 research domains first (14–21 days), then execute a modified Path A calendar with 42 total domains. Highest content completeness. Highest timing risk relative to spring legislative sessions and May 30 advocacy window.

#### Domains Included at Launch

Path B adds 7 domains to the existing 35 before distributing. The 42-domain framework at launch includes everything in Path A plus:

1. Domain 44 (Labor Rights / NLRB Crisis) — complete as of Session 930
2. Domain 44 alt (Reproductive Freedom) — complete as of Session 930
3. Domain 45 (Climate Policy Rollback) — research in progress
4. Domain 46 (Federal Research Policy) — research in progress
5. Domain 47 (Housing Security) — complete as of Session 929
6. Domain 48 (Surveillance Capitalism / Electoral Manipulation) — research in progress
7. Domain 49 (Callais / VRA / Redistricting Emergency) — research in progress
8. Domain 50 (Healthcare-Democracy Nexus) — research in progress

**Completion estimate**: Domains 44 (both versions), 47 are production-ready now. Domains 45, 46, 48, 49, 50 require 1–2 research sessions each. Full 42-domain suite: 14–21 days from decision.

**New Gists required for Path B**: 7–9 new cluster Gists beyond the 6 existing, plus the Domain 42 Gist (required for all paths). See `execution/phase-1-gist-creation-playbook.md` Section 3 for the Path B Gist architecture.

#### Contact Groups — Path B

Same contact groups as Path A, with distribution pushed to Days 14–35 from the research completion date. The Domain 42 sub-batch executes identically to Paths A and A+37, but timing is tighter: if Path B research extends past May 14, Domain 42 Category D (state AGs) must still go out by May 14–17 regardless.

**Path B critical constraint**: Domain 42 Category A/B outreach must go out by May 8–12 regardless of Path B research status. The DEA deadline does not move.

#### Path B Week 1–4 Timeline

| Period | Research Actions | Distribution Actions |
|--------|-----------------|---------------------|
| Days 0–14 | Complete 5–6 remaining Phase 2 domains; update proposal Gist | Domain 42 outreach (independent, runs in parallel) |
| Day 14–15 | Research checkpoint: are all 42 domains production-ready? | Begin Path A execution calendar from Day 0 equivalent |
| Days 15–28 | Minor domain updates as needed | Batch 1 send; social media launch; Wave 2 preparation |
| Days 28–35 | Full framework at 42 domains | Wave 2 send (10 contacts); Substack Posts 1–2 |

#### Path B Dependencies

Same as Path A, plus:
- 5–6 additional research sessions (1.5–2 hours each) before distribution can begin
- Path B is **not reversible** once committed — once you begin adding Phase 2 domains, you have entered the 14–21 day delay pipeline
- May 30 DOJ consent decree window: under Path B, organizations receive Domain 37 on or around Day 28, leaving 0–2 days to act on the May 30 window (vs. 17 days under Paths A and A+37)

---

## DELIVERABLE 2: Path A+37 Hybrid Risk Assessment

### Why PROJECTS.md Recommends Path A+37

The recommendation is grounded in the intersection of four factors visible in the research record:

**Factor 1 — Domain 37 is not a general-audience domain.** Domain 37 (Federal Executive Interference in the 2026 Midterms) documents five specific federal interference mechanisms tied to named actors and dated advocacy windows. Its primary users are election lawyers, voting rights litigators, and election protection organizations — contacts who need to assess immediately whether the document is actionable in their current docket. A general Tier 1 contact (a law school professor, a think tank analyst) receiving Domain 37 in a 35-domain package has no urgency to read it. The same document, sent with the subject line `Domain 37: 23 active DOJ voter roll cases + NVRA quiet period (Aug 7) — research for Democracy Docket`, reaches an organization that is actively tracking those same cases and will open it the same day.

**Factor 2 — Election protection organizations have different institutional rhythms.** Democracy Docket publishes on a near-daily cycle. The ACLU Voting Rights Project is in active litigation. Lawyers' Committee VRP is preparing for the August 7 NVRA quiet period right now. These organizations have short processing cycles — a targeted briefing with a specific advocacy window lands in active operational planning, not a reading queue. The general Tier 1 contacts (academics, policy analysts) have longer cycles. Sending Domain 37 to both groups in the same wave wastes the urgency signal for election protection contacts.

**Factor 3 — Phase 1b adds 1–2 hours of marginal work at effectively zero marginal risk.** The 12 Phase 1b emails use pre-written subject lines and templated opening paragraphs. The personalization per email is 5–10 minutes (find the organization's most recent active case, connect it to a specific Domain 37 section). The only new infrastructure is the Domain 37 Gist (10 minutes). The total additional burden vs. Path A is approximately 90 minutes. Against this, Path A+37 gains precision with the 12 election protection organizations most likely to actually use Domain 37.

**Factor 4 — The May 30 and August 7 windows are real.** May 30 is the DOJ consent decree finalization deadline. August 7 is the NVRA 90-day quiet period start — after which systematic voter roll removals are prohibited and an emergency injunction is the only legal remedy if they occur anyway. Election protection organizations need to be briefed on Domain 37 with enough lead time to build litigation-ready responses to both windows. Under Path A+37, they receive Domain 37 on Day 1–3 (May 15–17). Under Path A, they receive it in a 35-domain package on Day 0. The net effect is similar for organizations that read systematically (Brennan Center, Protect Democracy). For organizations with a high-volume intake (ACLU, Democracy Docket), the targeted email creates a cleaner action signal.

### What Domain 37 Adds That Justifies the Separate Send

Domain 37 is the only domain in the framework that:

1. Has named five specific federal interference mechanisms tied to specific actors (DOJ voter roll litigation operators, CISA dismantlement, EAC grant conditionality, ICE-at-polls, Bannon disinformation architecture)
2. Provides a dated advocacy windows calendar (May 30, June 30, August 7, September, October) that is directly actionable for organizations with litigation dockets
3. Has a pre-built baseline metrics document (`domains/domain-37-baseline-metrics.md`) with seven quantified pre-distribution baselines — enabling election protection organizations to track change over time
4. Has a companion domain (domain-37b-state-election-security.md, 70 KB, 43 citations) that maps vendor concentration, paper ballot progress, RLA adoption, ERIC departures, and election official turnover — all directly relevant to certification season planning

None of the other 34 domains in Phase 1a have the same combination of named actors, dated windows, and companion litigation infrastructure. Domain 37 is the framework's most operationally useful document for active election protection work.

### Additional Execution Burden vs. Path A

| Task | Time | Required vs. Optional |
|------|------|----------------------|
| Create Domain 37 standalone Gist | 10 min | Required |
| Research 7 Phase 1b Tier 1 org's current litigation | 35–70 min (5–10 min per org) | Required |
| Personalize 7 Phase 1b Tier 1 emails | 35–70 min (5–10 min per email) | Required |
| Send 7 Tier 1 Phase 1b emails (Day 1) | 20 min | Required |
| Research 5 Phase 1b Tier 2 org contacts | 25–50 min | Required |
| Send 5 Tier 2 Phase 1b emails (Day 2) | 15 min | Required |
| Monitor Phase 1b separately from Phase 1a | 5–10 min/day for first 14 days | Required |
| **Total additional burden vs. Path A** | **2.5–4.5 hours over Days 0–14** | — |

**Assessment**: The additional burden is real but modest. The primary cost is the per-org litigation research (5–10 min per org × 12 orgs = 60–120 min across Days 0–2). Everything else is mechanical execution of pre-scripted steps. Against this, the precision gain on 12 high-value election protection contacts is substantive. The risk-adjusted recommendation stands: Path A+37 is the right choice for any user who does not already have personal direct relationships with all 12 election protection organizations.

---

## DELIVERABLE 3: May 28 DEA Deadline — Domain 42 Distribution Analysis

### What Must Happen by May 28

**Hard deadline**: Written notice of desired participation in DEA-1362 (marijuana rescheduling hearing) must reach DEA by May 28, 2026. The docket and submission addresses:
- Email: nprm@dea.gov, Subject: "DEA-1362"
- Mail: DEA Attn: Administrator, 8701 Morrissette Drive, Springfield, VA 22152 (postmark by May 20 to arrive by May 28)

A participation notice costs nothing and preserves full hearing rights through July 15, 2026. The filing requires only three elements (per 91 Fed. Reg. 22777): (1) name and organization; (2) statement of participation intent; (3) whether the participant will offer expert testimony, cross-examine witnesses, or both.

**The action Domain 42 enables**: Organizations that file a participation notice can: submit written comments, present testimony, cross-examine DEA witnesses, and have their position entered in the administrative record. The administrative record is the basis for any subsequent federal court challenge to the DEA's hearing outcome. An organization that does not file by May 28 has no standing to challenge the outcome in federal court.

**Why Domain 42's framing matters for the hearing**: Most organizations that file in DEA-1362 will file through standard drug policy channels (public health evidence, state legalization data, industry harm reduction). Domain 42 introduces a democratic legitimacy framing that is analytically distinct: the hearing structure itself is a regulatory capture problem; the DEA's institutional posture as both regulator and adjudicator violates the APA's design intent; and the communities most subjected to enforcement are systematically excluded from the political processes that set enforcement policy. This framing, if entered into the administrative record through 3+ independent organizations, creates a foundation for an APA challenge to the hearing structure — separate from and supplementary to any challenge to the substantive outcome.

### Target Organizations for May 28 Participation

The Domain 42 outreach plan (`execution/domain-42-may-28-outreach-plan.md`) identifies 10 organizations across four categories. Priority ranking for May 28 participation:

**Tier 1 — Must reach by May 15, highest probability of filing**:

| Organization | Why Tier 1 | Contact |
|--------------|-----------|---------|
| Drug Policy Alliance (A-1) | Has filed in every major scheduling proceeding since 2002; staff includes former DEA analysts; most likely to cite Domain 42's democratic exclusion framing | press@drugpolicy.org |
| NORML (A-3) | Filed 47-page comment in 2023 rescheduling process; NORML's legal committee maintains DEA ALJ standing; likely already preparing DEA-1362 participation | norml@norml.org |
| ACLU Criminal Law Reform Project (B-1) | Has DEA standing; Domain 42 Section 3 (disenfranchisement feedback loop) is directly within their current mandate | nationaloffice@aclu.org |
| The Sentencing Project (B-3) | Their own data is cited in Domain 42; research staff can produce written comments in under two weeks | staff@sentencingproject.org |

**Tier 2 — Must reach by May 21, secondary amplifiers**:

| Organization | Best Outcome | Contact |
|--------------|-------------|---------|
| NAACP Legal Defense Fund (B-2) | Files participation notice framing DEA-1362 as a voting rights proceeding | naacpldf.org webform |
| Marijuana Policy Project (A-2) | Refers Domain 42 to federal policy director; congressional ally referral | mpp@mpp.org |
| LEAP (A-4) | Files short participation notice — law enforcement voice is unusually credible with DEA ALJs | info@leap.cc |
| SSDP (A-5) | Chapter network mobilization; referral to DPA/NORML | ssdp@ssdp.org |
| Mason Marks (C-1) | Methodological validation; may be planning independent testimony (he published the Yale Law Journal article Domain 42 cites) | mason.marks@yale.edu (verify current institution) |
| State AGs (D-1 through D-4) | One or more AG offices add federalism argument to existing DEA-1362 comment | See per-state contacts in `execution/domain-42-contact-list.md` |

**If only 5 contacts can be reached before May 15, priority order**: Drug Policy Alliance, NORML, ACLU Criminal Law Reform Project, The Sentencing Project, NAACP Legal Defense Fund.

### The May 8–27 Distribution Window

**Domain 42 outreach is path-independent.** The 10-organization sub-batch runs on its own calendar regardless of which path is selected for the general framework. The Domain 42 outreach plan was designed for this scenario explicitly (see `execution/domain-42-may-28-outreach-plan.md` Section 6: "What This Plan Does Not Require").

**Wave structure**:

| Wave | Date | Contacts | Count | Status |
|------|------|----------|-------|--------|
| Wave 1 | May 8 (TODAY — if not yet sent) | DPA, NORML, ACLU CLR, Sentencing Project, LEAP, SSDP | 6 | URGENT |
| Wave 2 | May 10–12 | NAACP LDF, Prison Policy Initiative, MPP, Mason Marks, Ohio State Moritz DEPC | 5 | Scheduled |
| Wave 3 | May 14–17 | Colorado AG, California AG, Michigan AG, Washington AG | 4 | Scheduled |
| Follow-up trigger | May 15–17 | All Wave 1 non-responders | Varies | Conditional |
| Final reminder | May 21 | All non-respondents | Varies | Hard-stop date |

**CRITICAL**: Wave 1 should have gone out on May 8 (as planned). If it has not been sent yet, it is overdue. Today is May 13. Organizations receiving the briefing today have 15 days to route internally and file — still viable for Tier 1 contacts with established DEA filing infrastructure, but marginal for organizations that need longer routing time. Send Wave 1 TODAY before any other Phase 1 execution work.

**May 28 and Path A/A+37/B interaction**: Domain 42 timing is unaffected by path selection. Under all three paths, the Domain 42 sub-batch runs on the May 8–21 calendar. The only difference across paths:
- Path A / A+37: Domain 42 Gist gets created on Day 0 (May 14) as part of the launch preparation. Any Domain 42 emails sent after May 14 include the live Gist URL.
- Minimal viable path (if no path decision yet): Domain 42 markdown file sent as direct attachment. Do not delay Domain 42 outreach waiting for the Gist.

### Domain 42 Calendar — Remaining Action Days

| Date | Action | Status |
|------|--------|--------|
| May 13 (TODAY) | Send Wave 1 if not yet sent — DPA, NORML, ACLU CLR, Sentencing Project, LEAP, SSDP | IMMEDIATE |
| May 14 | Create Domain 42 Gist (10 min); update all Domain 42 email template [GIST URL] fields | Day 0 |
| May 15–16 | Send Wave 2 — NAACP LDF, PPI, MPP, Mason Marks, Ohio State Moritz | Scheduled |
| May 17 | Send Wave 3 — State AGs (confirm current contacts first; WA AG changed — Ferguson is now Governor) | Scheduled |
| May 21 | Final reminder wave — all non-respondents. LAST DAY for any new Domain 42 outreach | Hard stop |
| May 28 | DEA participation deadline. Log which organizations filed. | External deadline |

---

## DELIVERABLE 4: Path A+37 Full Execution Sequence

### Step 1: Gist Creation (20 minutes, Day 0)

**What exists**: 6 canonical Gists live at `DISTRIBUTION_GIST_URLS.md`. These are the foundation — do not recreate them.

**What to create on Day 0**:

1. **Domain 42 Gist** (required for all paths, 10 minutes):
   - Source: `domains/domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md`
   - Full procedure: `execution/domain-42-gist-creation-steps.md`
   - Title: `domain-42-drug-policy-democratic-legitimacy-regulatory-capture-2026.md`
   - After creation: add URL to `DISTRIBUTION_GIST_URLS.md`; replace all 5 `[GIST URL — fill when created...]` instances in `execution/domain-42-email-template.md`

2. **Domain 37 Gist** (Path A+37 only, 10 minutes):
   - Source: `domains/domain-37-federal-executive-interference-2026-midterms.md`
   - Procedure: same Zone A/D structure as Domain 42; paste the Advocacy Windows table as Zone D footer (text in Deliverable 1 above)
   - Title: `domain-37-federal-executive-interference-2026-midterms.md`
   - After creation: add URL to `DISTRIBUTION_GIST_URLS.md`; fill `[Domain 37 Gist URL — fill after Block 7 creation]` in `execution-plans/EXECUTION_PLAN_PATH_A_PLUS_37.md`

**User-facing Gist creation guide**: Yes — `execution/phase-1-gist-creation-playbook.md` covers the complete procedure. Section 1 covers Domain 42. Section 2 covers Domain 37 (Path A+37). All steps numbered with exact text to paste.

### Step 2: Template Field Fill (30–40 minutes, Day 0)

**Script**: `scripts/fill_templates.py` — automated field substitution; does not call GitHub API; writes output to `scripts/filled_output/`

**Fields to fill in `fill_templates.py` before running**:

| Field | What to Enter | Source |
|-------|--------------|--------|
| `{{YOUR_NAME}}` | Your name | You |
| `{{YOUR_CONTACT_INFO}}` | Email / website / phone | You |
| `DISTRIBUTION_PATH` | `"A+37"` | Path decision |
| `{{SUBSTACK_HANDLE}}` | Your Substack handle if applicable | You |

**Fields that remain for manual fill in email drafts** (intentional — these require research at send time):
- `{{RECENT_JUST_SECURITY_ARTICLE}}` — visit justsecurity.org day of send
- `{{RECENT_WEISER_PUBLICATION}}` — visit brennancenter.org day of send
- `{{RECENT_CHENOWETH_PAPER}}` — visit hks.harvard.edu/faculty/erica-chenoweth day of send
- `{{RECENT_BASSIN_FILING}}` — visit protectdemocracy.org day of send
- `{{RECENT_ELIAS_CASE}}` — visit democracydocket.com day of send

**Total placeholder fields across all templates**: Approximately 47 total; the script fills approximately 40 automatically. The 7 manual fields (5 recent publications + 2 personal fields if not already in script) take 5–10 minutes each at send time.

**Estimated total time for template fill step**: 20–30 minutes (run script once, verify output, fill 5 recent publication fields in drafts on Day 0).

**Verification**: After running the script, search `scripts/filled_output/` for any remaining `{{...}}` strings. If any remain (other than the 5 manual publication placeholders), correct the `FIELD_VALUES` dictionary and re-run.

### Step 3: Contact Verification (30–45 minutes, Day 0)

**Batch 1 contacts** (last verified April 29, 2026 — 14 days ago as of May 13; verify again before sending):

| Contact | Institution | Verify Here | Email |
|---------|-------------|-------------|-------|
| Ryan Goodman | Just Security / NYU Law | justsecurity.org/about-us; law.nyu.edu/faculty | ryan.goodman@nyu.edu |
| Wendy Weiser | Brennan Center Democracy Program | brennancenter.org/about/leadership | wweiser@brennancenter.org |
| Erica Chenoweth | Harvard Kennedy School / Nonviolent Action Lab | hks.harvard.edu/faculty/erica-chenoweth | echenoweth@hks.harvard.edu |
| Ian Bassin | Protect Democracy | protectdemocracy.org/team/ian-bassin | ian@protectdemocracy.org |
| Marc Elias | Democracy Docket | democracydocket.com/about | marc@democracydocket.com |

**Estimated per-contact time**: 6 minutes (institution webpage + email format confirm). Total for 5 contacts: 30 minutes.

**Phase 1b contacts** (12 election protection orgs): Full verification checklist in `execution/phase-1-contact-verification-checklist.md` Sections 3–4. Estimated time: 40–60 minutes for 12 contacts. Can be done in parallel with Day 0 setup while Phase 1a emails are drafting.

**Note on Washington AG (Domain 42 Category D)**: Bob Ferguson moved from AG to Governor. Confirm current Washington AG and their press/policy contact before sending Wave 3.

**Note on Mason Marks (Domain 42 Category C)**: Listed as Yale Law School as of May 7. Confirm current institutional email before sending Category C wave.

**Have we verified all 45 Tier 1 contacts recently?** The 5 Batch 1 contacts are verified (April 29). The remaining 40 Tier 1 contacts have not been verified since initial research compilation. The contact verification checklist (`execution/phase-1-contact-verification-checklist.md`) batches these into 4 sections for systematic verification. Full Tier 1 verification: 3–4 hours (can split across 2 days, can run in parallel with path decision). **This is a pre-launch action that can start NOW without a path decision.**

### Step 4: Email Send Timing and Automation

**Send rules** (all paths):
- Institutional emails: Tuesday–Thursday before noon recipient's local time
- Reddit: Monday or Tuesday morning
- Substack: Tuesday or Wednesday 10:00 AM ET
- Twitter threads: Tuesday–Friday 08:00–10:00 AM ET
- Do not send institutional email Friday afternoon or Monday morning

**Batch 1 send sequence** (Day 0, 4-hour window):

| Time | Email | Rationale |
|------|-------|-----------|
| 16:00 | Ryan Goodman (Just Security) | Earliest credibility signal; 3–5 day editorial response cycle |
| 16:30 | Wendy Weiser (Brennan Center) | Response informs Batch 2 framing |
| 17:00 | Erica Chenoweth (Harvard Kennedy School) | Academic credibility; theory of change alignment |
| 17:30 | Ian Bassin (Protect Democracy) | Litigation and implementation focus |
| 18:00 | Marc Elias (Democracy Docket) | Media and litigation strategy |

**Spacing**: 30 minutes between sends. This prevents any appearance of a mass send and gives the email client time to confirm delivery of each.

**Scheduling/automation**: No automated sends for Batch 1 — these are manually composed and sent. The reason: each requires a manual personalization field (recent publication) that cannot be automated. After Batch 1, the `fill_templates.py` script handles URL and field substitution for subsequent batches. Substack and social media posts can be scheduled via their native schedulers after drafts are prepared.

**Does we have a scheduling plan?** Yes — `PHASE_1_DISTRIBUTION_EXECUTION_BLUEPRINT.md` Section 2.2 provides the complete Day 0–21 timeline with exact send times for each email, Reddit post, and Substack publication. Social media templates are in `distribution-substack-drafts.md` and `distribution-reddit-templates.md`.

### Step 5: Social Media Scheduling

**Are the templates ready?** Yes:
- Substack: 4 post drafts in `distribution-substack-drafts.md` — complete with URL placeholders that fill_templates.py replaces
- Reddit: 5 subreddit-tailored posts in `distribution-reddit-templates.md` — ready to post after URL substitution
- Twitter/X: 5-tweet opening thread draft — stage for Day 1 (May 15), 08:00 AM ET

**Scheduling tasks on Day 0**:
- Schedule Substack Post 1 for Day 3 (May 17), 10:00 AM ET
- Stage Twitter Thread 1 for Day 1 (May 15), 08:00 AM ET
- Stage r/law Reddit post for Day 2 (May 16)
- Stage r/PoliticalScience post for Day 4 (May 18)

**Dependency**: Social media templates contain `[link]` placeholders. The `fill_templates.py` script replaces these as part of Block 2. Confirm script has run and output files verified before scheduling social posts.

---

## DELIVERABLE 5: Pre-Launch Actions — Executable NOW Without Path Decision

The following actions are fully path-agnostic. They do not require knowing whether you will choose Path A, A+37, or B. They all reduce the Day 0 execution time and can begin immediately.

---

### Action 1: Contact Verification (START NOW — estimated 3–4 hours)

The 5 Batch 1 contacts were verified April 29 (14 days ago). Re-verify immediately. Then proceed with remaining Tier 1 contacts from the verification checklist.

**Full checklist**: `execution/phase-1-contact-verification-checklist.md`
- Section 1: Batch 1 (5 contacts, 30 min) — DO FIRST
- Section 2: Remaining Tier 1, Batches 2–3 (20 contacts, 2 hours)
- Section 3: Phase 1b election protection orgs (12 contacts, 1 hour) — needed only for Path A+37

**Priority**: Batch 1 re-verification is the highest-value 30-minute task available right now. Stale contact data on a Batch 1 send creates a hard bounce that cannot be undone.

**Washington AG note (Domain 42)**: Confirm the current Washington AG before the Category D wave. Bob Ferguson left the AG position when he became Governor. This verification should happen before May 14 (Category D send date).

**Mason Marks note (Domain 42)**: Confirm current institutional email. Yale Law was correct as of May 7. Verify before the Category C wave (May 12).

---

### Action 2: Domain 42 Wave 1 Send (DO TODAY if not yet sent — estimated 90 minutes)

**This is the most time-sensitive action in this entire document.** Wave 1 was planned for May 8. Today is May 13. Every day of delay compresses the time the receiving organizations have to file before May 28.

**Minimal viable path (no Gist required)**:
1. Open `execution/domain-42-email-template.md`
2. Fill in [Name], [Organization], and replace `[GIST URL — fill when created...]` with `attached` in all 5 Category A template instances
3. Attach `domains/domain-42-drug-policy-democratic-legitimacy-regulatory-capture.md` as a direct file attachment
4. Attach `execution/domain-42-may-28-dea-submission-guide.md` as a companion
5. Send to 6 contacts in the order: DPA, NORML, ACLU Criminal Law Reform, Sentencing Project, LEAP, SSDP (30-minute spacing)

**This requires no Gist, no path decision, no infrastructure.** An email client and the two files above are sufficient.

---

### Action 3: Create the Domain 42 Gist Structure Template (10 minutes)

Even without sending it, you can log in to GitHub as `esca8peArtist` and draft the Domain 42 Gist as a private draft (not public yet). When ready to distribute, toggle to public.

**Guide**: `execution/domain-42-gist-creation-steps.md`
**Zone A/D text to paste**: In that guide

This action removes 10 minutes from Day 0 execution.

---

### Action 4: Pre-Stage Email Templates with Fields Identified (20–30 minutes)

Open `scripts/fill_templates.py`. Without running it, fill in:
- `{{YOUR_NAME}}` in the FIELD_VALUES dictionary
- `{{YOUR_CONTACT_INFO}}` in the FIELD_VALUES dictionary

Then run it once with `DRY_RUN = True` to confirm zero warnings. This validates the template infrastructure before you need it.

After running: search `scripts/filled_output/` for any `{{...}}` strings that were not replaced. If any remain (other than the 5 intentional manual placeholders), identify the cause and fix the FIELD_VALUES entry. Do this before Day 0 so the Day 0 template fill step is a clean execution, not a debugging session.

---

### Action 5: Create the Weekly Monitoring Spreadsheet Template (30 minutes)

The adoption tracking spreadsheet schema is fully specified in `execution/phase-1-adoption-tracking-automation.md`. You do not need a path decision to create the blank spreadsheet — the schema is path-independent.

**What to build**:
- Google Sheet with 3 tabs: Tab 1 = Contact Log; Tab 2 = Gist View Tracking; Tab 3 = Media/Citation Monitoring
- Tab 1 schema: Name, Organization, Tier, Email, Date Sent, Subject Variant, Response Date, Response Type, Adoption Level (0–4), Notes
- Tab 2: Gist URL, View Count (Day 0 baseline), View Count (Day 7), View Count (Day 14), View Count (Day 30)
- Tab 3: Date, Source, URL, Mention Type, Domain Cited, Notes

**Reference**: `execution/phase-1-adoption-tracking-automation.md` Part 2 for complete column schema with auto-calculation formulas.

**Baseline capture** (can be done NOW): Log in to GitHub as `esca8peArtist` and record current Gist view counts for all 6 canonical Gists. Record in Tab 2 as "Pre-launch baseline." This gives you a true Day 0 baseline regardless of when you decide to launch.

---

### Action 6: Verify Sending Domain Not Blocklisted (5 minutes)

Before any email goes out: visit `mxtoolbox.com/blacklists.aspx`, enter your sending domain, and confirm it is not on any major blocklist. A clean result takes 2 minutes. A blocked domain requires switching to a Gmail or Protonmail address for the initial sends — this would need to be decided before any email leaves your outbox.

---

## Missing Pieces and Gaps

The following items are still needed or have open questions. None blocks Phase 1 launch, but all should be addressed before or during Day 0.

| Gap | Description | Blocking? | Resolution |
|-----|-------------|-----------|------------|
| Domain 42 Wave 1 overdue | Wave 1 was planned for May 8; today is May 13; organizations have 15 days remaining | No — 15 days is still viable for Tier 1 contacts | Send TODAY using minimal viable path (direct attachment) |
| Washington AG contact stale | Bob Ferguson became Governor; current AG unknown | No — Category D wave is scheduled May 14–17 | Verify before May 14 via atg.wa.gov |
| Mason Marks institutional email | Needs day-of confirmation (Yale Law as of May 7) | No — Category C wave is May 12 | Visit yale.edu/law or mason.marks current site before send |
| Tier 1 Batches 2–3 not re-verified since research | 40 contacts not position-verified since initial compilation | No — verification is a pre-send task per batch, not a pre-launch gate | Run `execution/phase-1-contact-verification-checklist.md` Sections 2–4 before each batch |
| Domain 37 standalone Gist does not yet exist | Must be created Day 0 for Path A+37 Phase 1b | Yes for A+37 Phase 1b only — does not block Phase 1a | Create Day 0 using `execution/phase-1-gist-creation-playbook.md` Section 2 |
| Social media accounts not confirmed active | Twitter/Bluesky/Reddit accounts not verified as accessible | No | Confirm login and access before staging Day 0 social posts |
| Phase 2 domain completion for Path B | 5–6 domains incomplete | Only for Path B | Not applicable for Paths A or A+37 |

---

## Execution Time Estimate — Path A+37 Decision to First Email Send

| Step | Task | Time |
|------|------|------|
| Pre-step | Domain 42 Wave 1 send (TODAY, minimal viable path) | 90 min |
| Block 1 | Verify 6 canonical Gists live in incognito browser | 10 min |
| Block 2 | Create Domain 42 Gist | 10 min |
| Block 3 | Create Domain 37 standalone Gist | 10 min |
| Block 4 | Run fill_templates.py; verify output | 20 min |
| Block 5 | Batch 1 contact re-verification (5 contacts × 6 min) | 30 min |
| Block 6 | Per-email personalization for 5 contacts (recent publication per contact) | 30 min |
| Block 7 | Draft 5 emails; manual placeholder fill; final QA read | 30 min |
| Block 8 | Tracking spreadsheet setup | 20 min |
| Block 9 | Social media staging (Substack + Twitter thread + Reddit) | 30 min |
| Block 10 | Batch 1 send (5 emails, 30-min spacing) | 120 min |
| Block 11 | Phase 1b Tier 1 org research (7 orgs × 7 min each — current docket check) | 50 min |
| **Total (Day 0)** | **Path decision to Batch 1 sent, Phase 1b preparation complete** | **~4.5–5 hours** |
| Day 1 blocks | Phase 1b Tier 1 personalization (7 emails) + send | 90 min |
| **Total to Phase 1b complete** | **Days 0–1** | **~6 hours** |

**The "path A+37 can launch by" answer**: Path A+37 can be launched with **Batch 1 emails sent by 6:00 PM on May 14, 2026**, pending only the four user actions listed in the Executive Finding at the top of this document. Phase 1b (election protection orgs) completes by end of day May 16, 2026.

The Domain 42 sub-batch (independent of path) should ideally start TODAY (May 13) via the minimal viable direct-attachment path. Wave 1 can be sent in 90 minutes with no Gist creation required.

---

## Path Summary — Final Verdict

| Question | Answer |
|----------|--------|
| Can the user launch today without a path decision? | Yes — Domain 42 Wave 1 can send immediately (minimal viable path) |
| What is the earliest Path A+37 Batch 1 can go out? | May 14, 2026 (pending 4 user actions, ~4.5 hours execution) |
| What is Phase 1b complete date? | May 16, 2026 |
| What is the May 28 DEA deadline risk if no action today? | Moderate — 15 days remain; viable for Tier 1 contacts with DEA infrastructure; marginal for others |
| What does Path B cost on May 30 window? | Almost certain miss of the May 30 DOJ consent decree window; Paths A/A+37 have 17-day lead time |
| Is any content blocking launch? | No — all 58+ domains are production-ready |
| What is the single most urgent action right now? | Send Domain 42 Wave 1 TODAY (overdue from May 8) |

---

*Created May 13, 2026. Integrates: PHASE_1_EXECUTION_READINESS.md (Session 662), PHASE_1_DISTRIBUTION_EXECUTION_BLUEPRINT.md (Session 933+), execution-plans/EXECUTION_PLAN_PATH_A_PLUS_37.md (Session 686), execution/domain-42-may-28-outreach-plan.md (Session ~981), execution/domain-42-contact-list.md, execution/phase-1-contact-verification-checklist.md, execution/phase-1-gist-creation-playbook.md, DISTRIBUTION_GIST_URLS.md.*
