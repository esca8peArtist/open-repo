#!/usr/bin/env python3
"""
usage-check.py — Token-based usage tracker for the SuperClaude orchestrator.

Reads actual token counts from Claude Code's local session files
(~/.claude/projects/.../  *.jsonl) and compares against calibrated plan limits.

Plan limits are back-calculated from the UI percentage + observed tokens.
Update them by running: python usage-check.py --calibrate <sonnet_pct> <all_pct>

Output modes:
  python usage-check.py              → human-readable report
  python usage-check.py --json       → JSON for scripting
  python usage-check.py --check      → exit 0 if under budget, exit 1 if over
  python usage-check.py --checkin    → compact one-liner for CHECKIN.md
  python usage-check.py --calibrate 22 14  → recalibrate limits from UI %
"""

import re
import sys
import json
import glob
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from collections import defaultdict

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS  = REPO_ROOT / "PROJECTS.md"
PAUSE_FILE    = REPO_ROOT / "USAGE_PAUSE"
OVERRIDE_FILE = REPO_ROOT / "USAGE_PAUSE_OVERRIDE"

# Claude Code stores sessions at ~/.claude/projects/<encoded-cwd>/*.jsonl
# Encoded path: absolute path with / replaced by - (including underscores)
CWD_ENCODED = str(REPO_ROOT).replace("/", "-").replace("_", "-")
SESSION_DIR = Path.home() / ".claude" / "projects" / CWD_ENCODED

# ── Calibrated plan limits (output tokens per billing week) ───────────────────
# Back-calculated from UI % on 2026-04-26:
#   ~1.97M Sonnet output tokens = 22%  →  limit ≈ 8,935,000
#   ~2.12M all-model output tokens = 14%  →  limit ≈ 15,114,000
# Update with --calibrate when you have fresh UI data.
DEFAULT_SONNET_LIMIT     = 8_935_000
DEFAULT_ALL_MODELS_LIMIT = 15_114_000

WARN_PCT     = 0.75   # warn at 75% of limit
THROTTLE_PCT = 0.90   # stop new sessions at 90% (buffer for current session)

SONNET_MODELS = {"claude-sonnet-4-6", "claude-sonnet-4-5"}
HAIKU_MODELS  = {"claude-haiku-4-5-20251001", "claude-haiku-4-5"}
OPUS_MODELS   = {"claude-opus-4-6", "claude-opus-4-7"}


def last_tuesday() -> datetime:
    """Return the most recent Tuesday at 00:00 UTC (billing week start)."""
    today = datetime.now(timezone.utc).date()
    days_back = (today.weekday() - 1) % 7  # weekday(): Mon=0, Tue=1
    reset_date = today - timedelta(days=days_back)
    return datetime(reset_date.year, reset_date.month, reset_date.day,
                    tzinfo=timezone.utc)


def next_tuesday() -> datetime:
    return last_tuesday() + timedelta(weeks=1)


def load_limits() -> tuple[int, int]:
    """Read calibrated limits from PROJECTS.md if present, else use defaults."""
    sonnet_limit = DEFAULT_SONNET_LIMIT
    all_limit = DEFAULT_ALL_MODELS_LIMIT
    if not PROJECTS.exists():
        return sonnet_limit, all_limit
    text = PROJECTS.read_text()
    m = re.search(r"sonnet[_\s]token[_\s]limit\s*[:=]\s*([\d_,]+)", text, re.IGNORECASE)
    if m:
        sonnet_limit = int(m.group(1).replace("_", "").replace(",", ""))
    m = re.search(r"all[_\s]models?[_\s]token[_\s]limit\s*[:=]\s*([\d_,]+)", text, re.IGNORECASE)
    if m:
        all_limit = int(m.group(1).replace("_", "").replace(",", ""))
    return sonnet_limit, all_limit


def collect_tokens(since: datetime) -> dict:
    """
    Read all session JSONL files and sum output tokens since `since`.
    Returns dict keyed by model name.
    """
    by_model: dict[str, dict] = defaultdict(lambda: {"output": 0, "input": 0, "sessions": set()})

    if not SESSION_DIR.exists():
        return {}

    for fpath in SESSION_DIR.glob("*.jsonl"):
        session_id = fpath.stem
        try:
            with open(fpath) as f:
                for line in f:
                    try:
                        msg = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if not isinstance(msg, dict) or msg.get("type") != "assistant":
                        continue
                    ts_str = msg.get("timestamp", "")
                    if not ts_str:
                        continue
                    try:
                        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00"))
                    except ValueError:
                        continue
                    if ts < since:
                        continue
                    usage = msg.get("message", {}).get("usage", {})
                    model = msg.get("message", {}).get("model", "unknown")
                    out = usage.get("output_tokens", 0) or 0
                    inp = usage.get("input_tokens", 0) or 0
                    if out == 0:
                        continue
                    by_model[model]["output"] += out
                    by_model[model]["input"] += inp
                    by_model[model]["sessions"].add(session_id)
        except OSError:
            continue

    return dict(by_model)


