# Stockbot Model Pipeline Architecture
> Written 2026-06-28. Describes Phase 1 of MODEL_PIPELINE_OPENSPEC as implemented.

---

## Overview

The model pipeline is a **nightly post-market search system** that automatically tests candidate model configurations against historical data and reports the best results via Discord. It runs on the **Pi (raspby1)**, not the Jetson. The Jetson runs the live trading sessions; the Pi does the offline search work overnight.

Phase 1 (implemented): automated nightly search + candidate database + Discord report.
Phase 2 (not yet implemented): automatic deployment of winning candidates to the Jetson.

---

## Schedule

```
Mon-Fri (market days only)

21:15 UTC  →  daily_model_search.py runs (~30 min)
21:45 UTC  →  generate_daily_pipeline_report.py runs (reads search results, sends Discord)
```

Market closes at 20:00 UTC. The 75-minute gap gives fill data time to settle before the search begins.

The search **does not run** on weekends or holidays. The first run of the week uses that day's fresh fills; no search results exist before Monday's open.

---

## Files

| File | Machine | Purpose |
|------|---------|---------|
| `scripts/daily_model_search.py` | Pi | Nightly search orchestrator |
| `scripts/generate_daily_pipeline_report.py` | Pi | Report generator + Discord sender |
| `src/pipeline/candidate_database.py` | Pi | Per-ticker SQLite DB layer |
| `database/model_search/{TICKER}_model_history.db` | Pi | Candidate audit trail (created on first run) |
| `reports/daily/{DATE}_pipeline.md` | Pi | Markdown report (created nightly) |

---

## How the Search Works

### Step 1 — Build Candidate List (per ticker)

For each ticker (JPM, AMZN, AAPL, MSFT, NVDA), the search builds up to 8 candidate configurations:

**Stage 1 — Architecture grid** (always runs first):
- Tests every combination of Tier 1 architectures (`lgbm_ho`, `ridge_wf`) × feature variants (`standard`, `momentum_only`)
- Tier 2 (`gradient_boosting`) added if budget allows
- All use `no_macro` overlay and no HMM gating in Phase 1

**Stage 2 — Optuna TPE** (fills remaining budget):
- Uses Tree-structured Parzen Estimator (Bayesian search) to suggest hyperparameter combinations for `lgbm_ho`
- Studies are **persisted across days** in the candidate DB — prior evaluations warm-start tomorrow's search, so the sampler learns from history
- Optimizes two objectives simultaneously: maximize OOS Sharpe, minimize max drawdown

### Step 2 — Quick Screen

Each candidate runs a **3-fold, 400-day lookback** evaluation (`quick=True` in ModelTrainingPipeline). This is fast — roughly 30-60 seconds per candidate.

Gate G1 (OOS Sharpe) is checked. If Sharpe < 0.70, the candidate is recorded as a quick fail and skipped. This eliminates weak configs cheaply before committing to full evaluation compute.

### Step 3 — Full Evaluation (quick-screen survivors only)

Survivors run a **10-fold, 4-year lookback** evaluation (`quick=False`). This tests all 6 gates:

| Gate | Metric | Threshold |
|------|--------|-----------|
| G1 | OOS Sharpe | > 1.0 |
| G2 | Max Drawdown | < 20% |
| G3 | t-statistic | > 2.0 |
| G4 | DSR Sharpe | > 0.80 |
| G5 | Regime-positive folds | ≥ 2/3 |
| G6 | Walk-forward efficiency | > 0.50 |

G7 (Monte Carlo p_loss_6mo, Sharpe p05) is advisory — recorded but not a gate.

A candidate that passes all 6 gates is eligible for deployment consideration.

### Step 4 — Record Results

Every candidate (pass and fail) is written to the **per-ticker SQLite database** — this is append-only and functions as a full audit trail. Nothing is deleted or modified after insertion.

After all candidates are evaluated, a `daily_search_summary` row is written recording counts and the best candidate ID.

### Step 5 — Report (21:45 UTC)

`generate_daily_pipeline_report.py` reads the day's results and:
1. Writes a Markdown file to `reports/daily/{DATE}_pipeline.md`
2. Posts a compact summary to Discord via `STOCKBOT_DISCORD_WEBHOOK_URL`

Discord format per ticker:
```
**AAPL** — Best candidate: lgbm_ho (Sharpe 1.43, DD 8.2%, 6/6 gates) | Live model: Sharpe 1.21
```

---

## Compute Constraints

- **Parallelism**: Up to 3 tickers run concurrently (`MODEL_SEARCH_MAX_WORKERS=3`), respecting the Pi's thermal budget
- **Thermal abort**: If Pi CPU temp exceeds 88°C (`THERMAL_ABORT_TEMP_C`), the search aborts
- **Hetzner offload**: `HETZNER_SSH_HOST` env var enables offloading to Hetzner burst compute (not configured yet)
- **Candidates per ticker**: Capped at 8 (`MODEL_SEARCH_CANDIDATES_PER_TICKER`)

