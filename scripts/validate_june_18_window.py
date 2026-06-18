#!/usr/bin/env python3
"""
Validation monitoring for June 18 stockbot market window (13:30-20:00 UTC).

Monitors Docker logs and database metrics during the validation window.
Sends Discord alerts at key checkpoints (HMM prime 14:15 UTC, window close 20:00 UTC).
Collects metrics for post-window analysis.
"""

import os
import sys
import json
import sqlite3
import subprocess
from datetime import datetime, timedelta
from pathlib import Path
import time

# Configuration
JETSON_HOST = "100.120.18.84"
JETSON_USER = "awank"
DATABASE_PATH = "/home/awank/dev/SuperClaude_Framework/projects/stockbot/database/stockbot.db"
LOG_OUTPUT = "/home/awank/dev/SuperClaude_Framework/projects/stockbot/VALIDATION_MONITORING_LOG.txt"
DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL")

# Validation window
WINDOW_START = datetime(2026, 6, 18, 13, 30, 0)  # UTC
WINDOW_END = datetime(2026, 6, 18, 20, 0, 0)    # UTC
HMM_PRIME_CHECKPOINT = datetime(2026, 6, 18, 14, 15, 0)  # UTC
ANALYSIS_TIME = datetime(2026, 6, 18, 20, 15, 0)  # UTC

# Success thresholds (from JUNE_18_VALIDATION_OUTCOME_REPORT.md)
PASS_THRESHOLD = 4  # ≥4 sessions must PASS
CAUTION_MIN = 2  # 2-3 sessions PASS
MIN_TRADES_PER_SESSION = 5
MIN_SIGNAL_HEALTH = 4.0
SESSIONS = ["aapl_lgbm_ho_001", "msft_lgbm_ho_001", "nvda_lgbm_ho_001", "amzn_lgbm_ho_001", "jpm_ridge_wf_001"]


def log_message(message):
    """Log message to stdout and file."""
    timestamp = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] {message}"
    print(line)
    with open(LOG_OUTPUT, "a") as f:
        f.write(line + "\n")


def send_discord_alert(title, message, color=3447003):  # blue by default
    """Send Discord embed alert."""
    if not DISCORD_WEBHOOK:
        log_message("⚠️ DISCORD_WEBHOOK_URL not set; skipping Discord notification")
        return

    try:
        payload = {
            "embeds": [{
                "title": title,
                "description": message,
                "color": color,
                "timestamp": datetime.utcnow().isoformat() + "Z"
            }]
        }
        subprocess.run(
            ["curl", "-s", "-H", "Content-Type: application/json",
             "-d", json.dumps(payload), DISCORD_WEBHOOK],
            check=False
        )
        log_message(f"✅ Discord alert sent: {title}")
    except Exception as e:
        log_message(f"❌ Discord alert failed: {e}")


def fetch_docker_logs_metric(since_minutes=30):
    """Fetch Docker logs from Jetson and extract key metrics."""
    try:
        # SSH into Jetson and fetch last N minutes of logs
        cmd = [
            "ssh", f"{JETSON_USER}@{JETSON_HOST}",
            f"docker logs stockbot --since {since_minutes}m 2>&1 | tail -500"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=10)
        logs = result.stdout

        # Count 40010001 errors
        error_count = logs.count("40010001")

        # Check for regime priming messages
        primed_sessions = {}
        for session in SESSIONS:
            if f"Primed {session}" in logs or f"Priming {session}" in logs:
                primed_sessions[session] = True

        # Extract latest buy_prob values (best effort)
        buy_prob_values = {}
        for session in SESSIONS:
            # Look for patterns like "buy_prob=0.1234"
            import re
            pattern = rf"({session}).*buy_prob=([0-9.]+)"
            matches = re.findall(pattern, logs)
            if matches:
                buy_prob_values[session] = float(matches[-1][1])  # Last occurrence

        return {
            "errors_40010001": error_count,
            "primed_sessions": primed_sessions,
            "buy_prob_values": buy_prob_values,
            "raw_logs_lines": len(logs.split("\n"))
        }
    except Exception as e:
        log_message(f"❌ Error fetching Docker logs: {e}")
        return {"error": str(e)}


def fetch_db_metrics():
    """Query database for validation metrics."""
    try:
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        # Trade count per session (today only)
        cursor.execute("""
            SELECT
                strategy_name,
                COUNT(*) as trade_count,
                SUM(CASE WHEN side = 'buy' THEN 1 ELSE 0 END) as buys,
                SUM(CASE WHEN side = 'sell' THEN 1 ELSE 0 END) as sells,
                MIN(filled_at) as first_fill,
                MAX(filled_at) as last_fill
            FROM trades
            WHERE DATE(filled_at) = '2026-06-18'
            GROUP BY strategy_name
            ORDER BY strategy_name
        """)
        trades = {row['strategy_name']: dict(row) for row in cursor.fetchall()}

        # Signal health metrics
        cursor.execute("""
            SELECT
                strategy_name,
                COUNT(*) as signal_count,
                MIN(buy_prob) as buy_prob_min,
                MAX(buy_prob) as buy_prob_max,
                AVG(buy_prob) as buy_prob_avg,
                SUM(CASE WHEN hmm_regime IS NOT NULL THEN 1 ELSE 0 END) as regimes_active
            FROM signals
            WHERE DATE(generated_at) = '2026-06-18'
              AND buy_prob IS NOT NULL
            GROUP BY strategy_name
            ORDER BY strategy_name
        """)
        signals = {row['strategy_name']: dict(row) for row in cursor.fetchall()}

        conn.close()

        return {
            "trades": trades,
            "signals": signals
        }
    except Exception as e:
        log_message(f"❌ Error querying database: {e}")
        return {"error": str(e)}


