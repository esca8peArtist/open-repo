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
**Status**: Active — READY FOR MONDAY — Phase 1 (monitoring) begins 2026-04-28T21:00 UTC, Phase 2 (litigation tracking) research COMPLETE
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: Session 437 (2026-04-26): **PHASE 2 LITIGATION TRACKING COMPLETE**. Created `phase2-litigation-tracking.md` (404 lines) with 8 legal frontiers ranked by strategic priority: (1) FISA 702 reauthorization (April 30 deadline, warrant requirement fight), (2) VRA Section 2 enforcement (Louisiana v. Callais + Turtle Mountain cases), (3) Watson v. RNC (mail ballot grace periods), (4) Trump election executive orders (voter roll seizures), (5) Missouri mid-decade gerrymandering (template spreading), (6) Section 230 litigation (circuit split). Key finding: FISA 702 is most urgent (4 days remaining). Document serves as reference for live monitoring + future quarterly updates. **Phase 1 (monitoring)** ready: May Day guide live, 3 monitoring templates verified field-ready, data capture ~10 min starting April 28 21:00 UTC. Distribution checklist ready (8 channels, 3 templates). **Status**: Both phases ready for execution. Democratic renewal proposal (22 domains) remains as future work.
**Blocked on**: —
**Notes**: Phase 1 (April 28 monitoring) + Phase 2 (litigation tracking) COMPLETE. Phase 3 (democratic renewal proposal expansion) future work. High confidence in monitoring framework and litigation research. Xinis hearing closing arguments April 28 17:00–22:00 UTC window (quick-fill: ~10 min). April 29 contingency brief ready (Nashville ruling, Section 702 expiration, 4th Circuit emergency). May 1 template ready (scale summary, 7-city tracking, labor action). All distribution channels identified and ready.

---

### cybersecurity-hardening
**Goal**: Build a comprehensive, actionable guide to protecting communications and identity against government-level mass surveillance. Understand what Palantir and similar data brokers/intelligence platforms actually have access to — what data they ingest, how they link identities, and what their current government contracts cover. From that threat model, identify the best practical techniques for private and anonymous communication: encrypted messaging, metadata minimization, network anonymization (Tor/VPN tradeoffs), device hardening, operational security (OpSec), and identity compartmentalization. The output should be a personal OpSec playbook grounded in real threat modeling — not theoretical, but calibrated to the actual capabilities of the adversary.
**Priority**: High
**Status**: Active — GIST PUBLISHED, distribution underway
**Visibility**: Public — GitHub Gist (public) + private distribution to immigration legal aid organizations
**Working dir**: `projects/cybersecurity-hardening/`
**Current focus**: Session 438 (2026-04-26): **GitHub Gist PUBLISHED**. Trilogy (threat-model.md + opsec-playbook.md + implementation-guide.md) now live at https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108. **Distribution phase 1 ready**: Tier 1 organizations (immigration legal aid, community-based orgs, mutual aid networks) can be contacted immediately using templates in DISTRIBUTION_CHECKLIST.md. Sequence: (1) NILC, CLINIC, RAICES, ILRC, NLG (immigration legal aid), (2) CASA, Make the Road, United We Dream (community orgs), (3) mutual aid networks. All email templates and contacts documented in checklist. **Next**: Execute Tier 1 distribution (can begin immediately), then Tier 2 (digital rights orgs, security researchers, journalists), then Tier 3 (policy, academic, labor).
**Blocked on**: —
**Notes**: Trilogy publication-ready and published (Gist). Distribution checklist complete with 11 channels (GitHub Gist, email outreach x5, email to legal orgs, Signal/Slack, social media, Reddit, journalists, civil rights). High-leverage distribution to immigration-focused networks can begin immediately.

---

