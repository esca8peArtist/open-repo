# Exploration Queue

> Autonomous research work when all projects are blocked on user actions.
> Items are prioritized by impact and feasibility.

## Completed Items (Session 933)

### ✅ Item 10: Stockbot Post-Gate-1 Architecture Design
**Status**: COMPLETE (Session 933, May 9 2026)
**Effort**: 3.5 hours
**Deliverable**: `projects/stockbot/POST_GATE_1_ARCHITECTURE_OPTIONS.md` (351 lines)
**Content**: 5 technical options evaluated for Gate 2 (Sharpe ≥1.0, MDD ≤20%):
- Option 1: Volatility-Adaptive Position Sizing (MEDIUM complexity, HIGH impact)
- Option 2: Trend/Regime-Following Overlay (MEDIUM complexity, MEDIUM impact)
- Option 3: Options Strategies for Downside Protection (HIGH complexity, MEDIUM impact)
- Option 4: Ensemble Model Reweighting Per Regime (LOW complexity, HIGH impact) — **RECOMMENDED FIRST**
- Option 5: Momentum Exit Gates + Time-Decay Avoidance (LOW complexity, MEDIUM impact)

**Key Findings**: HMM regime detection currently performs poorly (42.75% accuracy, sideways regime only 29.3%); Option 4 recommended as first post-Gate-1 implementation since it routes around HMM dependency
**Next Step**: Deploy immediately after May 12 checkpoint outcome (IF Gate 1 pass: Option 4 first; IF miss: Options 1+2 before live trading)

---

### ✅ Item 11: Resistance-Research Distribution Path Execution Planning
**Status**: COMPLETE (Session 933, May 9 2026)
**Effort**: 2.5 hours
**Deliverable**: `projects/resistance-research/DISTRIBUTION_PATH_EXECUTION_GUIDE.md` (50 KB)
**Content**: Detailed execution plans for all 3 distribution paths:
- **Path A**: 3-wave sequence (25 contacts, 21 days), full three-tier rollout (credibility anchors → institutional depth → civil society/labor)
- **Path A+37 Hybrid** (RECOMMENDED): Path A + Phase 1b election protection sequencing (Domain 37 strategic routing before May 28 deadline), 50% most-likely outcome for election impact
- **Path B**: 14-day research extension (domains 25, 19f, others) with force-launch protocol if deadline approaches

Plus: week-by-week calendars, contact sequencing, messaging customization by sector (law schools, think tanks, labor, civil rights, election protection), success metrics (reply rates by wave, institutional traction, policy uptake), contingency plans
**Key Insight**: Path A+37 balances immediacy (leverage May 12 checkpoint momentum) with strategic targeting (election organizations get Domain 37 before May 28 DEA deadline)
**Next Step**: User selects path → orchestrator executes immediately using provided calendars and contact sequences

---

### ✅ Item 12: Cybersecurity Tier 2 Pilot Launch Readiness
**Status**: COMPLETE (Session 933, May 9 2026)
**Effort**: 2.5 hours
**Deliverable**: `projects/cybersecurity-hardening/TIER_2_PILOT_LAUNCH_READINESS.md` (17 KB)
**Content**: 8-week pilot plan for 3-5 organizations:
- **Pilot Cohort**: Freedom of the Press Foundation (Playbook 5, journalist security, 65+ newsroom multiplier), National Lawyers Guild Mass Defense (Playbook 3, activist organizing), Community Legal Services Philadelphia (Playbook 1, immigration evasion validation); GAIN deferred (election worker playbook gap)
- **Timeline**: Weeks 1-3 parallel preparation (Phase 1 in flight), Week 4 pilot launch, Weeks 4-6 initial feedback, Week 6 adoption decision gate, Weeks 7-11 full Tier 2 rollout
- **Success Metrics**: 60%+ adoption rate among pilot orgs, 2+ messaging refinements, 1+ downstream policy asks
- **Contingency Plans**: Low adoption response, security incident escalation, contact turnover fallbacks

**Key Insight**: Parallel preparation (Weeks 1-3 while Phase 1 executes) compresses overall timeline by 2 weeks; pilot decision gate at Week 6 informs full Tier 2 wave launch
**Next Step**: After user approves Phase 1 execution, parallel-launch Tier 2 pilot while Phase 1 outreach completes

---

## Previously Completed Items

### ✅ Items 1–6: Core infrastructure (Sessions 912–914)
Stakeholder landscape, competitive intelligence, market positioning, technical infrastructure, engagement mechanisms, impact measurement frameworks

