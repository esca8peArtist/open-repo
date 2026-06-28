#!/usr/bin/env python3
"""
AUTOMATED_WAVE_2_CLASSIFICATION.py
Wave 2 Reply Auto-Classifier — Domain 59 / Domain 60

Created: 2026-06-28 (Session 4467)
Hard deadline: 2026-06-30 18:00 UTC
Classification deadline: 2026-06-30 00:00 UTC

Usage:
    python3 AUTOMATED_WAVE_2_CLASSIFICATION.py
    python3 AUTOMATED_WAVE_2_CLASSIFICATION.py --replies "June 27: 2, June 28: 1"
    python3 AUTOMATED_WAVE_2_CLASSIFICATION.py --count 3
    python3 AUTOMATED_WAVE_2_CLASSIFICATION.py --count 3 --total-sent 8

Cron (daily at 09:00 UTC — prompts for reply count):
    0 9 25-30 6 * /usr/bin/python3 /path/to/AUTOMATED_WAVE_2_CLASSIFICATION.py --count $(cat /tmp/wave2_reply_count.txt 2>/dev/null || echo 0)

Output:
    - Console: classification + recommended action
    - wave2_classification_log.csv: running log for tracking
"""

import argparse
import csv
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

# ─────────────────────────────────────────────────────────────
# Configuration
# ─────────────────────────────────────────────────────────────

CLASSIFICATION_DEADLINE_UTC = datetime(2026, 6, 30, 0, 0, 0, tzinfo=timezone.utc)
HARD_DEADLINE_UTC = datetime(2026, 6, 30, 18, 0, 0, tzinfo=timezone.utc)
GIST_URL = "https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba"
LOG_FILE = Path(__file__).parent / "wave2_classification_log.csv"

# Classification thresholds (deterministic — no subjective calls)
# Source: WAVE_2_ACTIVATION_DECISION_THRESHOLDS.md
THRESHOLDS = {
    "HIGH":     (4, float("inf")),   # 4+ replies
    "MODERATE": (2, 3),              # 2-3 replies
    "LOW":      (1, 1),              # exactly 1 reply
    "ZERO":     (0, 0),              # 0 replies
}

# Actions by classification
# Source: WAVE_2_ACTIVATION_DECISION_THRESHOLDS.md (Sections 1-4)
ACTIONS = {
    "HIGH": {
        "summary": "ACCELERATE — Consolidated Tier 3 sends (same-day window).",
        "steps": [
            "Log HIGH classification in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md with timestamp.",
            "By 2026-06-30 12:00 UTC: Send consolidated Tier 3 emails (all remaining contacts, 09:00-13:00 UTC window).",
            "By 2026-06-30 14:00 UTC: Reply to each HIGH-signal contact with acknowledgment + Gist URL.",
            "By 2026-06-30 18:00 UTC: Log all sends. Hard deadline.",
        ],
    },
    "MODERATE": {
        "summary": "CONTINUE — Standard timeline already planned. No acceleration or deceleration.",
        "steps": [
            "Log MODERATE classification in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md.",
            "Continue standard Tier 3 send schedule (no changes to spacing or sequence).",
            "By 2026-06-30 18:00 UTC: Complete any remaining Wave 2 sends (NELP if not yet sent; Domain 60 contacts).",
            "No new decision gates required before June 30 18:00 UTC.",
        ],
    },
    "LOW": {
        "summary": "ESCALATE — Verify delivery; send 2-3 sentence follow-up to top 2 non-responding contacts.",
        "steps": [
            "Log LOW classification in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md.",
            "By 2026-06-30 04:00 UTC: Verify all sends were delivered — check for bounces/SMTP rejections.",
            "By 2026-06-30 08:00 UTC: If sends confirmed delivered, send short follow-up to top 2 non-responding contacts (2-3 sentences; reference June 30 window).",
            "By 2026-06-30 14:00 UTC: If no follow-up response, switch remaining non-responding contacts to Gist-only path.",
            "By 2026-06-30 18:00 UTC: Log all attempts, responses, and path taken.",
        ],
    },
    "ZERO": {
        "summary": "FALLBACK — Activate Gist-only + retroactive protocol.",
        "steps": [
            "PRE-CHECK: Confirm zero replies are not due to delivery failure (check spam, bounces, Gist URL).",
            "Gist URL: " + GIST_URL,
            "Log ZERO classification in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md.",
            "Activate Gist-only distribution: share Gist on LinkedIn, Twitter/X, professional listservs.",
            "Record all contacts as 'Wave 2 attempted, no reply' — do not disqualify from future waves.",
            "By 2026-06-30 12:00 UTC: Complete any sends not yet attempted (NELP, Domain 60 contacts).",
            "By 2026-06-30 18:00 UTC: Final log entry documenting all attempts.",
        ],
    },
}

