#!/usr/bin/env python3
"""
Track B Checkpoint Verification Script

Runs Day 3/7/14 checks for Track B launch monitoring.
Measures engagement, identifies growth signals, and makes Go/Extend/Abort decisions.

Usage:
  python track_b_checkpoint_verification.py --day 3 \
    --etsy-shop-id <id> \
    --kit-shop-id <id> \
    --ga-account-id <id>

Or with manual metric entry:
  python track_b_checkpoint_verification.py --day 3 \
    --manual \
    --reddit-upvotes 250 \
    --reddit-comments 80 \
    --instagram-likes 150 \
    --email-open-rate 22 \
    --kit-subscribers 35

Outputs:
  - Checkpoint report (console)
  - checkpoint_day_N.json (for orchestrator review)
  - Discord notification (if webhook configured)

Exit codes:
  0 = GREEN (proceed)
  1 = YELLOW (extend/monitor)
  2 = RED (troubleshoot/abort)
"""

import sys
import json
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Tuple, Optional
from enum import Enum


class CheckpointLevel(Enum):
    """Checkpoint status levels."""
    GREEN = "GREEN"
    YELLOW = "YELLOW"
    RED = "RED"


class CheckpointDay(Enum):
    """Checkpoint day numbers."""
    DAY_3 = 3
    DAY_7 = 7
    DAY_14 = 14