### ✅ Item 8: Cross-Project Timeline Coordination (Session 915)
May 12–May 30–June 15 timeline coordinated across stockbot, resistance-research, seedwarden projects

---

## Completed Items (Session 941)

### ✅ Item 18: Jetson Resilience Assessment — POST-GATE-1 READY
**Status**: COMPLETE (Session 941, May 12 2026, 20:30 UTC)
**Effort**: 1.5 hours
**Deliverable**: `projects/stockbot/JETSON_RESILIENCE_ASSESSMENT.md` (5.4 KB)
**Content**: Comprehensive 6-part post-Gate-1 Jetson resilience evaluation:
1. **System health monitoring**: Critical metrics (disk, memory, CPU, I/O, network, DB size), thresholds (WARN/CRIT), automated health-check.sh script
2. **Failure recovery procedures**: Container crash recovery (2-3 min recovery time), disk full recovery (5-10 min), database corruption recovery with backup restore
3. **Network reliability**: SSH/API/Alpaca connectivity verification, latency baseline testing (50-150ms expected), SSH tunnel fallback for unstable ISP
4. **Power & data persistence**: Power cycle resilience test procedure, systemd auto-start verification, automated daily database backups (14-day history)
5. **Monitoring & alerting**: Monitoring stack matrix, Discord alert routing (WARN/CRIT levels), weekly/monthly review cadence
6. **Gate 2 recommendations**: Pre-deployment checklist (health-check script, power cycle test, backup verification, baseline testing), known limitations (disk I/O >85%, ISP latency variability, non-market-hours-only testing)

**Key findings**: Jetson system is well-positioned for 24/7 operation post-cleanup. All critical failure modes have documented recovery procedures with specific recovery times (2-10 min range). Health check automation enables hourly monitoring without manual intervention.

**Strategic impact**: Gate 2 deployment can proceed with confidence. Risk mitigation checklist provides clear pre-deployment actions. Post-Gate-1, this assessment is the final infrastructure prerequisite.

---

### ✅ Item 19: Domain 42 (DEA Hearing) — Outreach Amplification Strategy
**Status**: COMPLETE (Session 941, May 12 2026, 20:10 UTC)
**Effort**: 1.5 hours
**Deliverable**: `projects/resistance-research/DOMAIN_42_AMPLIFICATION_STRATEGY.md` (5.8 KB)
**Content**: Comprehensive 5-part post-Phase-1-distribution amplification strategy:
1. Media calendar (3 weeks of journalist targeting by sector + pitch angles)
2. Sector-specific messaging variants (drug policy, civil rights, academic, state AG)
3. Organization preparation checklists (internal briefing, testimony development, docket filing)
4. Post-May-28 impact assessment framework (metrics, decision trees, contingency triggers)
5. Contingency plans (late Phase 1 launch, low media pickup, organization capacity limits)

**Key findings**: Domain 42 amplification is path-independent (works for Path A, A+37, or B distributions). Strategy provides pre-built templates for all 4 organization categories, media targeting framework (policy→drug policy→civil rights weekly progression), and contingency triggers for low-participation scenarios. Actionable immediately upon Phase 1 distribution launch.

**Strategic impact**: May 28 DEA hearing (16 days away) is critical inflection point for drug policy democratic design advocacy. Phase 1 organizations will need detailed amplification infrastructure to maximize participation notice filings. This strategy bundles everything in one reference document.

---

## Completed Items (Session 934+)

### ✅ Item 13: Domain 42 (DEA Hearing) — Outreach Amplification Strategy
**Status**: COMPLETE (Session 934, May 9 2026) — **NEW**
**Impact**: HIGH — May 28 DEA hearing deadline for cannabis scheduling
**Goal**: Prepare comprehensive post-distribution outreach amplification for resistance-research Phase 1 organizations, custom messaging by sector (drug policy, civil rights, academic, state AGs), social media calendar, media/journalist follow-up, policy impact tracking
**Feasibility**: HIGH — execution infrastructure ready from `execution/domain-42-*` files
**Effort estimate**: 3-4 hours
**Deliverable**: `projects/resistance-research/DOMAIN_42_AMPLIFICATION_STRATEGY.md` (media calendar, sector-specific messaging, journalist briefing notes, policy contact tier-2 list, post-May-28 impact assessment framework)
**Why now**: 19 days to deadline; distributing Phase 1 in next 1-2 weeks means organizations will need detailed talking points, media list, and follow-up coordination by mid-May to organize public comment filing
**Next Step**: Start immediately if user chooses distribution path; otherwise queue for execution after distribution path decision

---

