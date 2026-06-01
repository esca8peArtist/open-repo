#!/usr/bin/env python3
"""
June 16 Mid-Window Checkpoint Verification Script.

Reads 10+ trading days of live P&L data (June 2-13) and analyzes trend:
is Z-score converging toward historical baseline or diverging?

Implements decision tree:
  PASS: Trends normalizing toward 0
  CAUTION: Stable drift, within acceptable bounds
  FAIL: Deteriorating, trends away from 0

Exit codes:
  0: PASS (continue planning)
  1: CAUTION (acceptable, no changes)
  2: FAIL (escalation required)

Output format: Trend analysis + decision markdown + JSON trend data
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
        "daily_mean": 0.0905 / 100,
        "daily_std": 0.0082,
    },
    "AMZN": {
        "model_type": "lgbm_ho",
        "oos_sharpe": 3.939,
        "max_dd": 0.063,
        "daily_mean": 0.2556 / 100,
        "daily_std": 0.015,
    },
}

TRADING_DAYS_PER_YEAR = 252

# Caution thresholds
CAUTION_Z_MIN = 1.5
CAUTION_Z_MAX = 2.5


def get_live_daily_returns(db_path: str, ticker: str, lookback_days: int = 20) -> List[float]:
    """Fetch daily returns from performance_metrics for given ticker."""
    try:
        conn = sqlite3.connect(db_path)
        since = (datetime.now(timezone.utc) - timedelta(days=lookback_days * 2)).strftime("%Y-%m-%d")

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


def calculate_z_score(live_mean: float, backtest_mean: float, backtest_std: float, n: int) -> float:
    """Calculate Z-score for live performance."""
    if n < 2:
        return 0.0
    se = backtest_std / math.sqrt(n)
    return (live_mean - backtest_mean) / se if se > 0 else 0.0


def calculate_rolling_z_scores(returns: List[float], baseline: Dict, window: int = 5) -> List[Tuple[int, float]]:
    """
    Calculate Z-scores in rolling windows.

    Returns list of (day_index, z_score) tuples showing trend over time.
    """
    z_scores = []
    for i in range(window, len(returns) + 1):
        window_returns = returns[i - window : i]
        if len(window_returns) < 2:
            continue

        mean = statistics.mean(window_returns)
        z = calculate_z_score(mean, baseline["daily_mean"], baseline["daily_std"], len(window_returns))
        z_scores.append((i, z))

    return z_scores


def analyze_trend(z_scores: List[Tuple[int, float]]) -> Tuple[str, float, str]:
    """
    Analyze Z-score trend direction.

    Returns: (trend_direction, slope, description)
    - trend_direction: "converging" | "stable" | "diverging"
    - slope: trend slope (positive = diverging worse)
    - description: human-readable summary
    """
    if len(z_scores) < 2:
        return ("insufficient", 0.0, "Not enough data points")

    # Simple linear trend: fit Z-score over time
    xs = [float(x[0]) for x in z_scores]
    ys = [x[1] for x in z_scores]

    x_mean = statistics.mean(xs)
    y_mean = statistics.mean(ys)

    numerator = sum((xs[i] - x_mean) * (ys[i] - y_mean) for i in range(len(xs)))
    denominator = sum((xs[i] - x_mean) ** 2 for i in range(len(xs)))

    slope = numerator / denominator if denominator > 0 else 0.0

    # Classify trend
    if abs(slope) < 0.01:  # Nearly flat
        trend = "stable"
    elif slope < 0:  # Decreasing toward 0
        trend = "converging"
    else:  # Increasing away from 0
        trend = "diverging"

    description = f"{trend.capitalize()} trend (slope={slope:.4f})"

    return (trend, slope, description)


def determine_decision(z_scores: List[Tuple[int, float]], trend: str, current_z: float) -> Tuple[str, str, int]:
    """
    Decision tree for June 16 checkpoint.

    Returns: (status, reasoning, exit_code)
    - status: PASS | CAUTION | FAIL
    - exit_code: 0 | 1 | 2
    """
    if not z_scores:
        return ("INSUFFICIENT", "No Z-score data available", 2)

    latest_z = z_scores[-1][1]

    # FAIL: Deteriorating — Z trending away from 0
    if trend == "diverging":
        reason = f"Z-score diverging (trend away from 0); latest Z={latest_z:.2f}"
        return ("FAIL", reason, 2)

    # CAUTION: Stable drift — Z consistently in 1.5-2.5σ range
    if trend == "stable" and CAUTION_Z_MIN < abs(latest_z) < CAUTION_Z_MAX:
        reason = f"Persistent drift (stable, Z={latest_z:.2f}); acceptable range"
        return ("CAUTION", reason, 1)

    # PASS: Metrics normalizing — Z trending toward 0 and within bounds
    if trend == "converging" or abs(latest_z) < CAUTION_Z_MIN:
        reason = f"Metrics normalizing (converging toward 0, Z={latest_z:.2f})"
        return ("PASS", reason, 0)

    # Default: stable drift outside caution range
    return ("CAUTION", f"Stable drift (Z={latest_z:.2f}); monitor", 1)


def format_ascii_chart(z_scores: List[Tuple[int, float]]) -> str:
    """
    Generate ASCII trend chart for Z-scores.

    Visual representation of Z-score evolution.
    """
    if not z_scores:
        return "No data"

    lines = []
    lines.append("Z-Score Trend Chart (ASCII):")
    lines.append("")

    # Scale: map Z-scores to chart width
    max_z = max(abs(z) for _, z in z_scores)
    if max_z == 0:
        max_z = 1.0

    chart_width = 40
    for day, z in z_scores:
        # Bar length scaled to Z-score
        bar_len = int((abs(z) / max_z) * (chart_width / 2))
        if z >= 0:
            bar = "+" * bar_len
        else:
            bar = "-" * bar_len

        lines.append(f"Day {day:2d}: {bar:^{chart_width}} Z={z:+.2f}")

    lines.append("")
    return "\n".join(lines)


def format_markdown_report(results: Dict) -> str:
    """Format trend analysis report as markdown for WORKLOG.md entry."""
    lines = [
        "## June 16 Checkpoint — Mid-Window Trend Validation",
        "",
        "| Ticker | Days | Latest Z | Trend | Direction | Decision | Action |",
        "|--------|------|----------|-------|-----------|----------|--------|",
    ]

    for ticker, data in results.items():
        if ticker == "ERROR":
            continue

        status = data["status"]
        emoji = "✅" if status == "PASS" else ("⚠️" if status == "CAUTION" else "❌")

        lines.append(
            f"| {ticker} | {data['num_days']} | {data['latest_z']:+.2f} | "
            f"{data['trend']} | {data['trend_desc']} | "
            f"{emoji} {status} | {data['action']} |"
        )

    lines.append("")
    lines.append("### Trend Analysis")
    lines.append("")

    for ticker, data in results.items():
        if ticker == "ERROR":
            lines.append(f"**ERROR**: {data}")
            continue

        lines.append(f"**{ticker}**: {data['status']}")
        lines.append(f"- Latest Z-score: {data['latest_z']:+.2f}")
        lines.append(f"- Trend: {data['trend_desc']}")
        lines.append(f"- Slope: {data['slope']:.4f}")
        lines.append(f"- Days tracked: {data['num_days']}")
        lines.append(f"- Decision: {data['reasoning']}")
        lines.append("")

    return "\n".join(lines)


def main():
    """Main execution."""
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
            # Fetch live returns for 10+ trading days (June 2-13)
            returns = get_live_daily_returns(db_path, ticker, lookback_days=15)
            returns = returns[:15]

            if not returns or len(returns) < 5:
                print(f"WARNING: Insufficient data for {ticker} (only {len(returns)} days)", file=sys.stderr)
                results[ticker] = {
                    "status": "INSUFFICIENT",
                    "num_days": len(returns),
                    "latest_z": 0.0,
                    "trend": "unknown",
                    "trend_desc": "Insufficient data",
                    "slope": 0.0,
                    "reasoning": "Not enough trading days",
                    "action": "Await more data",
                }
                continue

            # Calculate rolling Z-scores (5-day window)
            z_scores = calculate_rolling_z_scores(returns, baseline, window=5)

            if not z_scores:
                results[ticker] = {
                    "status": "INSUFFICIENT",
                    "num_days": len(returns),
                    "latest_z": 0.0,
                    "trend": "unknown",
                    "trend_desc": "Cannot compute Z-scores",
                    "slope": 0.0,
                    "reasoning": "Data quality issue",
                    "action": "Investigate data",
                }
                continue

            # Analyze trend
            trend, slope, trend_desc = analyze_trend(z_scores)

            # Determine decision
            status, reasoning, code = determine_decision(z_scores, trend, z_scores[-1][1])

            # Action based on status
            if status == "PASS":
                action = "Continue; plan June 23 assessment"
            elif status == "CAUTION":
                action = "Acceptable; monitor closely"
            else:  # FAIL
                action = "Escalation required; review strategy"

            latest_z = z_scores[-1][1]

            results[ticker] = {
                "status": status,
                "num_days": len(returns),
                "latest_z": latest_z,
                "trend": trend,
                "trend_desc": trend_desc,
                "slope": slope,
                "reasoning": reasoning,
                "action": action,
            }

            if code > exit_code:
                exit_code = code

            print(
                f"{ticker}: {status} | Trend: {trend} (slope={slope:.4f}) | "
                f"Latest Z: {latest_z:+.2f} | Days: {len(returns)}"
            )

        except Exception as e:
            print(f"ERROR processing {ticker}: {e}", file=sys.stderr)
            results["ERROR"] = str(e)
            exit_code = 2

    # Output report
    print("\n" + format_markdown_report(results))

    # Output JSON for programmatic access
    json_output = {
        "checkpoint_date": "2026-06-16",
        "results": results,
    }
    print("\n### JSON Data")
    print("```json")
    print(json.dumps(json_output, indent=2))
    print("```")

    # Write to WORKLOG.md
    worklog_path = repo_root / "projects/stockbot/WORKLOG.md"
    if worklog_path.exists():
        try:
            with open(worklog_path, "a") as f:
                f.write("\n\n" + format_markdown_report(results))
            print(f"\nAppended to {worklog_path}")
        except Exception as e:
            print(f"WARNING: Could not write to WORKLOG.md: {e}", file=sys.stderr)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