# ─────────────────────────────────────────────────────────────
# Core classification logic
# ─────────────────────────────────────────────────────────────

def classify_replies(total_replies: int) -> str:
    """
    Map total reply count to classification string.
    Thresholds are deterministic — no subjective evaluation.

    Args:
        total_replies: integer count of substantive replies received

    Returns:
        Classification string: HIGH | MODERATE | LOW | ZERO
    """
    if total_replies < 0:
        raise ValueError(f"Reply count cannot be negative: {total_replies}")

    for classification, (low, high) in THRESHOLDS.items():
        if low <= total_replies <= high:
            return classification

    # 4+ falls into HIGH (catch-all for large counts)
    return "HIGH"


def parse_date_count_string(reply_string: str) -> int:
    """
    Parse a human-readable reply-by-date string into a total count.

    Examples:
        "June 27: 2, June 28: 1, June 29: 2"  -> 5
        "June 27: 2"                             -> 2
        "3"                                      -> 3 (plain integer fallback)

    Args:
        reply_string: string in format "Month Day: N, Month Day: N, ..."

    Returns:
        Integer total count
    """
    reply_string = reply_string.strip()

    # Try plain integer first
    if reply_string.isdigit():
        return int(reply_string)

    # Extract all "N" from "Month Day: N" patterns
    matches = re.findall(r":\s*(\d+)", reply_string)
    if not matches:
        raise ValueError(
            f"Could not parse reply string: '{reply_string}'\n"
            "Expected format: 'June 27: 2, June 28: 1' or a plain integer."
        )

    return sum(int(m) for m in matches)


