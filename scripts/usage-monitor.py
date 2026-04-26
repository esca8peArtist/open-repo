#!/usr/bin/env python3
"""
usage-monitor.py — Periodic usage monitor with Discord alerts and 80% pause gate.

Run every 30 minutes via cron. Tracks which 10% thresholds have fired this
billing week and sends Discord alerts for each new one. Creates USAGE_PAUSE
at 80% to hold the orchestrator; revokes user override at 90%.

State is stored in WORKSPACE/.usage-monitor-state.json (reset each Tuesday).

Exit codes:
  0 — ran normally (does not indicate usage is OK — use usage-check.py --check)
  1 — error
"""

import json
import os
import sys
import subprocess
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STATE_FILE  = REPO_ROOT / ".usage-monitor-state.json"
PAUSE_FILE  = REPO_ROOT / "USAGE_PAUSE"
OVERRIDE_FILE = REPO_ROOT / "USAGE_PAUSE_OVERRIDE"
LOG_FILE    = REPO_ROOT / "orchestrator.log"

DISCORD_WEBHOOK = os.environ.get("DISCORD_WEBHOOK_URL", "")


# ── Helpers ───────────────────────────────────────────────────────────────────

def log(msg: str) -> None:
    ts = datetime.now().strftime("%a %d %b %H:%M:%S %Z %Y")
    line = f"[{ts}] usage-monitor: {msg}"
    print(line)
    try:
        with open(LOG_FILE, "a") as f:
            f.write(line + "\n")
    except OSError:
        pass


def discord(msg: str) -> None:
    if not DISCORD_WEBHOOK:
        return
    payload = json.dumps({"content": msg})
    try:
        subprocess.run(
            ["curl", "-s", "-H", "Content-Type: application/json",
             "-d", payload, DISCORD_WEBHOOK],
            capture_output=True, timeout=10
        )
    except Exception:
        pass


def current_week() -> str:
    today = datetime.now(timezone.utc).date()
    iso = today.isocalendar()
    return f"{iso[0]}-W{iso[1]:02d}"


def load_state() -> dict:
    try:
        if STATE_FILE.exists():
            return json.loads(STATE_FILE.read_text())
    except Exception:
        pass
    return {"week": "", "notified_thresholds": [], "paused": False}


def save_state(state: dict) -> None:
    try:
        STATE_FILE.write_text(json.dumps(state, indent=2))
    except Exception as e:
        log(f"WARNING: could not save state: {e}")


def get_usage() -> dict | None:
    """Run usage-check.py --json and return the parsed report."""
    try:
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "usage-check.py"), "--json"],
            capture_output=True, text=True, timeout=30
        )
        if result.returncode == 0:
            return json.loads(result.stdout)
    except Exception as e:
        log(f"ERROR reading usage: {e}")
    return None


def threshold_emoji(pct: float) -> str:
    if pct >= 90:
        return "🔴"
    if pct >= 80:
        return "🟠"
    if pct >= 60:
        return "🟡"
    return "🟢"


# ── Main ──────────────────────────────────────────────────────────────────────

def main() -> None:
    week = current_week()
    state = load_state()

    # ── New week: reset state and clear pause files ────────────────────────────
    if state["week"] != week:
        log(f"New billing week detected ({week}). Resetting monitor state.")
        state = {"week": week, "notified_thresholds": [], "paused": False}
        PAUSE_FILE.unlink(missing_ok=True)
        OVERRIDE_FILE.unlink(missing_ok=True)
        save_state(state)

    # ── Get current usage ──────────────────────────────────────────────────────
    report = get_usage()
    if report is None:
        log("Could not retrieve usage report — skipping.")
        return

    sonnet_pct   = report["pct"]["sonnet"]
    all_pct      = report["pct"]["all_models"]
    hours_left   = report["hours_until_reset"]
    sonnet_used  = report["usage"]["sonnet_output"]
    sonnet_limit = report["limits"]["sonnet"]
    all_used     = report["usage"]["total_output"]
    all_limit    = report["limits"]["all_models"]

    # Binding constraint is whichever is higher
    effective_pct = max(sonnet_pct, all_pct)

    log(f"Usage: Sonnet={sonnet_pct:.1f}%  All={all_pct:.1f}%  "
        f"Hours left={hours_left:.0f}h  Paused={state['paused']}")

    # ── Send Discord alert for each newly crossed 10% threshold ───────────────
    for threshold in range(10, 101, 10):
        if threshold in state["notified_thresholds"]:
            continue
        if effective_pct < threshold:
            continue

        # Crossed a new threshold
        state["notified_thresholds"].append(threshold)
        emoji = threshold_emoji(threshold)

        if threshold == 80:
            # Special message — pause is imminent (handled below)
            msg = (f"{emoji} **[Usage] 80% threshold reached**\n"
                   f"Sonnet: **{sonnet_pct:.1f}%** ({sonnet_used:,} / {sonnet_limit:,} tokens)\n"
                   f"All-models: {all_pct:.1f}% ({all_used:,} / {all_limit:,} tokens)\n"
                   f"Reset in **{hours_left:.0f}h**\n"
                   f"⏸ Orchestrator will be **PAUSED** until Tuesday or user override.\n"
                   f"Override: `touch {PAUSE_FILE.parent}/USAGE_PAUSE_OVERRIDE`")
        elif threshold == 90:
            msg = (f"{emoji} **[Usage] 90% — THROTTLE ACTIVE**\n"
                   f"Sonnet: **{sonnet_pct:.1f}%** | All-models: {all_pct:.1f}%\n"
                   f"Reset in {hours_left:.0f}h. Sessions blocked (override still active if set).")
        elif threshold == 100:
            msg = (f"⛔ **[Usage] Weekly limit reached**\n"
                   f"All sessions blocked until Tuesday reset.")
        else:
            msg = (f"{emoji} **[Usage] {threshold}% milestone**\n"
                   f"Sonnet: {sonnet_pct:.1f}% ({sonnet_used:,} tokens) | "
                   f"All-models: {all_pct:.1f}%\n"
                   f"Reset in {hours_left:.0f}h")

        discord(msg)
        log(f"Sent Discord alert for {threshold}% threshold.")

    # ── Manage 80% pause gate ─────────────────────────────────────────────────
    override_active = OVERRIDE_FILE.exists()

    if effective_pct >= 80 and not override_active:
        if not PAUSE_FILE.exists():
            PAUSE_FILE.write_text(f"Paused at {effective_pct:.1f}% on {datetime.now().isoformat()}\n")
            state["paused"] = True
            log(f"Created USAGE_PAUSE at {effective_pct:.1f}%.")
    elif PAUSE_FILE.exists() and override_active:
        log("Override active — USAGE_PAUSE present but override file found, orchestrator will proceed.")
        # Don't remove the pause file; usage-check.py --check handles the override logic

    if effective_pct < 80 and PAUSE_FILE.exists():
        # Safety: clear stale pause file if usage somehow dropped (shouldn't happen in practice)
        PAUSE_FILE.unlink(missing_ok=True)
        state["paused"] = False
        log("Cleared stale USAGE_PAUSE (usage dropped below 80%).")

    save_state(state)


if __name__ == "__main__":
    main()
