---
title: "Phase 3 Rapid Response Playbooks — Step-by-Step Activation Procedures"
subtitle: "25 Playbooks | Trigger Detection | Decision Authority | Execution Timeline | Success Metrics"
created: "2026-06-24"
status: "production-ready"
parent_documents:
  - "PHASE_3_CONTINGENCY_MATRIX.md (scenario table; probability/impact scores)"
  - "PHASE_3_PARALLEL_RESEARCH_RUNWAY.md (7-week sprint baseline)"
  - "PHASE_3_RESEARCHER_AVAILABILITY_CONTINGENCY.md (backup researcher contacts)"
  - "PHASE_3_FUNDING_CONTINGENCY_PLAN.md (budget reduction protocols)"
  - "PHASE_3_EXPERT_CONTACT_FRAMEWORK.md (35 contacts, engagement triggers)"
scope: "Step-by-step activation procedures for all 25 scenarios in PHASE_3_CONTINGENCY_MATRIX.md. Use alongside the matrix: identify scenario, reference playbook code (PB-XX), execute steps in sequence."
---

# Phase 3 Rapid Response Playbooks
## Step-by-Step Activation Procedures for All 25 Contingency Scenarios

**How to use this document:**
1. A crisis emerges during the Nov 4 – Dec 20 research sprint.
2. Open PHASE_3_CONTINGENCY_MATRIX.md. Find the scenario category. Identify the Severity level and Playbook code (PB-XX).
3. Come to this document. Find the playbook by code. Execute steps in sequence.
4. Check success metrics at the bottom of each playbook before considering the contingency resolved.

**Decision authority:**
- Severity 1 playbooks: execute autonomously (no user notification required).
- Severity 2 playbooks: execute steps 1–3 autonomously, then notify user within 24 hours.
- Severity 3 playbooks: stop at Step 1 (trigger confirmation) and notify user immediately before executing further steps.

---

## PLAYBOOKS: RESEARCHER AVAILABILITY (R-SERIES)

### PB-R1 — Primary Researcher Short-Term Absence (≤1 Week)

**Severity:** 1 (standard) / 2 (high) if Weeks 6–7

**Trigger Detection Checklist:**
- [ ] Researcher notifies unavailability on Day 0 or Day 1 of absence
- [ ] Absence duration confirmed ≤7 days
- [ ] Absence does NOT fall in Week 6 (Dec 9–16) or Week 7 (Dec 16–20)

**Decision Authority:** Autonomous execution. Notify user if absence extends past Day 5.

**Execution Timeline:**

Day 0 (Absence notification received):
- [ ] Document current research status: which tasks are in-flight, what sources are open, which contacts are awaiting responses
- [ ] Classify all open tasks into four buckets:
  - Bucket A: Can continue without primary researcher (source verification, Gist formatting, contact email prep, bibliography cross-check) — CONTINUE
  - Bucket B: Can be rescheduled 3–5 days without critical-path impact (coalition feedback calls, expert validation requests) — QUEUE
  - Bucket C: Should not proceed without primary researcher (new distribution sends to Tier 1 contacts, scope decisions, analytical frame choices) — HOLD
  - Bucket D: Cannot wait (any task with a deadline within 48 hours of absence start) — ESCALATE immediately

Day 1–5 (Absence duration):
- [ ] Execute all Bucket A tasks on normal schedule
- [ ] Queue Bucket B tasks with specific scheduled return dates (not "when back" — set calendar target)
- [ ] Hold Bucket C tasks; document queue for primary researcher review on return
- [ ] Monitor: if Bucket D items arise during absence, trigger PB-R2 escalation immediately

Day 5+ (If absence extends):
- [ ] If absence confirmed extending past 7 days: activate PB-R2 immediately
- [ ] Do not wait for primary researcher to confirm extension — if absence reaches Day 5 without confirmed return date, escalate

Day of Return:
- [ ] Primary researcher reviews Bucket B and C queues (estimated 1 hour)
- [ ] Bucket B tasks reschedule for next 2 business days
- [ ] Bucket C tasks execute in priority order (domain research > expert contacts > distribution planning)

**Resource Requirements:** No backup researcher needed. Support researcher (if available) can handle Bucket A tasks.

**Success Metrics:**
- [ ] All Bucket A tasks completed during absence with no quality reduction
- [ ] No Tier 1 distribution emails sent without primary researcher decision authority
- [ ] Return-day research resumes within 2 hours of return with full context
- [ ] December 20 deadline unaffected

---

### PB-R2 — Primary Researcher Extended Absence (1–3 Weeks)

**Severity:** 2 (high)

**Trigger Detection Checklist:**
- [ ] Absence confirmed to exceed 7 days, OR Day 5 reached without confirmed return date
- [ ] Absence duration: 7–21 days
- [ ] Absence does NOT require full Tier 3 replacement (primary researcher still available for async Q&A)

**Decision Authority:** Execute steps 1–3 autonomously. Notify user within 24 hours of Tier 2A activation.

**Execution Timeline:**

Hour 0–2 (Trigger confirmed):
- [ ] Activate Tier 2A backup researcher. Contact information: documented in PHASE_3_RESEARCHER_AVAILABILITY_CONTINGENCY.md Section 6 (Tier 2 Backup Researchers table). Candidate 2A is the primary target; Candidate 2B is on standby.
- [ ] Send briefing package to Tier 2A researcher:
  - Current research status document (2–3 sentences per zone: complete / next / blockers)
  - Contact list with status (who has been contacted, what their response was, what is pending)
  - Gist templates (Domain K and H formatting templates)
  - Expert call scripts (if any validation calls are pending)
  - Current source verification status (which citations need re-checking, any known broken links)

Hour 2–6 (Tier 2A onboarding):
- [ ] Tier 2A backup reads briefing package (estimated 90 minutes)
- [ ] 30-minute sync call between primary researcher (if available) and Tier 2A: walk through current status, outstanding decisions, expert relationship context
- [ ] Tier 2A confirms which tasks they can execute solo vs. which require primary researcher async sign-off

Day 1–14 (Extended absence execution):
- [ ] Tier 2A owns daily progress on active research tasks
- [ ] Primary researcher available for async Q&A (email; max 2-hour response time) — specifically for expert contact strategy, analytical frame choices, and scope decisions
- [ ] Daily 5-minute status note from Tier 2A to shared document: what completed, what next, any blockers
- [ ] Week 3 check: if absence extends to 21 days → activate PB-R3 immediately

Critical escalation rule — distribution windows:
- [ ] If absence spans Dec 9–16 (Week 6, Domain K distribution): escalate to PB-R3 immediately. Do not rely on async coordination for primary distribution sends.
- [ ] If absence spans Dec 16–20 (Week 7, Domain H distribution): escalate to PB-R3 immediately.

Return:
- [ ] Primary researcher reviews Tier 2A work: 1–2 hour review
- [ ] Approve or flag revisions (targeted, not full rewrite)
- [ ] Resume research on Day 1 of return; no ramp-up delay needed

**Resource Requirements:**
- Tier 2A backup researcher: estimated 20–30 hours of research work across 1–3 weeks
- Tier 2A briefing and coordination time: 4–6 hours

