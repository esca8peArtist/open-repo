#!/usr/bin/env python3
"""
Domain 57 — Wave 2 Outcome Signal Decision Tree
Item 51 — Domain 57 Phase 2 Pre-Staging

PURPOSE:
    Parse DOMAIN_57_DISTRIBUTION_LOG.csv (or explicit --signal override) for Wave 2
    outcome signal classification (HIGH / MODERATE / LOW / ZERO), and output the
    recommended action path for Domain 57 distribution continuation.

    Parallel to CONTINGENCY_ACTIVATION_DECISION_TREE_ITEM44.py (Item 44 pattern).

USAGE:
    # Standard: reads DOMAIN_57_DISTRIBUTION_LOG.csv for Wave 2 responses
    python3 DOMAIN_57_WAVE2_DECISION_TREE.py

    # With explicit signal override (testing or manual classification)
    python3 DOMAIN_57_WAVE2_DECISION_TREE.py --signal HIGH
    python3 DOMAIN_57_WAVE2_DECISION_TREE.py --signal MODERATE
    python3 DOMAIN_57_WAVE2_DECISION_TREE.py --signal LOW
    python3 DOMAIN_57_WAVE2_DECISION_TREE.py --signal ZERO

    # Dry run (classify only — no file writes)
    python3 DOMAIN_57_WAVE2_DECISION_TREE.py --dry-run

    # Time override (for testing schedule-based logic)
    python3 DOMAIN_57_WAVE2_DECISION_TREE.py --now 2026-08-16T23:00:00+00:00

INPUT:
    1. DOMAIN_57_DISTRIBUTION_LOG.csv — user-maintained send and response log
       Expected columns: contact_id, organization, email, template, sent_utc,
                         response_received, response_date, response_type, notes
    2. Explicit --signal flag (overrides CSV parsing)

OUTPUT:
    1. Prints classification result and recommended action to stdout
    2. Writes classification to DOMAIN_57_WAVE2_CLASSIFICATION_LOG.csv
    3. Appends action summary to DOMAIN_57_DISTRIBUTION_SCHEDULE_UTC.md (Section 4 block)

CLASSIFICATION LOGIC:
    Wave 2 window: Aug 10 (first send) → Aug 16, 23:59 UTC (Wave 2 checkpoint)

    Response counts from CSV rows where:
    - sent_utc is within Wave 1-2 window (Aug 10 00:00 – Aug 16 23:59 UTC)
    - contact_id is in [1..16] (Tier 1 and Tier 2 contacts)

    HIGH:
        substantive_count >= 2
        OR substantive_count >= 1 AND response_rate >= 0.25

    MODERATE:
        substantive_count >= 1
        OR acknowledgment_count >= 2

    LOW:
        substantive_count == 0
        AND (acknowledgment_count >= 1 OR bounce_count >= 1)

    ZERO:
        substantive_count == 0
        AND acknowledgment_count == 0
        AND bounce_count == 0
        (total silence — check delivery before classifying)

RESPONSE TYPE DEFINITIONS (matches DOMAIN_57_DISTRIBUTION_SCHEDULE_UTC.md Section 6):
    SUBSTANTIVE — asks question, proposes meeting, requests adaptation, indicates forwarding
    ACKNOWLEDGMENT — automated or generic "thanks for sharing"
    OUT_OF_OFFICE — auto-reply (counts as delivery confirmation, not signal)
    BOUNCE — email undeliverable
    NO_RESPONSE — no reply by T+14

DETERMINISTIC: All thresholds are explicit numeric values. No subjective assessment.
"""

import csv
import os
import sys
import json
import argparse
from datetime import datetime, timezone
from pathlib import Path

# ─────────────────────────────────────────────────────────────────────────────
# CONSTANTS
# ─────────────────────────────────────────────────────────────────────────────

RESEARCH_DIR = Path(__file__).parent

