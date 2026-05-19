#!/usr/bin/env python3
"""
Synthesis Execution Monitor — Wave 1 Signal Analysis
Resistance Research Project

Purpose: Reads the signal log (wave-1-signal-log-may18-21.md), applies the
deterministic classification rules from MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md,
computes Quality Reply Points, selects a branch path, and writes a draft
CHECKIN.md synthesis entry ready for the user to post.

Execute at: May 21, 2026, 19:00–20:00 UTC
Usage:
    uv run python synthesis-execution-monitor.py
    uv run python synthesis-execution-monitor.py --dummy
    uv run python synthesis-execution-monitor.py --signal-log /path/to/custom-log.md

Outputs:
    - Terminal report: classification, QRP, path, per-contact status
    - synthesis-execution-output.md: draft CHECKIN.md post, ready to copy-paste
    - synthesis-execution-log.txt: timestamped run record (appended each run)

Classification authority: MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md Section 3
"""

import argparse
import datetime
import os
import sys

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

SIGNAL_LOG_PATH = os.path.join(
    os.path.dirname(__file__),
    "post-wave-1-monitoring",
    "wave-1-signal-log-may18-21.md",
)
OUTPUT_PATH = os.path.join(
    os.path.dirname(__file__), "synthesis-execution-output.md"
)
RUN_LOG_PATH = os.path.join(
    os.path.dirname(__file__), "synthesis-execution-log.txt"
)

CONTACTS = [
    {"name": "Wendy Weiser", "org": "Brennan Center", "constituency": "think_tank"},
    {"name": "Marc Elias", "org": "Democracy Docket / ELG", "constituency": "immigration_legal"},
    {"name": "Ryan Goodman", "org": "Just Security / NYU Law", "constituency": "law_school"},
    {"name": "Erica Chenoweth", "org": "Harvard Kennedy School", "constituency": "law_school"},
    {"name": "Ian Bassin", "org": "Protect Democracy", "constituency": "think_tank"},
]

# Score-to-quality-point map per MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md Section 2
SCORE_TO_QRP = {0: 0, 1: 0, 2: 0, 3: 1, 4: 2, 5: None}  # 5 = STRONG OVERRIDE (None signals stop)

# Domain sequence tables (path-dependent) from MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md Section 4
DOMAIN_SEQUENCES = {
    "STRONG": [
        ("May 28", "Domain 56 distribution — on schedule"),
        ("June 1", "Domain 39 pre-distribution — NON-NEGOTIABLE"),
        ("June 8", "D57 Section 2 (constitutional asymmetry) outline drafted"),
        ("June 15", "Domain 58 distribution"),
        ("June 15", "Domain 57 LAUNCH (parallel with D59)"),
        ("June 15", "Domain 59 LAUNCH (parallel with D57)"),
        ("June 15–21", "Tier 2 pre-contact activation — all four constituencies"),
        ("May 28", "Domain 42 DEA participation notice — HARD DEADLINE"),
    ],
    "MODERATE": [
        ("May 28", "Domain 56 distribution — on schedule"),
        ("June 1", "Domain 39 pre-distribution — NON-NEGOTIABLE"),
        ("June 10", "Domain 57 PRIMARY research launch"),
        ("June 15", "Domain 58 distribution"),
        ("June 22–28", "Tier 2 pre-contact activation — lead with policy window urgency"),
        ("July 1", "Domain 59 SECONDARY research launch"),
        ("May 28", "Domain 42 DEA participation notice — HARD DEADLINE"),
    ],
    "WEAK": [
        ("May 22", "Begin delivery audit: re-verify all five email addresses"),
        ("May 28", "Domain 56 distribution — on schedule"),
        ("June 1", "Domain 39 pre-distribution — NON-NEGOTIABLE"),
        ("June 3", "Domain 38 (AI Regulatory Capture) pre-production begins"),
        ("June 15", "Domain 58 distribution"),
        ("June 22", "Domain 40 (Surveillance Capitalism) production begins"),
        ("June 29–July 5", "Tier 2 activation — contingent on D39 signal"),
        ("June 30", "Domain 38 distribution target"),
        ("July 15", "Domain 40 distribution target"),
        ("July 15", "Domain 59 research start"),
        ("August 1", "Domain 57 research start"),
        ("May 28", "Domain 42 DEA participation notice — HARD DEADLINE"),
    ],
    "TOO_EARLY": [
        ("May 22", "Delivery self-test if not already run. Continue monitoring."),
        ("May 23", "Think tank window closes (Day 5 for Weiser/Bassin). Any Score 3+ reply -> upgrade to MODERATE."),
        ("May 24", "Domain 42 DEA electronic filing deadline — 11:59 p.m. ET. Path-independent."),
        ("May 25", "MANDATORY RESOLUTION: run full classification formula. TOO EARLY resolves here."),
        ("May 28", "Domain 56 distribution — on schedule regardless of path"),
        ("June 1", "Domain 39 pre-distribution — NON-NEGOTIABLE"),
        ("May 28", "Domain 42 DEA participation notice — HARD DEADLINE"),
    ],
    "DELIVERY_PROBLEM": [
        ("URGENT", "Test email landed in spam — fix sender reputation before any further sends."),
        ("URGENT", "Do NOT revise content — this is a delivery problem, not a content problem."),
        ("After fix", "Re-run delivery self-test to confirm inbox delivery."),
        ("After fix", "Resume classification from Rule 3a with delivery confirmed."),
    ],
}


