---
title: "Synthesis Automation Runbook — May 25 Re-Synthesis Routing"
created: 2026-05-23
version: 1.0
authority: synthesis-outcome-router.py + post-synthesis-contingency-execution-playbooks.md
---

# Synthesis Automation Runbook

## Overview

On **May 25, 2026 at 20:00 UTC**, the Wave 1 synthesis will execute (if signal log is complete). This runbook describes how the synthesis outcome is automatically routed to the correct contingency execution path, with manual override options if needed.

**Automation timeline**:
- **May 25 19:00–20:00 UTC**: synthesis-execution-monitor.py runs and produces synthesis-execution-output.md with classification
- **May 25 20:15 UTC**: synthesis-outcome-router.py automatically detects synthesis completion and routes outcome
- **May 25 20:15–23:00 UTC**: Orchestrator executes immediate actions per contingency path
- **May 25 23:59 UTC**: All immediate actions complete; contingency path activated

---

## Automated Execution Flow

### Step 1: Synthesis Execution (May 25 20:00 UTC)

`synthesis-execution-monitor.py` runs automatically and produces:
- **synthesis-execution-output.md** — Classification (STRONG/MODERATE/WEAK/TOO_EARLY/DELIVERY_PROBLEM)
- **synthesis-execution-log.txt** — Run log entry
- **Terminal report** — Per-contact status and routing decision

### Step 2: Outcome Routing (May 25 20:15 UTC)

`synthesis-outcome-router.py` reads synthesis outcome and:
1. **Validates signal log** — checks that all [fill] fields are completed
2. **Reads classification** — extracts from synthesis-execution-output.md
3. **Routes to contingency path** — selects STRONG/MODERATE/WEAK/DELIVERY_PROBLEM path
4. **Generates activation status** — writes contingency-activation-status.md with immediate actions checklist
5. **Logs routing decision** — appends to synthesis-outcome-routing-log.txt

### Step 3: Immediate Actions (May 25 20:15–23:00 UTC)

Orchestrator executes the immediate actions checklist from contingency-activation-status.md:
- For **STRONG**: Pre-stage Domains 57+59, confirm Domain 39 ready, refresh Tier 2 list
- For **MODERATE**: Pre-stage Domain 57 primary + Domain 59 secondary tracks
- For **WEAK**: Audit delivery, pre-stage Domains 38-40 alternative path
- For **DELIVERY_PROBLEM**: Fix email infrastructure, re-test delivery
- For **TOO_EARLY**: Fill remaining signal log data, wait for May 25 gate closure

### Step 4: Status Reporting (May 25 23:00 UTC)

Updates CHECKIN.md and BLOCKED.md to document:
- Synthesis outcome classification
- Contingency path selected
- Immediate actions completed
- Next milestones and Phase 2 launch dates

---

## Manual Execution (If Automatic Fails)

If synthesis doesn't run automatically on May 25, manually execute the routing:

### Option A: Run synthesis first, then route

```bash
# Step 1: Run synthesis if it hasn't executed
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research
uv run python synthesis-execution-monitor.py

# Step 2: Route the outcome
uv run python synthesis-outcome-router.py
```

### Option B: Manual outcome override (for testing or emergency)

```bash
# Override with a specific outcome (STRONG, MODERATE, WEAK, etc.)
uv run python synthesis-outcome-router.py --outcome STRONG

# Dry-run first to preview without writing files
uv run python synthesis-outcome-router.py --outcome MODERATE --dry-run
```

### Option C: Check current routing status

```bash
# View the current contingency activation status
cat contingency-activation-status.md

# View routing log
cat synthesis-outcome-routing-log.txt

# View synthesis outcome
cat synthesis-execution-output.md
```

---

## Contingency Paths — Quick Reference

### STRONG (>40% engagement)

**Immediate next step**: Tier 2 Week 5 activation (June 15-21)

