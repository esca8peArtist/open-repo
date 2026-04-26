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

import fcntl
import json
import os
import sys
import subprocess
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path

REPO_ROOT   = Path(__file__).resolve().parent.parent
STATE_FILE  = REPO_ROOT / ".usage-monitor-state.json"
PAUSE_FILE  = REPO_ROOT / "USAGE_PAUSE"
OVERRIDE_FILE = REPO_ROOT / "USAGE_PAUSE_OVERRIDE"
LOG_FILE    = REPO_ROOT / "orchestrator.log"
LOCK_FILE   = REPO_ROOT / ".usage-monitor.lock"

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


def _last_tuesday() -> datetime:
    today = datetime.now(timezone.utc).date()
    days_back = (today.weekday() - 1) % 7
    reset_date = today - timedelta(days=days_back)
    return datetime(reset_date.year, reset_date.month, reset_date.day, tzinfo=timezone.utc)


def current_week() -> str:
    lt = _last_tuesday().date()
    return f"{lt.isoformat()}-billing"


def _write_alert_pending(msg: str) -> None:
    """Fallback: write alert to file so orchestrator picks it up."""
    alert_file = REPO_ROOT / "USAGE_ALERT_PENDING"
    try:
        with open(alert_file, "a") as f:
            f.write(f"[{datetime.now().isoformat()}] {msg}\n---\n")
        log(f"Wrote pending alert to USAGE_ALERT_PENDING (Discord unavailable).")
    except Exception as e:
        log(f"ERROR: could not write alert file: {e}")


def discord(msg: str, critical: bool = False) -> bool:
    """Returns True if sent successfully."""
    if not DISCORD_WEBHOOK:
        log("WARNING: DISCORD_WEBHOOK_URL not set — cannot send alert.")
        return False
    try:
        payload = json.dumps({"content": msg})
        result = subprocess.run(
            ["curl", "-s", "-w", "\n%{http_code}", "-H", "Content-Type: application/json",
             "-d", payload, DISCORD_WEBHOOK],
            capture_output=True, text=True, timeout=15
        )
        lines = result.stdout.strip().split("\n")
        http_code = lines[-1] if lines else "0"
        if result.returncode != 0 or not http_code.startswith("2"):
            log(f"WARNING: Discord notification failed (HTTP {http_code}): {result.stderr[:200]}")
            if critical:
                _write_alert_pending(msg)
            return False
        return True
    except Exception as e:
        log(f"WARNING: Discord notification exception: {e}")
        if critical:
            _write_alert_pending(msg)
        return False


def load_state() -> dict:
    try:
        if STATE_FILE.exists():
            return json.loads(STATE_FILE.read_text())
    except Exception:
        pass
    return {"week": "", "notified_thresholds": [], "paused": False}


def save_state(state: dict) -> None:
    tmp = STATE_FILE.with_suffix(".tmp")
    try:
        tmp.write_text(json.dumps(state, indent=2))
        os.replace(tmp, STATE_FILE)
    except Exception as e:
        log(f"WARNING: could not save state: {e}")
        tmp.unlink(missing_ok=True)


