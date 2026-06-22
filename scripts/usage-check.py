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

# ── Model classification ───────────────────────────────────────────────────────

def classify_model(model: str) -> str:
    if model.startswith("claude-sonnet"): return "sonnet"
    if model.startswith("claude-opus"):   return "opus"
    if model.startswith("claude-haiku"):  return "haiku"
    if model in ("<synthetic>", ""):      return "synthetic"
    return "other"

# ── Paths ─────────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).resolve().parent.parent
PROJECTS  = REPO_ROOT / "PROJECTS.md"
PAUSE_FILE    = REPO_ROOT / "USAGE_PAUSE"
OVERRIDE_FILE = REPO_ROOT / "USAGE_PAUSE_OVERRIDE"

# Claude Code stores sessions at ~/.claude/projects/<encoded-cwd>/*.jsonl
# Encoded path: absolute path with / replaced by - (including underscores)
CWD_ENCODED = str(REPO_ROOT).replace("/", "-").replace("_", "-")


def find_session_dir() -> Path:
    """Find the session dir that matches REPO_ROOT by checking cwd in JSONL files.
    Falls back to encoded-path heuristic if no match found."""
    encoded = CWD_ENCODED  # existing heuristic as fallback
    projects_dir = Path.home() / ".claude" / "projects"
    if not projects_dir.exists():
        return projects_dir / encoded

    target_cwd = str(REPO_ROOT)
    for d in projects_dir.iterdir():
        if not d.is_dir():
            continue
        # Quick check: does the encoded dirname match our path?
        if d.name == encoded:
            return d
        # Scan a few JSONL files for cwd field
        for fpath in list(d.glob("*.jsonl"))[:3]:
            try:
                with open(fpath) as f:
                    for line in f:
                        msg = json.loads(line)
                        if isinstance(msg, dict) and msg.get("cwd") == target_cwd:
                            return d
                        break  # only check first line of each file
            except Exception:
                continue
    # Fallback
    return projects_dir / encoded


SESSION_DIR = find_session_dir()

# ── Calibrated plan limits (output tokens per billing week) ───────────────────
# Back-calculated from UI % on 2026-04-26:
#   ~1.97M Sonnet output tokens = 22%  →  limit ≈ 8,935,000
#   ~2.12M all-model output tokens = 14%  →  limit ≈ 15,114,000
# Update with --calibrate when you have fresh UI data.
DEFAULT_SONNET_LIMIT     = 8_935_000
DEFAULT_ALL_MODELS_LIMIT = 15_114_000

WARN_PCT     = 0.75   # warn at 75% of limit
THROTTLE_PCT = 0.90   # stop new sessions at 90% (buffer for current session)


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
    else:
        if not re.search(r"sonnet[_\s]token[_\s]limit", text, re.IGNORECASE):
            print("WARNING: Sonnet token limit not found in PROJECTS.md — using default.", file=sys.stderr)
    m = re.search(r"all[_\s]models?[_\s]token[_\s]limit\s*[:=]\s*([\d_,]+)", text, re.IGNORECASE)
    if m:
        all_limit = int(m.group(1).replace("_", "").replace(",", ""))
    else:
        if not re.search(r"all[_\s]models?[_\s]token[_\s]limit", text, re.IGNORECASE):
            print("WARNING: All-models token limit not found in PROJECTS.md — using default.", file=sys.stderr)
    return sonnet_limit, all_limit


def collect_tokens(since: datetime) -> dict:
    """
    Read all session JSONL files and sum token types since `since`.
    Returns dict keyed by model name with output, input, cache_write, cache_read counts.
    """
    by_model: dict[str, dict] = defaultdict(
        lambda: {"output": 0, "input": 0, "cache_write": 0, "cache_write_5m": 0, "cache_read": 0, "sessions": set()}
    )

    if not SESSION_DIR.exists():
        return {}

    since_ts = since.timestamp()
    for fpath in SESSION_DIR.glob("*.jsonl"):
        if fpath.stat().st_mtime < since_ts:
            continue  # file not modified since billing week start — skip
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
                    out   = usage.get("output_tokens", 0) or 0
                    inp   = usage.get("input_tokens", 0) or 0
                    cw    = usage.get("cache_creation_input_tokens", 0) or 0
                    cw_5m = (usage.get("cache_creation", {}) or {}).get("ephemeral_5m_input_tokens", 0) or 0
                    cr    = usage.get("cache_read_input_tokens", 0) or 0
                    if out == 0 and cw == 0:
                        continue
                    by_model[model]["output"]       += out
                    by_model[model]["input"]         += inp
                    by_model[model]["cache_write"]   += cw
                    by_model[model]["cache_write_5m"] += cw_5m
                    by_model[model]["cache_read"]    += cr
                    by_model[model]["sessions"].add(session_id)
        except OSError:
            continue

    return dict(by_model)


