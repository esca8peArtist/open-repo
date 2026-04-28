---
title: "Phase 3 Real-Time Crisis Monitoring Infrastructure"
subtitle: "Unified Production Document — 35-Domain Proposal Monitoring, Contingency Tracking, and Coalition Integration"
date: 2026-04-28
status: production-ready
phase: 3
project: resistance-research
word_count: ~5,500
supersedes:
  - monitoring-infrastructure-2026.md
  - phase-3-monitoring-infrastructure-2026.md
operational_templates:
  - templates/monthly-snapshot-template.md
  - templates/contingency-trigger-template.md
  - templates/domain-update-template.md
  - monitoring/templates/monthly-crisis-snapshot.md
  - monitoring/templates/contingency-trigger-log.md
  - monitoring/templates/coalition-feedback-tracker.md
cross_references:
  - democratic-renewal-proposal.md (Part IV — Implementation Roadmap)
  - policy-influencer-mapping.md
  - first-amendment-suppression.md
  - environmental-rollbacks-tracker.md
  - police-brutality-consent-decree-tracker.md
  - litigation-tracker-2026.md
  - surveillance-tracking.md
---

# Phase 3 Real-Time Crisis Monitoring Infrastructure

*Unified Production Document — April 28, 2026*

---

## The Problem This Infrastructure Solves

The 35-domain Democratic Renewal Proposal documents crisis conditions as of April 2026. Institutional audiences — law school clinics, AG coalitions, labor unions, congressional staffers — evaluate proposals partly on currency. A proposal accurate in April but three months stale by the time it reaches a Senate staffer in July loses credibility precisely where it matters most: in the actionability window before the November 2026 midterms.

Sessions 529-530 demonstrated what happens when this problem is solved: SAVE Act Senate failure became evidence of a durable GOP institutionalist bloc; Trump v. Wilcox became documentation of judicial capture; the State Department "Operation Epic Fury" memo became definitive analysis of War Powers Reform exhaustion. Those updates, totaling 5,720 words across five domains, took one working session each and materially strengthened the proposal's credibility with election-protection organizations and law review editors.

This document formalizes that ad hoc process into a systematic monitoring infrastructure. It answers four questions:

1. Which of the 35 domains require automated monitoring, and which require human curation — and how do they feed monthly crisis snapshots?
2. What does a formalized monthly crisis snapshot look like, and what triggers move a domain to high urgency?
3. For each major domain, what are the most likely contingency outcomes and how does each change the implementation roadmap?
4. How does coalition feedback change domain prioritization — and which monitoring data is published versus kept internal?

---

## Part I: Monitoring Architecture — The 35-Domain Matrix

### Design Principle: Three-Tier Structure

Not all 35 domains require the same monitoring investment. High-volume, structured, public data can be tracked through automated alerts. Domains requiring interpretive judgment need human curation. Domains where operational intelligence exceeds public reporting need coalition input. The three-tier structure assigns each domain to the monitoring mode that matches its data environment.

**Summary**: 24 domains are reviewed monthly, 10 quarterly, 3 annually. Tier 1 (automated) is 6 domains; Tier 2 (human-curated) is 20 domains; Tier 3 (coalition-fed) is 9 domains with some overlap.

---

### Tier 1 — Automated Monitoring (High-Frequency, Low-Context)

These domains generate structured data in public databases within hours of significant events. A coordinator sets up alerts once and receives flagged events without ongoing manual effort.

**Domain 1 — Voting Rights and Elections**
Primary sources: Democracy Docket RSS (all 50 states, sortable by issue); CourtListener docket alerts for Watson v. RNC and Louisiana v. Callais; FEC API (independent expenditure reports, dark money routing); Congress.gov API (SAVE Act follow-on, VRA reauthorization). Flag triggers: new voter roll purge litigation filed; FEC filings showing dark money on voter ID campaigns; any Senate vote on electoral legislation; any new DOJ suit against state voter roll procedures.

**Domain 6 — Judicial Independence**
Primary sources: SCOTUS orders list (every Monday, 9:30 AM ET — CourtListener mirrors within 30 minutes); CourtListener docket alerts for Trump v. Slaughter (pending June 2026); Senate Judiciary Committee hearing notices via congress.gov; SCOTUSblog's interim docket tracker for shadow docket activity. Flag triggers: any shadow docket emergency application granted in a domain-relevant case; any Article III judge removal or impeachment vote; Senate Judiciary hearings on judicial conduct.

**Domain 29 — Prosecutorial Weaponization and DOJ Capture**
Primary sources: PACER via CourtListener for SPLC v. United States and related civil society prosecution dockets; DOJ press releases (pattern-trackable by subject); Just Security's Anti-Corruption Tracker (weekday manual screening, adequate lag for two-week update standard); Reporters Committee for Freedom of the Press. Flag triggers: new indictments of civil society organizations; congressional subpoenas to journalists; DOJ press conferences announcing investigations of Democratic officials.

**Domain 33 — State Legislative Autocratization**
Primary sources: LegiScan API keyword search (50 states — terms: "ballot initiative," "redistricting," "preemption," "voter ID," "supermajority requirement"); Democracy Docket state cases RSS; Ballotpedia state legislation database. Flag triggers: any state passing supermajority requirements for ballot initiatives; mid-decade congressional redistricting attempt; dark money state supreme court race filings (FEC cross-reference).