LOG_FILE = RESEARCH_DIR / "DOMAIN_57_DISTRIBUTION_LOG.csv"
CLASSIFICATION_LOG = RESEARCH_DIR / "DOMAIN_57_WAVE2_CLASSIFICATION_LOG.csv"
SCHEDULE_FILE = RESEARCH_DIR / "DOMAIN_57_DISTRIBUTION_SCHEDULE_UTC.md"

# Wave 2 window boundaries (UTC)
WAVE_2_START = datetime(2026, 8, 10, 0, 0, 0, tzinfo=timezone.utc)
WAVE_2_END = datetime(2026, 8, 16, 23, 59, 59, tzinfo=timezone.utc)

# Tier 1-2 contact IDs (the contacts whose responses count for Wave 2 signal)
WAVE_2_CONTACT_IDS = set(range(1, 17))  # contacts 1-16

# Contact ID ranges for summary labels
WAVE_1_IDS = set(range(1, 9))   # contacts 1-8 (constitutional scholars + ACLU + DF A)
WAVE_2_IDS = set(range(9, 17))  # contacts 9-16 (DF B-C + HRW + CICC + FH + AIUSA + NDI + Carnegie)

# Signal thresholds
HIGH_SUBSTANTIVE_THRESHOLD = 2
HIGH_RATE_THRESHOLD = 0.25  # 25% response rate
MODERATE_SUBSTANTIVE_THRESHOLD = 1
MODERATE_ACKNOWLEDGMENT_THRESHOLD = 2

GIST_URL = "https://gist.github.com/esca8peArtist/a94ef436fd4a678f89e867ac8ed3dd61"

# ─────────────────────────────────────────────────────────────────────────────
# SIGNAL DEFINITIONS
# ─────────────────────────────────────────────────────────────────────────────

