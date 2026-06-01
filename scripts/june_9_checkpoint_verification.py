#!/usr/bin/env python3
"""
June 9 Checkpoint Verification Script.

Reads first 5 trading days of live P&L data (June 2-6) and evaluates drift against
backtest baseline. Implements decision tree: GREEN/YELLOW/RED/CRITICAL based on
Z-score thresholds.

Exit codes:
  0: GREEN or YELLOW (continue monitoring)
  1: RED (investigate root cause)
  2: CRITICAL (execute rollback) or ERROR

Output format: Markdown table for WORKLOG.md entry
"""

import sys
import sqlite3
import statistics
import json
import math
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import List, Dict, Optional, Tuple

# Baseline metrics from JUNE_2_23_LIVE_MONITORING_PROTOCOL.md
BACKTEST_BASELINES = {
    "JPM": {
        "model_type": "ridge_wf",
        "oos_sharpe": 4.412,
        "max_dd": 0.024,
        "daily_mean": 0.0905 / 100,  # 0.0905%
        "daily_std": 0.0082,  # 0.82%
    },
    "AMZN": {
        "model_type": "lgbm_ho",
        "oos_sharpe": 3.939,
        "max_dd": 0.063,
        "daily_mean": 0.2556 / 100,  # 0.2556%
        "daily_std": 0.015,  # 1.5%
    },
}

TRADING_DAYS_PER_YEAR = 252

# Decision thresholds (Z-score in standard deviations)
THRESHOLD_GREEN = 1.5
THRESHOLD_YELLOW = 2.5
THRESHOLD_RED = 3.0

# Minimum Sharpe ratio thresholds
MIN_SHARPE_ACCEPTABLE = 1.0
MIN_SHARPE_CONCERN = 0.5


def get_live_daily_returns(db_path: str, ticker: str, lookback_days: int = 10) -> List[float]:
    """
    Fetch daily returns from performance_metrics for given ticker.

    Returns list of daily returns, oldest-first.
    """
    try:
        conn = sqlite3.connect(db_path)
        since = (datetime.now(timezone.utc) - timedelta(days=lookback_days * 2)).strftime("%Y-%m-%d")

        # Primary: from performance_metrics table
        rows = conn.execute(
            """
            SELECT date(timestamp) as day, AVG(daily_return) as dr
            FROM performance_metrics
            WHERE ticker = ? AND timestamp >= ? AND daily_return IS NOT NULL
            GROUP BY day ORDER BY day ASC
            """,
            (ticker, since),
        ).fetchall()

        returns = [float(r[1]) for r in rows if r[1] is not None]

        # Fallback: synthesize from trades if performance_metrics empty
        if not returns:
            rows = conn.execute(
                """
                SELECT date(timestamp) as day,
                       SUM(CASE WHEN realized_pnl IS NOT NULL THEN realized_pnl ELSE 0 END) as day_pnl,
                       SUM(price * ABS(quantity)) as day_notional
                FROM trades
                WHERE ticker = ? AND timestamp >= ? AND realized_pnl IS NOT NULL
                GROUP BY day HAVING day_notional > 0 ORDER BY day ASC
                """,
                (ticker, since),
            ).fetchall()

            returns = []
            for _day, day_pnl, day_notional in rows:
                if day_notional and day_notional > 0:
                    returns.append(float(day_pnl) / float(day_notional))

        conn.close()
        return returns
    except Exception as e:
        print(f"ERROR: Failed to fetch returns for {ticker}: {e}", file=sys.stderr)
        return []


def count_profitable_days(returns: List[float]) -> int:
    """Count number of days with positive return."""
    return sum(1 for r in returns if r > 0)