**Domain 34 — Congressional Power-of-the-Purse**
Primary sources: USASpending.gov API (obligation data vs. appropriations — flags holds); GAO ICA reports (Google Alert: "GAO Impoundment Control Act" — delivers within 24 hours); OMB apportionment portal (restored August 2025 per court order — monitor for Category C footnotes exceeding 8% of any discretionary account). Flag triggers: any Category C apportionment exceeding 8% of a discretionary account; any agency refusing to spend specifically appropriated funds; new GAO formal ICA referral.

**Domain 37 — Federal Executive Interference in 2026 Midterms**
Primary sources: CISA election security advisories; EAC security announcements; Democracy Docket RSS; DOJ voter roll litigation tracker (23 active cases as of April 2026). Flag triggers: any CISA budget cut passing appropriations committee; any ICE enforcement announcement tied to election calendar; new DOJ suits against state ballot access procedures.

---

### Tier 2 — Human-Curated Monitoring (Medium-Frequency, High-Context)

Automated sources capture raw events in these domains, but a coordinator must decide whether each event crosses the threshold for a domain update. The threshold question is always: does this development materially change the proposal's analysis, or is it another instance of a documented pattern?

**Monthly Tier 2 domains (15 domains):** Domain 2 (Civil Service — Schedule F litigation, OPM workforce data, MSPB appeals); Domain 3 (Immigration — NILA weekly, ICE operational tempo); Domain 7 (Democratic Participation — First Amendment tracker cross-reference, protest policing circuit cases); Domain 8 (Media/Press Freedom — Reporters Committee weekly, Pentagon corridor case); Domain 9 (Federalism — NAAG press releases, Public Rights Project, AG coalition activity); Domain 11 (Healthcare — Federal Register CMS/HHS alerts, June 2026 HHS guidance deadline); Domain 12 (Environmental — Harvard EELP tracker, Earthjustice docket, finalization of [PROPOSED] entries); Domain 15 (Labor — NLRB case decisions, AFL-CIO Tier 3 input, Slaughter cross-impact on NLRB independence); Domain 19f (War Powers — Senate roll call alerts, State Department WPR section 4 notifications, Iran outcome post-May 1); Domain 21 (Surveillance/Privacy — FISA 702 post-April 30 outcome, data broker gap, ACLU tracking); Domain 23 (Trade Policy — Court of International Trade docket for 24-state AG challenge, Section 301 investigation status); Domain 26 (Government Accountability — POGO weekly, CREW watchdog alerts, IG vacancy tracking); Domain 27 (Higher Education — AAUP statements, Harvard First Circuit docket, FIRE tracker, visa revocation patterns); Domain 30 (Reproductive Rights — EMTALA litigation status, Rewire News Group); Domain 31 (Healthcare/Medicaid — Georgetown CCF analyses, KFF monthly enrollment, June 2026 HHS guidance).

**Quarterly Tier 2 domains (8 domains):** Domain 4 (Economic Policy); Domain 5 (Social Safety Net — OBBBA implementation timeline); Domain 14 (Campaign Finance — quarterly FEC filings); Domain 16 (Housing); Domain 17 (Education/K-12); Domain 25 (Gun Rights — Second Circuit pipeline); Domain 28 (War Powers Venezuela — OLC memo set); Domain 36 (AI Governance — LegiScan state AI bills, NIST).

**Annual domains (3 domains):** Domain 10 (Tribal Sovereignty — NARF newsletter); Domain 13 (Constitutional Amendment — NPVIC state count); Domain 18 (Veterans Affairs — VA IG reports); Domain 24 (Infrastructure — GAO reports).

---

### Tier 3 — Coalition-Fed Monitoring (Low-Frequency, High-Leverage)

These domains require input from actual reform constituencies whose operational knowledge exceeds public data. The distribution strategy (policy-influencer-mapping.md) creates the natural intake channels.

**Domain 23 (Trade) — Business Roundtable, Chamber of Commerce litigation updates, Court of International Trade.** These actors have first-hand knowledge of the 24-state AG challenge timeline before it reaches public reporting.

**Domain 26 (Government Accountability) — POGO, CREW, MSPB case pipeline, Inspector General community.** These organizations track accountability failures in real time and will know whether IG capacity has been restored or further degraded before official data reflects it.

**Domain 31 (Healthcare/Medicaid) — Georgetown Center for Children and Families, KFF monthly enrollment, Families USA, state Medicaid director communications via NAMD.** The June 2026 HHS guidance window is the primary advocacy alert — this coalition will know whether the guidance has substantive content three weeks before it is published.

**Domain 9 (Federalism) — NAAG, individual AG websites, interstate compact activity (uniform law commission).** AG coalition contacts will know which states are considering joining multistate challenges before formal filings.

---

### How Tiers Feed Monthly Crisis Snapshots

The monthly crisis snapshot (template: `templates/monthly-snapshot-template.md`) is the operational output of the monitoring matrix. It has eight sections: Tier 1 automated review → current alerts (5-7 highest-urgency domains) → pending decision calendar → Tier 2 human-curated review → coalition feedback summary → three-tracker status review → implementation roadmap trigger assessment → monthly work plan. The snapshot is completed in the first two weeks of each month and takes approximately 6-8 hours of coordinator time for a full pass.

---

## Part II: Monthly Crisis Snapshot Protocol

### The Two-Week Currency Standard

