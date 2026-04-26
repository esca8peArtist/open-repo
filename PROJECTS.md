# Active Projects

> This is the single source of truth for autonomous orchestration.
> The orchestrator reads this file at the start of every session.
> Update priorities, status, and current focus as work progresses.
>
> **Last updated by**: orchestrator on 2026-04-25 (INBOX processing)

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
**Current focus**: Session 291: **Business plan COMPLETE** (`business-plan.md`). **CadQuery parametric designs COMPLETE** (`cadquery/modrun_rail.py`, `cadquery/modrun_clip.py`). Market research + competitive analysis were already complete (`market-research.md`). Etsy and Amazon listing copy already complete (`etsy-listing-modrun.md`). **Lead product: ModRun cable management system** — original design, Etsy-compliant, 65–72% net margins. **BLOCKING GATE: test print required.** User needs to: (1) run `pip install cadquery` in mfg-farm env or system Python, (2) run `python modrun_clip.py --output-dir ./stl/` and `python modrun_rail.py --output-dir ./stl/` to generate STL files, (3) test print and tune tolerance parameters, (4) photograph finished set, (5) list on Etsy. All copy, pricing, tags, photo brief are ready in `etsy-listing-modrun.md`.
**Blocked on**: Test print (user action required — see focus above)
**Notes**: Automation is the core constraint — products and workflows must be designed for minimal human touchpoints per unit. Physical products mean real fulfillment costs (packaging, shipping, storage) — factor these in from the start. Etsy and Amazon have different fee structures and audiences; may want both. Scaling from 1→N printers requires thinking about file management, queue management, quality control, and packaging throughput — not just the printers themselves.

---

### resistance-research
**Goal**: Identify solutions to a failing democracy — if the current government could be replaced and rebuilt from a clean slate, what would it look like? How could it be structured to ensure justice, life, liberty, and the pursuit of happiness for all citizens? How could it be objectively efficient, equitable, and functional? This project addresses the full scope of government: voting systems, taxation, education, infrastructure, healthcare, law enforcement, housing, and everything in between. The government exists to serve its citizens — so how do we actually achieve that? A secondary goal is tracking and understanding the specific crises the United States is currently facing, finding actionable responses, and building a comprehensive integrated proposal for democratic renewal.
**Priority**: High
**Status**: Active — **PHASE 1 PRE-LAUNCH VALIDATION COMPLETE** (Session 462), launch Monday 2026-04-28 21:00 UTC, all systems GO
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: Session 462 (2026-04-26): **PRE-LAUNCH VALIDATION COMPLETE**. Comprehensive validation passed (commit 8ffb45f): (1) GitHub Gist verified publicly accessible and correct (May Day Action Guide), (2) PHASE1_LAUNCH_CHECKLIST.md verified complete with 7-section operational plan, (3) All 3 monitoring templates tested end-to-end with mock data and field-ready, (4) UTC/EDT mapping verified across all 6 Phase 1 deadlines (April 28 21:00 UTC = 5 PM EDT, April 29 23:30 UTC = 7:30 PM EDT, etc.), (5) `MONDAY_LAUNCH_READINESS.md` created documenting Gist status, template verification, timezone mapping, fallback procedures (Gist source file at mayday-2026-action-guide.md, re-publishable in <3 min), and monitoring checklist. Non-blocking open items: optional distribution channels (Discord, Slack, Signal, email, Twitter/X) can be confirmed in hours before 21:00 UTC launch; CourtListener is viable substitute if PACER account unavailable. **Status**: Production-ready. Launch Monday 21:00 UTC confirmed.
**Blocked on**: —
**Notes**: Phase 1 (monitoring) and Phase 2 (litigation tracking) both COMPLETE and production-ready. All templates field-ready. Gist is confirmed working distribution channel. Optional channels can be added pre-launch. High confidence across monitoring framework, templates, timeline, and data capture flow. Launch readiness VERIFIED Saturday evening.

---