**Success Metrics:**
- [ ] Tier 2A activated within 6 hours of trigger
- [ ] Research continuity maintained: active research tracks not stalled for more than 24 hours
- [ ] Primary researcher notified of escalation events in real time
- [ ] December 20 deadline unaffected (or PB-R3 activated before deadline is missed)

---

### PB-R3 — Primary Researcher Full Exit (>3 Weeks or Permanent Transition)

**Severity:** 3 (critical)

**Trigger Detection Checklist:**
- [ ] Primary researcher confirms unavailability >21 days, OR communicates inability to continue Phase 3
- [ ] Absence falls in any week of the Nov 4 – Dec 20 window

**Decision Authority:** Stop at trigger confirmation. Notify user immediately. Do not execute further steps until user acknowledges.

**Execution Timeline (post-user acknowledgment):**

Hour 0–2 (User notification and acknowledgment):
- [ ] Send to user: current research status (complete, in-flight, blocked); estimated remaining hours by domain; Tier 3 candidate availability; recommended scope compress if exit occurs after Week 4
- [ ] Await user acknowledgment before activating Tier 3

Hour 2–6 (Tier 3 activation, post-user approval):
- [ ] Contact Tier 3 replacement researcher (documented in PHASE_3_RESEARCHER_AVAILABILITY_CONTINGENCY.md Section 6, Tier 3 contacts)
- [ ] Send complete handoff package:
  - All production documents (Domain K ~12,700 words, Domain H ~7,500 words — all existing research)
  - Phase 3 master calendar (PHASE_3_PARALLEL_RESEARCH_RUNWAY.md)
  - Expert contact framework (PHASE_3_EXPERT_CONTACT_FRAMEWORK.md — 35 contacts with engagement triggers)
  - Source databases (DOMAIN_K_SOURCE_MASTER_DATABASE.md, DOMAIN_H_SOURCE_MASTER_DATABASE.md)
  - All Gist templates and email distribution templates
  - Hard deadline reference card (December 20 / January 3 / January 10)

Hours 6–18 (Tier 3 onboarding — 8–12 hour ramp-up):
- [ ] Tier 3 reads existing Domain K research (~12,700 words): estimated 3–4 hours
- [ ] Tier 3 reads existing Domain H research (~7,500 words): estimated 2–3 hours
- [ ] Tier 3 reviews Phase 3 master calendar and dependency map: 1–2 hours
- [ ] Tier 3 reviews expert contact framework and outreach email templates: 1–2 hours
- [ ] Tier 3 syncs with peer reviewer on current phase status: 1 hour
- [ ] Tier 3 verifies Congress.gov / SCOTUSblog status current as of handoff date: 1 hour
- [ ] Tier 3 confirms readiness to assume full project ownership: Day 2

Scope compress decision (if exit occurs after Week 4):
- [ ] User decides: full Domain H Gist OR combined brief only for December 20
- [ ] If combined brief only: Domain H full Gist defers to January 10 window (within PHASE_3_PARALLEL_RESEARCH_RUNWAY.md tolerance)
- [ ] If exit occurs after Week 6: Domain H full production defers to Phase 4; combined brief only publishes by January 10

**Resource Requirements:**
- Tier 3 replacement researcher: 40–70 hours of research and distribution work
- Onboarding time: 8–12 hours
- User decision time: 2–4 hours for scope compress decision

**Success Metrics:**
- [ ] Tier 3 activated within 24 hours of exit confirmation
- [ ] Tier 3 confirms readiness for full project ownership within 48 hours of contact
- [ ] December 20 distribution target maintained (with scope compress if necessary)
- [ ] User informed and acknowledges scope changes before execution

---

### PB-R4 — Domain 37a Consumes November Capacity

**Severity:** 2 (high)

**Trigger Detection Checklist:**
- [ ] Confirm on November 4 (Phase 3 launch day): is Domain 37a production-complete?
- [ ] If NOT complete: estimate remaining hours (baseline 25–30 hours if starting from scratch)
- [ ] Confirm: solo researcher or 2-researcher model?

**Decision Authority:** Solo researcher executes compression autonomously and notifies user within 24 hours. 2-researcher model requires user notification to confirm Researcher B start timing.

**Execution Timeline:**

November 4 (Trigger confirmed):
- [ ] Domain 37a completion status check: document which sections exist vs. which require production
- [ ] Estimate remaining 37a hours: 15–25 hours if framework exists, 25–30 hours if starting from scratch
- [ ] Immediately update November capacity allocation:
  - Weeks 1–3 (Nov 4–25): Domain 37a primary (25–30 hours) + election results documentation (3–5 hours)
  - Weeks 3–4 (Nov 18–Dec 2): Domain 37a completion + Domain K preliminary activation (4–6 hours read-in)
  - December 2–20: Domain K research completion (8–13 hours)
  - December 16–January 10: Domain H research completion (14–19 hours)

Solo researcher path:
- [ ] No Domain K research in November — preserve November exclusively for Domain 37a
- [ ] Begin Domain K on December 2 (3-week window: Dec 2–20)
- [ ] Begin Domain H on December 16 (4-week window: Dec 16–Jan 10)
- [ ] Accept Domain H Tier 1 distribution slipping from Jan 10 to Jan 17 as within tolerance

2-researcher path:
- [ ] Researcher A: Domain 37a (November 4–25, full attention)
- [ ] Researcher B: Domain K (begin November 11 — 1-week delay to establish 37a framework so B can reference it for constitutional foundation sections)
- [ ] Week synchronization: Researchers A and B sync weekly to confirm 37a progress does not create Domain K analytical dependencies

**Resource Requirements:**
- No additional researchers beyond current model
- Timeline compression adds no cost; reduces scope of December parallel tracks (Domains 49, 51 update, 56 update defer to January)

**Success Metrics:**
- [ ] Domain 37a production-complete by November 25 (or earlier if 37a was partially pre-staged)
- [ ] Domain K research begins no later than December 2
- [ ] December 20 distribution target maintained for Domain K
- [ ] Domain H combined brief (minimum viable) completed by December 20

---

### PB-R5 — 2-Researcher Model, Mid-Sprint Handoff Required

**Severity:** 2 (high) if Weeks 5–7; 1 (standard) if Weeks 1–4

**Trigger Detection Checklist:**
- [ ] Confirm: 2-researcher model is active
- [ ] Confirm: one researcher confirms unavailability for 1+ remaining weeks mid-sprint
- [ ] Identify which week of the sprint the handoff occurs in

**Decision Authority:** Weeks 1–4 handoff: execute autonomously, notify user within 48 hours. Weeks 5–7 handoff: notify user immediately, await acknowledgment.

**Execution Timeline:**