The proposal remains credible with institutional audiences if domain content is within two weeks of the most significant crisis development in that domain. This standard is demonstrably achievable: Sessions 529-530 updated six domains using WebSearch + WebFetch against primary sources, producing 5,720 words with 45 citations.

The two-week standard means: if a major ruling (Trump v. Slaughter), significant legislation (SAVE Act final vote), or documented executive action (State Department WPR memo) occurs, the relevant domain document must be updated within two weeks. For distribution to institutional audiences, that standard is what distinguishes a live proposal from an archived document.

### First-of-Month Assessment Structure

**Week 1 — Automated Monitoring Review (2-3 hours)**
Run all six Tier 1 flag triggers. For each domain: has a flag trigger been crossed? If yes, queue for domain update session. Deliverable: updated status line in PROJECTS.md (Domains 1, 6, 29, 33, 34, 37 — status and last-checked date). Verify all automated alerts remain active (CourtListener case alerts, Federal Register agency subscriptions, Democracy Docket newsletter, Google Alert for "GAO Impoundment Control Act").

**Week 2 — Crisis Snapshot and Work Plan (3-4 hours)**
Complete the full monthly snapshot template. The output is the 5-7 most urgent domains for this month, each with: urgency reason, specific deadline or advocacy window, coalition contact type most affected, and action decision (full domain update / section addition / distribution update brief / coalition outreach only / monitor and hold).

**Urgency escalation criteria — what moves a domain from low/medium to high:**
- A pending court decision with a known date in the next 30 days
- An advocacy window closing (agency comment period, legislative whip count window, implementation deadline)
- A flag trigger that fired since the last snapshot
- Coalition contact engagement that reveals an untracked development
- A related domain has been updated and cross-references need synchronization

**Week 3 — Domain Update Sessions (4-6 hours)**
Execute domain updates for flagged domains. Priority order: (1) advocacy windows closing within 30 days; (2) domains flagged by coalition contacts as most urgent; (3) pending court decisions that will materially change the analysis.

**Week 4 — Distribution Integration**
Update the proposal's executive summary and Part I introduction to reflect new domain findings. If a significant development warrants a standalone update brief, draft it here. Update briefs are the primary vehicle for reaching audiences who have already received the proposal.

### Communicating Urgency to Coalition Partners

High-urgency domains (top 3 in the monthly snapshot) trigger two outputs:
1. **Development Alert** — a 2-4 paragraph public brief distributed within 48 hours of a significant trigger event via the distribution channels in policy-influencer-mapping.md. Format: what happened, what it means for the relevant domain, what coalition actors should do now.
2. **Monthly Current Alerts excerpt** — the urgency tier ranking for the top 5-7 domains, stripped of internal deliberation, formatted as a one-page "Monthly Framework Status" for Substack distribution or direct email.

Low-urgency domains (not in the top 7 for two consecutive months) are deprioritized without being removed from the matrix — they remain active in the cadence schedule but receive no coalition communication.

---

## Part III: Contingency Trigger Documentation

### Design Principle

A contingency trigger is an event that materially changes a load-bearing assumption in the three-wave implementation roadmap. The trigger tables in this section document: which assumptions are load-bearing, which outcomes are most likely, how each outcome changes the roadmap, and what the coordinator must do next. Six high-probability near-term triggers have pre-designed decision trees.

---

### Trigger 1: Iran WPR 60-Day Window (Decision Point: May 1-15, 2026)

**Status as of April 28**: Senate has rejected the Iran War Powers Resolution five times. The 60-day window expires approximately May 1. The administration has not certified to Congress that additional time is required. The State Department "Operation Epic Fury" memo argues the conflict is legally continuous from a pre-existing authorization.

**Branch A — Administration ignores deadline, no congressional action (highest probability)**
Domain 19f: Add Section 10 documenting complete enforcement mechanism exhaustion. This is qualitatively different from pre-deadline analysis — the proposal can now state definitively that the WPR enforcement mechanism has failed for the Iran case: notification (submitted), 60-day clock (run), congressional disapproval (voted five times, insufficient threshold), automatic termination (not enforced). Domain 34 cross-reference: funding cutoff is now the only remaining constitutional constraint; update Domain 34 analysis to note this explicitly. Roadmap: Update Wave 1 trigger table — "Iran WPR expires without compliance" is confirmed. War Powers reform is no longer preventive; it is retrospective.

**Branch B — Senate passes WPR resolution at 60-day mark (low probability)**
Domain 19f: Document the enforcement success; identify which GOP senators broke with the administration and why. Domain 1 cross-reference: if the senators who voted against Iran authorization overlap with the SAVE Act institutionalist bloc (four GOP defectors), document the coalition overlap — it strengthens the analysis that a coalition-fracture strategy is viable. Roadmap: Update Wave 1 — institutional resistance from a bipartisan bloc has appeared in both electoral and military domains.

**Branch C — Congress passes AUMF authorizing Iran operations**
Domain 19f: Document congressional capitulation rather than oversight. Domain 28 cross-reference: if Congress authorizes Iran operations by AUMF, assess whether the Venezuela precedent (arrest-operation framing as WPR avoidance) becomes moot or is reinforced as an alternative model for future executive military action.

---

### Trigger 2: Trump v. Slaughter SCOTUS Decision (Decision Point: June 2026)

