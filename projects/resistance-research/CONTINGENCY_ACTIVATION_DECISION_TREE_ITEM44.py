#!/usr/bin/env python3
"""
Domain M Post-June-30 Contingency Activation Decision Tree
Item 44 — Domain M Post-June-30 Contingency Activation Framework

PURPOSE:
    Parse INBOX.md for user's outcome post (sent/not sent Domain 51 emails by June 30),
    classify the contingency path (BRANCH_0 / PATH_A / PATH_B), copy domain-specific
    templates to a next-action directory, and send a Discord alert with the activation path.

USAGE:
    python3 CONTINGENCY_ACTIVATION_DECISION_TREE_ITEM44.py

    OR with explicit outcome override (for testing):
    python3 CONTINGENCY_ACTIVATION_DECISION_TREE_ITEM44.py --outcome SENT
    python3 CONTINGENCY_ACTIVATION_DECISION_TREE_ITEM44.py --outcome NOT_SENT

INPUT:
    1. INBOX.md — user posts outcome here by June 30 23:59 UTC
       Expected format (one of):
         "Domain 51 emails SENT June 24-30 [confirmation text]"
         "Domain 51 emails NOT SENT [reason]"
    2. Environment variable: DISCORD_WEBHOOK_URL (optional — alert suppressed if not set)

OUTPUT:
    1. Prints classification result to stdout
    2. Writes activation summary to: CONTINGENCY_ACTIVATION_LOG_ITEM44.csv
    3. Copies relevant templates to: ./next-action/ directory
    4. Sends Discord webhook alert if DISCORD_WEBHOOK_URL is set

CLASSIFICATION LOGIC:
    - Search INBOX.md for "Domain 51 emails SENT" or "Domain 51 emails NOT SENT"
    - If SENT by June 30 23:59 UTC -> BRANCH_0 (no contingency needed)
    - If NOT SENT -> evaluate current date
      - July 1 - July 8, 23:59 UTC -> PATH_A (Tier 2 accelerated sends)
      - July 9 - July 14, 23:59 UTC -> PATH_B (Domain M priority shift)
      - July 15+ -> PATH_B_LATE (Domain M continues; Domain 51 window closing)
    - INBOX.md absent or ambiguous -> UNKNOWN (escalate)

DETERMINISTIC: No subjective thresholds. All outputs are binary decisions based on
explicit UTC timestamps and unambiguous keyword matching.

TEMPLATE MAPPING:
    BRANCH_0: No action — archive contingency materials
    PATH_A: Copy DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md +
            TIER_2_ACCELERATED_SEND_MASTER_SCHEDULE.md to ./next-action/
    PATH_B: Copy DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md +
            DOMAIN_M_TIER_1_SEND_TEMPLATES.md to ./next-action/
    PATH_A+B: Both paths run in parallel (July 1-8 window) — copy all four files

DISCORD ALERT FORMAT:
    Sends a JSON payload to DISCORD_WEBHOOK_URL (if set) with:
    - Path classification
    - Activation summary (2-3 lines)
    - Links to relevant files
"""

import os
import re
import csv
import sys
import json
import shutil
import argparse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

RESEARCH_DIR = Path(__file__).parent

INBOX_FILE = RESEARCH_DIR / "INBOX.md"
LOG_FILE = RESEARCH_DIR / "CONTINGENCY_ACTIVATION_LOG_ITEM44.csv"
NEXT_ACTION_DIR = RESEARCH_DIR / "next-action"

# Deadline thresholds (UTC)
DEADLINE_JUNE_30 = datetime(2026, 6, 30, 23, 59, 59, tzinfo=timezone.utc)
DEADLINE_JULY_8 = datetime(2026, 7, 8, 23, 59, 59, tzinfo=timezone.utc)
DEADLINE_JULY_14 = datetime(2026, 7, 14, 23, 59, 59, tzinfo=timezone.utc)