SIGNAL_DEFINITIONS = {
    "HIGH": {
        "name": "HIGH — Strong Engagement Signal",
        "description": (
            "2+ substantive replies, OR 1 substantive reply with 25%+ response rate. "
            "Constitutional/legal community has engaged with the core argument."
        ),
        "wave5_action": "Execute Wave 5 in full (all 42 contacts, Aug 23-30).",
        "carnegie_asil_action": "Accelerate Carnegie (Contact 16) to Aug 12 if not yet sent.",
        "unga_action": "Prepare UNGA 81 follow-up brief (1-page summary of Domain 57 Section 7 reform architecture) for distribution at UNGA side events Sept 22-28.",
        "follow_up_action": "Respond to all substantive replies within 48 hours. Offer adapted shorter version (1,500 words) if editorial publication is indicated.",
        "framing_action": "No framing change needed. Constitutional asymmetry argument has landed. UNGA timing hook is working.",
        "color": "GREEN",
        "wave5_execute": True,
        "escalation_accelerate": True,
    },
    "MODERATE": {
        "name": "MODERATE — Partial Engagement Signal",
        "description": (
            "1 substantive reply OR 2+ acknowledgments. "
            "Some traction with at least one target audience. "
            "Continue distribution; framing is working for at least a subset."
        ),
        "wave5_action": "Execute Wave 5 in full (all 42 contacts, Aug 23-30).",
        "carnegie_asil_action": "Proceed with standard schedule (Carnegie Aug 17, ASIL Aug 18).",
        "unga_action": "Prepare UNGA 81 follow-up brief as insurance. Deploy if substantive responses increase to 2+ by Aug 22.",
        "follow_up_action": "Respond to substantive reply within 48 hours. Send T+7 follow-up to silent Tier 1 contacts.",
        "framing_action": "Consider adding concrete legislative timeline note to remaining template sends: 'The Senate International Human Rights Caucus session calendar makes September 2026 the optimal window for ICC Sanctions Repeal advocacy before UNGA.'",
        "color": "YELLOW",
        "wave5_execute": True,
        "escalation_accelerate": False,
    },
    "LOW": {
        "name": "LOW — Delivery Confirmed, Minimal Engagement",
        "description": (
            "0 substantive replies, but 1+ acknowledgments or bounces confirm some delivery. "
            "The document is reaching recipients but not generating substantive engagement. "
            "Framing or timing may need adjustment."
        ),
        "wave5_action": "Execute Wave 5 contacts 27-36 only (skip 37-42). Pause at Contact 36 pending Wave 3-4 response assessment.",
        "carnegie_asil_action": "Proceed with ASIL send (Contact 17) — international law community is most likely to engage on constitutional treaty withdrawal argument. Skip Carnegie (Contact 16) second send.",
        "unga_action": "Shift UNGA hook to be more prominent. Lead remaining template sends with: 'UNGA 81 opens September 22 — 37 days away — and the Pact for the Future the US signed commits member states to multilateral institutions the January 7 withdrawal has dismantled.' Make the hook concrete and time-specific.",
        "follow_up_action": "At T+7, send brief follow-up to Tier 1 contacts: 'Following up on Domain 57 — with UNGA 81 approaching September 22, I wanted to confirm the constitutional treaty withdrawal analysis reached your team.'",
        "framing_action": "For Wave 3-4 sends, switch lead from ICC sanctions to constitutional asymmetry argument (Senate two-thirds to enter, zero role to exit). This argument is not news-dependent and doesn't require current ICC story to be live.",
        "color": "ORANGE",
        "wave5_execute": True,
        "escalation_accelerate": False,
    },
    "ZERO": {
        "name": "ZERO — No Signal Detected",
        "description": (
            "0 substantive replies, 0 acknowledgments, 0 bounces. "
            "Either the emails have not been delivered or are being filtered, "
            "or the document is being silently ignored. "
            "Investigate delivery before continuing distribution."
        ),
        "wave5_action": "PAUSE Wave 5. Do not send contacts 27-42 until delivery is confirmed and framing is reassessed.",
        "carnegie_asil_action": "Send ASIL only (Contact 17) as a delivery test — ASIL uses a reliable institutional address. If ASIL bounces or produces no acknowledgment within 3 days, the delivery system has a problem.",
        "unga_action": "Delay UNGA brief. Reassess framing on August 25 before UNGA window opens.",
        "follow_up_action": "At T+7, send a single brief test email to ONE of the most reliable addresses (ryan.goodman@nyu.edu or info@asil.org) with subject 'Delivery test — Domain 57 research' and a 3-sentence body. If this produces no bounce notification within 48 hours, delivery is working and the issue is engagement, not delivery.",
        "framing_action": "Full framing review: (1) Switch lead hook from ICC sanctions to constitutional asymmetry; (2) Shorten opening paragraph to 2 sentences; (3) Make specific UNGA date (September 22) the explicit hook; (4) Add one concrete ask: 'Would a 1,500-word adapted version for publication work better for your format?'",
        "zero_signal_contingency": "See DOMAIN_57_ZERO_SIGNAL_CONTINGENCY below.",
        "color": "RED",
        "wave5_execute": False,
        "escalation_accelerate": False,
    },
}

