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
**Status**: Active — Phase 1 launched, Phase 2 live, **Phase 3 COMPLETE (Session 487)**
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: **Phase 3 Research Integration COMPLETE (Session 487, agent af2c0c7d2a166e403)**. Phase 3 research roadmap (7,148 words, 8 case studies) fully integrated into democratic renewal proposal:
- Pattern 6 in Section 3.1: Carnegie Endowment recovery playbook + Poland's PiS enclave problem
- Section 3.1a (new): Constitutional Design Dimension — 935-constitution study, Tunisia institutional failure, Germany Basic Law design
- Section 3.5 (new): Post-Electoral Recovery Challenge — 4-phase US sequence, autocratic enclave inventory, interstate compact strategies
- Domain 3: Ireland Citizens' Assembly two-stage model mechanics
- Domain 6 subsection 6i (new): German Basic Law as Weimar response — specific failure modes and US analogs

**✅ COMPLETED (Session 487)**:
- ✅ **Phase 3 research roadmap integration** — 5 substantive integrations woven into proposal structure (not appended)
- ✅ Files: `democratic-renewal-proposal.md`, `democratic-renewal-executive-summary.md`, `published/README.md` updated
- ✅ Committed: d911817 — "feat(resistance-research): integrate Phase 3 research roadmap into democratic renewal proposal"

**✅ COMPLETED (Session 485-486)**:
1. **Priority documents**: first-amendment-suppression.md (3,400 words), environmental-rollbacks-tracker.md (3,800 words), police-brutality-consent-decree-tracker.md (4,200 words)
2. **Proposal infrastructure**: democratic-renewal-executive-summary.md, DISTRIBUTION_GUIDE.md, published/README.md
3. **Distribution templates**: Substack drafts (4 posts), Reddit templates (5 posts), institutional outreach (8 templates)
4. **Phase 3 research roadmap**: 7,148 words, 8 case studies, implementation timelines, adoption pathways

**NEXT WORK**:
- **Distribution execution** (user action): Substack, Reddit, institutional templates ready for user posting
- **Tracker updates** (ongoing): First-amendment, environmental-rollbacks, police-brutality trackers are production-ready for regular updates

**Phase 4 — Theory of Change (new scope, 2026-04-26)**: The project has a strong diagnosis and a vision of "what better looks like." The identified gap is the *mechanism* question: how does a captured system get replaced when the people who'd need to approve change are the same ones who benefit from blocking it? Four documents to produce, in priority order:

1. **`comparative-democratic-recovery.md`** — Cross-national case study: countries that underwent democratic backsliding and recovered (South Korea post-1987, Spain post-Franco, Uruguay post-dictatorship) vs. those that failed to recover (Hungary, Venezuela, Turkey). What structural factors made the difference? What role did parallel institutions, international pressure, elite defection, and mass mobilization each play? Identify replicable patterns and apply explicitly to the US context. (~4,000 words, heavily cited)

2. **`power-mapping.md`** — Concrete analysis of who specifically holds veto power over systemic change in the US (not abstract "elites" — named institutions, networks, funding streams). Map: legislative veto players, judicial capture mechanisms, dark money networks (Federalist Society, Koch network, AIPAC), foreign lobbying exemptions (FARA gaps), and revolving-door pipelines. For each: what are their known vulnerabilities (electoral, legal, reputational)? What historical precedents exist for displacing comparable entrenched power? (~3,500 words)

3. **`parallel-institutions.md`** — Concrete models for building functional systems that reduce dependence on captured federal apparatus while developing the organizational base for structural reform. Cover: mutual aid networks, community land trusts, worker cooperatives, local food sovereignty, community broadband, credit unions vs. commercial banks, state-level single-payer experiments. For each: current scale, replication requirements, documented political effects (does local alternative-building translate to political capacity?). (~3,500 words)

4. **`elite-capture-case-study.md`** — The Epstein network as a documented case study in accountability system failure. Not speculative — use only what is established in court records, unsealed documents, investigative journalism (NYT, Miami Herald, Vanity Fair, Hersh). Cover: the 2008 NPA deal as prosecutorial capture, the Maxwell trial record, documented connections to intelligence services (Robert Maxwell/Mossad per multiple credible sources), the FARA gap that allowed foreign influence networks to operate without disclosure, and systemic implications for democratic accountability. Explicit framing: this is evidence of *structural* failure, not individual criminality. (~3,000 words)

**Blocked on**: —
**Notes**: Phase 3 COMPLETE. Phase 4 (theory of change) is the identified research gap — the project diagnoses what's broken and proposes what better looks like, but lacks the mechanism analysis: how captured systems actually get uncaptured. These four documents fill that gap and make the democratic renewal proposal actionable rather than aspirational.

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
**Status**: Active — paper trading live, **multi-strategy conflict resolution COMPLETE**, ready for strategy optimization
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**Current focus**: Paper trading running (AAPL_h10_lgbm_ho stacker). **Multi-strategy conflict resolution COMPLETE (Session 487, agent a660bdfc102ec8e28)**.

