# Exploration Queue

Active research items for advancing project Goals beyond current deliverables.

## Active Items

### 1. Resistance-Research Post-Deployment Measurement Framework
**Status**: Pending
**Project**: resistance-research
**Context**: Phase 2 research (35+ domains) is production-ready and awaiting user distribution decisions. However, the project Goal includes "tracking and understanding the specific crises the United States is currently facing, finding actionable responses." Post-deployment, we need a measurement framework to track advocacy window outcomes, constituency adoption, and policy impact.
**Research questions**:
- What are the Phase 1 success metrics across 7 constituencies (law schools, immigration, civil rights, academic, faith, labor, mutual aid)?
- How do we track policy wins (introduced bills, hearing testimony, regulatory action) back to domain distribution efforts?
- What's the minimal viable analytics infrastructure (Google Forms, Sheets, Bitly, email tracking)?
- Timeline: Can this be built in parallel with Phase 1 distribution, or must it wait?

**Suggested output**: `PHASE_1_MEASUREMENT_FRAMEWORK.md` (2,000-3,000 words, success metrics by constituency, daily/weekly/monthly tracking checklist, contingency escalation triggers)

**Priority**: Medium (only if user approves Phase 1 distribution before June 3)
**Tags**: #measurement #advocacy-ops #phase-1-critical-path

---

### 2. Seedwarden Track B Execution & Gate 1 Launch Readiness Verification
**Status**: Pending
**Project**: seedwarden
**Context**: Gate 1 infrastructure verified (Session 2552), but Track B has its own 5-gate sequence. Track B launch target May 30 (already passed — need current status). Research the full execution checklist, identify any blocking items beyond the documented Track A blockers, and map the path to Gate 2.
**Research questions**:
- What's the current status of Track B launch? Is May 30 deadline firm or has it shifted?
- Are there any Track B-specific blockers beyond what's documented in `TRACK_A_BLOCKER_RESOLUTION.md`?
- What does the full 5-gate sequence look like for Track B?
- Timeline: When can Gates 2-5 execute relative to June 22 – July 13 (Phase 3 assets)?

**Suggested output**: `TRACK_B_EXECUTION_CHECKLIST.md` (500-800 words, gate sequence, timeline, blockers, decision tree for Gate 1 pass/fail)

**Priority**: High (June 1 decision deadline for Track B activation)
**Tags**: #seedwarden-gates #launch-readiness #user-decision-required

---

### 3. Systems-Resilience Phase 7: Community Pilot Implementation Roadmap
**Status**: Pending
**Project**: systems-resilience
**Context**: Phase 6 (platform analysis + implementation guides) is complete. But the project Goal is to provide "resilience solutions at scale." Phase 7 should map the path to actual community deployment. What would a pilot look like? What's the minimal viable community? Timeline to production?
**Research questions**:
- Which of the 5 community-scale domains would make the best pilot (governance, food systems, information, security, scaling)?
- What community size/type is optimal for a pilot (100-person mutual aid network, 1000-person town, 10K-person watershed district)?
- What's the 6-month timeline from pilot site selection to operational infrastructure deployment?
- How do the platform choices (Discourse vs. Mighty Networks vs. Nextcloud) impact pilot complexity and cost?

**Suggested output**: `PHASE_7_PILOT_IMPLEMENTATION_ROADMAP.md` (3,000-4,000 words, domain selection, community selection criteria, timeline, cost modeling, risk assessment)

**Priority**: Medium (Phase 6 author decision gate June 3 may approve Phase 7)
**Tags**: #community-resilience #implementation #phase-7

---

### 4. Mfg-Farm Full Production Farm Scaling Strategy (Pending Test Print)
**Status**: Pending (blocks on test print execution, but research can proceed)
**Project**: mfg-farm
**Context**: Test print is blocked on user action (May 22-23 target), but the project Goal includes "path to a full print farm" and "scaling roadmap from single printer to multi-printer farm." Once test print results are known, the scaling strategy must be ready immediately. Research this now so execution can begin June 3.
**Research questions**:
- What's the breakeven point for a 2-printer vs. 1-printer operation (unit economics, labor, material costs)?
- What are the facility constraints (space, electrical, cooling, noise) for 2, 5, 10-printer farms?
- How does adjacent manufacturing (laser, CNC, resin) fit into the scaling roadmap? Bundled or separate?
- What's the optimal order: Etsy scale to $10K/mo → add Amazon → scale to 5 printers → add adjacent manufacturing?

**Suggested output**: `PRODUCTION_FARM_SCALING_STRATEGY.md` (3,000-4,000 words, unit economics per printer count, facility planning, adjacent manufacturing ROI, 12-month execution roadmap post-test-print)

**Priority**: High (needed for June 3 launch decision if test print passes)
**Tags**: #mfg-farm-scaling #production-ops #unit-economics

---

### 5. Cybersecurity-Hardening Threat Model Update: Q2 2026 Developments
**Status**: Pending (blocks on VeraCrypt restart, but research can proceed)
**Project**: cybersecurity-hardening
**Context**: Phase 1 threat model is production-ready (98% accurate per Session 876). But May-June 2026 is bringing new threat vectors (FBI FACE Services expansion, DHS Mobile Fortify deployment, drone surveillance scaling). Phase 2 scenario playbooks need updated threat intelligence before Tier 2 outreach launches.
**Research questions**:
- What new facial recognition and biometric systems have been deployed by federal/state law enforcement in May-June 2026?
- Are there updated capabilities or contracts for mass surveillance tools (Palantir, CLEAR, geofencing services)?
- What legal precedents have shifted (4th Amendment, electronic surveillance, border searches)?
- Timeline: When does this threat model update need to be complete for Tier 2 launch (~4 weeks post-Phase-1)?

**Suggested output**: `THREAT_MODEL_UPDATE_Q2_2026.md` (2,000-3,000 words, new threat vectors, capability updates, precedent shifts, countermeasure gaps, Tier 2 playbook implications)

**Priority**: Medium (needed for Tier 2 launch in June/July)
**Tags**: #threat-intelligence #surveillance-systems #phase-2-prep

---

## Backlog (Time-gated or externally blocked)

(None currently; all items above are ready for research)

## Completed / Crossed Out

(None yet)

---

## Queue Management Notes

- **Prioritization**: Focus on items supporting near-term user decisions (Track B June 1, mfg-farm June 3, systems-resilience June 3)
- **Autonomy**: All items above can be researched and scoped without user action, though some may need user decision gates to proceed
- **Dependencies**: mfg-farm scaling depends on test print results (user action); others can proceed independently