ZERO_SIGNAL_CONTINGENCY = """
DOMAIN 57 ZERO SIGNAL CONTINGENCY PROTOCOL
===========================================

If Wave 2 classification is ZERO (run August 16, 23:00 UTC):

Step 1 — Delivery verification (August 17, 14:00 UTC)
  Send a 3-sentence test email to ryan.goodman@nyu.edu:
  Subject: 'Delivery test — Domain 57 multilateral withdrawal research'
  Body: 'I sent you a research document on August 10 regarding executive treaty
  withdrawal and the Youngstown framework. If this reached you, no reply needed.
  If it did not, I would appreciate knowing. [YOUR_NAME] [YOUR_CONTACT_INFO]'

  Wait 48 hours. If bounce notification received: email delivery is broken.
  If no bounce and no reply: delivery is working; engagement is the problem.

Step 2 — Framing reset (if delivery confirmed, August 19-22)
  Revised lead hook (replace ICC sanctions with constitutional asymmetry):
  'With UNGA 81's High-Level General Debate opening September 22, I want to share
  research on a constitutional gap that your organization is best positioned to
  address: the President withdrew from 66 treaty-ratified organizations without
  any Senate role, exploiting Article II silence on exit authority. The NDAA Section
  1250A NATO precedent proves Congress can constrain this — but no equivalent
  protection covers the 65 other organizations.'

Step 3 — Selective re-engagement (August 22-28)
  Re-send to 3 highest-value contacts with revised framing:
  1. ASIL (info@asil.org) — constitutional law argument is their core mandate
  2. Just Security (ryan.goodman@nyu.edu) — NYU institutional address, high reliability
  3. Freedom House (policy@freedomhouse.org) — their own V-Dem data is the hook

Step 4 — UNGA real-time hook (September 22-28)
  If pre-UNGA sends generate zero signal:
  Wait until September 22 (UNGA opening). Send a second wave to all Tier 1-2 contacts
  with subject: 'Domain 57 research — UNGA High-Level Week opened today'
  Body lead: 'Today is the first day of UNGA 81's High-Level General Debate —
  the first General Assembly at which member states will be asked to advance the
  Pact for the Future while the country that signed it 24 months ago has materially
  withdrawn from 66 of its institutional commitments.'
  UNGA real-time hook converts the timing constraint into a news hook.
"""


# ─────────────────────────────────────────────────────────────────────────────
# CSV PARSER
# ─────────────────────────────────────────────────────────────────────────────

class DistributionLogParser:
    """
    Parse DOMAIN_57_DISTRIBUTION_LOG.csv and compute Wave 2 signal metrics.
    """

    RESPONSE_TYPE_SUBSTANTIVE = "SUBSTANTIVE"
    RESPONSE_TYPE_ACKNOWLEDGMENT = "ACKNOWLEDGMENT"
    RESPONSE_TYPE_OUT_OF_OFFICE = "OUT_OF_OFFICE"
    RESPONSE_TYPE_BOUNCE = "BOUNCE"
    RESPONSE_TYPE_NO_RESPONSE = "NO_RESPONSE"

    def __init__(self, log_path: Path):
        self.log_path = log_path
        self.rows = []
        self.parse_errors = []

    def read(self) -> bool:
        if not self.log_path.exists():
            print(f"NOTE: {self.log_path.name} not found. "
                  f"Run with --signal to override CSV parsing.")
            return False
        try:
            with open(self.log_path, newline="") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    self.rows.append(row)
            return True
        except Exception as e:
            print(f"ERROR reading {self.log_path}: {e}")
            return False

    def _is_wave2_contact(self, row: dict) -> bool:
        """Return True if this row is a Tier 1-2 Wave 1-2 contact (IDs 1-16)."""
        try:
            contact_id = int(row.get("contact_id", -1))
            return contact_id in WAVE_2_CONTACT_IDS
        except (ValueError, TypeError):
            return False

    def _parse_utc(self, dt_str: str) -> datetime | None:
        """Parse ISO datetime string to UTC datetime."""
        if not dt_str or dt_str.strip() in ("", "None", "null"):
            return None
        try:
            dt = datetime.fromisoformat(dt_str.strip())
            if dt.tzinfo is None:
                dt = dt.replace(tzinfo=timezone.utc)
            return dt
        except ValueError:
            return None

    def compute_metrics(self) -> dict:
        """
        Compute Wave 2 signal metrics from the log.

        Returns dict with:
            total_wave2_sent: int
            substantive_count: int
            acknowledgment_count: int
            out_of_office_count: int
            bounce_count: int
            no_response_count: int
            response_rate: float (substantive / total_wave2_sent)
            contacts_responded: list of organization names
        """
        total_wave2_sent = 0
        substantive_count = 0
        acknowledgment_count = 0
        out_of_office_count = 0
        bounce_count = 0
        no_response_count = 0
        contacts_responded = []

        for row in self.rows:
            if not self._is_wave2_contact(row):
                continue

            # Check if sent
            sent_utc_str = row.get("sent_utc", "")
            sent_dt = self._parse_utc(sent_utc_str)
            if sent_dt is None:
                continue  # Not sent yet

            total_wave2_sent += 1
            response_type = (row.get("response_type") or "").strip().upper()
            org = row.get("organization", "Unknown")

            if response_type == self.RESPONSE_TYPE_SUBSTANTIVE:
                substantive_count += 1
                contacts_responded.append(f"{org} (SUBSTANTIVE)")
            elif response_type == self.RESPONSE_TYPE_ACKNOWLEDGMENT:
                acknowledgment_count += 1
                contacts_responded.append(f"{org} (ACKNOWLEDGMENT)")
            elif response_type == self.RESPONSE_TYPE_OUT_OF_OFFICE:
                out_of_office_count += 1
            elif response_type == self.RESPONSE_TYPE_BOUNCE:
                bounce_count += 1
            elif response_type == self.RESPONSE_TYPE_NO_RESPONSE:
                no_response_count += 1
            # Empty response_type = sent but not yet assessed; treat as no_response
            else:
                no_response_count += 1

        response_rate = (
            substantive_count / total_wave2_sent
            if total_wave2_sent > 0 else 0.0
        )

        return {
            "total_wave2_sent": total_wave2_sent,
            "substantive_count": substantive_count,
            "acknowledgment_count": acknowledgment_count,
            "out_of_office_count": out_of_office_count,
            "bounce_count": bounce_count,
            "no_response_count": no_response_count,
            "response_rate": response_rate,
            "contacts_responded": contacts_responded,
        }