**Immediate actions checklist** (5 items, ~3 hours):
1. Verify signal log contains all 5 contact scores
2. Pre-stage Domains 57+59 working documents
3. Verify all primary sources live
4. Create writing schedule (55-65h D59 + 45-51h D57)
5. Confirm Domain 39 production-ready for June 1

**Phase 2 timeline**:
- June 15: Domain 57 + Domain 59 research launch
- Aug 10: Both domains complete
- Aug 1-31: Distribution to primary audiences
- June 15-21: Tier 2 activation

**Risk level**: MEDIUM (protected writing blocks required; OBBBA data dependency)

---

### MODERATE (25-40% engagement)

**Immediate next step**: Domain 57 primary track (June 10 start)

**Immediate actions checklist** (7 items, ~4 hours):
1. Verify signal log with 1-2 substantive replies OR 2-3 Gist clicks
2. Pre-stage Domain 57 working documents
3. Verify all 21 primary sources
4. Create 46-52h writing schedule for Domain 57
5. Verify OBBBA+Medicaid sources for Domain 59
6. Create 45-55h writing schedule for Domain 59 (July 1 start)
7. Note which sector underperformed; adjust Tier 2 messaging

**Phase 2 timeline**:
- June 10: Domain 57 primary track launch
- July 1: Domain 59 secondary track launch
- Aug 10: Domain 57 complete
- Aug 1: Domain 59 complete
- June 22-28: Tier 2 activation (adjusted messaging)

**Risk level**: LOW

---

### WEAK (<25% engagement)

**Immediate next step**: Delivery audit + alternative domains (38-40)

**Immediate actions checklist** (7 items, ~5 hours):
1. Run delivery self-test if not done
2. Confirm inbox delivery (not spam)
3. Determine: delivery problem or content problem
4. Confirm Domain 39 production-ready for June 1 HHS deadline
5. Pre-stage Domain 38 (AI Regulatory Capture) production plan
6. Pre-stage Domain 40 (Surveillance Capitalism) production plan
7. Adjust Phase 2 domain sequence per weak-outcome timeline

**Phase 2 timeline**:
- June 1: Domain 39 distribution (HHS deadline)
- June 1-15: Domain 38 production (AI)
- June 22-July 15: Domain 40 production (Surveillance)
- June 29-July 5: Tier 2 activation (contingent on D39 signal)

**Risk level**: HIGH (requires messaging pivot)

---

### DELIVERY_PROBLEM (test email in spam)

**Immediate next step**: Email infrastructure fix

**Immediate actions checklist** (6 items, ~2 hours, urgent):
1. DO NOT REVISE CONTENT — this is delivery, not content
2. Check domain/IP reputation (MXToolbox, Google Postmaster)
3. Verify SPF/DKIM/DMARC alignment
4. Test Gist URL domain reputation
5. Verify sender email address (not brand-new account)
6. Re-run delivery self-test after fixes

**Phase 2 timeline**:
- On hold pending delivery fix
- Estimated fix time: 24-48 hours
- Resume synthesis outcome classification once inbox delivery confirmed

**Risk level**: CRITICAL (blocks all Phase 2 activation)

---

### TOO_EARLY (signal log incomplete)

**Immediate next step**: Complete signal log by May 25 18:00 UTC

**Immediate actions checklist** (5 items, ~1 hour):
1. Fill any remaining [fill] fields in signal log with May 22-25 data
2. Re-run synthesis-execution-monitor.py on May 25 20:00 UTC
3. Ensure all 5 contacts have had at least 7 days (May 18-25)
4. Check for late-arriving Score 3+ replies
5. Re-run synthesis-outcome-router.py at May 25 20:15 UTC

**Phase 2 timeline**:
- On hold pending May 25 gate closure
- Gate closure: May 25 23:59 UTC
- Resolution: Complete 7-day signal collection, re-run synthesis

**Risk level**: MEDIUM (time-dependent; gate closes May 25)

---

## Edge Cases & Troubleshooting