### ✅ Item 14: Seedwarden Phase 2 — Photography & Field Logistics Planning
**Status**: COMPLETE (Session 934, May 9 2026) — **NEW**
**Impact**: HIGH — May 30 Phase 2 launch (3 weeks away), dependent on May field photography
**Goal**: Develop comprehensive photography site selection, species prioritization, habitat assessment framework, kit logistics, equipment checklist, post-shoot processing workflow, and specimen data capture structure. Enable user to execute 5-10 field sessions efficiently.
**Feasibility**: HIGH — KNOWLEDGE.md, Phase 1 guides, species database exist
**Effort estimate**: 3-4 hours
**Deliverable**: `projects/seedwarden/PHASE_2_PHOTOGRAPHY_LOGISTICS.md` (site selection criteria by ecosystem, species prioritization grid, daily field checklist, equipment manifest, habitat assessment form, specimen data template, post-shoot photo processing + metadata integration, photography timeline May 10-30)
**Why now**: 21 days to launch; photography logistics must be finalized by mid-May to allow 1-2 week buffer for photo processing and guide refinement before May 30
**Next Step**: Deliver logistics plan; user confirms availability May 10-30 field window; orchestrator coordinates with guide writing

---

## Completed Items (Session 937)

### ✅ Item 15: Seedwarden Phase 2 Guide Content Expansion Blueprint
**Status**: COMPLETE (Session 937, May 9 2026)
**Effort**: 3.5 hours
**Deliverable**: `projects/seedwarden/PHASE_2_GUIDE_CONTENT_BLUEPRINT.md` (531 lines, ~4,800 words)
**Content**: Species Priority Matrix (20 Tier 1, 15-20 Tier 2), 6-stage guide writing pipeline, photo-to-guide integration, seasonal content calendar (May-Dec), database schema (24-field species-database.csv), publishing cadence (45-50 species by year-end), content integration (Phase 1 cross-references, email campaigns, social media 5-post sequence, bundle triggers)
**Key Insight**: Guide-writing pipeline removes May 31 start-up friction. User can write continuously post-May-30 without discovery work.
**Next Step**: User confirms May 30 photography schedule → guide writing begins May 31 using this blueprint

---

### ✅ Item 16: mfg-farm Pre-Launch Fulfillment Workflow
**Status**: COMPLETE (Session 937, May 9 2026)
**Effort**: 2.5 hours
**Deliverable**: `projects/mfg-farm/PRE_LAUNCH_FULFILLMENT_WORKFLOW.md` (453 lines, ~4,460 words)
**Content**: Payment processor comparison (Stripe $1.02 vs PayPal $1.24 per order, Etsy integrated), shipping integration (USPS Ground Advantage $4.05-$7.65 Zone 3-4), fulfillment workflow (48-hour SLA), customer support (Freshdesk templates, <24 hr SLA), QA gates (3 checkpoints), packaging specs (Phase 1 $0.10-0.12, Phase 2 $0.38-1.10 branded), launch readiness checklist, 30-day ramp-up (0-3 Week 1, 20-50/week Month 3)
**Key Insight**: Post-test-print launch friction reduced to 1-2 hours. All fulfillment infrastructure pre-built.
**Gap identified**: Pre-launch batch print with explicit three-point FDM_TOLERANCE calibration (0.00, +0.05, +0.10 mm) is implicit, not explicitly structured. Recommend extending QA section before first production batch.
**Next Step**: User completes test print → fulfillment setup begins same day

---

### ✅ Item 17: Cybersecurity-Hardening Tier 1 Success Measurement Framework
**Status**: COMPLETE (Session 937, May 9 2026)
**Effort**: 3.0 hours
**Deliverable**: `projects/cybersecurity-hardening/TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md` (v2.0, ~5,800 words)
**Content**: KPI targets (45% click, 60% meeting acceptance, 10% adoption by Week 6), 5-tab Google Sheets tracking, 4 early warning triggers with diagnostic sequences, escalation decision tree (6 scenarios), 5 contingency scenarios (delivery failure, contact list quality, negative feedback, low engagement, positive escalation) with recovery times, Week 2/4/6 continuation gates, weekly dashboard template
**Key Insight**: Measurement baseline pre-built enables data-driven Tier 2 timing decisions. Escalation procedures prevent reactive mistakes during distribution.
**Benchmarks used**: HubSpot government 30.5% baseline, M+R Benchmarks 2025 (28-40% nonprofit), Congressional Management Foundation, Campaign Monitor
**Next Step**: User approves Phase 1 → measurement framework activated immediately

---

## Active Queue (Current Session 941+)