### cybersecurity-hardening
**Goal**: Build a comprehensive, actionable guide to protecting communications and identity against government-level mass surveillance. Understand what Palantir and similar data brokers/intelligence platforms actually have access to — what data they ingest, how they link identities, and what their current government contracts cover. From that threat model, identify the best practical techniques for private and anonymous communication: encrypted messaging, metadata minimization, network anonymization (Tor/VPN tradeoffs), device hardening, operational security (OpSec), and identity compartmentalization. The output should be a personal OpSec playbook grounded in real threat modeling — not theoretical, but calibrated to the actual capabilities of the adversary.
**Priority**: High
**Status**: Active — **TIER 1 DISTRIBUTION PREP COMPLETE** (Session 465), ready for user execution
**Visibility**: Public — GitHub Gist (public) + private distribution to immigration legal aid organizations
**Working dir**: `projects/cybersecurity-hardening/`
**Current focus**: Session 465 (2026-04-26): **TIER 1 DISTRIBUTION PREP COMPLETE**. Agent-created TIER1_DISTRIBUTION_PREP.md (358 lines) consolidates all distribution materials: 8 Tier 1 organizations (5 legal aid + 3 community org networks), 3 email templates (legal aid, community orgs, mutual aid networks), 5-step execution process, pre-send checklist, FAQ, success metrics, and quarterly review schedule. All templates include Gist URL and are ready for personalization. TIER1_DISTRIBUTION_PREP.md committed to master. **Next**: User reviews and approves templates → execute Tier 1 outreach → track responses → Tier 2 (digital rights, security researchers, journalists) → Tier 3 (policy, academic, labor).
**Blocked on**: —
**Notes**: All distribution materials production-ready. Trilogy (Gist) published and accessible. TIER1_DISTRIBUTION_PREP.md provides step-by-step execution guide with email templates, contact list, tracking templates, and quarterly review schedule. User can begin Tier 1 outreach immediately after approval.

---

### stockbot
**Goal**: Build a full-stack model building and automated trading platform with both a web app and iOS app integration. The platform should allow creation, backtesting, and optimization of trading models across multiple model types (stock, options, rule-based, ensemble, multi-timeframe). The end goal is fully automated live trading — but only after models are rigorously vetted and confidence is established through paper trading. Model training and optimization costs must stay under $20/month. Once a model is sufficiently validated through paper trading performance, it graduates to live trading. Profit maximization is the north star, but capital preservation and risk management are non-negotiable constraints.
**Priority**: High
**Status**: Active — **MONDAY MARKET OPEN READINESS VERIFIED** (Session 439), all systems green, P&L pipeline confirmed, zero blockers
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**Current focus**: Session 439 (2026-04-26): **MONDAY READINESS VERIFICATION COMPLETE**. Paper trading session `33a4afe676cae12a` (AAPL_h10_lgbm_ho stacker) LIVE and healthy. P&L data pipeline verified: trades/performance_metrics/model_runs tables correct, database baseline clean (0 trades in stockbot.db), equity curve algorithm validated. Jetson sync confirmed (all code files match dev exactly, 5 sessions cycling correctly, market_open flags false). **22/22 Monday readiness tests PASS**. Dashboard API ready to capture P&L beginning 2026-04-28 14:30 UTC market open. `MONDAY_READINESS.md` created with monitoring commands and fallback procedures. **Status**: Ready for live P&L capture Monday. No rebuild/restart needed. Paper trading will auto-cycle and capture trades/P&L for the week.
**Blocked on**: —
**Notes**: Monday market open at ~14:30 UTC on 2026-04-28. System is production-ready. P&L data will flow automatically. Next phase: monitor live P&L accumulation week-by-week, evaluate stacker performance against baseline metrics, prepare for escalation to live trading once paper trading demonstrates stable positive returns.

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
**Status**: Active — **UPLOAD VALIDATION COMPLETE** (Session 462), 3 tag corrections required before Monday upload
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/seedwarden/`
**Current focus**: Session 462 (2026-04-26): **PHASE 1 UPLOAD VALIDATION COMPLETE**. All assets verified production-ready: PDFs (682–754 KB), mockups (2400×2400 px PNG, 342–389 KB all compliant), titles/descriptions (3-point compliance check passed), keywords (properly front-loaded). `UPLOAD_READY_CHECKLIST.md` created documenting: ✓ all 6 PDFs present, ✓ all 21 mockups 2400×2400 px PNG (342–389 KB), ✓ titles/descriptions Etsy-compliant, ✓ previously corrected tag sets validated. **3 CRITICAL TAG CORRECTIONS REQUIRED** (documented in UPLOAD_READY_CHECKLIST.md Section 4): (1) **Companion Planting Chart** (critical—listing #1, Monday upload): No corrected tag set exists; original has 10 of 12 tags >20 chars; full replacement set of 13 compliant tags in checklist, (2) **Survival Garden Regional Plans**: "self sufficient garden" is 22 chars → replace with "self-sufficient" (15 chars), (3) **Zone-by-Zone Seed Starting Calendar**: "veggie planting guide" is 21 chars → replace with "veggie plant guide" (18 chars). **Visual flag**: Zone calendar mockup shows "$18 (Complete Bundle)" but individual listing priced $8 — verify before using this mockup. **3 MANUAL ACTIONS REQUIRED**: (1) Apply tag corrections from checklist before upload, (2) Verify Etsy seller account active + Etsy Payments connected, (3) Pre-schedule Day 3 social media announcement. **Status**: Ready for Monday upload after tag corrections (1.5–2 hrs estimated upload time across 3 days).
**Blocked on**: Manual user actions (tag corrections, Etsy account verification, social media pre-scheduling)
**Notes**: All product assets production-ready. Tag corrections are straightforward copy-paste operations with exact replacement sets provided. The zone-calendar mockup price badge discrepancy is a documentation issue, not a product issue — verify the badge matches the individual listing price. Phase 1 launch unblocked pending 3 manual actions. Phase 2-4 enhancements (phone mockups, lifestyle photography, printed page mockups) optional based on Phase 1 conversion data.

---

### open-repo
**Goal**: An open-source library for all things under the sun — a distributed, free, one-stop shop to find and share information that benefits all of humanity. Link to Wikipedia for general information, schematics, building plans, 3D models, recipes/instructions, services to share, and more. The core principle: no single person or organization controls any of it. Everything is distributed and open source. This is about leveling the playing field — giving all people the best chance to not only survive but thrive.
**Priority**: Medium
**Status**: Active — Phase 3 COMPLETE, **Phase 4 COMPLETE (Phases 1–4 all implemented)**, **194 TESTS PASSING (verified 2026-04-26)**, **BLOCKED on GitHub push (SSH permission issue)**
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-repo/`
**Current focus**: Session 465 (2026-04-26): **WAVE 4 PRODUCTION-READY BUT GITHUB PUSH BLOCKED**. Branch `feature/wave4-phase2-federation-service` (commits `fd2bf0d` Phase 1, `128994f` Phase 2, `557d5eb` Phase 3) verified complete and tested: **194/198 tests passing** (4 skipped), 0 failures. All Wave 4 federation infrastructure production-ready (partner registration, service layer, admin routes, HTTP signature verification, request signing, conflict detection). **BLOCKER**: SSH key (esca8peArtist) lacks write access to SuperClaude-Org/SuperClaude_Framework repository. Push fails with "permission denied". Branch code is ready; requires GitHub permission fix before push can succeed. **Next**: User either (1) adds esca8peArtist to SuperClaude-Org with push access, OR (2) configures alternate SSH key with access. Then push feature branch and merge. Optional Phase 5 (offline export/Kiwix) can follow.
**Blocked on**: **GitHub SSH permissions** (SuperClaude-Org write access for esca8peArtist)
**Notes**: All code, tests, and federation infrastructure COMPLETE and verified working. GitHub push is purely a permission/SSH configuration issue — once resolved, code can be pushed immediately. Phase 5 optional.