def aggregate(by_model: dict) -> dict:
    sonnet_out = sum(v["output"] for k, v in by_model.items() if k in SONNET_MODELS)
    opus_out   = sum(v["output"] for k, v in by_model.items() if k in OPUS_MODELS)
    haiku_out  = sum(v["output"] for k, v in by_model.items() if k in HAIKU_MODELS)
    other_out  = sum(v["output"] for k, v in by_model.items()
                     if k not in SONNET_MODELS | OPUS_MODELS | HAIKU_MODELS
                     and k not in ("unknown", "<synthetic>"))
    total_out = sonnet_out + opus_out + haiku_out + other_out

    sonnet_sessions = set()
    total_sessions = set()
    for k, v in by_model.items():
        total_sessions |= v["sessions"]
        if k in SONNET_MODELS:
            sonnet_sessions |= v["sessions"]

    return {
        "sonnet_output":   sonnet_out,
        "opus_output":     opus_out,
        "haiku_output":    haiku_out,
        "other_output":    other_out,
        "total_output":    total_out,
        "sonnet_sessions": len(sonnet_sessions),
        "total_sessions":  len(total_sessions),
    }


def build_report() -> dict:
    sonnet_limit, all_limit = load_limits()
    since = last_tuesday()
    next_reset = next_tuesday()

    by_model = collect_tokens(since)
    agg = aggregate(by_model)

    sonnet_pct  = agg["sonnet_output"] / sonnet_limit * 100 if sonnet_limit else 0
    all_pct     = agg["total_output"]  / all_limit    * 100 if all_limit    else 0
    sonnet_over = sonnet_pct >= THROTTLE_PCT * 100
    all_over    = all_pct    >= THROTTLE_PCT * 100
    sonnet_warn = sonnet_pct >= WARN_PCT * 100 and not sonnet_over
    all_warn    = all_pct    >= WARN_PCT * 100 and not all_over

    hours_left = (next_reset - datetime.now(timezone.utc)).total_seconds() / 3600

    return {
        "since":              since.isoformat(),
        "next_reset":         next_reset.isoformat(),
        "hours_until_reset":  round(hours_left, 1),
        "limits":             {"sonnet": sonnet_limit, "all_models": all_limit},
        "usage":              agg,
        "pct":                {"sonnet": round(sonnet_pct, 1), "all_models": round(all_pct, 1)},
        "status": {
            "sonnet_over": sonnet_over,
            "all_over":    all_over,
            "sonnet_warn": sonnet_warn,
            "all_warn":    all_warn,
            "over_any":    sonnet_over or all_over,
        },
        "recommendation": _recommend(sonnet_over, all_over, sonnet_warn, all_warn,
                                     agg["sonnet_output"], sonnet_limit,
                                     agg["total_output"], all_limit),
        "by_model": {k: {"output": v["output"], "sessions": len(v["sessions"])}
                     for k, v in by_model.items() if v["output"] > 0},
    }


def _recommend(s_over, a_over, s_warn, a_warn, s_used, s_lim, a_used, a_lim) -> str:
    s_pct = s_used / s_lim * 100 if s_lim else 0
    a_pct = a_used / a_lim * 100 if a_lim else 0
    if s_over:
        return (f"THROTTLE — Sonnet at {s_pct:.0f}% ({s_used:,}/{s_lim:,} tokens). "
                "Idling until Tuesday reset.")
    if a_over:
        return (f"THROTTLE — All-models at {a_pct:.0f}% ({a_used:,}/{a_lim:,} tokens). "
                "Idling until Tuesday reset.")
    if s_warn:
        return (f"WARNING — Sonnet at {s_pct:.0f}% ({s_lim - s_used:,} tokens remaining). "
                "Limit session depth; prioritise high-value tasks.")
    if a_warn:
        return (f"WARNING — All-models at {a_pct:.0f}% ({a_lim - a_used:,} tokens remaining). "
                "Prioritise high-value tasks.")
    return "Usage nominal — no throttling needed."


def print_report(r: dict) -> None:
    u = r["usage"]
    p = r["pct"]
    lim = r["limits"]
    s = r["status"]

    bar_s = _bar(u["sonnet_output"], lim["sonnet"])
    bar_a = _bar(u["total_output"],  lim["all_models"])
    flag_s = "🔴" if s["sonnet_over"] else ("🟡" if s["sonnet_warn"] else "🟢")
    flag_a = "🔴" if s["all_over"]    else ("🟡" if s["all_warn"]    else "🟢")

    print(f"\n{'='*62}")
    print(f"  SuperClaude Token Usage — since {r['since'][:10]}")
    print(f"  Reset in {r['hours_until_reset']:.0f}h  (Tue {r['next_reset'][:10]} 00:00 UTC)")
    print(f"{'='*62}")
    print(f"  {flag_s} Sonnet     {bar_s}  {p['sonnet']:.1f}%")
    print(f"       {u['sonnet_output']:>13,} / {lim['sonnet']:,} output tokens")
    print(f"  {flag_a} All models {bar_a}  {p['all_models']:.1f}%")
    print(f"       {u['total_output']:>13,} / {lim['all_models']:,} output tokens")
    print()
    print(f"  Sessions this week: {u['total_sessions']}  "
          f"(Sonnet: {u['sonnet_sessions']})")
    if r["by_model"]:
        for model, d in sorted(r["by_model"].items(), key=lambda x: -x[1]["output"]):
            print(f"    {model}: {d['output']:,} tokens  ({d['sessions']} sessions)")
    print()
    print(f"  ➜  {r['recommendation']}")
    print(f"{'='*62}")
    print()
    print("  Recalibrate from UI %:")
    print("    python usage-check.py --calibrate <sonnet_pct> <all_pct>")
    print("  (claude.ai → Settings → Usage & billing)")
    print()