def get_usage() -> dict | None:
    """Run usage-check.py --json and return the parsed report."""
    t0 = time.time()
    try:
        result = subprocess.run(
            [sys.executable, str(REPO_ROOT / "scripts" / "usage-check.py"), "--json"],
            capture_output=True, text=True, timeout=60
        )
        elapsed = time.time() - t0
        if elapsed > 10:
            log(f"WARNING: usage-check.py took {elapsed:.1f}s (unusually slow).")
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

    # ── Get current usage (needed for both new-week pre-population and alerts) ─
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

    # ── New week: reset state and clear pause files ────────────────────────────
    if state["week"] != week:
        log(f"New billing week detected ({week}). Resetting monitor state.")
        # Pre-populate thresholds already crossed so we don't flood alerts
        already_crossed = [t for t in range(10, 101, 10) if effective_pct >= t]
        state = {"week": week, "notified_thresholds": already_crossed, "paused": False}
        PAUSE_FILE.unlink(missing_ok=True)
        OVERRIDE_FILE.unlink(missing_ok=True)
        save_state(state)

    log(f"Usage: Sonnet={sonnet_pct:.1f}%  All={all_pct:.1f}%  "
        f"Hours left={hours_left:.0f}h  Paused={state['paused']}")

    # ── Send Discord alerts for newly crossed thresholds (coalesced) ──────────
    new_thresholds = sorted([t for t in range(10, 101, 10)
                              if t not in state["notified_thresholds"]
                              and effective_pct >= t])

    # Update notified list immediately for all new thresholds
    for t in new_thresholds:
        state["notified_thresholds"].append(t)

    alert_80 = 80 in new_thresholds
    other_new = [t for t in new_thresholds if t != 80]

    if other_new:
        if len(other_new) == 1:
            threshold = other_new[0]
            emoji = threshold_emoji(threshold)
            if threshold == 90:
                msg = (f"{emoji} **[Usage] 90% — THROTTLE ACTIVE**\n"
                       f"Sonnet: **{sonnet_pct:.1f}%** | All-models: {all_pct:.1f}%\n"
                       f"Reset in {hours_left:.0f}h. Sessions blocked (override still active if set).")
                discord(msg, critical=True)
            elif threshold == 100:
                msg = (f"⛔ **[Usage] Weekly limit reached**\n"
                       f"All sessions blocked until Tuesday reset.")
                discord(msg, critical=True)
            else:
                msg = (f"{emoji} **[Usage] {threshold}% milestone**\n"
                       f"Sonnet: {sonnet_pct:.1f}% ({sonnet_used:,} tokens) | "
                       f"All-models: {all_pct:.1f}%\n"
                       f"Reset in {hours_left:.0f}h")
                discord(msg)
        else:
            # Multiple thresholds: coalesce into one message
            labels = "/".join(str(t) + "%" for t in other_new)
            msg = (f"🟡 **[Usage] Crossed {labels} milestones**\n"
                   f"Sonnet: {sonnet_pct:.1f}% | All-models: {all_pct:.1f}% | "
                   f"Reset in {hours_left:.0f}h")
            is_critical = any(t >= 90 for t in other_new)
            discord(msg, critical=is_critical)
        log(f"Sent Discord alert for thresholds: {other_new}.")
        time.sleep(0.4)

    if alert_80:
        emoji = threshold_emoji(80)
        msg = (f"{emoji} **[Usage] 80% threshold reached**\n"
               f"Sonnet: **{sonnet_pct:.1f}%** ({sonnet_used:,} / {sonnet_limit:,} tokens)\n"
               f"All-models: {all_pct:.1f}% ({all_used:,} / {all_limit:,} tokens)\n"
               f"Reset in **{hours_left:.0f}h**\n"
               f"⏸ Orchestrator will be **PAUSED** until Tuesday or user override.\n"
               f"Override: `touch {PAUSE_FILE.parent}/USAGE_PAUSE_OVERRIDE`")
        discord(msg, critical=True)
        log(f"Sent Discord alert for 80% threshold.")

    # ── Manage 80% pause gate ─────────────────────────────────────────────────
    override_active = OVERRIDE_FILE.exists()

    if effective_pct >= 80:
        if not PAUSE_FILE.exists():
            PAUSE_FILE.write_text(f"Paused at {effective_pct:.1f}% on {datetime.now(timezone.utc).isoformat()}\n")
            state["paused"] = True
            log(f"Created USAGE_PAUSE at {effective_pct:.1f}%.")
    elif PAUSE_FILE.exists() and override_active:
        log("Override active — USAGE_PAUSE present but override file found, orchestrator will proceed.")
        # Don't remove the pause file; usage-check.py --check handles the override logic

    if effective_pct < 80 and PAUSE_FILE.exists():
        # Safety: clear stale pause file if usage somehow dropped (shouldn't happen in practice)
        PAUSE_FILE.unlink(missing_ok=True)
        OVERRIDE_FILE.unlink(missing_ok=True)  # clear stale override too
        state["paused"] = False
        log("Cleared stale USAGE_PAUSE (usage dropped below 80%).")

    save_state(state)

    # ── Touch last-run sentinel ────────────────────────────────────────────────
    sentinel = REPO_ROOT / ".usage-monitor-last-run"
    sentinel.write_text(datetime.now(timezone.utc).isoformat())


if __name__ == "__main__":
    lock_fd = open(LOCK_FILE, "w")
    try:
        fcntl.flock(lock_fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
    except OSError:
        # Another instance is running
        print("Another usage-monitor instance is running — exiting.")
        lock_fd.close()
        sys.exit(0)
    try:
        main()
    finally:
        fcntl.flock(lock_fd, fcntl.LOCK_UN)
        lock_fd.close()
