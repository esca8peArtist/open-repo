# Resistance Research Worklog

---

## April 26, 2026 (Session 421) — May Day Guide Production Readiness + Distribution Strategy

**Session type**: Production verification + distribution planning
**Date**: April 26, 2026
**Files updated**: `WORKLOG.md`

### What Was Done

**Task 1 — Gist Content Verification (production-readiness check)**

Compared the live Gist (https://gist.github.com/esca8peArtist/2c5ba783bd06405749b7c3decebaa6d4) against the source file (`mayday-2026-action-guide.md`, commit HEAD at 24ceb62). All four critical verification points confirmed:

1. Footer shows both update dates: "Updated: April 26, 2026 — event counts updated to 900+/85 cities; ICE tracker injunction added" and "Updated: April 27, 2026 — corrected ICE tracker app restoration status." Both April 26 and April 27 passes are present in the live Gist.

2. ICE tracker injunction present in Section 4 (Undocumented Participants subsection): Judge Alonso N.D. Illinois preliminary injunction language is there with the correct caveat that the court cannot compel Apple/Facebook to restore the apps. The April 27 correction (apps not confirmed restored, do not rely on them for May 1) is reflected.

3. Event counts correct: "900+ events confirmed nationally; 3,500+ total actions including walkouts projected" and "85+ cities." Matches the April 26 update pass.

4. Section 7 government response date parenthetical reads "(as of April 23, none confirmed)" — this is accurate and intentional. Section 7 was not changed in later update passes because no new confirmed government enforcement actions targeting May Day organizing had emerged as of April 27. The date is slightly stale but the substance is correct; no update needed at this stage given the guide's footer clearly shows the April 26-27 update passes.

**Production-readiness verdict: YES.** The Gist is production-ready. The source and live versions are in sync. Nine sections, 743 lines, 60+ sourced links, legal analysis current through April 27. One minor note for awareness: the Section 7 parenthetical "(as of April 23)" could theoretically be updated to April 27 on a final pass, but this is cosmetic — the substance of that section is accurate and the footer establishes the guide's update timeline.

**Task 2 — Distribution Channel Research**

Researched the active distribution landscape for the May Day coalition's own guide distribution.

Key findings:
- Coalition organizations are distributing through their institutional channels (NEA email lists, Indivisible chapter email, DSA chapter toolkits, mobilize.us event registration).
- NEA toolkit explicitly includes Bluesky in its social media messaging templates alongside Threads — this is the confirmed activist platform with active May Day content as of April 2026.
- Indivisible's guide includes social sharing via Bluesky and Facebook, plus Substack newsletter distribution.
- Action Network (actionnetwork.org) is running a May Day 2026 Weekend of Action campaign — this is a separate distribution channel from maydaystrong.org and mobilize.us, reaching different segment of civic organizers.
- No confirmed May Day-specific Signal groups or Slack workspaces identified in open web search. Signal groups are private by nature; Slack workspaces relevant to this work are not publicly indexed. The absence of search results here is expected, not indicative of absence of activity.
- Mastodon/Fediverse: active civic discourse in April 2026 but no May Day-specific channel infrastructure identified as dominant.

**Task 3 — Distribution Strategy + Message Drafted**

See distribution strategy and message draft in session 421 findings (returned directly to user as text output per protocol).

---

## April 26, 2026 (Session 420) — Cybersecurity-Hardening Phase 2 OSINT Deepening

**Session type**: Research — data broker expansion, ID barriers, court challenges
**Date**: April 26, 2026
**Files created**: `projects/cybersecurity-hardening/phase2-osint-deepening.md`

### What Was Done

Produced `phase2-osint-deepening.md` (three-part deep-dive) for cybersecurity-hardening project.

**Part A — Broker Catalog Expansion**: Documented the structural point that 200-broker lists conflate impact tiers. The actionable expansion is Tier B additions (CoreLogic, Verisk, DataLogix/Oracle, Crossix, Samba TV) plus 10 Tier C batch additions not in the current guide. Documented Tier A brokers with no opt-out path (Venntel, Babel Street, CLEAR, Clearview for federal purposes) — these require platform countermeasures, not opt-outs.

**Part B — ID-Restricted Services**: Documented which brokers require hard government ID (LexisNexis, CLEAR, Clearview), which use KBA instead (Acxiom, Epsilon), and strategies for people without standard U.S. ID. Key finding: California AB 60/AB 1766 provides undocumented California residents a path to state ID, which then unlocks DROP access — the most reliable verified path for this population. Proxy opt-out via advocacy orgs is emerging but has no national infrastructure.

**Part C — Court Challenge Landscape**: Documented Clearview BIPA settlement ($51.75M, March 2025) and its federal law enforcement carve-out. Identified BIPA private right of action as the most powerful litigation vehicle. Flagged SECURE Data Act (HR 8413, introduced April 22, 2026) as a threat to state enforcement authority via broad preemption. Documented PADFAA as an indirect regulatory lever via foreign data sales.

### Key Surprising Findings

1. The Clearview ACLU settlement explicitly carved out federal agencies — ICE retains a $9.2M contract and Illinois state law does not bind it. "We won" and "ICE still has it" are both true simultaneously.
2. California's DROP platform is accessible to undocumented residents specifically because AB 60/AB 1766 IDs exist — this connection is not documented in any guide found.
3. SECURE Data Act preemption, if enacted, would eliminate DROP, CCPA enforcement, and the 10-state consortium's authority in a single stroke.

---

## April 27, 2026 (Session 419) — April 28 Hearing Setup, Litigation Tracker Update, FISA/SB 4/CBP One

**Session type**: Monitoring setup + litigation tracker additions + hearing template creation
**Date**: April 27, 2026
**Files updated**: `monitoring/2026-04-28-results.md` (quick-fill template + April 29 analysis pass template added), `litigation-tracker-2026.md` (Texas SB 4 5th Circuit and CBP One parole entries added; pending deadlines table extended), `CHECKIN.md` (session 419 research threads update)

### What Was Done

**Task 1 — April 28 Hearing Monitoring Setup**

Read all existing monitoring files for the April 28 Xinis hearing. The infrastructure was already complete through April 27 (five documents: results, prep, pre-brief, watch-brief, tracking). Added to `monitoring/2026-04-28-results.md`:
- Quick-fill record table: 9-question grid, fillable in 10 minutes on April 28 evening
- Escalation level field and CHECKIN flag
- April 29 analysis pass template: five structured questions covering contempt, circuit watch, Nashville interaction, April 30 implications, and tracker update instructions

**Task 2 — Litigation Tracker: Two New Cases Added**

Added to `litigation-tracker-2026.md` (both were missing from tracker despite predating April 27):

1. **Texas SB 4 — 5th Circuit en banc (April 24, 2026)**: 10-7 ruling vacates injunction on standing grounds. SB 4 enforcement now unblocked. Constitutional question unresolved — leaves opening for fresh challenge by arrested individuals with clear standing.

2. **CBP One Parole Revocation — Judge Burroughs (April 1, 2026)**: 900,000 parole statuses restored. Mass termination via email held unlawful — CBP lacks "unfettered discretion" to terminate parole without individual process. Largest single immigration status restoration ruling of the current term.

Also updated pending deadlines table with tracking notes for both new cases.

**Task 3 — Context Verified (no action needed)**

Verified through web search that no new breaking developments on April 26-27 were missed in the existing monitoring documents. FISA Section 702 (expires April 30) still stalled — House blocked as of April 25-26 per Nextgov and Common Dreams reporting. AFL-CIO national still has not issued May Day strike call as of April 26. Nashville Crenshaw ruling still pending. All confirmed by existing CHECKIN.md entries.

---

## April 26, 2026 (Session 2) — Surveillance Tracking, Live Monitoring Checkpoints, Deep Dives

**Session type**: Surveillance infrastructure research + monitoring template creation + three-story deep dive
**Date**: April 26, 2026
**Files created**: `surveillance-tracking.md` (new), `monitoring/2026-04-29-mass-call.md` (new), `monitoring/2026-05-01-template.md` (new), `monitoring/2026-04-26-deep-dive.md` (new)
**Files updated**: `CHECKIN.md` (Section 702 FISA urgency added)

---

### What Was Done

**Task 1 — Surveillance Tracking (`surveillance-tracking.md` — NEW)**

Created the first surveillance infrastructure tracking document. Key findings documented:

- **Section 702 FISA expiration (CRITICAL — April 30)**: 10-day extension runs out in 4 days. No reauthorization deal in place. Three-year bill circulating without warrant requirement. The "data broker loophole" (allows warrant-free purchase of Venntel-type location data) is the key reform provision to watch. Filed as Urgent #0 in CHECKIN.md.

- **Palantir ImmigrationOS ($30M ICE contract)**: Sole-source contract awarded April 17, 2025, running through September 2027. Pulls from IRS, SSA, passport, and ALPR data. Directly connected to the IRS-ICE data sharing injunctions before Talwani and Kollar-Kotelly. Prototype delivered September 25, 2025; platform now operational.

- **Palantir USDA bossware ($75M no-bid, March 2026)**: Sole-source award for federal worker RTO compliance surveillance. Separate $300M USDA food security contract announced April 22. Palantir total federal obligations grew from $541M (2024) to $970M (2025) — 79% annual increase.

- **Venntel/Gravy Analytics FTC ban (January 2025)**: Final FTC order prohibiting sale of sensitive location data. Senator Wyden demanded DHS OIG investigation March 3, 2026, into whether ICE continues purchasing through alternative channels. ICE's current location data route is through Babel Street's surviving data products and Accurint.

- **Clearview AI**: $9.2M HSI contract (September 2025) + $225K CBP contract (February 2026). 50B+ image database. Mobile Fortify field app deployed for real-time facial recognition. At least 8 wrongful arrests in 2026 from false positives. ICE Out of Our Faces Act introduced February 2026 — no floor vote yet.

- **Ad Tech RFI (January 2026)**: ICE seeking vendor input on behavioral data from advertising technology pipelines — designed to route around the FTC's Venntel precedent using "non-sensitive behavioral data" characterization.

- **Regional ICE deployment shifts**: 12% national arrest decline (peak 8,347/week to 7,369/week) post-Minneapolis. Elevated in KY, IN, NC, FL. 120% workforce expansion announced January 3. 150+ new facility leases nationwide.

- **Maryland HB 711**: State law blocking DMV records from ICE — leading state model for data privacy as enforcement brake.

- **Counter-measures table**: Confirmed operational tools for protest environments, including clarification that Eyes Up and ICE Sightings - Chicagoland are NOT confirmed restored despite the N.D. Illinois injunction.

**Task 2 — April 29 Mass Call File (`monitoring/2026-04-29-mass-call.md` — NEW)**

Pre-brief and documentation template for the April 29, 7:30 p.m. ET national coordination call. Records: confirmed coalition status entering the call; confirmed event counts (922 events); confirmed city logistics; five specific watch items (AFL-CIO national endorsement being highest priority); post-call action item checklist.

**Task 3 — May Day Documentation Template (`monitoring/2026-05-01-template.md` — NEW)**

Comprehensive May 1 documentation template with: scale summary table; major city reporting structure; labor action tracker; government response section; legal/litigation developments checkpoint (Nashville, April 30 discovery deadline, Section 702, DHS payroll); narrative/media framing section; verified monitoring sources; strategic assessment questions (to complete May 2-3).

**Task 4 — Three Deep Dives (`monitoring/2026-04-26-deep-dive.md` — NEW)**

1. **Nashville / Crenshaw**: Full record analysis. Two paths (dismissal vs. Blanche testimony compelled). Timing interaction matrix with April 28 hearing. Confirmed ruling still pending as of April 26.

2. **Erez Reuveni whistleblower**: How the complaint is being used in Maryland civil litigation to argue the case should remain active. Specificity value for a contempt-proof Xinis order. Emil Bove connection. CBS 60 Minutes interview as video corroboration.

3. **DHS payroll cliff**: Specific payroll numbers ($1.6-1.7B/two weeks; under $1.4B remaining as of April 19). Who gets paid vs. who doesn't (enforcement staff protected; civilian staff at risk). Senate $70B reconciliation resolution passed 50-48 April 23; House still must vote. Enforcement surge pattern to watch April 28–May 4.

---

### Files Created

- `/projects/resistance-research/surveillance-tracking.md` — CREATED (new tracking document)
- `/projects/resistance-research/monitoring/2026-04-29-mass-call.md` — CREATED
- `/projects/resistance-research/monitoring/2026-05-01-template.md` — CREATED
- `/projects/resistance-research/monitoring/2026-04-26-deep-dive.md` — CREATED
- `/projects/resistance-research/CHECKIN.md` — UPDATED (Section 702 urgency added as #0)

---

## April 26, 2026 — April 28 Prep, Mass Call Tracking Setup, Guide Quality Pass

**Session type**: Pre-hearing preparation + guide quality review
**Date**: April 26, 2026
**Files created/updated**: `monitoring/2026-04-28-prep.md` (new), `mayday-2026-action-guide.md` (updated)

---

### What Was Done

**Task 1 — April 28 Hearing Preparation (`monitoring/2026-04-28-prep.md` — NEW)**

Created a comprehensive decision-support document for the April 28 hearing. Key content:

- **DC Circuit Boasberg ruling analysis**: Full treatment of how the April 15 DC Circuit 2-1 ruling (Rao-Walker majority, Childs dissent) will be deployed by DOJ at the April 28 hearing, and why it is weaker against Xinis's civil contempt posture than it was against Boasberg's criminal contempt inquiry. Four-part counterargument documented: civil vs. criminal contempt distinction; Fourth Circuit independence from DC Circuit precedent; SCOTUS April 10 return order as controlling authority; Xinis's documented factual record (1,140 documents withheld, "bad faith" finding).

- **Three sealed-record theories**: Organized the April 23 sealed filing into three analytically distinct scenarios (Theory A: negotiated partial compliance; Theory B: sealed refusal with Fourth Circuit appeal preparation; Theory C: partial compliance under privilege assertion), each with its observable signal at hearing open.

- **Outcome checklist**: Four specific outcomes to record in `2026-04-28-results.md`: (1) civil contempt issued Y/N; (2) deposition status disclosed or sealed; (3) April 30 deadline confirmed/modified/vacated; (4) Liberia demand addressed. Escalation action matrix by outcome type.

- **April 29 Mass Call tracking**: Documented what is confirmed (7:30 p.m. ET Zoom, registration via maydaystrong.org, text "solidarity" to 58910), what is not confirmed (speaker list, attendance estimate, direct Zoom link). Five specific watch items for the call.

- **May 1 action count protocol**: Current baseline 900+ events, 85 cities. Protocol for creating `monitoring/2026-05-01-results.md`.

- **Primary monitoring source table**: Eight sources with speed-of-reporting estimates for April 28.

**Task 2 — May Day Guide Quality Pass (`mayday-2026-action-guide.md` — UPDATED)**

Two substantive fixes:

1. **Stale event counts corrected**: Line 115-116 updated from "600+ actions / 65+ cities" to "900+ events confirmed / 85+ cities" with source (The People's Dissent tracker April 25; Payday Report April 24).

2. **ICE tracker injunction added to Section 4**: Added a new paragraph in the undocumented participant safety resources block noting the April 18-23 N.D. Illinois preliminary injunction (Judge Alonso) restoring Eyes Up and ICE Sightings - Chicagoland under First Amendment protection. This is directly relevant to May Day participant situational awareness and was the one identified gap in the guide.

3. **Date stamp updated**: Footer updated to note April 26 update pass and point to `monitoring/2026-04-28-prep.md` as companion.

No other substantive changes needed. All links active, legal rights section accurate, safety section complete, sources section comprehensive (40+ links).

**Nashville / Crenshaw watch**: Confirmed no ruling as of April 26. Search results show the February 26 hearing remains the last public event; ruling still described as "imminent" but no docket entry confirmed. Remains in CHECKIN.md as highest-impact unpredicted event.

---

### Files Modified

- `/projects/resistance-research/monitoring/2026-04-28-prep.md` — CREATED
- `/projects/resistance-research/mayday-2026-action-guide.md` — UPDATED (event counts, ICE tracker injunction, date stamp)

---

## April 26, 2026 — Pre-May Day / April 28 Readiness Pass

**Session type**: Monitoring + update pass
**Date**: April 26, 2026
**Files updated**: `monitoring/2026-04-28-results.md`, `litigation-tracker-2026.md`

---

### What Was Done

**Task 1 — April 28 Hearing Preparation**

The April 28 Xinis hearing has not yet occurred (today is April 26). Updated `monitoring/2026-04-28-results.md` with:

- Detailed monitoring protocol for April 28: four specific outcomes to record (contempt Y/N, deposition disclosure, April 30 deadline status, Liberia demand addressed), primary monitoring sources (CourtListener, PACER, Courthouse News, Sandoval-Moshenberg, AILA)
- Watch alert for DOJ emergency application to Fourth Circuit or SCOTUS post-contempt-order, which is the pattern in escalating cases

**Task 2 — April 27-28 New Developments**

Four material developments not in the pre-brief were found and logged:

1. **DC Circuit terminates Boasberg contempt inquiry (April 15)** — CRITICAL. A 2-1 DC Circuit panel ruled criminal contempt requires orders "unmistakably clear and specific." DOJ will use this ruling to challenge any Xinis contempt order at the April 28 hearing. This is the most significant development not in the pre-brief. Logged in both `2026-04-28-results.md` and `litigation-tracker-2026.md` (new April 26 section).

2. **ICE arrests down 12% nationally (April 25 data)** — New Deportation Data Project analysis shows a decline from 8,347/week to 7,369/week after the post-Minneapolis February 4 drawdown. But arrests increased in KY, IN, NC, and FL. Collateral arrests also down. Enforcement posture for May Day is moderated nationally, elevated in Southeast/Midwest. Logged in both files.

3. **New Jersey AFL-CIO — 1 million union members formally mobilized for May Day (April 22)** — NJ AFL-CIO (representing 1M+ members) held a formal press conference in Newark with NJEA and AFT-NJ leaders. This is the largest single state federation to explicitly mobilize its membership. National AFL-CIO has still not issued a formal strike call. Event count now 900+; total projected actions including walkouts 3,500+. Logged in `2026-04-28-results.md`.

4. **Trump v. CASA oral arguments — date correction** — Arguments were April 1, 2026, not May 15. Post-argument read from SCOTUSblog is that the Court appears likely to side against the administration on birthright citizenship. Decision expected late June. Updated deadline table in litigation tracker.

**Task 3 — May Day Action Guide Review**

Read the full guide (`mayday-2026-action-guide.md`). Assessment:

- All nine sections present and internally consistent
- Legal rights section is accurate (First Amendment baseline, NLRA analysis, union vs. non-union risk matrix)
- Undocumented participant section is detailed and honest about risk; four-absolutes format is clear; city-level resources are linked
- April 29 Mass Call information correct (7:30 PM ET / 7:00 PM CT Zoom)
- Sources section comprehensive (40+ links)
- No broken internal structure; formatting clean

One recommended last-minute update: the guide's "Government response indicators" section (Section 7) says "no confirmed executive orders, DOJ actions, or DHS enforcement actions targeting May Day organizing have been confirmed as of April 23." That remains accurate as of April 26 — no targeted May Day enforcement actions have been announced. No update needed; the guide is production-ready.

**One item to note for the guide**: The ICE tracker app injunction (N.D. Ill., April 18-23 — Eyes Up and ICE Sightings restored) is mentioned in the pre-brief and results brief. It is not explicitly referenced in the May Day guide's undocumented participant section. This is not a critical gap — the guide points to rapid-response networks — but if there is a final update window, a line noting the injunction that restored ICE-monitoring tools would strengthen the safety resources section.

---

### What to Monitor Next

- April 28 Xinis hearing outcome — fill in `monitoring/2026-04-28-results.md` HEARING OUTCOME section
- Nashville Crenshaw ruling — could land any day; log immediately when it does
- April 29 Mass Call — any last-minute coalition changes, safety updates
- April 30 5 PM — discovery deadline reactivation in Abrego Garcia case
- DHS payroll cliff — first week of May

---

### Files Modified

- `/projects/resistance-research/monitoring/2026-04-28-results.md` — added monitoring protocol, four new developments section, updated sources
- `/projects/resistance-research/litigation-tracker-2026.md` — added April 26 monitoring pass section with Boasberg DC Circuit ruling, ICE arrest data, updated deadline table