def _bar(used: int, total: int, width: int = 20) -> str:
    if total == 0:
        return "░" * width
    ratio = min(used / total, 1.0)
    filled = int(ratio * width)
    ch = "█" if ratio < WARN_PCT else ("▓" if ratio < THROTTLE_PCT else "█")
    return ch * filled + "░" * (width - filled)


def checkin_line(r: dict) -> str:
    p = r["pct"]
    u = r["usage"]
    s = r["status"]
    flag = "🔴" if s["over_any"] else ("🟡" if (s["sonnet_warn"] or s["all_warn"]) else "🟢")
    return (f"{flag} Usage: Sonnet {p['sonnet']}% ({u['sonnet_output']:,} tokens) | "
            f"All-models {p['all_models']}% | "
            f"Reset in {r['hours_until_reset']:.0f}h | "
            f"check: claude.ai → Settings → Usage & billing")


def calibrate(sonnet_pct: float, all_pct: float) -> None:
    """Back-calculate and write new limits to PROJECTS.md."""
    r = build_report()
    u = r["usage"]

    new_sonnet = int(u["sonnet_output"] / (sonnet_pct / 100)) if sonnet_pct > 0 else DEFAULT_SONNET_LIMIT
    new_all    = int(u["total_output"]  / (all_pct    / 100)) if all_pct    > 0 else DEFAULT_ALL_MODELS_LIMIT

    print(f"Calibrating: Sonnet={sonnet_pct}%, All-models={all_pct}%")
    print(f"  Current Sonnet output  : {u['sonnet_output']:,} tokens")
    print(f"  Implied Sonnet limit   : {new_sonnet:,} tokens/week")
    print(f"  Current total output   : {u['total_output']:,} tokens")
    print(f"  Implied all-models lim : {new_all:,} tokens/week")

    if not PROJECTS.exists():
        print("ERROR: PROJECTS.md not found.")
        return

    text = PROJECTS.read_text()
    today_str = str(date.today())

    def upsert_line(text, key, value, note):
        pattern = rf"- \*\*{re.escape(key)}.*"
        replacement = f"- **{key}: {value:,}**  ← {note}"
        if re.search(pattern, text):
            return re.sub(pattern, replacement, text)
        return text.replace("**Throttle rules",
                            f"{replacement}\n\n**Throttle rules")

    text = upsert_line(text, "Sonnet token limit",    new_sonnet,
                       f"calibrated {today_str} (UI showed {sonnet_pct}%)")
    text = upsert_line(text, "All models token limit", new_all,
                       f"calibrated {today_str} (UI showed {all_pct}%)")
    PROJECTS.write_text(text)
    print(f"  Saved to PROJECTS.md.")


if __name__ == "__main__":
    args = sys.argv[1:]

    if "--calibrate" in args:
        idx = args.index("--calibrate")
        try:
            s_pct = float(args[idx + 1])
            a_pct = float(args[idx + 2])
        except (IndexError, ValueError):
            print("Usage: usage-check.py --calibrate <sonnet_pct> <all_models_pct>")
            sys.exit(1)
        calibrate(s_pct, a_pct)
        sys.exit(0)

    report = build_report()

    if "--json" in args:
        print(json.dumps(report, indent=2, default=str))
    elif "--check" in args:
        # Exit 1 = over 90% budget (hard stop)
        # Exit 2 = paused at 80% by usage-monitor (soft stop; user can override)
        # Exit 0 = proceed
        if report["status"]["over_any"]:
            print(f"THROTTLE: {report['recommendation']}")
            sys.exit(1)
        if PAUSE_FILE.exists():
            if OVERRIDE_FILE.exists():
                print(f"OVERRIDE ACTIVE: paused at 80% but override file present — proceeding.")
                sys.exit(0)
            pct = max(report["pct"]["sonnet"], report["pct"]["all_models"])
            print(f"PAUSED: usage at {pct:.1f}% — orchestrator held at 80% gate. "
                  f"Override: touch {OVERRIDE_FILE}")
            sys.exit(2)
        print(f"OK: {report['recommendation']}")
        sys.exit(0)
    elif "--checkin" in args:
        print(checkin_line(report))
    else:
        print_report(report)