def check_hmm_prime():
    """Check if HMM regimes are initialized (not None)."""
    try:
        logs = fetch_docker_logs_metric(since_minutes=60)
        primed = logs.get("primed_sessions", {})

        primed_count = sum(1 for v in primed.values() if v)
        status = "✅ GOOD" if primed_count >= 3 else "⚠️ CAUTION"

        message = f"{primed_count}/5 sessions HMM primed. Status: {status}"
        log_message(f"[HMM PRIME CHECKPOINT] {message}")

        if primed_count >= 3:
            send_discord_alert(
                "✅ HMM Prime Checkpoint (14:15 UTC)",
                f"{primed_count}/5 sessions successfully primed with regime detection.",
                color=3066993  # green
            )
        else:
            send_discord_alert(
                "⚠️ HMM Prime Checkpoint (14:15 UTC)",
                f"Only {primed_count}/5 sessions primed. Monitor closely.",
                color=15105570  # yellow
            )

        return primed_count >= 3
    except Exception as e:
        log_message(f"❌ HMM prime check failed: {e}")
        return False


def run_window_monitoring():
    """Run continuous monitoring during the validation window."""
    log_message("=" * 60)
    log_message("🚀 JUNE 18 VALIDATION WINDOW MONITORING STARTED")
    log_message(f"Window: {WINDOW_START} to {WINDOW_END} UTC")
    log_message("=" * 60)

    send_discord_alert(
        "🚀 Validation Window Open (13:30 UTC)",
        "5-session stockbot validation started. Monitoring active.",
        color=3066993  # green
    )

    now = datetime.utcnow()

    # Check HMM prime at 14:15 UTC
    if now >= HMM_PRIME_CHECKPOINT and now < (HMM_PRIME_CHECKPOINT + timedelta(minutes=5)):
        log_message("\n[CHECKPOINT] HMM Prime (14:15 UTC)")
        check_hmm_prime()

    # Periodic monitoring (every 15 minutes during window)
    if WINDOW_START <= now <= WINDOW_END:
        metrics = fetch_db_metrics()
        logs = fetch_docker_logs_metric(since_minutes=30)

        # Log summary
        log_message("\n[METRICS] Database snapshot:")
        if "trades" in metrics:
            for session, data in metrics["trades"].items():
                log_message(f"  {session}: {data.get('trade_count', 0)} trades")

        if "signals" in metrics:
            for session, data in metrics["signals"].items():
                buy_prob_avg = data.get('buy_prob_avg', 0)
                log_message(f"  {session}: avg buy_prob={buy_prob_avg:.4f}")

        log_message(f"\n[METRICS] Docker logs: {logs.get('errors_40010001', 0)} 40010001 errors")

    # Window closure analysis at 20:00 UTC
    if now >= WINDOW_END and now < (WINDOW_END + timedelta(minutes=5)):
        log_message("\n" + "=" * 60)
        log_message("📊 VALIDATION WINDOW CLOSED — ANALYSIS PHASE")
        log_message("=" * 60)

        send_discord_alert(
            "📊 Validation Window Closed (20:00 UTC)",
            "Validation monitoring complete. Analysis report being generated.",
            color=3447003  # blue
        )

        # Collect final metrics
        final_metrics = fetch_db_metrics()
        final_logs = fetch_docker_logs_metric(since_minutes=360)  # Last 6 hours

        # Tally results
        passed_sessions = 0
        results = {}

        if "trades" in final_metrics:
            for session in SESSIONS:
                trade_data = final_metrics["trades"].get(session, {})
                trade_count = trade_data.get('trade_count', 0)
                passed = trade_count >= MIN_TRADES_PER_SESSION
                results[session] = {
                    "trades": trade_count,
                    "passed": passed
                }
                if passed:
                    passed_sessions += 1

        # Verdict
        if passed_sessions >= PASS_THRESHOLD:
            verdict = "PASS"
            color = 3066993  # green
            message = f"{passed_sessions}/{len(SESSIONS)} sessions PASSED validation. Phase 4 GREEN LIGHT."
        elif passed_sessions >= CAUTION_MIN:
            verdict = "CAUTION"
            color = 15105570  # yellow
            message = f"{passed_sessions}/{len(SESSIONS)} sessions passed. Investigate before Phase 4."
        else:
            verdict = "FAIL"
            color = 15158332  # red
            message = f"Only {passed_sessions} sessions passed. Rollback recommended."

        log_message(f"\n🎯 VERDICT: {verdict}")
        log_message(f"Sessions passed: {passed_sessions}/{len(SESSIONS)}")
        log_message(f"Details: {results}")

        send_discord_alert(
            f"📊 Validation Verdict: {verdict}",
            message,
            color=color
        )

        log_message(f"\n✅ Monitoring log written to: {LOG_OUTPUT}")
        log_message("ℹ️  Next step: Run JUNE_18_VALIDATION_OUTCOME_REPORT.md fill-in at 20:15 UTC")
        return verdict

    return None


if __name__ == "__main__":
    # Initialize log
    Path(LOG_OUTPUT).parent.mkdir(parents=True, exist_ok=True)

    # Check current time and run appropriate action
    now = datetime.utcnow()

    if now < WINDOW_START:
        log_message(f"⏳ Validation window starts at {WINDOW_START} UTC ({(WINDOW_START - now).total_seconds() / 3600:.1f}h from now)")
        log_message("Run this script again during the window (13:30–20:00 UTC)")
        sys.exit(0)

    # Run monitoring
    result = run_window_monitoring()

    if result:
        sys.exit(0)
    elif now > WINDOW_END + timedelta(hours=1):
        log_message("⚠️ Validation window closed >1 hour ago. Run manual analysis instead.")
        sys.exit(1)
    else:
        sys.exit(0)