**Completed (Session 487)**:
1. ✅ **Multi-strategy conflict resolution** — COMPLETE:
   - `src/trading/strategy_coordinator.py` — `StrategyCoordinator` class (stdlib only, zero external deps)
   - **Conflict classes identified and solved**:
     1. Position double-counting (same ticker across strategies) → `aggregate_open_positions()` sums cross-strategy exposure
     2. Competing orders (both strategies submit independently) → `acquire_symbol_lock(symbol)` serializes order submission per ticker
     3. Rate limit multiplication (N engines × max_orders cap) → shared 60-second sliding window global counter
   - `tests/unit/test_trading/test_strategy_coordinator.py` — 43 comprehensive unit tests, all pass
   - **Total test suite**: 723 trading unit tests pass, 0 regressions
   - **Integration pattern**: Lock acquisition → aggregate positions → validate with guardrails → submit → record global order
   - Committed: 9c28451 — "feat(stockbot): implement StrategyCoordinator for multi-strategy conflict resolution"

**Completed (Session 486)**:
1. ✅ **Live trading guardrails** — COMPLETE:
   - `live-trading-guardrails.md` specification (rationale, implementation approach, config parameters)
   - `src/guardrails.py` module: 6 validators (emergency halt, instrument ban, cash-only, position limit, concurrent cap, daily loss killswitch)
   - 88 unit tests (all passing)

**Next tasks — work these in order:**

2. **Strategy optimization** — run backtests on existing strategies; evaluate performance per graduation criteria; eliminate underperformers; document in `strategy-evaluation.md`

3. **Live trading readiness checklist** — when paper trading shows consistent positive performance (per graduation criteria), produce user-facing checklist: switch to funded live account, verify cash account (no margin), confirm guardrails active, set initial funding

4. **Live trading launch** — once model graduation criteria met and all checks pass, transition to Jetson deployment with live trading enabled

**Blocked on**: —
**Notes**: Multi-strategy system is now conflict-free. Next: optimize and evaluate which strategies should graduate to live trading. Paper trading provides the validation signal. Guardrails are in place. Live trading will begin with minimal funding ($100–500) and scale only after 2+ weeks of profitable live performance.

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
**Status**: Active — Phase 1 upload pending user tag corrections; native plants guide on hold for image rebuild
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/seedwarden/`
**Current focus**: **Two parallel tracks:**

**Track A — Phase 1 launch (blocked on user)**: 3 tag corrections and Etsy account verification required before upload (documented in `UPLOAD_READY_CHECKLIST.md`). Once user completes those, the 8 text-heavy products below are ready to list immediately. Do NOT hold up these products waiting on the native plants guide.

**Phase 1 products ready to launch** (text-heavy, no photo dependency):
- Companion Planting Chart, Zone-by-Zone Seed Starting Calendar, Seed Saving Field Manual, Survival Garden Regional Plans, Apartment Seed Starting Kit, Container Growing Blueprint Pack, Food Sovereignty Starter Guide, 12-Month Urban Growing Planner

**Track B — Native plants guide image rebuild** (Session 486 COMPLETE): The PDF was 56.96 MB (exceeds 5 MB Etsy limit). Root cause: fpdf2 embeds JPEG images verbatim (no recompression). Solution applied (agent ae85740e7bcee5ae1):
- Modified `generate_pdfs.py` with Pillow-based recompression: max 600px on long axis, JPEG quality 55
- Implemented `_compressed_image_path()` function: caches recompressed images (one-time per unique image per run)
- **Result**: PDF reduced 56.96 MB → 4.91 MB, still clearly legible (138 DPI), NOW ETSY-COMPLIANT
- Images remain correctly identified (Wikipedia/iNaturalist botanical sources)

**Blocked on**: Tag corrections + Etsy account verification (user action, Track A only). Track B has no blockers.
**Notes**: User reviewed deliverables and found formatting issues in some PDFs and unreliable photos in native plants guide. Text-heavy products are solid and can launch. Native plants guide needs image rebuild — use authoritative botanical sources (USDA, Wikimedia) not web scraping. Phases 2–4 (phone mockups, lifestyle photography, printed page mockups) to be evaluated after Phase 1 conversion data is in.

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

- **workout: nutrition and tracking companion** — comprehensive-plan.md is complete but lacks nutrition guidance and progress tracking. Add: a nutrition framework (macros by goal + equipment tier), a weekly tracking template (lifts, bodyweight, energy), and a progress milestone chart. Write to `projects/workout/nutrition-and-tracking.md`. This extends the plan without requiring user review of the existing document.

- **cybersecurity-hardening: device hardening deep-dive** — the Palantir threat model is complete. Next gap: practical device hardening for iPhone and Android against government-level surveillance. Research: aeroplane mode vs. full-power-off for RF silence, locked bootloader implications, GrapheneOS vs. CalyxOS tradeoffs, iCloud vs. local backup security, location data brokers and how to opt out, and SIM swapping as an attack vector. Write to `projects/cybersecurity-hardening/device-hardening-guide.md`.

---

## Completed (Archive)

<!-- Move completed projects here with a completion date -->