def aggregate(by_model: dict) -> dict:
    def _sum(field, cls):
        return sum(v[field] for k, v in by_model.items() if classify_model(k) == cls)
    def _sum_not(field, classes):
        return sum(v[field] for k, v in by_model.items() if classify_model(k) not in classes)

    sonnet_out = _sum("output", "sonnet")
    opus_out   = _sum("output", "opus")
    haiku_out  = _sum("output", "haiku")
    other_out  = _sum_not("output", ("sonnet", "opus", "haiku", "synthetic"))
    total_out  = sonnet_out + opus_out + haiku_out + other_out

    sonnet_cw    = _sum("cache_write", "sonnet")
    haiku_cw     = _sum("cache_write", "haiku")
    opus_cw      = _sum("cache_write", "opus")
    total_cw     = sum(v["cache_write"]    for v in by_model.values())
    total_cw_5m  = sum(v["cache_write_5m"] for v in by_model.values())
    total_cr     = sum(v["cache_read"]     for v in by_model.values())
    total_fresh  = sum(v["input"]          for v in by_model.values())

    sonnet_sessions = set()
    total_sessions = set()
    for k, v in by_model.items():
        total_sessions |= v["sessions"]
        if classify_model(k) == "sonnet":
            sonnet_sessions |= v["sessions"]

    return {
        "sonnet_output":      sonnet_out,
        "opus_output":        opus_out,
        "haiku_output":       haiku_out,
        "other_output":       other_out,
        "total_output":       total_out,
        "sonnet_cache_write": sonnet_cw,
        "haiku_cache_write":  haiku_cw,
        "opus_cache_write":   opus_cw,
        "total_cache_write":  total_cw,
        "total_cache_write_5m": total_cw_5m,
        "total_cache_read":   total_cr,
        "total_fresh_input":  total_fresh,
        "sonnet_sessions":    len(sonnet_sessions),
        "total_sessions":     len(total_sessions),
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
        "by_model": {k: {
                         "output":        v["output"],
                         "fresh_input":   v["input"],
                         "cache_write":   v["cache_write"],
                         "cache_write_5m": v["cache_write_5m"],
                         "cache_read":    v["cache_read"],
                         "sessions":      len(v["sessions"]),
                     } for k, v in by_model.items() if v["output"] > 0 or v["cache_write"] > 0},
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
    print(f"  Reset in {r['hours_until_reset']:.0f}h  (Tue {r['next_reset'][:10]} ~05:00 UTC)")
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
            cw = d.get("cache_write", 0)
            cw_str = f"  cache_write: {cw:,}" if cw else ""
            print(f"    {model}: {d['output']:,} tokens  ({d['sessions']} sessions){cw_str}")
    print()
    cw_total    = u.get("total_cache_write", 0)
    cw_5m_total = u.get("total_cache_write_5m", 0)
    cr_total    = u.get("total_cache_read", 0)
    fi_total    = u.get("total_fresh_input", 0)
    if cw_total or cr_total or fi_total:
        print(f"  Fresh input  (all models): {fi_total:,} tokens")
        print(f"  Cache writes 1h (all):     {cw_total:,} tokens")
        if cw_5m_total:
            print(f"  Cache writes 5m (all):     {cw_5m_total:,} tokens")
        print(f"  Cache reads  (all models): {cr_total:,} tokens")
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
    if ratio >= THROTTLE_PCT:
        ch = "█"   # throttle — solid
    elif ratio >= WARN_PCT:
        ch = "▓"   # warning — dense
    else:
        ch = "▒"   # normal — medium
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


def read_pause_state() -> dict:
    """Return current pause state as a dict.

    Keys: paused (bool), reason (str|None), timestamp (str|None), override (bool)
    Handles both JSON (written by write_pause_state) and plain-text (written by
    usage-monitor.py) PAUSE_FILE formats.
    """
    state = {"paused": False, "reason": None, "timestamp": None, "override": False}
    if PAUSE_FILE.exists():
        state["paused"] = True
        try:
            data = json.loads(PAUSE_FILE.read_text())
            state["reason"]    = data.get("reason")
            state["timestamp"] = data.get("timestamp")
        except (json.JSONDecodeError, OSError):
            # Plain-text format written by usage-monitor.py
            try:
                state["reason"] = PAUSE_FILE.read_text().strip() or "Paused (no reason recorded)"
            except OSError:
                state["reason"] = "Paused (no reason recorded)"
    state["override"] = OVERRIDE_FILE.exists()
    return state


def write_pause_state(paused: bool, reason: str = "", override: bool = False) -> None:
    """Write or clear the orchestrator pause state.

    paused=True  → creates PAUSE_FILE with JSON metadata
    paused=False → removes PAUSE_FILE
    override=True  → creates OVERRIDE_FILE (orchestrator proceeds despite pause)
    override=False → removes OVERRIDE_FILE
    """
    if paused:
        payload = {
            "paused":    True,
            "reason":    reason or "Manually paused",
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }
        tmp = PAUSE_FILE.with_suffix(".tmp")
        tmp.write_text(json.dumps(payload, indent=2) + "\n")
        os.replace(tmp, PAUSE_FILE)
    else:
        PAUSE_FILE.unlink(missing_ok=True)

    if override:
        OVERRIDE_FILE.touch()
    else:
        OVERRIDE_FILE.unlink(missing_ok=True)


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
    tmp = PROJECTS.with_suffix(".tmp")
    tmp.write_text(text)
    os.replace(tmp, PROJECTS)
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
        # OVERRIDE_FILE bypasses both the 80% gate and the 90% hard throttle.
        if OVERRIDE_FILE.exists():
            pct = max(report["pct"]["sonnet"], report["pct"]["all_models"])
            print(f"OVERRIDE ACTIVE: usage at {pct:.1f}% — all limits bypassed by override file.")
            sys.exit(0)
        if report["status"]["over_any"]:
            print(f"THROTTLE: {report['recommendation']}")
            sys.exit(1)
        if PAUSE_FILE.exists():
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
