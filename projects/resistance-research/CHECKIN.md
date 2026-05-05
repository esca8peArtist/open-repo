# CHECKIN — Needs Your Input

*Updated: May 5, 2026 (Exploration Queue Item 38 — tracker automation design)*

---

## Completed: Tracker Automation Infrastructure Design (May 5, 2026)

All four design documents for Exploration Queue Item 38 are complete and production-ready. These should be reviewed before any automation work begins.

**Files created**:
- `projects/resistance-research/tracker-data-source-audit.md` (508 lines) — Audits current sources for all four trackers; identifies 5–7 new automatable sources per tracker with API endpoints, legal feasibility tables, and priority rankings. Every source identified is real, currently live, and free.
- `projects/resistance-research/tracker-automation-architecture.md` (530 lines) — Full pipeline design: ingestion engine (Python + APScheduler), normalization layer, scope validation, deduplication algorithm, database schema (SQLite/PostgreSQL), governance matrix, and technology stack. Estimated total monthly cost: $6–30.
- `projects/resistance-research/tracker-dashboard-mockups.md` (480 lines) — Datasette-based interactive dashboard, static PDF generation, institutional briefing format, all four export formats (CSV, JSON, RSS, iCalendar), five visualization options, and WCAG 2.1 accessibility requirements.
- `projects/resistance-research/tracker-maintenance-playbook.md` (416 lines) — Exact update cadences per tracker (daily vs. 2–3x weekly), role definitions, 10-item validation checklist, false positive detection thresholds, monthly/quarterly source maintenance schedule, archival procedures, community contributions framework, escalation matrix.

**Key design decisions to review**:
1. Prosecutorial weaponization tracker does not yet exist as a standalone file — needs to be created and seeded from existing entries before automation goes live.
2. Wave 1 implementation (CourtListener, Federal Register API, DOJ USAO RSS, Press Freedom Tracker API, Regulations.gov) costs $0 and can begin immediately.
3. The dashboard uses Datasette (open source, no frontend development required) — a strong fit for the current team size.
4. The automation governance matrix (Section 6.1 of architecture doc) determines which entries auto-publish vs. require human review. Review and confirm the High-confidence auto-approve threshold before implementation.

---

*Updated: April 26-27, 2026 (session 419)*

---

## Published

### Cybersecurity Hardening Trilogy — PUBLICATION-READY (Session 422)

Three-document corpus verified complete and publication-ready. All infrastructure updated. Final publishing checklist documented.

**Files**:
- `projects/cybersecurity-hardening/threat-model.md` (446 lines — Palantir/NSA/FBI/data broker threat analysis, primary-sourced)
- `projects/cybersecurity-hardening/opsec-playbook.md` (635 lines — countermeasures by tier)
- `projects/cybersecurity-hardening/implementation-guide.md` (1,057 lines — step-by-step setup with verification checkpoints)

**Infrastructure** (also complete):
- `PUBLICATION_README.md` — publishing instructions, citation formats, pre-pub checklist (all items checked)
- `DISTRIBUTION_CHECKLIST.md` — channel strategy, sharing scripts, organization contacts
- `publication-prep.md` — executive summary (600 words), corrected TOC, 40-term glossary; status updated from `draft` to `complete`
- `CHECKIN.md` (new) — full publishing checklist with Yes/No per channel

**Awaiting user action**: Create GitHub Gist at https://gist.github.com (5 minutes) to produce a shareable URL, then distribute per DISTRIBUTION_CHECKLIST.md. Highest-priority first contact: NILC/CLINIC/RAICES via the email script in the distribution checklist.

**Note**: Spanish translation of Part 0 + Tier 1 checklist identified as the highest-leverage follow-on — not yet produced.

---

### May Day 2026 Action Guide — LIVE

Published April 26, 2026 as a public GitHub Gist:

**https://gist.github.com/esca8peArtist/2c5ba783bd06405749b7c3decebaa6d4**

743 lines, 9 sections, 60+ sourced links, legal analysis, situation-specific guidance. Source file: `projects/resistance-research/mayday-2026-action-guide.md` (committed to master, HEAD at 24ceb62).

Requires user action to distribute — see session notes for channel strategy.

---

## Urgent / Time-Sensitive

### 0a. SCOTUS Callais v. Landry — VRA Section 2 Gutted (April 29, 2026) — NEEDS DOMAIN UPDATES

**Flagged: May 5, 2026 (Phase 2 Candidate 2 research)**

The Supreme Court ruled 6-3 on April 29, 2026, in *Callais v. Landry* (Louisiana redistricting) that Section 2 of the Voting Rights Act now requires proof of intentional racial discrimination, not merely discriminatory effect. This is the most consequential voting rights ruling since *Shelby County v. Holder* (2013) and possibly the most severe single blow to the VRA since its passage.

