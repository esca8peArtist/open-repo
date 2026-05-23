#!/usr/bin/env python3
"""
Synthesis Outcome Router — Automated Phase 2 Contingency Path Activation
Resistance Research Project

Purpose: Read May 25 synthesis outcome, validate signal log, and automatically route to the
correct contingency execution path (STRONG/MODERATE/WEAK/DELIVERY_PROBLEM).

Execute at: May 25, 2026, 20:15 UTC (immediately post-synthesis)
Usage:
    uv run python synthesis-outcome-router.py
    uv run python synthesis-outcome-router.py --outcome STRONG  # Manual override for testing
    uv run python synthesis-outcome-router.py --dry-run

Outputs:
    - Terminal report: classification, routing decision, immediate actions
    - synthesis-outcome-routing-log.txt: timestamped run record
    - contingency-activation-status.md: readiness checklist for orchestrator/user
"""

import argparse
import datetime
import os
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PROJECT_DIR = os.path.dirname(__file__)
SYNTHESIS_OUTPUT_PATH = os.path.join(PROJECT_DIR, "synthesis-execution-output.md")
SIGNAL_LOG_PATH = os.path.join(PROJECT_DIR, "post-wave-1-monitoring", "wave-1-signal-log-may18-21.md")
CONTINGENCY_PLAYBOOKS_PATH = os.path.join(PROJECT_DIR, "post-synthesis-contingency-execution-playbooks.md")
ROUTING_LOG_PATH = os.path.join(PROJECT_DIR, "synthesis-outcome-routing-log.txt")
ACTIVATION_STATUS_PATH = os.path.join(PROJECT_DIR, "contingency-activation-status.md")

# Contingency paths and their immediate action checklists
CONTINGENCY_PATHS = {
    "STRONG": {
        "description": ">40% substantive engagement — high validation signal",
        "phase2_domains": ["Domain 57", "Domain 59"],
        "domain_launch_dates": {"Domain 57": "June 15", "Domain 59": "June 15"},
        "tier2_activation": "June 15-21 (Week 5)",
        "critical_actions": [
            "Copy PHASE_2_DOMAINS_57_59_OUTLINES.md to working documents",
            "Verify Domain 57 sources (Ikenberry, CRS R48868, etc.)",
            "Verify Domain 59 OBBBA sources",
            "Create writing schedule for 55-65h Domain 59 + 45-51h Domain 57",
            "Confirm Domain 39 production-ready for June 1 HHS deadline distribution",
            "Create Tier 2 pre-contact list refresh with strong-signal framing",
            "Set calendar holds: June 15-July 31 protected writing blocks",
        ],
        "risk_level": "MEDIUM",
    },
    "MODERATE": {
        "description": "25-40% engagement — proceed with standard Phase 2 timeline",
        "phase2_domains": ["Domain 57 (primary)", "Domain 59 (secondary)"],
        "domain_launch_dates": {"Domain 57": "June 10", "Domain 59": "July 1"},
        "tier2_activation": "June 22-28 (Week 6)",
        "critical_actions": [
            "Copy PHASE_2_DOMAINS_57_59_OUTLINES.md to working documents",
            "Verify Domain 57 sources — create source verification doc",
            "Create writing schedule: 46-52h Domain 57 (June 10-Aug 10)",
            "Verify OBBBA + Medicaid data sources for Domain 59",
            "Create writing schedule: 45-55h Domain 59 (July 1-Aug 1)",
            "Stage Tier 1 distribution targets (international affairs, Senate FREC)",
            "Note which sector underperformed; adjust Tier 2 messaging",
        ],
        "risk_level": "LOW",
    },
    "WEAK": {
        "description": "<25% engagement — activate alternative domains (38-40)",
        "phase2_domains": ["Domain 38", "Domain 39", "Domain 40"],
        "domain_launch_dates": {"Domain 38": "June 1-15", "Domain 39": "June 1", "Domain 40": "June 22-July 15"},
        "tier2_activation": "June 29-July 5 (Week 7)",
        "critical_actions": [
            "Run delivery self-test if not done — confirm inbox delivery",
            "Flag for messaging audit — determine if delivery or content problem",
            "Confirm Domain 39 production-ready for June 1 HHS deadline",
            "Create Domain 38 (AI Regulatory Capture) production plan (June 1-15)",
            "Create Domain 40 (Surveillance Capitalism) production plan (June 22-July 15)",
            "Adjust Phase 2 domain sequence per weak-outcome timeline",
            "Prepare contingency messaging: focus on Domain 39 signal strength",
        ],
        "risk_level": "HIGH",
    },
    "DELIVERY_PROBLEM": {
        "description": "Test email landed in spam — delivery issue, not content issue",
        "phase2_domains": [],
        "domain_launch_dates": {},
        "tier2_activation": "On hold pending delivery fix",
        "critical_actions": [
            "DO NOT revise content — this is a delivery problem",
            "Check domain/IP reputation tools (MXToolbox, Google Postmaster, etc.)",
            "Test email infrastructure: SPF/DKIM/DMARC alignment",
            "Verify Gist URL and sender reputation",
            "Confirm sender email address has history (not brand-new account)",
            "Re-run delivery self-test after any infrastructure changes",
            "Resume classification once inbox delivery confirmed",
        ],
        "risk_level": "CRITICAL",
    },
    "TOO_EARLY": {
        "description": "Incomplete signal log or timing window not closed — must resolve May 25",
        "phase2_domains": [],
        "domain_launch_dates": {},
        "tier2_activation": "On hold pending May 25 gate resolution",
        "critical_actions": [
            "Fill any remaining [fill] fields in signal log with May 22-25 data",
            "Re-run synthesis-execution-monitor.py on May 25 with complete data",
            "Ensure all 5 contacts have had at least 7 days (May 18-25)",
            "Determine if data is truly too early or if contacts are silent",
            "Route to STRONG/MODERATE/WEAK based on complete 7-day signal",
        ],
        "risk_level": "MEDIUM",
    },
}