### Edge Case 1: Signal log incomplete on May 25 20:00 UTC

**Symptom**: Synthesis runs but produces TOO_EARLY outcome (incomplete signal log)

**Solution**:
1. Fill any remaining [fill] fields with May 23-25 data
2. Re-run synthesis: `uv run python synthesis-execution-monitor.py`
3. Re-run router: `uv run python synthesis-outcome-router.py`
4. New classification should be STRONG/MODERATE/WEAK (not TOO_EARLY)

**Timeline**: Can be resolved within 30 minutes if data is available

---

### Edge Case 2: Synthesis doesn't run automatically

**Symptom**: May 25 20:15 UTC passes; no synthesis-execution-output.md

**Solution**:
1. Check signal log completion: `grep -c '\[fill\]' wave-1-signal-log-may18-21.md`
2. If unfilled > 0: fill fields first
3. Run synthesis manually: `uv run python synthesis-execution-monitor.py`
4. Run router manually: `uv run python synthesis-outcome-router.py`

**Timeline**: Can be resolved within 1 hour

---

### Edge Case 3: Classification is STRONG/MODERATE/WEAK but signal log still has [fill] fields

**Symptom**: Router runs with valid signal log but produces WARN_SIGNAL_LOG_INCOMPLETE warning

**Solution**:
1. Verify signal log manually: `head -50 wave-1-signal-log-may18-21.md`
2. Count [fill] fields: `grep -c '\[fill\]' wave-1-signal-log-may18-21.md`
3. If >0 unfilled fields: review which sections are incomplete
4. May 21 snapshot section can be missing (classification is still valid if contact data is complete)
5. Proceed with contingency actions but note advisory in CHECKIN.md

**Timeline**: Proceed immediately; advisory is informational only if contact data is complete

---

### Edge Case 4: Need to override outcome for testing

**Symptom**: Want to test contingency path without waiting for May 25 synthesis

**Solution**:
```bash
# Test STRONG path
uv run python synthesis-outcome-router.py --outcome STRONG --dry-run

# Test MODERATE path and write files
uv run python synthesis-outcome-router.py --outcome MODERATE

# Test DELIVERY_PROBLEM path
uv run python synthesis-outcome-router.py --outcome DELIVERY_PROBLEM --dry-run
```

**Note**: Manual overrides are logged separately in synthesis-outcome-routing-log.txt with note "SOURCE: MANUAL OVERRIDE"

---

### Edge Case 5: Delivery problem detected; need to fix and re-route

**Symptom**: Classification is DELIVERY_PROBLEM; test email landed in spam

**Solution**:
1. Follow "DELIVERY_PROBLEM" immediate actions: fix SPF/DKIM, test reputation tools
2. Re-run delivery self-test when fixed
3. Once inbox delivery confirmed, manually override:
   ```bash
   uv run python synthesis-outcome-router.py --outcome MODERATE
   ```
4. Continue with MODERATE contingency path (or STRONG/WEAK as appropriate)

**Timeline**: 24-48 hours for email infrastructure fix + re-route

---

## Safety Checks

### Pre-synthesis Safety (May 25 19:00 UTC)

Before synthesis-execution-monitor.py runs, verify:
- [ ] Signal log is in correct location: `projects/resistance-research/post-wave-1-monitoring/wave-1-signal-log-may18-21.md`
- [ ] Signal log has contact data (not just [fill] placeholders)
- [ ] synthesis-execution-monitor.py is executable: `chmod +x synthesis-execution-monitor.py`
- [ ] synthesis-outcome-router.py is executable: `chmod +x synthesis-outcome-router.py`
- [ ] All five contact email addresses are current (verify in PHASE_1_DISTRIBUTION_BATCH_1.md)

### Post-synthesis Safety (May 25 20:15 UTC)

