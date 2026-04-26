#!/usr/bin/env python3
"""
Stockbot Discord monitor.
Polls the paper trading status every 60s and sends a Discord notification
whenever signals change, trades execute, or sessions start/stop.
"""

import json
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

API_BASE = "http://100.120.18.84:8000"
API_KEY = "9dc5633ed026d9c818417ac0cba43f521e4ffa7cd2cca8b7e272da8e2ca89479"
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1492974312188018780/Cf54p5vEUbbOeu7o1Eq3HrqD7nCM1KGklL018uRdroruRdg9PpVtNz0sbrbh4ze_LX_Y"
STATE_FILE = Path("/tmp/stockbot-monitor-state.json")
POLL_INTERVAL = 60  # seconds


def api_get(path):
    req = urllib.request.Request(
        f"{API_BASE}{path}",
        headers={"Authorization": f"Bearer {API_KEY}"},
    )
    with urllib.request.urlopen(req, timeout=10) as resp:
        return json.loads(resp.read())


def send_discord(message):
    payload = json.dumps({"content": message}).encode()
    req = urllib.request.Request(
        DISCORD_WEBHOOK,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        urllib.request.urlopen(req, timeout=10)
    except Exception as e:
        print(f"[{now()}] Discord send failed: {e}")


def now():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def load_state():
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text())
        except Exception:
            pass
    return {}


def save_state(state):
    STATE_FILE.write_text(json.dumps(state))


SIGNAL_EMOJI = {"buy": "🟢", "sell": "🔴", "hold": "⚪"}
STRATEGY_LABEL = {
    "momentum": "Momentum",
    "rsi_mean_reversion": "RSI MeanRev",
    "sma_crossover": "SMA Cross",
}


def format_indicators(indicators):
    parts = []
    if "momentum_21d_pct" in indicators:
        parts.append(f"mom={indicators['momentum_21d_pct']:+.2f}%")
    if "rsi_14" in indicators:
        parts.append(f"RSI={indicators['rsi_14']:.1f}")
    if "sma_fast_10" in indicators and "sma_slow_50" in indicators:
        parts.append(
            f"SMA10={indicators['sma_fast_10']:.2f} SMA50={indicators['sma_slow_50']:.2f}"
        )
    if "close_price" in indicators:
        parts.append(f"@${indicators['close_price']:.2f}")
    return " | ".join(parts)


def check_and_notify(sessions, prev_state):
    messages = []

    for sid, session in sessions.items():
        strategy = session.get("strategy", sid)
        label = STRATEGY_LABEL.get(strategy, strategy)
        result = session.get("last_cycle_result") or {}
        signals = result.get("signals", {})
        trades = session.get("trades_executed", 0)
        status = session.get("status", "unknown")

        prev = prev_state.get(sid, {})
        prev_signals = prev.get("signals", {})
        prev_trades = prev.get("trades", 0)
        prev_status = prev.get("status", "unknown")

        # Session status changed
        if prev_status and prev_status != status:
            messages.append(
                f"**[Stockbot]** {label} session {status.upper()} (was {prev_status})"
            )

        # New trades executed
        if trades > prev_trades:
            new_count = trades - prev_trades
            messages.append(
                f"**[Stockbot]** {label}: {new_count} new trade(s) executed "
                f"(total: {trades})"
            )

        # Signal changes per ticker
        for ticker, sig_data in signals.items():
            signal = sig_data.get("signal", "hold")
            reason = sig_data.get("reason", "")
            indicators = sig_data.get("indicators", {})
            prev_signal = prev_signals.get(ticker, {}).get("signal")

            if prev_signal is not None and prev_signal != signal:
                emoji = SIGNAL_EMOJI.get(signal, "❓")
                ind_str = format_indicators(indicators)
                messages.append(
                    f"**[Stockbot]** {emoji} **{ticker}** ({label}): "
                    f"`{prev_signal}` → `{signal}`\n"
                    f"> {reason}\n"
                    f"> {ind_str}"
                )

    return messages


def snapshot_state(sessions):
    state = {}
    for sid, session in sessions.items():
        result = session.get("last_cycle_result") or {}
        signals = result.get("signals", {})
        state[sid] = {
            "status": session.get("status"),
            "trades": session.get("trades_executed", 0),
            "signals": {
                ticker: {"signal": sig.get("signal")}
                for ticker, sig in signals.items()
            },
        }
    return state


def main():
    print(f"[{now()}] Stockbot monitor starting. Polling every {POLL_INTERVAL}s.")
    send_discord(
        "**[Stockbot Monitor]** Started — watching momentum, RSI mean reversion, "
        "SMA crossover sessions. Will notify on signal changes and trades."
    )

    prev_state = load_state()

    while True:
        try:
            data = api_get("/api/paper-trading/status")
            sessions = data.get("sessions", {})

            if not sessions:
                print(f"[{now()}] No active sessions found.")
            else:
                messages = check_and_notify(sessions, prev_state)
                for msg in messages:
                    print(f"[{now()}] Sending: {msg[:120]}")
                    send_discord(msg)

                prev_state = snapshot_state(sessions)
                save_state(prev_state)

        except urllib.error.URLError as e:
            print(f"[{now()}] API unreachable: {e}")
        except Exception as e:
            print(f"[{now()}] Error: {e}")

        time.sleep(POLL_INTERVAL)


if __name__ == "__main__":
    main()