# Template files for each path
TEMPLATES = {
    "BRANCH_0": [],
    "PATH_A": [
        "DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md",
        "TIER_2_ACCELERATED_SEND_MASTER_SCHEDULE.md",
        "DOMAIN_51_48_TIER_2_CONTACT_MATRIX_CURRENT.md",
    ],
    "PATH_B": [
        "DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md",
        "DOMAIN_M_TIER_1_SEND_TEMPLATES.md",
    ],
    "PATH_A_AND_B": [
        "DOMAIN_51_TIER_2_ACCELERATED_SEND_SEQUENCE.md",
        "TIER_2_ACCELERATED_SEND_MASTER_SCHEDULE.md",
        "DOMAIN_51_48_TIER_2_CONTACT_MATRIX_CURRENT.md",
        "DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md",
        "DOMAIN_M_TIER_1_SEND_TEMPLATES.md",
    ],
    "UNKNOWN": [],
}

# Branch definitions
BRANCH_DEFINITIONS = {
    "BRANCH_0": {
        "name": "No Contingency Required",
        "description": "Domain 51 emails sent by June 30 23:59 UTC — 100% value preserved",
        "value": "100%",
        "domain_51_action": "Proceed to standard Phase 2 completion (Wave 2 sends, T+7 checkpoint)",
        "domain_m_action": "Domain M Phase 2 activation proceeds on independent track (July 1-15)",
        "templates": TEMPLATES["BRANCH_0"],
        "discord_color": 3066993,  # green
    },
    "PATH_A": {
        "name": "Path A — Tier 2 Accelerated Sends (Domain 51)",
        "description": "Domain 51 deadline missed; July 1-8 Tier 2 accelerated send sequence activating",
        "value": "60-75%",
        "domain_51_action": "Execute TIER_2_ACCELERATED_SEND_MASTER_SCHEDULE.md — 14 sends July 1-8, 2-3 per day",
        "domain_m_action": "Domain M Phase 2 activation proceeds in parallel (July 1-15)",
        "templates": TEMPLATES["PATH_A"],
        "discord_color": 16776960,  # yellow
    },
    "PATH_A_AND_B": {
        "name": "Path A+B — Tier 2 Accelerated Sends + Domain M Priority Shift (parallel)",
        "description": "July 1-8 window: both Domain 51 Tier 2 AND Domain M are active simultaneously",
        "value": "60-75% (Domain 51) + Domain M independent track",
        "domain_51_action": "Execute TIER_2_ACCELERATED_SEND_MASTER_SCHEDULE.md — 14 sends July 1-8",
        "domain_m_action": "Execute DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md — research sprint July 1-5, sends July 7-15",
        "templates": TEMPLATES["PATH_A_AND_B"],
        "discord_color": 16776960,  # yellow
    },
    "PATH_B": {
        "name": "Path B — Domain M Priority Shift (Domain 51 window closing)",
        "description": "July 8+ deadline for Domain 51 Tier 2 passed; shift focus to Domain M July 1-15",
        "value": "50-60% (Domain 51 limited window) + Domain M independent track",
        "domain_51_action": "Execute DOMAIN_51_JULY_15_PLUS_FULL_SCALE_PROTOCOL.md for any remaining Domain 51 sends",
        "domain_m_action": "Execute DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md — highest priority, sends July 7-15",
        "templates": TEMPLATES["PATH_B"],
        "discord_color": 16711680,  # red
    },
    "PATH_B_LATE": {
        "name": "Path B Late — Domain M Continues; Domain 51 Window Closing",
        "description": "July 15+: Domain 51 accelerated window closed; Domain M Tier 1 still active through August 1",
        "value": "40-50% (Domain 51 post-deadline protocol) + Domain M through August 1",
        "domain_51_action": "Domain 51 DOMAIN_51_JULY_15_PLUS_FULL_SCALE_PROTOCOL.md for remaining sends",
        "domain_m_action": "Domain M Tier 1 sends still active (BISC, Democracy Docket, Common Cause) — complete by August 1",
        "templates": TEMPLATES["PATH_B"],
        "discord_color": 16711680,  # red
    },
    "UNKNOWN": {
        "name": "Unknown — INBOX.md ambiguous or absent",
        "description": "User has not posted outcome to INBOX.md, or the post is ambiguous",
        "value": "Indeterminate — cannot classify",
        "domain_51_action": "Check INBOX.md — post 'Domain 51 emails SENT [date]' or 'Domain 51 emails NOT SENT [reason]'",
        "domain_m_action": "Domain M Phase 2 activation can proceed independently — see DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md",
        "templates": TEMPLATES["UNKNOWN"],
        "discord_color": 8421376,  # grey
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# INBOX PARSING
# ─────────────────────────────────────────────────────────────────────────────

class InboxOutcomeParser:
    """Parse INBOX.md for user outcome post."""

    SENT_PATTERN = re.compile(
        r"Domain\s+51\s+emails?\s+SENT\b",
        re.IGNORECASE,
    )
    NOT_SENT_PATTERN = re.compile(
        r"Domain\s+51\s+emails?\s+NOT\s+SENT\b",
        re.IGNORECASE,
    )
    # Also catch shorthand forms
    SENT_SHORT = re.compile(r"\bemails?\s+SENT\b", re.IGNORECASE)
    NOT_SENT_SHORT = re.compile(r"\bNOT\s+SENT\b", re.IGNORECASE)

    def __init__(self, inbox_path: Path):
        self.inbox_path = inbox_path
        self.content = None
        self.outcome = None  # "SENT" | "NOT_SENT" | None

    def read(self) -> bool:
        if not self.inbox_path.exists():
            print(f"WARNING: {self.inbox_path} does not exist.")
            return False
        try:
            with open(self.inbox_path, "r") as f:
                self.content = f.read()
            return True
        except Exception as e:
            print(f"ERROR reading {self.inbox_path}: {e}")
            return False

    def parse(self) -> str:
        """Return 'SENT', 'NOT_SENT', or 'UNKNOWN'."""
        if not self.content:
            return "UNKNOWN"

        # Primary patterns
        sent_match = self.SENT_PATTERN.search(self.content)
        not_sent_match = self.NOT_SENT_PATTERN.search(self.content)

        if sent_match and not not_sent_match:
            self.outcome = "SENT"
        elif not_sent_match and not sent_match:
            self.outcome = "NOT_SENT"
        elif not_sent_match and sent_match:
            # Both found — use most recent (last) occurrence
            if not_sent_match.start() > sent_match.start():
                self.outcome = "NOT_SENT"
            else:
                self.outcome = "SENT"
        else:
            # No primary pattern — try shorthand
            if self.NOT_SENT_SHORT.search(self.content):
                self.outcome = "NOT_SENT"
            elif self.SENT_SHORT.search(self.content):
                self.outcome = "SENT"
            else:
                self.outcome = "UNKNOWN"

        return self.outcome


# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFIER
# ─────────────────────────────────────────────────────────────────────────────

class ContingencyClassifierItem44:
    """
    Deterministic contingency path classifier for Domain M Post-June-30 framework.

    Decision logic:
        outcome == SENT   -> BRANCH_0 (100% value preserved)
        outcome == NOT_SENT:
            now <= DEADLINE_JULY_8  -> PATH_A_AND_B (parallel activation, July 1-8)
            DEADLINE_JULY_8 < now <= DEADLINE_JULY_14 -> PATH_B (Domain M focus)
            now > DEADLINE_JULY_14  -> PATH_B_LATE (Domain M continues through August 1)
        outcome == UNKNOWN -> UNKNOWN
    """

    def __init__(self, outcome: str, now: datetime | None = None):
        self.outcome = outcome
        self.now = now or datetime.now(timezone.utc)
        self.path = None

    def classify(self) -> str:
        if self.outcome == "SENT":
            self.path = "BRANCH_0"
        elif self.outcome == "NOT_SENT":
            if self.now <= DEADLINE_JULY_8:
                self.path = "PATH_A_AND_B"
            elif self.now <= DEADLINE_JULY_14:
                self.path = "PATH_B"
            else:
                self.path = "PATH_B_LATE"
        else:
            self.path = "UNKNOWN"

        return self.path

    def get_branch_info(self) -> dict:
        if not self.path:
            self.classify()
        return BRANCH_DEFINITIONS.get(self.path, BRANCH_DEFINITIONS["UNKNOWN"])


# ─────────────────────────────────────────────────────────────────────────────
# TEMPLATE COPIER
# ─────────────────────────────────────────────────────────────────────────────

class TemplateCopier:
    """Copy relevant templates to the next-action/ directory."""

    def __init__(self, source_dir: Path, dest_dir: Path):
        self.source_dir = source_dir
        self.dest_dir = dest_dir

    def copy(self, template_files: list[str]) -> list[str]:
        """Copy files and return list of successfully copied paths."""
        if not template_files:
            print("No templates to copy (BRANCH_0 or UNKNOWN path).")
            return []

        self.dest_dir.mkdir(parents=True, exist_ok=True)
        copied = []

        for filename in template_files:
            src = self.source_dir / filename
            dst = self.dest_dir / filename

            if not src.exists():
                print(f"WARNING: Template not found: {src}")
                continue

            try:
                shutil.copy2(src, dst)
                print(f"  Copied: {filename} -> next-action/{filename}")
                copied.append(str(dst))
            except Exception as e:
                print(f"ERROR copying {filename}: {e}")

        return copied


# ─────────────────────────────────────────────────────────────────────────────
# LOGGING
# ─────────────────────────────────────────────────────────────────────────────

class ActivationLogger:
    """Log classification to CSV."""

    def __init__(self, log_path: Path):
        self.log_path = log_path

    def log(
        self,
        path: str,
        branch_info: dict,
        inbox_outcome: str,
        classification_time: datetime,
        copied_files: list[str],
    ) -> bool:
        row = {
            "classification_timestamp": classification_time.isoformat(),
            "inbox_outcome": inbox_outcome,
            "path": path,
            "path_name": branch_info["name"],
            "value_score": branch_info["value"],
            "domain_51_action": branch_info["domain_51_action"],
            "domain_m_action": branch_info["domain_m_action"],
            "templates_copied": "; ".join(copied_files) if copied_files else "none",
        }

        file_exists = self.log_path.exists()
        try:
            with open(self.log_path, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=row.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(row)
            return True
        except Exception as e:
            print(f"ERROR writing to {self.log_path}: {e}")
            return False


# ─────────────────────────────────────────────────────────────────────────────
# DISCORD ALERT
# ─────────────────────────────────────────────────────────────────────────────

class DiscordAlerter:
    """Send Discord webhook alert with activation path summary."""

    def __init__(self, webhook_url: str | None):
        self.webhook_url = webhook_url

    def send(
        self,
        path: str,
        branch_info: dict,
        classification_time: datetime,
    ) -> bool:
        if not self.webhook_url:
            print("Discord webhook URL not set (DISCORD_WEBHOOK_URL env var missing) — alert skipped.")
            return False

        # Build embed
        embed = {
            "title": f"CONTINGENCY ACTIVATED: {path}",
            "description": branch_info["description"],
            "color": branch_info.get("discord_color", 8421376),
            "fields": [
                {
                    "name": "Path Name",
                    "value": branch_info["name"],
                    "inline": False,
                },
                {
                    "name": "Expected Value",
                    "value": branch_info["value"],
                    "inline": True,
                },
                {
                    "name": "Classification Time (UTC)",
                    "value": classification_time.strftime("%Y-%m-%d %H:%M UTC"),
                    "inline": True,
                },
                {
                    "name": "Domain 51 Next Action",
                    "value": branch_info["domain_51_action"],
                    "inline": False,
                },
                {
                    "name": "Domain M Next Action",
                    "value": branch_info["domain_m_action"],
                    "inline": False,
                },
            ],
            "footer": {
                "text": "Item 44 — Domain M Post-June-30 Contingency Activation Framework"
            },
            "timestamp": classification_time.isoformat(),
        }

        payload = {"embeds": [embed]}

        try:
            data = json.dumps(payload).encode("utf-8")
            req = urllib.request.Request(
                self.webhook_url,
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=10) as response:
                if response.status in (200, 204):
                    print(f"Discord alert sent successfully (HTTP {response.status}).")
                    return True
                else:
                    print(f"Discord alert returned HTTP {response.status}.")
                    return False
        except Exception as e:
            print(f"ERROR sending Discord alert: {e}")
            return False


# ─────────────────────────────────────────────────────────────────────────────
# REPORT PRINTER
# ─────────────────────────────────────────────────────────────────────────────

def print_report(
    path: str,
    branch_info: dict,
    inbox_outcome: str,
    classification_time: datetime,
    copied_files: list[str],
) -> None:
    print("\n" + "=" * 80)
    print("DOMAIN M POST-JUNE-30 CONTINGENCY ACTIVATION CLASSIFICATION")
    print("Item 44 — Domain M Post-June-30 Contingency Activation Framework")
    print("=" * 80)
    print(f"Classification Time: {classification_time.isoformat()}")
    print(f"INBOX.md Outcome: {inbox_outcome}")
    print()
    print("-" * 80)
    print(f"PATH: {path}")
    print(f"Name: {branch_info['name']}")
    print(f"Description: {branch_info['description']}")
    print(f"Expected Value: {branch_info['value']}")
    print()
    print(f"DOMAIN 51 NEXT ACTION:\n  {branch_info['domain_51_action']}")
    print()
    print(f"DOMAIN M NEXT ACTION:\n  {branch_info['domain_m_action']}")
    print("-" * 80)

    if path == "BRANCH_0":
        print("\nSTATUS: IDEAL OUTCOME — NO CONTINGENCY ACTIVATION NEEDED")
        print("  - Domain 51 emails sent by June 30 23:59 UTC")
        print("  - 100% value preserved")
        print("  - Proceed to standard Phase 2 completion (Wave 2 sends, T+7 checkpoint)")
        print("  - Domain M Phase 2 proceeds on independent track (July 1-15)")
        print("  - Item 44 contingency infrastructure archived")

    elif path == "PATH_A_AND_B":
        print("\nSTATUS: CONTINGENCY ACTIVATED — PATH A + PATH B (PARALLEL)")
        print("  Domain 51 (Path A):")
        print("  - Execute TIER_2_ACCELERATED_SEND_MASTER_SCHEDULE.md")
        print("  - 14 sends, July 1-8, 2-3 per day, 90 min spacing")
        print("  - Gist URL: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372")
        print("  - T+7 checkpoint: July 8, 18:00 UTC")
        print()
        print("  Domain M (Path B — parallel):")
        print("  - Execute DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md")
        print("  - Research sprint July 1-5 (3,000-4,000 word brief)")
        print("  - Gist creation July 5-7")
        print("  - Tier 1 sends July 7-15 (BISC, Democracy Docket, Common Cause)")
        print("  - Templates: DOMAIN_M_TIER_1_SEND_TEMPLATES.md")

    elif path == "PATH_B":
        print("\nSTATUS: CONTINGENCY ACTIVATED — PATH B (DOMAIN M PRIORITY SHIFT)")
        print("  Domain 51:")
        print("  - Tier 2 accelerated window (July 1-8) has closed or is closing")
        print("  - Execute DOMAIN_51_JULY_15_PLUS_FULL_SCALE_PROTOCOL.md for remaining sends")
        print("  - Expected value: 50-60% (limited window)")
        print()
        print("  Domain M (highest priority):")
        print("  - Execute DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md IMMEDIATELY")
        print("  - If research brief not yet produced: begin July 1-5 sprint now")
        print("  - Tier 1 sends July 7-15 (BISC, Democracy Docket, Common Cause)")
        print("  - November 3 ballot deadline; July is the high-leverage send window")

    elif path == "PATH_B_LATE":
        print("\nSTATUS: CONTINGENCY ACTIVATED — PATH B LATE (DOMAIN M CONTINUES)")
        print("  Domain 51:")
        print("  - Accelerated window closed; use DOMAIN_51_JULY_15_PLUS_FULL_SCALE_PROTOCOL.md")
        print("  - Expected value: 40-50%")
        print()
        print("  Domain M:")
        print("  - Tier 1 sends still active through August 1 (BISC, Democracy Docket, Common Cause)")
        print("  - If Tier 1 not yet sent: execute DOMAIN_M_TIER_1_SEND_TEMPLATES.md NOW")
        print("  - September send remains available for voter contact framing (lower value)")

    elif path == "UNKNOWN":
        print("\nSTATUS: UNKNOWN — INBOX.MD AMBIGUOUS OR ABSENT")
        print("  Required user action:")
        print("  - Post to INBOX.md: 'Domain 51 emails SENT [date/confirmation]'")
        print("                   OR: 'Domain 51 emails NOT SENT [reason]'")
        print("  - Then re-run this script")
        print()
        print("  Domain M can proceed regardless:")
        print("  - Execute DOMAIN_M_JULY_1_15_ACTIVATION_SEQUENCE.md independently")
        print("  - Domain M does not depend on Domain 51 outcome")

    if copied_files:
        print()
        print(f"Templates copied to next-action/ ({len(copied_files)} files):")
        for f in copied_files:
            print(f"  - {Path(f).name}")

    print("\n" + "=" * 80 + "\n")


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Domain M Post-June-30 Contingency Activation Decision Tree (Item 44)"
    )
    parser.add_argument(
        "--outcome",
        choices=["SENT", "NOT_SENT"],
        help="Override INBOX.md parsing with explicit outcome (for testing or manual override)",
    )
    parser.add_argument(
        "--now",
        help="Override current UTC datetime (ISO format: 2026-07-03T14:00:00+00:00) — for testing",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Classify and report without copying files or sending Discord alert",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    classification_time = datetime.now(timezone.utc)

    print("Domain M Post-June-30 Contingency Activation Decision Tree — Item 44")
    print(f"Running at: {classification_time.isoformat()}")
    print()

    # Step 1: Determine now (with optional override)
    now = classification_time
    if args.now:
        try:
            now = datetime.fromisoformat(args.now)
            if now.tzinfo is None:
                now = now.replace(tzinfo=timezone.utc)
            print(f"[TEST MODE] Overriding current time to: {now.isoformat()}")
        except ValueError as e:
            print(f"ERROR: Invalid --now value: {e}")
            return 1

    # Step 2: Determine inbox outcome
    if args.outcome:
        inbox_outcome = args.outcome
        print(f"[OVERRIDE] Using explicit outcome: {inbox_outcome}")
    else:
        print(f"Reading INBOX.md from: {INBOX_FILE}")
        parser = InboxOutcomeParser(INBOX_FILE)
        if not parser.read():
            print("INBOX.md not found or unreadable — setting outcome to UNKNOWN")
            inbox_outcome = "UNKNOWN"
        else:
            inbox_outcome = parser.parse()
            print(f"INBOX.md outcome detected: {inbox_outcome}")

    # Step 3: Classify
    classifier = ContingencyClassifierItem44(outcome=inbox_outcome, now=now)
    path = classifier.classify()
    branch_info = classifier.get_branch_info()

    print(f"Classification: {path}")
    print(f"Path name: {branch_info['name']}")

    # Step 4: Copy templates
    copied_files = []
    if not args.dry_run:
        copier = TemplateCopier(RESEARCH_DIR, NEXT_ACTION_DIR)
        templates_to_copy = branch_info["templates"]
        if templates_to_copy:
            print(f"\nCopying {len(templates_to_copy)} templates to next-action/ ...")
            copied_files = copier.copy(templates_to_copy)
        else:
            print("\nNo templates to copy for this path.")
    else:
        print("[DRY RUN] Skipping template copy.")
        if branch_info["templates"]:
            print(f"Would copy {len(branch_info['templates'])} templates:")
            for t in branch_info["templates"]:
                print(f"  - {t}")

    # Step 5: Log classification
    if not args.dry_run:
        logger = ActivationLogger(LOG_FILE)
        if logger.log(path, branch_info, inbox_outcome, classification_time, copied_files):
            print(f"\nClassification logged to: {LOG_FILE}")
        else:
            print("\nWARNING: Could not write to classification log.")
    else:
        print("[DRY RUN] Skipping log write.")

    # Step 6: Print report
    print_report(path, branch_info, inbox_outcome, classification_time, copied_files)

    # Step 7: Discord alert
    webhook_url = os.environ.get("DISCORD_WEBHOOK_URL")
    if not args.dry_run:
        alerter = DiscordAlerter(webhook_url)
        alerter.send(path, branch_info, classification_time)
    else:
        if webhook_url:
            print("[DRY RUN] Would send Discord alert to configured webhook.")
        else:
            print("[DRY RUN] No DISCORD_WEBHOOK_URL set — Discord alert would be skipped.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