def calculate_metrics(returns: List[float]) -> Dict:
    """
    Calculate daily Sharpe, max drawdown, win rate from return series.

    Returns dict with: sharpe, max_dd, win_rate, mean, std, num_days
    """
    if not returns or len(returns) < 2:
        return {
            "sharpe": 0.0,
            "max_dd": 0.0,
            "win_rate": 0.0,
            "mean": 0.0,
            "std": 0.0,
            "num_days": len(returns),
        }

    # Mean and std
    mean = statistics.mean(returns)
    std = statistics.stdev(returns) if len(returns) >= 2 else 0.0

    # Annualized Sharpe
    sharpe = 0.0
    if std > 0:
        sharpe = mean / std * math.sqrt(TRADING_DAYS_PER_YEAR)

    # Max drawdown: largest peak-to-trough decline
    cumulative = 0.0
    peak = 0.0
    max_dd = 0.0
    for r in returns:
        cumulative += r
        if cumulative > peak:
            peak = cumulative
        dd = peak - cumulative
        if dd > max_dd:
            max_dd = dd

    # Win rate
    win_rate = count_profitable_days(returns) / len(returns) if returns else 0.0

    return {
        "sharpe": sharpe,
        "max_dd": max_dd,
        "win_rate": win_rate,
        "mean": mean,
        "std": std,
        "num_days": len(returns),
    }


def calculate_z_score(live_mean: float, backtest_mean: float, backtest_std: float, n: int) -> float:
    """
    Calculate Z-score: (live_mean - backtest_mean) / SE
    where SE = backtest_std / sqrt(n)
    """
    if n < 2:
        return 0.0
    se = backtest_std / math.sqrt(n)
    if se > 0:
        return (live_mean - backtest_mean) / se
    return 0.0


def determine_decision(z_score: float, sharpe: float, backtest_sharpe: float) -> Tuple[str, str, int]:
    """
    Decision tree logic.

    Returns: (status, reasoning, exit_code)
    - status: GREEN | YELLOW | RED | CRITICAL
    - reasoning: human-readable explanation
    - exit_code: 0 (continue) | 1 (investigate) | 2 (critical)
    """
    abs_z = abs(z_score)

    # CRITICAL: Z > 3.0σ OR Sharpe < 0.5 for 2+ days
    if abs_z > THRESHOLD_RED or sharpe < MIN_SHARPE_CONCERN:
        reason = f"Z-score={z_score:.2f} > {THRESHOLD_RED}σ OR Sharpe={sharpe:.2f} < {MIN_SHARPE_CONCERN}"
        return ("CRITICAL", reason, 2)

    # RED: Z 2.5-3.0σ OR Sharpe < 1.0
    if abs_z > THRESHOLD_YELLOW or sharpe < MIN_SHARPE_ACCEPTABLE:
        reason = f"Z-score={z_score:.2f} in ({THRESHOLD_YELLOW}σ, {THRESHOLD_RED}σ] OR Sharpe={sharpe:.2f} < {MIN_SHARPE_ACCEPTABLE}"
        return ("RED", reason, 1)

    # YELLOW: Z 1.5-2.5σ
    if abs_z > THRESHOLD_GREEN:
        reason = f"Z-score={z_score:.2f} in ({THRESHOLD_GREEN}σ, {THRESHOLD_YELLOW}σ]; monitor closely"
        return ("YELLOW", reason, 0)

    # GREEN: Z < 1.5σ AND Sharpe > 2.0
    reason = f"Z-score={z_score:.2f} < {THRESHOLD_GREEN}σ; Sharpe={sharpe:.2f} normal"
    return ("GREEN", reason, 0)


def format_markdown_table(results: Dict) -> str:
    """Format decision table as markdown for WORKLOG.md entry."""
    lines = [
        "## June 9 Checkpoint — Z-Score Drift Detection",
        "",
        "| Ticker | Model | Days | Live Sharpe | BT Sharpe | Daily Mean | Z-Score | Decision | Action |",
        "|--------|-------|------|-------------|-----------|------------|---------|----------|--------|",
    ]

    for ticker, data in results.items():
        if ticker == "ERROR":
            continue

        status = data["status"]
        emoji = "🟢" if status == "GREEN" else ("🟡" if status == "YELLOW" else ("🔴" if status == "RED" else "⛔"))

        lines.append(
            f"| {ticker} | {data['model_type']} | {data['num_days']} | "
            f"{data['sharpe']:.2f} | {data['backtest_sharpe']:.2f} | "
            f"{data['mean']:.4%} | {data['z_score']:.2f} | "
            f"{emoji} {status} | {data['action']} |"
        )

    lines.append("")
    lines.append("### Decision Summary")
    lines.append("")

    for ticker, data in results.items():
        if ticker == "ERROR":
            lines.append(f"**ERROR**: {data}")
            continue

        status = data["status"]
        lines.append(f"**{ticker}**: {status} — {data['reasoning']}")

    return "\n".join(lines)


