---
title: "Stockbot JPM Model Type Decision Framework"
created: "2026-05-27"
status: "Blocker #2 — User Decision Required"
decision_window: "May 27-28, 2026"
---

# Stockbot JPM Model Type Decision Framework

**Context**: JPM stacker configuration requires a model type decision before Phase 2 activation can proceed. This framework presents both options with tradeoffs so you can decide which is best for your goals.

**Key facts**:
- AMZN is configured and ready: `lgbm_ho` (light gradient boosting, hourly open strategy)
- JPM is blocked: Config specifies `ridge_wf` (linear ridge regression, walk-forward) but only `lgbm_ho` pkl file exists
- Training spec recommends ridge_wf for JPM's return distribution characteristics
- Both models are production-ready; the choice is architectural direction

---

## Option A: Retrain JPM with ridge_wf (Preserves Intended Architecture)

### What you're choosing:
- Honor the original AMZN_JPM_TIER1_TRAINING_SPECIFICATION.md architecture
- AMZN → lgbm_ho (non-linear, adaptive)
- JPM → ridge_wf (linear, mean-reverting model)
- Two fundamentally different model types = architecture diversity test

### Why ridge_wf for JPM (from training spec):
> "JPM's return distribution is more Gaussian and mean-reverting than AMZN's... driven by interest rate cycles, credit spreads, and macro policy rather than product release momentum. The ridge_wf model's linear regression structure matches JPM's predictability pattern."

**Rationale**: JPM's stock price responds to structural factors (Fed rates, credit environment) that are linear. AMZN's price responds to catalyst events (product launches, earnings surprises) that are non-linear. Different models for different regimes.

### Effort required:
- **Time**: ~2-3 hours
- **Steps**:
  1. SSH to Jetson: `ssh -T git@jetson`
  2. Navigate: `cd /opt/stockbot/`
  3. Run training: `uv run python scripts/train_model.py --ticker JPM --model ridge_wf --lookback 60 --walk-forward 10 --output pkl`
  4. Verify output: `ls -lh JPM_h10_ridge_wf_*.pkl` (new file should be created)
  5. Update config: Change `active-sessions-4session.json` entry `JPM_h10` model_type from `lgbm_ho` to `ridge_wf`
  6. Generate stacker_id: `python -c "import uuid; print(uuid.uuid4())"` → paste into config

### Risk level: **LOW**
- Retraining process is straightforward (same as AMZN)
- Ridge regression is simpler than lgbm (less likely to overfit)
- You have existing training infrastructure
- If retrain fails, you can fall back to Option B

### Benefit:
- ✅ Matches original intended architecture
- ✅ Tests whether architecture diversity improves risk-adjusted returns (Sharpe ratio)
- ✅ Establishes pattern for future model selection (analyst-driven rather than one-size-fits-all)
- ✅ Cleaner narrative for post-checkpoint reporting ("JPM runs linear model for mean-reverting regime")

### Timeline:
- **Start**: May 27 afternoon
- **Finish**: May 28 morning
- **Impact**: Phase 2 activation clearable same day (May 28)

---

## Option B: Update Config to Use Existing lgbm_ho (Faster Activation)

### What you're choosing:
- Use the JPM lgbm_ho pkl that already exists (created April 27, ~5 weeks old)
- Both AMZN and JPM run the same model type (lgbm_ho)
- Simpler architecture: "same model, different symbols"
- Faster activation = start Phase 2 immediately

### Tradeoffs vs intended architecture:
- ❌ Loses architecture diversity test (both models are non-linear)
- ❌ JPM loses specialized linear model for mean-reverting regime
- ❌ Slight theoretical mismatch (non-linear model on linear price driver)
- ✅ Minimal model age concern (4-week-old pkl is fine for research; re-validation via paper trading will catch any drift)

### Effort required:
- **Time**: 10 minutes
- **Steps**:
  1. Edit `projects/stockbot/active-sessions-4session.json`
  2. Find JPM entry (search for "JPM_h10")
  3. Change `"model_type": "ridge_wf"` → `"model_type": "lgbm_ho"`
  4. Change `"model_file": "JPM_h10_ridge_wf_..."` → `"model_file": "JPM_h10_lgbm_ho_4e7f5806.pkl"`
  5. Generate stacker_id: `python -c "import uuid; print(uuid.uuid4())"` → paste into config
  6. Save and commit

### Risk level: **VERY LOW**
- Existing pkl file is proven (4 weeks old, was in production Apr 27)
- lgbm_ho is simpler/more robust than ridge_wf
- Paper trading will catch any model drift immediately
- You can always retrain later if needed

