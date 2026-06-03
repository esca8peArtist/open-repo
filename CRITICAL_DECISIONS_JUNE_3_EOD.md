# Critical User Decisions — June 3 EOD Deadline

**Deadline**: 23:59 UTC today (June 3, 2026)  
**Current time**: 13:15 UTC  
**Time remaining**: 10 hours 44 minutes

Three major projects have reached decision gates that unlock downstream work. All decisions gate significant autonomous pipeline work. **Recommend reviewing and deciding by 18:00 UTC to allow orchestrator time to execute any follow-up actions today.**

---

## 1. mfg-farm — Test Print Execution

### Current Status
- **All pre-launch preparation COMPLETE**: launch sequence framework production-ready, SEO strategy locked, competitive analysis done, pricing and supply chain planned
- **Blocking item**: Single test print required to validate snap-arm tolerance (1.4mm is highest-risk feature)
- **Deliverables ready**: `ETSY_LAUNCH_SEQUENCE_AND_CHECKLIST.md` (5,500+ words, production-ready), `PRODUCTION_FARM_SCALING_STRATEGY.md` (12-month roadmap with unit economics, facility constraints, ROI analysis)

### What Needs to Happen
Execute single test print with specifications:
- **Layer height**: 0.20mm
- **Material**: PLA+
- **Walls**: 3
- **Temperature**: 220–225°C

**Evaluation**: Report snap-arm clearance against FDM_TOLERANCE target. Outcome determines launch timeline:
- **PASS**: Proceed to May 25–30 pre-launch shop setup (already documented)
- **PASS-WITH-ADJUSTMENTS**: Retune in 1–2 iterations, launch delayed 3–5 days
- **FAIL**: Design revert required; assess whether to redesign or pivot to different product
- **PARTIAL-FAIL**: Limited scope re-iteration; minimal delay

### Impact of Decision
**If executed by June 5**: Launch readiness → Phase 1 (June 3–15 execution) → Phase 2 (2nd printer + Amazon FBA, July) → Phase 3 (laser engraving, Aug)  
**If delayed past June 10**: Push to Phase 1 v2 (late June) — acceptable but loses June 3–15 market momentum  
**If decided NOT to execute**: Pivot required (product selection or manufacturing method change)

### Recommendation
**EXECUTE test print by June 6**. Unit economics are solid (68.6–70.9% gross margin across all scales, 11–21 day payback per printer). Only unknown is snap-arm tolerance. Test print provides the data to de-risk and proceed with confidence.

**Timeline impact**: Orchestrator can execute Phase 1 (launch sequence + shop setup) while test print cures (24–48h), parallelizing work.

---

## 2. seedwarden — Track A vs Track B vs Both

### Current Status
- **Gate 1 launch materials COMPLETE**: All 8 zone PDFs, 5 email bodies, 15 influencer contacts, 18 social post drafts, logo, 8 companion runbooks verified production-ready (Session 2505 dry-run verification)
- **Track A** (Etsy-first, search traffic): June 1 target (past deadline but materials ready)
- **Track B** (audience-first social→lead magnet→email→Etsy): June 5 target, **3-day margin still available**
- **BOTH** (dual execution): Parallel June 1 (Track A) + June 5 (Track B), different audiences, no conflict

### What Each Track Means

| Factor | Track A (Etsy-first) | Track B (Audience-first) | BOTH |
|--------|----------------------|--------------------------|------|
| **Audience** | Etsy search traffic (organic, low intent) | Foragers/homesteaders (social, high intent) | Both simultaneously |
| **Entry point** | Etsy listing + PPC ads | Instagram/TikTok post + lead magnet | Dual entry |
| **Timeline** | June 1 execution (overdue but ready) | June 5 execution (in window) | June 1 + June 5 parallel |
| **Effort** | ~2 hrs/day for 5 days (shop setup, PPC) | ~3 hrs/day for 7 days (social scheduling, email sequence) | ~5 hrs/day for 5–7 days (both) |
| **Risk** | Lower intent audience; longer conversion | Higher intent; faster feedback | Requires attention to both channels |
| **Phase 3 audience** | New: Medicinal herbs buyers | Aligned: Homesteaders → medicinal herbs | Both positions for Phase 3 |

### Impact of Decision

**Track A only**: Single channel, predictable but slower traction (may miss Phase 2 momentum). Phase 3 requires rebuilding audience.

**Track B only**: Skip Etsy first-mover advantage. Audience-first is lower-risk but less SEO leverage.

**BOTH (recommended)**: Parallel execution June 1 (Track A shop setup) + June 5 (Track B social). Different audiences mean complementary reach. Phase 3 (June 22) benefits from dual-channel funnel already warmed.

### Recommendation
**EXECUTE BOTH, staggered**:
1. **June 1**: Track A shop setup (Etsy listing, PPC baseline) — orchestrator can execute while you manage manual steps
2. **June 5**: Track B launch (social posts, lead magnet, email sequence) — 3-day margin preserved
3. **Phase 2 benefit**: Dual funnels enable A/B testing (which audience converts better? which source scales?)

**Timeline impact**: Gate 1 materials are production-ready. Decision unlocks immediate orchestrator execution of all distribution prep.

---

## 3. systems-resilience — Platform Choice (Nextcloud+Matrix vs Discourse)