def main():
    """Main execution."""
    # Determine database path
    repo_root = Path(__file__).parent.parent
    db_candidates = [
        repo_root / "projects/stockbot/database/stockbot.db",
        repo_root / "projects/stockbot/stockbot.db",
    ]

    db_path = None
    for candidate in db_candidates:
        if candidate.exists():
            db_path = str(candidate)
            break

    if not db_path:
        print("ERROR: Could not find stockbot.db", file=sys.stderr)
        sys.exit(2)

    print(f"Using database: {db_path}")

    results = {}
    exit_code = 0

    # Process each ticker
    for ticker, baseline in BACKTEST_BASELINES.items():
        try:
            # Fetch live returns for first 5 trading days (June 2-6)
            returns = get_live_daily_returns(db_path, ticker, lookback_days=5)

            # Trim to first 5 days
            returns = returns[:5]

            if not returns or len(returns) < 1:
                print(f"WARNING: No live data for {ticker} yet", file=sys.stderr)
                results[ticker] = {
                    "model_type": baseline["model_type"],
                    "num_days": 0,
                    "sharpe": 0.0,
                    "max_dd": 0.0,
                    "mean": 0.0,
                    "backtest_sharpe": baseline["oos_sharpe"],
                    "z_score": 0.0,
                    "status": "PENDING",
                    "reasoning": "Insufficient data (< 1 day)",
                    "action": "Await more data",
                }
                continue

            # Calculate metrics
            metrics = calculate_metrics(returns)

            # Calculate Z-score
            z_score = calculate_z_score(
                metrics["mean"],
                baseline["daily_mean"],
                baseline["daily_std"],
                metrics["num_days"],
            )

            # Determine decision
            status, reasoning, code = determine_decision(
                z_score,
                metrics["sharpe"],
                baseline["oos_sharpe"],
            )

            # Determine action
            if status == "GREEN":
                action = "Continue without changes"
            elif status == "YELLOW":
                action = "Monitor closely; no changes"
            elif status == "RED":
                action = "Investigate root cause; prepare contingency"
            else:  # CRITICAL
                action = "Execute rollback playbook"

            results[ticker] = {
                "model_type": baseline["model_type"],
                "num_days": metrics["num_days"],
                "sharpe": metrics["sharpe"],
                "max_dd": metrics["max_dd"],
                "mean": metrics["mean"],
                "backtest_sharpe": baseline["oos_sharpe"],
                "z_score": z_score,
                "status": status,
                "reasoning": reasoning,
                "action": action,
            }

            # Update exit code (RED or CRITICAL => non-zero)
            if code > exit_code:
                exit_code = code

            print(
                f"{ticker}: {status} (Z={z_score:.2f}, Sharpe={metrics['sharpe']:.2f}, "
                f"days={metrics['num_days']})"
            )

        except Exception as e:
            print(f"ERROR processing {ticker}: {e}", file=sys.stderr)
            results["ERROR"] = str(e)
            exit_code = 2

    # Output markdown table
    print("\n" + format_markdown_table(results))

    # Write to WORKLOG.md if provided
    worklog_path = repo_root / "projects/stockbot/WORKLOG.md"
    if worklog_path.exists():
        try:
            with open(worklog_path, "a") as f:
                f.write("\n\n" + format_markdown_table(results))
            print(f"\nAppended to {worklog_path}")
        except Exception as e:
            print(f"WARNING: Could not write to WORKLOG.md: {e}", file=sys.stderr)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