### Benefit:
- ✅ Immediate Phase 2 activation (no 2-3 hour training delay)
- ✅ Risk-lighter (use proven model file, not brand-new retrain)
- ✅ Same model type → consistent parameterization across AMZN/JPM
- ✅ Faster time-to-market for paper trading validation

### Timeline:
- **Start**: May 27 evening
- **Finish**: May 27 evening (10 min)
- **Impact**: Phase 2 activation clearable immediately

---

## Decision Matrix

| Factor | Option A (Retrain ridge_wf) | Option B (Use lgbm_ho) |
|--------|---|---|
| **Effort** | 2-3 hours | 10 minutes |
| **Activation speed** | May 28 afternoon | May 27 evening |
| **Architecture fidelity** | ✅ Matches spec | ❌ Deviates from spec |
| **Model diversity** | ✅ Tests AMZN vs JPM theory | ❌ Same model type both |
| **Risk level** | Low (straightforward retrain) | Very low (proven pkl) |
| **Failure mode** | Retrain can fail; fallback to Option B | Minimal failure risk |
| **Paper trading time to insight** | Slightly faster (optimized model) | +1-2 days (older pkl might need re-optimization) |
| **Post-checkpoint reporting** | Stronger narrative (architecture proves theory) | Simpler narrative (standardized approach) |

---

## Recommendation

**If you have 2-3 hours available: Choose Option A (Retrain ridge_wf)**
- You get the architecture diversity test you originally designed for
- Stronger post-checkpoint reporting ("JPM's linear model outperformed AMZN's non-linear model in mean-reverting environment")
- Sets precedent for thoughtful model selection going forward

**If you want immediate Phase 2 activation: Choose Option B (Use lgbm_ho)**
- Activates Phase 2 today (May 27) instead of May 28
- Lower risk (proven model file)
- Architecture diversity can be tested in Phase 2+ with other symbols (e.g., train 50% of symbols as ridge_wf, 50% as lgbm_ho)

---

## How to Decide

**Ask yourself**:
1. **Do I want to test the theory?** (JPM linear model on linear drivers vs AMZN non-linear)
   - YES → **Option A** (spend 2-3 hours now, get cleaner test)
   - NO → **Option B** (skip theory test, activate faster)

2. **Do I have time today/tomorrow?**
   - YES (2-3 hrs available) → **Option A**
   - NO (urgent activation needed) → **Option B**

3. **What's my Phase 2 goal?**
   - Prove the AMZN/JPM theoretical difference → **Option A** (dedicated ridge_wf for JPM)
   - Scale to 4+ symbols quickly → **Option B** (standardize on lgbm_ho, deploy all at once)

---

## Making the Decision

**To choose Option A** (Retrain):
- Send message to orchestrator: "Approve Option A — I'll retrain JPM with ridge_wf on [DATE]"
- Orchestrator will provide exact training command and post-retrain validation steps

**To choose Option B** (Use existing):
- Send message to orchestrator: "Approve Option B — update config to JPM lgbm_ho, activate Phase 2 immediately"
- Orchestrator will execute config update and commit same day

---

## Post-Decision Actions

Once you decide, the orchestrator will:

1. **Populate JPM stacker_id** (using UUID 92ea4e8b-c865-4d5c-9286-462ac2ba13ff or regenerated)
2. **Verify config** (confirm both AMZN and JPM entries match active Jetson pkl files)
3. **Commit to master** (orchestrator commits config + any retrain artifacts)
4. **Signal Phase 2 readiness** (update BLOCKED.md, PROJECTS.md)
5. **Begin paper trading** (AMZN + JPM sessions launch 2-4 hours later)

---

## Next Steps

**Timeline**:
- **Now (May 27)**: Review this framework, make decision, communicate choice
- **May 27-28**: Orchestrator executes your choice
- **May 28+**: Phase 2 paper trading begins (AMZN + JPM + potentially TSLA, META as time permits)

**Questions?**
- See `AMZN_JPM_TIER1_TRAINING_SPECIFICATION.md` for original architecture rationale
- See `stockbot/docs/model-selection-framework.md` for future model selection criteria

---

## Summary

**Choose A** (Retrain ridge_wf): Theory-first. More work, cleaner proof. Recommended if testing the AMZN/JPM architecture difference is important to you.

**Choose B** (Use lgbm_ho): Speed-first. Less work, faster Phase 2. Recommended if deploying Phase 2 quickly matters more than testing the specific theory.

**Either choice works**. The system is designed to handle both. Make the choice that aligns with your priorities.