Before executing contingency immediate actions, verify:
- [ ] synthesis-execution-output.md exists and is valid
- [ ] contingency-activation-status.md was generated (no errors)
- [ ] Classification is one of: STRONG, MODERATE, WEAK, DELIVERY_PROBLEM, TOO_EARLY
- [ ] Signal log completeness matches classification (if TOO_EARLY, confirm why)
- [ ] Immediate actions checklist is clear and unambiguous

### Rollback Safety

If any immediate action fails:
1. Log the failure in contingency-activation-status.md with timestamp
2. Do NOT delete synthesis-execution-output.md or contingency-activation-status.md
3. Fix the specific failure (check error message)
4. Re-run the failed action
5. Update CHECKIN.md with "Immediate action retry — {action name} — completed successfully"

---

## Files Reference

| File | Purpose | Generated by | Read by |
|------|---------|--------------|---------|
| wave-1-signal-log-may18-21.md | Signal data (user-filled) | User | synthesis-execution-monitor.py |
| synthesis-execution-monitor.py | Synthesis classifier | Orchestrator (Session 1454) | (standalone) |
| synthesis-execution-output.md | Synthesis outcome | synthesis-execution-monitor.py | synthesis-outcome-router.py |
| synthesis-execution-log.txt | Synthesis run log | synthesis-execution-monitor.py | (reference) |
| synthesis-outcome-router.py | Outcome routing automation | Orchestrator (Session [current]) | (standalone) |
| contingency-activation-status.md | Routing decision + actions | synthesis-outcome-router.py | Orchestrator / User |
| synthesis-outcome-routing-log.txt | Routing run log | synthesis-outcome-router.py | (reference) |
| post-synthesis-contingency-execution-playbooks.md | Contingency actions (manual) | Orchestrator (Session 1472) | (reference) |

---

## Success Criteria

After May 25 synthesis + routing + immediate actions, verify:
- [ ] contingency-activation-status.md is complete and accurate
- [ ] synthesis-outcome-routing-log.txt has an entry for May 25 execution
- [ ] CHECKIN.md updated with synthesis outcome and contingency path
- [ ] All immediate actions in checklist are marked [x] (completed)
- [ ] No unresolved [FILL] fields in contingency-activation-status.md
- [ ] BLOCKED.md updated (if DELIVERY_PROBLEM or TOO_EARLY, block to BLOCKED.md; if STRONG/MODERATE/WEAK, resolve any prior blocks)

---

## Who Executes What

| Actor | Task | Timeline |
|-------|------|----------|
| Orchestrator (async) | synthesis-execution-monitor.py | May 25 20:00 UTC |
| Orchestrator (async) | synthesis-outcome-router.py | May 25 20:15 UTC |
| Orchestrator (human) | Execute immediate actions | May 25 20:15–23:00 UTC |
| Orchestrator (human) | Update CHECKIN.md + BLOCKED.md | May 25 23:00–23:59 UTC |
| Subagent or Orchestrator | Phase 2 domain research | Domain launch dates (June 1+) |
| Orchestrator | Tier 2 activation | Tier 2 activation date |

---

## Manual Control

If automation fails at any step, manual control options:

```bash
# Manual synthesis execution
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research
uv run python synthesis-execution-monitor.py

# Manual routing execution
uv run python synthesis-outcome-router.py

# Manual outcome override (for testing or emergency)
uv run python synthesis-outcome-router.py --outcome STRONG

# Check current status
cat contingency-activation-status.md
cat synthesis-outcome-routing-log.txt
```

---

## Questions & Support

If automatic routing fails or produces unexpected results:
1. Check contingency-activation-status.md for detailed routing decision
2. Check synthesis-outcome-routing-log.txt for run history
3. Run manual syntax check: `uv run python synthesis-outcome-router.py --dry-run`
4. Contact orchestrator with actual classification + error message

---

*Last updated: 2026-05-23*
*Authority: synthesis-outcome-router.py (this session) + post-synthesis-contingency-execution-playbooks.md (Session 1472)*