**Status**: Argued December 8, 2025. Decision expected by end of June 2026. Conservative majority signaled strong support for Trump's position. If Court rules for Trump, it functionally overrules Humphrey's Executor (1935) and eliminates removal protections for independent agency commissioners — approximately two dozen agencies including FTC, FCC, CFPB, SEC, NLRB, MSPB, EEOC.

**Branch A — Court rules for Trump (high probability)**
Domain 6: Add a new subsection documenting Humphrey's Executor overruling. State explicitly that independent agency independence is structurally eliminated, not merely weakened. Domain 2 cross-reference: the same executive power logic could be extended to argue Schedule F reclassification is now constitutionally supported — update Domain 2 risk analysis. Domain 34: The agencies now subject to presidential removal include CFPB, SEC, and NLRB — update the analysis of congressional capacity to constrain executive action, noting that independent agency resistance is no longer a partial constraint. Domain 35: Document Slaughter as the term's defining administrative law decision. Roadmap: Trigger Wave 1 table entry. Supreme Court Ethics Enforcement Act and term limits legislation become more urgent as the only remaining judicial independence levers.

**Branch B — Court rules narrowly (partial probability)**
Domain 6: Document which agencies retain meaningful protection under the new framework. Domain 35: Note doctrinal ambiguity — narrowing rulings invite further litigation. Roadmap: Partial trigger. Statutory protection for specific agencies (CFPB, NLRB) may be viable.

**Branch C — Court rules for Slaughter (low probability)**
Domain 6: Document as significant institutional resilience finding. Roadmap: No trigger fires. Confirmation that some judicial backstop remains — strengthens Wave 1 assessment.

---

### Trigger 3: 2026 Midterm Election Outcomes (Decision Point: November 3, 2026)

This is the most consequential trigger for the entire implementation roadmap.

**Branch A — House flips to Democratic control**
All 35 domains: Reform pathways shift from "defensive" to "offensive." Audit all domains within 90 days for legislative pathway updates. Roadmap: Accelerate Wave 2 — compress 6-36 month window to 6-24 months. Activate pre-drafted legislation for VRA restoration, Automatic Voter Registration Act, Supreme Court Ethics Enforcement Act. Update executive summary to frame the proposal as a 24-month statutory agenda, not a crisis analysis.

**Branch B — House stays Republican, margin under 10 seats**
Domain 9 (Federalism): Elevated priority — state-federal conflict framework becomes the primary reform vehicle. Domain 33: Check whether election results shift state legislative chamber balance; identify which AG races changed coalition composition. Roadmap: Extend Wave 1 defense phase. Priority shifts to AG coalition and state-level action. No change to framing as crisis document.

**Branch C — House stays Republican, margin over 20 seats**
Roadmap: Wave 1 defense posture extended through 2028. Identify which domains have the most time-sensitive reform windows closing before 2028. Document extended timeline. The 2030 Census redistricting tracker becomes the critical long-horizon metric — which 2026 state legislative races are most consequential for 2031 map-drawing?

---

### Trigger 4: Medicaid Work Requirements (Decision Point: January 2027)

**Branch A — Federal court issues preliminary injunction before effective date**
Domain 11 and Domain 31: Note injunction, update litigation status. The reform window remains open; the fight shifts to preliminary injunction merits and circuit court review. Coalition feedback: Georgetown CCF and KFF will have real-time data on whether the injunction prevents enrollment disruption.

**Branch B — Work requirements take effect without injunction**
Domain 11 and Domain 31: This is the threshold event. Update both with live KFF and Georgetown CCF enrollment data (published within 60-90 days of implementation). Reform pathway shifts from "prevent" to "reverse" — different litigation strategy and advocacy targets. Coalition activation: Tier 3 sources (Georgetown CCF, KFF, Families USA, state Medicaid directors) will have enrollment impact data before it is publicly reported — activate the operational intelligence log in the coalition feedback tracker. Distribution: Publish an update brief specifically on Medicaid; enrollment data is a powerful advocacy document for congressional and media audiences.

---

### Trigger 5: CISA FY27 Defunding (Decision Point: September-December 2026)

**Branch A — CISA election security programs defunded in FY27 appropriations**
Domain 37: Update with funding cut. Activate Contingency Scenario B: state-only election security. Identify which states have independent election security infrastructure sufficient to compensate and which do not. Domain 34: Document as the clearest case study of appropriations used to defund election security specifically. Roadmap: Update Wave 1 success criteria for elections domain — federal election infrastructure has been materially degraded.

**Branch B — CISA survives with reduced budget**
Domain 37: Note as partial success. Monitor whether reduced budget affects operational capacity (staffing, state partnerships, vulnerability assessments). No roadmap trigger fires, but domain remains at high urgency through November 2026.

---

### Trigger 6: FISA Section 702 Post-April 30 Outcome (Decision Point: May 2026)

**Branch A — Short-term extension passes**
Surveillance-tracking.md: Update with specific extension vehicle, duration, and any reform provisions included (specifically: whether the attorney-level approval reform was included). No domain trigger fires.

**Branch B — Full lapse**
Surveillance-tracking.md: Document the lapse. Analysis: technology company legal challenge window opens; shift to EO 12333 authorities (less constrained, no judicial oversight requirement); data broker loophole (commercial location data used by ICE/DHS) remains completely unaddressed regardless of Section 702 outcome. Domain 21: Update with shift in surveillance legal landscape. Distribution: The lapse is a significant news hook; publish a Development Alert within 48 hours.

---

### Simultaneous Trigger Protocol

