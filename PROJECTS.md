# Active Projects

> This is the single source of truth for autonomous orchestration.
> The orchestrator reads this file at the start of every session.
> Update priorities, status, and current focus as work progresses.
>
> **Last updated by**: orchestrator on 2026-04-13 (Session 87)

---

## Priority Order
1. stockbot
2. resistance-research
3. open-source-rideshare
4. seedwarden
5. open-repo
6. off-grid-living
7. containerized-agents
8. workout
9. resume

---

## Projects

### resistance-research
**Goal**: Identify solutions to a failing democracy — if the current government could be replaced and rebuilt from a clean slate, what would it look like? How could it be structured to ensure justice, life, liberty, and the pursuit of happiness for all citizens? How could it be objectively efficient, equitable, and functional? This project addresses the full scope of government: voting systems, taxation, education, infrastructure, healthcare, law enforcement, housing, and everything in between. The government exists to serve its citizens — so how do we actually achieve that? A secondary goal is tracking and understanding the specific crises the United States is currently facing, finding actionable responses, and building a comprehensive integrated proposal for democratic renewal.
**Priority**: High
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: Democratic renewal proposal at 22 domains / 2,544 lines / 13 feedback loops. All 22 domains at full evidence depth. Session 87: April 20 watch brief complete — `monitoring/2026-04-20-watch.md` (46 sources). Key status: CAPE Phase 1 launches April 20 (26,664 importers enrolled, $120B duty value; ACH enrollment gap is primary risk — ~$46B unenrolled; AD/CVD and drawback entries excluded); Abrego Garcia DOJ brief due April 20 — four scenarios mapped (Liberia maintain + structural exec-power args most likely, hands Xinis contempt predicate; Fourth Circuit emergency filing is code-red escalation scenario); White House ballroom post-April-17 branch unconfirmed (Branch C — stay expiry + contempt — had strongest circumstantial support as of April 13); Nashville/Crenshaw: dismissal still imminent, Blanche public statements in record; Section 122 CIT: no ruling, July 24 expiry; Humphrey's Executor (Trump v. Slaughter): narrowing likeliest, decision by June; May Day Strong coalition confirmed, April 29 lead-up, May 1 general strike. **Next**: April 20 monitoring pass — CAPE launch reporting + Abrego Garcia DOJ brief on filing + confirm post-April-17 ballroom branch; April 28 Xinis hearing is next hard event.
**Blocked on**: —
**Notes**: Ongoing research and monitoring project. Existing files cover ICE detention, litigation tracking, case studies, civic action. When no specific task is queued, extend existing threads, find new angles, and monitor developments. Democratic renewal proposal is comprehensive at 22 domains; remaining work is quality deepening and publication preparation.

---

### stockbot
**Goal**: Build a full-stack model building and automated trading platform with both a web app and iOS app integration. The platform should allow creation, backtesting, and optimization of trading models across multiple model types (stock, options, rule-based, ensemble, multi-timeframe). The end goal is fully automated live trading — but only after models are rigorously vetted and confidence is established through paper trading. Model training and optimization costs must stay under $20/month. Once a model is sufficiently validated through paper trading performance, it graduates to live trading. Profit maximization is the north star, but capital preservation and risk management are non-negotiable constraints.
**Priority**: High
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**Current focus**: Paper trading LIVE as of 2026-04-13. 3 sessions running and healthy (verified Session 77): momentum (SPY/QQQ/MSFT), rsi_mean_reversion (AAPL/NVDA), sma_crossover (AMZN/SPY). All cycling every 60s, market_open=false (weekend). First trades fire Monday 9:30 AM ET (13:30 UTC). Monitor via `http://127.0.0.1:8000` Trading page or `curl -H "Authorization: Bearer $STOCKBOT_API_KEY" http://127.0.0.1:8000/api/paper-trading/cycle-log?limit=20`. Next: review Monday cycle logs after market open — did momentum fire? Any errors? iOS app deferred until paper trading stable.
**Blocked on**: —
**Notes**: Web app is in good shape. Model creation and most optimisation is operational. Paper trading has just started but has had issues — this is the current priority. iOS app is out of scope until paper trading is solid. All features must work across ALL model types (stock, options, rule-based, ensemble, MTF) — do not implement something for one type only.

