---
title: "Phase 3 Crisis Monitoring Infrastructure — Deep Design Document"
subtitle: "Extending monitoring-infrastructure-2026.md with contingency trees, domain cadence matrix, technical automation specs, and coalition intake architecture"
date: 2026-04-28
status: production-ready
phase: 3
project: resistance-research
word_count: ~4,200
extends: monitoring-infrastructure-2026.md
cross_references:
  - monitoring/templates/monthly-crisis-snapshot.md
  - monitoring/templates/contingency-trigger-log.md
  - monitoring/templates/coalition-feedback-tracker.md
  - policy-influencer-mapping.md
  - implementation-roadmap.md
  - domains/domain-19f-war-powers-reform.md
  - domains/domain-06-judicial-independence.md
---

# Phase 3 Crisis Monitoring Infrastructure — Deep Design Document

*April 28, 2026 — Extends monitoring-infrastructure-2026.md with four components that document left as design intentions: explicit contingency decision trees, per-domain review cadence matrix, technical automation specifications, and coalition feedback intake architecture.*

---

## The Four Gaps This Document Fills

The monitoring infrastructure document (Session 531) established the three-tier monitoring matrix, trigger tables, monthly cadence protocol, and publication strategy. It left four design components at the intention level rather than the implementation level:

1. **Contingency documentation** was structured as trigger tables (if X, then Y) but did not provide the branching logic that allows a coordinator to determine which specific domain text changes when a trigger fires — or what happens when two triggers fire simultaneously.

2. **Domain review cadence** was described as "monthly vs. quarterly vs. annual" but not assigned to specific domains, leaving the coordinator without a maintenance calendar.

3. **Technical automation** was described by source name but not by implementation method — a coordinator reading the infrastructure document knows *what* to monitor but not *how to set up* the monitoring without additional research.

4. **Coalition feedback** was described architecturally but the intake form itself — what questions to ask, how to structure responses, what to do with them — was not produced.

This document resolves all four gaps.

---

## Part I: Contingency Decision Trees

### Design Principle

A contingency decision tree answers: given that trigger event X has occurred, which specific text in which specific domain documents changes, and in which direction? The trigger table in monitoring-infrastructure-2026.md Part II records *that* a trigger fires and *what assumption is violated*. The decision tree records *exactly what the coordinator must do next*.

The trees below cover the six highest-probability near-term triggers (all with decision points in May–November 2026) and two longer-horizon triggers that are structurally important enough to pre-design.

---

### Tree 1: Iran WPR 60-Day Window Outcome (Decision Point: May 1–15, 2026)

**Status as of April 28, 2026**: The Senate has rejected the Iran War Powers Resolution five times. The 60-day window expires approximately May 1. The administration has not certified to Congress that additional time is needed for safe troop withdrawal. The State Department "Operation Epic Fury" memo (April 21) argues the conflict is legally continuous from a pre-existing authorization. Domain 19f has been updated with the pre-deadline legal analysis.

**Branch A — Administration claims compliance or ignores deadline without congressional action**

This is the highest-probability outcome based on the pattern of five Senate rejections and administration non-compliance posture.

- Domain 19f: Add Section 10 documenting the post-deadline legal vacuum. The constitutional enforcement mechanism has now been exhausted in full: notification (submitted), 60-day clock (run), congressional disapproval (voted five times, insufficient threshold), automatic termination (not enforced). This is qualitatively different from pre-deadline analysis — the proposal can now state definitively that the WPR enforcement mechanism has failed for the Iran case.
- Domain 34 (Power-of-the-Purse): Cross-reference. The funding cutoff mechanism (cutting appropriations for unauthorized operations) is now the only remaining constitutional enforcement tool. Add to Domain 34 analysis: Congress has the authority to refuse appropriations for Iran operations. This cross-reference makes Domain 34 more urgent.
- Implementation roadmap: Update Wave 1 trigger "Iran WPR 60-day window expires without compliance" as confirmed. Note: Phase IV risk assessment shifts — two constitutional constraints (WPR notification process, congressional disapproval vote) have now both failed. War Powers reform is no longer preventive; it is retrospective.

**Branch B — Senate passes War Powers Resolution at 60-day mark (low probability)**

If a 60-vote WPR resolution passes, this would represent the first successful congressional constraint of a Trump military action.

