# June 24 Validation Outcome Data Sheet

**Purpose**: Single-page user-fill checklist for capturing June 24 20:00 UTC validation completion data.

**Usage**: Fill this sheet immediately after market close (20:00–20:15 UTC) using post-market diagnostic commands. Submit to PHASE_4_OUTCOMES_DECISION_MATRIX.md for automatic Phase 4 path recommendation.

**Timeline**: Fill 20:00–20:15 UTC (15-min window). Data maps directly to decision matrix cells.

---

## Quick Data Entry (Copy-Paste Ready)

**Validation Outcome**: ☐ PASS / ☐ CAUTION / ☐ NO-GO

**Run these commands post-market (20:00 UTC) and fill results below:**

```bash
# Session count
ssh awank@100.120.18.84 "curl -s http://100.120.18.84:8000/health | python3 -m json.tool | grep sessions"

# Non-HOLD signal count
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'signal generated' | grep -v HOLD | wc -l"

# Buy probability max
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'buy_prob=' | grep -oP 'buy_prob=[\d.]+' | sort -t= -k2 -n | tail -1"

# Trades executed today
ssh awank@100.120.18.84 "sqlite3 /opt/stockbot/database/stockbot.db \"SELECT COUNT(*) FROM trades WHERE DATE(timestamp) = '2026-06-24';\""

# Realized P&L by session
ssh awank@100.120.18.84 "sqlite3 /opt/stockbot/database/stockbot.db \"SELECT session_id, SUM(realized_pnl) as total_pnl FROM trades WHERE DATE(timestamp) = '2026-06-24' GROUP BY session_id ORDER BY session_id;\""

# Regime status (sample — first 10)
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'regime=' | tail -10"

# Z-score drift (all sessions, last 1 day)
uv run python /opt/stockbot/scripts/query_drift_logs.py --days 1 --json
```

---

## Primary Metrics (Fill from command outputs above)

### 1. Session Health

| Session | Ticker | Status | Notes |
|---------|--------|--------|-------|
| jpm_ridge_wf_001 | JPM | ☐ Active / ☐ Error | Docker logs show "sleeping until market open" at 13:15 UTC? |
| amzn_lgbm_ho_001 | AMZN | ☐ Active / ☐ Error | — |
| aapl_lgbm_ho_001 | AAPL | ☐ Active / ☐ Error | — |
| msft_lgbm_ho_001 | MSFT | ☐ Active / ☐ Error | — |
| nvda_lgbm_ho_001 | NVDA | ☐ Active / ☐ Error | — |

**Expected**: All 5 active. If ≥1 shows error → ALERT.

---

### 2. Signal Generation (Post-Market Query)

**Result from command**: `docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'signal generated' | grep -v HOLD | wc -l`

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Non-HOLD signal count** | ___ | ≥87 (6.5h × 5 sessions × 0.33/min) | ☐ PASS (≥87) / ☐ WARN (50–86) / ☐ FAIL (<50) |
| **Sessions with ≥1 signal** | ___ (count) | ≥3 of 5 | ☐ PASS (≥3) / ☐ FAIL (<3) |

**Per-session breakdown** (count BUY + SELL for each):

```
docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'signal generated' | \
  awk '{for(i=1;i<=NF;i++) if($i ~ /session_id|ticker/) print $i}' | paste - - | sort | uniq -c
```

| Session | Ticker | BUY Count | SELL Count | HOLD Count | Non-HOLD Total | Status |
|---------|--------|-----------|------------|------------|-----------------|--------|
| jpm_ridge_wf_001 | JPM | ___ | ___ | ___ | ___ | ☐ ≥1 |
| amzn_lgbm_ho_001 | AMZN | ___ | ___ | ___ | ___ | ☐ ≥1 |
| aapl_lgbm_ho_001 | AAPL | ___ | ___ | ___ | ___ | ☐ ≥1 |
| msft_lgbm_ho_001 | MSFT | ___ | ___ | ___ | ___ | ☐ ≥1 |
| nvda_lgbm_ho_001 | NVDA | ___ | ___ | ___ | ___ | ☐ ≥1 |

**Scoring** (for decision matrix):

- ≥4 sessions with ≥1 signal: **Signal Quality Score = 9/10** ✅
- 3 sessions with ≥1 signal: **Signal Quality Score = 7/10** ✓
- 2 sessions with ≥1 signal: **Signal Quality Score = 5/10** ⚠️
- <2 sessions with ≥1 signal: **Signal Quality Score = 2/10** ❌

