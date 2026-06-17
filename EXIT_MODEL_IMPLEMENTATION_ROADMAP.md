# Exit Model Implementation Roadmap

**Purpose**: Three-stage progressive implementation plan for the exit model, gated by
cumulative AAPL round-trip count from live trading. Each stage builds on the previous.

**Prerequisite**: All Section 5 gates in EXIT_MODEL_TRAINING_DATA_READINESS_CHECKLIST.md
must pass before beginning Stage A.

**Architecture note**: The ExitModel class (`src/models/exit_model.py`) already exists and
supports `backend="gradient_boosting"` and `backend="random_forest"`. The training helper
`prepare_training_data_from_trades()` and the SQL extraction pattern for round trips are
documented in `EXIT_MODEL_BACKTEST_APPROACH.md`. This roadmap governs when to invoke them
and at what complexity level.

---

## Cumulative Round-Trip Cadence Projection

Based on 5 live sessions (AAPL, MSFT, JPM, AMZN, NVDA) deployed as of June 15, targeting
5–10 AAPL/MSFT trips per trading day from June 18 forward (post-Phase 4 GO decision):

| Target | Round Trips | Projected Date | Confidence |
|--------|------------|----------------|------------|
| Stage A trigger | 50 AAPL | June 27–30, 2026 | 75% |
| Stage B trigger | 100 AAPL | July 10–15, 2026 | 65% |
| Stage C trigger | 150 AAPL | July 22–28, 2026 | 55% |

**Projection assumptions**:
- Signal frequency: ~2–4 AAPL BUY signals per day in sideways/bull HMM regime
- Fill rate: ~60–80% of signals result in fills (paper trading, no partial fills)
- Market days: 5 per week (US equities, no holidays between June 18–July 28)

**Downside scenario** (fill rate < 40% or HMM bear regime sustained): delay each date
by 1–2 weeks. Re-assess cadence at each 20:00 UTC post-market checkpoint.

**Timeline routing (July 1 assessment point)**:
- If AAPL trips >= 150 by July 1: activate Stage C multi-strategy ensemble directly
- If AAPL trips 100–149 by July 1: begin Stage B; Stage C available ~2 weeks later
- If AAPL trips 50–99 by July 1: proceed with Stage A baseline; plan Stage B for mid-July
- If AAPL trips < 50 by July 1: defer Phase 3b; continue accumulation; reassess July 15

---

## Stage A — Baseline Exit Model (50 trips)

**Trigger**: 50 completed AAPL round trips in `trading.db`, all Section 5 gates pass.
**Timeline**: 1 week from trigger (implementation + validation + deployment prep)
**Implementation deadline**: Complete within 5 business days of hitting 50 trips

### Model specification

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Backend | `"gradient_boosting"` | Default ExitModel; scikit-learn GBC; architectural diversity from LightGBM entry model |
| Threshold | 0.60 (default) | Starting point per EXIT_MODEL_BACKTEST_APPROACH.md; sweep 0.50–0.75 on holdout set |
| Max depth | 3 (sklearn default for GBC) | Prevents overfitting at small N |
| n_estimators | 100 (reduce from default 200) | Conservative at 50-trip data size |
| Feature set | `EXIT_FEATURE_NAMES` default | 13-feature set from `ExitFeatureComputer`; no custom additions at Stage A |

### Stage A feature set (from `ExitFeatureComputer`)

The `EXIT_FEATURE_NAMES` tuple in `exit_model.py` defines the exact 13 features used.
Do not add or remove features at Stage A — the live signal path uses the same names in
the same order, and mismatches produce silent shape errors.

### Training procedure

1. Extract round trips per `EXIT_MODEL_BACKTEST_APPROACH.md` Section 1
2. Apply 70/30 chronological split (see EXIT_MODEL_BACKTEST_EXECUTION_RUNBOOK.md)
3. Call `prepare_training_data_from_trades()` with h10_horizon=10 (match live config)
4. Instantiate `ExitModel(name="exit_AAPL_stage_a", backend="gradient_boosting")`
5. Set `n_estimators=100` via `ExitModel.params` before calling `.fit()`
6. Validate on holdout set per Stage A gates below