---

### open-source-rideshare
**Goal**: Build a free, open-source alternative to Uber and Lyft that stops price-gouging both riders and drivers. The platform should be a web and mobile app that minimises deployment and maintenance costs, ideally using a model where the platform itself is non-profit or cooperative — the margin extracted by Uber/Lyft goes back to drivers and riders instead. Solve the real problems: regulatory compliance in different jurisdictions, driver and rider safety and security, insurance, payment processing, and trust. Also build a plan for bootstrapping the user and driver base — a rideshare app with no users is worthless, so growth strategy is part of the scope.
**Priority**: Medium
**Status**: Active — early stage
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-source-rideshare/`
**Current focus**: Backend comprehensive — 2,288 tests passing. Features include: matching engine, WebSocket, payments (Stripe, cancellation fees), pricing (demand-aware, time-of-day), geocoding, auth, admin API, Alembic migrations, ride history, profile endpoints, safety service (SOS, trip sharing, emergency contacts), admin SOS monitoring, cancellation policy, notification service (Twilio SMS + SendGrid email + Firebase FCM push), driver rating aggregation, rate limiting, admin SOS WebSocket, scheduled rides, dispatch scheduler + retry logic, admin cancellation stats, driver earnings, promo codes & referral system, ride receipts, service areas/geofencing, admin feedback & disputes, ride & driver metrics dashboard, ride pooling/shared rides, vehicle management & WAV matching, in-app chat, transparent demand pricing, driver ETA estimation, saved locations, admin document verification, recurring rides/commute scheduling, multi-stop rides/waypoints, fare splitting, driver payout & settlement (Stripe Connect), SMS/email notification integration, audit logging & compliance reporting, background check integration (Checkr API), device token management (FCM), driver incentive/bonus programs (quest, peak-hours, streak, earnings guarantee), rider rating system (drivers rating riders, low-rated flag, admin monitoring), per-user push notification preferences (opt-in/out by type + channel, SOS bypass, full CRUD API), driver availability and scheduling (weekly schedule slots, online/offline toggle, heartbeat, admin monitoring), driver availability dispatch integration (MatchingEngine filters to online+heartbeat+schedule-window drivers; opt-in model; `availability_filter` param; 20 new tests), driver insurance document management (DriverInsuranceDocument + InsuranceExpiryAlert models; status machine; 45 tests), driver vehicle inspection records (VehicleInspection model; 5 types; auto-expiry; 69 tests), driver license + vehicle registration document management (DriverLicense + VehicleRegistration models; expiry tracking + alerts; 71 tests), **driver onboarding status and activation workflow** (DriverOnboarding model; OnboardingStatus: incomplete/pending_review/approved/suspended; checklist aggregates background check + license + registration + inspection + insurance + profile; activate_driver validates all items; suspend_driver with mandatory reason; admin list endpoints for pending/incomplete with pagination; 6 API endpoints; Alembic migration d1e2f3a4b5c6; 49 tests). Push to GitHub blocked pending SSH key/credentials setup. Both Flutter apps have full user flows.
**Blocked on**: —
**Notes**: This is the only public project. Higher standards for documentation, test coverage, and code quality since it's community-facing. Regulatory/safety/security solutions and growth strategy are in scope alongside the technical build.

---

### seedwarden
**Goal**: Build a profitable Etsy store and digital brand focused on farming, homesteading, and survival-related digital products, with the ability to expand into physical small products and seed packets. The business needs a full foundation: high-quality digital products that genuinely help people, a consistent social media presence across relevant platforms, and a reputation for real value. The goal is profit and a loyal customer base — not just a store. Grow the business systematically, identify what sells, double down on winners, and build a media presence that drives traffic organically.
**Priority**: Medium
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/seedwarden/`
**Current focus**: 19 products total (14 Tier 1, 3 Tier 2, 0 Tier 3). Session 87: Apartment Growing Complete Guide upgraded Tier 3→Tier 2 — Etsy listing copy written ($13, 13 tags, cross-links to Apartment Plant Catalog/Container Pack/Seed Starting Kit). Wild edibles habit photos (Stellaria + Taraxacum) already downloaded in `assets/wild-edibles/`. **Biggest blocker**: PDF mockup images needed for all listings — #1 conversion factor on Etsy, requires Canva or mockup generator. Also: PDF regeneration needed after content edits. Photo sourcing pass for Native Plants guide still pending.
**Blocked on**: —
**Notes**: Etsy store exists with some products started but not yet quality to sell. Social media has plans but nothing executed. Need to fix quality before promoting. Plant images: all 120 native-plants images already downloaded and cached (verified Session 74) — "0/18" note in prior session was stale.