If two triggers fire in the same monitoring cycle, complete entries for both and assess whether simultaneous firing indicates a pattern rather than two independent events. For example: if Iran WPR Branch A fires simultaneously with CISA defunding, the combined assessment is that two distinct constitutional constraint mechanisms (war powers oversight + election security infrastructure) have been disabled in the same 90-day window — this is domain 34 material and warrants a combined update brief rather than two separate domain updates.

---

## Part IV: Coalition Feedback Loop

### Intake Process

When a Tier 1 or Tier 2 contact from policy-influencer-mapping.md engages substantively with the proposal, the structured intake form in phase-3-monitoring-infrastructure-2026.md Part IV should be used. The form covers five areas: domain gap assessment (rating each relevant domain 1-5 with primary gaps); operational intelligence (most important development in the past 30 days not yet publicly reported; pending decisions in the next 90 days); framework utility assessment (how the contact has used the proposal); Phase 3 research direction rankings; and signals that require revision (court ruling, legislative action, international precedent, closed advocacy window, contradicting empirical data).

Processing protocol: log contact in coalition feedback tracker → assess each domain gap against current document content → flag pending decisions for entry into the monthly crisis snapshot pending decision calendar → route research direction rankings to the expansion roadmap prioritization matrix → queue any domain for update if Section E revision signals are checked → send acknowledgment within 5 business days.

### How Institutional Input Changes Domain Prioritization

**From legislative Tier 1 contacts (senators and House members):** Congressional staff responses flag which domains are immediately actionable given current committee activity. Senator Whitehouse staff engaging with Domain 6 signals judicial independence legislation is a viable vehicle; that signal should update Tier 2 monitoring priority order — the most actively legislated domains become the highest-priority human-curated monitoring. This is the only mechanism by which legislative calendar intelligence enters the monitoring matrix.

**From think tanks and law school Tier 1-2 contacts:** Academic responses identify where the proposal's analysis is incomplete or where significant recent scholarship has not been incorporated. Ryan Goodman (Just Security) engagement would validate the litigation tracker and Domain 6 analysis; Erica Chenoweth engagement would validate the mobilization theory in the implementation roadmap. These responses constitute expert peer review and should be treated as domain update candidates — they are the highest-quality external input available for substantive accuracy.

**From labor, civil rights, and state-level Tier 3 contacts:** These organizations have operational knowledge not publicly reported. An AFL-CIO contact engaging with Domain 15 will know which NLRB cases are most consequential before they reach public reporting. A state Medicaid director contact engaging with Domain 31 will know whether the June 2026 HHS guidance has substantive content three weeks before it is published. This operational intelligence is the highest-value input for domain monitoring and should be treated as confidential coalition intelligence.

### The Feedback-to-Priority Loop

Coalition engagement → identify most-engaged domains → elevate to Tier 2 human-curated monitoring → execute targeted domain updates → distribute updates specifically to engaged contacts → deepen engagement with evidence that the framework responds to their input → generates further engagement. This loop is the mechanism by which the proposal becomes a living document. The monitoring infrastructure is not only about currency — it is about creating ongoing relationships with institutional constituencies that are the foundation of any implementation strategy.

### Feedback Solicitation Cadence

- Initial intake form: sent when a Tier 1-2 contact engages substantively with the proposal for the first time
- 90-day follow-up: a one-question check-in ("has anything in your domain area changed materially since we last connected?")
- Annual structural feedback: sent to all active contacts in December/January, timed to inform the January structural refresh
- Event-triggered outreach: after any significant trigger event in a contact's domain area, a targeted 48-hour Development Alert also serves as a feedback solicitation ("does this assessment match what you're seeing?")

---

## Part V: Publication and Credibility Strategy

### What Should Be Published

**Domain update documents:** When a domain is updated with new citations and analysis, distribute an update brief to the proposal's recipient list with a one-paragraph summary of what changed and why. This serves two functions: demonstrates ongoing currency to audiences evaluating whether to act on the proposal, and gives unengaged contacts a second-touch reason to read it.

**Monthly Current Alerts excerpt:** The snapshot's identification of the 5-7 most urgent domains can be published as a "Current Alerts" section on a public-facing Substack or brief. The urgency ranking is a news hook — it tells journalists, advocates, and policy staff what the framework's current assessment is without requiring them to read 35 domains. The public version omits specific trigger-to-roadmap analysis and internal action decisions.

**The litigation tracker:** `litigation-tracker-2026.md` is already designed for public distribution. Significant new case additions — especially cases filed against voting rights, judicial independence, or executive overreach — should be distributed immediately via the channels in policy-influencer-mapping.md.

**The three public trackers:** `first-amendment-suppression.md`, `environmental-rollbacks-tracker.md`, and `police-brutality-consent-decree-tracker.md` are already framed as public reference documents. Monthly update notes (dated section headers) make these function as live resources.

**Development Alerts:** Trigger-specific 2-4 paragraph public briefs distributed within 48 hours of a significant trigger event. These are the primary media engagement vehicle — journalists are attracted by timeliness of specific findings. A six-month-old framework is not newsworthy; a same-week ruling analysis is.

### What Should Be Kept Internal

**Contingency trigger logs:** The specific analysis of which roadmap pathways close under which adverse outcomes is strategic planning information. Publishing it alerts opposing actors to which outcomes matter most to the reform coalition. Share only with high-trust Tier 1 coalition contacts (from policy-influencer-mapping.md) under norms preventing further dissemination.