**Your Signal Quality Score**: ___/10

---

### 3. Regime Stability

**Query**: 
```bash
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'regime=' | tail -20"
```

**Expected output** (example):
```
2026-06-24T15:30:45Z JPM regime=Bull
2026-06-24T15:35:12Z AMZN regime=Bull
2026-06-24T15:40:08Z AAPL regime=Bull
...
2026-06-24T19:55:30Z JPM regime=Sideways
```

| Session | Ticker | Regime at 13:45 UTC | Regime at 20:00 UTC | # Flips | Flip Rate (/hr) | Status |
|---------|--------|--------------------|--------------------|---------|-----------------|--------|
| jpm_ridge_wf_001 | JPM | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___ | ☐ ≤2–3 / ☐ >4 (ALERT) |
| amzn_lgbm_ho_001 | AMZN | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___ | ☐ ≤2–3 / ☐ >4 (ALERT) |
| aapl_lgbm_ho_001 | AAPL | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___ | ☐ ≤2–3 / ☐ >4 (ALERT) |
| msft_lgbm_ho_001 | MSFT | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___ | ☐ ≤2–3 / ☐ >4 (ALERT) |
| nvda_lgbm_ho_001 | NVDA | [Bull/Bear/Sideways/None] | [Bull/Bear/Sideways/None] | ___ | ___ | ☐ ≤2–3 / ☐ >4 (ALERT) |

**Scoring** (for decision matrix):

- All 5 sessions: regime ≠ None at 20:00 UTC; ≤3 flips each: **Regime Stability Score = 9/10** ✅
- 4 sessions initialized; max flips 3: **Regime Stability Score = 8/10** ✓
- 3–4 sessions; some flips ≤4/hr: **Regime Stability Score = 6/10** ⚠️
- Any session stays regime=None; or >4 flips/hour: **Regime Stability Score = 3/10** ❌

**Your Regime Stability Score**: ___/10

---

### 4. Trade Execution Quality

**Queries**:
```bash
# Total trades
ssh awank@100.120.18.84 "sqlite3 /opt/stockbot/database/stockbot.db \"SELECT COUNT(*) FROM trades WHERE DATE(timestamp) = '2026-06-24';\""

# P&L by session
ssh awank@100.120.18.84 "sqlite3 /opt/stockbot/database/stockbot.db \"SELECT session_id, SUM(realized_pnl) as pnl FROM trades WHERE DATE(timestamp) = '2026-06-24' GROUP BY session_id;\""

# Error counts
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep -E '(40010001|401|403)' | wc -l"
```

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Total trades executed** | ___ | ≥1 | ☐ PASS |
| **Duplicate order errors (40010001)** | ___ | 0 | ☐ PASS (0) / ☐ FAIL |
| **Credential errors (401/403)** | ___ | 0 | ☐ PASS (0) / ☐ FAIL |
| **Total errors** | ___ | 0 | ☐ PASS (0) / ☐ FAIL |

**Per-session P&L**:

| Session | Ticker | Realized P&L | Status |
|---------|--------|-------------|--------|
| jpm_ridge_wf_001 | JPM | $_______ | |
| amzn_lgbm_ho_001 | AMZN | $_______ | |
| aapl_lgbm_ho_001 | AAPL | $_______ | |
| msft_lgbm_ho_001 | MSFT | $_______ | |
| nvda_lgbm_ho_001 | NVDA | $_______ | |
| **TOTAL PORTFOLIO** | — | $_______ | Target: $2,500–$3,500 (2–3% of $106K) |

**Scoring** (for decision matrix):

- ≥1 trade; 0 errors; positive portfolio P&L: **Execution Quality Score = 9/10** ✅
- ≥1 trade; 0 errors; negative or zero P&L: **Execution Quality Score = 7/10** ✓
- ≥1 trade; <3 errors; P&L near zero: **Execution Quality Score = 5/10** ⚠️
- 0 trades OR ≥3 errors: **Execution Quality Score = 2/10** ❌

**Your Execution Quality Score**: ___/10

---

### 5. Buy Probability (Signal Confidence)

**Query**:
```bash
ssh awank@100.120.18.84 "docker logs stockbot --since '2026-06-24T13:30:00Z' 2>&1 | grep 'buy_prob=' | grep -oP 'buy_prob=[\d.]+' | sort -t= -k2 -n | tail -5"
```

