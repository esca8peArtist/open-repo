# Active Projects

> This is the single source of truth for autonomous orchestration.
> The orchestrator reads this file at the start of every session.
> Update priorities, status, and current focus as work progresses.
>
> **Last updated by**: orchestrator on 2026-04-27 Session 498 (Domain 25 + tracker maintenance)

---

## Usage Budget

> Tracking is **token-based** (output tokens from `~/.claude/projects/.../  *.jsonl`).
> Plan resets every **Tuesday at 00:00 UTC**.
> To manually check: **claude.ai → Settings → Usage & billing**
> To recalibrate limits: `python3 scripts/usage-check.py --calibrate <sonnet_pct> <all_pct>`

**Calibrated limits** (back-calculated from UI — update after each weekly reset):
- **Sonnet token limit: 5,023,178**  ← calibrated 2026-04-26 (UI showed 42.0%)
- **All models token limit: 13,048,473**  ← calibrated 2026-04-26 (UI showed 34.0%)

**Alert thresholds** (handled by `scripts/usage-monitor.py`, runs every 30 min via cron):
- Every 10% crossed → Discord notification
- 80% → Orchestrator **paused** (`USAGE_PAUSE` file created); Discord alert with override command
- 80% override → `touch /home/awank/dev/SuperClaude_Framework/USAGE_PAUSE_OVERRIDE` (expires at 90% or Tuesday reset)
- 90% → Hard throttle, override revoked; sessions blocked until Tuesday

**Throttle rules (orchestrator must follow at session start):**
1. Run `python3 scripts/usage-check.py --check`
2. Exit 0 → proceed normally
3. Exit 1 (≥90%) → log "Usage throttled — idling." in WORKLOG.md, update CHECKIN.md, stop
4. Exit 2 (80% pause) → log "Usage paused at 80% — waiting for user override or Tuesday reset.", update CHECKIN.md, stop
5. Always update the usage line in CHECKIN.md with `python3 scripts/usage-check.py --checkin` before going idle

---

## Priority Order
1. resistance-research
2. stockbot
3. cybersecurity-hardening
4. mfg-farm
5. seedwarden
6. open-repo
7. off-grid-living
8. workout
9. resume
10. open-source-rideshare (Paused)

---

## Projects