### Stage A validation gates

| Gate | Threshold | Measured by |
|------|-----------|------------|
| A1: Holdout win rate | > 45% of voluntary exits profitable | Backtest synthetic exit path (Runbook Step 5) |
| A2: ΔPnL direction | Positive (exit model beats baseline) | `mean(pnl_with_model) - mean(pnl_without)` on holdout |
| A3: Voluntary exit rate | > 50% of holdout trades exit via model | Count model-exits / total holdout trades |
| A4: Avg hold time | 3–30 minutes | Mean of `(exit_time - entry_time).minutes` for model exits |

**All 4 gates must pass to deploy**. If A1 or A2 fail, apply threshold sweep per
EXIT_MODEL_BACKTEST_EXECUTION_RUNBOOK.md Section 7 before concluding failure.

### Stage A scope limits

- Train on AAPL only. MSFT, JPM, AMZN exit models follow when each reaches 50 trips.
- No regime weighting at this stage (data insufficient for reliable regime-conditional fits)
- No cross-ticker feature transfer
- Deploy to AAPL session only (`aapl_lgbm_ho_001`)

---

## Stage B — Multivariate Feature Discovery (100+ trips)

**Trigger**: 100 completed AAPL round trips, Stage A model deployed and running >= 1 week.
**Timeline**: 2–3 weeks from trigger
**Purpose**: Discover whether adding market-structure features (regime, VIX proxy, volume
percentile) improves exit quality beyond the baseline position-aware features.

### Model specification

| Parameter | Value | Change from Stage A |
|-----------|-------|---------------------|
| Backend | `"random_forest"` | Switch to RF for feature importance scores |
| Threshold | Re-sweep from Stage A optimal | Not inherited — re-sweep on larger dataset |
| n_estimators | 200 | Restore full default |
| Feature set | Default + regime indicator | Add `hmm_regime` (0=bear, 1=sideways, 2=bull) as explicit feature |

### New features at Stage B

The `ExitFeatureComputer` will need one additional feature to be added to the feature
construction path. Before implementing, verify that `hmm_regime` is reliably logged in
the `trades` table via the `regime` column (or reconstruct from `SignalRecord` table).

```sql
-- Check if regime is stored per trade
SELECT regime, COUNT(*) FROM trades WHERE mode = 'paper' GROUP BY regime;
```

If `regime` is NULL in most rows: reconstruct regime from the `signal_records` table
(if populated) or re-run HMM on historical bars to label training data by regime.

### Stage B validation gates

| Gate | Threshold | Change from Stage A |
|------|-----------|---------------------|
| B1: Holdout win rate | > 50% | Tightened from A1's 45% |
| B2: ΔPnL vs Stage A | >= 0 (Stage B at least as good) | New: must not regress from Stage A |
| B3: Voluntary exit rate | > 55% | Tightened from A3's 50% |
| B4: Feature importance | Top 3 features not all position-based | Ensures new features contribute |
| B5: Regime-conditional performance | Win rate positive in >= 2 of 3 regimes | New regime-specific validation |

**If B2 fails** (Stage B regresses below Stage A performance): retain Stage A model,
document the negative result, and do not proceed to Stage C. Stage A remains live until
Stage C is independently validated.

### Stage B parallel work

While Stage B validation runs, begin MSFT exit model training (Stage A procedure) if
MSFT has also reached 50 trips. MSFT and AAPL exit models are independent artifacts.

---

## Stage C — Ensemble Exit Model with Regime Weighting (150+ trips)

**Trigger**: 150 completed AAPL round trips, Stage B model validated (or Stage A if B failed).
**Timeline**: 3–4 weeks from trigger
**Purpose**: Regime-conditional ensemble that weights predictions differently in bull vs.
sideways vs. bear, addressing the bias identified in EXIT_MODEL_TRAINING_DATA_READINESS_CHECKLIST.md
Section 4.2.

### Model specification