Total wall-clock time: roughly 30 minutes for 5 tickers at 8 candidates each.

---

## Candidate Database Schema

Each ticker gets its own SQLite file at `database/model_search/{TICKER}_model_history.db`.

Three tables:

**`model_candidates`** — one row per evaluation
- Identifies the config: model_type, feature_variant, macro_overlay, hmm_gated, hyperparameters
- Records the eval parameters: train window, OOS months, walk-forward folds
- Stores all gate values and pass/fail flags (G1-G7)
- Extra OOS metrics: win_rate, profit_factor, total_trades, sortino, calmar
- Deployment tracking fields: `deployed`, `deployed_at`, `live_sharpe` (populated in Phase 2)

**`daily_search_summary`** — one row per (ticker, date)
- Aggregate counts: candidates generated, quick-screen pass, full-eval, all-gates pass
- Points to best_candidate_id and records live_model_sharpe for comparison

**`deployment_events`** — Phase 2 stub (empty in Phase 1)
- Will track deploy/rollback events when auto-deployment is implemented

Indexes on (ticker, run_date), (ticker, all_gates_passed, g1_oos_sharpe), and (ticker, deployed) for fast common queries.

---

## What "Live Model Sharpe" Means

The report compares each best candidate against the **live model's OOS Sharpe**. In Phase 1, `get_live_model_sharpe()` queries for rows where `deployed=1` — which means this field will always return `None` until Phase 2 wires up the deployment tracking. The search runs correctly regardless; the comparison just shows "no live record" for now.

---

## Optuna Study Persistence

The Optuna study for each ticker is named `{TICKER}_daily_search_v1` and persists in the candidate DB. On subsequent nights, the TPE sampler loads prior trial history and uses it to inform new hyperparameter suggestions — the search improves over time as it accumulates evaluations.

If the study storage fails (DB corrupt, schema mismatch), it falls back to an in-memory study and continues — no crash.

---

## Environment Variables

All have defaults. Override via `.env` or shell:

| Variable | Default | Purpose |
|----------|---------|---------|
| `MODEL_SEARCH_TICKERS` | `JPM,AMZN,AAPL,MSFT,NVDA` | Ticker list |
| `MODEL_SEARCH_MAX_WORKERS` | `3` | Parallel ticker cap |
| `MODEL_SEARCH_QUICK_MIN_SHARPE` | `0.70` | Quick-screen floor |
| `MODEL_SEARCH_CANDIDATES_PER_TICKER` | `8` | Max candidates per ticker |
| `MODEL_SEARCH_DB_DIR` | `database/model_search` | DB file location |
| `THERMAL_ABORT_TEMP_C` | `88.0` | Pi thermal safety abort |
| `HETZNER_SSH_HOST` | *(empty)* | Hetzner burst (disabled) |
| `STOCKBOT_DISCORD_WEBHOOK_URL` | *(required for Discord)* | Already declared in .env |

---

## Manual Trigger

To run the search manually outside of cron (e.g. on a Sunday before Monday open):

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/stockbot

# Full search (will take ~30 min)
uv run python scripts/daily_model_search.py --tickers JPM,AMZN,AAPL,MSFT,NVDA

# Dry run (writes stub records, no actual model evaluation)
uv run python scripts/daily_model_search.py --tickers JPM,AMZN,AAPL,MSFT,NVDA --dry-run

# Then generate the report
uv run python scripts/generate_daily_pipeline_report.py

# Or report to stdout only (skip Discord + file write)
uv run python scripts/generate_daily_pipeline_report.py --dry-run
```

---

## What Is NOT Implemented Yet (Phase 2)

- **Auto-deployment**: no candidate is ever automatically pushed to the Jetson. Deployment events table is a stub. A human decision is still required to swap the live model.
- **Live model tracking**: `deployed` flag is never set to 1, so live Sharpe comparisons always show "no live record"
- **Hetzner offload**: the env var exists but the SSH offload logic is not implemented
- **HMM-gated candidates**: `hmm_gated=False` is hardcoded in Phase 1; HMM-gated search is deferred

---

## Relationship to Live Trading

The pipeline is **completely separate from live trading**. The Jetson container runs the 5 active sessions (JPM ridge_wf, AMZN/AAPL/MSFT/NVDA lgbm_ho) independently. The Pi's nightly search reads historical data, writes to local SQLite DBs, and sends Discord reports — it makes no calls to Alpaca, does not touch the Jetson, and has no impact on live session behavior.

The only bridge between the two is a human decision to take a Phase 1 candidate and deploy it via `scripts/deploy-to-jetson.sh`.