- Domain 19f: Document the enforcement success. Identify which GOP senators flipped and why (Senator Curtis's position on record; others?). Update the Domain 19f reform pathway analysis — enforcement is possible when the right political coalition forms.
- Domain 1 cross-reference: The same institutionalist bloc that blocked SAVE Act (four GOP defectors) would be relevant here. Document overlap if senators who voted against Iran authorization are the same group.
- Implementation roadmap: Update Wave 1 — institutional resistance from a bipartisan bloc has now appeared in both electoral and military domains. Strengthens the analysis that a coalition-fracture strategy is viable.

**Branch C — Congress passes AUMF authorizing Iran operations**

- Domain 19f: Document the authorization. Update the Domain 19f reform analysis — congressional capitulation rather than oversight. Note which senators shifted from opposition to authorization.
- Domain 28 (Venezuela): Cross-reference. If Congress authorizes Iran operations by AUMF, assess whether the Venezuela precedent (arrest-operation framing as WPR avoidance) becomes moot or is reinforced as an alternative strategy.

---

### Tree 2: Trump v. Slaughter SCOTUS Decision (Decision Point: June 2026)

**Status**: Argued December 8, 2025. Decision expected by end of June 2026. Conservative majority signaled strong support for the administration's position. If the Court rules for Trump, it functionally overrules Humphrey's Executor (1935) and eliminates removal protections for independent agency commissioners.

**Branch A — Court rules for Trump (high probability)**

- Domain 6 (Judicial Independence): Add a new subsection documenting Humphrey's Executor overruling. This is a landmark shift in administrative law — the proposal should state explicitly that independent agency independence is now structurally eliminated, not merely weakened. Document which agencies are immediately affected (FTC, FCC, CFPB, SEC, NLRB, MSPB, EEOC — approximately two dozen agencies).
- Domain 2 (Civil Service): Cross-reference. The same executive power logic that eliminates commissioner independence could be extended to argue that Schedule F reclassification is now constitutionally supported by Slaughter. Update Domain 2 risk analysis.
- Domain 35 (SCOTUS 2026 Term Preview): Document Slaughter as the term's defining administrative law decision. Update the Domain 35 summary of OT2025 outcomes.
- Domain 34 (Power-of-the-Purse): The agencies now subject to presidential removal include the CFPB (consumer financial protection), SEC (securities regulation), and NLRB (labor protection). Update Domain 34's analysis of congressional capacity to constrain executive action — Congress can no longer rely on independent agency resistance as a partial constraint.
- Implementation roadmap: Trigger the Wave 1 table entry. Update: "Domain 6 reform pathways: statutory options require explicit Constitutional amendment framing; add to Wave 1 urgency list." Specifically, Supreme Court Ethics Enforcement Act and term limits legislation become more urgent as the only remaining judicial independence levers.

**Branch B — Court rules narrowly (partial probability)**

If the Court rules that Humphrey's Executor survives but is significantly narrowed — for example, allowing removal of commissioners for policy disagreement but not pure partisanship — the analysis is more complex.

- Domain 6: Document the narrowing. Identify which agencies retain meaningful protection and which do not under the new framework.
- Domain 35: Note the doctrinal ambiguity — narrowing rulings invite further litigation.
- Implementation roadmap: Partial trigger. Wave 1 adaptation required but less severe than full overruling. Statutory protection for specific agencies (CFPB, NLRB) may be viable.

**Branch C — Court rules for Slaughter (low probability)**

- Domain 6: Document as a significant institutional resilience finding. Note it as evidence that the six-justice conservative majority has limits.
- Domain 35: Significant finding for OT2026 independence — the Court did not follow oral argument signals.
- Implementation roadmap: No trigger fires. Note the confirmation that some judicial backstop remains.

---

### Tree 3: 2026 Midterm Election Outcomes (Decision Point: November 2026)

This is the most consequential trigger for the entire implementation roadmap. Three outcome branches.

**Branch A — House flips to Democratic control**

- Roadmap: Accelerate Wave 2. Compress the 6-36 month window to 6-24 months. Immediately activate pre-drafted legislation for Voting Rights Act restoration, Automatic Voter Registration Act, Supreme Court Ethics Enforcement Act.
- All 35 domains: The reform pathways section of each domain shifts from "defensive" (prevent further erosion) to "offensive" (legislative restoration). Each domain should be audited within 90 days of the election for legislative pathway updates.
- Distribution strategy: The proposal becomes a legislative briefing document. Update the executive summary to frame it as a 24-month statutory agenda, not a crisis analysis.

**Branch B — House stays Republican with margin under 10 seats**

- Roadmap: Extend Wave 1 defense phase. No legislative window opens. Focus shifts to AG coalition + state-level action.
- Domain 9 (Federalism): Elevated priority. The state-federal conflict framework becomes the primary reform vehicle.
- Domain 33 (State Legislative Autocratization): Check whether the election results shift the balance of state legislative chambers. Identify which state attorney general races changed the coalition composition.
- Distribution strategy: No change to framing as a crisis document. Priority shifts to state-level institutional partners.

**Branch C — House stays Republican with margin over 20 seats**

- Roadmap: Wave 1 defense posture extended through 2028. Assess whether any Wave 2 preparation can begin independently of legislative success.
- Implementation roadmap: Document the extended timeline. Update the 2028 election preparation analysis. Identify which domains have the most time-sensitive reform windows that will close between 2026 and 2028.

---

### Tree 4: Medicaid Work Requirements (Decision Point: January 2027)

**Background**: The OBBBA Medicaid provisions include work requirements scheduled for effective implementation in 2027. If no injunction is secured, requirements take effect and enrollment drops begin.

**Branch A — Federal court issues preliminary injunction before effective date**

- Domain 11 (Healthcare Access): Note the injunction. Update the litigation status. The reform window remains open — the fight shifts to the preliminary injunction merits and ultimate circuit court review.
- Domain 31 (Healthcare Medicaid): Cross-reference. The injunction buys time for coalition action at both federal and state levels.

**Branch B — Work requirements take effect without injunction**

- Domain 11 and Domain 31: This is the threshold event. Update both domains with live enrollment data (KFF and Georgetown CCF will publish state-by-state impact within 60-90 days of implementation). The reform pathway shifts from "prevent" to "reverse."
- Coalition feedback: This trigger most directly affects Tier 3 coalition sources (Georgetown CCF, KFF, Families USA, state Medicaid directors). Activate the operational intelligence log in the coalition feedback tracker. These sources will have enrollment impact data before it is publicly reported.
- Distribution strategy: Publish an update brief specifically on Medicaid — the enrollment data is a powerful advocacy document for congressional and media audiences.

---

### Tree 5: CISA FY27 Defunding (Decision Point: September–December 2026)

**Branch A — CISA election security programs defunded in FY27 continuing resolution or appropriations**

- Domain 37 (2026 Midterm Interference): Update with the funding cut. Activate Contingency Scenario B: state-only election security. Identify which states have independent election security infrastructure sufficient to compensate and which do not.
- Domain 34 (Power-of-the-Purse): Document as evidence that appropriations are being used to defund election security specifically. This is the domain's clearest case study.
- Implementation roadmap: Update Wave 1 success criteria for elections domain. Document that federal election infrastructure has been materially degraded.

**Branch B — CISA survives FY27 with reduced but functional budget**

- Domain 37: Note as partial success. Monitor whether reduced budget affects operational capacity (staffing, state partnerships, vulnerability assessments).

---

### Tree 6: FISA Section 702 Post-April 30 Outcome (Decision Point: May 2026)

**Background**: The 10-day stopgap expires April 30. The Foreign Intelligence Accountability Act (3-year proposal) has been introduced but not voted on.

**Branch A — Short-term extension passes, surveillance-tracking.md update needed**

- Surveillance-tracking.md: Update with the specific extension vehicle, duration, and any reform provisions. Note whether the attorney-level approval reform was included.

**Branch B — Full lapse (no extension)**

- Surveillance-tracking.md: Document the lapse. Add analysis of what this means in practice: technology company legal challenge window opens; shift to EO 12333 authorities (less legally constrained, no judicial oversight requirement); data broker loophole (commercial location data used by ICE/DHS) remains completely unaddressed regardless of Section 702 outcome.
- Domain 21 (Surveillance/Privacy): If this domain exists as a separate file, update it. If not, ensure surveillance-tracking.md cross-references are current.
- Distribution strategy: The lapse is a significant news hook. Publish an update brief specifically on the surveillance gap.

---

## Part II: Domain Review Cadence Matrix

The following table formalizes which review cadence applies to each of the 35 base domains plus the 6 April 2026 updates. The cadence is assigned based on: (1) how rapidly the domain's situation changes; (2) whether automated monitoring sources provide reliable real-time signals; and (3) whether pending decisions create near-term inflection points.

**Review cadence definitions**:
- **Monthly** — review at every Monthly Crisis Snapshot; flag triggers checked weekly
- **Quarterly** — review at January, April, July, October structural checkpoints
- **Annual** — review at January structural refresh only; no pending near-term triggers

| Domain | Cadence | Rationale | Primary Alert Source |
|--------|---------|-----------|---------------------|
| Domain 1 — Voting Rights and Elections | **Monthly** | 2026 election cycle; active litigation | Democracy Docket RSS; CourtListener alerts |
| Domain 2 — Civil Service and Executive Constraint | **Monthly** | Schedule F litigation active; Slaughter cross-impact | OPM workforce data; MSPB appeal statistics |
| Domain 3 — Immigration Enforcement | **Monthly** | ICE operational tempo; litigation volume | National Immigration Litigation Alliance weekly |
| Domain 4 — Economic Policy | **Quarterly** | Tariff litigation ongoing; CIT decisions | Court of International Trade docket; CBO reports |
| Domain 5 — Social Safety Net | **Quarterly** | OBBBA implementation timeline; quarterly HHS data | KFF monthly enrollment; CMS guidance |
| Domain 6 — Judicial Independence | **Monthly** | Slaughter pending June 2026; shadow docket active | SCOTUS orders list (Monday); CourtListener |
| Domain 7 — Democratic Participation | **Monthly** | First Amendment tracker cross-reference; protest policing | First Amendment tracker monthly review |
| Domain 8 — Media and Press Freedom | **Monthly** | Pentagon corridor litigation; press pool actions | Reporters Committee weekly alerts |
| Domain 9 — Federalism and State-Federal Conflict | **Monthly** | AG coalition activity; state challenges | NAAG press releases; Public Rights Project |
| Domain 10 — Tribal Sovereignty | **Quarterly** | Less active litigation currently | NARF (Native American Rights Fund) newsletter |
| Domain 11 — Healthcare Access | **Monthly** | June 2026 HHS guidance; work requirement timeline | KFF Medicaid tracker; CMS Federal Register alerts |
| Domain 12 — Environmental Justice and Climate | **Monthly** | Endangerment Finding post-effective; Earthjustice litigation | Harvard EELP tracker; Earthjustice docket |
| Domain 13 — Constitutional Amendment | **Annual** | No near-term amendment activity | NPVIC state count quarterly |
| Domain 14 — Campaign Finance | **Quarterly** | FEC filings due quarterly; DISCLOSE Act status | FEC.gov API; OpenSecrets quarterly |
| Domain 15 — Labor Rights | **Monthly** | NLRB cases; Slaughter cross-impact on NLRB independence | NLRB case decisions; AFL-CIO Tier 3 input |
| Domain 16 — Housing | **Quarterly** | HUD rulemaking; fair housing rollbacks | Federal Register HUD alerts |
| Domain 17 — Education (K-12) | **Quarterly** | Title IX guidance; DEI enforcement | Dept. of Education Federal Register alerts |
| Domain 18 — Veterans Affairs | **Annual** | Less acute crisis currently | VA Inspector General reports |
| Domain 19 — National Security | **Quarterly** | Catch-all; most specific items in 19f | Congressional Research Service reports |
| Domain 19f — War Powers Reform | **Monthly** | Iran WPR active; post-May 1 outcome pending | Senate roll call alerts; State Dept. publications |
| Domain 20 — Foreign Policy | **Quarterly** | Diplomatic corps depletion ongoing | State Department press releases |
| Domain 21 — Surveillance/Privacy | **Monthly** | FISA 702 lapse post-April 30; data broker gap | ACLU surveillance tracking; surveillance-tracking.md |
| Domain 22 — Criminal Justice | **Quarterly** | DOJ priorities; consent decree rollback | Consent decree tracker; POGO |
| Domain 23 — Trade Policy | **Monthly** | CIT 24-state challenge; Section 301 active | Court of International Trade docket |
| Domain 24 — Infrastructure | **Annual** | Bipartisan Infrastructure Law implementation | GAO reports |
| Domain 25 — Gun Rights | **Quarterly** | Second Circuit pipeline; Bruen implementation | CourtListener Second Amendment alerts |
| Domain 26 — Government Accountability | **Monthly** | IG vacancies; CREW/POGO tracking active | POGO weekly; CREW watchdog alerts |
| Domain 27 — Higher Education | **Monthly** | Harvard First Circuit pending; visa revocations | AAUP; FIRE tracker; NASFAA |
| Domain 28 — War Powers Venezuela | **Quarterly** | OLC memo set; no new operations announced | Congressional Research Service; DOJ OLC publications |
| Domain 29 — Prosecutorial Weaponization | **Monthly** | SPLC case active; DOJ pattern ongoing | Just Security anti-corruption tracker; PACER |
| Domain 30 — Reproductive Rights | **Monthly** | EMTALA litigation; state-level restrictions active | Rewire News Group; Center for Reproductive Rights |
| Domain 31 — Healthcare/Medicaid | **Monthly** | June 2026 HHS guidance; work requirement clock | Georgetown CCF; KFF; Tier 3 coalition sources |
| Domain 32 — LGBTQ+ Rights | **Monthly** | Title IX; military service ban; state bills | Lambda Legal; ACLU LGBT rights tracker |
| Domain 33 — State Legislative Autocratization | **Monthly** | 100+ bills in 15+ states; Missouri Amendment 4 | LegiScan push alerts; Democracy Docket state cases |
| Domain 34 — Congressional Power-of-the-Purse | **Monthly** | OMB apportionment restored; impoundment active | USASpending.gov API; GAO ICA reports |
| Domain 35 — SCOTUS 2026 Term Preview | **Monthly** | Slaughter June 2026; OT2026 pipeline building | SCOTUSblog cert monitoring; SCOTUS orders list |
| Domain 36 — AI Governance | **Quarterly** | No federal statute; state activity building | State legislative AI bills (LegiScan keyword); NIST |
| Domain 37 — Federal Midterm Interference | **Monthly** | CISA budget; election cycle active | CISA advisories; Democracy Docket; EAC |

**Summary counts**: Monthly (24 domains), Quarterly (10 domains), Annual (3 domains).

**Maintenance load estimate**: Monthly review of 24 domains at the flag-trigger check level requires approximately 2-3 hours per month for the Tier 1 automated sources. Human-curated review of the same 24 domains for substantive update assessment requires an additional 3-4 hours. Total monthly maintenance load: approximately 6-8 hours for a full monitoring pass.

---

## Part III: Technical Automation Specifications

### What Can Be Fully Automated (Zero Marginal Coordinator Time)

**CourtListener docket alerts (free, immediate)**

Setup: Create a free account at CourtListener.com. Navigate to any case docket and select "Get Alerts" — choose email delivery. For webhook delivery, use the Legal Alert APIs (v4.3 requires authentication). Cases to set immediately:

- Trump v. Slaughter (SCOTUS — Domain 6)
- Watson v. RNC (District — Domain 1)
- Louisiana v. Callais (SCOTUS — Domain 1)
- Any open SPLC v. United States case files (PACER number, then search CourtListener — Domain 29)
- Any open consent decree case in Cleveland and Oakland (Domain 7, consent decree tracker)

Alert delivery: email notification within ~30 minutes of a court RSS feed update. SCOTUS cases update on Monday mornings when orders lists are published.

**Federal Register agency email subscriptions (free, daily digest)**

Setup: Go to federalregister.gov → any agency page → green "subscribe" box → email option. Subscribe to:

- CMS (Centers for Medicare and Medicaid Services) — for Domain 11 and Domain 31 Medicaid guidance
- HHS (Department of Health and Human Services) — for Domain 11 work requirement guidance (June 2026 deadline)
- DOJ (Department of Justice) — for Domain 29 prosecutorial actions
- OPM (Office of Personnel Management) — for Domain 2 civil service rules
- EPA — for Domain 12 environmental rollbacks

Custom search subscriptions are also possible: set a keyword alert for "apportionment" in the Federal Register to catch any OMB notices on appropriations holds (Domain 34 cross-reference).

**LegiScan push API (free tier for monitoring; paid for real-time push)**

Setup: Register at legiscan.com for a free API key. The public API supports keyword search across 50 states. For automated monitoring of Domain 33 (state legislative autocratization), configure searches for: "ballot initiative supermajority," "redistricting," "voter ID," "preemption ordinance," "election administration."

Free tier limitation: results are pulled on demand, not pushed. For push delivery (updates every 15 minutes to 4 hours), a paid subscription is required. Recommended path: use free tier for monthly manual checks; if budget allows, upgrade to push for the 2026 election cycle monitoring window (most critical September–November 2026).

**SCOTUSblog cert monitoring (free, manual)**

SCOTUSblog does not offer automated alerts, but its weekly "Petitions We're Watching" column and the SCOTUS orders list (every Monday at 9:30 AM ET) are sufficient for weekly manual review. Cornell LII offers email subscriptions to Supreme Court decision syllabi. For cert-stage monitoring (before oral argument), the SCOTUSblog SCOTUS cases tracker is the best free resource. Set a calendar reminder for every Monday at 9:30 AM ET to check the orders list during the October 2025–June 2026 term (all remaining decisions including Slaughter are in this window).

**Democracy Docket newsletter (free)**

Setup: Subscribe at newsletters.democracydocket.com. The newsletter delivers breaking news on election cases and includes premium member access to case scoreboards. The newsletter is adequate for Domain 1 and Domain 37 monitoring. For state-level case tracking beyond the newsletter, the Democracy Docket case tracker can be checked monthly against the priority states list (Arizona, Georgia, Michigan, Pennsylvania, Wisconsin).

---

### What Requires Human Review (Cannot Be Automated)

**Just Security litigation tracker (weekday manual screening)**

Just Security's team screens new lawsuits every weekday and catalogs substantive changes. Their tracker has been relaunched with continually updated totals and improved search filters. The monitoring protocol for the democratic renewal proposal is: check the Just Security tracker on the first Monday of each month as part of the automated monitoring review (Section 1 of the monthly crisis snapshot). Flag any case that appears in both the Just Security tracker and a domain-relevant flag trigger.

Note on the tracker's methodology: Just Security relies on a team doing manual daily screening, not automated PACER crawling. This means the tracker may lag by 24-48 hours on new filings but is reliably updated on substantive developments (orders, injunctions, rulings) within one business day. For the framework's purposes, this is adequate — the proposal's update window is two weeks, not two hours.

**OMB apportionment monitoring (manual quarterly, with alert potential)**

OMB was ordered to restore apportionment data publicly on August 15, 2025 after taking it down in March 2025. Current status: publicly available but subject to re-removal. The USASpending.gov API provides obligation data but does not directly flag the gap between appropriated and obligated funds that indicates impoundment. The CRS report on OMB apportionment monitoring (congress.gov/crs-product/IN12538) documents the oversight challenge.

Monitoring protocol: Check OMB.gov/apportionment quarterly for new Category C apportionment footnotes exceeding 8% of a discretionary account. Cross-reference with USASpending.gov for obligation shortfalls. GAO ICA reports (published as GAO letter reports when impoundment concerns are identified) are the primary alert mechanism — set a Google Alert for "GAO" + "Impoundment Control Act" to catch new reports within 24 hours of publication.

**KFF Medicaid enrollment data (monthly manual)**

KFF publishes state-by-state Medicaid enrollment data monthly, approximately six weeks after the reference month. For June 2026 HHS guidance (the work requirement deadline), the Georgetown Center for Children and Families is the most timely source — they publish impact analyses within 2-4 weeks of new guidance. Protocol: check kff.org/medicaid on the first Monday of each month; check ccf.georgetown.edu around the first of each month for new analyses.

---

### Integration Into a Single Dashboard

The minimal viable dashboard for this monitoring infrastructure is a maintained Markdown file (or simple spreadsheet) with the following columns, updated monthly:

| Domain | Tier | Last Reviewed | Last Event | Flag Triggered? | Next Review Date | Update Needed? |
|--------|------|--------------|-----------|----------------|-----------------|---------------|

This table is the operational version of the domain urgency heatmap in the coalition feedback tracker. A coordinator can maintain it in the monthly crisis snapshot document (Section 1 expanded). No external tool is required — the snapshot template already serves this function if completed consistently.

If a digital dashboard is preferred: a shared Airtable or Notion database with the same columns supports the same function with better filtering and notification capabilities. Airtable's free tier supports up to 1,000 records and can send email notifications when a record is updated — sufficient for a 37-domain monitoring matrix.

---

## Part IV: Coalition Feedback Form (Structured Intake)

The coalition feedback tracker template documents ongoing engagement, but it does not specify what to ask. The following structured intake form should be used when a Tier 1 or Tier 2 coalition contact engages substantively with the proposal. It can be sent via email or administered in a brief call (20-30 minutes).

---

### Democratic Renewal Proposal — Institutional Feedback Form

*This form is for institutional partners who have reviewed the Democratic Renewal Proposal and can provide substantive domain expertise. Responses are used to update domain documents and prioritize research direction. All responses are treated as internal coalition information.*

**Contact information** (for follow-up only — not published):
- Organization name:
- Role/title:
- Primary domain areas of expertise:
- Preferred follow-up method (email / call / no follow-up needed):

---

**Section A: Domain Assessment**

For each domain your organization works on, rate the current analysis:

*Scale: 1 = significant gaps or errors; 3 = adequate; 5 = comprehensive and current*

| Domain | Rating (1-5) | Primary Gap or Error (if rating < 4) | Most Significant Recent Development Not Captured |
|--------|-------------|--------------------------------------|--------------------------------------------------|
| [List domains relevant to contact] | | | |

---

**Section B: Operational Intelligence**

These questions seek information that may not be publicly reported. Please answer only what you are able to share:

1. In your organization's area of work, what is the single most important development in the past 30 days that is not yet reflected in public reporting?

2. Are there pending court decisions, agency guidance deadlines, or legislative votes in the next 90 days that are critically important for your domain area? (Please specify case names, agencies, or bill numbers if known.)

3. In your assessment, which recommendation in the proposal most urgently needs updating given current conditions?

4. Are there proposals or legislative vehicles currently under active consideration in your domain that the framework has not captured?

---

**Section C: Framework Utility Assessment**

1. How has your organization used or cited the framework? (Check all that apply)
   - [ ] Internal briefing/background research
   - [ ] Cited in published work
   - [ ] Shared with legislative contacts
   - [ ] Shared with coalition partners
   - [ ] Used in litigation strategy
   - [ ] Not yet used

2. Which sections of the proposal are most useful for your work?

3. Which sections need the most strengthening? What specific improvements would make this more useful for your organization's work?

4. Are there other organizations we should be coordinating with that are not currently in our distribution?

---

**Section D: Phase 2 Research Direction**

The proposal is developing additional research in the following areas. Which would be most useful for your work? (Rank 1-5, with 1 being most useful):

- [ ] Litigation tracking — expanded case-by-case analysis of active challenges
- [ ] State-level implementation guides — jurisdiction-specific reform pathways
- [ ] International precedent research — comparative democratic recovery models
- [ ] Coalition coordination tools — shared organizing infrastructure
- [ ] Legislative model bills — pre-drafted statutory language for reform proposals

---

**Section E: Signals That Require Revision**

A domain recommendation needs revision when one or more of the following conditions is met. Please note whether any of these conditions are currently present in your domain area:

- [ ] A court ruling has materially changed the legal landscape assumed in the recommendation
- [ ] A legislative action has contradicted an assumption in the recommendation (e.g., a provision the proposal assumed would protect against X has been repealed)
- [ ] International precedent has established a new model that should be incorporated
- [ ] The advocacy window for a recommendation has closed or materially narrowed
- [ ] New evidence has emerged (empirical data, litigation outcomes, expert analysis) that contradicts the proposal's factual claims

*If any box is checked, please describe specifically:*

---

**Processing Protocol for Completed Forms**:

1. Log contact in coalition feedback tracker (contact engagement log section)
2. Assess each domain gap identified (Section A) against current domain document content
3. Flag any pending decisions identified (Section B, question 2) for immediate entry into the monthly crisis snapshot pending decision calendar
4. Route Phase 2 research direction rankings to the phase-2-expansion-roadmap.md prioritization matrix
5. If Section E boxes are checked, queue the affected domain for update in the next monthly work session
6. Send acknowledgment to contact within 5 business days confirming receipt and noting any updates made based on their input

---

## Part V: Publishing and Authority Strategy — Comparative Analysis

### How Think Tanks Maintain Framework Currency: Two Models

The evidence on how established policy organizations maintain currency for living-document frameworks divides into two operational models.

**Model A: Daily manual screening with selective publication (Just Security)**

Just Security's litigation tracker is updated by a team doing manual weekday screening. Updates are published continuously as cases are added or changed. The methodology is labor-intensive (daily screening of new filings) but produces a resource that institutional audiences treat as authoritative precisely because it is always current. The relaunch in 2026 added continually updated totals and improved search filters — reflecting that the tracker had become important enough to invest in better infrastructure.

What this model costs: a team of 2-4 people doing daily work. What it produces: an authoritative reference document that journalists, litigators, and legislative staff cite as the canonical case record. Authority comes from completeness and currency, not from publication brand.

**Model B: Periodic comprehensive analysis with timed publication (Brennan Center, Center for American Progress)**

Brennan Center publishes comprehensive reports on voting rights, judicial independence, and campaign finance on a periodic basis (typically 4-6 major reports per year per program area). Between major reports, they publish shorter blog posts, issue briefs, and policy updates. The major reports are designed to be definitive reference documents; the shorter updates maintain engagement and signal continued attention.

What this model costs: significant staff time for each major report (4-8 weeks of research and writing per report); lighter ongoing maintenance. What it produces: authoritative comprehensive documents that are widely cited and serve as the credentialing mechanism for the organization's authority in the space.

**Recommendation for the Democratic Renewal Proposal**:

The proposal is closer to Model B (comprehensive document) with elements of Model A (real-time tracker integration through the three public trackers). The sustainable path forward is a hybrid:

- The 35-domain proposal itself is the Model B comprehensive document — updated quarterly via the Monthly Crisis Snapshot protocol
- The three public trackers (First Amendment, environmental, police brutality) operate as Model A running trackers — updated as events occur
- Monthly update briefs (2-4 pages) serve as the between-major-report engagement mechanism, highlighting the most significant new developments and pointing back to updated domain documents

---

### What to Publish to Reinforce Framework Authority

**Publish immediately** when any of the following occur:
- A domain is materially updated with new citations (publish the update brief identifying what changed and citing the new sources)
- A trigger event from the contingency trigger log fires (publish a "Development Alert" noting the event and its implications for the relevant domain)
- A public tracker (First Amendment, environmental, police brutality) crosses a monitoring threshold (add a dated section header to the tracker and share it via the distribution channels)

**Publish monthly** regardless of specific events:
- The "Current Alerts" section of the Monthly Crisis Snapshot (the urgency tier ranking for 5-7 domains) — stripped of internal deliberation, formatted as a one-page "Monthly Framework Status" for public distribution via Substack or equivalent

**Keep internal**:
- Contingency trigger log entries (especially the adversary response pattern log)
- Coalition feedback tracker (full version — contact names, operational intelligence, engagement metrics)
- Distribution pipeline status (which contacts have been reached, who has not responded)
- The specific trigger-to-roadmap-adaptation analysis (publishing which outcomes most concern the coalition alerts opposition actors to which outcomes to produce)

---

### Effect of Real-Time Currency Publishing on Institutional Adoption

The key insight from think tank practice: institutional audiences (law school clinics, AG offices, congressional staff) adopt frameworks that they can cite with confidence that the citation will not be outdated by the time a document goes through institutional review. A proposal that is six months stale when it reaches a Senate staffer's desk is not a reference document — it is a historical artifact.

The monthly update brief mechanism serves a specific function here: it gives institutional partners who have already received the proposal a reason to keep it in active circulation. "The March update brief shows the proposal was updated to reflect the Slaughter ruling" is a sentence a staffer can include in an internal memo to justify continuing to cite the framework. Without that update mechanism, institutional adoption degrades over time regardless of initial quality.

For media attention, the dynamic is different: journalists are attracted by timeliness of specific findings (a new domain development is newsworthy; a six-month-old framework is not), so the trigger-specific Development Alerts serve the media function better than the comprehensive monthly update. Development Alerts should be distributed to the media contacts in the policy-influencer-mapping.md list as standalone one-paragraph news items within 48 hours of a significant trigger event.

---

## Implementation Roadmap: Automation First, Human Review Second

### Week 1 (Pre-Distribution — Immediate)

- Set CourtListener docket alerts for: Trump v. Slaughter, Watson v. RNC, Louisiana v. Callais, Cleveland consent decree case, Oakland consent decree case
- Subscribe to Federal Register email alerts for: CMS, HHS, DOJ, OPM, EPA
- Subscribe to Democracy Docket newsletter
- Subscribe to Cornell LII Supreme Court decision email alerts
- Set Google Alert for: "GAO Impoundment Control Act"
- Register for LegiScan free API key; configure keyword searches for Domain 33 monitoring
- Complete the first Monthly Crisis Snapshot (May 2026) — first field entry after Iran WPR outcome is known

### Weeks 2-4 (Concurrent with Distribution Launch)

- Complete contingency trigger log entries for any triggers that fire in May 2026 (Iran WPR, FISA outcome)
- Send coalition feedback form to first Tier 1 contacts as they engage with the proposal
- Publish first update brief if any trigger event occurs

### Month 2 (June 2026)

- Complete June Monthly Crisis Snapshot — Slaughter decision will be known by end of June; execute Domain 6 contingency tree as appropriate
- First full quarterly review of Tier 2 (human-curated) domains
- Assess coalition feedback from Tier 1 contacts; update domain engagement heatmap

### Months 3-6 (July–October 2026)

- Monthly rhythm fully operational
- Elevate any Tier 3 coalition sources that have become active to Tier 2 curated monitoring
- September–October: heightened monitoring cadence for all Domain 37 (midterm interference) sources
- First annual structural refresh planning begins October — to be completed January 2027

---

## Confidence Assessment

**High confidence**:
- Technical automation specifications: all sources verified operational as of April 2026
- Iran WPR May 2026 outcome: five failed Senate resolutions confirm Branch A (administration non-compliance) is the highest-probability outcome; Domain 19f contingency tree Branch A can be treated as near-certain
- Slaughter decision timeline: confirmed argued December 8, decision expected June 2026 end of term
- Just Security tracker methodology: confirmed weekday manual screening; adequate for monthly monitoring pass

**Medium confidence**:
- Midterm election contingency trees: outcome is uncertain; all three branches need to be designed in advance but probability weighting is not possible
- Coalition feedback form adoption: depends on Tier 1 contacts engaging substantively; form utility is proven only once used
- Airtable dashboard recommendation: feasible at free tier but requires coordinator technical setup; if coordinator is not technically oriented, the Markdown file approach is lower-risk

**Evidence gaps**:
- OMB apportionment data: restored August 2025 per court order, but the political commitment to maintaining access is uncertain; the monitoring protocol assumes continued public availability
- LegiScan coverage gaps: the existing infrastructure document correctly notes that Texas odd-year sessions and other non-standard legislative calendars create partial gaps; these are structural limitations of the API
- FEC dark money lag: the 6-8 week reporting lag on 501(c)(4) spending identified in the infrastructure document is confirmed by FEC API documentation; OpenSecrets remains the best available source for near-real-time dark money analysis despite this limitation

---

## Sources

- [CourtListener Docket Alerts Documentation](https://www.courtlistener.com/help/alerts/)
- [CourtListener Legal Alert APIs](https://www.courtlistener.com/help/api/rest/alerts/)
- [CourtListener Webhook API](https://www.courtlistener.com/help/api/webhooks/)
- [CourtListener REST API v4.3 Changes](https://www.courtlistener.com/help/api/rest/changes/)
- [Just Security Litigation Tracker](https://www.justsecurity.org/107087/tracker-litigation-legal-challenges-trump-administration/)
- [Just Security Litigation Tracker Relaunch](https://www.justsecurity.org/118505/relaunch-trump-litigation-tracker/)
- [LegiScan API Documentation](https://legiscan.com/legiscan)
- [LegiScan Push API User Manual v1.91](https://api.legiscan.com/dl/LegiScan_API_User_Manual.pdf)
- [Congress.gov API](https://api.congress.gov/)
- [FEC Campaign Finance Reports Due in 2026](https://www.fec.gov/updates/reports-due-in-2026/)
- [openFEC GitHub](https://github.com/fecgov/openFEC)
- [Federal Register Subscription Options](https://www.federalregister.gov/reader-aids/using-federalregister-gov/subscription-options-and-managing-your-subscriptions)
- [SCOTUSblog Trump v. Slaughter case page](https://www.scotusblog.com/cases/case-files/trump-v-slaughter-2/)
- [PBS News: SCOTUS hears Trump v. Slaughter](https://www.pbs.org/newshour/show/supreme-court-hears-arguments-on-trumps-power-over-independent-agencies)
- [Constitutional Accountability Center: Trump v. Slaughter](https://www.theusconstitution.org/litigation/slaughter-v-trump/)
- [Time: Iran War WPR Congress, April 2026](https://time.com/article/2026/04/22/as-iran-war-nears-two-month-congress-continues-to-forgo-oversight-role/)
- [Democracy Now: Senate Defeats Iran WPR Fifth Time](https://www.democracynow.org/2026/4/23/headlines/senate_republicans_defeat_iran_war_powers_resolution_for_fifth_time)
- [CNN: War Powers Act analysis, April 25 2026](https://www.cnn.com/2026/04/25/politics/war-powers-act-trump-iran-war-congress-analysis)
- [CRS Report: OMB Apportionment Reporting](https://www.congress.gov/crs-product/IN12538)
- [GAO Letter to OMB on Apportionments](https://www.gao.gov/products/e12062)
- [USASpending.gov API](https://api.usaspending.gov/)
- [Democracy Docket Newsletter Subscriptions](https://newsletters.democracydocket.com/)
- [Cornell LII SCOTUS Subscriptions](https://www.law.cornell.edu/supct/subscribe.html)
- [Advocacy Coalition Framework — PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10010954/)
- [Frontiers in Political Science — ACF Review](https://www.frontiersin.org/journals/political-science/articles/10.3389/fpos.2024.1497731/full)

---

*Production-ready. Companion to monitoring-infrastructure-2026.md. Templates in monitoring/templates/. Part of Phase 3 structural deepening sequence. Session 539.*
