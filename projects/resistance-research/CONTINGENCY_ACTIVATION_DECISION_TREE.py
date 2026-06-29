#!/usr/bin/env python3
"""
Domain 51 Contingency Activation Classification Script
Item 33 — Phase 2 Post-Deadline Contingency Execution Framework

PURPOSE:
    Parse DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md for send dates and classify
    contingency outcome (BRANCH_0/A/B/C) automatically. Deterministic routing
    with no subjective interpretation.

USAGE:
    python3 CONTINGENCY_ACTIVATION_DECISION_TREE.py

INPUT:
    DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md (assumed present in same directory)

OUTPUT:
    Writes to: contingency_classification_log.csv
    Prints classification result to stdout with recommended action path

CLASSIFICATION LOGIC:
    - Read all send dates from execution log
    - Extract latest Wave 1 send date (CLC + Issue One)
    - Compare against hardcoded deadline thresholds (UTC)
    - Assign outcome branch deterministically
    - Log classification decision with timestamp

THRESHOLDS (UTC):
    - July 1, 23:59 UTC: Branch 0 (no contingency)
    - July 2 - July 10, 23:59 UTC: Branch A (accelerated)
    - July 11 - July 14, 23:59 UTC: Branch B (limited window)
    - July 15 - August 8, 23:59 UTC: Branch C (full-scale post-deadline)
    - After August 8, 23:59 UTC: FAILED (no action)

DETERMINISTIC: No subjective thresholds. All outputs are binary decisions based
on explicit UTC timestamps.
"""

import os
import re
import csv
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path