**Immediate practical effects**:
- Louisiana's majority-Black congressional district (created under court order after the prior Allen v. Milligan ruling) was struck down as a racial gerrymander
- Alabama immediately filed an emergency motion seeking expedited review of its pending redistricting appeal on the same theory
- Georgia Governor Kemp announced he will not order redistricting in response to the ruling (GPB, May 1, 2026)
- Multiple states now have grounds to redraw majority-minority districts as "racial gerrymanders"
- The intent standard, rather than the effect standard, is now the operative VRA Section 2 test

**Domains requiring updates**:
- Domain 1 (Electoral Reform — voting rights section requires full update)
- Domain 33 (State Legislative Autocratization — mid-decade redistricting analysis changes)
- Phase 2 Candidate 2 (this document already incorporates the ruling — see Section 1.4 and Section 5.2)
- Litigation Tracker 2026 — add Callais as new entry

**Sources**: [Democracy Docket: SCOTUS Smothers Voting Rights Act](https://www.democracydocket.com/news-alerts/scotus-smothers-voting-rights-act-greenlighting-racial-discrimination-and-a-rash-of-gop-gerrymanders/); [NPR: Supreme Court Strikes Severe Blow to VRA (April 29, 2026)](https://www.npr.org/2026/04/29/nx-s1-5754657/supreme-court-louisiana-redistricting); [GPB: Kemp Won't Order Redistricting (May 1, 2026)](https://www.gpb.org/news/2026/05/01/kemp-wont-order-redistricting-in-georgia-after-supreme-court-weakens-voting-rights); [Campaign Legal Center: What's Next after VRA Evisceration](https://campaignlegal.org/update/us-supreme-court-has-eviscerated-voting-rights-act-whats-next)

---

### 0. Section 702 FISA — HOUSE PASSED 235-191 (April 29) — SENATE ACTION PENDING BY MAY 1

**Updated April 29, 2026 (Session 658)**

The House passed S.1318 (Foreign Intelligence Accountability Act, three-year warrantless renewal) **235-191 on April 29**. The April 30 deadline will not produce a lapse. Senate cloture vote on companion S.4344 is set for no later than May 1 (Thune UC agreement). Presidential signature expected after Senate passage. The CBDC ban attached to the House version is expected to be stripped in the Senate.

**What is confirmed:**
- (a) Warrant requirement: NOT included
- (b) Commercial data broker loophole: NOT closed
- (c) Lapse: Did not occur; collection authority continues
- (d) New expiration date: April 30, 2029 (pending Senate passage)
- (e) SAVE Act attachment: Not included (Trump dropped this condition)

**What still needs to be filled** (after Senate vote and presidential signature):
- Senate vote count on S.4344 or amended S.1318
- Date of presidential signature
- Whether CBDC ban survived into enacted text (expected: no)
- First EFF/ACLU post-passage challenge filing

**Where to update**: surveillance-tracking.md (FISA outcome checklist), domain-25-fisa-702-april-2026-outcome.md Section 7 checklist (partially updated this session), PROJECTS.md "Active Trackers"

**Research filed to**: domain-25-fisa-702-april-2026-outcome.md (Section 7 updated + Section 9 added), domain-01-voting-rights-elections.md Section 4.2 (corrected "lapsed" framing), domains/MAY_2026_UPDATES.md (April 29-30 developments section added)

---

### 0a. Distribution Placeholder Audit — COMPLETE (Session 658)

Full placeholder audit completed for all three distribution template files. Results documented in DISTRIBUTION_GUIDE.md at the top (new "DISTRIBUTION READINESS: PLACEHOLDER AUDIT" section). Summary:

- **URL placeholders**: All `[link]` fields in Substack, Reddit, and institutional templates point to 6 canonical documents. Cannot be filled until public URLs (GitHub Gists) are created. This is the sole blocker for distribution launch.
- **Contact fields**: `[Your name]` and `[Contact information]` appear in all 11 institutional outreach templates; user must fill before sending.
- **Canonical file ambiguity**: Resolved. Two executive summary versions (96-line print-ready vs. 132-line analytical version) serve different audiences. No conflict.
- **Pre-launch time estimate**: approximately 90 minutes of user action to create Gists, fill URL placeholders, and fill contact fields — path-independent.

**No agent action required** — audit is informational. When user decides path, execution begins immediately from this documented state.

---

### 1. April 28 Xinis Hearing (TOMORROW)
The results brief is filed at `monitoring/2026-04-28-results.md` with a "Hearing Outcome" placeholder at the top. The hearing has not yet occurred — outcome needs to be added on April 28.

**The most important thing to watch for:**
- Does Xinis issue a contempt order with teeth (fines, official jeopardy)?
- Does the April 23 sealed deposition stay mean a negotiated resolution is emerging, or just a delay?
- Any disclosure of what actually happened during the four depositions?

### 2. Nashville Crenshaw Ruling — Could Land Any Day
Judge Waverly Crenshaw's ruling on the Abrego Garcia vindictive prosecution motion is described by multiple sources as "imminent" or "at any time." No date set. If Crenshaw **dismisses charges**, that eliminates DOJ's rationale for keeping Abrego Garcia in U.S. criminal jurisdiction — and reshapes both the Maryland civil case and the Liberia deportation pressure entirely. This is the highest-impact unpredicted event in the queue right now.

**What to check**: CourtListener docket for United States v. Abrego Garcia, 3:25-cr-00115.

### 3. DHS Payroll Cliff — Week of May 4-8
DHS emergency funds run out after the first May payroll. The Senate passed the $70B reconciliation budget resolution 50-48 on April 23, but the House has not yet voted. If the House does not pass the budget resolution before May 4-8, DHS faces a genuine payroll crisis for 270,000 employees. This is not the same as enforcement capacity disappearing — law enforcement-designated staff have been paid throughout — but it is a material escalation of the political standoff.

**Practical flag for May Day**: Any acceleration of ICE enforcement in the days before a funding crisis, as political pressure tool, is a known pattern. Watch the first week of May.

### 4. April 29 Mass Call — 7:30 p.m. EST / 7:00 p.m. CDT
May Day Strong final coordination call. Check for any last-minute route changes, safety alerts, or coalition news. The May Day guide should only be updated if genuinely critical logistics change.

---

## Phase 2 Domain Expansion — New Scope Documents (April 27, 2026)

Three new domain scope documents written in this session (Phase 2 autonomous expansion):

1. **`domains/domain-37a-post-election-section3-litigation-recovery.md`** — Post-election Section 3 litigation and congressional certification recovery strategy. Covers the Fulton County FBI seizure threat model, the FCEA/House contestation mechanism, Section 3 enforcement after *Trump v. Anderson*, and the pre-certification TRO litigation strategy. Three-phase framework (election night → certification → post-seating). Cross-references Domains 29, 37. **Advocacy window: September–October 2026. Full research: 1–2 sessions.**

2. **`domains/domain-37b-state-election-security-coordination.md`** — Post-CISA state election security architecture. Documents what states have built to replace CISA (National Guard cyber units, state police integration, university partnerships, state appropriations), why the coordination gap cannot be closed at state level, and the competitive state vulnerability matrix (AZ, GA, MI, PA, WI against documented capacity indicators). Governance recommendations include NASS emergency working group, paid MS-ISAC pool, statutory independence for federal coordination. Cross-references Domains 21, 33, 36, 37. **Advocacy window: April–July 2026. Full research: 1 session.**

3. **`domains/domain-31x-healthcare-tariff-collision.md`** — Healthcare tariff collision scope document. Three-track convergence: (a) Section 232 100% pharmaceutical tariffs (effective July 31, 2026 — confirmed legally enforceable after IEEPA Supreme Court ruling); (b) OBBBA Medicaid work requirements (effective January 1, 2027); (c) Strait of Hormuz / Iran war shipping disruption compounding generic drug API supply chain. Seven-date advocacy timeline from May 2026 through January 2027. Electoral political economy analysis (MFN pricing strategy as pre-election messaging tool). Cross-references Domains 23, 28, 31. **Most urgent: 95 days to July 31 tariff date. Full research: 1–2 sessions.**

**All three files are scope documents (ready for full research execution), not completed research domains. No user approval required to proceed to full research.**

---

## Research Threads Open (no urgent action required)

- Litigation tracker update: ICE tracker injunction (Alonso, N.D. Ill., April 18-23) should be added as a new entry — this is a significant First Amendment win for organizers. NOTE: Rosado v. Bondi status correction already in tracker and monitoring/2026-04-27-tracking.md.
- ProPublica/Frontline "Caught in the Crackdown" findings should be summarized in the know-your-rights document as documented precedent for protest arrest patterns.
- Williamsport warehouse case (Maryland v. Noem) preliminary injunction hearing pending — no date confirmed.
- Texas SB 4 (5th Circuit en banc, April 24) and CBP One parole restoration (Judge Burroughs, April 1) both added to litigation-tracker-2026.md in session 419.
- FISA Section 702 expires April 30 — House still blocked as of April 26; data broker loophole is the key reform provision. See surveillance-tracking.md.
- Democratic renewal proposal: all 22 domains complete with evidence depth. No new domains needed. Follow-up: consider publication pathway and outreach targets once post-May Day monitoring stabilizes.