**Coalition feedback tracking:** Which organizations engaged with which domains, and what their specific concerns or additions were, constitutes strategic intelligence about coalition formation. Use it to inform domain sequencing and advocacy messaging; do not publish it.

**Adversary response assessment sections:** Analysis of which opposition responses are most likely for each domain should be shared only with coalition partners who have agreed to work on implementation, not distributed broadly.

**Engagement metrics and contact pipeline:** Tracking which contacts have received the proposal, whether they responded, and their feedback is operational information that, if published, would compromise the relationship-building dynamic that makes the distribution strategy work.

### Authority Maintenance: The Key Insight

Institutional audiences (law school clinics, AG offices, congressional staff) adopt frameworks they can cite with confidence that the citation will not be outdated by the time a document goes through institutional review. The monthly update brief mechanism gives institutional partners who have already received the proposal a reason to keep it in active circulation. "The March update brief shows the proposal was updated to reflect the Slaughter ruling" is a sentence a staffer can include in an internal memo to justify continuing to cite the framework. Without that update mechanism, institutional adoption degrades over time regardless of initial quality.

---

## Part VI: Implementation Roadmap Integration

### How Real-Time Monitoring Changes Part IV Recommendations

The three-wave implementation roadmap (democratic-renewal-proposal.md Part IV) was written in April 2026 against specific assumptions. The monitoring infrastructure's core function is to maintain alignment between those assumptions and evolving conditions. Five integration points matter most:

**Wave 1 assumption alignment (monthly check):** Wave 1 success requires courts to function as a check, elections to proceed without federal suppression, and the civil service to retain minimum staffing. Each Monthly Crisis Snapshot Section 7 (Roadmap Trigger Assessment) checks whether these criteria are being met. If the trigger table shows two or more Wave 1 criteria degraded, the Wave 2 preparation timeline should accelerate — Wave 2 is designed to proceed on the assumption that some institutional floor exists, but that assumption must be actively monitored rather than assumed.

**Election trigger (November 3, 2026):** The 2026 midterms are the single most consequential variable in the recovery sequence. The Trigger 3 decision tree (above) pre-designs the roadmap adaptation for each outcome — these adaptations are not drafted when results are known, they are executed from pre-designed plans that have been reviewed and refined during the monitoring period.

**Domain-specific roadmap updates:** When a domain is materially updated following a trigger event, the relevant section of the implementation roadmap should be cross-referenced. The roadmap document (democratic-renewal-proposal.md Section 4.1-4.4) is not updated on every domain change — only when a trigger-table event fires. Domain updates without trigger events are recorded in WORKLOG.md and noted in the Monthly Crisis Snapshot but do not require roadmap revision.

**Structural refresh at January and June:** Twice per year, the full 35-domain matrix should be reviewed against the trigger tables for assumption validity. This assessment produces: (a) updated trigger table with new assumptions identified, (b) domains requiring full rewrites rather than incremental updates, (c) any new domains warranting addition. The January 2027 structural refresh is also the point at which the 2026 midterm trigger analysis is fully integrated into the roadmap.

**Revision cycle:** The proposal's Part IV implementation roadmap is a living document. The monitoring infrastructure's contribution to that document is: (1) monthly snapshot records of which assumptions are holding; (2) trigger log entries when assumptions are violated; (3) annual structural refresh assessments. The roadmap should be formally revised when a trigger fires (immediate) and when a structural refresh produces material new findings (twice per year).

---

## Part VII: Automation and Tools

### What Can Be Fully Automated (Zero Marginal Coordinator Time)

**CourtListener docket alerts** — free, immediate, adequate for two-week update standard. Setup: create free account at courtlistener.com, navigate to case docket, select "Get Alerts," choose email delivery. Cases to set immediately: Trump v. Slaughter (Domain 6); Watson v. RNC (Domain 1); Louisiana v. Callais (Domain 1); SPLC v. United States docket (Domain 29); Cleveland and Oakland consent decree cases (Domains 6 and 7). Alert delivery: email within ~30 minutes of court RSS update. SCOTUS cases update Monday mornings.

**Federal Register agency email subscriptions** — free, daily digest. Setup: federalregister.gov → agency page → green "subscribe" → email. Subscribe to: CMS (Domains 11, 31 — June 2026 Medicaid guidance); HHS (Domain 11 work requirements); DOJ (Domain 29); OPM (Domain 2 civil service rules); EPA (Domain 12). Custom keyword alerts (e.g., "apportionment" for Domain 34 OMB holds) can be set via the Federal Register API.

**Democracy Docket newsletter** — free, breaks election case news. Subscribe at newsletters.democracydocket.com. Adequate for Domain 1 and Domain 37 monitoring for the 2026 election cycle. Supplement with manual monthly check of the case tracker for priority states: Arizona, Georgia, Michigan, Pennsylvania, Wisconsin.

**Google Alert: "GAO Impoundment Control Act"** — free, delivers GAO ICA reports within 24 hours of publication. This is the primary alert mechanism for Domain 34 impoundment monitoring.

**Congress.gov API** — free with API key. Configure keyword monitoring for VRA reauthorization activity, SAVE Act follow-on legislation, and Electoral Count Act amendments. The API returns bill status and full text; updates within 24 hours of committee and floor action.

### What Requires Human Review