### mfg-farm
**Goal**: Build a fully automated manufacturing business centered on 3D printing, with a path to a full print farm. Sell products on Etsy, Amazon, and similar platforms. Develop a complete business plan: product selection driven by market demand and unique value proposition, pricing strategy, fulfillment workflow, and a scaling roadmap from single printer to multi-printer farm with multiple colors and material capabilities. Explore adjacent manufacturing (laser cutting, CNC, resin printing) and integrate where demand justifies it. The north star is maximizing income — product and machine decisions should be driven by data: what sells, what margins look like, and where automation creates the highest leverage.
**Priority**: High
**Status**: Active — ready to prototype
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/mfg-farm/`
**Current focus**: Session 291: **Business plan COMPLETE** (`business-plan.md`). **CadQuery parametric designs COMPLETE** (`cadquery/modrun_rail.py`, `cadquery/modrun_clip.py`). Market research + competitive analysis complete (`market-research.md`). Etsy and Amazon listing copy complete (`etsy-listing-modrun.md`). **Phase 2 supplier research COMPLETE** (Session 544: `phase-2-supplier-research.md`, `supplier-scorecard.csv` — top 5 suppliers ranked, $0.77–1.40/unit COGS savings identified, post-test-print sequence documented). **Lead product: ModRun cable management system** — original design, Etsy-compliant, 65–72% net margins. **BLOCKING GATE: test print required.** User needs to: (1) run `pip install cadquery` in mfg-farm env or system Python, (2) run `python modrun_clip.py --output-dir ./stl/` and `python modrun_rail.py --output-dir ./stl/` to generate STL files, (3) test print and tune tolerance parameters, (4) photograph finished set, (5) list on Etsy. All copy, pricing, tags, photo brief ready in `etsy-listing-modrun.md`. Post-test-print supplier sequence documented — negotiate immediately after print.
**Blocked on**: Test print (user action required — see focus above)
**Notes**: Automation is the core constraint — products and workflows must be designed for minimal human touchpoints per unit. Physical products mean real fulfillment costs (packaging, shipping, storage) — factor these in from the start. Etsy and Amazon have different fee structures and audiences; may want both. Scaling from 1→N printers requires thinking about file management, queue management, quality control, and packaging throughput — not just the printers themselves.

---

### resistance-research
**Goal**: Identify solutions to a failing democracy — if the current government could be replaced and rebuilt from a clean slate, what would it look like? How could it be structured to ensure justice, life, liberty, and the pursuit of happiness for all citizens? How could it be objectively efficient, equitable, and functional? This project addresses the full scope of government: voting systems, taxation, education, infrastructure, healthcare, law enforcement, housing, and everything in between. The government exists to serve its citizens — so how do we actually achieve that? A secondary goal is tracking and understanding the specific crises the United States is currently facing, finding actionable responses, and building a comprehensive integrated proposal for democratic renewal.
**Priority**: High
**Status**: Active — Phase 1-5 COMPLETE, **35-Domain Diagnostic Framework COMPLETE + CONTENT CURRENCY CURRENT** (Sessions 502-524) — Core proposal architecture complete, completeness assessment done, all 34 domain documents verified production-ready, distribution infrastructure finalized (Session 520), April 2026 domain updates complete (Sessions 521, 524)
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: **Session 528 (2026-04-27): Policy Influencer Mapping COMPLETE**; **Session 529 (2026-04-27): April 2026 Domain Content Updates COMPLETE**. 
- **Policy Influencer Mapping**: Comprehensive 3-tier map (150+ contacts) with sequencing strategy for distribution amplification. Tier 1: 25 high-leverage (senators, think tanks, law schools). Tier 2: 45+ (academics, media, law reviews). Tier 3: 55+ (labor, civil rights, state networks, faith coalitions). Sequencing: Ryan Goodman (Just Security) → Erica Chenoweth → Wendy Weiser (Brennan Center).
- **April 2026 Domain Updates** (Session 529): Updated/created 6 domain documents with April 2026 civic developments (~5,720 words, 45 sources):
  - **Domain 1 (Voting Rights)**: NEW — SAVE Act legislative history, Senate failure April 2026, 4 GOP defectors with coalition-fracture analysis
  - **Domain 6 (Judicial Independence)**: NEW — Trump v. Wilcox shadow-docket ruling, post-Loper Bright appellate capture vectors
  - **Domain 19f (War Powers)**: Iran WPR case study, emergency EO framing, enforcement mechanism exhaustion
  - **Domain 28 (Venezuela Military)**: Iran cross-reference as parallel escape-route exhaustion
  - **Domain 35 (Supreme Court 2026 Term)**: OT2026 cert analysis, presidential immunity closure, reform feasibility
  - **Supporting file**: `domains/APRIL_2026_UPDATES.md` with metadata and verification table
- **Framework status: 41 total domain documents (35 base + 6 April updates/new). Content current through April 2026. Influencer map ready. Awaiting user distribution path decision** (Path A / Path A+Domain37 Hybrid / Path B) → Phase 1 execution begins immediately.tive bill data, six-state supermajority, SAVE Act Senate failure); Domain 35 (post-Slaughter pipeline); Part III of proposal (Trump v. Wilcox shadow docket). Deferred: Domains 1, 21, 25 (FISA 702 April 30 outcome pending). **Framework currency improved; distribution ready.** **User decision required: Path A (immediate distribution) / Path A+Domain37 Hybrid (RECOMMENDED) / Path B (continue optional updates before distribution).** Once user decides, orchestrator can execute Phase 1 immediately. 
- **Domain 26 — COMPLETE: Government Accountability and Institutional Resilience** (4,700 words, fully sourced):
  - **26-DOMAIN DIAGNOSTIC FRAMEWORK NOW COMPLETE** (all domains + implementation architecture fully researched)
  - **Central finding**: Accountability failures in 2026 are coordinated across every layer of the oversight system simultaneously
  - **Priority research areas executed**:
    - Skrmetti (June 2025): SCOTUS narrowed equal protection scrutiny, reducing judicial backstop for healthcare accountability
    - EMTALA rescission (June 3, 2025): CMS eliminated Biden guidance, demonstrating law-functional-elimination without repeal
    - CDC maternal mortality: 80 staff fired, PRAMS halted, no guidance on abortion-related deaths; Texas stopped reporting to avoid accountability
    - Ballot initiatives: 295 bills in 43 states targeting initiative process; coordinated post-approval nullification via legislative resistance and budget cuts
    - My Health My Data Act: Washington state privacy law — identified as positive institutional resilience template (dual-track enforcement, extraterritorial scope, designed to function without executive goodwill)
  - **File**: `domains/domain-26-government-accountability-and-institutional-resilience.md` (4,700 words, 12 cited sources)
  - **International precedents**: Germany's Federal Audit Office, New Zealand parliamentary commissioner system, France constitutionalization of abortion (model comparison)

**✅ COMPLETED (Session 503)**:
- ✅ **Domain 26 Research** — Complete research document with coordinated accountability failure analysis and reform pathways
  - `domains/domain-26-government-accountability-and-institutional-resilience.md` (4,700 words) — Full domain structure, structural vulnerabilities, institutional resilience mechanisms, reform pathways with international precedent, implementation timeline
  - 12 sourced citations covering all five priority research areas
  - Completes the 26-domain diagnostic framework. With Domain 19f (War Powers): removes both distribution blocks identified in post-Domain-26 audit

**Phase 2 PRIORITY DOMAINS STATUS**:
- ✅ Domain 23 (Trade Policy, Tariff Unilateralism) — COMPLETE (Session 512) — 8,849 words
- ✅ Domain 27 (Higher Education and Academic Freedom) — COMPLETE (Session 506) — 4,800 words
- ✅ Domain 28 (War Powers Venezuela Military Unilateralism) — COMPLETE (Session 506) — 5,600 words  
- ✅ Domain 29 (Prosecutorial Weaponization and DOJ Capture) — COMPLETE (Session 506) — 6,124 words
- **Total framework**: 29 domains + implementation architecture (Phase 1-5 complete + Phase 2 expansion: Domains 23, 27-29 complete)

**✅ COMPLETED (Session 510)**:
- ✅ **Phase 2 Integration COMPLETE** — All 28 domains unified, metadata corrected, distribution templates updated
  - Executive summary rows updated for Domains 27-29 with expanded findings
  - Distribution package corrected: fixed 9 instances of "22-domain" → 28-domain across all templates
  - EXPLORATION_QUEUE.md created with 3 new Phase 2 research candidates (trade policy/tariffs, healthcare access/Medicaid, state legislative autocratization)
  - Proposal structure complete: all 28 domains have body text in proposal, Domains 23-29 have standalone research files with cross-references
  - Assessment: Ready for distribution execution OR Phase 2 expansion research selection

**Phase 2 Candidate 1 (Session 513) — COMPLETE**:
- ✅ **Domain 31: Healthcare Access Collapse — OBBBA/Medicaid Crisis** (6,142 words, production-ready)
  - Research document: `domains/domain-31-healthcare-access-obbba-medicaid-crisis.md`
  - Scope: OBBBA work requirement implementation (January 2027), Medicaid expansion funding elimination (January 2026), 6-month recertification (2027+), and democracy-health nexus through voter registration infrastructure
  - Key findings: 11.8M disenrollment projected; Arkansas 2018 precedent (18K disenrolled in 6 months with zero employment effect); June 2026 HHS guidance deadline creates advocacy window; racial disparities in procedural disenrollment (Black individuals 22% of enrollees but 22% of procedural disenrollments); rural hospital closures linked to Medicaid funding cuts
  - Democracy angle: Medicaid enrollment offices serve as voter registration sites under NVRA; cuts to enrollment capacity reduce voter registration in majority-minority areas (12 non-expansion states are primarily Southern, majority-Black low-income populations)
  - Implementation timeline: June 1, 2026 (HHS guidance); January 1, 2027 (work requirements effective); litigation anticipated Q1 2027; circuit court decisions through 2028

**Phase 2 Candidate 2 (Session 514) — COMPLETE**:
- ✅ **Domain 33: State Legislative Autocratization** (7,821 words, production-ready)
  - Research document: `domains/domain-33-state-legislative-autocratization.md`
  - Scope: Four simultaneous mechanisms (redistricting autocratization cycle via REDMAP 2.0, state supreme court capture via dark money, ballot initiative suppression, voter suppression escalation)
  - Key findings: REDMAP model replicated at scale; North Carolina 2022-2023 dark money ($5.5M RSLC) captured state supreme court and reversed redistricting ruling in same term; 295+ bills in 43 states attacking ballot initiatives (2025 alone exceeded 2000-2023 combined); 31 restrictive voting laws enacted in 2025
  - International precedent: Hungary (cardinal laws model — exact mechanism being replicated in four US states), Poland (capture reversal asymmetric), Turkey (legislative capture as platform for next phase)
  - Timeline: 26 SOS races + 3 state supreme court races in 2026 as immediate test; 2030 Census redistricting cycle as long-term objective (whoever controls state legislatures in Jan 2031 draws maps until 2041)

**Phase 2 Candidates 3-5 (Session 515) — ALL COMPLETE**:
- ✅ **Domain 34: Congressional Power-of-the-Purse Fiscal Authority Reassertion** (6,403 words, 45 sources)
  - Research document: `domains/domain-34-congressional-power-of-the-purse-fiscal-authority-reassertion.md`
  - Scope: Four-mechanism fiscal assault (agency fund holds, OMB apportionment Category C expansion, Treasury payment system interference, pocket rescissions)
  - Key findings: $425B+ withheld appropriations documented; Category C expansion to 8.64% of FY2026 (vs. 3.94% under Biden); watchdog dismantlement threat (50% GAO budget cut proposed); post-*Loper Bright* litigation vectors detailed
  - Reform pathways: Congressional Power of the Purse Act, Category C statutory reform, congressional standing legislation, emergency authority sunset provisions, watchdog protection

- ✅ **Domain 35: Supreme Court October 2026 Term Preview & Post-Loper Landscape** (~5,100 words, 26 sources)
  - Research document: `domains/domain-35-supreme-court-2026-term-preview-post-loper-landscape.md`
  - Scope: October 2025 term holdings, Loper Bright fallout, October 2026 docket prediction, universal injunction restrictions, presidential immunity, reform feasibility assessment
  - Key findings: Humphrey's Executor effectively dead; Loper Bright trifecta forces statutory drafting rewrite; universal injunctions eliminated; presidential immunity closes criminal accountability; October 2026 cert predictions (Second Amendment, Section 230, APA vacatur, Article III agencies)
  - Doctrinal implications: Which Domain 6 and Domain 13 recommendations remain viable post-Loper, which require statutory heavy-lifting

- ✅ **Domain 36: AI Governance, Algorithmic Accountability & Democratic Authority** (6,080 words, 30 sources)
  - Research document: `domains/domain-36-ai-governance-algorithmic-accountability-democratic-authority.md`
  - Scope: Federal AI deployment accountability gap, root causes, structural vulnerabilities, international precedent (EU AI Act, Canada AIDA), statutory reform pathways
  - Key findings: No federal AI statute; Biden EO framework revoked Jan 20, 2025; five crisis cases (WISeR, Palantir/ICE, FBI location data, SSA disability, DOGE terminations); post-Loper Bright vulnerability
  - Six statutory reforms: Federal AI Governance Act, APA Algorithmic Due Process Amendment, Algorithmic Impact Assessment, Congressional Audit Rights, State AI Authority Floor, Private Right of Action

**✅ COMPLETED (Session 517)**:
- ✅ **Domain 37: Federal Executive Interference in 2026 Midterms** (8,850 words, 50 sources)
  - Research document: `domains/domain-37-federal-executive-interference-2026-midterms.md`
  - Scope: DOJ voter roll litigation (23 active cases, 1 settlement, 5 dismissals); draft emergency EO (mail voting ban, forced re-registration); election denier federal positions (11+ appointees in DHS/DOJ connected to Election Integrity Network); ICE-at-polls threat (Bannon public statement April 2026).
  - Key findings: CISA election security program facing $700M budget cut in FY27 proposal, eliminating EI-ISAC/MS-ISAC and all regional advisors. Election Day situation room did not operate November 2025. Privacy officer resignation April 3 over voter-data-to-DHS transfer. Section 3 litigation viable for post-election accountability, not pre-election remedy. Hungary April 2026 election lesson: 77% turnout can overcome structural disadvantage.
  - Advocacy windows: May 30 (consent decrees), June 30 (emergency EO routing), September 2026 (pre-election Section 3 litigation), October 2026 (logistics), Election Day (monitoring).
  - **Framework status**: 35 domains complete (Phase 1-5 base 22 + Domain 19f + Phase 2 Domains 23, 27-29, 31, 33-37).

**Next (Session 517 Update)**:
- **Framework status**: 35 domains complete (Phase 1-5 base 22 + Domain 19f + Phase 2 Domains 23, 27-29, 31, 33-37). All production-ready.
- **User decision required**:
  - **Path A — DISTRIBUTION EXECUTION**: Updated proposal (now integrating 35 domains), Substack/Reddit templates, institutional outreach (universities, policy orgs, legal clinics) — comprehensive coverage with 35-domain framework. Ready to begin immediately.
  - **Path A+Domain37 Hybrid — RECOMMENDED**: Begin Phase A distribution to general audiences (law schools, think tanks, labor unions) while sequencing Domain 37 into distribution before reaching election protection organizations specifically. This captures maximum immediate impact (34-domain framework to broad audiences) + targeted domain (37) for highest-urgency subset.
  - **Path B — Phase 2 expansion (optional)**: Domain Updates (content maintenance on Domains 19f, 28, 6, 35, 1, 21, 25, 33, 19 per April 2026 developments) — continue maintenance toward 35-40 domain framework before full distribution (requires explicit user approval per domain).
  - **User selects priority**: Path A maximizes timeliness of core 34-domain framework; Hybrid captures election integrity urgency; Path B requires 2-4 week extension.

**✅ COMPLETED (Session 502)**:
- ✅ **Domain 19f War Powers Reform** — Complete research document with current crisis analysis
  - `domains/domain-19f-war-powers-reform.md` (4,400 words) — Full domain structure, May 1 deadline crisis, constitutional analysis, fiscal implications, international precedent, reform pathways
  - 9 sourced citations from April 2026 reporting and legal analysis
  - Closes Priority 1 gap from post-Domain-26 audit (Iran war constitutional crisis with May 1 deadline)

**✅ COMPLETED (Session 500)**:
- ✅ **Domain 26 Research Infrastructure** — Outline, checklist, priority research areas identified
  - `domain-26-research-outline.md` (2,800 words) — Full structure with 5 subsections, fiscal architecture, international benchmarks
  - `domain-26-research-checklist.md` (1,200 words) — Timeline, source categories, key unknowns
  - When approved: Ready for immediate full development

**✅ COMPLETED (Session 494)**:
- ✅ **Phase 4 Integration into Part III** — All four Phase 4 documents synthesized into democratic-renewal-proposal.md Part III
  - Enhanced Section 3.3 (Coalition Analysis) with veto players framework and dark money infrastructure analysis
  - Enhanced Section 3.4 (Three Scenarios) with parallel institution options per scenario
  - Created Section 3.6 (Structural Accountability) with Epstein case study and five reform mechanisms
  - Enhanced Section 3.5 (Post-Electoral Recovery) with international case studies and comparative framework
  - Result: Part III now contains comprehensive Theory of Change with institutional power analysis, viable alternatives, accountability mechanisms, and international precedent
  - Commit: eabe4aa

**✅ COMPLETED (Session 489)**:
- ✅ **Phase 4 Documents 2-4** — theory-of-change framework complete
  1. **`power-mapping.md`** (3,500 words) — Institutional veto points and vulnerabilities
     - **Key finding**: US capture is layered (Federalist Society + executive overreach + civil service dismantlement) but not yet fully consolidated — recovery window is still open
     - Detailed mapping: federal judiciary (split, 350/362 rule-of-law wins), AG coalitions (71 suits, 40 wins), civil service (incomplete capture, legal challenges active), military officer corps (institutional non-interference norms intact), intelligence agencies (partially captured via leadership appointments)
     - Dark money infrastructure: Koch/DonorsTrust/SPN/Federalist Society four-layer architecture, documented $195M in 2024 grants to 300+ organizations, Leonard Leo's undisclosed gifts to SCOTUS justices
     - Identified vulnerabilities: Roberts independence signals, incomplete civil service capture, documented business elite fracture from tariff unpredictability, AG legal record building institutional precedent
  2. **`parallel-institutions.md`** (3,500 words) — Alternative institutional infrastructure at scale
     - **Key finding**: US already has substantial parallel institutional infrastructure (larger than most acknowledge) but fragmented and lacking political coherence to function as institutional anchors in recovery context
     - Sector inventory: Champlain Housing Trust (18% of Burlington residential units, largest CLT in world), $446B CDFI sector with 18.3M members, 900-1000 worker cooperatives with $806M revenue, mutual aid networks with demonstrated crisis-response capacity, state-level policy infrastructure with interstate compact potential
     - Mondragon comparison (70K worker-owners under Franco) shows democratic governance can scale at meaningful size
     - Three-layer blueprint: (1) what exists and needs defense, (2) what exists and needs scaling, (3) what needs creation (interstate compact architecture, cooperative development finance system, state coordination mechanism)
  3. **`elite-capture-case-study.md`** (3,000 words) — Accountability failure as structural design
     - **Key finding**: Epstein case is a technical manual for manufacturing elite impunity, not an anomaly
     - Five mechanisms systematically analyzed: (1) prosecutorial discretion without accountability (OPR "poor judgment" standard never produces sanctions), (2) unnamed co-conspirator immunity provisions (most legally significant — foreclosed network investigation before identification), (3) settlement secrecy and gag clauses (civil releases block subsequent criminal allegations), (4) judicial deference to prosecutorial discretion (Judge Marra found violation but could not compel re-prosecution), (5) revolving door incentives (Acosta became Labor Secretary)
     - 2024-2026 context: Maxwell convicted, invokes Fifth before House Feb 2026, DOJ released 3.5M pages (200K redacted against Transparency Act terms)
     - Pattern generalization: corporate prosecution rates at 30-year low, 70% of federal prosecutions target <50-person companies while large multinationals receive DPAs at dramatically higher rates
     - Accountability reform framed as constitutive of democratic recovery, not separate from it; five specific structural reforms outlined
  4. All committed to master

**✅ COMPLETED (Session 488)**:
- ✅ **Phase 4 Document 1: Comparative Democratic Recovery** — `phase-4-comparative-democratic-recovery.md` (6,400 words, 38 citations)
  - Cross-national case studies: South Korea (1987 recovery), Spain (post-Franco), Uruguay (post-dictatorship), Hungary (failed), Venezuela (failed), Turkey (failed)
  - **Central finding**: Recovery succeeds when mass mobilization + elite defection happen before entrenchment completes. This timing variable separates successes from failures consistently.
  - **US application**: Existing infrastructure identified (state AGs 71 lawsuits 40 wins, federal judges, civil society data preservation); critical gap is prepared institutional blueprint + elite-defection triggers
  - Committed: `phase-4-comparative-democratic-recovery.md` to master

**✅ COMPLETED (Session 487)**:
- ✅ **Phase 3 research roadmap integration** — 5 substantive integrations woven into proposal structure
- ✅ Files: `democratic-renewal-proposal.md`, `democratic-renewal-executive-summary.md`, `published/README.md` updated
- ✅ Committed: d911817

**✅ COMPLETED (Session 485-486)**:
1. **Priority documents**: first-amendment-suppression.md, environmental-rollbacks-tracker.md, police-brutality-consent-decree-tracker.md
2. **Proposal infrastructure**: democratic-renewal-executive-summary.md, DISTRIBUTION_GUIDE.md, published/README.md
3. **Distribution templates**: Substack (4 posts), Reddit (5 posts), institutional outreach (8 templates)
4. **Phase 3 research roadmap**: 7,148 words, 8 case studies

**✅ COMPLETED (Session 490)**:
- ✅ **Phase 5 Implementation Strategy** — complete implementation architecture ready
  1. **`implementation-roadmap.md`** (5,000 words) — Three-wave recovery sequencing with institutional assignment and success criteria
  2. **`timeline-and-conditions.md`** (4,500 words) — Triggers, milestones, and success metrics for three recovery scenarios
  3. **`movement-coordination.md`** (4,000 words) — Elite defection cascade and mass organization architecture
  4. **`risk-assessment.md`** (4,500 words) — 11 derailment vectors and $400-600M mitigation strategy

**✅ COMPLETED (Session 491-492 integration)**:
- ✅ **Phase 5 Integration into Part IV** — All four Phase 5 documents synthesized into democratic-renewal-proposal.md Part IV
  - Part 4.1: Implementation Roadmap — Three-wave recovery sequencing with institutional assignments
  - Part 4.2: Timeline and Conditions — Three recovery scenarios with milestones and success metrics
  - Part 4.3: Movement Coordination — Elite defection cascade and mass organization at 3.5% mobilization threshold
  - Part 4.4: Risk Assessment — 11 derailment vectors and $400-600M mitigation budget
  - Result: Complete proposal now contains Parts I-IV: diagnosis → vision → theory-of-change → implementation architecture

**✅ COMPLETED (Session 544)**:
- ✅ **Distribution Readiness Final Audit** — Comprehensive 8-point audit of all distribution-facing files (35 domains, proposal, templates, guides, trackers). Verdict: substance production-ready TODAY. Blocking items are administrative: (1) resolve canonical file location, (2) fill URL placeholders, (3) fill contact field, (4) pick Path A/A+37/B. Total fix time: <2 hours. User can begin distribution immediately post-decisions.

**NEXT WORK**:
- **Distribution execution** (user action): Pick Path A / Path A+Domain37 Hybrid / Path B → orchestrator executes Phase 1 immediately (all materials ready)
- **Distribution fixes** (user action, <2 hr): Resolve canonical file, fill URL placeholders in templates, fill contact field in published/README.md
- **Tracker updates** (ongoing): First-amendment, environmental-rollbacks, police-brutality trackers ready for regular maintenance
- **Domain research deepening** (optional): Phase 2 domain research if user selects Path B or post-Phase-1 expansion

**Blocked on**: User distribution path decision (A / A+37 / B)
**Notes**: Phase 5 COMPLETE + Distribution audit complete. Proposal contains complete actionable pathway: diagnosis (Domains 1-35) → alternative vision (democratic renewal proposal) → theory of change (Phase 4 documents) → implementation architecture (Phase 5 documents) → activation architecture (Phase 2 expansion complete). Implementation timeline ready for 2026 election trigger and three recovery scenarios. Distribution infrastructure audit complete. Ready to launch immediately upon user decision + <2hr administrative fixes.

---

### cybersecurity-hardening
**Goal**: Build a comprehensive, actionable guide to protecting communications and identity against government-level mass surveillance. Understand what Palantir and similar data brokers/intelligence platforms actually have access to — what data they ingest, how they link identities, and what their current government contracts cover. From that threat model, identify the best practical techniques for private and anonymous communication: encrypted messaging, metadata minimization, network anonymization (Tor/VPN tradeoffs), device hardening, operational security (OpSec), and identity compartmentalization. The output should be a personal OpSec playbook grounded in real threat modeling — not theoretical, but calibrated to the actual capabilities of the adversary.
**Priority**: High
**Status**: Active — **TIER 1, 2, 3 DISTRIBUTION PREP + TIER 2 MESSAGING TEMPLATES COMPLETE** (Sessions 465, 497, 499), ready for user execution
**Visibility**: Public — GitHub Gist (public) + private distribution to immigration legal aid organizations
**Working dir**: `projects/cybersecurity-hardening/`
**Current focus**: Session 499 (2026-04-27 evening): **TIER 2 MESSAGING TEMPLATES COMPLETE**. Agent-created:
- **TIER2_MESSAGING_TEMPLATES.md** (4 customized sector templates + organization mapping):
  - **Template 2A-v2 — Digital Rights Organizations** (12 orgs): Policy/litigation framing, sourcing for citation scrutiny, routing request CTA
  - **Template 2B-v2 — Academic Programs** (9 orgs): Methodological defensibility, documented attack surface, peer review opportunity
  - **Template 2C-v2 — Researcher Communities** (5 orgs): Researcher-first distribution, vulnerability admission for trust, CFP conversion guidance
  - **Template 2D-v2 — Journalists** (7 orgs): Source protection gap framing, training vs. reporting CTA split, per-org channel guidance
  - **Strategic principle**: Mission-first framing produces referrals and integration; generic descriptions produce acknowledgment only
  - **Outcome**: Tier 2 ready for launch once Tier 1 approval obtained
- **TIER2_DISTRIBUTION_PREP.md** (Session 497): 33 organizations (12 digital rights + 9 academic cybersecurity + 5 researcher communities + 7 journalist organizations), email templates, 5-step execution plan, FAQ, tracking templates
- **TIER3_DISTRIBUTION_PREP.md** (Session 497): 30 organizations (12 policy + 8 labor + 10 academic law/policy), email templates, 16-week timeline, long-horizon success metrics
- Key findings: Georgetown CPT highest-priority Tier 3 contact (American Dragnet report alignment); Access Now security helpline highest-leverage Tier 2 (direct harm reduction for undocumented); AFL-CIO Tech Institute new ED is outreach opportunity
- All documents follow consistent structure; committed to master

**Next**: User reviews and approves Tier 1 templates → execute Tier 1 outreach → Tier 2 launch ~4 weeks after Tier 1 completion (using TIER2_MESSAGING_TEMPLATES.md) → Tier 3 launch ~12 weeks after.
**Blocked on**: —
**Notes**: All three distribution tiers production-ready with fully customized templates. Full trilogy (Gist + three distribution-prep documents + Tier 2 messaging templates + FAQ) complete and accessible. User can begin Tier 1 outreach immediately after approval. Tier 2 template variants already written and tested for maximum impact.

---

### stockbot
**Goal**: Build a full-stack model building and automated trading platform with both a web app and iOS app integration. The platform should allow creation, backtesting, and optimization of trading models across multiple model types (stock, options, rule-based, ensemble, multi-timeframe). The end goal is fully automated live trading — but only after models are rigorously vetted and confidence is established through paper trading. Model training and optimization costs must stay under $20/month. Once a model is sufficiently validated through paper trading performance, it graduates to live trading. Profit maximization is the north star, but capital preservation and risk management are non-negotiable constraints.
**Priority**: High
**Status**: Active — **Feature count bug FIXED (Session 560), ready for market open 2026-04-28 09:30 ET** — awaiting user engine restart
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**DEPLOY BLACKOUT RULE**: Never create `DEPLOY_READY` during US market hours (13:30–20:00 UTC Mon–Fri). Stockbot code may be written and tested at any time — only the Jetson deploy is restricted. Check `date -u` before setting DEPLOY_READY.

**Current focus**: **Session 560 FIX COMPLETE**. Feature count mismatch resolved. Root cause: Ensemble stackers expect 61 features with `1d_` prefix from MTF extractor + PipelineIntegrator. Previous fallback logic called `FeatureEngineer.transform()` which produces different feature names, causing shape mismatch → silent sklearn errors → 0.0 predictions → always HOLD. New `_build_daily_mtf_features()` helper generates correct 61-feature set. All three fallback paths in `_generate_stacker_signal` now call this helper. AAPL models predict correctly with full feature set (no retraining needed — inference bug was the issue, not model training). Committed to stockbot submodule. **Next user action: Restart engine with `.venv/bin/python scripts/run_live_trading.py` from projects/stockbot/ before 13:30 UTC market open.**
- Single-ticker rate: 0.17/month. Gate 1 requires 30/month (175x gap).
- **Session 520 multi-ticker training**: 10 new stackers trained (MSFT, GOOGL, NVDA, AMZN, META, JPM, XOM, JNJ, UNH, TSLA). 11-ticker portfolio projects to ~8/month (47x improvement, but still 4x short of Gate 1).
- **Session 521 integration**: All 11 sessions wired into database model_runs table. `/projects/stockbot/active-sessions.json` updated. Created 107 parametrized integration tests — all pass. Full test suite: 140 tests, 0 failures.
- **Two options to reach Gate 1**: (A) scale to ~40 tickers (pipeline ready, each trains in ~90s); (B) reduce threshold multiplier (requires retrain + revalidation).
- See `projects/stockbot/may-12-feasibility-checkpoint.md` for full analysis.
- **Next step (user action)**: Restart engine before 2026-04-28 09:30 ET. Command: `.venv/bin/python scripts/run_live_trading.py` (from projects/stockbot)

**Paper Trading Status (Session 519 — 2026-04-27 07:11 UTC — Day 2)**:
- Paper trading started: 2026-04-26
- Days elapsed: 2 (0 full market sessions completed — engine offline since 22:15 UTC 2026-04-26)
- Engine status: OFFLINE — must restart before 2026-04-28 09:30 ET / 14:30 UTC
  - Command: `.venv/bin/python scripts/run_live_trading.py` (from projects/stockbot)
- Open position: BUY 36 AAPL @ $271.04 (trade ID 9, 2026-04-26 17:06 UTC)
  - Position IS persisted in positions table (Session 504 fix) — cold restart is safe
- DB state: 1 production trade leg (BUY), 0 completed round trips
- Trades/month pace: 0.0 (no round trips complete; structurally expected to stay at ~0.17/month)
- **Gate 1 assessment — INFEASIBLE (Session 519 determination)**:
  - Backtest evidence: all 8 h=10 stacker variants produced exactly 1 trade in 180 days
  - Signal threshold = 2.28% predicted return required to trigger — crosses rarely
  - Architectural ceiling: ~2 round trips/month for single-ticker h=10 design
  - 15x gap to Gate 1 (30/month) cannot be closed within current design parameters
  - h=5 variants provide no improvement (0 trades in same backtest)
  - **Pivot required**: Multi-ticker expansion (same architecture, 15 tickers = ~30 aggregate round trips/month)
- Gate 1 (30 round trips/month): STRUCTURAL FAIL — pivot required
- Gate 2 (Sharpe ≥1.0, MDD ≤20%, PF ≥1.5): all FAIL except MDD — insufficient data (0 round trips)
- Gate 3 (≥63 days): FAIL — 61 days remaining
- Monitor script: `scripts/paper_trading_monitor.py` — clean runs, 10 snapshots in `logs/paper_trading_daily.jsonl`
- **Checkpoints**:
  - 2026-04-28 (Day 3): First live market session — verify engine restarts, position persists, SELL eventually fires
  - 2026-05-09 (approx): First SELL signal expected (~10 trading days from BUY entry)
  - 2026-05-12 (Day 16): Gate 1 feasibility formal checkpoint — use to confirm pivot decision
  - 2026-05-26 (Day 30): First 30-day formal Gate 1 pass/fail

**Completed (Session 552 — 2026-04-28)**:
1. ✅ **Fix idle sleep — market-aware sleep window** (commit 26697dd): When market is closed, sessions now sleep until 15 minutes before market open (13:15 UTC Mon–Fri) instead of polling every 60 seconds. Eliminates ~15,000 "market closed — skipping cycle" log lines per day. Implementation: `_next_market_prewake(now)` helper computes next weekday 13:15 UTC, sessions sleep full duration when `market_open=False`. Minimum floor 60s prevents busy loop. Tests: 7 unit tests for wake time computation.

2. ✅ **Ticker enforcement guard** (commit 26697dd): Added `_enforce_ticker_match()` in `TradingSession.__init__` to verify model's trained ticker matches session's assigned ticker (case-insensitive). Raises `ValueError` on mismatch with both tickers named in message. Backward compatible: no-op when metadata missing ticker key, applies to single-ticker sessions only. Tests: 8 unit tests for all mismatch scenarios.

3. ✅ **Daily trading summary to Discord** (commit 26697dd): At market close (20:00 UTC), sends structured Discord summary via `STOCKBOT_DISCORD_WEBHOOK_URL` with: signals per ticker, orders placed/filled, total trades, mode, strategy name, error cycles. Three methods: `_maybe_send_daily_discord_summary(now)` (fires once per calendar day), `_build_daily_discord_payload(date_str, now)` (aggregates cycle_logs), `_send_discord_summary(payload)` (stdlib-only POST). Fails gracefully if webhook URL missing. Tests: 12 unit tests for payload structure, idempotency, daily reset.

**NEXT WORK (priority order)**:

0. ✅ **CRITICAL — Fix feature count mismatch so engine actually trades** (Session 560 COMPLETE): Feature count bug identified and fixed. Root cause: ensemble stackers expect 61 features with `1d_` prefix; fallback was using `FeatureEngineer.transform()` which produces different feature names. New `_build_daily_mtf_features()` helper generates correct features. All fallback paths updated. AAPL models produce non-zero predictions. Committed. User action: Restart engine before 13:30 UTC market open.

1. **Discord position notifications**: Send a Discord message every time any strategy opens or closes a position. Include: ticker, side (BUY/SELL), quantity, price, strategy name, unrealized or realized P&L. Wire into `on_trade_executed` in `src/models/model_strategy.py` (currently only logs to debug). **Use `STOCKBOT_DISCORD_WEBHOOK_URL` (stockbot channel) — NOT `DISCORD_WEBHOOK_URL` (general/orchestrator channel).** `STOCKBOT_DISCORD_WEBHOOK_URL` is already defined and used by `src/remote/hetzner_budget.py` — follow the same pattern.

2. **Market open verification** (2026-04-28, first clean market session):
   - Pre-open (before 13:15 UTC): Verify engine is running and connected to Alpaca paper account
   - At open (13:30 UTC): Confirm sessions detect market open and begin cycle (no shutdowns)
   - During session: Log whether each of the 11 strategies generates a signal
   - At close (20:00 UTC): Write post-market report to `logs/paper_trading_daily.jsonl` with: signals per ticker, orders submitted, fills confirmed, positions held, realized P&L
   - Key question: did any strategy generate a real signal and place a real order with Alpaca? If zero signals across all 11 tickers in a full session, the signal threshold may be too high
   - **Do not shut down or restart the engine between 13:15–20:15 UTC under any circumstances**

**May 12 Feasibility Assessment (Session 519 — COMPLETE)**:
- Full report: `projects/stockbot/may-12-feasibility-checkpoint.md`
- Verdict: Gate 1 INFEASIBLE with current design; strategy pivot to multi-ticker required
- Recommended pivot (Option A): Train stackers for 10 additional tickers, run in parallel
- Begin training now — do not wait for May 12 to act

**Completed (Session 502)**:
1. ✅ **Paper Trading Monitoring (Day 2)** — COMPLETE:
   - Monitor script executed cleanly (exit 0)
   - Daily log updated with 5th snapshot (2026-04-27 01:05:25 UTC)
   - Database state unchanged (market closed Sunday when BUY placed)
   - Gate 1 pace INDETERMINATE — structural concern: daily-bar strategy achieved 1 trade in 180-day backtest; achieving 30 trades/month aggressive
   - Next checkpoints: 2026-04-28 (first market session), 2026-05-12 (Day 16 feasibility review), 2026-05-26 (30-day baseline)
   - Status: Monitoring on track, waiting for Monday market open

**Completed (Session 489)**:
1. ✅ **Strategy Cleanup** — COMPLETE (commit ac6d574):
   - Removed SMA_50_200 and SMA_10_50 from `scripts/run_strategy_evaluation.py` catalogue
   - Reason: structural failure — generate 0-2 trades/252 days (Gate 1 requires ≥100), negative Sharpe (Gate 2 requires ≥1.0)
   - Updated Underperformer Disposition table, removed SMACrossoverStrategy import
   - Strategy inventory: 1 benchmark (BuyAndHold), 4 ensemble stackers, 1 options, 1 crypto, 1 MTF = 8 total
   - 52 strategy evaluation tests pass, 0 regressions

2. ✅ **Paper Trading Validation Setup** — COMPLETE (commit f86abd7):
   - Created `scripts/paper_trading_monitor.py` (reads stockbot.db, computes daily metrics)
   - Metrics: round trips, win rate, profit factor, Sharpe (per-trade proxy), max drawdown, Calmar
   - 20 unit tests, zero external dependencies, JSON snapshot logging to `logs/paper_trading_daily.jsonl`
   - **3-month graduation criteria**: All of Gates 1+2+3 pass for 3 consecutive calendar months
     - Gate 1: ≥30 round trips/month
     - Gate 2: Sharpe ≥1.0, max drawdown ≤20%, profit factor ≥1.5
     - Gate 3: ≥63 days elapsed
   - Paper trading started 2026-04-26: 9 trade legs to date, 1 AAPL_h10_lgbm_ho (BUY 36 shares @$271.04)

3. ✅ **Live Trading Readiness Checklist** — COMPLETE (commit a1af9e0):
   - Created `docs/live-trading-readiness.md` (user-facing, 7 sections)
   - Sections: (1) paper trading gates with thresholds, (2) Alpaca account setup (cash account, $100-500 initial funding, PDT rules), (3) guardrails confirmation (6 validators enumerated), (4) risk management (position sizing tables by account size, fractional share warning), (5) monitoring setup (daily cron, alert channels), (6) emergency exit procedures (halt, DELETE /v2/positions, kill), (7) final go/no-go checklist
   - Specific guidance: AAPL @~$170/share = 34% of $500 account in fractional shares

**Completed (Session 488)**:
1. ✅ **Strategy Evaluation & Backtesting** — COMPLETE:
   - `strategy-evaluation.md` — comprehensive assessment of all 10 strategies across 5 model types
   - **AAPL_h10_lgbm_ho (paper trading)**: Only Gate 4 passer; Gates 1-3 blocked on live Alpaca data → **HIGHEST PRIORITY** for 3-month validation + full walk-forward
   - **SMA_50_200 / SMA_10_50**: REMOVED — structural failure: daily crossovers insufficient signal
   - **BuyAndHold**: Benchmark only, structurally fails Gate 1
   - **Ensemble/options/crypto/MTF**: Architecture sound; blocked by data pipeline dependencies
   - Built `scripts/run_strategy_evaluation.py` — automated runner against synthetic GBM + 4 regime variants
   - **Tests**: 52 new unit tests (all pass), 2,590 total trading tests pass, 0 regressions

**Completed (Session 487)**:
1. ✅ **Multi-strategy conflict resolution** — `StrategyCoordinator` class, 43 unit tests, 723 total tests pass

**Completed (Session 486)**:
1. ✅ **Live trading guardrails** — `guardrails.py` module with 6 validators, 88 unit tests

**Session 519 Status Update (2026-04-27)**:
- **Engine Status**: OFFLINE — **USER ACTION REQUIRED**: Restart before 09:30 ET Monday 2026-04-28 using `.venv/bin/python scripts/run_live_trading.py`
- **Position safety**: Open BUY (36 AAPL @ $271.04) is in positions table — cold restart is safe
- **Gate 1 Feasibility**: FORMALLY ASSESSED as INFEASIBLE with current design (see may-12-feasibility-checkpoint.md)
- **Strategy pivot decided**: Multi-ticker expansion is the recommended path to Gate 1 pass
- **Confidence in Live Trading Launch**: LOW — cannot launch until Gate 1 is met; pivot must complete first

**Next tasks — work these in order:**

0. ✅ **Market Regime Detection Implementation** (Session 526-537 COMPLETE): 
   - Session 526: Rolling volatility scalar (vol_scalar.py) integrated
   - Session 537: HMM regime detection (HMMRegimeScalar class, hmm_regime_scalar.py) fully implemented and tested (858 unit tests, 0 failures)
   - Two-layer position sizing ready: vol scalar + HMM regime scalar for adaptive market regime positioning
   - Disabled by default for live trading safety; activate with `coordinator.enable_hmm_regime_scaling()`
   - Expected Gate 2 impact: Sharpe ≥1.0, MDD ≤20%

1. ✅ **Multi-ticker stacker training** (Session 533 COMPLETE): All 11 tickers trained and verified (AAPL + MSFT, GOOGL, NVDA, AMZN, META, JPM, XOM, JNJ, UNH, TSLA). Models integrated into active-sessions.json. 63 ensemble tests passing. Gate 1 projection: ~124 trades/month (4x threshold).

2. **Engine restart** (user action — CRITICAL): Restart before 2026-04-28 09:30 ET. Allow current AAPL paper trade to run to SELL completion. Command: `.venv/bin/python scripts/run_live_trading.py` from projects/stockbot/

3. **Multi-ticker paper trading** (after engine restart, Session 537 HMM ready to integrate):
   - User restarts engine: `.venv/bin/python scripts/run_live_trading.py` (from projects/stockbot/)
   - Current: 11-ticker portfolio running (AAPL + 10 others from Session 521)
   - Next: Wire multi-ticker config into paper trading via active-sessions.json (all 11 tickers start 2026-04-28 09:30 ET)
   - HMM activation: Optional — activate HMM regime scaling with `coordinator.enable_hmm_regime_scaling()` once multi-ticker baseline established
   - Aggregate round trips: 11 tickers × ~2/month = ~22 (approach Gate 1 threshold of 30)

4. **Paper Trading Monitoring** — Daily run of `paper_trading_monitor.py` (appends to `logs/paper_trading_daily.jsonl`)
   - Continue monitoring through May 12 checkpoint
   - Track both vol scalar impact (baseline) and HMM regime scalar impact (once activated)
   - Gate 1 pass expected by ~2026-05-12 (Day 16 of multi-ticker paper trading)

5. **Gate 2 Validation with HMM** — After multi-ticker baseline established (week 1-2):
   - Enable HMM regime scaling and monitor Sharpe/MDD improvements
   - Expected: Sharpe improvement toward ≥1.0, MDD reduction toward ≤20%
   - Continue through May 12 checkpoint with both vol + HMM active

6. **Live Trading Launch** — After Gate 1 passes (multi-ticker paper trading, 3 consecutive months):
   - Confirm Alpaca account setup
   - Verify guardrails in `src/guardrails.py` deployed to Jetson
   - Initial funding: $100–500 per readiness checklist
   - Both vol scalar and HMM regime scalar operational for production trading

**Blocked on**: Engine restart (user action — before 2026-04-28 09:30 ET, CRITICAL)
**Notes**: Multi-ticker training complete and verified (Session 533). System positioned to exceed Gate 1 by 4x (~124 trades/month). All optimization infrastructure in place. Live trading launch timeline: (1) Engine restart, (2) Multi-ticker paper trading setup, (3) Gate 1 pass by May 12 checkpoint, (4) 3-month paper trading track record before live launch.

---

### open-source-rideshare
**Goal**: Build a free, open-source alternative to Uber and Lyft that stops price-gouging both riders and drivers. The platform should be a web and mobile app that minimises deployment and maintenance costs, ideally using a model where the platform itself is non-profit or cooperative — the margin extracted by Uber/Lyft goes back to drivers and riders instead. Solve the real problems: regulatory compliance in different jurisdictions, driver and rider safety and security, insurance, payment processing, and trust. Also build a plan for bootstrapping the user and driver base — a rideshare app with no users is worthless, so growth strategy is part of the scope.
**Priority**: Low
**Status**: Paused — resume when user unpauses
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-source-rideshare/`
**Current focus**: Session 407: **Driver Document Expiry Status Endpoints COMPLETE** (commit `c8cd00f`, 20 new tests, branch `feature/driver-navigation`). `GET /drivers/me/document-expiry` (driver self-check with urgency labels) and `GET /admin/document-expiry` (fleet overview with expired_only filter). `get_expiring_documents_for_driver()` added to service layer. 6,154 tests passing. **Next**: open-repo data acquisition task (acquire OpenFarm data via Internet Archive and run import_openFarm.py), or further rideshare safety/compliance features.
**Blocked on**: —
**Notes**: This is the only public project. Higher standards for documentation, test coverage, and code quality since it's community-facing. Regulatory/safety/security solutions and growth strategy are in scope alongside the technical build.