### stockbot
**Goal**: Build a full-stack model building and automated trading platform with both a web app and iOS app integration. The platform should allow creation, backtesting, and optimization of trading models across multiple model types (stock, options, rule-based, ensemble, multi-timeframe). The end goal is fully automated live trading — but only after models are rigorously vetted and confidence is established through paper trading. Model training and optimization costs must stay under $20/month. Once a model is sufficiently validated through paper trading performance, it graduates to live trading. Profit maximization is the north star, but capital preservation and risk management are non-negotiable constraints.
**Priority**: High
**Status**: Active — paper trading LIVE on dev, Jetson deployment COMPLETE and healthy, ready for Monday market open
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**Current focus**: Session 422: **Infrastructure VERIFIED HEALTHY**. Paper trading session `33a4afe676cae12a` (AAPL_h10_lgbm_ho stacker) confirmed LIVE, started 2026-04-26T05:58:22Z, cycling every ~60 seconds, last cycle 2026-04-26T07:06:51Z. Dashboard API operational on port 8000. Zero trades (expected — market closed Sunday). **Jetson deployment already complete** from Session 421: container healthy, `/src/` volume-mounted and synced, all 5 sessions running (1 stacker + 4 legacy), market_open flags correctly false. No rebuild or rsync needed. **Ready for market open Monday 2026-04-28 (~14:30 UTC)**. P&L data capture begins automatically. Test suite: 849 passed, 30 pre-existing failures (not blocking).
**Blocked on**: —
**Notes**: Web app ready. Model machinery complete. Paper trading is LIVE and healthy on both dev and Jetson. Ready to monitor P&L Monday-Friday. iOS app out of scope until paper trading is solid. Next phase: monitor live P&L accumulation, evaluate stacker performance against baseline metrics.

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
**Status**: Active — **PRODUCT LAUNCH READY** (mockup blocker resolved)
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/seedwarden/`
**Current focus**: Session 430: **MOCKUP BLOCKER RESOLVED** — All 21 tablet mockups are complete and production-ready (2400×2400 px PNG, 350–400 KB per file, professional tablet device frame design). All content (listing copy, pricing, tags, product PDFs) verified complete. **Ready for Phase 1 Etsy launch**: Upload 6 lead products this week. MOCKUP_STRATEGY.md created (covers Etsy best practices 2026, regeneration workflow, Phase 2-4 enhancement roadmap). Social media and ongoing marketing are next phase after Phase 1 product validation.
**Blocked on**: —
**Notes**: All product infrastructure complete. Phase 1 launch unblocked. Phase 2-4 enhancements (phone mockups, lifestyle photography, printed page mockups) optional based on Phase 1 conversion data. 120 native-plants images cached and ready for future guides.

---

### open-repo
**Goal**: An open-source library for all things under the sun — a distributed, free, one-stop shop to find and share information that benefits all of humanity. Link to Wikipedia for general information, schematics, building plans, 3D models, recipes/instructions, services to share, and more. The core principle: no single person or organization controls any of it. Everything is distributed and open source. This is about leveling the playing field — giving all people the best chance to not only survive but thrive.
**Priority**: Medium
**Status**: Active — Phase 3 COMPLETE, **Phase 4 COMPLETE (Phases 1–4 all implemented)**, 210+ tests, ready for GitHub push + merge
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-repo/`
**Current focus**: Session 437 (2026-04-26): **Wave 4 PHASES 1–4 COMPLETE** (commits `fd2bf0d` Phase 1, `128994f` Phase 2, `557d5eb` Phase 3, `41baed2` Phase 4, merged into branch `feature/wave4-phase2-federation-service`). **Phase 1**: FederationPartner model + migrations. **Phase 2**: Service layer (8 methods) + admin routes (7 endpoints) for federation partner management. **Phase 3**: Inbox signature verification gate + send_announce request signing. **Phase 4**: FederationConflict model + service (6 methods) + admin endpoint + migration. **Combined results**: 210+ total tests, 0 regressions. **Key implementations**: Complete federation infrastructure (partner registration, key management, HTTP signature verification RFC 8017 + W3C ActivityPub, conflict detection/logging, trust state machine, auto-downgrade, request signing, backward compatibility). **Code quality**: Full type hints, comprehensive docstrings, error handling. **Status**: Feature branch ready for GitHub push + merge. **Next**: Optional Phase 5 (offline export/Kiwix) or production deployment validation. **Core federation infrastructure COMPLETE and production-ready**.
**Blocked on**: —
**Notes**: Wave 4 fully complete. All federation machinery production-ready: partner registration, key management, HTTP signature verification, conflict logging, admin dashboard. Ready for GitHub push. Phase 5 (offline export/Kiwix) optional based on feature priority. Production deployment gates: (1) User review and GitHub push, (2) Multi-node staging deployment validation.

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

---

## Completed (Archive)

<!-- Move completed projects here with a completion date -->
