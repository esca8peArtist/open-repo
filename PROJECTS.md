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
- **Sonnet token limit: 8,935,000**  ← calibrated 2026-04-26 (UI showed 22%)
- **All models token limit: 15,114,000**  ← calibrated 2026-04-26 (UI showed 14%)

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
**Status**: Active — May Day guide PUBLISHED, live monitoring phase begins 2026-04-28
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: Session 420: **Monitoring templates verified and complete**. April 28 Xinis hearing (`2026-04-28-results.md`, quick-fill table + April 29 analysis template). April 29 contingency brief created (`2026-04-29-contingency.md`, covers Nashville/Crenshaw ruling, 4th Circuit stay post-contempt, Section 702 field). May 1 monitoring template verified (`2026-05-01-template.md`, scale summary + 7-city incident tracking + ICE enforcement table + Section 702 expiration field). **Monday readiness: CLEAN**. Section 702 expires April 30 — strategically positioned in templates to track surveillance constraint impact on May 1. April 28 hearing close ~5pm EST → quick-fill 10 min → April 29 analysis overnight → May 1 live at ~6am. **User action**: Distribute May Day guide Gist URL (https://gist.github.com/esca8peArtist/2c5ba783bd06405749b7c3decebaa6d4) to organizing channels (Slack, Signal, Mastodon) as legal/analytical companion to coalition guides (Indivisible, NEA, DSA).
**Blocked on**: —
**Notes**: Monitoring infrastructure ready. Democratic renewal proposal (22 domains) and Phase 2 litigation tracking remain. All templates ready for live data capture Monday.

---

### cybersecurity-hardening
**Goal**: Build a comprehensive, actionable guide to protecting communications and identity against government-level mass surveillance. Understand what Palantir and similar data brokers/intelligence platforms actually have access to — what data they ingest, how they link identities, and what their current government contracts cover. From that threat model, identify the best practical techniques for private and anonymous communication: encrypted messaging, metadata minimization, network anonymization (Tor/VPN tradeoffs), device hardening, operational security (OpSec), and identity compartmentalization. The output should be a personal OpSec playbook grounded in real threat modeling — not theoretical, but calibrated to the actual capabilities of the adversary.
**Priority**: High
**Status**: Active — Phase 2 OSINT deepening COMPLETE, ready to integrate or publish
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/cybersecurity-hardening/`
**Current focus**: Session 420: **Phase 2 OSINT/Data Broker Deepening COMPLETE** — `phase2-osint-deepening.md` (new, ~2,400 words). **Part A** (Broker taxonomy expansion): Identified "no opt-out path" brokers (Venntel, Babel Street Locate X, Thomson Reuters CLEAR, Clearview), Tier B priority additions (CoreLogic, Verisk — feed into law enforcement ID resolution), Tier C batch (PrivateEye, Clustrmaps, Nuwber, USPhoneBook, Spy Dialer, NumLooker, others). **Part B** (ID-restricted services): Identified critical invisible path — California AB 60/AB 1766 IDs enable DROP eligibility for undocumented residents (highest-leverage opt-out path for most at-risk population, currently undocumented in guides). ITIN as SSN substitute plausible but unconfirmed. Proxy opt-out via advocacy orgs emerging but no national infrastructure. **Part C** (Court challenges): Clearview BIPA settlement ($51.75M) template, but explicitly excludes federal agencies (ICE retains $9.2M contract). Illinois BIPA private right of action most powerful lever. PADFAA (Feb 2026 FTC warning letters) emerging regulatory hook for brokers selling to foreign adversaries + domestic law enforcement. SECURE Data Act (HR 8413, introduced April 22) is threat — would preempt CCPA, DROP, CA AG enforcement. **Ready to integrate into Part 0**: (1) Add AB 60/AB 1766 note to Step 0.1 (DROP eligibility), (2) Add "no opt-out available" table to Part 0 framing, (3) Add CoreLogic + Verisk to Step 0.2 batch table, (4) Add 8-10 Tier C brokers, (5) Add SECURE Data Act policy-monitoring item. **Status**: Publication prep ready. Phase 2 deepening complete. Awaits decision: integrate and re-publish, or publish as-is. Commit: `69e073d` (from session 417).
**Blocked on**: —
**Notes**: Trilogy ready for publication. OSINT deepening identifies highest-leverage path (California AB 60/1766 → DROP for undocumented residents). All deepening research verified for 2026 currency. Fold into Part 0 or publish standalone. Recommend fold + republish for maximum Tier 1 reader coverage.

---

### stockbot
**Goal**: Build a full-stack model building and automated trading platform with both a web app and iOS app integration. The platform should allow creation, backtesting, and optimization of trading models across multiple model types (stock, options, rule-based, ensemble, multi-timeframe). The end goal is fully automated live trading — but only after models are rigorously vetted and confidence is established through paper trading. Model training and optimization costs must stay under $20/month. Once a model is sufficiently validated through paper trading performance, it graduates to live trading. Profit maximization is the north star, but capital preservation and risk management are non-negotiable constraints.
**Priority**: High
**Status**: Active — paper trading LIVE, Jetson deployment doc ready, Docker rebuild needed
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**Current focus**: Session 420: **Paper trading VERIFIED LIVE on dev machine (raspby1)**. Session `33a4afe676cae12a` (AAPL_h10_lgbm_ho stacker `0676c84e`) started 2026-04-26T05:50:34Z, cycling every ~60 seconds. `dashboard_api.py` running (PID 162260). Live signal generation begins Monday 2026-04-28 at market open (~14:30 UTC). **CRITICAL JETSON GAP**: Container image is stale — no stacker code from session 417. Jetson has pkl files + registry but cannot load them. Model_runs table empty (0 rows). **New file created**: `JETSON_DEPLOYMENT.md` (8.1 KB) documents connection details (Tailscale SSH works), gap analysis, pre-deployment checklist, rsync + docker rebuild + session-start steps, verification commands, rollback procedure. **Next action**: rsync session-417 source, rebuild Docker image on Jetson, restart container, start paper trading session via API. All steps documented. **PRIORITY 1 (done)**: Paper trading live on dev ✅ **PRIORITY 2**: Monitor live P&L Monday-Friday. **PRIORITY 3 (ready)**: Execute Jetson deployment (rsync + rebuild + session start). Test suite: 849 passed, 30 pre-existing failures (not blocking).
**Blocked on**: —
**Notes**: Web app ready. Model machinery complete and wired. Paper trading is live and accumulating on dev. Jetson deployment doc complete — awaiting execution (should not block Monday market open since dev machine will capture paper trading data). iOS app out of scope until paper trading is solid.

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
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/seedwarden/`
**Current focus**: Session 103: **21 products, all PDFs generated, all listing copy complete.** Added Zone-by-Zone Seed Starting Calendar (1,635 lines, 82pp PDF, $7–$18) to product catalog — was missing from PDF generator and audit. Apartment Growing Complete Guide PDF now generated (146pp). Southwest region in Native Plants guide expanded (was 19 entries, target 30+; agent running). **Biggest blocker**: PDF mockup images needed for all listings — #1 conversion factor on Etsy, requires Canva or mockup generator. All content is ready; launch is blocked only on mockup images.
**Blocked on**: —
**Notes**: Etsy store exists with some products started but not yet quality to sell. Social media has plans but nothing executed. Need to fix quality before promoting. Plant images: all 120 native-plants images already downloaded and cached (verified Session 74) — "0/18" note in prior session was stale.

---

### open-repo
**Goal**: An open-source library for all things under the sun — a distributed, free, one-stop shop to find and share information that benefits all of humanity. Link to Wikipedia for general information, schematics, building plans, 3D models, recipes/instructions, services to share, and more. The core principle: no single person or organization controls any of it. Everything is distributed and open source. This is about leveling the playing field — giving all people the best chance to not only survive but thrive.
**Priority**: Medium
**Status**: Active — Phase 3 data layer COMPLETE, ready for Phase 3 routes
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-repo/`
**Current focus**: Session 416: **Phase 3 Data Layer COMPLETE** — SQLAlchemy models (Contribution state machine PENDING→REVISION_REQUESTED/APPROVED/REJECTED, ReviewerQueueItem, ContributionFeedback), 12 Pydantic schemas, 26 comprehensive tests (all passing). **Deliverables**: (1) 3 data models + 4 enums, (2) 12 schema classes, (3) 26 tests (field validation, relationship integrity, workflows, status transitions). Backward compatible with Phase 1–2. **Next**: Phase 3 routes (8 endpoint groups per PHASE_3_DESIGN.md — POST contributions, GET pending, review decision, history, finalize, request revision, contributor stats). **Remaining effort**: 38 story points total (~58 hours, 3.5-4 weeks). Expected 53-60 new tests. Commit: `3a94093`.
**Blocked on**: —
**Notes**: Backend Phase 1–2 production-ready and fully backward compatible. Phase 3 data layer validated, tested, ready. All core architecture solid (FastAPI, PostgreSQL, Meilisearch, async). Ready to prioritize Phase 3 routes implementation.

---

### off-grid-living
**Goal**: A comprehensive plan for off-grid, sustainable living. Define full plans for construction, implementation, operation, maintenance, and repair. Cover the complete operational architecture: food production, shelter, medicine, electricity generation, food preparation and storage, water, and general survival necessities. Include disaster scenarios up to and including nuclear disaster. Also cover community building, organization, and mutual support.
**Priority**: Medium
**Status**: Active — research phase
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/off-grid-living/`
**Current focus**: **ALL 16 DOMAIN FILES NOW COMPLETE.** Session 103: `01-site-selection.md` (1,178 lines — 32-criterion parcel evaluation checklist; weighted scoring matrix; prior appropriation vs. riparian doctrine; state-by-state water/zoning/off-grid legality; regional comparison table with Mid-South/Appalachian/Pacific NW/Mountain West/Southwest detail; due diligence guide with minerals/easements/perc test/flood plain; 3-phase transition model with budget tables) and `12-security-defense.md` (1,252 lines — 13-threat probability×consequence matrix; fencing/camera/dog systems; livestock predator table 14 species; firearms loadout + storage + training; community defense protocols; 12 threat-specific response protocols; quarterly audit checklist; regional profiles; 50+ product reference list with 2026 prices). Both domains were the only ones listed as "Planned" in master-outline.md. **Document map now 100% complete.** **Next**: Quality review pass OR publish-ready formatting pass across all 16 domains.
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

---

## Completed (Archive)

<!-- Move completed projects here with a completion date -->