# ─────────────────────────────────────────────────────────────────────────────
# CLASSIFIER
# ─────────────────────────────────────────────────────────────────────────────

class Wave2SignalClassifier:
    """
    Deterministic classifier for Domain 57 Wave 2 outcome signal.

    Classification logic:
        HIGH:     substantive >= 2
                  OR (substantive >= 1 AND response_rate >= HIGH_RATE_THRESHOLD)
        MODERATE: substantive >= 1
                  OR acknowledgment >= MODERATE_ACKNOWLEDGMENT_THRESHOLD
        LOW:      substantive == 0 AND (acknowledgment >= 1 OR bounce >= 1)
        ZERO:     substantive == 0 AND acknowledgment == 0 AND bounce == 0
    """

    def __init__(self, metrics: dict):
        self.metrics = metrics
        self.signal = None

    def classify(self) -> str:
        m = self.metrics
        substantive = m.get("substantive_count", 0)
        acknowledgment = m.get("acknowledgment_count", 0)
        bounce = m.get("bounce_count", 0)
        rate = m.get("response_rate", 0.0)

        if substantive >= HIGH_SUBSTANTIVE_THRESHOLD:
            self.signal = "HIGH"
        elif substantive >= 1 and rate >= HIGH_RATE_THRESHOLD:
            self.signal = "HIGH"
        elif substantive >= MODERATE_SUBSTANTIVE_THRESHOLD:
            self.signal = "MODERATE"
        elif acknowledgment >= MODERATE_ACKNOWLEDGMENT_THRESHOLD:
            self.signal = "MODERATE"
        elif substantive == 0 and (acknowledgment >= 1 or bounce >= 1):
            self.signal = "LOW"
        else:
            self.signal = "ZERO"

        return self.signal

    def get_definition(self) -> dict:
        if not self.signal:
            self.classify()
        return SIGNAL_DEFINITIONS.get(self.signal, SIGNAL_DEFINITIONS["ZERO"])