Hours 0–24 (Handoff initiation):
- [ ] Handing-off researcher produces HANDOFF_NOTES.md within 24 hours of handoff decision
  - HANDOFF_NOTES.md template:
    - Current research status (% complete by zone, with specific completion markers)
    - Next 3 tasks in priority sequence
    - Open questions (unresolved analytical choices, pending expert responses)
    - Source verification status (which of the domain's citations are still unverified)
    - Contact activation status (which experts have been contacted, response status, any scheduled calls)
    - Expert relationship context (communication style notes for key contacts — what they responded positively to, their current priorities)

Hours 24–48 (Receiving researcher sync):
- [ ] Receiving researcher reads HANDOFF_NOTES.md (estimated 90 minutes)
- [ ] 1-hour synchronization meeting or async review session (written Q&A if synchronous meeting unavailable)
- [ ] Receiving researcher confirms which tasks to absorb immediately vs. queue

Week 5–7 specific protocol (if handoff unavoidable in distribution window):
- [ ] Receiving researcher prioritizes combined brief (Week 6) above all domain-specific Gist work
- [ ] Receiving researcher does NOT attempt to absorb full domain authorship in Weeks 5–7; instead absorbs distribution-specific tasks (contact outreach, email prep, Gist formatting)
- [ ] Handing-off researcher retains async responsibility for analytical decisions even after handoff (subject matter knowledge cannot transfer in 24 hours)

Mandatory synchronization points (both researchers):
- [ ] Week 6 sync: combined K+H brief — agree on structure, divide section writing (1-hour meeting minimum)
- [ ] Week 7 sync: consistency review — confirm bill numbers, international precedent descriptions, expert contact list consistent across both documents (30-minute check)

**Resource Requirements:**
- HANDOFF_NOTES.md: 4–6 hours to produce (thorough documentation)
- Synchronization: 2–4 hours per handoff event

**Success Metrics:**
- [ ] HANDOFF_NOTES.md complete within 24 hours of handoff decision
- [ ] 1-hour sync completed within 48 hours
- [ ] No research continuity gap exceeding 48 hours
- [ ] Combined brief produced on schedule regardless of which researcher produces it
- [ ] December 20 distribution target maintained

---

## PLAYBOOKS: EXPERT CONTACT (E-SERIES)

### PB-E1 — Tier 1 Contact Unresponsive (Single Organization)

**Severity:** 1 (standard)

**Trigger Detection:** No response from Tier 1 contact within 7 days of initial outreach.

**Decision Authority:** Autonomous execution. No user notification required.

**Execution Steps:**

Day 8 (Follow-up):
- [ ] Send one follow-up email to same contact
  - Subject line change: make more specific to a Domain K or H finding relevant to their current work (e.g., "Re: your recent SCOTUS term limits push — Domain K analysis you may find useful")
  - Body: shorter (3–4 sentences max); reference one specific finding they would care about; re-attach the Gist link
  - Timing: send between 9 AM and 11 AM on a Tuesday or Wednesday (highest open rates for organizational email)

Day 14 (Secondary contact pivot):
- [ ] If still no response, pivot to secondary contact at same organization:
  - Fix the Court (if Gabe Roth unresponsive): Fix the Court has 2 additional staff; contact research@fixthecourt.com or the general info address
  - Brennan Center (if Derek Rosenfeld unresponsive): try Alicia Bannon (Judiciary Program Director) at alicia.bannon@brennancenter.org
  - Demand Justice (if Josh Orton unresponsive): try hello@demandjustice.org (institutional address; routes to staff)
  - ACS (if Nancy Rodriguez unresponsive): try info@acslaw.org (institutional address)
- [ ] Subject line for secondary contact: "Research brief on [Domain K/H topic] — sharing with [Organization Name] team"

Day 21 (Non-responsive protocol):
- [ ] Mark contact as "non-responsive" in distribution log
- [ ] Proceed with distribution to all other Tier 1 contacts on schedule
- [ ] Do not hold distribution waiting for this contact
- [ ] Add to Tier 2 follow-up list for January 2027 outreach (congressional window)

**Success Metrics:**
- [ ] Follow-up sent by Day 8
- [ ] Secondary contact identified and contacted by Day 14
- [ ] Distribution to other contacts proceeds on schedule regardless of this contact's response
- [ ] Non-responsive status documented in distribution log by Day 21

---

### PB-E2 — Multiple Tier 1 Contacts Simultaneously Unresponsive

**Severity:** 2 (high)

**Trigger Detection:** Three or more Tier 1 contacts non-responsive after 14 days of initial outreach.

**Decision Authority:** Execute steps 1–3 autonomously. Notify user within 24 hours if format pivot decision required.

**Execution Steps:**

Day 14 (Trigger confirmed):
- [ ] Timing hypothesis: check whether non-response coincides with major news event (election results, SCOTUS ruling, congressional recess). If so, hold 7 additional days before concluding format problem.
- [ ] Format diagnosis: review Phase 2 outreach actuals (BATCH_1_CONTACT_LOG.md, BATCH_1_CONTACT_VERIFICATION.md). Were similar Tier 1 contacts responsive in Phase 2? If yes, format is not the problem — timing or specific contact failure is.

Day 15–21 (If timing hypothesis is NOT the explanation):
- [ ] Activate university-based alternates:
  - Yale Law School: Jack Balkin (comparative constitutional theory), balkin@yale.edu; Judith Resnik (federal courts), resnik@yale.edu
  - Harvard Law School: Jeannie Suk Gersen (Harvard Law Review faculty advisor); Cass Sunstein (constitutional law, federal regulatory authority)
  - Berkeley Law: Erwin Chemerinsky (dean), echemerinsky@law.berkeley.edu
  - Georgetown Law: David Cole (national security and civil liberties, ACLU connection); Sherrilyn Ifill (civil rights litigation, formerly NAACP LDF President)
- [ ] Contact NCC (Jeffrey Rosen) as bipartisan bridge: constitutioncenter.org/about/contact or media@constitutioncenter.org. NCC distribution reaches audiences outside the progressive ecosystem.
- [ ] Substack / passive discovery test: publish a summary of Domain K or H research as a Substack post. Monitor whether the same organizations engage through inbound discovery rather than outbound email.

Day 21 (Format pivot decision, if required):
- [ ] Notify user with specific recommendation: (a) continue direct outreach with format modifications, OR (b) pivot to passive discovery (Substack/Obsidian Publish) as primary distribution channel, OR (c) activate co-publication partnership (consult PHASE_3_CONTINGENCY_ROUTING.md Contingency C)
- [ ] Await user decision before changing distribution strategy

Distribution proceeds:
- [ ] Regardless of Tier 1 non-response, distribute to all responding Tier 2 and Tier 3 contacts on schedule by December 20

**Success Metrics:**
- [ ] Timing hypothesis tested before format conclusion
- [ ] University-based alternates contacted by Day 21
- [ ] User notified if format pivot decision required
- [ ] December 20 distribution proceeds to all responsive contacts

---

### PB-E3 — International Expert Unavailable

**Severity:** 1 (standard)

**Trigger Detection:** International expert contact (Scheppele, Roznai, Frankenberg) unresponsive after 14 days or explicitly confirms unavailability.

**Decision Authority:** Autonomous execution. No user notification required.

**Execution Steps:**

Immediate (Unavailability confirmed):
- [ ] Identify which section of Domain H the expert was verifying:
  - Scheppele: comparative constitutional resilience (Hungary, Poland, India case studies in Zone 2)
  - Roznai: unamendability doctrine (Zone 3 amendment strategy)
  - Frankenberg: German Basic Law amendment (Zone 2 international precedent)
- [ ] Identify the published primary source that replaces expert confirmation:
  - Scheppele: cite her published work directly ("Autocratic Legalism," U of Chicago Law Review 2018; "Orbán's Laboratory of Illiberalism," The Atlantic 2019)
  - Roznai: cite Unconstitutional Constitutional Amendments (Oxford University Press, 2017) — this is the primary academic authority on unamendability doctrine; expert confirmation is secondary to this publication
  - Frankenberg: cite Germany Federal Law Gazette (Bundesgesetzblatt) for the Basic Law amendment text directly

In-document notation:
- [ ] Add footnote to relevant sections: "[Expert name]'s published analysis of [topic] — [citation] — forms the basis of this section. Direct accuracy verification via correspondence was not obtained prior to publication."
- [ ] This notation is standard academic practice; it signals scholarly integrity, not a quality deficit

**Success Metrics:**
- [ ] Published primary source identified for each expert contact that is unavailable
- [ ] Domain H sections do not have factual claims that lack sourcing
- [ ] No delay to Domain H production schedule

---

### PB-E4 — Expert Provides Conflicting Factual Feedback

**Severity:** 1 (standard) for factual corrections; 2 (high) for analytical methodology disputes

**Trigger Detection:** Expert response contains factual or analytical correction to Domain K or H research.

**Decision Authority:** Factual corrections: autonomous execution. Methodology disputes: notify user within 24 hours.

**Execution Steps:**

Classification (Immediate):
- [ ] Is this a factual correction? (Bill number wrong, co-sponsor count outdated, citation date incorrect)
  - YES: execute factual correction protocol below
- [ ] Is this an analytical dispute? (Feasibility assessment challenged, constitutional interpretation disagreed, framework scope questioned)
  - YES: execute analytical dispute protocol below

Factual correction protocol:
- [ ] Locate the specific claim in the production document
- [ ] Verify expert's correction against primary source (Congress.gov for bill status, GovTrack for co-sponsor counts, CRS reports for legislative history)
- [ ] If primary source confirms expert is correct: update in-place immediately. Note in revision log: "[Date]: [Expert name] corrected [specific claim]. Verified against [primary source]. Updated."
- [ ] If primary source contradicts expert: document the discrepancy. Note both the original claim and the expert correction with sources. Do not change the document until discrepancy is resolved (triangulate with second source).

Analytical dispute protocol:
- [ ] Document expert's critique specifically: what claim are they disputing, what is their counter-argument?
- [ ] Triangulate with a second source: find either a second expert or a second primary source that speaks to the disputed claim
- [ ] If two sources agree with the critique: update the analysis. Document both the original claim and the revision.
- [ ] If sources conflict: document both views in the relevant section with attribution. Do not hold publication.
- [ ] If the dispute concerns a central finding (not a peripheral claim): flag immediately in CHECKIN.md and notify user. Do not modify central analytical framework without user decision.

**Success Metrics:**
- [ ] Factual corrections verified against primary source before acceptance
- [ ] No undocumented changes to the production document
- [ ] Central finding disputes escalated to user within 24 hours
- [ ] No publication delay for factual corrections

---

## PLAYBOOKS: DATA SOURCES (D-SERIES)

### PB-D1 — Congress.gov Unavailable

**Severity:** 1 (standard)

**Trigger Detection:** Congress.gov inaccessible for more than 4 hours during scheduled research session.

**Decision Authority:** Autonomous execution.

**Execution Steps:**

Hour 0–1 (Outage confirmed):
- [ ] Check Congress.gov status via downdetector.com or status.github.com (outages often affect multiple government sites simultaneously)
- [ ] Estimate likely outage duration: government site outages typically resolve within 4–12 hours

Immediate alternatives (activate in order):
1. [ ] GovTrack.us — primary mirror for legislative status (bill text, committee assignments, co-sponsor counts, latest action)
2. [ ] Ballotpedia Legislative Reference — state and federal bill tracking; available if Ballotpedia access is active
3. [ ] Fix the Court legislative status page — for judicial reform bills specifically, Fix the Court publishes monthly status updates
4. [ ] ProPublica Congress API — provides JSON data for bills, votes, and members; free API with registration

Queue tasks requiring Congress.gov primary sourcing:
- [ ] Create a "pending Congress.gov verification" queue in the research log
- [ ] Continue all research tasks not requiring Congress.gov (writing, international source verification, expert contact outreach)
- [ ] Return to Congress.gov queue immediately upon restoration

Time estimate: if mirror data is used, add 2–4 hours for any task that normally takes 1–2 hours (mirrors require cross-checking across two sources where Congress.gov is authoritative on its own).

**Success Metrics:**
- [ ] Alternative source activated within 1 hour of Congress.gov outage
- [ ] No research tasks stalled for more than 4 hours due to Congress.gov outage
- [ ] All Congress.gov-dependent verification tasks queued and completed upon restoration

---

### PB-D2 — Primary Source URLs Broken (Domain H 90+ Citations)

**Severity:** 2 (high) for anchor sources; 1 (standard) for secondary sources

**Trigger Detection:** Source verification pass finds more than 10 broken URLs, OR any anchor source URL broken.

**Decision Authority:** Execute autonomously. Notify user only if anchor source data has materially changed (not just URL changed).

**Execution Steps:**

Step 1 — Triage broken URLs (1–2 hours):
- [ ] Sort broken URLs into two categories:
  - Anchor sources: V-Dem Democracy Index, Germany Basic Law amendment text (Bundesgesetzblatt), IEEPA statutory text, Humphrey's Executor case text, Trump v. Slaughter ruling (when available), NPV compact state count
  - Secondary sources: journalism articles, blog posts, organizational reports, press releases

Step 2 — Wayback Machine protocol for anchor sources (2–3 hours):
- [ ] For each broken anchor source URL, go to web.archive.org
- [ ] Search for the original URL; find the most recent crawl that is complete
- [ ] Verify the archived version matches the substance of the citation (check specific data points cited)
- [ ] Update document citation to: "[Original URL] (archived version: web.archive.org/web/[date]/[URL])"

Step 3 — Government mirror protocol (1–2 hours):
- [ ] For government primary sources with broken URLs:
  - IEEPA text: find on govinfo.gov (U.S. Government Publishing Office archive)
  - CRS reports: find on Congress.gov/crs-products or EveryCRSReport.com (CRS report mirror site)
  - Court documents: find on CourtListener.com (PACER mirror) or Supreme Court official archive (supremecourt.gov)
  - Germany Basic Law: Bundesgesetzblatt official archive (gesetze-im-internet.de) or Bundestag digital archive

Step 4 — International source mirror protocol (1–2 hours):
- [ ] For international sources (Israel Knesset Official Gazette, Germany Basic Law, Hungary Fundamental Law):
  - Use official institutional archives rather than English-language secondary summaries
  - Israel: knesset.gov.il (official Knesset archive with English translations)
  - Hungary: njt.hu (Hungarian National Legislation Database; some English translations)
  - Germany: gesetze-im-internet.de (official German law texts)
- [ ] For V-Dem data: vdem.net/data — V-Dem maintains direct download access to their annual Democracy Report data

Step 5 — Secondary source replacement (2–4 hours):
- [ ] For secondary journalism and blog sources with broken URLs:
  - Option A: find the article through the publication's own search (if original publication URL changed)
  - Option B: cite the Internet Archive version with archived date
  - Option C: if the article is no longer accessible anywhere: note "source confirmed at [date of research]" and find a replacement secondary source that makes the same point
- [ ] Prioritization: secondary sources that support unique claims (not duplicated elsewhere) require replacement. Secondary sources that are one of many supporting a well-documented claim can be noted as "formerly available; [archived date]."

**Resource Requirements:** 8–12 hours for systematic source verification and update pass. Plan within December research allocation.

**Success Metrics:**
- [ ] All anchor sources have verified, accessible citations (Wayback or government mirror if original broken)
- [ ] All secondary sources that support unique claims have verified replacements
- [ ] Updated citation list matches Domain H source count (90+) with zero unresolved broken links
- [ ] User notified if any anchor source data has materially changed (e.g., V-Dem scores revised)

---

### PB-D3 — Trump v. Slaughter Ruling Integration

**Severity:** 1 (standard) if clean ruling; 2 (high) if fractured plurality

**Trigger Detection:** Trump v. Slaughter ruling issued after October 31, 2026.

**Decision Authority:** Autonomous execution of pre-built integration protocol.

**Execution Steps:**

Hour 0–2 (Ruling confirmed):
- [ ] Read the ruling. Determine outcome:
  - Humphrey's Executor OVERRULED (most likely per oral argument signals): activate Integration Protocol A
  - Humphrey's Executor AFFIRMED: activate Integration Protocol B (minimal)
  - FRACTURED PLURALITY (no majority opinion): activate Integration Protocol C

Integration Protocol A — Humphrey's Executor Overruled (6–8 hours total):
Domain K updates (3–4 hours):
- [ ] Add Zone 1.3: "Independent Agency Structural Collapse after Trump v. Slaughter"
  - Content: ruling's holding and reasoning; which agencies are now subject to at-will presidential removal; why SCERT Act legislative framing must now explicitly address the gap
  - Add to the legislative advocacy frame: restoring statutory removal protections (Humphrey's Executor-era standard) as a companion bill to the SCERT Act, not a subset of it
  - Cross-reference to Domain H Zone 3's Statutory Reclamation section
- [ ] Update Zone 1.1 (Structural Capture analysis): note that the independent agency removal protection gap is no longer a pending vulnerability — it has been actualized by Trump v. Slaughter
- [ ] Update the legislative feasibility table: restoration of Humphrey's Executor via statute (No Kings Act, SHADOW Act) moves from "defensive measure" to "affirmative repair target"

Domain H updates (3–4 hours):
- [ ] Add Section 1.5: "Regulatory Independence Collapse as Constitutional Amendment Priority"
  - Content: Trump v. Slaughter's logic, if extended, eliminates independent monetary policy (Fed), independent telecommunications regulation (FCC), independent election administration funding (EAC). Zone 3 amendment strategy must address this.
  - Add constitutional amendment option: explicit Article II limitation on removal authority (structurally similar to the German Basic Law's "eternity clause" protection for constitutional principles)
- [ ] Update Zone 3 (Statutory Reclamation): add Humphrey's Executor restoration as a named target in the Statutory Reclamation legislative agenda
- [ ] Update Zone 1.2 (Executive Consolidation): upgrade this section to "actual" rather than "threatened" — Trump v. Slaughter completes the consolidation trajectory

Integration Protocol B — Humphrey's Executor Affirmed (1 hour total):
- [ ] Add one paragraph to Domain K Zone 1 noting that Trump v. Slaughter affirmed Humphrey's Executor, preserving existing removal protection framework
- [ ] Add one sentence to Domain H Zone 1.2 noting that independent agency removal protection survived Trump v. Slaughter (this removes a "pending threat" notation from the document)

Integration Protocol C — Fractured Plurality (8 hours total):
- [ ] Read all separate opinions; identify the majority principle (what can be held as binding precedent)
- [ ] Write 500-word interpretive analysis for research notes: what does this ruling actually hold? Which agencies are now definitively exposed to at-will removal? Which remain in legal uncertainty?
- [ ] Flag in CHECKIN.md: "Trump v. Slaughter produced fractured plurality — interpretive analysis underway; may require user decision on how to frame legal uncertainty in Domain K and H"
- [ ] Implement Integration Protocol A's structural updates but frame the ruling's scope as uncertain where it is genuinely uncertain

**Success Metrics:**
- [ ] Ruling integrated into both Domain K and Domain H within 5 days of issuance
- [ ] New zones/sections are self-contained (do not require rereading the full domain document to understand)
- [ ] User notified if plurality interpretation requires framing decision
- [ ] No delay to overall December 20 distribution from ruling integration

---

### PB-D4 — Election Results Delayed or Contested

**Severity:** 2 (high) for full delay; 1 (standard) for partial delay

**Trigger Detection:** November 14 — congressional composition for 120th Congress cannot be determined with confidence from available certified results.

**Decision Authority:** Execute steps 1–2 autonomously. Notify user by November 20 if composition still undetermined.

**Execution Steps:**

November 4–14 (Election results monitoring):
- [ ] Track certified results by state from: Associated Press (primary call source), Decision Desk HQ (second source), state secretary of state official results pages
- [ ] Determine by November 14: can the 120th Congress composition (House majority, Senate majority) be stated with confidence based on races called by AP?
- [ ] If YES: proceed to Decision Gate 1 (PHASE_3_PARALLEL_RESEARCH_RUNWAY.md Week 1) — write the electoral frame for Domain K based on composition

If composition undetermined by November 14:
- [ ] Activate parallel drafting: write all three electoral frame scenarios (Democratic majority in at least one chamber; Republican retention of both; split control). Total additional time: 4–6 hours.
- [ ] Continue all non-electoral-frame research in Domain K that does not depend on composition (Zone 1 structural analysis, Zone 2 term limits constitutional analysis, Zone 6 judicial capacity) — do not stall the whole track waiting for results
- [ ] Flag in CHECKIN.md: "Election results not certified by November 14; parallel drafting underway. User decision needed on which frame to prioritize by December 1."

November 20 (User notification):
- [ ] If composition still not definitively determined: notify user with options:
  - Option A: produce all three frames; redact based on final results
  - Option B: produce a split-scenario brief that is composition-independent ("Under either likely 120th Congress composition...")
  - Option C: delay Domain K distribution to December 9 (compress from 2 weeks Tier 1 outreach to 1 week) to allow another 2 weeks of results waiting

December 1 (Hard stop — must decide):
- [ ] If composition still contested: proceed with split-scenario brief (Option B) regardless of uncertainty. Do not miss December 20 distribution date waiting for certified results.

**Success Metrics:**
- [ ] Electoral frame research does not stall Domain K's other research zones
- [ ] Parallel drafting scenario completed if needed by November 20
- [ ] User notified and decision received by November 20 if composition undetermined
- [ ] Domain K distribution proceeds by December 20 regardless of certification status

---

### PB-D5 — FEC Post-Election Data Delayed

**Severity:** 1 (standard)

**Trigger Detection:** FEC summary data not available on December 1.

**Decision Authority:** Autonomous execution.

**Execution Steps:**
- [ ] Switch to Campaign Finance Institute (CFI) interim data: cfinst.org — CFI publishes preliminary 2026 cycle data within 2–3 weeks of election day using FEC raw filing data
- [ ] Alternative: OpenSecrets preliminary 2026 cycle totals: opensecrets.org/elections-overview — available within 1–2 weeks of election day
- [ ] Note in Domain 51 update: "FEC official summary data for the 2026 cycle is not yet available as of [date]. This analysis uses CFI/OpenSecrets preliminary data derived from FEC raw filings."
- [ ] Add a revision note for January 2027: update with FEC official summary when released

**Success Metrics:**
- [ ] Domain 51 update proceeds without delay using interim data sources
- [ ] Data source notation is transparent about the preliminary nature of the data

---

## PLAYBOOKS: PUBLICATION PIPELINE (P-SERIES)

### PB-P1 — Gist Platform Inaccessible

**Severity:** 1 (standard)

**Trigger Detection:** Gist platform inaccessible within 48 hours of planned distribution send.

**Decision Authority:** Autonomous execution.

**Execution Steps:**

Immediate:
- [ ] Attempt Gist access from a different network/device to rule out local network issue
- [ ] Check GitHub status: githubstatus.com — determines if platform-wide outage or account-level issue

If platform outage:
- [ ] GitHub Pages fallback (30 minutes): create a new GitHub repository, push the production document as a README.md or index.md, enable GitHub Pages in repository settings. URL format: username.github.io/repository-name. Copy this URL for distribution.
- [ ] Notify distribution recipients in the email body: "Note: Research document is hosted at [GitHub Pages URL] rather than our usual Gist format. Access and format are equivalent."

If account-level access issue (credentials, account suspension):
- [ ] Google Docs fallback (10 minutes): upload the production document to Google Docs. Set sharing to "Anyone with the link can view." Use the share URL as the distribution link.
- [ ] If Google account also unavailable: Obsidian Publish fallback — publish directly to Obsidian Publish site if already configured.
- [ ] Escalate credential recovery in parallel with fallback deployment; do not delay distribution waiting for Gist access restoration.

Longer-term (if Gist account is compromised):
- [ ] Create a new GitHub account for future Gist publications
- [ ] Archive all prior Phase 1–2 Gist URLs in a new format (GitHub Pages or Obsidian Publish) for continuity

**Success Metrics:**
- [ ] Fallback URL live within 30 minutes of Gist inaccessibility confirmed
- [ ] Distribution emails sent with fallback URL on original timeline
- [ ] All distribution recipients notified of format change

---

### PB-P2 — Obsidian Publish Site Down

**Severity:** 1 (standard)

**Trigger Detection:** Obsidian Publish site inaccessible for more than 12 hours during distribution window.

**Decision Authority:** Autonomous execution.

**Execution Steps:**
- [ ] Confirm outage is Obsidian Publish platform (obsidian.md/publish status) vs. local sync issue
- [ ] Proceed with primary distribution (Gist + direct email) — Obsidian Publish is a secondary discovery channel only
- [ ] Note in distribution emails: "Our knowledge commons site is temporarily unavailable. All research materials are available via Gist link in this email."
- [ ] Monitor Obsidian Publish restoration; resend Obsidian Publish URL to distribution list when restored (no urgency — secondary channel)

**Success Metrics:**
- [ ] Primary distribution (Gist + email) proceeds on schedule unaffected by Obsidian Publish status
- [ ] Distribution log notes Obsidian Publish outage for tracking

---

### PB-P3 — Email Delivery Failures to Tier 1 Contacts

**Severity:** 2 (high)

**Trigger Detection:** Delivery failure notification received, or no acknowledgment from fast-responding contacts within 72 hours.

**Decision Authority:** Autonomous execution steps 1–2. Notify user if delivery failures affect more than two Tier 1 contacts.

**Execution Steps:**

Step 1 — Address verification (before sending, not after failure):
- [ ] Verify all Tier 1 contact email addresses against current organizational websites before sending distribution emails in November 2026. Staff turnover at advocacy organizations runs 20–30% annually. Email addresses verified in Phase 2 (May 2026) may be 6 months stale by November 2026.
- [ ] Specifically verify: gabe@fixthecourt.com (Fix the Court), alicia.bannon@brennancenter.org (Brennan Center), contact at Demand Justice, contact at ACS.

Step 2 — Post-send failure response:
- [ ] If delivery failure returned: immediately use institutional contact form as fallback
  - Fix the Court: fixthecourt.com/contact
  - Brennan Center: brennancenter.org/contact (includes a research inquiry form)
  - Demand Justice: demandjustice.org/contact or hello@demandjustice.org
  - ACS: acslaw.org/contact or info@acslaw.org

Step 3 — LinkedIn as last resort:
- [ ] For named contacts with no other reachable address: LinkedIn direct message with brief summary and a request for the correct email or institutional form routing
- [ ] Contacts verified as LinkedIn-active: Gabe Roth, Nancy Rodriguez, multiple Brennan Center staff

Step 4 — User notification:
- [ ] If more than two Tier 1 contacts have delivery failures: notify user with specific contacts and failure details; recommend either LinkedIn outreach or user personal connection with these individuals (if user has direct relationships)

**Success Metrics:**
- [ ] All Tier 1 contact addresses verified before November distribution send
- [ ] Delivery failure response within 4 hours (institutional form backup)
- [ ] No more than 24-hour delay to any single Tier 1 distribution from delivery failure

---

### PB-P4 — Combined K+H Brief Format Rejected

**Severity:** 1 (standard)

**Trigger Detection:** Contact explicitly declines combined brief format, or congressional office specifies format requirements incompatible with combined brief.

**Decision Authority:** Autonomous execution.

**Execution Steps:**
- [ ] Standalone documents available immediately: Domain K research document and Domain H research document both exist as standalone deliverables; offer these as alternative
- [ ] Congressional office one-pager (1 hour to produce):
  - Lead with the three most actionable legislative proposals (from Domain K)
  - Second paragraph: constitutional amendment priorities most relevant to 120th Congress (from Domain H)
  - Third paragraph: January 3 action items (specific bills, specific committee targets)
  - Embedded Gist link for full research documentation
  - Length: one page, formatted for Hill staff reading habits (bullet points, headers, under 600 words)
- [ ] Offer format options when sending distribution email: "We're sharing the combined brief as an attachment; we also have the standalone Domain K and Domain H documents available if you prefer. Please let us know your format preference."

**Success Metrics:**
- [ ] All contacts receive research in a format they can use
- [ ] No distribution send delayed by format negotiation

---

### PB-P5 — Major News Event Disrupts Distribution Send

**Severity:** 2 (high) if hold extends beyond December 22

**Trigger Detection:** Major breaking news confirmed within 48 hours of planned distribution send.

**Decision Authority:** 48-hour hold: autonomous execution. Hold extending past December 22: notify user.

**Execution Steps:**

Hour 0 (Breaking news confirmed):
- [ ] Classify the news event:
  - Type A: Directly relevant to Domain K or H (SCOTUS ruling, major executive action on judicial reform or independent agencies, constitutional crisis)
  - Type B: Major news event dominating attention but not directly relevant to Domain K or H (natural disaster, major international event, political scandal)
- [ ] Type A events: integrate before sending (see PB-D3 for SCOTUS ruling integration; for other relevant events, 2–4 hour integration task), then send. A directly relevant ruling is an opportunity, not a delay.
- [ ] Type B events: initiate 48-hour hold

48-hour hold protocol:
- [ ] Document hold start time and reason
- [ ] Queue all prepared distribution emails (do not send)
- [ ] Monitor news cycle: has attention shifted from the Type B event? (Typically within 24–48 hours for most events)
- [ ] Resume send at first available window after 24 hours if news cycle has shifted

December 22 hard stop:
- [ ] If hold extends to December 22 (48 hours remaining before December 24): distribute regardless of news cycle. January 3 deadline cannot be missed.
- [ ] Notify user of hold extension before December 22 hard stop

**Success Metrics:**
- [ ] Type A events integrated within 48 hours; distribution enhanced not delayed
- [ ] Type B holds do not extend past December 22
- [ ] User notified before December 22 hard stop if hold continues

---

## PLAYBOOKS: TIMELINE OVERRUN (T-SERIES)

### PB-T1 — Domain K Behind Schedule by Week 3

**Severity:** 2 (high)

**Trigger Detection:** Domain K research complete percentage below 70% at end of Week 3 (November 18–25).

**Decision Authority:** Autonomous scope compress up to 15%. Notify user if compress exceeds 15%.

**Execution Steps:**

Day 1 of Week 4 (November 25):
- [ ] Assess Domain K completion: which sections are complete, which are in-flight, which are not started?
  - Zones typically complete at this stage: Zone 1 (structural capture), Zone 2 (term limits analysis)
  - Zones typically incomplete at this stage: Zone 4 (political feasibility, electoral frame), Zone 5 (public legitimacy metrics), Gist formatting
- [ ] Identify scope compress opportunities (15% reduction target):
  - Defer: Domain 49 cross-reference section (valuable but not required for Domain K's primary argument)
  - Compress: reduce international comparison from three case studies (Israel, Germany, Canada) to one (Germany Basic Law amendment is the most directly analogous)
  - Defer: Domain K Tier 2 distribution (Strict Scrutiny podcast pitch, Erwin Chemerinsky accuracy review, SCOTUSblog commentary) to January 2027
  - Retain: all Zone 4 content (political feasibility is Domain K's core contribution); all Zone 1 content (structural capture is foundational)

Resource reallocation:
- [ ] Reallocate 4–6 hours from Domain 49 parallel research (Track C) to Domain K completion
- [ ] In 2-researcher model: Researcher B provides 4-hour source verification assistance to Researcher A for Domain K (a task Researcher B can do without domain ownership)

Distribution calendar adjustment:
- [ ] Domain K Tier 1 distribution shifts from December 2 to December 9–16
- [ ] Combined brief production compresses from Week 6 (Dec 9–16) to Week 7 (Dec 16–20) — still achievable

**Success Metrics:**
- [ ] 15% scope compress identified and pre-authorized within 48 hours of trigger
- [ ] Domain K research complete by December 5 (compressed timeline)
- [ ] Tier 1 distribution proceeds by December 16
- [ ] December 20 combined brief target maintained

---

### PB-T2 — Domain H Behind Schedule by Week 5

**Severity:** 2 (high)

**Trigger Detection:** Domain H research complete percentage below 50% at end of Week 5 (December 2–9).

**Decision Authority:** Execute combined-brief-only compress autonomously. Notify user of scope change within 24 hours.

**Execution Steps:**

December 9 (Trigger confirmed):
- [ ] Assess Domain H completion: which zones are complete, which are in-flight?
  - Zone 3 (Amendment Strategy) post-election update: is this complete?
  - Domain K integration bridge text: is this drafted?
  - Section 1.5 (Trump v. Slaughter integration): is this done?
- [ ] Decision: is full Domain H Gist achievable by December 20 with the remaining time?
  - If yes (>10 hours of work remaining, >10 days available): continue on full Gist track; no compress
  - If no (<10 hours remaining, <10 days available): activate combined-brief-only protocol

Combined brief-only protocol:
- [ ] Required for December 20: post-election Zone 3 update (2–3 hours) + Domain K integration bridge (1 hour) + combined brief writing (4–5 hours) = 7–9 hours total
- [ ] Deferred to January 10 window: full Domain H Gist (remaining Zone 1–4 updates, full formatting, Tier 1 distribution)
- [ ] Notify user: combined brief only for December 20; full Domain H Gist for January 10

January 10 preparation:
- [ ] Queue all deferred Domain H work for January 3–10 execution
- [ ] Pre-draft Domain H Tier 1 distribution emails for January send (Fix the Court, Brennan Center, Domain H-specific academic contacts, NCC)

**Success Metrics:**
- [ ] Combined brief completed by December 20 regardless of full Domain H completion status
- [ ] User notified of scope change within 24 hours
- [ ] January 10 plan in place before December 20

---

### PB-T3 — Both Domains Behind; December 20 at Risk

**Severity:** 3 (critical)

**Trigger Detection:** Both Domain K and Domain H research complete percentages below 70% at end of Week 5, with less than 2 weeks remaining.

**Decision Authority:** Stop and notify user immediately. Await user decision before executing Core Only protocol.

**Execution Steps:**

Immediate (Trigger confirmed):
- [ ] Notify user with specific completion percentages, hours remaining by domain, and recommended Core Only protocol
- [ ] Present two options:
  - Option A: Core Only (abbreviated Domain K + combined brief) — achievable by December 20
  - Option B: Push December 20 to January 3 — miss the pre-seating window; distribute at Congressional seating

Core Only protocol (if user approves Option A):
Domain K Abbreviated (8–10 hours):
- [ ] Produce 1,500–2,000 word abbreviated document with:
  - Three top legislative proposals (TERM Act / SCERT Act / Ethics in Government Act) with bill status and co-sponsor counts
  - Political feasibility assessment per 120th Congress composition
  - Two-paragraph action items for incoming Judiciary Committee staff
- [ ] Format as Gist; send to Tier 1 contacts by December 20

Combined K+H Brief (4–5 hours):
- [ ] Produce 6–8 page combined brief using existing production document content:
  - The Problem (1 page): constitutional capture metrics
  - Statutory Fixes (1–2 pages): top 3 bills from Domain K
  - Constitutional Pathways (1–2 pages): top 3 amendment priorities from Domain H
  - International Precedent (1 page): Germany Basic Law amendment
  - January Action Items (1 page): specific bills, committee targets, witnesses
- [ ] This brief draws on existing production documents (Domain K ~12,700 words, Domain H ~7,500 words); writing time is 4–5 hours, not original research

Full production document deferred:
- [ ] Domain K full Gist: January 10 distribution
- [ ] Domain H full Gist: January 10–17 distribution

**Success Metrics:**
- [ ] User notified immediately upon trigger
- [ ] Core Only achieves December 20 distribution to Fix the Court, Brennan Center, Demand Justice, ACS, Senate Judiciary Committee contacts
- [ ] January 10 plan established before December 20

---

### PB-T4 — November 37a Emergency + December Compression

**Severity:** 3 (critical)

**Trigger Detection:** Domain 37a confirmed not pre-staged on November 4 AND one or more researchers experiences any absence in November.

**Decision Authority:** Execute compression autonomously (per pre-authorization in PHASE_3_PARALLEL_RESEARCH_RUNWAY.md). Notify user within 24 hours.

**Execution Steps:**

November 4–5 (Trigger confirmed):
- [ ] Run the full Domain 37a completion status check:
  - Framework sections complete (results-independent legal analysis): can begin immediately
  - Election-dependent sections: must wait for November 3 results (certified results expected November 5–14)
- [ ] Activate R4 compression (PHASE_3_PARALLEL_RESEARCH_RUNWAY.md Scenario B):
  - Domain K starts December 2 (not November)
  - Domain H starts December 16 (not November or early December)
  - Accept Domain H slipping to January 10 distribution as pre-authorized

Solo researcher track (if applicable):
- [ ] November 4–25: Domain 37a exclusively (25–30 hours)
- [ ] November 25 – December 2: Domain K read-in and preliminary activation (4–6 hours)
- [ ] December 2–20: Domain K completion and Tier 1 distribution
- [ ] December 16–20: combined K+H brief (7–9 hours; draws on existing production documents)
- [ ] January 3–10: Domain H full Gist production and Tier 1 distribution

2-researcher track (if applicable):
- [ ] Researcher A: Domain 37a (November 4–25)
- [ ] Researcher B: Domain K (November 11 — 1-week delay to establish 37a constitutional framework)
- [ ] Both: combined brief production (December 16–20)
- [ ] Researcher B: Domain H (January 3–17)

**Success Metrics:**
- [ ] Domain 37a production-complete by November 25
- [ ] Domain K Tier 1 distribution by December 20
- [ ] Combined brief by December 20
- [ ] User notified within 24 hours of compression activation

---

### PB-T5 — December Capacity Below 30 Hours

**Severity:** 2 (high)

**Trigger Detection:** Confirmed December capacity below 30 hours as of December 5 assessment.

**Decision Authority:** Execute priority restack autonomously. Notify user of deferred tracks within 24 hours.

**Execution Steps:**

December 5 (Capacity assessment):
- [ ] Confirm available December hours (estimate based on current rate and remaining obligations)
- [ ] Priority stack for ≤30 hours:
  - Priority 1: Domain K completion and Tier 1 distribution (8–12 hours) — execute first
  - Priority 2: Combined K+H brief (4–5 hours) — execute second
  - Priority 3: Domain H abbreviated update (2–3 hours for Zone 3 post-election update) — if time permits
  - Deferred: Domain 49 (redistricting), Domain 51 update, Domain 56 update — all defer to January 2027

In 2-researcher model:
- [ ] Researcher A focuses exclusively on Domain K (8–12 hours)
- [ ] Researcher B focuses exclusively on combined brief and Domain H abbreviated Zone 3 update (6–8 hours)
- [ ] All parallel tracks (49, 51 update, 56 update) defer to January

January 2027 resequencing:
- [ ] Queue Domain H full Gist for January 3–10 window
- [ ] Queue Domain 49, Domain 51 update, Domain 56 update for January 10 – February 28 window (January-March roadmap per PHASE_3_EXECUTION_TIMELINE.md)
- [ ] Notify user of January resequencing plan before December 20

**Success Metrics:**
- [ ] Domain K distribution achieved by December 20
- [ ] Combined K+H brief achieved by December 20
- [ ] Deferred tracks documented and resequenced for January
- [ ] User notified within 24 hours

---

## PLAYBOOK QUICK INDEX

| Code | Scenario | Severity | Time to Resolve |
|------|----------|----------|----------------|
| PB-R1 | Short-term researcher absence | 1 | 5–7 days (duration of absence) |
| PB-R2 | Extended researcher absence | 2 | 24 hours to activate; ongoing through absence |
| PB-R3 | Full researcher exit | 3 | 48 hours to Tier 3 onboarding; user required |
| PB-R4 | Domain 37a consumes November | 2 | Immediate resequencing; 4 weeks execution |
| PB-R5 | 2-researcher mid-sprint handoff | 1/2 | 24–48 hours for handoff document + sync |
| PB-E1 | Single Tier 1 contact unresponsive | 1 | 21 days (Day 8 follow-up + Day 14 secondary + Day 21 non-responsive) |
| PB-E2 | Multiple Tier 1 contacts unresponsive | 2 | 21 days; format pivot may require user |
| PB-E3 | International expert unavailable | 1 | 2–4 hours (published source substitution) |
| PB-E4 | Expert provides conflicting feedback | 1/2 | 4–24 hours; central findings require user |
| PB-D1 | Congress.gov unavailable | 1 | 4–12 hours (outage duration) |
| PB-D2 | Primary source URLs broken | 1/2 | 8–12 hours (systematic URL replacement) |
| PB-D3 | Trump v. Slaughter integration | 1/2 | 6–8 hours (clean ruling); 8 hours (plurality) |
| PB-D4 | Election results delayed or contested | 1/2 | Through December 1 (hard stop) |
| PB-D5 | FEC post-election data delayed | 1 | 2–4 hours (interim data source switch) |
| PB-P1 | Gist platform inaccessible | 1 | 30 minutes (GitHub Pages fallback) |
| PB-P2 | Obsidian Publish down | 1 | No action required; proceed with primary |
| PB-P3 | Email delivery failures | 2 | 4–24 hours; institutional form backup |
| PB-P4 | Combined brief format rejected | 1 | 1 hour (one-pager production) |
| PB-P5 | Major news event disrupts send | 2 | 48-hour hold; December 22 hard stop |
| PB-T1 | Domain K behind by Week 3 | 2 | 15% scope compress; distribution Dec 9–16 |
| PB-T2 | Domain H behind by Week 5 | 2 | Combined brief only; defer full Gist to Jan 10 |
| PB-T3 | Both domains behind; Dec 20 at risk | 3 | Core Only protocol; user required |
| PB-T4 | 37a emergency + December compression | 3 | Immediate resequencing; notify user 24h |
| PB-T5 | December capacity below 30 hours | 2 | Priority restack; notify user 24h |

---

*Created: Resistance Research Agent — June 24, 2026*
*File: projects/resistance-research/PHASE_3_RAPID_RESPONSE_PLAYBOOKS.md*
*Cross-reference: PHASE_3_CONTINGENCY_MATRIX.md (scenarios + probability/impact), PHASE_3_RESOURCE_REALLOCATION_FRAMEWORK.md (budget scenarios)*