**Expected output** (example):
```
buy_prob=0.65
buy_prob=0.61
buy_prob=0.58
buy_prob=0.55
buy_prob=0.52
```

| Metric | Value | Target | Status |
|--------|-------|--------|--------|
| **Max buy_prob observed** | ___ | ≥0.40 | ☐ PASS |
| **Average buy_prob (if >0)** | ___ | ≥0.35 | ☐ PASS / ☐ WARN |

**Scoring** (for decision matrix):

- Max buy_prob ≥0.60: **Signal Confidence Score = 9/10** ✅ (excellent recovery from June 18 failure)
- Max buy_prob 0.40–0.59: **Signal Confidence Score = 7/10** ✓
- Max buy_prob 0.30–0.39: **Signal Confidence Score = 5/10** ⚠️ (marginal)
- Max buy_prob <0.30: **Signal Confidence Score = 2/10** ❌ (failed, like June 18)

**Your Signal Confidence Score**: ___/10

---

### 6. Z-Score Drift (Day 1 Baseline)

**Query**:
```bash
uv run python /opt/stockbot/scripts/query_drift_logs.py --days 1 --json
```

**Expected output** (example):
```json
[
  {"ticker": "JPM", "z_score": -0.12, "band": "GREEN"},
  {"ticker": "AMZN", "z_score": 0.23, "band": "GREEN"},
  {"ticker": "AAPL", "z_score": -0.05, "band": "GREEN"},
  {"ticker": "MSFT", "z_score": 0.31, "band": "GREEN"},
  {"ticker": "NVDA", "z_score": -0.18, "band": "GREEN"}
]
```

| Ticker | Z-Score | Band | Status |
|--------|---------|------|--------|
| JPM | ___ | ☐ GREEN (<2.0) / ☐ YELLOW (2.0–3.0) / ☐ RED (>3.0) | ☐ OK |
| AMZN | ___ | ☐ GREEN / ☐ YELLOW / ☐ RED | ☐ OK |
| AAPL | ___ | ☐ GREEN / ☐ YELLOW / ☐ RED | ☐ OK |
| MSFT | ___ | ☐ GREEN / ☐ YELLOW / ☐ RED | ☐ OK |
| NVDA | ___ | ☐ GREEN / ☐ YELLOW / ☐ RED | ☐ OK |

**Note**: Day 1 Z-scores are baseline only. Statistical significance requires ≥5 trading days.

**Scoring** (for decision matrix):

- All 5 sessions GREEN (|Z| <2.0): **Z-Score Status = 9/10** ✅
- 4 sessions GREEN; 1 YELLOW: **Z-Score Status = 7/10** ✓
- 3+ sessions GREEN; some YELLOW: **Z-Score Status = 5/10** ⚠️
- ≥1 session RED (|Z| >3.0): **Z-Score Status = 2/10** ❌

**Your Z-Score Status Score**: ___/10

---

## Summary Scoring (Fill Below)

**Aggregate Validation Baseline Score** (calculate from scores above):

```
Validation Baseline Score = Average of:
  - Signal Quality Score: ___/10
  - Regime Stability Score: ___/10
  - Execution Quality Score: ___/10
  - Signal Confidence Score: ___/10
  - Z-Score Status Score: ___/10

AVERAGE = (___+___+___+___+___) / 5 = ___/10
```

**PHASE 4 VALIDATION BASELINE SCORE (FOR DECISION MATRIX)**: ___/10

---

## Verdict Mapping (Automatic)

**Use this table to map your scores to recommendation:**

| Baseline Score | Interpretation | Phase 4 Recommendation |
|----------------|-----------------|----------------------|
| **≥8.0** | PASS — All metrics excellent | ✅ **PROCEED** to Phase 4 (select A/B/C path per decision matrix) |
| **7.0–7.9** | PASS — All critical gates met | ✅ **PROCEED** (minor tuning may be needed post-go-live) |
| **6.0–6.9** | CAUTION — Core gates pass, but 1–2 metrics marginal | ⏳ **HOLD 48h** (monitor June 25–26; re-validate if gap closes) |
| **5.0–5.9** | CAUTION — Multiple metrics below target | ⏳ **HOLD 72h** (extended monitoring; escalate if no improvement) |
| **<5.0** | NO-GO — ≥2 critical metrics failed | ❌ **BLOCK** (root-cause analysis + fix required; re-validate June 27) |