### Current Status
- **Phase 6 platform analysis COMPLETE**: Nextcloud+Matrix recommended 9.5/10, Discourse secondary 8.0/10
- **Phase 7 pilot implementation roadmap COMPLETE**: Governance as pilot entry point, 80–150 person optimal community size
- **User decision required**: Platform selection → Phase 5 Wave 1 author recruitment June 5

### Platform Comparison

| Factor | Nextcloud+Matrix | Discourse |
|--------|------------------|-----------|
| **Offline capability** | FULL (LoRa meshtastic bridge June 2026) | None (requires internet) |
| **Cost** | $0–180/year | $84–204/year |
| **Setup time** | 8–10 hours | 2–3 hours |
| **Collaborative editing** | Real-time (via Collabora) | Asynchronous only |
| **Self-governance** | Manual (file permissions) | Trust-level automation |
| **REST API** | Full (both Nextcloud + Matrix) | Full (Discourse) |
| **For Phase 5 Wave 1** | Flexible, can run offline workshops | Requires cloud hosting |
| **For Phase 7 pilots** | Resilience to infrastructure failure | Fragile (single point of failure) |
| **Recommendation score** | 9.5/10 | 8.0/10 |

### Phase 5 Wave 1 Impact (June 5 onward)
- **Nextcloud+Matrix choice**: Enables recruitment of "offline-capable" communities (rural, indigenous, resilience-focused). Aligns with Phase 7 philosophy (governance that works when infrastructure fails).
- **Discourse choice**: Faster setup, simpler for traditional urban organizing. Requires reliable internet (limits Phase 7 applicability).

### Pilot Timeline (Month 1–3)
- **Month 1 (June)**: Author recruitment, platform setup, 20–30 person pilot launch
- **Month 2–3 (July–Aug)**: Governance testing, feature validation, scale to 80–150 persons
- **Platform differences materialize**: Month 3–5 (when you test offline capability, collaborative editing, resilience scenarios)

### Recommendation
**CHOOSE NEXTCLOUD+MATRIX**. 

**Reasoning**:
1. **Higher score** (9.5 vs 8.0) and platform-agnostic architecture
2. **Offline-first design** aligns with Phase 7 (building systems that survive infrastructure collapse)
3. **Real-time collaborative editing** enables better Phase 5 author experience (writing governance documents together in real-time)
4. **June 5 Wave 1 author recruitment** benefits from messaging: "We're piloting offline-capable organizing infrastructure"
5. **7-day setup buffer**: Even with 8–10 hour setup, you can complete by June 12, leaving time for pilot recruitment/launch

**Setup contingency**: If you prefer simpler setup, Discourse is viable but accept 1-point lower score and future pivot cost if Phase 7 pilots require offline capability.

---

## Timeline Dependencies & Orchestrator Execution Plan

Once decisions are made, orchestrator execution order:

### Immediate (June 3–4, today + tomorrow)
1. **mfg-farm**: If test print approved, prep Phase 1 execution sequence (shop setup, PPC baseline)
2. **seedwarden**: Deploy Track A or B or BOTH launch execution immediately (all materials ready)
3. **systems-resilience**: Recruit Phase 5 Wave 1 authors (updated with platform choice)

### June 5
1. **mfg-farm**: Monitor test print cure (24–48h), prepare to route outcome (PASS/FAIL/ADJUSTMENTS)
2. **seedwarden Track B**: If BOTH chosen, execute June 5 social launch
3. **systems-resilience**: If Nextcloud+Matrix chosen, begin platform setup (target completion June 12)

### June 15 checkpoint
1. **mfg-farm**: Test print outcome → decide launch date (June 15–25 window)
2. **seedwarden**: Measure Track A/B performance (open rates, click rates, conversion %)
3. **systems-resilience**: Phase 5 Wave 1 pilot recruitment + platform setup 50% complete

### Impact if decisions delayed past June 3 EOD
- **mfg-farm**: Loss of June 3–15 momentum (still recoverable; pushes to late June)
- **seedwarden**: Pushes Track B to June 10+ (acceptable but loses 5-day social momentum)
- **systems-resilience**: Delays Phase 5 Wave 1 launch past June 5 (loses June cohort, next cohort July)

---

## Recommendation Summary

| Project | Decision | Rationale | Urgency |
|---------|----------|-----------|---------|
| **mfg-farm** | Execute test print by June 6 | All prep done; only unknown is snap-arm tolerance | HIGH — momentum window through June 15 |
| **seedwarden** | Execute BOTH tracks staggered (June 1 + June 5) | Different audiences; dual-channel testing; Phase 3 benefit | MEDIUM-HIGH — June 5 margin still available |
| **systems-resilience** | Choose Nextcloud+Matrix | Better score (9.5 vs 8.0), offline-first aligns Phase 7 goal, real-time editing | MEDIUM — June 5 Wave 1 recruitment unlocks autonomously |

**Recommend deciding by 18:00 UTC** to allow orchestrator time to execute any follow-up actions today (June 3).

---

## How to Confirm Decisions

Reply in Discord / email / CHECKIN.md with format:
```
mfg-farm: [EXECUTE / DEFER / DECIDE_LATER]
seedwarden: [TRACK_A_ONLY / TRACK_B_ONLY / BOTH]
systems-resilience: [NEXTCLOUD_MATRIX / DISCOURSE]
```

Once confirmed, orchestrator will execute all downstream work automatically (no further decisions required until June 15 checkpoint).