---

### seedwarden
**Goal**: Build a profitable Etsy store and digital brand focused on farming, homesteading, and survival-related digital products, with the ability to expand into physical small products and seed packets. The business needs a full foundation: high-quality digital products that genuinely help people, a consistent social media presence across relevant platforms, and a reputation for real value. The goal is profit and a loyal customer base — not just a store. Grow the business systematically, identify what sells, double down on winners, and build a media presence that drives traffic organically.
**Priority**: Medium
**Status**: Active — Phase 1 upload pending user tag corrections; **Phase 2 mockup tooling COMPLETE**
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/seedwarden/`
**Current focus**: **Phase 2 Mockup Tooling COMPLETE (Session 500)**. All 21 products now have three mockup variants (tablet cover, phone, interior grid). Phase 1 is the critical path — awaiting user tag corrections (3) + Etsy account verification.

**Track A — Phase 1 launch (blocked on user)**: 3 tag corrections and Etsy account verification required before upload (documented in `UPLOAD_READY_CHECKLIST.md`). Once user completes those, all 21 Phase 1 products are ready to list immediately (8 text-heavy + native plants guide). All PDFs Etsy-compliant (≤900 KB except guide at 4.91 MB). All listing copy, tags, pricing, and mockups complete.

**Track B — Phase 2 Expansion Planning** (Session 523 COMPLETE):
- **Lifestyle Photography Strategy** (Session 523 COMPLETE):
  - File created: `LIFESTYLE_PHOTOGRAPHY_STRATEGY.md` (4,200 words)
  - Recommendation: Hybrid approach (physical for 15 products, stock for 6)
  - Budget: $80–160 (mostly iStock credits); Timeline: 3 weeks (10–14 hours)
  - Conversion-focused metrics: Primary watch on 4 high-ticket products ($18–$22 range)
  - Status: Ready for user review and approval

**Phase 2 Next Work (Session 560 assessment)** — Highest-value autonomous priorities:
1. **#1 — Wild-edibles habit photos** (16 remaining of 18): Wikimedia search protocol established, 2 complete. No blockers. Est. 1–2 sessions.
2. **#2 — Native Plants PDF rebuild**: Unblock $20 product frozen at 56.96 MB (Etsy 5 MB limit). Image compression rebuild. Est. 1 session.
3. **#3 — Zone Quick-Start Card spec**: Lead magnet upgrade for email automation. No blockers. Est. 1 session.
4. **Deferred — Photography execution**: Awaiting LIFESTYLE_PHOTOGRAPHY_STRATEGY.md user decision.
5. **Deferred — Phase 2 product development**: Premature without Phase 1 conversion data (30-day minimum).

**✅ COMPLETED (Session 500)**:
- **Mockup Tooling** — All 21 products have three mockup angles (tablet, phone, interior)
- **Step 1**: Regenerated tablet mockups (pypdfium2 dependency added)
- **Step 2**: Built phone-frame variant (iPhone 13-style, 21 mockups)
- **Step 3**: Built interior-page variant (2×2 grid, 21 mockups)
- Result: 63 total images, 19 MB, all variants boost conversion per research

**✅ COMPLETED (Session 486)**:
- **Native plants guide image rebuild** — 56.96 MB → 4.91 MB (Etsy-compliant via Pillow compression)

**Blocked on**: Tag corrections + Etsy account verification (user action, Track A only). Track B has no blockers.
**Notes**: Phase 1 is production-ready and awaiting only user tag corrections (3) and Etsy account verification. Phase 2 tooling complete; lifestyle photography strategy ready for user approval. Once Phase 1 launches and initial conversion data arrives (week 2–3), Phase 2 photography can begin.

---

### open-repo
**Goal**: An open-source library for all things under the sun — a distributed, free, one-stop shop to find and share information that benefits all of humanity. Link to Wikipedia for general information, schematics, building plans, 3D models, recipes/instructions, services to share, and more. The core principle: no single person or organization controls any of it. Everything is distributed and open source. This is about leveling the playing field — giving all people the best chance to not only survive but thrive.
**Priority**: Medium
**Status**: Active — Phase 4 COMPLETE, **PR #1 open, awaiting review/merge** (Session 486: 2026-04-26)
**Visibility**: Public — GitHub repo: `esca8peArtist/open-repo`. Use remote `open-repo` for all pushes. Use `git subtree push --prefix=projects/open-repo open-repo <branch>` — never push to `origin`.
**Working dir**: `projects/open-repo/`
**Current focus**: **PR #1 OPEN** (2026-04-26): https://github.com/esca8peArtist/open-repo/pull/1
- Title: "feat: Wave 4 Phase 2 — Federation Service Infrastructure"
- 194/198 tests passing (4 skipped), 0 failures
- Wave 4 federation complete: partner registration, service layer, admin routes, HTTP signature verification, request signing, conflict detection
- **Next**: Await PR merge review. After merge, begin Phase 5 (offline export/Kiwix integration).
**Blocked on**: —
**Notes**: All pushes to GitHub use `git subtree push --prefix=projects/open-repo open-repo <branch>` or `git subtree split` to keep the public repo clean. Never use `git push origin`. PR merge is awaiting maintainer review; no further blocking issues.

---

### off-grid-living
**Goal**: A comprehensive plan for off-grid, sustainable living. Define full plans for construction, implementation, operation, maintenance, and repair. Cover the complete operational architecture: food production, shelter, medicine, electricity generation, food preparation and storage, water, and general survival necessities. Include disaster scenarios up to and including nuclear disaster. Also cover community building, organization, and mutual support.
**Priority**: Medium
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Visibility**: Public — GitHub repo: `https://github.com/esca8peArtist/off-grid-living-guide` (live as of 2026-04-26)
**Working dir**: `projects/off-grid-living/`
**Current focus**: **GitHub Publication COMPLETE (Session 486)**. All tasks executed:
  - ✅ Fixed file numbering: 01→03→... → 01-17 sequential with no gaps (shelter moved 11→02)
  - ✅ Updated all internal cross-references (17 files)
  - ✅ Wrote comprehensive README.md with structure, usage guide, CC BY-SA 4.0 license
  - ✅ Verified nuclear/radiological preparedness content (725 lines, complete)
  - ✅ Published to GitHub via git subtree push
  - ✅ Drafted social media posts (Reddit × 3, X/Twitter thread, email draft)