---

### open-repo
**Goal**: An open-source library for all things under the sun — a distributed, free, one-stop shop to find and share information that benefits all of humanity. Link to Wikipedia for general information, schematics, building plans, 3D models, recipes/instructions, services to share, and more. The core principle: no single person or organization controls any of it. Everything is distributed and open source. This is about leveling the playing field — giving all people the best chance to not only survive but thrive.
**Priority**: Medium
**Status**: Active — research phase
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-repo/`
**Current focus**: Landscape research COMPLETE. Architecture notes COMPLETE. MVP protocol design COMPLETE (Session 78) — `mvp-protocol-design.md` (711 lines): 5 JSON-LD content type schemas, endorsement schema, ActivityPub federation protocol, 5-phase bootstrapping plan, MVP stack decisions (FastAPI/PostgreSQL/Meilisearch/Kubo/Next.js). Content import pipeline research COMPLETE — `content-import-openFarm.md`: OpenFarm API/schema/license documented, field mapping + sample transformation + 5-step implementation plan. Extraction script scaffolded: `scripts/import_openFarm.py` — `fetch_crops()`, `transform_crop()` (implemented), `validate_schema()`, `export_jsonl()`, `compute_cid_placeholder()`, CLI entry point. Key finding: OpenFarm live API shut down April 2025; data acquisition via self-hosted MongoDB export or Internet Archive snapshot. Next: acquire data (clone OpenFarm + mongoexport OR Internet Archive crawl), run import_openFarm.py, review output sample.
**Blocked on**: —
**Notes**: Start with landscape research before any building. The goal is ambitious — don't reinvent what already exists well. Identify the missing layer that ties it all together or fills the gaps nobody else is filling.

---

### off-grid-living
**Goal**: A comprehensive plan for off-grid, sustainable living. Define full plans for construction, implementation, operation, maintenance, and repair. Cover the complete operational architecture: food production, shelter, medicine, electricity generation, food preparation and storage, water, and general survival necessities. Include disaster scenarios up to and including nuclear disaster. Also cover community building, organization, and mutual support.
**Priority**: Medium
**Status**: Active — research phase
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/off-grid-living/`
**Current focus**: Master outline complete (`master-outline.md`, 752 lines, 16 domains). Domains complete: `03-water.md` (850 lines), `04-food-production.md` (1,301 lines), `05-food-preservation.md` (1,522 lines), `06-energy-power.md` (997 lines), `07-heating-cooling.md` (846 lines), `08-medical-health.md` (1,139 lines), `09-waste-sanitation.md` (1,110 lines), `10-tools-fabrication.md` (1,507 lines), `11-shelter-construction.md` (~1,540 lines), `12-communications.md` (1,854 lines, complete — ham/GMRS/satellite/shortwave/CB; EMP hardening with E1/E2/E3 mechanism; grid-down protocols with coded status words + runner decontamination; 55-row cost table; CBRN comms; decision matrix), `13-community-organization.md` (1,785 lines, complete — governance models: consensus/council/sociocracy; mutual aid setup; skill inventories; conflict resolution ladder; trade/barter ledgers; security governance; emergency decision-making by scenario CBRN/wildfire/grid-down; membership process; mental health protocols), `14-finances-trade.md` (1,516 lines, complete — 3-phase transition model; income bridge runway formula; homestead revenue streams with revenue range tables; raw milk state legality; USDA FSA/502 loan rates 2026; seller financing; Schedule F + SE tax + hobby loss rules; ACA 2026 subsidy cliff; LETS/time banks; barter IRS reporting; ag-use tax designation; sample financial models at 3 budget tiers; 55-item cost table; 9-scenario decision matrix). Next: `15-disaster-scenarios.md` — extended power outage, severe storm, pandemic, economic collapse, civil unrest, nuclear event planning.
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