**LegiScan API** — free tier supports demand-pull (coordinator queries when needed); paid push tier delivers updates every 15 minutes to 4 hours. Recommended: use free tier for monthly Domain 33 manual checks May-August 2026; upgrade to push for September-November 2026 (election cycle monitoring window). Configure keyword searches for: "ballot initiative supermajority," "redistricting," "voter ID," "preemption ordinance," "election administration." Known gap: Texas odd-year sessions and other non-standard legislative calendars create partial coverage gaps.

**Just Security Litigation Tracker** — weekday manual screening by Just Security staff, adequate lag for two-week update standard. Check on the first Monday of each month as part of the automated monitoring review (Section 1 of the Monthly Crisis Snapshot). Flag any case that appears in both the Just Security tracker and a domain flag trigger.

**KFF and Georgetown CCF Medicaid data** — KFF publishes state-by-state enrollment data monthly, approximately six weeks after reference month. Georgetown CCF publishes impact analyses within 2-4 weeks of new guidance. Protocol: check kff.org/medicaid on the first Monday of each month; check ccf.georgetown.edu around the first of each month for new analyses.

**OMB apportionment monitoring** — USASpending.gov API provides obligation data but does not directly flag gaps between appropriated and obligated funds. Manual quarterly check of OMB.gov/apportionment for Category C footnotes. The Google Alert for "GAO Impoundment Control Act" handles near-real-time formal ICA referrals.

**SCOTUSblog cert monitoring** — no automated alerts available. Manual check every Monday at 9:30 AM ET for orders list during the October 2025-June 2026 term (all remaining decisions including Slaughter are in this window). Cornell LII email subscriptions cover decision syllabi. SCOTUSblog's "Petitions We're Watching" weekly column covers cert-stage monitoring.

### Custom-Build vs. Off-Shelf Recommendation

No custom infrastructure is needed for the monitoring matrix as designed. Every tool listed above is either free or available at low cost on existing platforms. The minimal viable dashboard is a maintained Markdown file (the Monthly Crisis Snapshot template) with the domain status table columns: Domain | Tier | Last Reviewed | Last Event | Flag Triggered? | Next Review Date | Update Needed?

If a digital dashboard with filtering and notification is preferred: Airtable's free tier supports up to 1,000 records and can send email notifications when a record is updated — sufficient for a 37-domain monitoring matrix. Notion's free tier supports the same function with better text integration for the contingency trigger log and coalition feedback tracker. Neither requires custom development.

The one tool worth custom development if the program scales to multiple coordinators: a shared Airtable base with the domain status table, trigger log, and coalition feedback tracker integrated — replacing three separate Markdown files with a single queryable database. Estimated setup time: 4-6 hours. Justified if the program reaches three or more active coordinators.

### Full Tool Inventory