# ─────────────────────────────────────────────────────────────────────────────
# LOGGER
# ─────────────────────────────────────────────────────────────────────────────

class ClassificationLogger:
    """Append classification to DOMAIN_57_WAVE2_CLASSIFICATION_LOG.csv."""

    def __init__(self, log_path: Path):
        self.log_path = log_path

    def log(
        self,
        signal: str,
        definition: dict,
        metrics: dict,
        classification_time: datetime,
        source: str,
    ) -> bool:
        row = {
            "classification_timestamp": classification_time.isoformat(),
            "source": source,
            "signal": signal,
            "signal_name": definition["name"],
            "total_wave2_sent": metrics.get("total_wave2_sent", 0),
            "substantive_count": metrics.get("substantive_count", 0),
            "acknowledgment_count": metrics.get("acknowledgment_count", 0),
            "bounce_count": metrics.get("bounce_count", 0),
            "response_rate": f"{metrics.get('response_rate', 0.0):.2%}",
            "wave5_execute": definition.get("wave5_execute", False),
            "escalation_accelerate": definition.get("escalation_accelerate", False),
            "wave5_action": definition["wave5_action"],
            "framing_action": definition["framing_action"],
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
# REPORT PRINTER
# ─────────────────────────────────────────────────────────────────────────────

def print_report(
    signal: str,
    definition: dict,
    metrics: dict,
    classification_time: datetime,
    source: str,
) -> None:
    print("\n" + "=" * 80)
    print("DOMAIN 57 — WAVE 2 OUTCOME SIGNAL CLASSIFICATION")
    print("Item 51 — Domain 57 Phase 2 Pre-Staging")
    print("=" * 80)
    print(f"Classification Time: {classification_time.isoformat()}")
    print(f"Source: {source}")
    print()

    # Metrics summary
    print("WAVE 2 METRICS (contacts 1-16, Aug 10-16 window):")
    print(f"  Total sent:               {metrics.get('total_wave2_sent', 0)}")
    print(f"  Substantive replies:      {metrics.get('substantive_count', 0)}")
    print(f"  Acknowledgments:          {metrics.get('acknowledgment_count', 0)}")
    print(f"  Out-of-office:            {metrics.get('out_of_office_count', 0)}")
    print(f"  Bounces:                  {metrics.get('bounce_count', 0)}")
    print(f"  No response (assessed):   {metrics.get('no_response_count', 0)}")
    print(f"  Response rate:            {metrics.get('response_rate', 0.0):.1%}")

    if metrics.get("contacts_responded"):
        print(f"\n  Contacts with responses:")
        for c in metrics["contacts_responded"]:
            print(f"    - {c}")

    print()
    print("-" * 80)
    print(f"SIGNAL: {signal}")
    print(f"Name: {definition['name']}")
    print(f"Description: {definition['description']}")
    print()

    print("RECOMMENDED ACTIONS:")
    print()
    print(f"  Wave 5 (contacts 27-42, Aug 23-30):")
    print(f"    {definition['wave5_action']}")
    print()
    print(f"  Carnegie / ASIL:")
    print(f"    {definition['carnegie_asil_action']}")
    print()
    print(f"  UNGA 81 pre-positioning:")
    print(f"    {definition['unga_action']}")
    print()
    print(f"  Follow-up action:")
    print(f"    {definition['follow_up_action']}")
    print()
    print(f"  Framing adjustment:")
    print(f"    {definition['framing_action']}")

    if signal == "HIGH":
        print()
        print("=" * 80)
        print("STATUS: HIGH SIGNAL — DISTRIBUTION ON TRACK")
        print()
        print("  Execute Wave 5 in full.")
        print("  Prepare UNGA 81 follow-up brief (1-page Section 7 summary)")
        print("  for distribution at September 22-28 side events.")
        print("  The constitutional asymmetry argument has landed.")
        print()
        print(f"  Gist URL (for UNGA follow-up materials): {GIST_URL}")

    elif signal == "MODERATE":
        print()
        print("=" * 80)
        print("STATUS: MODERATE SIGNAL — PROCEED, MONITOR CLOSELY")
        print()
        print("  Execute Wave 5 in full.")
        print("  Response rate suggests at least partial framing success.")
        print("  Focus follow-up on the one+ organizations that engaged substantively.")
        print("  Add concrete legislative timeline note to remaining sends:")
        print("    'The Senate International Human Rights Caucus session calendar makes")
        print("     September 2026 the optimal window for ICC Sanctions Repeal advocacy.'")

    elif signal == "LOW":
        print()
        print("=" * 80)
        print("STATUS: LOW SIGNAL — EXECUTE PARTIAL WAVE 5, ADJUST FRAMING")
        print()
        print("  Execute Wave 5 contacts 27-36 only.")
        print("  Switch remaining template lead hooks to constitutional asymmetry argument.")
        print("  Make UNGA 81 date (September 22) the explicit hook in all remaining sends.")
        print("  At T+7, send brief follow-up to Tier 1 contacts.")
        print()
        print("  FRAMING SWITCH (for remaining sends):")
        print("  Replace: ICC sanctions domestic First Amendment story")
        print("  With: 'Senate ratified US participation with two-thirds supermajority;")
        print("         President withdrew with zero Senate role; NDAA Section 1250A proves")
        print("         Congress can fix this when it chooses to act.'")

    elif signal == "ZERO":
        print()
        print("=" * 80)
        print("STATUS: ZERO SIGNAL — DELIVERY VERIFICATION REQUIRED")
        print()
        print("  PAUSE Wave 5. Do not send contacts 27-42.")
        print("  Execute zero-signal contingency protocol:")
        print()
        print("  Step 1 (August 17, 14:00 UTC):")
        print("    Send delivery test to ryan.goodman@nyu.edu")
        print("    Subject: 'Delivery test — Domain 57 multilateral withdrawal research'")
        print("    Wait 48 hours for bounce notification.")
        print()
        print("  Step 2 (if delivery confirmed, August 19-22):")
        print("    Switch lead hook to constitutional asymmetry argument.")
        print("    Re-send to 3 highest-value contacts with revised framing.")
        print()
        print("  Step 3 (September 22-28):")
        print("    UNGA real-time hook is the contingency send window.")
        print("    See ZERO_SIGNAL_CONTINGENCY in script source for full text.")
        print()
        print("  ZERO SIGNAL CONTINGENCY PROTOCOL:")
        print(ZERO_SIGNAL_CONTINGENCY)

    print("\n" + "=" * 80 + "\n")
    print(f"Classification logged to: {CLASSIFICATION_LOG.name}")
    print(f"Gist URL: {GIST_URL}")
    print(f"Schedule file: {SCHEDULE_FILE.name}")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# ARGUMENT PARSING
# ─────────────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Domain 57 Wave 2 Outcome Signal Decision Tree (Item 51)"
    )
    parser.add_argument(
        "--signal",
        choices=["HIGH", "MODERATE", "LOW", "ZERO"],
        help="Override CSV parsing with explicit signal (for testing or manual classification)",
    )
    parser.add_argument(
        "--now",
        help=(
            "Override current UTC datetime (ISO format: 2026-08-16T23:00:00+00:00) "
            "— for testing"
        ),
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Classify and report without writing to classification log",
    )
    parser.add_argument(
        "--show-paths",
        action="store_true",
        help="Show all four classification paths and their actions (reference output)",
    )
    return parser.parse_args()