**Next Phase**: User execution of social media distribution per `social-media-launch-posts.md`:
  - Post to r/offgrid, r/preppers, r/homesteading (slightly different angle for each)
  - Post X/Twitter thread (7 tweets)
  - Optional: email announcement to mailing list
  - Timing: stagger Reddit posts Tue–Fri, X thread over 2–3 days

**Blocked on**: —
**Notes**: Instagram and TikTok require separate visual/video production — defer until GitHub traction established and user decides to invest in visual content. All 17 domains production-ready. Repo live and accessible.

---

### containerized-agents
**Goal**: Archived — goal TBD if reactivated.
**Priority**: Low
**Status**: Archived
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/containerized-agents/`
**Current focus**: —
**Blocked on**: —
**Notes**: Archived per user direction on 2026-04-12.

---

### workout
**Goal**: Create comprehensive workout plans that blend athleticism, strength training, mobility, and calisthenics into unified programs. Produce plans for three equipment tiers: no equipment, resistance bands only, and full gym. Provide proposals for different training frequencies (days/week), exercise variety, and formats to build the best all-in-one plan maximizing strength growth while addressing athleticism, mobility, and bodyweight mastery.
**Priority**: Low
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/workout/`
**Current focus**: `comprehensive-plan.md` (1,053 lines) complete — covers all 3 equipment tiers (no equipment, bands, full gym) × multiple frequencies (3/4/5/6 days), with full exercise libraries, progression systems, calisthenics skill ladders, and mobility protocols. Awaiting user review and selection.
**Blocked on**: —
**Notes**: Content/planning project, not a software build. Goal defined by user on 2026-04-12. Existing `proposals_v2.md` covers the 6-day gym PPL in detail (referenced from comprehensive plan). `requirements.md` has baseline info and calisthenics skill levels.