**Your Verdict**: ☐ PASS / ☐ CAUTION / ☐ NO-GO

---

## Next Steps (Automatic from Verdict)

### If PASS (≥6.0):

1. ☐ Open **PHASE_4_OUTCOMES_DECISION_MATRIX.md**
2. ☐ Fill column 8 (Validation Baseline Score) with your score from above
3. ☐ Read the "Deterministic Path Selection" table
4. ☐ Identify winning path(s): [☐ Path A / ☐ Path B / ☐ Path C / ☐ A+C]
5. ☐ Open **PHASE_4_IMPLEMENTATION_ROADMAP_TEMPLATE.md**
6. ☐ Copy relevant roadmap section (A / B / C) for your selected path(s)
7. ☐ Update PROJECTS.md with "Phase 4 path selected: ____; implementation begins June 24 21:00 UTC"

### If CAUTION (5.0–6.9):

1. ☐ Update WORKLOG.md: "June 24 validation CAUTION — [specific gaps identified]"
2. ☐ Continue monitoring 5-session config June 25–26
3. ☐ Schedule re-validation for June 26 18:00 UTC
4. ☐ If gap resolves by June 26 18:00 UTC → expedited re-validation June 27
5. ☐ If gap persists → escalate to NO-GO path

### If NO-GO (<5.0):

1. ☐ Update WORKLOG.md: "June 24 validation NO-GO — root cause: [identify specific failure]"
2. ☐ File in BLOCKED.md with recommended fix + ETA
3. ☐ Disable HMM masking (set `hmm_observe_mode: true` in session config)
4. ☐ Deploy diagnostic logging to Jetson (24–48h window)
5. ☐ Schedule root-cause fix implementation for June 25 08:00–16:00 UTC
6. ☐ Plan expedited re-validation for June 27 or June 28

---

## User Checklist (June 24 20:00–20:30 UTC)

- [ ] All diagnostic commands executed successfully
- [ ] All metrics above filled in (signal count, regime status, P&L, buy_prob, Z-scores)
- [ ] All 5 scores calculated (Signal Quality, Regime Stability, Execution Quality, Signal Confidence, Z-Score)
- [ ] Aggregate Validation Baseline Score calculated: ___/10
- [ ] Verdict determined: [PASS / CAUTION / NO-GO]
- [ ] Next steps checklist reviewed + initiated
- [ ] PHASE_4_OUTCOMES_DECISION_MATRIX.md filled in (if PASS)
- [ ] PROJECTS.md updated with validation outcome

---

## Quick Reference: Score Mapping to Decision Matrix

| Your Score | Decision Matrix Use |
|-----------|-------------------|
| Signal Quality ___/10 | → Path A/B/C Signal Quality column (compare to baseline) |
| Regime Stability ___/10 | → Path B Inverse ETF score (higher = better HMM health) |
| Execution Quality ___/10 | → Path A/B/C Execution Quality column (order reliability) |
| Signal Confidence ___/10 | → Buy probability restoration gate (Path A/C readiness) |
| Z-Score Status ___/10 | → Model alignment check; if <7, monitor through day 5 |
| **Validation Baseline ___/10** | → **Column 8 of decision matrix** (fill this field only) |

---

## Troubleshooting: If Commands Fail

| Command | Error | Fix |
|---------|-------|-----|
| `ssh awank@100.120.18.84 ...` | "Connection refused" | Check Jetson is reachable: `ping 100.120.18.84` |
| `docker logs stockbot` | "permission denied" | SSH into Jetson first: `ssh awank@100.120.18.84`, then run |
| `sqlite3 ... SELECT` | "database is locked" | Jetson may still be writing; wait 30 sec, retry |
| `query_drift_logs.py` | "No data found" | Run after market close 20:00 UTC; requires ≥1 day data |
| Any command hangs | "timeout" | Press Ctrl+C; check network; retry |

---

*Template created: 2026-06-24 (Session 4113, orchestrator autonomous prep)*  
*Status: PRODUCTION-READY — user-fill only, no analysis required*  
*Submission deadline: June 24 20:15 UTC (post-market)*  
*Reference: PHASE_4_OUTCOMES_DECISION_MATRIX.md (receives data from this sheet)*
