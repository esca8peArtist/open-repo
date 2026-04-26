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
**Status**: Active — Phase 1-4 COMPLETE, **Phase 5 COMPLETE (Session 490)** — Full implementation architecture ready
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: **Phase 5 COMPLETE (Session 490)**. All four implementation strategy documents written and committed. Proposal now contains complete pathway: diagnosis (Domains 1-22) → alternative vision → theory of change (Phase 4) → implementation architecture (Phase 5). Next: Integration of Phase 5 into main proposal and distribution execution.

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

**NEXT WORK**:
- **Phase 5 Integration** (next phase): Integrate Phase 5 documents into democratic-renewal-proposal.md as Part III (Theory of Change) and Part IV (Implementation Architecture)
- **Distribution execution** (user action): Substack, Reddit, institutional templates ready for user posting (Phase 4+5 now fully actionable)
- **Tracker updates** (ongoing): First-amendment, environmental-rollbacks, police-brutality trackers ready for regular maintenance

**Blocked on**: —
**Notes**: Phase 5 COMPLETE. Proposal now contains complete actionable pathway: diagnosis (Domains 1-22) → alternative vision (democratic renewal proposal) → theory of change (Phase 4 documents: power-mapping, parallel-institutions, elite-capture-case-study, comparative-democratic-recovery) → implementation architecture (Phase 5 documents: implementation-roadmap, timeline-and-conditions, movement-coordination, risk-assessment). Implementation timeline ready for 2026 election trigger and three recovery scenarios (House flip / tight House / federal collapse).

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
**Status**: Active — paper trading live, **strategy optimization COMPLETE**, ready for monitoring + live trading launch
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**Current focus**: Paper trading running (AAPL_h10_lgbm_ho stacker). **All three strategy optimization tasks COMPLETE** (Sessions 488-489). AAPL_h10_lgbm_ho validation plan in place, monitoring script deployed, live trading readiness checklist ready. **Next**: Monitor paper trading daily, assess progress toward Gate 1 (30 trades/month), prepare live trading transition once all gates pass for 3 consecutive months.

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

**Next tasks — work these in order:**

1. **Paper Trading Monitoring** — Daily run of `paper_trading_monitor.py` via cron (appends to `logs/paper_trading_daily.jsonl`)
   - Track progress toward Gate 1 (30 trades/month) — started 2026-04-26, expecting data by 2026-05-26
   - Monthly checkpoints: 2026-05-26, 2026-06-26, 2026-07-26
   - All three gates (1+2+3) must pass for 3 consecutive months before graduation

2. **Live Trading Launch** — After 3-month validation complete:
   - Confirm Alpaca account setup (cash account, funds ready)
   - Verify all guardrails in `src/guardrails.py` deployed to Jetson
   - Initial funding: $100–500 (position limits per readiness checklist)
   - Monitor daily for first 2 weeks, scale only after 2+ weeks profitable performance
   - Use `docs/live-trading-readiness.md` as user-facing launch checklist

**Blocked on**: —
**Notes**: All optimization tasks complete. Strategy portfolio cleaned (8 strategies, SMA structural failures removed). Validation plan in place with clear graduation criteria. Guardrails verified. Paper trading provides the validation signal. Live trading will begin with minimal capital ($100–500) and scale incrementally only after demonstrated profitable performance.

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

- ~~**workout: nutrition and tracking companion**~~ — **Done (Session 493)**: `projects/workout/nutrition-and-tracking.md` (6,226 words) — comprehensive nutrition framework (macro targets by goal/tier/frequency), meal planning with 3 sample days (2,000/2,600/3,000 cal), weekly tracking template, progress timeline expectations, deload protocol, integration with comprehensive-plan.md.

- ~~**cybersecurity-hardening: device hardening deep-dive**~~ — **Done (Session 493)**: `projects/cybersecurity-hardening/device-hardening-guide.md` (3,200 words) — iPhone hardening (iCloud ADP as critical attack surface, airplane mode vs. power-off technical differences), Android hardening (bootloader paradox, GrapheneOS verified boot recovery, Cellebrite forensics leak data), cross-platform compartmentalization and recovery scenarios, evidence-based (Apple guidelines, GrapheneOS docs, EFF guides, privsec.dev analysis).

---

## Completed (Archive)

<!-- Move completed projects here with a completion date -->
