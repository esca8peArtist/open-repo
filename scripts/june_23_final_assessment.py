#!/usr/bin/env python3
"""
June 23 Final Assessment Script — Phase 4.4 Activation Gate.

Reads full 15+ trading days of live P&L data (June 2-23) and evaluates against
pass/fail criteria to determine Phase 4.4 activation vs Phase 4.3 extension.

Pass Criteria (Phase 4.4 activation):
  - Total return > 0% (profitable)
  - Sharpe ratio > 1.0 (acceptable risk-adjusted returns)
  - Max drawdown < 15% (portfolio preservation)
  - Outperformance convergence (Z-score normalizing)

Fail Criteria (extend Phase 4.3 or escalate):
  - Total return < -5% (significant loss)
  - Sharpe ratio < 0.5 (poor risk-adjusted)
  - Max drawdown > 20% (concerning loss)
  - Negative outperformance drift

Exit codes:
  0: ACTIVATE Phase 4.4
  1: EXTEND Phase 4.3
  2: ERROR/ESCALATE

Output: Comprehensive report + activation decision
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
        "expected_monthly_return": 0.0905 * 21 / 100,  # ~1.9% for 21 trading days
    },
    "AMZN": {
        "model_type": "lgbm_ho",
        "oos_sharpe": 3.939,
        "max_dd": 0.063,
        "daily_mean": 0.2556 / 100,
        "daily_std": 0.015,
        "expected_monthly_return": 0.2556 * 21 / 100,  # ~5.4% for 21 trading days
    },
}

TRADING_DAYS_PER_YEAR = 252

# Pass/Fail criteria
MIN_TOTAL_RETURN = 0.00  # 0%
MIN_SHARPE = 1.0
MAX_DRAWDOWN = 0.15  # 15%

FAIL_TOTAL_RETURN = -0.05  # -5%
FAIL_SHARPE = 0.5
FAIL_MAX_DRAWDOWN = 0.20  # 20%


def get_live_daily_returns(db_path: str, ticker: str, lookback_days: int = 30) -> List[Tuple[str, float]]:
    """
    Fetch daily returns from performance_metrics, including dates.

    Returns list of (date_str, daily_return) tuples, oldest-first.
    """
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

        returns = [(r[0], float(r[1])) for r in rows if r[1] is not None]

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
            for day, day_pnl, day_notional in rows:
                if day_notional and day_notional > 0:
                    returns.append((day, float(day_pnl) / float(day_notional)))

        conn.close()
        return returns
    except Exception as e:
        print(f"ERROR: Failed to fetch returns for {ticker}: {e}", file=sys.stderr)
        return []


def calculate_metrics(returns: List[Tuple[str, float]]) -> Dict:
    """
    Calculate comprehensive metrics from return series.

    Returns dict with: sharpe, max_dd, total_return, win_rate, num_days, dates
    """
    if not returns or len(returns) < 1:
        return {
            "sharpe": 0.0,
            "max_dd": 0.0,
            "total_return": 0.0,
            "win_rate": 0.0,
            "num_days": 0,
            "mean": 0.0,
            "std": 0.0,
            "dates": [],
        }

    dates = [r[0] for r in returns]
    values = [r[1] for r in returns]

    # Total return (product of daily returns)
    total_return = 1.0
    for v in values:
        total_return *= (1.0 + v)
    total_return -= 1.0

    # Mean and std
    mean = statistics.mean(values)
    std = statistics.stdev(values) if len(values) >= 2 else 0.0

    # Annualized Sharpe
    sharpe = 0.0
    if std > 0:
        sharpe = mean / std * math.sqrt(TRADING_DAYS_PER_YEAR)

    # Max underwater drawdown
    cumulative = 0.0
    peak = 0.0
    max_dd = 0.0
    for v in values:
        cumulative += v
        if cumulative > peak:
            peak = cumulative
        dd = peak - cumulative
        if dd > max_dd:
            max_dd = dd

    # Win rate
    win_rate = sum(1 for v in values if v > 0) / len(values) if values else 0.0

    return {
        "sharpe": sharpe,
        "max_dd": max_dd,
        "total_return": total_return,
        "win_rate": win_rate,
        "num_days": len(values),
        "mean": mean,
        "std": std,
        "dates": dates,
    }


def calculate_z_score(live_mean: float, backtest_mean: float, backtest_std: float, n: int) -> float:
    """Calculate Z-score for live performance."""
    if n < 2:
        return 0.0
    se = backtest_std / math.sqrt(n)
    return (live_mean - backtest_mean) / se if se > 0 else 0.0


def evaluate_pass_criteria(metrics: Dict, baseline: Dict) -> Tuple[bool, List[str]]:
    """
    Evaluate Phase 4.4 activation pass criteria.

    Returns: (pass, list_of_issues)
    """
    issues = []

    # Total return > 0%
    if metrics["total_return"] < MIN_TOTAL_RETURN:
        issues.append(f"Total return {metrics['total_return']:.2%} < {MIN_TOTAL_RETURN:.2%}")

    # Sharpe > 1.0
    if metrics["sharpe"] < MIN_SHARPE:
        issues.append(f"Sharpe {metrics['sharpe']:.2f} < {MIN_SHARPE:.2f}")

    # Max drawdown < 15%
    if metrics["max_dd"] > MAX_DRAWDOWN:
        issues.append(f"Max DD {metrics['max_dd']:.2%} > {MAX_DRAWDOWN:.2%}")

    # Outperformance convergence: Z-score reasonable
    z_score = calculate_z_score(
        metrics["mean"],
        baseline["daily_mean"],
        baseline["daily_std"],
        metrics["num_days"],
    )
    if abs(z_score) > 3.0:
        issues.append(f"Z-score {z_score:.2f} indicates significant divergence")

    return (len(issues) == 0, issues)


def evaluate_fail_criteria(metrics: Dict, baseline: Dict) -> Tuple[bool, List[str]]:
    """
    Evaluate Phase 4.3 extension fail criteria.

    Returns: (fail, list_of_failures)
    """
    failures = []

    # Total return < -5%
    if metrics["total_return"] < FAIL_TOTAL_RETURN:
        failures.append(f"Total return {metrics['total_return']:.2%} < {FAIL_TOTAL_RETURN:.2%}")

    # Sharpe < 0.5
    if metrics["sharpe"] < FAIL_SHARPE:
        failures.append(f"Sharpe {metrics['sharpe']:.2f} < {FAIL_SHARPE:.2f}")

    # Max drawdown > 20%
    if metrics["max_dd"] > FAIL_MAX_DRAWDOWN:
        failures.append(f"Max DD {metrics['max_dd']:.2%} > {FAIL_MAX_DRAWDOWN:.2%}")

    return (len(failures) > 0, failures)


def determine_decision(metrics: Dict, baseline: Dict) -> Tuple[str, str, int]:
    """
    Decision tree for Phase 4.4 activation.

    Returns: (decision, reasoning, exit_code)
    - decision: ACTIVATE | EXTEND | ESCALATE
    - exit_code: 0 (activate) | 1 (extend) | 2 (escalate)
    """
    if metrics["num_days"] < 5:
        return ("ESCALATE", "Insufficient trading days for final assessment", 2)

    # Check fail criteria first
    is_fail, fail_reasons = evaluate_fail_criteria(metrics, baseline)
    if is_fail:
        reason = "Fail criteria met: " + "; ".join(fail_reasons)
        return ("EXTEND", reason, 1)

    # Check pass criteria
    is_pass, pass_issues = evaluate_pass_criteria(metrics, baseline)
    if is_pass:
        return ("ACTIVATE", "All pass criteria met; ready for Phase 4.4", 0)

    # Intermediate: issues but not critical
    if pass_issues:
        reason = "Pass criteria not fully met: " + "; ".join(pass_issues) + "; monitor and retry"
        return ("EXTEND", reason, 1)

    # Safe default
    return ("EXTEND", "Caution: monitor performance", 1)


def format_comprehensive_report(results: Dict) -> str:
    """Format final assessment report as markdown."""
    lines = [
        "## June 23 Final Assessment — Phase 4.4 Activation Gate",
        "",
        "| Ticker | Days | Total Return | Sharpe | Max DD | Z-Score | Decision |",
        "|--------|------|--------------|--------|--------|---------|----------|",
    ]

    for ticker, data in results.items():
        if ticker == "ERROR":
            continue

        decision = data["decision"]
        emoji = "🚀" if decision == "ACTIVATE" else ("⏸️" if decision == "EXTEND" else "⛔")

        lines.append(
            f"| {ticker} | {data['num_days']} | {data['total_return']:+.2%} | "
            f"{data['sharpe']:.2f} | {data['max_dd']:.2%} | {data['z_score']:+.2f} | "
            f"{emoji} {decision} |"
        )

    lines.append("")
    lines.append("### Detailed Assessment")
    lines.append("")

    for ticker, data in results.items():
        if ticker == "ERROR":
            lines.append(f"**ERROR**: {data}")
            continue

        decision = data["decision"]
        lines.append(f"**{ticker}** ({data['model_type']})")
        lines.append(f"- Decision: **{decision}**")
        lines.append(f"- Total Return: {data['total_return']:+.2%} (expected ~{data['expected_return']:+.2%})")
        lines.append(f"- Sharpe Ratio: {data['sharpe']:.2f} (target > {data['min_sharpe']:.2f})")
        lines.append(f"- Max Drawdown: {data['max_dd']:.2%} (limit < {data['max_dd_limit']:.2%})")
        lines.append(f"- Z-Score: {data['z_score']:+.2f} (normalcy check)")
        lines.append(f"- Win Rate: {data['win_rate']:.1%}")
        lines.append(f"- Trading Days: {data['num_days']}")
        lines.append(f"- Reasoning: {data['reasoning']}")
        lines.append("")

    lines.append("### Decision Summary")
    lines.append("")

    # Aggregate decision
    decisions = [data["decision"] for ticker, data in results.items() if ticker != "ERROR"]
    if "ESCALATE" in decisions:
        aggregate = "ESCALATE — Manual intervention required"
    elif all(d == "ACTIVATE" for d in decisions):
        aggregate = "ACTIVATE — Phase 4.4 ready"
    else:
        aggregate = "EXTEND — Continue Phase 4.3 monitoring"

    lines.append(f"**Aggregate Decision**: {aggregate}")
    lines.append("")

    # Pass criteria summary
    lines.append("### Pass Criteria Check")
    lines.append("")
    lines.append(f"- Minimum total return: {MIN_TOTAL_RETURN:.2%}")
    lines.append(f"- Minimum Sharpe ratio: {MIN_SHARPE:.2f}")
    lines.append(f"- Maximum drawdown: {MAX_DRAWDOWN:.2%}")
    lines.append("")

    # Fail criteria summary
    lines.append("### Fail Criteria Check")
    lines.append("")
    lines.append(f"- Critical total return: {FAIL_TOTAL_RETURN:.2%}")
    lines.append(f"- Critical Sharpe ratio: {FAIL_SHARPE:.2f}")
    lines.append(f"- Critical drawdown: {FAIL_MAX_DRAWDOWN:.2%}")

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
            # Fetch live returns for full 15+ trading days (June 2-23)
            returns = get_live_daily_returns(db_path, ticker, lookback_days=25)
            returns = returns[:21]  # Cap to ~3 weeks

            if not returns or len(returns) < 5:
                print(f"WARNING: Insufficient data for {ticker} ({len(returns)} days)", file=sys.stderr)
                results[ticker] = {
                    "decision": "ESCALATE",
                    "num_days": len(returns),
                    "total_return": 0.0,
                    "sharpe": 0.0,
                    "max_dd": 0.0,
                    "z_score": 0.0,
                    "win_rate": 0.0,
                    "model_type": baseline["model_type"],
                    "expected_return": baseline["expected_monthly_return"],
                    "min_sharpe": MIN_SHARPE,
                    "max_dd_limit": MAX_DRAWDOWN,
                    "reasoning": "Insufficient trading data for final assessment",
                }
                exit_code = 2
                continue

            # Calculate comprehensive metrics
            metrics = calculate_metrics(returns)

            # Calculate Z-score
            z_score = calculate_z_score(
                metrics["mean"],
                baseline["daily_mean"],
                baseline["daily_std"],
                metrics["num_days"],
            )

            # Determine decision
            decision, reasoning, code = determine_decision(metrics, baseline)

            results[ticker] = {
                "decision": decision,
                "num_days": metrics["num_days"],
                "total_return": metrics["total_return"],
                "sharpe": metrics["sharpe"],
                "max_dd": metrics["max_dd"],
                "z_score": z_score,
                "win_rate": metrics["win_rate"],
                "model_type": baseline["model_type"],
                "expected_return": baseline["expected_monthly_return"],
                "min_sharpe": MIN_SHARPE,
                "max_dd_limit": MAX_DRAWDOWN,
                "reasoning": reasoning,
            }

            if code > exit_code:
                exit_code = code

            print(
                f"{ticker}: {decision} | Return: {metrics['total_return']:+.2%} | "
                f"Sharpe: {metrics['sharpe']:.2f} | DD: {metrics['max_dd']:.2%} | "
                f"Days: {metrics['num_days']}"
            )

        except Exception as e:
            print(f"ERROR processing {ticker}: {e}", file=sys.stderr)
            results["ERROR"] = str(e)
            exit_code = 2

    # Output comprehensive report
    print("\n" + format_comprehensive_report(results))

    # Output JSON for programmatic access
    json_output = {
        "checkpoint_date": "2026-06-23",
        "aggregate_decision": (
            "ACTIVATE" if all(r["decision"] == "ACTIVATE" for t, r in results.items() if t != "ERROR")
            else ("ESCALATE" if any(r["decision"] == "ESCALATE" for t, r in results.items() if t != "ERROR")
            else "EXTEND")
        ),
        "results": results,
    }
    print("\n### JSON Output")
    print("```json")
    print(json.dumps(json_output, indent=2))
    print("```")

    # Write to WORKLOG.md
    worklog_path = repo_root / "projects/stockbot/WORKLOG.md"
    if worklog_path.exists():
        try:
            with open(worklog_path, "a") as f:
                f.write("\n\n" + format_comprehensive_report(results))
            print(f"\nAppended to {worklog_path}")
        except Exception as e:
            print(f"WARNING: Could not write to WORKLOG.md: {e}", file=sys.stderr)

    sys.exit(exit_code)


if __name__ == "__main__":
    main()