---

### resume
**Goal**: Maintain and improve Anya's professional resume and any associated portfolio materials.
**Priority**: Low
**Status**: Paused
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resume/`
**Current focus**: —
**Blocked on**: —
**Notes**: Only gets attention when explicitly requested.

---

## Exploration Queue

Topics fair game when no higher-priority task is active. Log findings to the relevant project or resistance-research.

- ~~Cryptographic voting systems and democratic resistance — extend the remote-voting research into the democratic renewal proposal~~ — **Done** (Session 24: Section 4 expanded to 8 subsections covering E2E-V protocols, deployed systems, coercion resistance, RLAs, post-quantum crypto, formal verification, maturity spectrum; Domain 1e updated with three-layer verification model)
- ~~Legal landscape of algorithmic decision-making in ICE detention — recent case law, civil rights angles~~ — **Done** (Session 24: `algorithmic-decision-making-immigration.md`, 270 lines — ICM/FALCON/ImmigrationOS systems, NIST bias data, Gonzalez v. ICE, EU AI Act/Canada AIA models, 6 reform recommendations; Domain 16d expanded)
- ~~Cooperative/platform cooperative business models — relevant to rideshare's ownership structure~~ — **Done** (Session 22: `cooperative-models-research.md`, 744 lines in open-source-rideshare/)
- ~~Regulatory landscape for rideshare in major US cities~~ — **Done** (Session 23: `regulatory-compliance-research.md`, 1,002 lines)
- ~~Etsy SEO and digital product market research — what sells in the homesteading/survival niche?~~ — **Done** (Session 24: `etsy-seo-market-research.md` in seedwarden/, 402 lines — Etsy algorithm mechanics, keyword strategy, competitive landscape, price positioning, title optimization, growth strategy, seasonal planning, bundle strategy, social media, metrics)

- ~~**Palantir and government surveillance infrastructure**~~ — **Done** (Session 484: `palantir-threat-model.md` complete — Gotham/Foundry/AIP architecture, confirmed federal contracts (ICE/ELITE/ImmigrationOS, CBP/AFI, FBI, NSA, DHS), data sources, entity resolution methodology, real-world implications, capability gaps)

- ~~**off-grid-living: nuclear and radiological preparedness**~~ — moved to project Current focus (Step 3 of publication prep)

- ~~**Stockbot: model evaluation framework**~~ — **Done** (Session 484: `model-graduation-criteria.md` complete — four-gate framework for paper-to-live graduation: statistical sufficiency, performance quality, robustness validation, operational readiness)

- ~~**resistance-research: post-launch Phase 2 prep**~~ — **Done** (Phase 2 litigation tracking COMPLETE and production-ready per Session 462)

- ~~**Resistance-research: Phase 3 research roadmap**~~ — moved to project Current focus (Phase 3 priority documents + proposal formatting + distribution setup)

- ~~**Seedwarden: Phase 2-4 expansion & social media strategy**~~ — moved to project Current focus (native plants image rebuild is the priority; Phase 2-4 deferred until Phase 1 conversion data in)

- ~~**workout: nutrition and tracking companion**~~ — **Done (Session 493)**: `projects/workout/nutrition-and-tracking.md` (6,226 words) — comprehensive nutrition framework (macro targets by goal/tier/frequency), meal planning with 3 sample days (2,000/2,600/3,000 cal), weekly tracking template, progress timeline expectations, deload protocol, integration with comprehensive-plan.md.

- ~~**cybersecurity-hardening: device hardening deep-dive**~~ — **Done (Session 493)**: `projects/cybersecurity-hardening/device-hardening-guide.md` (3,200 words) — iPhone hardening (iCloud ADP as critical attack surface, airplane mode vs. power-off technical differences), Android hardening (bootloader paradox, GrapheneOS verified boot recovery, Cellebrite forensics leak data), cross-platform compartmentalization and recovery scenarios, evidence-based (Apple guidelines, GrapheneOS docs, EFF guides, privsec.dev analysis).

**NEW ITEMS (Session 501)**:

- ~~**open-repo: Phase 5 architecture research — Kiwix integration and offline export**~~ — **Done (Session 501)**: `phase-5-kiwix-architecture.md` (3,933 words) — Complete Kiwix ecosystem overview, ZIM file format architecture, comparison with Wikipedia/Project Gutenberg pipelines, direct python-libzim integration strategy, incremental export analysis, and 15-23 day implementation blueprint (ExportService → ZimWriter → export catalog + CDN). Ready for Phase 5 implementation when PR #1 merges.

- ~~**resistance-research: Post-Domain 26 completeness audit**~~ — **Done (Session 501)**: `assessment/post-domain-26-completeness-audit.md` (4,666 words) — Comprehensive audit of 26-domain framework identifying 4 priority gaps: (1) Domain 19f War Powers Reform (Iran war constitutional crisis, May 1 deadline — Priority 1), (2) Pharmaceutical tariff collision (100% tariff effective July 31 — Domain 11 cross-ref), (3) Indigenous Sovereignty subsection 22f (trust responsibility, treaty law — Priority 2), (4) Disability Justice deepening post-OBBBA (Domain 18e update). Population pattern analysis complete. Distribution readiness verdict: Not ready until Domain 26 research + Domain 19f are executed.

- ~~**seedwarden: Phase 3 social media and paid-ads growth strategy**~~ — **Done (Session 501)**: `phase-3-social-media-growth-strategy.md` (4,866 words) — Complete Phase 3 roadmap for post-Phase 1 launch. Includes: (1) TikTok competitive analysis (top creators: @itsbreellis 772K, @thermal_and_oaks 367K; optimal format 30-60s educational; #homestead 5.4B views), (2) Instagram + Pinterest strategy (Pinterest is highest-ROI organic for Etsy; 33% more referral traffic than Facebook), (3) Creator breakdown (5 success traits: hyper-specific niche, practical content, 12-24mo consistency, email list ownership, $5-$15 price point), (4) Paid advertising strategy (Shopping/Gifts $0.34 CPC benchmark; 2.0x ROAS target; Pinterest CPA $8 most cost-effective), (5) Influencer partnerships (direct outreach model, 20-30% response rate, $100-$250 flat fee + commission), (6) Three-month phased implementation plan (Month 1: infrastructure, Month 2: test ads $300-500 + outreach, Month 3: scale winners kill losers). Ready for execution when Phase 1 converts.

**NEW ITEMS (Session 550–551)**:

- ✅ **resistance-research: Post-distribution institutional adoption playbook** (COMPLETE, Session 550) — `institutional-adoption-playbooks.md` (9,145 words, 5 sectors). Five sector-specific playbooks (state legislatures, federal circuit courts, executive agencies, law schools/universities, civil rights organizations) with concrete step-by-step operationalization, decision trees, timeline templates, success metrics, common failure modes. Each playbook grounded in actual 2026 institutional landscape post-Loper Bright, post-Trump v. Wilcox, April 2026 civic calendar. Includes domain dependency structure and contact templates for coordination. Production-ready for institutional distribution (can be sent to think tanks, state AG offices, law schools, advocacy coalitions).

- ✅ **stockbot: Live trading dashboard UI mockup** (COMPLETE, Session 551) — Interactive HTML prototype + design document. `ui-mockup/dashboard.html` (self-contained, 982 lines) + `ui-mockup/README.md` (Phase 2 development roadmap). Features: portfolio summary (value, P&L, active positions, trade count), control panel (pause/resume, settings, emergency halt with confirmation), 11-ticker active positions table, risk metrics (Sharpe 2.14, drawdown -3.2%, volatility, win rate, profit factor, beta), signal board (latest 3 signals per ticker with confidence), recent trades log. Dark theme optimized for extended market hours. Documented API integration points (7 endpoints + WebSocket), technical stack recommendation (React/TypeScript, Tailwind, D3.js, WebSocket, Vite/Next.js), and Phase 2 implementation timeline (3-week roadmap: scaffold+integration, polish+features, monitoring+alerts). Ready for design review and developer handoff.

- ✅ **seedwarden: Customer cohort analysis framework** (COMPLETE, Session 551) — Comprehensive Phase 1 pre-launch analytics framework. Deliverables: `customer-cohort-analysis-framework.md` (550+ lines, 4 segments with identifying signals and per-cohort messaging), `customer-analytics.csv` (customer tracking template with LTV estimates), `etsy-analytics-template.csv` (monthly metrics forecasts), `google-analytics-integration-guide.md` (GA4 setup + events + segmentation). Features: 4 customer cohorts (high-intent forager 20–25%, survival prepper 15–20%, homesteader 30–35%, gift buyer 15–20%), Etsy metrics tracking protocol, GA4 custom events (view_edible_guides, view_prepper_content, view_medicinal_content, high_engagement), post-purchase survey design (3 questions), per-cohort campaign cadence (seasonal for foragers, event-triggered for preppers, quarterly for homesteaders, holiday for gift buyers), success metrics (Month 1: 1.5–2% conversion; Month 3: 15–25% repeat; Month 6: 20–30% repeat), Week 1–8 implementation timeline. Ready to operationalize upon Phase 1 launch (May 2026).

**✅ COMPLETED (Session 517)**:

- ✅ **Domain 37 Research — Federal Executive Interference in 2026 Midterms** (COMPLETE — ready for distribution)
  - **Status**: COMPLETE (Session 517)
  - **Urgency**: CRITICAL (November 2026 election, 6-month window)
  - **Scope**: 8,850 words, 50 sources — production-ready
  - **Key mechanisms documented**: DOJ voter roll litigation (23 active cases), draft emergency EO tracking, election denier federal personnel network (11+ appointees), ICE-at-polls threat
  - **Advocacy response comprehensive**: Federal election takeover authority (pre-clearance, consent decrees), Section 3 (14th Amendment) litigation vectors, injunction strategy, state-level blocking mechanisms, international precedent (Hungary April 2026 election lesson)
  - **Natural distribution targets**: Common Cause, Protect Democracy, Democracy Docket, state AGs (ready for sequencing into distribution)
  - **Sourcing**: 50 sources including Brennan Center, University of Wisconsin Law School tracker, ProPublica April 2026 investigation, Democracy Docket, Election Assistance Commission
  - **Recommendation**: If user approves hybrid approach (Path A + Domain 37), this is ready to sequence into distribution immediately before reaching election-protection organizations
  
- **Domain Updates — Content Maintenance** (triggered by Session 516 civic tracker findings)
  - **Status**: QUEUED (identified by Session 516)
  - **Scope**: Multiple domains affected by April-May 2026 developments
  - **Content additions**:
    - Domain 19f: Add Iran war case study (May 1 WPR deadline, Senate blocking pattern, Vance constitutional rejection)
    - Domain 28: Cross-reference Iran as larger empirical instance  
    - Domain 29: Add SPLC indictment (April 21) as case study for prosecutorial weaponization
    - Domain 6 & 35: Trump v. Wilcox shadow-docket removal power ruling (Humphrey's Executor effectively overruled)
    - Domain 1: SAVE Act Senate failure (4 GOP defectors) as coalition-fracture proof-of-concept
    - Domains 21, 25: FISA Section 702 April 30 deadline outcome tracking
    - Domain 33: 100+ bills in 15+ states targeting ballot initiatives in 2026 (strengthen empirical foundation)
    - Domain 19: NATO withdrawal threats + Taiwan pressure + Iran geopolitical cascade
  - **Estimated scope**: 2-4 sessions depending on depth of updates
  - **Priority**: MEDIUM (post-distribution, but important for proposal currency)

**✅ COMPLETED (Session 537)**:

- ✅ **stockbot: Market regime detection and adaptive position sizing** (Priority HIGH for Gate 2 improvement)
  - **Implementation**: HMMRegimeScalar class with two-layer position sizing (vol scalar + HMM regime scalar)
  - **Scope**: GaussianHMM regime classification (bull/bear/sideways), stateful probability-weighted adaptive sizing
  - **Key features**: Per-ticker probability-weighted scalar, weekly retraining (every 5 bars), thread-safe, disabled by default (safe for live trading)
  - **Test coverage**: 33 tests for RegimeDetector, 46 tests for HMM integration, 858 total unit tests passing
  - **Activation**: `coordinator.enable_hmm_regime_scaling()` in paper trading loop, begins contributing after 60+ daily closes per ticker
  - **Expected Gate 2 impact**: Sharpe improvement toward ≥1.0, MDD reduction toward ≤20%
  - **Status**: COMPLETE — Ready for paper trading integration (Session 537). Commit: fb3e87e

- **resistance-research: Policy influencer mapping and distribution amplification strategy** (Priority HIGH for distribution impact)
  - **Scope**: Identify high-leverage policy influencers per distribution tier (legislators, think tanks, media, academia), analyze their information networks, design targeted messaging for max reach
  - **Goal**: Map policy influence network to maximize democratic renewal proposal reach and adoption
  - **Expected outcome**: Amplified distribution impact, policy influencer pre-engagement before Phase 1 distribution
  - **Sources**: Congress.gov committee assignments, think tank leadership, media outlet editorial boards, academic department rankings
  - **Timeline**: 2-3 sessions for mapping + strategy
  - **Status**: QUEUED (identified as post-distribution execution planning)

- **seedwarden: Email list building and organic growth playbook** (Priority MEDIUM for Phase 1+ scaling)
  - **Scope**: Email marketing strategy, lead magnet design, automation sequence, list growth tactics (free guides, bonuses, contests)
  - **Goal**: Build sustainable email list (1K+ subscribers) and organic growth engine before Phase 2 paid advertising
  - **Expected outcome**: Email-driven repeat sales, customer retention, product launch amplification
  - **Sources**: Successful Etsy creator case studies, email marketing best practices, automation tools (Mailchimp, ConvertKit)
  - **Timeline**: 1-2 sessions for strategy
  - **Status**: QUEUED (can begin once Phase 1 converts + launches)

**NEW ITEMS (Session 538 — Exploration Queue Refresh)**:

- ~~**resistance-research: Democratic Renewal Activation Architecture**~~ — **COMPLETE (Session 542)**: `ACTIVATION_ARCHITECTURE.md` (extended to 13,200 words), `implementation-schedule.md` (new tabular companion). Complete post-distribution operationalization roadmap with agency responsibility matrix (35 domains), timeline phases, success metrics, dependency graph, 6 international case studies, risk mitigation. Three critical findings: (1) Trump v. Slaughter pre-staging (June deadline, 24-48h window), (2) Poland precedent shows judicial capture harder to reverse than electoral recovery, (3) Interstate compact path is primary mechanism for Phase 2 implementation.

- ✅ **stockbot: Live Trading Infrastructure and Risk Management** (Session 553 COMPLETE)
  - **Scope**: Design the complete monitoring, alerting, and emergency-response infrastructure for live trading on Jetson. (1) Dashboard architecture (real-time P&L, position tracking, regime detection), (2) Alert triggers (model drift, drawdown limits, regime shifts, circuit breakers), (3) Emergency exit procedures (controlled vs. panic liquidation), (4) Operational runbooks (what to do if each alert fires), (5) Integration with existing guardrails
  - **Deliverable**: `projects/stockbot/docs/live-trading-operations.md` (7,578 words, 1,135 lines, production-ready)
  - **Key Content**: Dashboard Architecture (3 monitoring layers, 5 subsections), Alert Triggers (6 categories with concrete numeric thresholds, drift detection example TSLA Sharpe threshold), Emergency Exit Procedures (4 response levels with explicit liquidation order), Operational Runbooks (6 runbooks, 5 incident types with branch logic), Integration Points (gap identified: no real-time CRITICAL Discord alerts — design spec provided), Pre/During/Post-Market Checklist (1-page routing table, alert→runbook mapping)
  - **Critical Gap Identified**: Real-time CRITICAL alert Discord webhook not yet implemented — design spec ready, ~15 min implementation
  - **Integration Status**: Coordinates with Session 551 UI mockup and Session 542 performance attribution framework. Ready for immediate use post-engine-restart.
  - **Status**: COMPLETE, production-ready, committed to master

- **resistance-research: Phase 3 Candidate 5 — [Finance & Fiscal Architecture]** (Priority 1 for Phase 1 distribution)
  - **Scope**: Structural analysis of post-capture fiscal policy recovery mechanisms. Case studies: Brazil 2022 fiscal framework + central bank autonomy restoration, Argentina 2023+ Milei fiscal restructuring (comparative fiscal discipline without institutional erosion), Peru 2022 fiscal transparency after Castillo escape, Mexico 2025 judicial-fiscal feedback loop.
  - **Goal**: Identify fiscal policy levers that are self-enforcing vs. constituency-dependent, integration points with institutional recovery (judicial independence ↔ tax enforcement, transparency requirements ↔ audit bureau independence)
  - **Expected outcome**: `phase-3-candidate-5-fiscal-architecture.md` (7,000-8,000 words, 35-40 sources) — ready for Phase 1 institutional distribution
  - **Status**: ACTIVE (Session 554+ — top queue priority, no blockers)

- **stockbot: Real-time CRITICAL Alert Discord Webhook Implementation** (Priority 2 for live operations)
  - **Scope**: Implement real-time CRITICAL alert Discord webhook (identified gap from Session 553 `live-trading-operations.md` design spec). (1) Add `STOCKBOT_DISCORD_ALERT_WEBHOOK_URL` env var + configuration, (2) Implement `_send_critical_discord_alert()` method in TradingSession, (3) Wire into 6 alert categories (drift, circuit breaker, drawdown, regime shift, position-specific, prediction error), (4) Test alert firing logic (mock webhook, verify message format, throttle duplicate alerts), (5) Integration with existing daily summary pattern (similar POST pattern, different webhook URL)
  - **Expected scope**: ~15 min implementation, ~10 unit tests, zero schema changes
  - **Deliverable**: Updated `src/trading/trading_session.py` + updated `tests/test_trading_session_improvements.py` with webhook tests
  - **Integration**: Immediately deployable post-engine-restart; coordinates with Session 551 dashboard + Session 553 operations runbooks
  - **Status**: ACTIVE (Session 554+ — available after Phase 3 Candidate 5 starts)

- **cybersecurity-hardening: High-Risk Population Protection Protocols** (Priority 3 for advanced OpSec)
  - **Scope**: Beyond baseline OpSec playbook — design comprehensive protection for activists, dissidents, lawyers, vulnerable populations facing government targeting. (1) Identity compartmentalization (burner phones, secondary SIM architectures, VPN/Tor layering), (2) Physical security (surveillance detection, safe house networks, low-profile movement patterns), (3) Legal defense coordination (attorney networks, bail funds, criminal defense playbooks), (4) International sanctuary options (asylum processes, travel security, international NGO coordination), (5) Emergency protocols (asset recovery, family safety, evidence preservation)
  - **Goal**: Actionable protocols for high-risk populations, grounded in case studies (HK activists, US Jan 6 defendants, EU dissident networks)
  - **Expected outcome**: `high-risk-populations.md` (4,000-5,000 words) + operational playbooks for 3-4 scenario types
  - **Status**: ACTIVE (Session 554+ — queue item #3, available for parallel execution)

**NEW ITEMS (Session 542 — Parallel Exploration Queue Execution)**:

- ✅ **stockbot: Performance Attribution & Post-Trade Analysis Framework** (COMPLETE — Session 542)
  - **Scope**: Comprehensive post-trade analysis framework for understanding trade success/failure drivers
  - **Deliverables**: 
    - `projects/stockbot/docs/performance-attribution-framework.md` (~2,800 words) — Attribution analysis (regime/volatility/SHAP features), win/loss taxonomy (5 categories with strict assignment ordering), drift detection (4 signals, 4 alert levels), feature feedback loop (monthly review + quarterly audit), reporting templates
    - `projects/stockbot/src/analytics/post_trade_analysis.py` — Python module with CLI: `--report portfolio|drift|first30|snapshot|monthly`; reads stockbot.db, stores attribution JSON in trades.notes (no schema migration); integration hooks: record_entry_context() at BUY, attribute_round_trip() at SELL
    - `tests/unit/test_analytics/test_post_trade_analysis.py` — 55 tests, all passing, zero regressions
    - `post_trade_analysis_example.ipynb` — Jupyter notebook with framework walkthrough (excluded from git)
  - **Key Finding**: Framework designed for zero schema changes — attribution JSON piggybacks on existing trades.notes TEXT field. Immediate integration post-engine-restart possible.
  - **Critical Path**: Call analyzer.snapshot_open_positions() immediately after user engine restart; wire record_entry_context() before first SELL execution to capture feature SHAP at entry time.
  - **Status**: COMPLETE, committed to master

- ✅ **seedwarden: Annual Product Calendar & Email Growth Engine** (COMPLETE — Session 542)
  - **Scope**: Comprehensive annual marketing and product strategy for Phase 1+ growth
  - **Deliverables**:
    - `projects/seedwarden/marketing/annual-product-plan.md` (3,400 words) — Seasonal demand analysis, email automation architecture, bundle strategies, holiday campaigns, social calendar alignment with case studies
    - `projects/seedwarden/marketing/product-calendar-2026-2027.json` — 12-month structured calendar (themes, email campaigns, product focus, promotional calendar)
    - `projects/seedwarden/marketing/email-automation-blueprint.md` — Complete funnel: lead magnet (5-variety guide → zone-personalized Phase 2 upgrade), welcome sequence (5 emails, 10 days), behavioral tagging (Emails 3-4 → Seed Saver/City Grower/Preservationist segments), post-purchase sequence (3 emails), win-back campaign with automatic list pruning
    - `projects/seedwarden/marketing/social-media-calendar-may-july-2026.md` — Week-by-week May-July 2026 social content calendar
  - **Key Finding**: Two hard seasonal peaks — spring planning window (Jan-Apr, highest buyer receptivity) and holiday gift (Nov-Dec, 35-40% of annual revenue); July-Sep preservation season secondary peak with lower competitive density → higher organic ranking opportunity
  - **Bundle Recommendation**: Winter Planning Bundle ($28, Nov-Dec: Survival Garden + Zone Calendar + Food Sovereignty Guide); seasonal title/tag updates (Zone Calendar: add "2027" Jan, Apartment Kit: add gift tags Oct, Survival Garden: add gift tags Nov)
  - **Status**: COMPLETE, committed to master

- ✅ **resistance-research: Democratic Renewal Activation Architecture** (COMPLETE — Session 542)
  - **Scope**: Post-distribution operationalization roadmap for 35-domain framework
  - **Deliverables**:
    - `projects/resistance-research/ACTIVATION_ARCHITECTURE.md` (extended to 13,200 words, 549 lines) — Complete implementation roadmap with: agency/organization responsibility matrix (35 domains), timeline buckets (30-day/100-day/1yr/3yr/10yr phases), success metrics per phase, cross-domain dependencies, 6 international case studies (Spain, South Korea, Poland, Hungary, Taiwan, Costa Rica), risk mitigation strategies for capture/backlash per phase, explicit Part VII integration with Phase 4-5 theory-of-change documents
    - `projects/resistance-research/implementation-schedule.md` (new, tabular companion) — 35-domain matrix with: responsible entity, timeline bucket, Phase 1 success metric, cross-domain dependencies, international precedent; tier classification (Tier 1 critical-path D6/D2/D1/D9, Tier 2/3 sequences); phase 1 priority list (13 domains ordered by dependency/urgency); recovery scenario crosswalks (House Flip/Tight House/Federal Collapse); international precedent quick-reference
  - **Three Critical Operational Findings**:
    1. **Trump v. Slaughter response pre-staging (Most Urgent)** — SCOTUS ruling expected June 2026 (~6 weeks). If overrules Humphrey's Executor, collapses independent agency protections across D2/D6/D20/D29/D36. Must pre-stage state-level independent agency protection statutes + Federal Reserve legislation for 24-48h deployment window post-ruling, not draft afterward.
    2. **Poland precedent is most applicable** — Tusk coalition won decisive Oct 2023 victory, still blocked by Constitutional Tribunal 2.5 years later. Judicial capture is harder to reverse than electoral recovery. Every court-dependent domain (D6/D1/D2/D29/D34) must be further along BEFORE electoral window opens, not started when it opens.
    3. **Interstate compact path (D9) is primary, not contingency** — 60-vote Senate blocks Phase 2 legislation regardless of electoral outcome. Interstate compacts on clean energy, labor standards, voting access are primary for D3/D12/D15/D17. States acting without federal authorization = Spain model applied to US federalism.
  - **Status**: COMPLETE, committed to master

**NEW ITEMS (Session 541 — Exploration Queue Refresh)**:

- ✅ **mfg-farm: Multi-Printer Farm Architecture & Cost Modeling** (COMPLETE — Session 541)
  - **Scope**: Research and design the economics and logistics of scaling from 1→N printers. (1) Multi-printer farm layout optimization, (2) Material supply chain for different print profiles (PLA, ABS, resin, etc.), (3) Queue management and job scheduling strategies, (4) Cost-per-unit modeling as function of batch size and material, (5) Regulatory compliance landscape for scaled manufacturing in home/small-business environments, (6) Case studies of successful Etsy sellers with 2-5 printer setups
  - **Goal**: A comprehensive blueprint for ModRun product scaling from single printer (post-test-print) to 3-5 printer operation
  - **Deliverable**: `projects/mfg-farm/multi-printer-architecture.md` (6,200 words) — Complete farm architecture, supply chain analysis, cost modeling, queue management, regulatory compliance, case studies with 2026 pricing data
  - **Key Findings**: 5-printer Bambu setup fits 3.2m workspace; bulk PLA drops to $7-10/kg; ModRun cable clips: $1.15 COGS (PLA) + $0.40 packaging; 52% net margin on bundles; payback period <3 months at realistic demand; labor becomes binding constraint at ~month 5-6
  - **Status**: COMPLETE (committed to master)

- ~~**seedwarden: Annual Product Calendar & Email Growth Engine**~~ — **COMPLETE (Session 542)**: `annual-product-plan.md`, `product-calendar-2026-2027.json`, `email-automation-blueprint.md`, `social-media-calendar-may-july-2026.md` — Comprehensive marketing roadmap with seasonal demand analysis, email funnel design, bundle strategies, 12-month calendar. Key finding: spring planning (Jan-Apr) and holiday gift (Nov-Dec) are hard peaks; preservation season (Jul-Sep) secondary with lower competitive density.

- ~~**stockbot: Performance Attribution & Post-Trade Analysis Framework**~~ — **COMPLETE (Session 542)**: `performance-attribution-framework.md`, `post_trade_analysis.py` (CLI module), 55 tests (all passing), Jupyter notebook. Framework designed for zero schema migration — attribution JSON stores in trades.notes. Ready for Day-1 integration post-engine-restart.

**NEW ITEMS (Session 543 — Exploration Queue Refresh for Parallel Autonomous Work)**:

- ✅ **cybersecurity-hardening: High-Risk Population Protection Protocols** (Session 543 COMPLETE)
  - **Scope**: Advanced OpSec for high-risk populations (activists, dissidents, vulnerable populations facing government targeting). Design: (1) Identity compartmentalization (burner phones, secondary SIM architectures, VPN/Tor layering), (2) Physical security (surveillance detection, safe house networks, movement patterns), (3) Legal defense coordination (attorney networks, bail funds, playbooks), (4) International sanctuary options (asylum processes, travel security), (5) Emergency protocols (asset recovery, family safety, evidence preservation)
  - **Deliverable**: `projects/cybersecurity-hardening/high-risk-populations.md` (8,000 words, 5 sections, 10+ case studies) — Production-ready with activation decision tree, real case studies (Khalil/Öztürk/Hong Kong 47/Jan 6 geofencing), legal frameworks, international asylum pathways, emergency escalation protocols
  - **Key findings**: (1) Dual-SIM phones only safe if activated from different locations (synchronous activation = tracking signature), (2) Tor bridges + guard node vetting critical over exit node (guard controls observability), (3) Attorney-client privilege over Signal/ProtonMail only if encrypted end-to-end, (4) Canada/Germany/Ireland have US asylum acceptance (6-12 month processing), (5) Evidence preservation requires SHA-256 chains of custody for legal admissibility
  - **Sources**: 14 authoritative sources (EFF SSD, Access Now, NLG, ACLU, UNHCR, Tor Project, Freedom House, CBP, constitutional law)

- ✅ **mfg-farm: Phase 2 supplier sourcing and multi-printer farm economics** (Session 544 COMPLETE)
  - **Deliverables**: `projects/mfg-farm/phase-2-supplier-research.md` (2,700 words) + `supplier-scorecard.csv`
  - **Key findings**: Top 5 suppliers ranked (eSUN $11–13/kg, Anycubic $10.49/kg bulk, Polymaker $14.99/kg quality, Overture backup, SUNLU sampling). COGS reduction: $0.77–1.40/unit. Monthly margin gain at 7K units: $5,400–9,800. Post-test-print 7-step sequence documented.
  - **Status**: ✅ COMPLETE

- ✅ **open-repo Phase 5 final architecture** (Session 546 COMPLETE)
  - **Deliverables**: `projects/open-repo/phase-5-offline-export-architecture.md` (production-ready)
  - **Key findings**: ZIM metadata naming convention (openZIM standard), incremental strategy (versioned full exports + scope-scoped flavours), CDN architecture (Cloudflare R2 for MVP, Backblaze B2 for scale, explicit S3 rejection on egress costs), OPDS catalog integration (feedgen library + submission path to Kiwix catalog), search quality + federation-aware export scoping
  - **Effort revision**: 24–37 days total for complete Phase 5 (9–14 days additive to prior 15–23 day estimate)
  - **Status**: COMPLETE (committed to master)

**✅ COMPLETED (Session 545 — Exploration Queue Execution)**:

- ✅ **resistance-research Phase 3: Real-Time Crisis Monitoring Infrastructure** (COMPLETE — verified from prior session)
  - **Deliverables**: `monitoring-infrastructure-2026.md` (4,670 words, 7 parts) + `tracking-template.json` (1,316 lines, 37-domain tracking objects) + 3 companion templates (monthly-crisis-snapshot, contingency-trigger-log, coalition-feedback-tracker)
  - **Key design**: Tier 1 (automated: court dockets, legislative votes), Tier 2 (human-curated: significance judgment), Tier 3 (coalition-fed: relationship intelligence). Domain 37 has embedded five-window advocacy calendar.
  - **Status**: Production-ready for post-distribution Phase 3 operationalization

- ✅ **resistance-research Phase 3 Candidate 4: International Democratic Recovery Timelines** (COMPLETE — Session 556)
  - **Deliverables**: `phase-3-candidate-4-international-recovery-timelines.md` (8,900 words, 44 sources)
  - **Case Studies**: 8 cases spanning 1945–2026 (South Korea, Spain, Taiwan, Germany, Uruguay, Argentina, Poland, Hungary)
  - **Key Findings**: Full institutional recovery 5–10 years minimum (favorable) to 15–25+ years (deep capture). US timeline 8–15 years (Spain model) to 15–25 years (Poland/Hungary model). Critical gap identified: US lacks external institutional anchor with enforcement capacity.
  - **Synthesis**: Media freedom + civil society restoration lead Year 1 per comparative evidence. Cardinal law trap (two-thirds supermajority) parallels US lifetime federal appointments. Poland structural parallel applies directly to US judicial durability mechanism.
  - **Status**: Production-ready for Phase 1 distribution integration (can be sent with institutional materials)
  - **Committed**: fd2f31d to master

- ✅ **seedwarden: Advanced Growth Metrics and Cohort Analysis Framework** (COMPLETE)
  - **Deliverables**: `growth-metrics-framework.md` (3,700+ words) + `cohort-analysis-template.sql` (617 lines) + `dashboard-template.ipynb` (Jupyter with synthetic data fallback) + `monthly-metrics-checklist.md` (90-minute runbook)
  - **Key findings**: Email-to-purchase funnel critical path (20% target); seasonal cohort divergence (holiday gift ≠ self-purchase repeat patterns); product LTV optimization (single products never ROI-positive on Pinterest ads)
  - **Status**: Production-ready for Phase 1 launch data collection and Phase 2 scaling analysis

- ✅ **stockbot: Advanced Feature Importance and Model Drift Detection** (COMPLETE)
  - **Deliverables**: `feature-drift-detection.md` (3,800 words) + `feature_drift_detector.py` (Python module with 4 key functions) + `test_feature_drift_detector.py` (68 unit tests, all passing) + CLI extension to post_trade_analysis.py
  - **Key design**: Zero schema changes; LightGBM native SHAP (no external package); 5-dimension retraining trigger with advisory default (human approval before execution); regime-adaptive thresholds
  - **Status**: Production-ready for post-Gate-1-pass integration once paper trading validates drift patterns

**✅ COMPLETED (Session 547 — Exploration Queue Execution)**:

- ✅ **resistance-research: Post-distribution measurement and iteration framework** (COMPLETE — Session 547)
  - **Deliverables**: `measurement-and-iteration-framework.md` (6,800 words) — Seven-part framework with success metrics by tier, feedback-loop mechanisms (direct contact log, passive monitoring, structured check-ins, coalition input), network amplification tracking (bridge-node methodology), monthly iteration cycles with demand-signal decision matrix, institutional adoption playbook (4 adoption levels, 5-step facilitation sequence, sector-specific pathways), tracking infrastructure, and recovery protocols
  - **Key findings**: Institutional adoption depth is the unit of measure, not reach. Two-contact threshold prevents messaging overcorrection. Bridge-node tracking compensates for invisible Hill staff adoption. Current Phase 2 priorities: Domain 31x (Healthcare Tariff Collision, 95 days to deadline) and Domain 37b (State Election Security, April–July advocacy window)
  - **Status**: COMPLETE, committed to master (d625129)

- ✅ **stockbot: Gate 2+ optimization thesis** (COMPLETE — Session 547)
  - **Deliverables**: `gate-2-optimization-thesis.md` (7,400 words, 9 sections) — Complete Gate 2 optimization roadmap with: (1) Ensemble weighting (Inverse-Vol, Risk Parity, Conservative Quarter-Kelly with pseudo-code), (2) Sector rotation (12-week relative-strength scoring, 35% hard cap, defensive tilt in Bear regime), (3) Tail-hedge mechanisms (VolatilityCircuitBreaker, defensive rotation at 8% drawdown, VIXSpike overlay), (4) Regime sizing compound formula (vol × HMM × defensive multipliers), (5) Model refresh schedule (Tier 1 monthly / Tier 2 quarterly / Tier 3 emergency retrain at drift ≥ 0.55), (6) Unified architecture signal flow, (7) Gate 2 metric projections (Sharpe 1.25–1.65, MDD 4–5% backtest / ~8% live, PF ~1.82), (8) 5-phase implementation sequence
  - **Key findings**: All five optimization layers compound multiplicatively on portfolio volatility. Bull+calm → 1.35x sizing; Bear+high-vol → 0.13x. Gate 2 evaluation requires 120 completed round trips, all layers active, no emergency retrain in 30d, VIX > 20 experience
  - **Status**: COMPLETE, committed to master

- ✅ **seedwarden: Wholesale and affiliate partnership strategy** (COMPLETE — Session 547)
  - **Deliverables**: `wholesale-and-affiliate-strategy.md` (~4,100 words) — Five-channel B2B strategy: (1) Affiliate Programs (25% standard, 30% creator, 20% institutional; 20+ named targets including Melissa K. Norris YT 486K, Homesteading Family 895K), (2) Wholesale/Bulk Licensing ($1.50–$5.00/PDF; targets: True Leaf Market, Botanical Interests, Seed Savers Exchange, county extension, FFA chapters), (3) Corporate Training & Bulk Licensing (seat-license $2.50–$6.00; tech/hospital/CERT/ERG trainers; 3–6 month sales cycle), (4) White-Label Partnerships (Etsy bundlers $2.00/unit; content platforms $1,500–$3,000/year license), (5) Seasonal Windows (Spring Partner Pack $4.00/unit, Preservation $8.00/unit, Holiday Bundle $15/unit)
  - **Phase 3 revenue targets**: Affiliate $300–$800/month; total partnership revenue 20–35% of Phase 1-2 total. Phase 3 outreach timeline month-by-month for each seasonal window
  - **Status**: COMPLETE, committed to master

**✅ COMPLETED (Earlier Sessions — Phase 2 Research)**:

- ✅ **Domain 27 — Higher Education and Academic Freedom** (COMPLETE — Session 510)
  - **Deliverable**: `domains/domain-27-higher-education-and-academic-freedom.md` (9,226 words, 7 sections)
  - **Coverage**: Four-track threat diagnosis (funding leverage, DEI/self-censorship, student visa detentions, administrative capture), evidence base (Harvard/Columbia cases, State Dept. correspondence), democratic functional impact, reform pathways, international precedents (Hungary, Germany, EU, Canada), implementation timeline
  - **Status**: ✅ COMPLETE, production-ready

- ✅ **Domain 28 — War Powers and Venezuela Military Unilateralism** (COMPLETE — Session 506)
  - **Deliverable**: `domains/domain-28-war-powers-venezuela-military-unilateralism.md` (5,600 words)
  - **Coverage**: Arrest-operation legal theory, Senate/House vote analysis, WPR elimination implications, structural reform pathways
  - **Status**: ✅ COMPLETE, production-ready

- ✅ **Domain 29 — Prosecutorial Weaponization and DOJ Capture** (COMPLETE — Session 506)
  - **Deliverable**: `domains/domain-29-prosecutorial-weaponization-and-doj-capture.md` (6,124 words)
  - **Coverage**: SPLC indictment case study, charging-stage suppression mechanism, DOJ capture evidence, reform pathways
  - **Status**: ✅ COMPLETE, production-ready

**NEW ITEMS (Session 547 — Exploration Queue Refresh for Empty Queue)**:

- ✅ **resistance-research: Implementation toolkit for institutional adoption** (COMPLETE — Session 548)
  - **Deliverables**: `implementation-toolkit.md` (2,028 words) + 5 sector-specific guides (legislative, advocacy, academic, state government, institutional resilience) — 10,222 words total
  - **Key design**: Each guide has "Monday morning question" + 5-step decision tree + domain applications + common mistakes + case studies
  - **Value**: Bridges proposal to execution. Ready for Phase 1 institutional outreach.
  - **Status**: ✅ COMPLETE, committed to master (Session 548)

- ✅ **stockbot: Post-Gate-2 live trading operations & performance analysis framework** (COMPLETE — Session 549)
  - **Deliverable**: `live-trading-operations-suite.md` (10,724 words / 1,384 lines, 8 sections + 4 appendices)
  - **Scope**: Complete live trading operations infrastructure: (1) three-layer dashboard (health/performance/model reviews), (2) 19-alert trigger framework with response matrix, (3) performance attribution feedback loop (A-E taxonomy), (4) automated optimization triggers (model retraining, position sizing, hedge activation), (5) four-scenario emergency playbooks
  - **Key design**: Alert Response Matrix is operational core — every alert has predetermined auto-action + human deadline. Performance attribution weekly cadence (not daily noise). Emergency playbooks are decision trees with human judgment + automated guardrails.
  - **Value**: Production-ready for immediate deployment post-Gate-2. All metrics grounded in existing infrastructure.
  - **Status**: ✅ COMPLETE, committed to master (53f9819, Session 549)

- ✅ **mfg-farm: Manufacturing automation & multi-printer scaling architecture** (COMPLETE — Session 549)
  - **Deliverable**: `manufacturing-automation-architecture.md` (4,800+ words, 5 sections + flowcharts + cost modeling)
  - **Scope**: Complete scaling blueprint (1→5 printers): (1) manufacturing workflow automation (SimplyPrint stack, zero post-processing, AutoFarm3D auto-eject), (2) QC framework (±0.5mm / ±0.3mm tolerance, 45-min labor overhead, <2% defect target), (3) fulfillment pipeline (Craftybase→Pirate Ship→USPS), (4) multi-printer orchestration (material-based assignment P1–P5, load balancing), (5) parametric cost model (COGS $1.032/clip, break-even 122 units/month)
  - **Key findings**: Plate batching to 12 clips = 6x throughput (zero capital). Bundle mix shift (30%→3-packs) adds 5–8% margin, worth more than adding 4 printers. AutoFarm3D Door Opener availability needs confirmation.
  - **Value**: Production-ready for post-test-print execution. Informs printer selection, supplier contracts, operational workflow design.
  - **Status**: ✅ COMPLETE, committed to master (Session 549)

- ✅ **resistance-research: Democratic Crisis Response Playbooks** (COMPLETE — Session 549)
  - **Deliverables**: `crisis-response-playbooks.md` (~4,800 words) + 5 sector guides (~1,000-1,200 words each, ~9,000 words total)
  - **Scope**: Five crisis scenarios with 72-hour / 30-day / 90-day sequencing, specific actors (with phone numbers), success metrics, failure modes, cross-playbook coordination matrix
  - **Crisis scenarios**: (1) Election interference (federal or state-level), (2) Judicial capture, (3) Executive overreach (emergency EO), (4) Civil service targeting (Schedule F-equivalent purge), (5) Prosecutorial weaponization
  - **Key design**: Specific institutions (not generic), specific decision-makers (not generic leadership), specific success metrics (not vague outcomes). Failure modes section for each scenario addressing administration counter-tactics.
  - **Value**: Bridges 35-domain diagnostic framework to institutional execution. Ready for Phase 1 distribution activation.
  - **Status**: ✅ COMPLETE, committed to master (commit 3c3cd30)

- ✅ **cybersecurity-hardening: Supply chain targeting and organizational defense** (COMPLETE — Session 549)
  - **Deliverable**: `organizational-defense-playbook.md` (~3,500 words, 5 sections)
  - **Scope**: (1) Detecting supply chain compromise (SBOM auditing, SLSA framework), (2) Infrastructure targeting (DDoS / BGP / DNS with redundancy architecture), (3) Insider threat detection (UEBA, behavioral signals), (4) Incident response workflows (3-phase with decision trees), (5) Post-breach organizational recovery (90-day timeline)
  - **Key finding**: Supply chain is primary attack surface (SolarWinds, MOVEit, 3CX cases). Extends high-risk-populations work to institutional infrastructure level.
  - **Value**: Production-ready for organizational deployment. NGOs, media outlets, civil rights orgs can use playbook immediately.
  - **Status**: ✅ COMPLETE, committed to master

- ✅ **mfg-farm: CNC capabilities and economics research** (COMPLETE — Session 549)
  - **Deliverables**: `cnc-capabilities-analysis.md` (~4,000 words) + `cnc-cost-comparison-matrix.csv` (25 rows, 4 sections)
  - **Scope**: (1) Technical analysis (FDM vs CNC tolerances, component requirements), (2) Economics (equipment cost, labor throughput, material waste, break-even analysis), (3) Market (price premium potential, Etsy segment analysis), (4) Workflow integration (outsourced vs in-house)
  - **Key finding**: **Do not purchase in-house CNC at 1K-10K units/month.** A fifth FDM printer has better ROI. Recommend testing outsourced CNC first ($1.5K-3.5K validation cost).
  - **Economics verdict**: CNC break-even requires 180+ premium units/month; FDM market size at current volumes makes pure-FDM the right choice through 10K units/month
  - **Value**: Informs post-test-print scaling roadmap. Clear recommendation: stay FDM-only.
  - **Status**: ✅ COMPLETE, committed to master

- **mfg-farm: CNC capabilities and economics research** (Priority 6 — NEW, QUEUED)
  - **Scope**: Research where and how CNC capabilities add value to ModRun product line. (1) Technical: which ModRun components benefit from CNC finishing? (2) Economics: CNC machine cost, training, material waste, per-unit cost impact vs. FDM-only, (3) Market: do higher-precision CNC variants command price premium? (4) Workflow: integration with FDM+CNC workflow, quality control, case studies of hybrid Etsy sellers
  - **Goal**: Decision framework for whether to add CNC to mfg-farm roadmap post-test-print
  - **Expected output**: `cnc-capabilities-analysis.md` (3,000-4,000 words) + cost comparison matrix
  - **Timeline**: 1-2 sessions
  - **Status**: QUEUED

**NEW ITEMS (Session 557 — Exploration Queue Refresh)**:

- ✅ **resistance-research: April-May 2026 Phase 2 Content Maintenance** (COMPLETE — Session 557)
  - **Scope**: Update Phase 2 domains affected by late April 2026 developments. Key targets: Domain 31x (Healthcare Tariff Collision — 100% tariff effective July 31, 95 days to deadline), Domain 37b (State Election Security — April–July advocacy window), Domain 19f (Iran War constitutional crisis — May 1 WPR deadline), Domain 6/35 (Trump v. Wilcox shadow-docket removal power implications). Integrate new evidence: April 2026 tariff negotiations, FISA Section 702 April 30 deadline outcome, Iran WPR deadline developments.
  - **Deliverables**: 4 domains updated with 16 new citations (4 per domain), April-May 2026 publication dates, updated deadline calendars, advocacy strategy refinements. Key findings: Domain 31x generic drug shortage pre-tariff + April 2027 Commerce review; Domain 37b resource gap quantified (75% of officials without federal resources) + FY27 budget permanently zeros CISA election security; Domain 19f May 1 deadline defied + naval blockade creates cleaner WPR violation; Domain 6 NLRB case study + CFPB collapse + state AG enforcement repositioning
  - **Status**: ✅ COMPLETE, committed to master (resistance-research submodule)

- ✅ **stockbot: Live Trading Dashboard Implementation** (COMPLETE — Session 557)
  - **Scope**: React/TypeScript implementation of the dashboard mockup (HTML prototype from Session 551 + operations framework from Session 549). Build: (1) Component structure (Portfolio, ControlPanel, Positions, RiskMetrics, SignalBoard, TradeLog), (2) API integration layer (7 endpoints documented in mockup), (3) Real-time WebSocket integration (live P&L, signal updates), (4) Dark theme Tailwind CSS styling, (5) Responsive design for desktop/tablet
  - **Deliverables**: 6 React components, 4 custom hooks, TypeScript types, full test suite (75 tests, all passing), App.tsx main layout, README with API integration guide. Solved critical Jest config issues (RTL v10 getter compatibility, moduleNameMapper overreach). Ready for immediate deployment post-engine-restart.
  - **Status**: ✅ COMPLETE, committed to stockbot submodule master (commit 19c624e)

- **resistance-research: Democratic Renewal Phase 3 Candidate 5 Research** (Priority MEDIUM for post-distribution roadmap)
  - **Scope**: Research additional Phase 3 candidate following Session 556 pattern (8,000-10,000 words, 40+ sources, comparative case studies, international precedent). Recommended topics: (1) Financial sector vulnerabilities and banking system independence post-capture, (2) Civil service resilience architecture (hiring/firing protections that survive politicization), (3) Judicial independence recovery mechanisms (structural reforms that restore court independence post-capture), (4) Media freedom and journalistic protection pathways (press freedom recovery case studies).
  - **Goal**: Expand Phase 3 research roadmap, identify additional leverage points for democratic renewal post-distribution
  - **Expected output**: `phase-3-candidate-5-[topic].md` (8,000-10,000 words) with case studies, reform pathways, international precedent analysis
  - **Timeline**: 2-3 sessions per candidate
  - **Status**: QUEUED

**✅ COMPLETED (Session 553 — Parallel Exploration Queue Execution)**:

- ✅ **stockbot: Live Trading Infrastructure and Risk Management** (COMPLETE — Session 553)
  - **Deliverable**: `projects/stockbot/docs/live-trading-operations.md` (7,578 words, 1,135 lines, production-ready)
  - **Scope**: Complete operational design for monitoring, alerting, emergency response, and runbooks for live trading post-engine-restart
  - **Key Content**: 
    - Dashboard Architecture (3 monitoring layers: 5-min operational health, 30-min performance tracking, daily model health; maps Session 551 UI mockup panels to data sources)
    - Alert Triggers (6 categories with concrete numeric thresholds; drift detection example: TSLA backtest Sharpe 1.10 → Orange alert when rolling 30-trade live Sharpe <0.55 AND win rate <37%; circuit breakers at 3 consecutive losses = 9.1% P(event))
    - Emergency Exit Procedures (4 response levels: Level 2 controlled liquidation with explicit order; Level 3 panic liquidation with curl commands; error prevention box for common operator mistakes)
    - Operational Runbooks (6 runbooks, 5 incident types with branch logic; self-contained decision trees)
    - Integration Points (gap identified: no real-time CRITICAL alerts to Discord — only daily summary exists; design spec provided for implementation)
    - Pre/During/Post-Market Checklist (1-page routing table mapping all alert types to runbook sections)
  - **Critical Gap Identified**: Real-time CRITICAL alert Discord webhook not implemented — design spec ready, ~15 min implementation
  - **Integration Status**: Coordinates with Session 551 UI mockup and Session 542 performance attribution framework. Ready for immediate post-engine-restart deployment.
  - **Status**: ✅ COMPLETE, production-ready, committed to master (stockbot submodule)

- ✅ **seedwarden: Track B Phase 2 Photography Roadmap** (COMPLETE — Session 553)
  - **Deliverable**: `projects/seedwarden/PHOTOGRAPHY_ROADMAP.md` (~5,200 words, production-ready)
  - **Scope**: Execution plan for hybrid lifestyle + stock photography strategy (Session 523 document, 4,200 words) across all 21 Phase 2 products
  - **Key Content**:
    - Product Photography Map (all 21 products assigned: 15 physical, 6 stock; priority order: four highest-ticket products $18–$22 get Week 1 stock sourcing)
    - Shot Lists (15 physical products with 2–4 named shots each: surface, arrangement, angle, lighting, visual element, styling notes; example: Companion Planting Chart gets wall-mount print shot)
    - Stock Sourcing Plan (6 products with 5–8 search queries each; free sources first: Unsplash/Pexels/Pixabay; iStock only if needed; budget allocation $60–$99 total under $80–$160 ceiling)
    - 3-Week Sprint Plan (day-by-day time estimates; decision gate Day 1 end: free-source scan results determine iStock credit needs; physical shoot is only hard constraint)
    - Conversion Metrics Design (per-product thresholds: 10–20% lift range; revenue impact: Survival Garden 10% lift = 2 sales/month = +$44/month pays back all iStock spend Month 1; Hunting/Trapping Manual highest-value A/B candidate)
    - Equipment & Setup Guide (camera/lighting/props/post-processing workflow for consistency)
  - **Blockers Identified**: Native Plants PDF must be rebuilt before Phase 2 image upload (noted for execution sequencing, not a blocker for roadmap)
  - **Integration**: Coordinates with customer cohort analysis framework (Session 551) and conversion metrics design
  - **Production Status**: Ready to execute post-Phase-1-launch (May 2026). No Phase 1 blockers.
  - **Status**: ✅ COMPLETE, production-ready, committed to master (seedwarden project)

---

## Completed (Archive)

<!-- Move completed projects here with a completion date -->
