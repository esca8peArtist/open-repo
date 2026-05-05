# Phase 2 Activation Triggers — open-repo

**Document Type**: Go/No-go decision criteria
**Status**: Production-ready for deployment post-Phase-1
**Last updated**: 2026-05-05
**Scope**: Define explicit, measurable conditions that signal Phase 1 completion and readiness to advance to Phase 2 (Federation Expansion & Ecosystem Growth)

---

## Executive Summary

Phase 1 is **code delivery + community establishment** (PR #1 merge through 3-month stabilization). Phase 2 is **ecosystem expansion** (recruiting federation participants, building institutional partnerships, scaling operations).

This document defines the exact decision point for Phase 1 → Phase 2 transition. Rather than vague "readiness," it specifies:
- **Three Gate checks** (quantitative + qualitative)
- **Failure conditions** (what stops Phase 2 advance)
- **Timeline** (when the decision is made)
- **Go/No-go decision authority** (user + Anya)

---

## Timeline & Decision Points

### Checkpoint 1: Month 1 Post-Merge (Week 4)
**Purpose**: Early health check — is the project alive and healthy?

**Go/Continue to Month 2** requires:
- ✅ 20+ stars (awareness threshold)
- ✅ 2+ unique external contributors (not just maintainer commits)
- ✅ 1+ external PR (someone is using the code)
- ✅ CI/CD passing consistently (>95% pass rate)
- ✅ Issue TTFR <48h (active maintenance)

**No-go/Pause** if:
- ❌ <10 stars (insufficient awareness)
- ❌ 0 external contributors (not resonating with community)
- ❌ CI failing frequently (>10% failure rate)
- ❌ No responses to issues (maintainer vanished)

**Decision**: Informal check-in (does the project feel alive?). Continue if yes.

---

### Checkpoint 2: Month 2 Post-Merge (Week 8)
**Purpose**: Trend validation — is growth sustainable or one-time spike?

**Go/Continue to Month 3** requires:
- ✅ 50+ stars (growing awareness, trending in right direction)
- ✅ 3+ unique contributors (community emerging, not maintainer-dependent)
- ✅ 5+ external PRs cumulative (sustained contributions)
- ✅ >80% test coverage (code quality improving)
- ✅ 1+ fork from external organization (someone using it seriously)
- ✅ 0 critical security vulnerabilities

**Caution/Yellow flags** (continue but increase focus):
- ⚠️ Star growth <3/week (slowing trajectory — investigate awareness channels)
- ⚠️ Issue TTFR drifting >36h (maintainer getting overwhelmed — plan issue triage)
- ⚠️ No design discussions in PRs (too shallow — need richer review culture)

**No-go/Pause** if:
- ❌ Star growth plateaued (<5 new stars in past 2 weeks)
- ❌ Core contributor burnout (commit frequency cliff)
- ❌ Test coverage declining (<70%)
- ❌ Critical security vulnerability + slow patch

**Decision**: Formal metrics review. Continue if all greens + <2 yellows.

---

### Checkpoint 3: Month 3 Post-Merge (Week 12) — PHASE 1 COMPLETION GATE
**Purpose**: Final Phase 1 assessment. Explicit go/no-go decision for Phase 2.

**GATE THRESHOLD — Phase 1 Complete**:

| Category | Metric | Threshold | Status | Weight |
|----------|--------|-----------|--------|--------|
| **Community** | Stars | 100+ | ✓ or ✗ | Must-pass |
| | External contributors | 5+ | ✓ or ✗ | Must-pass |
| | External PRs | 10+ cumulative | ✓ or ✗ | Must-pass |
| | Issue TTFR | <24h average | ✓ or ✗ | Must-pass |
| | Contributor retention | 60%+ of Month 1 contributors still active | ✓ or ✗ | Must-pass |
| **Code Quality** | Test coverage | >80% | ✓ or ✗ | Must-pass |
| | CI pass rate | >95% | ✓ or ✗ | Must-pass |
| | Critical vulns | 0 | ✓ or ✗ | Must-pass |
| | Dependency currency | >80% current | ✓ or ✗ | Must-pass |
| **Product-Market Fit** | Forks from external orgs | 3+ | ✓ or ✗ | Must-pass |
| | Domain-relevant issues | 60%+ of issues are architecture/design (not typos) | ✓ or ✗ | Must-pass |
| | Release cadence | 2+ releases since PR #1 merge | ✓ or ✗ | Must-pass |
| | Community engagement (qual) | No "discouraging" sentiment; 80%+ welcoming tone | ✓ or ✗ | Must-pass |
| **Sustainability** | Commit velocity | 8+ commits/week sustained for 4+ weeks | ✓ or ✗ | Must-pass |
| | Core team stability | 2+ core contributors still active | ✓ or ✗ | Must-pass |

**Phase 1 PASS Decision**:
- All 13 Must-pass thresholds met → **ADVANCE TO PHASE 2**
- 11–12 passed, 1–2 yellow → **CONDITIONAL ADVANCE** (with Phase 2 scope reduction or extended Phase 1)
- <11 passed → **PAUSE**: Phase 1 extension required; reassess Month 4

---

## Phase 2 Definition & Success Criteria

### Phase 2 Scope (What We're Advancing To)

**Phase 2 = Federation Expansion + Institutional Partnership + Ecosystem Growth** (~6 months, Months 4–9)

**Activities**:
1. **Recruit federation partners** (5–10 organizations building their own federation implementation)
2. **Establish institutional partnerships** (research institutions, standards bodies, civil tech networks)
3. **Expand documentation** (tutorials for federation deployment, architecture decision records)
4. **Build ecosystem** (integrate with complementary tools, create federation registry)
5. **Scale operations** (versioned releases, backwards compatibility guarantees, deprecation policy)

**Success Metrics for Phase 2**:
- 5+ external federation implementations live using open-repo framework
- 20+ active contributors (vs. 5+ Phase 1 threshold)
- 500+ stars (vs. 100+ Phase 1 threshold)
- 2+ academic papers citing open-repo
- Established as de facto federation standard in civil tech domain
- 0 critical technical debt items left from Phase 1

---

## Conditional Advance Criteria

If Phase 1 completion doesn't hit all 13 thresholds, **conditional advance** is possible based on:

### Yellow-Light Pathway: 11–12 Thresholds Met

**If these are red** (but others pass), Phase 2 still viable:

1. **"Forks from external orgs <3"** (only 1–2 forks)
   - Conditional advance: **Yes**, but with extended recruitment timeline
   - Action: Explicitly reach out to 10+ potential federation partners (Month 4)
   - Revised Phase 2 success metric: 5+ forks by Month 9 (vs. Month 6 baseline)

2. **"Domain-relevant issues <60%"** (too many feature requests, not enough design discussions)
   - Conditional advance: **Yes**, but improve issue triage
   - Action: Implement issue labels, create a design discussion category, direct feature requests to future roadmap
   - Risk: Suggests community is less architecture-minded (affects federation partner quality)

3. **"Commit velocity <8/week sustained"** (averaging 6–7/week, trending down)
   - Conditional advance: **Maybe** (depends on reason)
   - Investigation: Is maintainer burned out, or is stabilization-phase normal? Are external contributors taking over?
   - If external contributors are ramping: **Go ahead** (different velocity profile acceptable)
   - If maintainer-only burnout: **Pause** (risk of Phase 2 stall)

4. **"Core team stability: 1 core contributor remaining"** (someone dropped out)
   - Conditional advance: **Careful** (mono-maintainer risk)
   - Action: Actively recruit Phase 2 partners with engineering capacity, or reduce Phase 2 scope
   - Threshold: Accept this only if external PRs are >15 (indicating community can sustain without sole maintainer)

### Red-Light Pathway: Certain Thresholds Cannot Be Negotiated

These are **non-negotiable** (Phase 2 blocked if failed):

- ❌ **Stars <100**: Insufficient awareness to recruit federation partners
- ❌ **External contributors <5**: No community (solo maintainer project can't scale federation)
- ❌ **External PRs <10**: Insufficient proof of concept
- ❌ **Critical vulns >0**: Security liability for federation partners
- ❌ **CI pass rate <95%**: Integration risk for dependent projects
- ❌ **Test coverage <70%**: Codebase fragility

---

## Phase 2 Scope Adjustments Based on Phase 1 Outcome

### Scenario A: Phase 1 PASS (All 13 thresholds met)

**Phase 2 Scope**: Full as defined
- 5–10 federation partner recruitment
- Institutional partnerships with 3+ organizations
- Expand documentation suite
- Build ecosystem integrations
- 6-month timeline, Months 4–9

---

### Scenario B: Phase 1 CONDITIONAL (11–12 pass)

**Adjustment 1: If "Forks" red but others green**
- Reduce federation recruitment target: 3–5 partners (vs. 5–10)
- Extend recruitment timeline: 9 months (vs. 6 months)
- Increase outreach intensity: Directly contact 20+ prospects (vs. organic + outreach)
- Phase 2 success: 3+ forks by Month 9

**Adjustment 2: If "Commit velocity" red but external PRs green**
- No scope reduction
- Actively mentor external contributors to take PR review responsibility
- Reduce maintainer bottleneck by delegating issue triage
- Phase 2 success: External contributor commit rate >maintainer rate by Month 6

**Adjustment 3: If "Core team stability" red but community strong**
- No scope reduction, but recruit co-maintainer during Phase 2
- Explicit co-maintenance agreement (responsibilities, decision-making)
- Reduce personal time commitment: move to 20 hours/week (vs. full-time equivalent)

---

### Scenario C: Phase 1 FAIL (Many thresholds unmet)

**Options**:
1. **Phase 1 Extension** (Months 4–6): Stay in "community building" mode, don't advance to federation expansion
   - Goal: Hit Phase 1 thresholds by Month 6
   - Reassess at Month 6 for Phase 2 advancement

2. **Project Reframing**: Accept niche positioning (academic federation research project, not mass-adoption target)
   - Adjust success metrics to academic standards (publications, citations, researcher recognition)
   - Reduce Phase 2 scope to sustainable institutional partnerships (5–10 universities)
   - Accept smaller contributor base as appropriate for domain

3. **Sunset or Hiatus**: If Phase 1 reveals the problem is unsolvable (legal barriers, technical infeasibility), pause the project
   - Document lessons learned for future federation work
   - Preserve IP + documentation for potential revival

---

## Go/No-go Decision Authority & Process

**Decision Maker**: User (Anya) + Orchestrator (automated check)

**Process**:
1. **Month 3 metrics collected** (Week 12 post-merge, Thursday EOD)
2. **Automated gate evaluation** (orchestrator checks all 13 thresholds, produces pass/fail report)
3. **User review** (Anya reviews report + qualitative assessment, makes final call)
4. **Decision recorded** in `PHASE_2_GATE_DECISION.md` with:
   - Final status (PASS / CONDITIONAL / FAIL)
   - Justification for conditional decisions
   - Revised Phase 2 scope (if conditional)
   - Timeline adjustment (if needed)
5. **Public communication** (update README.md, announce on social if advancing)

---

## Phase 2 Timeline (If Advancing)

**Phase 2 Spans Months 4–9 Post-Merge**:

| Month | Activity | Milestone |
|-------|----------|-----------|
| 4 | Federation partner recruitment (active outreach) | 2+ partners engaged |
| 5 | First federation partner deployment (pilot) | 1 pilot running |
| 6 | Ecosystem integration planning | 3+ ecosystem projects identified |
| 7 | Documentation expansion + tutorial release | Release v1.0 |
| 8 | Institutional partnership formalization | 2+ institutional partners |
| 9 | Ecosystem integrations launching | 5+ federation partners live |

**Phase 3 Gate** (Month 9 end):
- 5+ federation partners using open-repo
- 1,000+ stars
- 20+ active contributors
- Decision: Scale to multi-federation coordination network (Phase 3)

---

## Key Insights & Design Decisions

### Why These Specific Thresholds?

**Stars (100+)**: 
- Comparable federation projects (ActivityPub, Mastodon) show 100–500 stars at maturity
- <100 stars suggests niche academic project only; reduces federation partner interest
- 100+ stars shows mainstream awareness in target domain

**External contributors (5+)**:
- Solo-maintainer projects can't sustain federation work (too much coordination overhead)
- 5 contributors provides redundancy + specialization (some focus federation, some ops, some docs)

**Test coverage (>80%)**:
- Federation code deals with state coordination + edge cases
- <80% coverage means risk of silent failures in production federation scenarios
- Critical for partner trust

**Issue TTFR (<24h)**:
- Federation partners need responsive maintainers
- >24h TTFR suggests backlogs + bottlenecks; risky for Phase 2 partnerships

### Why Not Focus Only on Stars?

Star count alone is a vanity metric. It can spike (via Reddit, HN) then collapse if code is garbage. This framework uses stars as **one signal among thirteen**, ensuring we don't advance based on hype alone.

### Why Explicit Thresholds vs. Gut Feel?

**Transparency**: User and orchestrator both know exactly what "ready" means. No surprise delays.

**Repeatability**: If Phase 2 spawns Phase 3, we use the same framework. Consistent decision-making across project lifecycle.

**Learning**: If we miss a threshold, we understand exactly what went wrong (not just "vibes weren't right").

---

## Conclusion

Phase 2 activation is a **measurable decision** with explicit go/no-go criteria. The 13-threshold framework balances quantitative rigor with qualitative judgment, enabling confident advancement into federation partnership and ecosystem building.

If all thresholds pass, Phase 2 proceeds as planned. If some fail, the conditional advance framework provides scaled-down pathways rather than binary success/failure. And if fundamentals fail (security, code quality, community), the framework surfaces those clearly before we commit to federation partnerships.