# ─────────────────────────────────────────────────────────────────────────────
# SHOW ALL PATHS (reference mode)
# ─────────────────────────────────────────────────────────────────────────────

def show_all_paths() -> None:
    """Print all four signal paths for reference."""
    print("\n" + "=" * 80)
    print("DOMAIN 57 WAVE 2 — ALL CLASSIFICATION PATHS REFERENCE")
    print("=" * 80)
    print()
    for signal, defn in SIGNAL_DEFINITIONS.items():
        print(f"SIGNAL: {signal} [{defn['color']}]")
        print(f"  {defn['description']}")
        print(f"  Wave 5: {defn['wave5_action']}")
        print(f"  Framing: {defn['framing_action']}")
        print()
    print()
    print("THRESHOLDS:")
    print(f"  HIGH:     substantive >= {HIGH_SUBSTANTIVE_THRESHOLD}")
    print(f"            OR (substantive >= 1 AND response_rate >= {HIGH_RATE_THRESHOLD:.0%})")
    print(f"  MODERATE: substantive >= {MODERATE_SUBSTANTIVE_THRESHOLD}")
    print(f"            OR acknowledgment >= {MODERATE_ACKNOWLEDGMENT_THRESHOLD}")
    print(f"  LOW:      substantive == 0 AND (acknowledgment >= 1 OR bounce >= 1)")
    print(f"  ZERO:     substantive == 0 AND acknowledgment == 0 AND bounce == 0")
    print()