---

### off-grid-living
**Goal**: A comprehensive plan for off-grid, sustainable living. Define full plans for construction, implementation, operation, maintenance, and repair. Cover the complete operational architecture: food production, shelter, medicine, electricity generation, food preparation and storage, water, and general survival necessities. Include disaster scenarios up to and including nuclear disaster. Also cover community building, organization, and mutual support.
**Priority**: Medium
**Status**: Active — quality review COMPLETE, awaiting publication decision
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/off-grid-living/`
**Current focus**: Session 425: **Quality Review COMPLETE** (8.5/10 quality score). All 16 domain files (1,310 KB total) verified: zero TODOs, all acronyms defined, consistent formatting, accurate cross-references. **5 issues found and fixed** (commit `de5ccb3`): (1) 08-medical-health.md YAML front matter missing cross-refs field (added), (2) 14-finances-trade.md YAML header completely missing (added + standardized heading format), (3) 07-heating-cooling.md cross-ref `02-shelter-construction` → `11-shelter-construction`, (4) 10-tools-fabrication.md two cross-ref fixes (front matter + body), (5) 12-communications.md cross-ref `13-community-governance` → `13-community-organization`. All cross-references now valid. Project is now publication-ready. **Next**: User decision to publish or hold pending further additions.
**Blocked on**: —
**Notes**: This is a planning and research project, not a software build. Practical and actionable plans over theory. Include real costs, sourcing, and skill requirements where possible. Nuclear disaster scenario is in scope — treat it seriously.

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

- **off-grid-living: nuclear and radiological preparedness** — the goal explicitly includes nuclear disaster scenarios. Current content is thin here. Research: fallout shelter construction standards, potassium iodide protocols, contamination detection, decontamination procedures, long-term food/water storage under fallout conditions, and community triage. Write to `projects/off-grid-living/` as a new domain file.

- ~~**Stockbot: model evaluation framework**~~ — **Done** (Session 484: `model-graduation-criteria.md` complete — four-gate framework for paper-to-live graduation: statistical sufficiency, performance quality, robustness validation, operational readiness)

- ~~**resistance-research: post-launch Phase 2 prep**~~ — **Done** (Phase 2 litigation tracking COMPLETE and production-ready per Session 462)

---

## Completed (Archive)

<!-- Move completed projects here with a completion date -->