| Parameter | Value | Change from Stage B |
|-----------|-------|---------------------|
| Backend | `"gradient_boosting"` (regime-split) | Train separate GBC per HMM regime; ensemble via regime-conditional inference |
| Thresholds | Per-regime thresholds | Bull threshold, sideways threshold, bear threshold |
| Feature set | Stage B features + momentum features | Add 5-bar momentum, ATR percentile relative to 30-day range |

### Regime-split ensemble approach

Because the ExitModel class does not natively support regime-conditional ensembles,
implement via the following wrapper pattern:

1. Split training data into 3 subsets by `hmm_regime` value
2. Train 3 separate `ExitModel` instances: `exit_AAPL_bull`, `exit_AAPL_sideways`, `exit_AAPL_bear`
3. At inference time in `ExitSignalGenerator`, query the live session's current HMM regime
   and select the appropriate model instance

**If any regime has < 30 training trips**: do not train that regime-specific model. Fall
back to Stage B model for that regime. Confirm minimum counts with:

```sql
SELECT regime, COUNT(*) FROM trades
WHERE action = 'BUY' AND mode = 'paper' AND ticker = 'AAPL'
  AND EXISTS (SELECT 1 FROM trades s WHERE s.ticker = trades.ticker
              AND s.action = 'SELL' AND s.timestamp > trades.timestamp)
GROUP BY regime;
```

### Stage C validation gates

| Gate | Threshold | Notes |
|------|-----------|-------|
| C1: Ensemble win rate | > 55% | Overall, not per-regime |
| C2: ΔPnL vs Stage B | >= 0 | Must not regress from best prior stage |
| C3: Regime-conditional win rate | > 50% in each active regime | Regime not represented: skip gate |
| C4: Voluntary exit rate | > 60% | |
| C5: Avg hold time | 5–25 min | Tighter than Stage A/B; regime model should improve timing |

### Multi-strategy ensemble (July 1 fast-path)

If cumulative round trips exceed the Stage C threshold by July 1 AND all Stage B
validation gates pass: activate multi-strategy ensemble directly from Stage B by
adding the regime dimension as a feature (not separate models). This compresses the
Stage B → Stage C timeline from 3–4 weeks to 1 week.

**Trigger condition**: `n_AAPL_trips >= 150 AND stage_b_b1_pass AND stage_b_b2_pass`

---

## Implementation Risk Register

| Risk | Probability | Severity | Mitigation |
|------|------------|---------|------------|
| Low fill rate delays Stage A beyond July 15 | 35% | Medium | Accept delay; Phase 3b is non-blocking |
| Stage A model fails A2 (negative ΔPnL) | 20% | High | Run threshold sweep first; if still fails, document and defer |
| Regime underrepresentation in Stage B | 40% | Medium | Document which regimes are absent; defer regime weighting to Stage C |
| ExitModel API change breaks training scripts | 10% | Low | Pin to current commit before training; run `uv run pytest tests/` after any model changes |
| Paper-to-live transfer degradation | 25% | High | Stage A live shadow-mode for 5 sessions before enabling voluntary exits |

---

## Deliverable Checklist per Stage

**Stage A deliverables**:
- [ ] `models/exit_AAPL_stageA_<YYYYMMDD>.pkl` — trained model artifact
- [ ] `models/exit_AAPL_stageA_<YYYYMMDD>.meta.json` — auto-written by `model.save()`
- [ ] Stage A validation report (4-gate results, threshold sweep table)
- [ ] Updated `active-sessions-*.json` for `aapl_lgbm_ho_001` with `exit_model_enabled: true`

**Stage B deliverables**:
- [ ] `models/exit_AAPL_stageB_<YYYYMMDD>.pkl`
- [ ] Feature importance table (RF feature importances, top 10)
- [ ] Stage B validation report (5-gate results, regime breakdown)
- [ ] MSFT Stage A model (if MSFT >= 50 trips)

**Stage C deliverables**:
- [ ] `models/exit_AAPL_<regime>_stageC_<YYYYMMDD>.pkl` (one per active regime)
- [ ] Regime-conditional threshold table (3 thresholds)
- [ ] Stage C validation report (5-gate results, per-regime breakdown)
- [ ] Updated `ExitSignalGenerator` wiring if regime-conditional dispatch requires code change