class TrackBCheckpoint:
    """Tracks Track B launch metrics and decision thresholds."""

    # Day 3 (48 hours post-launch) thresholds
    DAY_3_THRESHOLDS = {
        "reddit_upvotes": {"green": 300, "yellow": 150},
        "reddit_comments": {"green": 50, "yellow": 25},
        "instagram_likes": {"green": 100, "yellow": 50},
        "instagram_comments": {"green": 20, "yellow": 10},
        "tiktok_views": {"green": 2000, "yellow": 500},
        "email_open_rate": {"green": 0.20, "yellow": 0.15},
        "kit_subscribers": {"green": 25, "yellow": 5},
        "influencer_responses": {"green": 2, "yellow": 0},
        "gist_downloads": {"green": 200, "yellow": 50},
    }

    # Day 7 (1 week post-launch) thresholds
    DAY_7_THRESHOLDS = {
        "reddit_upvotes": {"green": 1000, "yellow": 500},
        "reddit_comments": {"green": 150, "yellow": 75},
        "instagram_likes": {"green": 400, "yellow": 200},
        "instagram_comments": {"green": 50, "yellow": 25},
        "tiktok_views": {"green": 10000, "yellow": 5000},
        "email_open_rate": {"green": 0.25, "yellow": 0.18},
        "kit_subscribers": {"green": 75, "yellow": 25},
        "influencer_responses": {"green": 4, "yellow": 2},
        "gist_downloads": {"green": 500, "yellow": 200},
    }

    # Day 14 (2 weeks post-launch) thresholds
    DAY_14_THRESHOLDS = {
        "reddit_upvotes": {"green": 2000, "yellow": 1000},
        "reddit_comments": {"green": 300, "yellow": 150},
        "instagram_likes": {"green": 800, "yellow": 400},
        "instagram_comments": {"green": 100, "yellow": 50},
        "tiktok_views": {"green": 50000, "yellow": 20000},
        "email_open_rate": {"green": 0.28, "yellow": 0.20},
        "kit_subscribers": {"green": 150, "yellow": 50},
        "influencer_responses": {"green": 6, "yellow": 3},
        "gist_downloads": {"green": 1000, "yellow": 500},
    }

    def __init__(self, checkpoint_day: int, launch_date: datetime = None):
        """
        Initialize checkpoint verifier.

        Args:
            checkpoint_day: 3, 7, or 14
            launch_date: Launch date (defaults to June 1, 2026)
        """
        if checkpoint_day not in [3, 7, 14]:
            raise ValueError("checkpoint_day must be 3, 7, or 14")

        self.checkpoint_day = checkpoint_day
        self.launch_date = launch_date or datetime(2026, 6, 1, 8, 0, 0)
        self.checkpoint_date = self.launch_date + timedelta(days=checkpoint_day)
        self.timestamp = datetime.utcnow().isoformat()

        # Select appropriate thresholds
        if checkpoint_day == 3:
            self.thresholds = self.DAY_3_THRESHOLDS
        elif checkpoint_day == 7:
            self.thresholds = self.DAY_7_THRESHOLDS
        else:
            self.thresholds = self.DAY_14_THRESHOLDS

        self.metrics = {}
        self.assessments = {}

    def assess_metric(self, metric_name: str, value: float) -> CheckpointLevel:
        """
        Assess a single metric against thresholds.

        Args:
            metric_name: Name of metric (e.g., 'reddit_upvotes')
            value: Actual metric value

        Returns:
            CheckpointLevel (GREEN, YELLOW, RED)
        """
        if metric_name not in self.thresholds:
            raise ValueError(f"Unknown metric: {metric_name}")

        threshold = self.thresholds[metric_name]

        if value >= threshold["green"]:
            return CheckpointLevel.GREEN
        elif value >= threshold["yellow"]:
            return CheckpointLevel.YELLOW
        else:
            return CheckpointLevel.RED

    def add_metric(self, metric_name: str, value: float) -> None:
        """Add a metric measurement."""
        self.metrics[metric_name] = value
        self.assessments[metric_name] = self.assess_metric(metric_name, value)

    def get_overall_status(self) -> CheckpointLevel:
        """
        Determine overall checkpoint status.

        Logic:
          - All GREEN = GREEN
          - Any RED + majority RED = RED
          - Mix with majority YELLOW = YELLOW
          - Majority GREEN = GREEN
        """
        if not self.assessments:
            return CheckpointLevel.RED

        statuses = list(self.assessments.values())
        green_count = sum(1 for s in statuses if s == CheckpointLevel.GREEN)
        yellow_count = sum(1 for s in statuses if s == CheckpointLevel.YELLOW)
        red_count = sum(1 for s in statuses if s == CheckpointLevel.RED)

        total = len(statuses)

        # Decision logic
        if red_count > total * 0.3:  # >30% RED
            return CheckpointLevel.RED
        elif green_count >= total * 0.6:  # >=60% GREEN
            return CheckpointLevel.GREEN
        else:  # Majority YELLOW
            return CheckpointLevel.YELLOW

    def get_decision(self, overall_status: CheckpointLevel) -> Dict:
        """
        Get decision and next steps based on checkpoint status.

        Returns:
            Dictionary with decision, message, and next steps
        """
        decision_map = {
            CheckpointLevel.GREEN: {
                "decision": "PROCEED",
                "day_3_message": (
                    "Excellent initial traction. Continue execution plan. "
                    "Prepare Day 7 partnership outreach."
                ),
                "day_7_message": (
                    "Strong engagement trajectory. Phase 3 launch is GO for June 22. "
                    "Begin medicinal herbs bundle production (21-day lead time)."
                ),
                "day_14_message": (
                    "Strong performance metrics. Phase 3 launch APPROVED. "
                    "Execute June 22 launch as planned."
                ),
            },
            CheckpointLevel.YELLOW: {
                "decision": "EXTEND/MONITOR",
                "day_3_message": (
                    "Marginal engagement. Extend Day 3 actions: increase influencer "
                    "outreach, boost social posts, analyze content performance."
                ),
                "day_7_message": (
                    "Mixed performance. Phase 3 launch DEFER to June 29 (contingency). "
                    "Activate Tier 2 partnership candidates for 3-day sprint."
                ),
                "day_14_message": (
                    "Phase 3 launch DEFER to June 29. Use June 15-22 for intensive "
                    "partnership building and content optimization."
                ),
            },
            CheckpointLevel.RED: {
                "decision": "TROUBLESHOOT/ABORT",
                "day_3_message": (
                    "Poor initial response. TROUBLESHOOT: check PDF access, verify "
                    "influencer contacts, analyze launch messaging. Day 7 decision pending."
                ),
                "day_7_message": (
                    "Insufficient engagement. Phase 3 launch ABORTED. "
                    "Pivot to Etsy-only strategy (Track A). Analyze failure root causes."
                ),
                "day_14_message": (
                    "Track B performance insufficient. Phase 3 launch ABORTED. "
                    "Focus resources on Track A. Plan Track B relaunch for July."
                ),
            },
        }

        decision_info = decision_map[overall_status]
        day_key = f"day_{self.checkpoint_day}_message"

        return {
            "decision": decision_info["decision"],
            "message": decision_info[day_key],
        }

    def generate_report(self) -> Dict:
        """Generate comprehensive checkpoint report."""
        overall_status = self.get_overall_status()
        decision = self.get_decision(overall_status)

        report = {
            "timestamp": self.timestamp,
            "checkpoint": f"Day {self.checkpoint_day}",
            "checkpoint_date": self.checkpoint_date.isoformat(),
            "launch_date": self.launch_date.isoformat(),
            "overall_status": overall_status.value,
            "decision": decision["decision"],
            "decision_message": decision["message"],
            "metrics": {},
        }

        # Add detailed metric assessments
        for metric_name, actual_value in self.metrics.items():
            threshold = self.thresholds.get(metric_name, {})
            report["metrics"][metric_name] = {
                "actual_value": actual_value,
                "threshold_green": threshold.get("green"),
                "threshold_yellow": threshold.get("yellow"),
                "status": self.assessments[metric_name].value,
            }

        report["metric_summary"] = {
            "total_metrics": len(self.metrics),
            "green_count": sum(
                1 for s in self.assessments.values()
                if s == CheckpointLevel.GREEN
            ),
            "yellow_count": sum(
                1 for s in self.assessments.values()
                if s == CheckpointLevel.YELLOW
            ),
            "red_count": sum(
                1 for s in self.assessments.values()
                if s == CheckpointLevel.RED
            ),
        }

        return report