# ---------------------------------------------------------------------------
# Signal log validator
# ---------------------------------------------------------------------------

def validate_signal_log(log_path):
    """
    Check signal log completeness. Return (is_complete, unfilled_count, error_msg).
    """
    if not os.path.exists(log_path):
        return False, None, f"Signal log not found at: {log_path}"

    with open(log_path, "r", encoding="utf-8") as f:
        content = f.read()

    unfilled = content.lower().count("[fill]")
    if unfilled > 0:
        return False, unfilled, f"Signal log has {unfilled} unfilled [fill] fields"

    return True, 0, None


# ---------------------------------------------------------------------------
# Synthesis outcome parser
# ---------------------------------------------------------------------------

def read_synthesis_outcome(output_path):
    """
    Parse synthesis-execution-output.md to extract classification.
    Return (classification, details_dict, error_msg).
    """
    if not os.path.exists(output_path):
        return None, {}, f"Synthesis output not found at: {output_path}"

    with open(output_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Extract classification from YAML frontmatter or first "CLASSIFICATION:" line
    classification_match = re.search(r"(?:classification|CLASSIFICATION):\s*(\w+)", content)
    if not classification_match:
        return None, {}, "Could not parse classification from synthesis output"

    classification = classification_match.group(1).upper()
    if classification not in CONTINGENCY_PATHS:
        return None, {}, f"Unknown classification: {classification}"

    # Extract QRP and other metrics if available
    qrp_match = re.search(r"Quality Reply Points[\"']?\s*\|\s*([\d.]+|STRONG OVERRIDE)", content, re.IGNORECASE)
    qrp = qrp_match.group(1) if qrp_match else "N/A"

    details = {
        "classification": classification,
        "qrp": qrp,
        "parsed_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    }

    return classification, details, None


# ---------------------------------------------------------------------------
# Routing decision
# ---------------------------------------------------------------------------

def route_to_contingency_path(classification, signal_log_valid):
    """
    Determine which contingency path to activate based on classification and signal log status.
    Return (action_type, path_info_dict).

    action_type: "PROCEED", "WAIT_FOR_SIGNAL_LOG", "HOLD_FOR_DELIVERY_FIX", etc.
    """
    # Handle special classifications that override signal log status
    if classification == "DELIVERY_PROBLEM":
        return "HOLD_FOR_DELIVERY_FIX", {
            "reason": "Test email in spam — delivery infrastructure issue",
            "critical": True,
            "next_step": "Fix SPF/DKIM/DMARC, confirm inbox delivery, re-run router",
            "estimated_resolution": "Within 24-48 hours",
        }

    if classification == "TOO_EARLY":
        if signal_log_valid:
            return "HOLD_FOR_GATE", {
                "reason": "Signal window not closed; cannot classify until May 25",
                "gate_closes": "May 25 23:59 UTC",
                "next_step": "Re-run router May 25 20:15 UTC with additional signal data",
                "estimated_resolution": "May 25 23:59 UTC",
            }
        else:
            return "WAIT_FOR_SIGNAL_LOG", {
                "reason": "Signal log incomplete; cannot finalize classification",
                "next_step": "Complete signal log by May 25 18:00 UTC; re-run router May 25 20:15 UTC",
                "estimated_resolution": "May 25 20:30 UTC",
            }

    if not signal_log_valid:
        return "WARN_SIGNAL_LOG_INCOMPLETE", {
            "reason": "Classification is STRONG/MODERATE/WEAK but signal log appears incomplete",
            "advisory": "Verify signal log completion manually before executing contingency actions",
            "estimated_resolution": "Immediate (manual verification)",
        }

    # For STRONG, MODERATE, WEAK with valid signal log: proceed with contingency activation
    return "PROCEED", {
        "path": classification,
        "contingency": CONTINGENCY_PATHS[classification],
        "estimated_resolution": "Immediate execution of contingency immediate actions",
    }


# ---------------------------------------------------------------------------
# Immediate actions formatter
# ---------------------------------------------------------------------------

def format_immediate_actions_checklist(classification):
    """
    Format the immediate actions checklist for the contingency path.
    """
    if classification not in CONTINGENCY_PATHS:
        return ""

    path_info = CONTINGENCY_PATHS[classification]
    lines = []
    lines.append(f"## Immediate Actions — {classification} Outcome\n")
    lines.append(f"**Description**: {path_info['description']}\n")
    lines.append(f"**Risk Level**: {path_info['risk_level']}\n")
    lines.append(f"**Phase 2 Domains**: {', '.join(path_info['phase2_domains'])}\n")
    lines.append(f"**Tier 2 Activation**: {path_info['tier2_activation']}\n")
    lines.append("\n### Checklist\n")
    for i, action in enumerate(path_info["critical_actions"], 1):
        lines.append(f"- [ ] {action}\n")

    return "".join(lines)


# ---------------------------------------------------------------------------
# Report generation
# ---------------------------------------------------------------------------

def generate_routing_report(classification, details, action_type, action_info, signal_valid):
    """
    Generate terminal routing report.
    """
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    lines = []
    lines.append("=" * 80)
    lines.append("SYNTHESIS OUTCOME ROUTER — Phase 2 Contingency Path Activation")
    lines.append(f"Run time: {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    lines.append("=" * 80)
    lines.append("")
    lines.append(f"SYNTHESIS OUTCOME: {classification}")
    lines.append(f"Quality Reply Points: {details.get('qrp', 'N/A')}")
    lines.append(f"Signal log valid: {'YES' if signal_valid else 'NO'}")
    lines.append(f"Routing decision: {action_type}")
    lines.append("")

    if action_type == "PROCEED":
        contingency = action_info.get("contingency", {})
        lines.append(f"CONTINGENCY PATH: {classification}")
        lines.append(f"Description: {contingency.get('description', 'N/A')}")
        lines.append(f"Phase 2 domains: {', '.join(contingency.get('phase2_domains', []))}")
        lines.append(f"Tier 2 activation: {contingency.get('tier2_activation', 'N/A')}")
        lines.append(f"Risk level: {contingency.get('risk_level', 'N/A')}")
        lines.append("")
        lines.append("IMMEDIATE ACTIONS CHECKLIST:")
        for action in contingency.get("critical_actions", []):
            lines.append(f"  [ ] {action}")
    else:
        lines.append(f"ROUTING STATUS: {action_type}")
        for key, value in action_info.items():
            lines.append(f"  {key}: {value}")

    lines.append("")
    lines.append("=" * 80)
    lines.append(f"Next step: See contingency-activation-status.md for detailed roadmap")
    lines.append("=" * 80)

    return "\n".join(lines)


def write_activation_status(classification, action_type, action_info, signal_valid):
    """
    Write contingency-activation-status.md with routing decision and roadmap.
    """
    now_utc = datetime.datetime.now(datetime.timezone.utc)

    content = f"""---
title: "Contingency Activation Status — Synthesis Outcome Routing"
generated: {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}
outcome: {classification}
routing_decision: {action_type}
---

# Synthesis Outcome Routing — {classification}

Generated by `synthesis-outcome-router.py` at {now_utc.strftime('%H:%M UTC')}.

**Routing Decision**: {action_type}
**Signal log valid**: {'Yes' if signal_valid else 'No'}
**Synthesis outcome**: {classification}

---

## Contingency Path: {classification}

"""

    if action_type == "PROCEED":
        contingency = action_info.get("contingency", CONTINGENCY_PATHS.get(classification, {}))
        content += f"""
**Description**: {contingency.get('description', 'N/A')}

**Phase 2 Domains**: {', '.join(contingency.get('phase2_domains', []))}

**Domain launch dates**:
"""
        for domain, date in contingency.get("domain_launch_dates", {}).items():
            content += f"- {domain}: {date}\n"

        content += f"""
**Tier 2 activation**: {contingency.get('tier2_activation', 'N/A')}

**Risk level**: {contingency.get('risk_level', 'N/A')}

---

## Immediate Actions (Execute within 4 hours)

"""
        for i, action in enumerate(contingency.get("critical_actions", []), 1):
            content += f"{i}. [ ] {action}\n"

        content += """
---

## Success Criteria

After routing, verify all of the following:
- [ ] Contingency path identified and documented
- [ ] Immediate actions checklist reviewed
- [ ] Critical path items flagged
- [ ] Signal log status confirmed
- [ ] May 25 gate resolved (not TOO_EARLY)
- [ ] CHECKIN.md updated with routing decision
- [ ] All immediate actions complete by midnight May 25

---

## Next Steps (by Date)

| Date | Milestone | Owner | Status |
|------|-----------|-------|--------|
| May 25 (tonight) | Execute immediate actions | Orchestrator | Pending |
| May 26 | Verify execution complete | User | Pending |
| Domain launch date | Phase 2 domain research begins | Subagent | Pending |
| Tier 2 activation date | Tier 2 outreach begins | Orchestrator | Pending |

"""
    else:
        content += f"""
**Routing status**: {action_type}

**Action needed**:
"""
        for key, value in action_info.items():
            content += f"- **{key}**: {value}\n"

        content += f"""

---

## Resolution Timeline

**Gate closes**: {action_info.get('gate_closes', 'TBD')}
**Estimated resolution**: {action_info.get('estimated_resolution', 'TBD')}
**Next run scheduled**: When gate conditions are met (see BLOCKED.md)

---

## Manual Override

If conditions change and you need to manually override this routing:

```bash
uv run python synthesis-outcome-router.py --outcome {classification}
```

This will re-run routing logic and generate new activation status.

"""

    content += f"""
---

*Generated by synthesis-outcome-router.py at {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}*
*Authoritative framework: post-synthesis-contingency-execution-playbooks.md*
"""

    with open(ACTIVATION_STATUS_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def append_routing_log(classification, action_type, signal_valid):
    """
    Append a timestamped run record to routing log.
    """
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    signal_status = "VALID" if signal_valid else "INCOMPLETE"
    line = (
        f"{now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')} | "
        f"{classification} | {action_type} | signal_log={signal_status}\n"
    )
    with open(ROUTING_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Synthesis Outcome Router. "
            "Read May 25 synthesis outcome and route to correct contingency execution path. "
            "Activated immediately post-synthesis (May 25 20:15 UTC) or manually for testing."
        )
    )
    parser.add_argument(
        "--outcome",
        choices=list(CONTINGENCY_PATHS.keys()),
        help="Manual outcome override (for testing or override conditions)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print report to terminal only; do not write output files.",
    )
    args = parser.parse_args()

    print()
    print("Synthesis Outcome Router — Initializing")
    print()

    # Validate signal log
    signal_valid, unfilled_count, signal_error = validate_signal_log(SIGNAL_LOG_PATH)
    if signal_error and not args.outcome:
        print(f"Signal log check: {signal_error}")
        print()

    # Read synthesis outcome
    if args.outcome:
        # Manual override for testing
        classification = args.outcome
        details = {"classification": classification, "source": "MANUAL OVERRIDE"}
        synthesis_error = None
    else:
        classification, details, synthesis_error = read_synthesis_outcome(SYNTHESIS_OUTPUT_PATH)
        if synthesis_error:
            print(f"ERROR: {synthesis_error}")
            print()
            print("To test with manual outcome: uv run python synthesis-outcome-router.py --outcome STRONG")
            sys.exit(1)

    # Route to contingency path
    action_type, action_info = route_to_contingency_path(classification, signal_valid)

    # Generate outputs
    report = generate_routing_report(classification, details, action_type, action_info, signal_valid)
    print(report)

    # Write outputs
    if not args.dry_run:
        write_activation_status(classification, action_type, action_info, signal_valid)
        append_routing_log(classification, action_type, signal_valid)
        print()
        print(f"Activation status written to: {ACTIVATION_STATUS_PATH}")
        print(f"Routing logged to: {ROUTING_LOG_PATH}")
    else:
        print()
        print("--- DRY RUN: No files written ---")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