| Source | Coverage | Access | Cost |
|--------|----------|--------|------|
| [CourtListener](https://www.courtlistener.com/) | Federal district + appellate + SCOTUS dockets | Docket alerts via email; REST API | Free |
| [Democracy Docket](https://www.democracydocket.com/cases/) | Voting rights litigation, all 50 states | RSS; newsletter | Free |
| [Just Security Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/) | All administration challenges | Manual weekly check | Free |
| [Congress.gov API](https://api.congress.gov/) | Federal bill status and text | REST API (free key) | Free |
| [LegiScan API](https://legiscan.com/legiscan) | 50-state bill tracking | REST API; push tier available | Free / paid push |
| [FEC.gov Data](https://www.fec.gov/data/) | Campaign finance, PAC filings, dark money | REST API; bulk download | Free |
| [Federal Register](https://www.federalregister.gov/) | Agency rulemaking, proposed and final rules | API; email alerts by agency | Free |
| [USASpending.gov](https://usaspending.gov/) | Federal obligations vs. appropriations | REST API | Free |
| [SCOTUSblog](https://www.scotusblog.com/) | Cert petitions, orders, argument calendar | Manual weekly; no API | Free |
| [Harvard EELP Regulatory Tracker](https://eelp.law.harvard.edu/regulatory-tracker/) | Environmental rollbacks, agency-by-agency | Manual | Free |
| [KFF Medicaid Tracker](https://www.kff.org/medicaid/) | Medicaid enrollment, waiver status | Manual | Free |
| [Georgetown CCF](https://ccf.georgetown.edu/) | Medicaid state-by-state impact | Manual | Free |
| [PACER](https://pacer.uscourts.gov/) | Federal court dockets | Per-page fee after $30 quarterly waiver | ~Free limited use |

---

## Confidence Assessment

**High confidence:** Tier 1 monitoring sources — all operational, free, and actively maintained as of April 2026. Monthly refresh protocol — demonstrated achievable in Sessions 529-530. Trigger table for Wave 1 — based on documented outcomes with known decision-point dates. Iran WPR Branch A (administration non-compliance) — five failed Senate resolutions make this the near-certain outcome; can be treated as confirmed pending May 1 deadline. Slaughter decision timeline — confirmed argued December 8, 2025; decision expected by end of June 2026 term.

**Medium confidence:** Coalition feedback architecture — depends on successful Tier 1 distribution engagement, which has not yet begun; the form and process are designed but their utility is demonstrated only once used. Wave 2 and 3 trigger tables — longer-horizon assumptions are necessarily more speculative; review at January 2027 structural refresh. Airtable dashboard recommendation — feasible at free tier but requires coordinator technical setup.

**Evidence gaps:** Tier 3 coalition-fed monitoring sources depend on relationships that do not yet exist — closes as distribution proceeds. LegiScan has known coverage gaps in non-standard legislative calendar states. FEC dark money tracking has a structural 6-8 week lag on 501(c)(4) spending; OpenSecrets is the best available source despite this limitation. OMB apportionment data was restored August 2025 per court order but is subject to re-removal; the monitoring protocol assumes continued public availability.

---

## Immediate Setup Checklist

**Before distribution begins:**
- [ ] CourtListener alerts set: Trump v. Slaughter, Watson v. RNC, Louisiana v. Callais, Cleveland consent decree, Oakland consent decree
- [ ] Federal Register email subscriptions active: CMS, HHS, DOJ, OPM, EPA
- [ ] Democracy Docket newsletter subscription active
- [ ] Cornell LII Supreme Court decision email alerts active
- [ ] Google Alert "GAO Impoundment Control Act" active
- [ ] LegiScan free API key registered; Domain 33 keyword searches configured
- [ ] Monthly Crisis Snapshot template (templates/monthly-snapshot-template.md) downloaded and ready for May 2026

**Within 30 days of distribution launch:**
- [ ] Complete first Monthly Crisis Snapshot (identify 5-7 most urgent domains given Iran WPR and FISA outcomes now known)
- [ ] Send Development Alert for any trigger event occurring in May 2026
- [ ] Begin tracking Tier 1 contact responses in coalition feedback tracker

**60-90 days post-launch:**
- [ ] Evaluate which Tier 3 coalition sources have become active; promote active sources to Tier 2 curated monitoring
- [ ] Complete first quarterly review of Tier 2 domains on quarterly cadence
- [ ] Assess Wave 1 trigger table — are assumptions holding?
- [ ] Slaughter decision (by end of June) — execute Tree 2 decision tree immediately upon ruling

---

## Sources

- [CourtListener Docket Alerts Documentation](https://www.courtlistener.com/help/alerts/)
- [CourtListener Legal Alert APIs](https://www.courtlistener.com/help/api/rest/alerts/)
- [Democracy Docket Case Tracker](https://www.democracydocket.com/cases/)
- [Democracy Docket Newsletter Subscriptions](https://newsletters.democracydocket.com/)
- [Just Security Litigation Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/)
- [Just Security Anti-Corruption Tracker](https://www.justsecurity.org/117267/anti-corruption-tracker/)
- [Just Security Litigation Tracker Relaunch](https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/)
- [SCOTUSblog Trump v. Slaughter case page](https://www.scotusblog.com/cases/case-files/trump-v-slaughter-2/)
- [SCOTUS Orders of the Court 2026](https://www.supremecourt.gov/orders/ordersofthecourt/26)
- [Congress.gov API](https://api.congress.gov/)
- [LegiScan API Documentation](https://legiscan.com/legiscan)
- [LegiScan Push API User Manual v1.91](https://api.legiscan.com/dl/LegiScan_API_User_Manual.pdf)
- [FEC Campaign Finance Data](https://www.fec.gov/data/)
- [FEC Reports Due in 2026](https://www.fec.gov/updates/reports-due-in-2026/)
- [OpenSecrets Dark Money Tracking](https://www.opensecrets.org/dark-money/basics)
- [Brennan Center — Dark Money Hit Record High $1.9B in 2024](https://www.brennancenter.org/our-work/research-reports/dark-money-hit-record-high-19-billion-2024-federal-races)
- [Federal Register Subscription Options](https://www.federalregister.gov/reader-aids/using-federalregister-gov/subscription-options-and-managing-your-subscriptions)
- [USASpending.gov API](https://api.usaspending.gov/)
- [Harvard EELP Regulatory Tracker](https://eelp.law.harvard.edu/regulatory-tracker/)
- [KFF Medicaid Tracker](https://www.kff.org/medicaid/)
- [Georgetown Center for Children and Families](https://ccf.georgetown.edu/)
- [CRS Report: OMB Apportionment Reporting](https://www.congress.gov/crs-product/IN12538)
- [GAO Letter to OMB on Apportionments](https://www.gao.gov/products/e12062)
- [Time: Iran War WPR Congress, April 2026](https://time.com/article/2026/04/22/as-iran-war-nears-two-month-congress-continues-to-forgo-oversight-role/)
- [Democracy Now: Senate Defeats Iran WPR Fifth Time](https://www.democracynow.org/2026/4/23/headlines/senate_republicans_defeat_iran_war_powers_resolution_for_fifth_time)
- [CNN: War Powers Act analysis, April 25 2026](https://www.cnn.com/2026/04/25/politics/war-powers-act-trump-iran-war-congress-analysis)
- [Constitutional Accountability Center: Trump v. Slaughter](https://www.theusconstitution.org/litigation/slaughter-v-trump/)
- [Cornell LII SCOTUS Subscriptions](https://www.law.cornell.edu/supct/subscribe.html)
- [Public Rights Project](https://www.publicrightsproject.org/)
- [National Immigration Litigation Alliance](https://immigrationlitigation.org/)
- [Democracy Forward Research](https://democracyforward.org/work/research/)

---

*Production-ready unified document. Supersedes monitoring-infrastructure-2026.md and phase-3-monitoring-infrastructure-2026.md for the purposes of reference and distribution; those documents remain available for their detailed template references and extended contingency trees. Operational templates remain in templates/ and monitoring/templates/. Session 609.*