# ---------------------------------------------------------------------------
# Dummy signal data for testing (--dummy flag)
# ---------------------------------------------------------------------------

DUMMY_SIGNAL_DATA = {
    "contacts": [
        {
            "name": "Wendy Weiser",
            "org": "Brennan Center",
            "constituency": "think_tank",
            "score": 3,
            "signal_type": "REPLY",
            "key_content": "Domain-specific question about Section 5 redistricting cascade and state legislative response.",
            "ooo": False,
            "bounce": False,
        },
        {
            "name": "Marc Elias",
            "org": "Democracy Docket / ELG",
            "constituency": "immigration_legal",
            "score": 0,
            "signal_type": "NO SIGNAL",
            "key_content": "No response within 72h window.",
            "ooo": False,
            "bounce": False,
        },
        {
            "name": "Ryan Goodman",
            "org": "Just Security / NYU Law",
            "constituency": "law_school",
            "score": 0,
            "signal_type": "NO SIGNAL",
            "key_content": "No response — TOO EARLY (academic cycle, Day 3).",
            "ooo": False,
            "bounce": False,
        },
        {
            "name": "Erica Chenoweth",
            "org": "Harvard Kennedy School",
            "constituency": "law_school",
            "score": 0,
            "signal_type": "NO SIGNAL",
            "key_content": "No response — TOO EARLY (academic cycle, Day 3).",
            "ooo": False,
            "bounce": False,
        },
        {
            "name": "Ian Bassin",
            "org": "Protect Democracy",
            "constituency": "think_tank",
            "score": 0,
            "signal_type": "NO SIGNAL",
            "key_content": "No response within 72h window.",
            "ooo": False,
            "bounce": False,
        },
    ],
    "gist_delta": 7,
    "delivery_self_test": "inbox",  # "inbox", "spam", or "inconclusive"
}


# ---------------------------------------------------------------------------
# Signal log parser
# ---------------------------------------------------------------------------