### ⏳ Item 18: Jetson Resilience Assessment — POST-GATE-1 READY
**Status**: QUEUED (Session 941, May 12 2026) — NOW ACTIONABLE post-checkpoint
**Impact**: HIGH — Jetson disk now healthy (132GB free); need to assess network stability, power cycling recovery, container restart automation
**Goal**: Comprehensive Jetson system evaluation for 24/7 trading engine durability (gate 2 prerequisite)
**Feasibility**: HIGH — SSH access verified, disk/cron issues already fixed
**Effort estimate**: 2-3 hours
**Deliverable**: `projects/stockbot/JETSON_RESILIENCE_ASSESSMENT.md` (health check procedures, failure recovery scripts, monitoring setup, redundancy recommendations)
**Why now**: Post-checkpoint infrastructure work complete; Jetson is accessible and clean. Gate 2 deployment depends on resilience assurance.
**Next Step**: If session time available after May 14 monitoring setup, execute immediately.

---

### ✅ Item 19: Domain 42 (DEA Hearing) — Outreach Amplification Strategy  
**Status**: COMPLETE (Session 941, May 12 2026, 20:10 UTC)
**Impact**: HIGH — May 28 DEA hearing (16 days away); resistance-research Phase 1 launch imminent
**Goal**: Prepare comprehensive post-distribution outreach amplification for Phase 1 organizations, sector-specific messaging, social media calendar, media follow-up
**Feasibility**: HIGH — execution infrastructure ready from `projects/resistance-research/execution/domain-42-*` files
**Effort estimate**: 3-4 hours
**Deliverable**: `projects/resistance-research/DOMAIN_42_AMPLIFICATION_STRATEGY.md` (media calendar, sector messaging, journalist briefing, policy tier-2 list, post-May-28 impact assessment)
**Why now**: 19 days to deadline; Phase 1 distribution launching in next 1-2 weeks means organizations need detailed talking points, media contacts, follow-up coordination by mid-May
**Blocker**: User distribution path decision (A / A+37 / B) — but this can be path-agnostic preparation
**Next Step**: Execute after user selects distribution path, OR start now to have ready (path-neutral content covers all scenarios)

---

### ⏳ Item 20: Seedwarden Phase 2 — Species Prioritization & Guide Writing Workflow Prep
**Status**: QUEUED (Session 941, May 12 2026)
**Impact**: MEDIUM — May 30 Phase 2 launch (18 days); dependent on May field photography schedule
**Goal**: Deepen the Phase 2 guide writing pipeline from existing blueprint (`PHASE_2_GUIDE_CONTENT_BLUEPRINT.md`): finalize species priority matrix (Tier 1 vs Tier 2), estimate guide writing velocity, pre-stage template collection, identify highest-value species groups for May/June publishing
**Feasibility**: HIGH — content blueprint complete, species database exists, writing templates ready
**Effort estimate**: 2.5-3 hours
**Deliverable**: `projects/seedwarden/PHASE_2_WRITING_VELOCITY_ANALYSIS.md` (60 species prioritized, writing pipeline optimized, May-June publication schedule, content dependencies mapped)
**Why now**: 18 days to Phase 2 launch; current uncertainty is whether field photography window is May 10-30 or May 17-30. Writing velocity analysis removes that blocker — guides can be staged and ready regardless of photo timing
**Blocker**: User confirmation of May field photography window (needed for publishing timeline)
**Next Step**: Execute analysis now (can be done independently); when user confirms photo schedule, guide writing begins immediately with optimized workflow

---

## Previously Pending Items

### ⏳ Item 9: Jetson Resilience Assessment
**Status**: PENDING (awaiting May 12 checkpoint to assess Jetson hardware impact)
**Effort**: 2-3 hours
**Goal**: Post-Gate-1, assess Jetson resilience for 24/7 trading engine (disk 87%, network stability, power cycling recovery)
**Blocker**: Prefer to assess after Gate 1 checkpoint to understand real hardware load
**Reactivation**: May 13 (immediately post-checkpoint) if Gate 1 passes

---

## Deferred Items

### ⏸️ Item 7: Seedwarden Phase 2 Photography Logistics
User must conduct May 30 field photography. Orchestrator ready to coordinate but cannot execute photo work.
**Reactivation**: After user provides photography schedule (mid-May target)

---

## Summary

**Session 933 deliverables**: 3 exploration items completed (distribution logistics, post-Gate-1 architecture, Tier 2 pilot planning). All three are high-impact pre-work that enables immediate orchestrator execution once user approvals/decisions received.

**Total effort**: 8.5 hours of research
**Total output**: 7.5+ KB of actionable planning documents across 3 projects
**Strategic impact**: All three projects now have detailed execution plans ready to deploy on user signal