def deadline_status(now: datetime) -> dict:
    """
    Return human-readable deadline status relative to now.

    Args:
        now: current UTC datetime

    Returns:
        dict with 'classification_deadline' and 'hard_deadline' status strings
    """
    def format_delta(target: datetime, now: datetime) -> str:
        delta = target - now
        if delta.total_seconds() < 0:
            return "PAST (deadline has passed)"
        hours = int(delta.total_seconds() // 3600)
        minutes = int((delta.total_seconds() % 3600) // 60)
        return f"{hours}h {minutes}m remaining"

    return {
        "classification_deadline": format_delta(CLASSIFICATION_DEADLINE_UTC, now),
        "hard_deadline": format_delta(HARD_DEADLINE_UTC, now),
    }


# ─────────────────────────────────────────────────────────────
# Output and logging
# ─────────────────────────────────────────────────────────────

def print_classification_report(
    total_replies: int,
    classification: str,
    total_sent: int,
    now: datetime,
    reply_string: str = "",
) -> None:
    """Print a human-readable classification report to stdout."""
    deadlines = deadline_status(now)
    response_rate = (total_replies / total_sent * 100) if total_sent > 0 else 0

    print()
    print("=" * 60)
    print("  WAVE 2 AUTO-CLASSIFIER — DOMAIN 59 / DOMAIN 60")
    print("=" * 60)
    print(f"  Run time (UTC):      {now.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"  Replies input:       {reply_string if reply_string else str(total_replies)}")
    print(f"  Total replies:       {total_replies}")
    print(f"  Total sent:          {total_sent}")
    print(f"  Response rate:       {response_rate:.1f}%")
    print()
    print(f"  CLASSIFICATION:      {classification}")
    print(f"  ACTION:              {ACTIONS[classification]['summary']}")
    print()
    print(f"  Classification deadline: {deadlines['classification_deadline']}")
    print(f"  ({CLASSIFICATION_DEADLINE_UTC.strftime('%Y-%m-%d %H:%M UTC')})")
    print(f"  Hard deadline:           {deadlines['hard_deadline']}")
    print(f"  ({HARD_DEADLINE_UTC.strftime('%Y-%m-%d %H:%M UTC')})")
    print()
    print("  REQUIRED STEPS:")
    for i, step in enumerate(ACTIONS[classification]["steps"], 1):
        print(f"    {i}. {step}")
    print()
    print(f"  Gist URL: {GIST_URL}")
    print("=" * 60)
    print()


def append_to_log(
    log_path: Path,
    now: datetime,
    total_replies: int,
    total_sent: int,
    classification: str,
    reply_string: str,
) -> None:
    """
    Append a row to the CSV tracking log.
    Creates the log file with headers if it does not exist.

    CSV columns: timestamp_utc, total_replies, total_sent, response_rate_pct,
                 classification, reply_input_string
    """
    file_exists = log_path.exists()
    response_rate = (total_replies / total_sent * 100) if total_sent > 0 else 0

    with open(log_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow([
                "timestamp_utc",
                "total_replies",
                "total_sent",
                "response_rate_pct",
                "classification",
                "reply_input_string",
            ])
        writer.writerow([
            now.strftime("%Y-%m-%d %H:%M:%S UTC"),
            total_replies,
            total_sent,
            f"{response_rate:.1f}",
            classification,
            reply_string or str(total_replies),
        ])

    print(f"  Log updated: {log_path}")
    print()


# ─────────────────────────────────────────────────────────────
# CLI entry point
# ─────────────────────────────────────────────────────────────

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description=(
            "Wave 2 Reply Auto-Classifier for Domain 59 / Domain 60.\n"
            "Input reply counts; receive classification (HIGH/MODERATE/LOW/ZERO) "
            "and the deterministic recommended action.\n\n"
            "Examples:\n"
            '  python3 AUTOMATED_WAVE_2_CLASSIFICATION.py --replies "June 27: 2, June 28: 1"\n'
            "  python3 AUTOMATED_WAVE_2_CLASSIFICATION.py --count 3\n"
            "  python3 AUTOMATED_WAVE_2_CLASSIFICATION.py --count 3 --total-sent 8\n"
            "  python3 AUTOMATED_WAVE_2_CLASSIFICATION.py  (interactive prompt)"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--replies",
        type=str,
        default=None,
        help=(
            'Reply string in format "Month Day: N, Month Day: N, ..."\n'
            'Example: "June 27: 2, June 28: 1, June 29: 2" = 5 total'
        ),
    )
    parser.add_argument(
        "--count",
        type=int,
        default=None,
        help="Total reply count as a plain integer (alternative to --replies).",
    )
    parser.add_argument(
        "--total-sent",
        type=int,
        default=8,
        help=(
            "Total emails sent in Wave 2 (default: 8, covering D59 Tier 2 + D60 Wave 1). "
            "Used for response rate calculation only — does not affect classification."
        ),
    )
    parser.add_argument(
        "--no-log",
        action="store_true",
        default=False,
        help="Skip writing to the CSV log file.",
    )
    parser.add_argument(
        "--log-path",
        type=str,
        default=None,
        help=f"Path to CSV log file (default: {LOG_FILE})",
    )
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()

    now = datetime.now(timezone.utc)

    # Resolve reply count
    total_replies = None
    reply_string = ""

    if args.count is not None and args.replies is not None:
        print("ERROR: Provide either --count or --replies, not both.", file=sys.stderr)
        sys.exit(1)

    if args.count is not None:
        total_replies = args.count
        reply_string = str(args.count)

    elif args.replies is not None:
        try:
            total_replies = parse_date_count_string(args.replies)
            reply_string = args.replies
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)

    else:
        # Interactive mode — prompt the user
        print()
        print("Wave 2 Auto-Classifier (interactive mode)")
        print(f"Current time: {now.strftime('%Y-%m-%d %H:%M UTC')}")
        print()
        raw = input(
            'Enter reply count or date-string (e.g., "June 27: 2, June 28: 1" or just "3"): '
        ).strip()
        try:
            total_replies = parse_date_count_string(raw)
            reply_string = raw
        except ValueError as e:
            print(f"ERROR: {e}", file=sys.stderr)
            sys.exit(1)

    # Validate
    if total_replies < 0:
        print(f"ERROR: Reply count cannot be negative ({total_replies}).", file=sys.stderr)
        sys.exit(1)

    if args.total_sent < 1:
        print(f"ERROR: --total-sent must be at least 1 ({args.total_sent}).", file=sys.stderr)
        sys.exit(1)

    # Classify
    classification = classify_replies(total_replies)

    # Print report
    print_classification_report(
        total_replies=total_replies,
        classification=classification,
        total_sent=args.total_sent,
        now=now,
        reply_string=reply_string,
    )

    # Log to CSV
    if not args.no_log:
        log_path = Path(args.log_path) if args.log_path else LOG_FILE
        try:
            append_to_log(
                log_path=log_path,
                now=now,
                total_replies=total_replies,
                total_sent=args.total_sent,
                classification=classification,
                reply_string=reply_string,
            )
        except OSError as e:
            print(f"WARNING: Could not write to log file: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