def parse_signal_log(log_path):
    """
    Parse the wave-1-signal-log-may18-21.md file to extract:
    - Per-contact signal data (score, signal type, key content, OOO, bounce)
    - Gist total delta from the May 21 snapshot section
    - Delivery self-test result if present

    Returns a dict in the same format as DUMMY_SIGNAL_DATA.
    If the log cannot be read or is not filled, returns None with an error message.
    """
    if not os.path.exists(log_path):
        return None, f"Signal log not found at: {log_path}"

    with open(log_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Check if the May 21 snapshot section has been filled
    if "[fill]" in content.lower() and "20:00 UTC" in content:
        unfilled = content.lower().count("[fill]")
        if unfilled > 5:
            return None, (
                f"Signal log has {unfilled} unfilled [fill] fields. "
                "User must complete the May 21 snapshot section before synthesis can run. "
                "Use --dummy to test with sample data."
            )

    # Extract contact-level data from the SIGNAL LOG TABLE
    contact_data = {}
    for c in CONTACTS:
        contact_data[c["name"]] = {
            "name": c["name"],
            "org": c["org"],
            "constituency": c["constituency"],
            "score": 0,
            "signal_type": "NO SIGNAL",
            "key_content": "Not logged in signal table.",
            "ooo": False,
            "bounce": False,
        }

    # Parse signal table rows (format: | Date | UTC Time | Contact | Org | Signal Type | Score | ... | Key Content | ... |)
    lines = content.split("\n")
    in_table = False
    for line in lines:
        if "| Date | UTC Time |" in line or "| Date | UTC" in line:
            in_table = True
            continue
        if in_table and line.startswith("|") and "---" not in line and "BASELINE" not in line:
            parts = [p.strip() for p in line.split("|")]
            if len(parts) >= 9:
                contact_name = parts[3].strip()
                signal_type = parts[5].strip() if len(parts) > 5 else ""
                score_raw = parts[6].strip() if len(parts) > 6 else "0"
                key_content = parts[8].strip() if len(parts) > 8 else ""

                # Match contact name to known contacts
                matched_name = None
                for c in CONTACTS:
                    if c["name"].lower() in contact_name.lower() or contact_name.lower() in c["name"].lower():
                        matched_name = c["name"]
                        break

                if matched_name:
                    try:
                        score = int(score_raw)
                    except (ValueError, TypeError):
                        score = 0
                    is_ooo = "OOO" in signal_type.upper()
                    is_bounce = "BOUNCE" in signal_type.upper()
                    contact_data[matched_name] = {
                        **contact_data[matched_name],
                        "score": score,
                        "signal_type": signal_type,
                        "key_content": key_content,
                        "ooo": is_ooo,
                        "bounce": is_bounce,
                    }
        elif in_table and line.strip() == "":
            in_table = False

    # Extract Gist delta from May 21 snapshot section
    gist_delta = 0
    gist_section_found = False
    for line in lines:
        if "Total Gist delta" in line and "fill" not in line.lower():
            parts = line.split("|")
            if len(parts) >= 3:
                val_raw = parts[2].strip()
                try:
                    gist_delta = int(val_raw)
                    gist_section_found = True
                except (ValueError, TypeError):
                    pass

    # Extract delivery self-test result if logged
    delivery = "inconclusive"
    for line in lines:
        line_lower = line.lower()
        if "delivery self-test" in line_lower or "test email" in line_lower:
            if "inbox" in line_lower:
                delivery = "inbox"
            elif "spam" in line_lower:
                delivery = "spam"

    parsed = {
        "contacts": list(contact_data.values()),
        "gist_delta": gist_delta,
        "delivery_self_test": delivery,
        "_gist_confirmed": gist_section_found,
    }
    return parsed, None


# ---------------------------------------------------------------------------
# Classification engine
# ---------------------------------------------------------------------------

def compute_qrp(contact_signals, gist_delta):
    """
    Compute Total Quality Reply Points per MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md Section 3.

    QRP = sum(quality points per Score 3+ reply) + min(gist_delta / 5, 1.0)
    Score 5 is STRONG OVERRIDE — detected separately before QRP computation.
    """
    contact_qrp = 0
    for c in contact_signals:
        score = c.get("score", 0)
        if c.get("ooo") or c.get("bounce"):
            continue  # OOO and bounces excluded from QRP
        if score == 5:
            return None  # STRONG OVERRIDE signal — caller handles
        elif score == 4:
            contact_qrp += 2
        elif score == 3:
            contact_qrp += 1
        # Score 0–2 contributes 0 QRP

    gist_bonus = min(gist_delta / 5.0, 1.0)
    return round(contact_qrp + gist_bonus, 2)


def effective_send_count(contact_signals):
    """Effective send count = total (5) minus hard bounces minus OOOs with return date after May 21."""
    total = len(contact_signals)
    excluded = sum(1 for c in contact_signals if c.get("bounce") or c.get("ooo"))
    return total - excluded


def substantive_response_rate(contact_signals):
    """Score 3+ replies / effective send count."""
    effective = effective_send_count(contact_signals)
    if effective == 0:
        return 0.0
    score3_plus = sum(
        1 for c in contact_signals
        if c.get("score", 0) >= 3 and not c.get("ooo") and not c.get("bounce")
    )
    return score3_plus / effective


def classify(signal_data):
    """
    Apply the three-rule classification from MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md Section 3.
    Returns (classification_str, details_dict).

    Classifications: STRONG, MODERATE, WEAK, TOO_EARLY, DELIVERY_PROBLEM
    """
    contacts = signal_data["contacts"]
    gist_delta = signal_data.get("gist_delta", 0)
    delivery = signal_data.get("delivery_self_test", "inconclusive")

    details = {}

    # Rule 1: Score 5 Override
    score5_contacts = [
        c for c in contacts if c.get("score") == 5 and not c.get("bounce") and not c.get("ooo")
    ]
    if score5_contacts:
        details["rule_triggered"] = "Rule 1 — Score 5 STRONG OVERRIDE"
        details["override_contact"] = score5_contacts[0]["name"]
        details["override_org"] = score5_contacts[0]["org"]
        details["override_content"] = score5_contacts[0].get("key_content", "")
        return "STRONG", details

    # Compute QRP for Rule 2
    qrp = compute_qrp(contacts, gist_delta)
    effective = effective_send_count(contacts)
    response_rate = substantive_response_rate(contacts)
    score3_plus_count = sum(
        1 for c in contacts
        if c.get("score", 0) >= 3 and not c.get("ooo") and not c.get("bounce")
    )

    details["qrp"] = qrp
    details["effective_send_count"] = effective
    details["response_rate"] = response_rate
    details["score3_plus_count"] = score3_plus_count
    details["gist_delta"] = gist_delta

    # Rule 2: Quality Reply Points
    if qrp is not None and qrp >= 2 and response_rate >= 0.40:
        details["rule_triggered"] = "Rule 2 — QRP >= 2 AND response rate >= 40%"
        return "STRONG", details

    if qrp is not None and qrp >= 2 and response_rate < 0.40:
        details["rule_triggered"] = "Rule 2 — QRP >= 2 but response rate < 40% (Gist-bonus-driven)"
        return "MODERATE", details

    if qrp is not None and qrp >= 1:
        details["rule_triggered"] = "Rule 2 — QRP >= 1 (at least one Score 3+ reply)"
        return "MODERATE", details

    if gist_delta > 10 and score3_plus_count == 0:
        details["rule_triggered"] = "Rule 2 — Gist delta > 10 with zero email replies (proxy signal)"
        return "MODERATE", details

    # Rule 3: Structural Fallback
    # Check if all contacts are silent (zero QRP, gist_delta <= 5)
    any_signal = any(
        c.get("score", 0) > 0 or c.get("ooo") or c.get("bounce")
        for c in contacts
    )

    if not any_signal and gist_delta <= 5:
        # Step 3a: Delivery check
        if delivery == "spam":
            details["rule_triggered"] = "Rule 3 — Delivery Problem (test email landed in spam)"
            return "DELIVERY_PROBLEM", details
        elif delivery == "inconclusive":
            details["rule_triggered"] = "Rule 3 — TOO EARLY (delivery inconclusive; cannot classify as WEAK)"
            details["note"] = "Run delivery self-test before classifying as WEAK or TOO EARLY."
            return "TOO_EARLY", details
        else:
            # Delivery confirmed (inbox), gist_delta <= 5, zero signals
            # Step 3b: Law school structural carve-out
            # If all five are silent and none have bounced: TOO EARLY (not WEAK)
            bounced = [c for c in contacts if c.get("bounce")]
            if not bounced:
                details["rule_triggered"] = "Rule 3 — TOO EARLY (zero signals, no bounces, delivery confirmed — law school window not closed)"
                details["note"] = (
                    "All 5 contacts silent at 72h. No bounces. Delivery confirmed. "
                    "Goodman and Chenoweth have 5–10 day academic cycles. "
                    "Classify TOO EARLY — not WEAK — until May 25 gate."
                )
                return "TOO_EARLY", details
            else:
                details["rule_triggered"] = "Rule 3 — WEAK (delivery confirmed, bounces detected, zero remaining signals)"
                return "WEAK", details

    # If QRP < 1 but gist_delta <= 5 and there ARE some signals (OOO, bounce, Score 1-2)
    if delivery == "inbox" and qrp is not None and qrp < 1 and gist_delta <= 5:
        details["rule_triggered"] = "Rule 3 — WEAK (delivery confirmed, QRP < 1, Gist delta <= 5)"
        details["note"] = (
            "WEAK classification requires delivery self-test confirmation. "
            "Before messaging audit, confirm this is not a delivery problem."
        )
        return "WEAK", details

    # Fallback to TOO EARLY if nothing else matches
    details["rule_triggered"] = "Fallback — TOO EARLY (no clear classification match)"
    return "TOO_EARLY", details


# ---------------------------------------------------------------------------
# Constituency assessment
# ---------------------------------------------------------------------------

def constituency_assessment(contacts):
    """Return per-constituency status string for CHECKIN.md template."""
    think_tanks = [c for c in contacts if c["constituency"] == "think_tank"]
    law_schools = [c for c in contacts if c["constituency"] == "law_school"]
    immigration = [c for c in contacts if c["constituency"] == "immigration_legal"]

    def assess(group):
        max_score = max((c.get("score", 0) for c in group if not c.get("bounce") and not c.get("ooo")), default=0)
        if max_score >= 5:
            return "STRONG OVERRIDE"
        elif max_score >= 4:
            return "STRONG"
        elif max_score >= 3:
            return "MODERATE"
        elif max_score >= 1:
            return "MONITORING (Score 1–2 only)"
        else:
            return "SILENT — MONITORING"

    think_tank_status = assess(think_tanks)
    law_school_status = "TOO EARLY — 5–10 day academic cycle; classify at May 25"
    immigration_status = assess(immigration)

    return {
        "think_tank": think_tank_status,
        "law_school": law_school_status,
        "immigration": immigration_status,
    }


# ---------------------------------------------------------------------------
# Strongest signal finder
# ---------------------------------------------------------------------------

def find_strongest_signal(contacts):
    """Return the contact with the highest score, or None if all are Score 0."""
    active = [c for c in contacts if not c.get("bounce") and not c.get("ooo")]
    if not active:
        return None
    best = max(active, key=lambda c: c.get("score", 0))
    if best.get("score", 0) == 0:
        return None
    return best


# ---------------------------------------------------------------------------
# Report and output generation
# ---------------------------------------------------------------------------

def format_contact_status(c):
    """Format a single contact for CHECKIN.md per-contact block."""
    if c.get("bounce"):
        return f"BOUNCED — re-verify address before May 25"
    elif c.get("ooo"):
        return f"OOO AUTOREPLY — return date TBD"
    elif c.get("score", 0) >= 1:
        return f"REPLIED Score {c['score']} — {c.get('key_content', 'no description')}"
    else:
        return "SILENT"


def generate_checkin_template(classification, details, signal_data):
    """Generate the CHECKIN.md synthesis post template (Section 8 of the framework)."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    contacts = signal_data["contacts"]
    gist_delta = signal_data.get("gist_delta", 0)
    qrp = details.get("qrp", 0)
    if qrp is None:
        qrp = "STRONG OVERRIDE"
    effective = details.get("effective_send_count", len(contacts))
    score3_count = details.get("score3_plus_count", 0)
    response_rate_pct = round(details.get("response_rate", 0) * 100, 1)

    # Per-contact status
    contact_lines = []
    for c in contacts:
        line = f"- {c['name']} ({c['org']}): {format_contact_status(c)}"
        contact_lines.append(line)
    contact_block = "\n".join(contact_lines)

    # Strongest signal
    strongest = find_strongest_signal(contacts)
    if strongest:
        strongest_str = (
            f"{strongest['name']}, {strongest['org']}, Score {strongest['score']} — "
            f"{strongest.get('key_content', 'no description')}"
        )
    else:
        strongest_str = "No substantive signals at 72h"

    # Constituency assessment
    const_data = constituency_assessment(contacts)

    # Path letter mapping
    path_letter = {"STRONG": "A", "MODERATE": "B", "WEAK": "C", "TOO_EARLY": "D", "DELIVERY_PROBLEM": "E"}.get(classification, "?")

    # Domain 42 days remaining
    deadline = datetime.datetime(2026, 5, 28, tzinfo=datetime.timezone.utc)
    days_to_deadline = (deadline - now_utc).days

    # Path-specific immediate action
    immediate_actions = {
        "STRONG": "Do NOT begin D57/D59 pre-production. Flag in CHECKIN.md. User approval required at May 25 gate.",
        "MODERATE": "Standard Phase 2 timeline holds. Continue monitoring. No accelerated action until May 25.",
        "WEAK": "Run delivery self-test if not done. Flag for messaging audit. User decision required: delivery problem or content problem.",
        "TOO_EARLY": "Continue monitoring. Delivery self-test if not run. No path decision before May 25.",
        "DELIVERY_PROBLEM": "STOP all further sends. Fix sender reputation. Do not revise content.",
    }

    # May 25 gate text
    may25_notes = {
        "STRONG": "Law school window closes Day 7. Think tank window (Weiser/Bassin) closes Day 5 (May 23). Confirm STRONG at May 25 gate before D57/D59 pre-production begins.",
        "MODERATE": "Law school window closes Day 7. Any Score 3+ arrival may upgrade to STRONG. Elias Day 7 threshold. Rerun full QRP formula with all data.",
        "WEAK": "Confirm WEAK with full 7-day data. If law school contacts (Goodman, Chenoweth) have replied at Score 3+, remove from WEAK diagnosis. Determine: delivery problem or content problem.",
        "TOO_EARLY": "MANDATORY RESOLUTION at May 25. All five contacts have had 7 days. TOO EARLY cannot persist past May 25 — resolves to STRONG, MODERATE, or WEAK.",
        "DELIVERY_PROBLEM": "Fix delivery before May 25. Re-test. Reclassify when inbox delivery is confirmed.",
    }

    # Strong/Weak user approval blocks
    user_decision_block = ""
    if classification == "STRONG":
        user_decision_block = "[STRONG PATH] User approval required: STRONG path activates D57 + D59 pre-production June 15. Confirm at May 25 gate before any pre-production work begins."
    elif classification == "WEAK":
        user_decision_block = "[WEAK PATH] User decision required: WEAK classification confirmed with delivery verified. Determine: delivery problem or content problem? See PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 4.4."
    elif classification == "DELIVERY_PROBLEM":
        user_decision_block = "[DELIVERY PROBLEM] Urgent: Test email landed in spam. Fix sender reputation before any further sends. Do not revise content. Check domain/IP reputation tools."

    template = f"""## Wave 1 Synthesis — May 21, 20:00 UTC

**Classification**: {classification}
**Total Quality Reply Points**: {qrp}
**Substantive response rate**: {response_rate_pct}% ({score3_count} of {effective} contacts at Score 3+)
**Gist delta**: {gist_delta} views since H+0 (May 18 ~08:00 UTC)

**Per-contact status**:
{contact_block}

**Strongest signal**: {strongest_str}
**Law school constituency**: {const_data['law_school']}
**Think tank constituency (Weiser, Bassin)**: {const_data['think_tank']}
**Immigration legal constituency (Elias)**: {const_data['immigration']}

**Selected path**: {path_letter}: {classification}
**Immediate next action**: {immediate_actions.get(classification, '[see path documentation]')}
**May 22–26 milestones**: See MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md Section 4.{path_letter if path_letter.isdigit() else '1' if classification == 'STRONG' else '2' if classification == 'MODERATE' else '3' if classification == 'WEAK' else '4'}

**May 25 final gate**: {may25_notes.get(classification, 'Run full synthesis formula with all available data.')}

**Domain 42 DEA deadline**: May 28 — {days_to_deadline} days remaining. Electronic filing deadline May 24, 11:59 p.m. ET. Check BATCH_1_CONTACT_LOG.md Domain 42 section for send status.

{user_decision_block}
"""
    return template.strip()


def generate_report(classification, details, signal_data):
    """Generate the terminal-format synthesis report."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    contacts = signal_data["contacts"]
    gist_delta = signal_data.get("gist_delta", 0)
    qrp = details.get("qrp", "N/A (Score 5 override)")

    lines = []
    lines.append("=" * 72)
    lines.append("WAVE 1 SYNTHESIS EXECUTION MONITOR")
    lines.append(f"Run time: {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}")
    lines.append("=" * 72)
    lines.append("")
    lines.append(f"CLASSIFICATION: {classification}")
    lines.append(f"Rule triggered: {details.get('rule_triggered', 'N/A')}")
    if details.get("note"):
        lines.append(f"Note: {details['note']}")
    lines.append("")
    lines.append("--- AGGREGATE METRICS ---")
    lines.append(f"Total sent: 5")
    lines.append(f"Effective send count: {details.get('effective_send_count', 'N/A')}")
    lines.append(f"Score 3+ replies: {details.get('score3_plus_count', 0)}")
    lines.append(f"Substantive response rate: {round(details.get('response_rate', 0) * 100, 1)}%")
    lines.append(f"Total Quality Reply Points: {qrp}")
    lines.append(f"Gist total delta: {gist_delta}")
    lines.append("")
    lines.append("--- PER-CONTACT STATUS ---")
    for c in contacts:
        status = format_contact_status(c)
        lines.append(f"  {c['name']} ({c['org']}): Score {c.get('score', 0)} — {status}")
    lines.append("")
    lines.append("--- PHASE 2 DOMAIN SEQUENCE ---")
    for date, action in DOMAIN_SEQUENCES.get(classification, []):
        lines.append(f"  {date}: {action}")
    lines.append("")
    lines.append("--- SUCCESS CRITERIA ---")
    lines.append("After synthesis, verify all of the following:")
    lines.append("  [ ] All 5 contacts have a row in the contact response summary")
    lines.append("  [ ] Aggregate metrics table complete — no [FILL] fields remaining")
    lines.append("  [ ] Exactly one classification is selected")
    lines.append("  [ ] CHECKIN.md post is present under 'Wave 1 Synthesis — May 21'")
    lines.append("  [ ] Domain 42 DEA deadline reminder included in CHECKIN.md post")
    lines.append("  [ ] May 25 final gate explicitly noted in CHECKIN.md post")
    lines.append("")
    lines.append(f"Output file: {OUTPUT_PATH}")
    lines.append(f"Run log: {RUN_LOG_PATH}")
    lines.append("=" * 72)
    return "\n".join(lines)


def write_output(classification, details, signal_data, checkin_template):
    """Write the synthesis output to synthesis-execution-output.md."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    content = f"""---
title: "Synthesis Execution Output — May 21, 2026"
generated: {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}
classification: {classification}
authority: MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md
---

# Wave 1 Synthesis Output — May 21, 2026

Generated by `synthesis-execution-monitor.py` at {now_utc.strftime('%H:%M UTC')}.
Classification: **{classification}**
Rule triggered: {details.get('rule_triggered', 'N/A')}

---

## CHECKIN.md Draft Entry

Copy the block below and post it under "Wave 1 Synthesis — May 21" in CHECKIN.md.
Fill any remaining [FILL] fields from live inbox data before posting.

```
{checkin_template}
```

---

## Phase 2 Domain Sequence — {classification} Path

| Date | Action |
|------|--------|
"""
    for date, action in DOMAIN_SEQUENCES.get(classification, []):
        content += f"| {date} | {action} |\n"

    content += f"""
---

## Classification Details

| Metric | Value |
|--------|-------|
| Classification | {classification} |
| Quality Reply Points | {details.get('qrp', 'STRONG OVERRIDE')} |
| Effective send count | {details.get('effective_send_count', 'N/A')} |
| Score 3+ count | {details.get('score3_plus_count', 0)} |
| Substantive response rate | {round(details.get('response_rate', 0) * 100, 1)}% |
| Gist delta | {signal_data.get('gist_delta', 0)} |
| Rule triggered | {details.get('rule_triggered', 'N/A')} |

---

## Per-Contact Data Used

| Contact | Org | Score | Signal Type | OOO | Bounce | Key Content |
|---------|-----|-------|-------------|-----|--------|-------------|
"""
    for c in signal_data.get("contacts", []):
        content += (
            f"| {c['name']} | {c['org']} | {c.get('score', 0)} "
            f"| {c.get('signal_type', 'NO SIGNAL')} "
            f"| {'Y' if c.get('ooo') else 'N'} "
            f"| {'Y' if c.get('bounce') else 'N'} "
            f"| {c.get('key_content', '')} |\n"
        )

    content += f"""
---

*Next steps: Post the CHECKIN.md draft above. Update wave-1-signal-log-may18-21.md May 21 snapshot section.*
*Authoritative framework: MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md*
*Generated: {now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')}*
"""
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def append_run_log(classification, details, dummy_mode):
    """Append a one-line timestamped run record to the run log."""
    now_utc = datetime.datetime.now(datetime.timezone.utc)
    mode = "DUMMY" if dummy_mode else "LIVE"
    qrp = details.get("qrp", "OVERRIDE")
    line = (
        f"{now_utc.strftime('%Y-%m-%d %H:%M:%S UTC')} | "
        f"{mode} | {classification} | QRP={qrp} | "
        f"rule={details.get('rule_triggered', 'N/A')[:60]}\n"
    )
    with open(RUN_LOG_PATH, "a", encoding="utf-8") as f:
        f.write(line)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description=(
            "Wave 1 Synthesis Execution Monitor. "
            "Reads the signal log and applies MAY_21_SYNTHESIS_EXECUTION_FRAMEWORK.md "
            "classification rules to produce a CHECKIN.md draft entry and terminal report."
        )
    )
    parser.add_argument(
        "--dummy",
        action="store_true",
        help="Run against built-in dummy signal data (for testing; no live file required).",
    )
    parser.add_argument(
        "--signal-log",
        default=SIGNAL_LOG_PATH,
        help=f"Path to wave-1-signal-log-may18-21.md (default: {SIGNAL_LOG_PATH})",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print report to terminal only; do not write output files.",
    )
    args = parser.parse_args()

    print()
    print("Wave 1 Synthesis Execution Monitor — Initializing")
    print(f"Mode: {'DUMMY (test data)' if args.dummy else 'LIVE (signal log)'}")
    print()

    if args.dummy:
        signal_data = DUMMY_SIGNAL_DATA
        parse_error = None
    else:
        signal_data, parse_error = parse_signal_log(args.signal_log)

    if parse_error:
        print(f"ERROR: {parse_error}")
        print()
        print("To test with dummy data: uv run python synthesis-execution-monitor.py --dummy")
        sys.exit(1)

    if signal_data is None:
        print("ERROR: Signal data is None. Cannot proceed.")
        sys.exit(1)

    # Run classification
    classification, details = classify(signal_data)

    # Generate outputs
    checkin_template = generate_checkin_template(classification, details, signal_data)
    report = generate_report(classification, details, signal_data)

    # Print terminal report
    print(report)

    if not args.dry_run:
        write_output(classification, details, signal_data, checkin_template)
        append_run_log(classification, details, dummy_mode=args.dummy)
        print()
        print(f"Output written to: {OUTPUT_PATH}")
        print(f"Run logged to: {RUN_LOG_PATH}")
    else:
        print()
        print("--- DRY RUN: CHECKIN.md DRAFT ---")
        print(checkin_template)
        print()
        print("--- DRY RUN: No files written ---")

    print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