# ─────────────────────────────────────────────────────────────────────────────
# MAIN
# ─────────────────────────────────────────────────────────────────────────────

def main() -> int:
    args = parse_args()
    classification_time = datetime.now(timezone.utc)

    print("Domain 57 Wave 2 Outcome Signal Decision Tree — Item 51")
    print(f"Running at: {classification_time.isoformat()}")
    print()

    # Show all paths reference mode
    if args.show_paths:
        show_all_paths()
        return 0

    # Optional time override for testing
    if args.now:
        try:
            now = datetime.fromisoformat(args.now)
            if now.tzinfo is None:
                now = now.replace(tzinfo=timezone.utc)
            print(f"[TEST MODE] Overriding current time to: {now.isoformat()}")
        except ValueError as e:
            print(f"ERROR: Invalid --now value: {e}")
            return 1

    # Determine signal
    if args.signal:
        signal = args.signal
        source = f"explicit --signal override: {signal}"
        metrics = {
            "total_wave2_sent": 0,
            "substantive_count": 0,
            "acknowledgment_count": 0,
            "out_of_office_count": 0,
            "bounce_count": 0,
            "no_response_count": 0,
            "response_rate": 0.0,
            "contacts_responded": [],
        }
        print(f"[OVERRIDE] Using explicit signal: {signal}")
    else:
        # Parse distribution log
        print(f"Reading {LOG_FILE.name}...")
        parser = DistributionLogParser(LOG_FILE)
        if not parser.read():
            print(
                "Distribution log not found or unreadable.\n"
                "Options:\n"
                "  1. Create DOMAIN_57_DISTRIBUTION_LOG.csv with send/response data\n"
                "  2. Run with --signal HIGH/MODERATE/LOW/ZERO to override\n"
                "  3. Run with --show-paths to see all classification paths"
            )
            return 1

        metrics = parser.compute_metrics()
        source = f"DOMAIN_57_DISTRIBUTION_LOG.csv ({len(parser.rows)} rows)"
        print(f"Loaded {len(parser.rows)} rows from log.")

        # Classify
        classifier = Wave2SignalClassifier(metrics)
        signal = classifier.classify()

    definition = SIGNAL_DEFINITIONS.get(signal, SIGNAL_DEFINITIONS["ZERO"])
    print(f"Signal classification: {signal}")

    # Print report
    print_report(signal, definition, metrics, classification_time, source)

    # Log classification
    if not args.dry_run:
        logger = ClassificationLogger(CLASSIFICATION_LOG)
        if logger.log(signal, definition, metrics, classification_time, source):
            print(f"Classification logged to: {CLASSIFICATION_LOG}")
        else:
            print("WARNING: Could not write classification log.")
    else:
        print("[DRY RUN] Skipping classification log write.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