class ContingencyClassifier:
    """Deterministic contingency outcome classifier for Domain 51 Phase 2."""

    # Hardcoded deadline thresholds (UTC)
    DEADLINE_JULY_1 = datetime(2026, 7, 1, 23, 59, 59, tzinfo=timezone.utc)
    DEADLINE_JULY_10 = datetime(2026, 7, 10, 23, 59, 59, tzinfo=timezone.utc)
    DEADLINE_JULY_14 = datetime(2026, 7, 14, 23, 59, 59, tzinfo=timezone.utc)
    DEADLINE_AUG_8 = datetime(2026, 8, 8, 23, 59, 59, tzinfo=timezone.utc)

    BRANCH_DEFINITIONS = {
        "BRANCH_0": {
            "name": "No Contingency Required",
            "description": "Wave 1 executed by July 1, 23:59 UTC",
            "value": "100%",
            "next_action": "Proceed to standard Phase 2 completion",
        },
        "BRANCH_A": {
            "name": "Accelerated Contingency",
            "description": "Wave 1 executed July 2-10, 23:59 UTC",
            "value": "60-75%",
            "next_action": "Activate DOMAIN_51_JULY_2_10_ACCELERATED_CONTINGENCY.md",
        },
        "BRANCH_B": {
            "name": "Limited Window Contingency",
            "description": "Wave 1 executed July 11-14, 23:59 UTC",
            "value": "50-60%",
            "next_action": "Activate Branch B compressed schedule (8 contacts, July 12-14)",
        },
        "BRANCH_C": {
            "name": "Full-Scale Post-Deadline Protocol",
            "description": "Wave 1 executed July 15 - August 8, 23:59 UTC",
            "value": "40-50%",
            "next_action": "Activate DOMAIN_51_JULY_15_PLUS_FULL_SCALE_PROTOCOL.md",
        },
        "FAILED": {
            "name": "Execution Failed",
            "description": "Wave 1 NOT executed by August 8, 23:59 UTC",
            "value": "0%",
            "next_action": "Document loss and proceed to Phase 2 conclusion (no further action)",
        },
    }

    def __init__(self, log_file: str = "DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md"):
        self.log_file = Path(log_file)
        self.execution_log_content = None
        self.classification_log_path = Path("contingency_classification_log.csv")
        self.wave1_sends = []
        self.classification = None
        self.classification_time = datetime.now(timezone.utc)

    def read_execution_log(self) -> bool:
        """Read the execution log file."""
        if not self.log_file.exists():
            print(f"ERROR: {self.log_file} not found in current directory.")
            return False

        try:
            with open(self.log_file, "r") as f:
                self.execution_log_content = f.read()
            return True
        except Exception as e:
            print(f"ERROR reading {self.log_file}: {e}")
            return False

    def extract_wave1_sends(self) -> bool:
        """
        Extract Wave 1 send dates (CLC + Issue One) from execution log.
        Looks for patterns like:
          - Send Date/Time: 2026-06-29 14:00 UTC
          - Send Date/Time: June 29, 2026 14:00 UTC
          - Sent: YES (implies a send occurred)
        """
        if not self.execution_log_content:
            return False

        # Pattern 1: "Send Date/Time: 2026-06-29 14:00 UTC"
        pattern1 = r"Send Date/Time:\s*(\d{4}-\d{2}-\d{2})\s+(\d{2}):(\d{2})\s+UTC"
        # Pattern 2: "Send 1 (CLC)" section with date
        pattern2 = r"Send Date/Time\s*\|\s*\[.*?\]\s*(PENDING|.*?\d{4}.*?)"

        matches = re.findall(pattern1, self.execution_log_content)

        if matches:
            for match in matches:
                date_str = match[0]
                hour = int(match[1])
                minute = int(match[2])
                try:
                    send_dt = datetime(
                        int(date_str[:4]),
                        int(date_str[5:7]),
                        int(date_str[8:10]),
                        hour,
                        minute,
                        tzinfo=timezone.utc,
                    )
                    self.wave1_sends.append(send_dt)
                except ValueError:
                    pass

        # If no matches, check for "Sent: YES" with timing context
        if not self.wave1_sends:
            lines = self.execution_log_content.split("\n")
            for i, line in enumerate(lines):
                if "Send 1" in line or "Send 2" in line:
                    # Check next 5 lines for date info
                    for j in range(i, min(i + 5, len(lines))):
                        match = re.search(r"(\d{4}-\d{2}-\d{2})\s+(\d{2}):(\d{2})", lines[j])
                        if match:
                            try:
                                send_dt = datetime(
                                    int(match.group(1)[:4]),
                                    int(match.group(1)[5:7]),
                                    int(match.group(1)[8:10]),
                                    int(match.group(2)),
                                    int(match.group(3)),
                                    tzinfo=timezone.utc,
                                )
                                self.wave1_sends.append(send_dt)
                                break
                            except ValueError:
                                pass

        return len(self.wave1_sends) > 0

    def classify_contingency(self) -> str:
        """
        Determine contingency branch based on Wave 1 send dates.
        Returns branch classification (BRANCH_0, BRANCH_A, BRANCH_B, BRANCH_C, FAILED).
        """
        if not self.wave1_sends:
            self.classification = "FAILED"
            return self.classification

        # Get the latest send date (most conservative interpretation)
        latest_send = max(self.wave1_sends)

        if latest_send <= self.DEADLINE_JULY_1:
            self.classification = "BRANCH_0"
        elif latest_send <= self.DEADLINE_JULY_10:
            self.classification = "BRANCH_A"
        elif latest_send <= self.DEADLINE_JULY_14:
            self.classification = "BRANCH_B"
        elif latest_send <= self.DEADLINE_AUG_8:
            self.classification = "BRANCH_C"
        else:
            self.classification = "FAILED"

        return self.classification

    def log_classification(self) -> bool:
        """Log the classification to CSV with timestamp and metadata."""
        if not self.classification:
            return False

        branch_info = self.BRANCH_DEFINITIONS[self.classification]

        # Prepare CSV row
        row = {
            "classification_timestamp": self.classification_time.isoformat(),
            "branch": self.classification,
            "branch_name": branch_info["name"],
            "description": branch_info["description"],
            "value_score": branch_info["value"],
            "next_action": branch_info["next_action"],
            "wave1_send_count": len(self.wave1_sends),
            "latest_wave1_send": (
                max(self.wave1_sends).isoformat() if self.wave1_sends else "NO_SENDS"
            ),
        }

        # Append to CSV log
        file_exists = self.classification_log_path.exists()
        try:
            with open(self.classification_log_path, "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=row.keys())
                if not file_exists:
                    writer.writeheader()
                writer.writerow(row)
            return True
        except Exception as e:
            print(f"ERROR writing to {self.classification_log_path}: {e}")
            return False

    def print_report(self):
        """Print human-readable classification report."""
        if not self.classification:
            print("ERROR: Classification not completed.")
            return

        branch_info = self.BRANCH_DEFINITIONS[self.classification]

        print("\n" + "=" * 80)
        print("DOMAIN 51 CONTINGENCY ACTIVATION CLASSIFICATION")
        print("=" * 80)
        print(f"Classification Time: {self.classification_time.isoformat()}")
        print(f"\nWave 1 Sends Detected: {len(self.wave1_sends)}")
        if self.wave1_sends:
            print(f"Latest Send Date: {max(self.wave1_sends).isoformat()}")
        print("\n" + "-" * 80)
        print(f"CLASSIFICATION: {self.classification}")
        print(f"Branch Name: {branch_info['name']}")
        print(f"Description: {branch_info['description']}")
        print(f"Value Score: {branch_info['value']}")
        print(f"\nNEXT ACTION: {branch_info['next_action']}")
        print("-" * 80)

        if self.classification == "BRANCH_0":
            print("\nSTATUS: IDEAL OUTCOME")
            print("  - No contingency activation required")
            print("  - Proceed to standard Phase 2 completion (Item 38 measurement)")
            print("  - Archive contingency protocols")

        elif self.classification == "BRANCH_A":
            print("\nSTATUS: CONTINGENCY ACTIVATED (Accelerated)")
            print("  - Activate Tier 2 contacts immediately")
            print("  - Congress returns July 11; window closes July 10")
            print("  - Target: 10 sends complete by July 10, 23:59 UTC")
            print("  - T+7 checkpoint: July 9, 18:00 UTC")

        elif self.classification == "BRANCH_B":
            print("\nSTATUS: CONTINGENCY ACTIVATED (Limited Window)")
            print("  - Hill staff back to work; recess ended")
            print("  - Compressed schedule: 8 contacts, July 12-14")
            print("  - Value declining; hill engagement minimal")
            print("  - T+4 checkpoint: July 15")

        elif self.classification == "BRANCH_C":
            print("\nSTATUS: CONTINGENCY ACTIVATED (Full-Scale Post-Deadline)")
            print("  - Legislative window closed; research evergreen")
            print("  - Full roster activation: 15 contacts")
            print("  - Longer timeline: July 15 - August 8")
            print("  - T+30 checkpoint: August 15")

        elif self.classification == "FAILED":
            print("\nSTATUS: EXECUTION FAILED")
            print("  - Wave 1 not executed by August 8, 23:59 UTC")
            print("  - No contingency activation possible")
            print("  - Document loss and proceed to Phase 2 conclusion")

        print("\n" + "=" * 80 + "\n")

    def run(self) -> bool:
        """Execute the full classification workflow."""
        print("Domain 51 Contingency Activation Classifier")
        print(f"Reading execution log: {self.log_file}")

        if not self.read_execution_log():
            return False

        print(f"Execution log read successfully ({len(self.execution_log_content)} chars)")

        if not self.extract_wave1_sends():
            print("No Wave 1 sends found in execution log.")
            print("Setting classification to FAILED.")
            self.wave1_sends = []
            self.classify_contingency()
        else:
            print(f"Wave 1 sends extracted: {len(self.wave1_sends)} send(s) found")
            for send in sorted(self.wave1_sends):
                print(f"  - {send.isoformat()}")

            if not self.classify_contingency():
                return False

            print(f"Classification: {self.classification}")

        if not self.log_classification():
            print("Warning: Could not write to classification log.")

        self.print_report()
        return True


def main():
    """Entry point."""
    classifier = ContingencyClassifier()
    success = classifier.run()
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
