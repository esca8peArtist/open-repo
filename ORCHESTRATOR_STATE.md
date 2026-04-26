# Orchestrator State
> Auto-generated at 2026-04-26T23:03:48Z — do not edit. Source: PROJECTS.md, WORKLOG.md, BLOCKED.md, INBOX.md.

## Usage
🟢 Usage: Sonnet 47.5% (2,386,251 tokens) | All-models 42.9% | Reset in 25h | check: claude.ai → Settings → Usage & billing

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

## Active Projects
### mfg-farm
**Status**: Active — ready to prototype
**Focus**: Session 291: **Business plan COMPLETE** (`business-plan.md`). **CadQuery parametric designs COMPLETE** (`cadquery/modrun_rail.py`, `cadquery/modrun_clip.py`). Market research + competitive analysis were already complete (`market-research.md`). Etsy and Amazon listing copy already complete (`etsy-lis
**Blocked**: Test print (user action required — see focus above)

### resistance-research
**Status**: Active — Phase 1-5 COMPLETE, **Phase 4 Integration COMPLETE (Session 494)** — Full proposal synthesis ready
**Focus**: **Phase 4 Integration COMPLETE (Session 494)**. All Phase 4 documents (power-mapping, parallel-institutions, elite-capture-case-study, comparative-democratic-recovery) seamlessly woven into Part III of democratic-renewal-proposal.md. Proposal now contains complete pathway: diagnosis (Domains 1-22) �

### cybersecurity-hardening
**Status**: Active — **TIER 1 DISTRIBUTION PREP COMPLETE** (Session 465), ready for user execution
**Focus**: Session 465 (2026-04-26): **TIER 1 DISTRIBUTION PREP COMPLETE**. Agent-created TIER1_DISTRIBUTION_PREP.md (358 lines) consolidates all distribution materials: 8 Tier 1 organizations (5 legal aid + 3 community org networks), 3 email templates (legal aid, community orgs, mutual aid networks), 5-step e

### stockbot
**Status**: Active — paper trading live, **strategy optimization COMPLETE**, ready for monitoring + live trading launch
**Focus**: Paper trading running (AAPL_h10_lgbm_ho stacker). **All three strategy optimization tasks COMPLETE** (Sessions 488-489). AAPL_h10_lgbm_ho validation plan in place, monitoring script deployed, live trading readiness checklist ready. **Next**: Monitor paper trading daily, assess progress toward Gate 1

### seedwarden
**Status**: Active — Phase 1 upload pending user tag corrections; **Phase 2 mockup tooling COMPLETE**
**Focus**: **Two parallel tracks:**
**Blocked**: Tag corrections + Etsy account verification (user action, Track A only). Track B has no blockers.

### open-repo
**Status**: Active — Phase 4 COMPLETE, **PR #1 open, awaiting review/merge** (Session 486: 2026-04-26)
**Focus**: **PR #1 OPEN** (2026-04-26): https://github.com/esca8peArtist/open-repo/pull/1

### off-grid-living
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Focus**: **GitHub Publication COMPLETE (Session 486)**. All tasks executed:

### workout
**Status**: Active
**Focus**: `comprehensive-plan.md` (1,053 lines) complete — covers all 3 equipment tiers (no equipment, bands, full gym) × multiple frequencies (3/4/5/6 days), with full exercise libraries, progression systems, calisthenics skill ladders, and mobility protocols. Awaiting user review and selection.
## Active Blocks
### mfg-farm — Test print required before launch prep continues
**Date blocked**: 2026-04-12
**Context**: Business plan, CadQuery designs (modrun_rail.py, modrun_clip.py), market research, and listing copy are all complete. Orchestrator cannot proceed with launch prep until a physical test print confirms the designs are printable.
**What I need**: Run a test print of the CadQuery rail and clip designs and confirm they printed correctly.
**Verify with**: `# manual — cannot auto-verify`
**Resolution**:
---

## Inbox (unprocessed)
*(no new items)*

## Recent Log (last 40 lines of WORKLOG.md)
     - Mitigation: international accountability, federal defection support, sanctuary networks, armed resistance preparation (last resort)
   - **Resource risks** (funding cuts, movement collapse)
     - Mitigation: diversified funding architecture, grassroots fundraising, alternative economy development
   - **External risks** (international interference)
     - Mitigation: international coalition building, ally coordination, domestic resilience narrative
   - Total estimated mitigation cost: $400-600M over 5-year recovery period ($80-120M/year)
     - For context: single presidential campaign spends $500M+; Democratic party 2024 spending exceeded $2.5B

**Confidence Assessment**: 0.95 (95%)
- ✅ No duplicates (Phase 5 never attempted before)
- ✅ Architecture compliance (follows Phase 3-4 template, markdown format)
- ✅ Official documentation verified (Phase 4 docs, comparative case studies, movement research archive)
- ✅ Working OSS implementations referenced (Poland 2023, Brazil 2022, South Africa transition models)
- ✅ Root cause identified (Phase 5 scope explicit in PROJECTS.md)

**Integration Status**:
- Phase 5 documents created in `/projects/resistance-research/`
- Synthesized from: Phase 4 documents (power-mapping, parallel-institutions, elite-capture, comparative-recovery), democratic-renewal-proposal.md, resistance research archive (160+ movement case studies), comparative democratic transition literature
- These documents should be integrated into the democratic-renewal-proposal.md as Part III (Theory of Change) and Part IV (Implementation Architecture) in next phase

**Next Steps**:
- Integration into main proposal document (next phase work)
- Distribution preparation: existing templates ready for user posting (Substack, Reddit, institutional outreach)
- Tracker updates: first-amendment, environmental-rollbacks, police-brutality trackers ready for regular maintenance

**Token Usage**: ~45,000 (confidence check + 4 Phase 5 documents)

## 2026-04-26 — cybersecurity-hardening — Device Hardening Guide (iOS + Android)

**File created**: `/projects/cybersecurity-hardening/device-hardening-guide.md`

**Summary**: Comprehensive device hardening guide for iOS and Android against government-level surveillance. Covers: iPhone iCloud/ADP threat model, airplane mode vs power-off RF analysis (Find My BFU Bluetooth beacon behavior), Lockdown Mode, SIM swapping countermeasures, Faraday pouch use cases, device compartmentalization. Android: GrapheneOS vs CalyxOS vs stock Android with documented threat-model tradeoffs, bootloader re-lock requirement (the critical security paradox of custom ROMs), BFU/AFU forensic extraction states, F-Droid security issues vs Play Store. Cross-platform: power-off decision matrix, compartmentalization profile table, backup strategy by tier, crisis protocol. Sources include Apple law enforcement guidelines (October 2025), leaked Cellebrite support matrix (February 2025), GrapheneOS documentation, EFF SSD, privsec.dev, academic forensics research.

**Key findings**:
- iCloud without Advanced Data Protection is the most productive law enforcement target against iPhone users — ADP removes Apple's ability to comply with warrants
- Modern iPhones continue Bluetooth beaconing after power-off if Find My is enabled; only disabling Find My before shutdown provides full RF silence
- GrapheneOS re-locks the bootloader after installation — this is what makes it forensically durable; CalyxOS/LineageOS with unlocked bootloaders are weaker than stock Android
- BFU state (before first unlock) is the critical protection posture; power off before potential seizure
- F-Droid has documented infrastructure vulnerabilities (outdated servers, no TLS pinning, slow updates) that make it weaker than Play Store for security-focused users