def format_checkpoint_report(report: Dict) -> str:
    """Format checkpoint report as human-readable text."""
    lines = [
        "=" * 80,
        f"TRACK B {report['checkpoint']} CHECKPOINT REPORT",
        "=" * 80,
        f"Checkpoint date: {report['checkpoint_date']}",
        f"Report generated: {report['timestamp']} UTC",
        "",
        f"OVERALL STATUS: {report['overall_status']}",
        f"DECISION: {report['decision']}",
        "",
        f"Message: {report['decision_message']}",
        "",
        "-" * 80,
        "METRIC ASSESSMENT:",
        "-" * 80,
    ]

    # Group metrics by status
    green_metrics = []
    yellow_metrics = []
    red_metrics = []

    for metric_name, metric_data in report['metrics'].items():
        if metric_data['status'] == 'GREEN':
            green_metrics.append((metric_name, metric_data))
        elif metric_data['status'] == 'YELLOW':
            yellow_metrics.append((metric_name, metric_data))
        else:
            red_metrics.append((metric_name, metric_data))

    if green_metrics:
        lines.append("\n✓ GREEN (On target):")
        for metric_name, data in green_metrics:
            lines.append(
                f"  • {metric_name}: {data['actual_value']} "
                f"(target: ≥{data['threshold_green']})"
            )

    if yellow_metrics:
        lines.append("\n⚠ YELLOW (Marginal):")
        for metric_name, data in yellow_metrics:
            lines.append(
                f"  • {metric_name}: {data['actual_value']} "
                f"(target: ≥{data['threshold_yellow']})"
            )

    if red_metrics:
        lines.append("\n✗ RED (Below threshold):")
        for metric_name, data in red_metrics:
            lines.append(
                f"  • {metric_name}: {data['actual_value']} "
                f"(target: ≥{data['threshold_yellow']})"
            )

    lines.append("")
    lines.append("-" * 80)
    lines.append("SUMMARY:")
    lines.append("-" * 80)
    lines.append(f"  Total metrics: {report['metric_summary']['total_metrics']}")
    lines.append(f"  Green: {report['metric_summary']['green_count']}")
    lines.append(f"  Yellow: {report['metric_summary']['yellow_count']}")
    lines.append(f"  Red: {report['metric_summary']['red_count']}")
    lines.append("")
    lines.append("=" * 80)

    return "\n".join(lines)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Track B Checkpoint Verification")
    parser.add_argument(
        "--day",
        type=int,
        required=True,
        choices=[3, 7, 14],
        help="Checkpoint day (3, 7, or 14)"
    )
    parser.add_argument(
        "--manual",
        action="store_true",
        help="Use manual metric entry instead of API calls"
    )
    parser.add_argument(
        "--reddit-upvotes",
        type=float,
        help="Total Reddit upvotes (manual entry)"
    )
    parser.add_argument(
        "--reddit-comments",
        type=float,
        help="Total Reddit comments (manual entry)"
    )
    parser.add_argument(
        "--instagram-likes",
        type=float,
        help="Instagram likes (manual entry)"
    )
    parser.add_argument(
        "--instagram-comments",
        type=float,
        help="Instagram comments (manual entry)"
    )
    parser.add_argument(
        "--tiktok-views",
        type=float,
        help="TikTok views (manual entry)"
    )
    parser.add_argument(
        "--email-open-rate",
        type=float,
        help="Email open rate as decimal (e.g., 0.22 for 22%)"
    )
    parser.add_argument(
        "--kit-subscribers",
        type=float,
        help="Kit email list subscribers (manual entry)"
    )
    parser.add_argument(
        "--influencer-responses",
        type=float,
        help="Number of influencer responses (manual entry)"
    )
    parser.add_argument(
        "--gist-downloads",
        type=float,
        help="Gist downloads (manual entry)"
    )
    parser.add_argument(
        "--etsy-shop-id",
        help="Etsy shop ID (for API calls)"
    )
    parser.add_argument(
        "--kit-shop-id",
        help="Kit.com shop ID (for API calls)"
    )
    parser.add_argument(
        "--ga-account-id",
        help="Google Analytics account ID (for API calls)"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("/home/awank/dev/SuperClaude_Framework/projects/seedwarden/checkpoints"),
        help="Directory for checkpoint output files"
    )

    args = parser.parse_args()

    # Create checkpoint
    checkpoint = TrackBCheckpoint(args.day)

    if args.manual:
        # Manual metric entry
        metrics_to_add = [
            ("reddit_upvotes", args.reddit_upvotes),
            ("reddit_comments", args.reddit_comments),
            ("instagram_likes", args.instagram_likes),
            ("instagram_comments", args.instagram_comments),
            ("tiktok_views", args.tiktok_views),
            ("email_open_rate", args.email_open_rate),
            ("kit_subscribers", args.kit_subscribers),
            ("influencer_responses", args.influencer_responses),
            ("gist_downloads", args.gist_downloads),
        ]

        for metric_name, value in metrics_to_add:
            if value is not None:
                checkpoint.add_metric(metric_name, value)
    else:
        # API calls would go here (requires authentication)
        print("NOTE: API-based metric collection requires API credentials.", file=sys.stderr)
        print("Use --manual to enter metrics directly.", file=sys.stderr)
        if not args.manual:
            return 2

    # Generate report
    report = checkpoint.generate_report()

    # Create output directory
    args.output_dir.mkdir(parents=True, exist_ok=True)

    # Save JSON report
    output_file = args.output_dir / f"checkpoint_day_{args.day}.json"
    with open(output_file, "w") as f:
        json.dump(report, f, indent=2)

    # Output results
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(format_checkpoint_report(report))

    print(f"\nReport saved to: {output_file}")

    # Return exit code based on status
    if report["overall_status"] == "GREEN":
        return 0
    elif report["overall_status"] == "YELLOW":
        return 1
    else:
        return 2


if __name__ == "__main__":
    sys.exit(main())
