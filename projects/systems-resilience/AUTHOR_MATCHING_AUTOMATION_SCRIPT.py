#!/usr/bin/env python3
"""
Wave 2 Author-Domain Matching Automation
Systems Resilience Phase 6 — Item 88

Processes completed author intake JSON forms, scores authors on the 5-dimension
rubric from AUTHOR_DOMAIN_MAPPING_RUBRIC.md, matches authors to domains 60-65,
detects conflicts, assigns tiers, and produces a prioritized onboarding sequence.

Usage:
    python AUTHOR_MATCHING_AUTOMATION_SCRIPT.py --input intake_responses.json
    python AUTHOR_MATCHING_AUTOMATION_SCRIPT.py --demo     # run with built-in test data
    python AUTHOR_MATCHING_AUTOMATION_SCRIPT.py --demo --output results.json

Schema for intake_responses.json: list of AuthorIntakeRecord objects (see schema below).
Output: structured pairing recommendations, tier assignments, conflict flags, and
        prioritized onboarding sequence — written to stdout and optionally to --output.
"""

import json
import sys
import argparse
from dataclasses import dataclass, field, asdict
from typing import Optional
from enum import Enum
from datetime import date


# ---------------------------------------------------------------------------
# Constants — drawn directly from AUTHOR_DOMAIN_MAPPING_RUBRIC.md
# ---------------------------------------------------------------------------

DOMAINS = {
    60: {
        "name": "International Coordination",
        "short": "International Coordination",
        "difficulty_modifier": -2,
        "source_readiness_pct": 55,
        "description": (
            "How communities access international knowledge and mutual aid networks "
            "when national-level coordination fails or is adversarial."
        ),
        "min_d1": 3,
        "min_d5": 3,
    },
    61: {
        "name": "Intergenerational Knowledge Transmission",
        "short": "Intergenerational Knowledge",
        "difficulty_modifier": -1,
        "source_readiness_pct": 70,
        "description": (
            "Systems for preserving and transmitting critical practical skills across "
            "generations without formal educational infrastructure."
        ),
        "min_d1": 3,
        "min_d5": 3,
    },
    62: {
        "name": "Infrastructure Interdependencies",
        "short": "Infrastructure Interdependencies",
        "difficulty_modifier": -2,
        "source_readiness_pct": 60,
        "description": (
            "Community-scale cascade failure analysis and resilience design for "
            "interdependent physical infrastructure systems."
        ),
        "min_d1": 3,
        "min_d5": 3,
    },
    63: {
        "name": "Ecosystem Restoration",
        "short": "Ecosystem Restoration",
        "difficulty_modifier": 0,
        "source_readiness_pct": 82,
        "description": (
            "Soil ecology, agroecology, permaculture, and regenerative agriculture "
            "at community scale in Zone 5 Midwest context."
        ),
        "min_d1": 3,
        "min_d5": 3,
    },
    64: {
        "name": "Community Economic Resilience",
        "short": "Economic Resilience",
        "difficulty_modifier": 0,
        "source_readiness_pct": 78,
        "description": (
            "Local currencies, mutual credit, cooperative enterprise, commons governance, "
            "and inter-community trade when cash economy fails."
        ),
        "min_d1": 3,
        "min_d5": 3,
    },
    65: {
        "name": "Institutional Learning and Governance Scaling",
        "short": "Governance Scaling",
        "difficulty_modifier": -1,
        "source_readiness_pct": 72,
        "description": (
            "How community governance structures learn, adapt, and scale from 25 to "
            "100+ people — including failure mode analysis."
        ),
        "min_d1": 3,
        "min_d5": 3,
    },
}

# Approved adjacent domain pairings for split-domain assignments (Tier A only).
# From Section 5 of AUTHOR_DOMAIN_MAPPING_RUBRIC.md.
ADJACENT_PAIRINGS = [
    (63, 64),  # Ecosystem Restoration + Economic Resilience
    (61, 62),  # Intergenerational Knowledge + Infrastructure Interdependencies
    (64, 65),  # Economic Resilience + Governance Scaling
]

# Domains where source readiness is low enough to block split-domain assignment.
SPARSE_SOURCE_DOMAINS = {60, 62}  # modifier -2 domains

# Tier thresholds for Phase 6 (5-dimension rubric, max 25)
TIER_A_MIN = 20
TIER_B_MIN = 14
TIER_C_MIN = 6

# Tier thresholds for the Phase 5 intake form (4-dimension rubric, max 20)
PHASE5_TIER_A_MIN = 16
PHASE5_TIER_B_MIN = 11
PHASE5_TIER_C_MIN = 4


# ---------------------------------------------------------------------------
# Data Classes
# ---------------------------------------------------------------------------

class Tier(str, Enum):
    A = "A"
    B = "B"
    C = "C"
    HOLD = "HOLD"


@dataclass
class DomainScores:
    """Author's self-assessed scores for a specific domain.

    d1: Domain Knowledge (1-5) — directly in this domain
    d5: Domain Practitioner Grounding (1-5) — lived/field experience in this domain

    Note: d2 (Writing), d3 (Markdown), d4 (Research) are author-level, not domain-level.
    They are stored on AuthorIntakeRecord and used per-domain only in the assignment score.
    """
    domain_id: int
    d1_domain_knowledge: int  # 1-5
    d5_practitioner_grounding: int  # 1-5


@dataclass
class AuthorIntakeRecord:
    """JSON schema for a completed intake form response.

    This mirrors the AUTHOR_READINESS_INTAKE_FORM.md fields that are scorable.
    Free-text fields (writing samples, conflict description, etc.) are captured
    as optional strings for audit trail but do not affect scoring.
    """
    # Identity
    author_id: str  # unique slug, e.g. "author_001"
    name: str
    email: str
    background_type: str  # "academic" | "practitioner" | "organizer" | "mixed"
    zone5_familiarity: str  # "direct" | "adjacent" | "limited"

    # Cross-domain skill scores (Section 1 of intake form)
    d2_writing: int  # 1-5: Long-Form Practitioner Writing
    d3_markdown: int  # 1-5: Markdown and Digital Collaboration
    d4_research: int  # 1-5: Research and Citation

    # Domain-specific scores (one entry per domain the author is credible in)
    # Authors only fill in domains relevant to their background
    domain_scores: list[DomainScores]

    # Time commitment (Section 4)
    hours_per_week_confirmed: int  # confirmed available hours per week
    sprint_conflicts: list[str] = field(default_factory=list)  # date ranges as strings
    conflict_in_t7_window: bool = False  # June 14-19
    conflict_in_peer_review_window: bool = False  # June 24-27
    scope_flexibility_preference: str = "confident"  # "reduce_scope" | "extension" | "confident"

    # Communication (Section 3)
    response_time: str = "within_24h"  # "same_day" | "within_24h" | "within_48h" | "batch_weekly"

    # Support needs (Section 5)
    anticipated_challenge: str = ""
    zone5_note: str = ""

    # Optional audit fields (free text from form)
    writing_sample_titles: list[str] = field(default_factory=list)
    conflict_disagreement_response: str = ""
    additional_notes: str = ""


@dataclass
class DomainEligibility:
    domain_id: int
    eligible: bool
    tier_ceiling: Tier  # best tier author can achieve in this domain
    eligibility_reason: str
    d1_score: int
    d5_score: int
    raw_assignment_score: int = 0
    adjusted_assignment_score: int = 0


@dataclass
class ConflictFlag:
    severity: str  # "blocker" | "warning" | "note"
    rule: str
    description: str
    resolution: str


@dataclass
class AuthorMatchResult:
    author_id: str
    name: str
    email: str

    # Scoring
    total_score: int  # sum of best applicable d1 + d2 + d3 + d4 + d5 (max 25)
    tier: Tier
    tier_justification: str

    # Domain eligibility and ranking
    domain_eligibilities: list[DomainEligibility]
    ranked_eligible_domains: list[int]  # domain IDs, best-fit first

    # Assignment recommendation
    primary_domain_recommendation: Optional[int]
    split_domain_recommendation: Optional[tuple[int, int]]
    split_domain_eligible: bool
    split_domain_rationale: str

    # Conflict flags
    conflict_flags: list[ConflictFlag]

    # Onboarding tier details
    onboarding_depth: str
    checkin_cadence: str
    scope_word_count_range: str

    # Decision trace for audit
    decision_trace: list[str]


@dataclass
class DomainAssignmentPlan:
    domain_id: int
    domain_name: str
    assigned_authors: list[str]  # author_ids
    assignment_type: str  # "solo" | "split" | "unassigned" | "tier_c_with_support"
    confidence: float  # 0.0 - 1.0
    notes: list[str]
    contingency: str


@dataclass
class MatchingReport:
    generated_date: str
    authors_processed: int
    domains_covered: int
    domains_unassigned: list[int]
    author_results: list[AuthorMatchResult]
    domain_assignment_plan: list[DomainAssignmentPlan]
    prioritized_onboarding_sequence: list[dict]
    summary_stats: dict
    orchestrator_notes: list[str]


# ---------------------------------------------------------------------------
# Scoring Engine
# ---------------------------------------------------------------------------

def compute_tier_from_score(total: int) -> tuple[Tier, str]:
    """Return (Tier, justification) from a 25-point total score."""
    if total >= TIER_A_MIN:
        return Tier.A, f"Score {total}/25 >= {TIER_A_MIN} (Tier A threshold)"
    elif total >= TIER_B_MIN:
        return Tier.B, f"Score {total}/25 >= {TIER_B_MIN} (Tier B threshold)"
    elif total >= TIER_C_MIN:
        return Tier.C, f"Score {total}/25 >= {TIER_C_MIN} (Tier C threshold)"
    else:
        return Tier.HOLD, f"Score {total}/25 < {TIER_C_MIN} (Hold threshold)"


def apply_override_rules(
    author: AuthorIntakeRecord,
    domain_score: DomainScores,
    base_tier: Tier,
    trace: list[str],
) -> tuple[Tier, list[ConflictFlag]]:
    """Apply Section 2 modified tier assignment rules from the rubric.

    Returns (effective_tier, conflict_flags_generated).
    Override rules take precedence over the matrix score.
    """
    flags = []
    effective_tier = base_tier

    # Rule: D2 (writing) = 1 → do not assign, regardless of other scores
    if author.d2_writing == 1:
        effective_tier = Tier.HOLD
        flags.append(ConflictFlag(
            severity="blocker",
            rule="D2=1 override",
            description="Long-form writing score is 1. Writing production is the core deliverable.",
            resolution="Do not assign until D2 improves to at least 2.",
        ))
        trace.append("OVERRIDE: D2=1 → HOLD (writing is core deliverable)")

    # Rule: D1 = 1 → do not assign, regardless of total score
    if domain_score.d1_domain_knowledge == 1:
        if effective_tier != Tier.HOLD:
            effective_tier = Tier.HOLD
        flags.append(ConflictFlag(
            severity="blocker",
            rule="D1=1 override",
            description=f"Domain Knowledge score for domain {domain_score.domain_id} is 1. "
                        "Cannot produce accurate content without domain knowledge.",
            resolution="Do not assign to this domain.",
        ))
        trace.append(f"OVERRIDE: D1=1 for domain {domain_score.domain_id} → HOLD")

    # Rule: D5=1 and D1=2 → Tier C maximum
    if domain_score.d5_practitioner_grounding == 1 and domain_score.d1_domain_knowledge == 2:
        if effective_tier in (Tier.A, Tier.B):
            effective_tier = Tier.C
            flags.append(ConflictFlag(
                severity="warning",
                rule="D5=1,D1=2 override",
                description=f"Practitioner grounding (D5=1) is very low for domain "
                            f"{domain_score.domain_id}. D1=2 only. Capped at Tier C.",
                resolution="Reduce scope to 2,500-3,500 words. Project lead provides source sprint support.",
            ))
            trace.append(f"OVERRIDE: D5=1,D1=2 for domain {domain_score.domain_id} → cap Tier C")

    # Rule: D4 < 3 → Tier B maximum
    if author.d4_research < 3 and effective_tier == Tier.A:
        effective_tier = Tier.B
        flags.append(ConflictFlag(
            severity="warning",
            rule="D4<3 override",
            description=f"Research/Citation score (D4={author.d4_research}) is below 3. "
                        "Tier B maximum.",
            resolution="Project lead performs citation audit at T+7.",
        ))
        trace.append(f"OVERRIDE: D4={author.d4_research} < 3 → cap Tier B, citation audit at T+7")

    return effective_tier, flags


def score_author_for_domain(
    author: AuthorIntakeRecord,
    domain_id: int,
    trace: list[str],
) -> DomainEligibility:
    """Compute eligibility and assignment score for one author×domain pair."""
    domain = DOMAINS[domain_id]

    # Find this author's scores for the requested domain
    ds = next(
        (s for s in author.domain_scores if s.domain_id == domain_id),
        DomainScores(domain_id=domain_id, d1_domain_knowledge=0, d5_practitioner_grounding=0),
    )

    d1 = ds.d1_domain_knowledge
    d5 = ds.d5_practitioner_grounding
    d2 = author.d2_writing
    d4 = author.d4_research
    mod = domain["difficulty_modifier"]
    min_d1 = domain["min_d1"]
    min_d5 = domain["min_d5"]

    trace.append(f"  Domain {domain_id} ({domain['short']}): D1={d1}, D5={d5}, D2={d2}, D4={d4}, modifier={mod}")

    # Step 1: Eligibility screen (both D1 and D5 must be >= 3 for Tier A/B)
    if d1 >= min_d1 and d5 >= min_d5:
        eligible = True
        tier_ceiling = Tier.A  # full eligibility — actual tier determined by total score
        eligibility_reason = f"D1={d1} >= {min_d1} and D5={d5} >= {min_d5}: full eligibility"
    elif d1 >= min_d1 or d5 >= min_d5:
        eligible = True
        tier_ceiling = Tier.C  # only one dimension meets threshold → Tier C max
        eligibility_reason = (
            f"Only one dimension meets threshold (D1={d1}, D5={d5}): eligible for Tier C only"
        )
    else:
        eligible = False
        tier_ceiling = Tier.HOLD
        eligibility_reason = (
            f"Both D1={d1} and D5={d5} are below threshold ({min_d1}/{min_d5}): ineligible"
        )

    if not eligible:
        trace.append(f"    → INELIGIBLE: {eligibility_reason}")
        return DomainEligibility(
            domain_id=domain_id,
            eligible=False,
            tier_ceiling=Tier.HOLD,
            eligibility_reason=eligibility_reason,
            d1_score=d1,
            d5_score=d5,
            raw_assignment_score=0,
            adjusted_assignment_score=0,
        )

    # Step 2: Compute assignment score
    # Formula: (D1 × 2) + (D5 × 2) + D2 + D4 — max 24
    raw_score = (d1 * 2) + (d5 * 2) + d2 + d4
    adjusted_score = raw_score + mod

    trace.append(f"    → ELIGIBLE: raw={(d1*2)}+{(d5*2)}+{d2}+{d4}={raw_score}, "
                 f"adjusted={raw_score}{mod:+d}={adjusted_score}")

    return DomainEligibility(
        domain_id=domain_id,
        eligible=True,
        tier_ceiling=tier_ceiling,
        eligibility_reason=eligibility_reason,
        d1_score=d1,
        d5_score=d5,
        raw_assignment_score=raw_score,
        adjusted_assignment_score=adjusted_score,
    )


def compute_author_total_score(author: AuthorIntakeRecord) -> int:
    """Compute the author's overall 25-point score.

    Uses the best available D1 and D5 scores across all domains the author
    has grounding in, plus the cross-domain D2, D3, D4.
    """
    if not author.domain_scores:
        return author.d2_writing + author.d3_markdown + author.d4_research

    best_d1 = max(ds.d1_domain_knowledge for ds in author.domain_scores)
    best_d5 = max(ds.d5_practitioner_grounding for ds in author.domain_scores)
    return best_d1 + author.d2_writing + author.d3_markdown + author.d4_research + best_d5


def check_operational_conflicts(
    author: AuthorIntakeRecord,
    trace: list[str],
) -> list[ConflictFlag]:
    """Check for scheduling and operational conflicts from Section 4 intake data."""
    flags = []

    if author.hours_per_week_confirmed < 4:
        flags.append(ConflictFlag(
            severity="blocker",
            rule="hours_below_minimum",
            description=f"Author confirmed only {author.hours_per_week_confirmed} hrs/week. "
                        "Minimum is 4 hrs/week for solo domain.",
            resolution="Do not assign until availability is confirmed at ≥4 hrs/week.",
        ))
        trace.append(f"CONFLICT: hours_per_week={author.hours_per_week_confirmed} < 4 → blocker")

    if author.conflict_in_t7_window:
        flags.append(ConflictFlag(
            severity="warning",
            rule="conflict_t7_window",
            description="Author has a conflict in the T+7 checkpoint window (June 14-19).",
            resolution="Adjust T+7 checkpoint date by 1-2 days; confirm alternative date before June 12.",
        ))
        trace.append("CONFLICT: availability gap in T+7 window → warning")

    if author.conflict_in_peer_review_window:
        flags.append(ConflictFlag(
            severity="warning",
            rule="conflict_peer_review_window",
            description="Author has a conflict in the peer review window (June 24-27). "
                        "This blocks partner's revision timeline.",
            resolution="Adjust peer review window by 1-2 days; notify peer reviewer of adjustment.",
        ))
        trace.append("CONFLICT: availability gap in peer review window → warning")

    if author.response_time == "batch_weekly":
        flags.append(ConflictFlag(
            severity="warning",
            rule="slow_response_time",
            description="Author typically batches communications weekly. "
                        "Sprint requires response within 48 hours.",
            resolution="Author must agree to daily platform message check during sprint. "
                       "Confirm this explicitly before onboarding.",
        ))
        trace.append("CONFLICT: response_time=batch_weekly → warning")

    if author.zone5_familiarity == "limited":
        flags.append(ConflictFlag(
            severity="note",
            rule="limited_zone5_familiarity",
            description="Author has limited Zone 5 Midwest context familiarity.",
            resolution="Note in scope document; add Zone 5 calibration question to T+7 review.",
        ))
        trace.append("NOTE: zone5_familiarity=limited → note in scope document")

    return flags


def check_split_domain_eligibility(
    author: AuthorIntakeRecord,
    tier: Tier,
    primary_domain: Optional[int],
    domain_eligibilities: dict[int, DomainEligibility],
    trace: list[str],
) -> tuple[bool, Optional[tuple[int, int]], str]:
    """Determine if the author is eligible for a split-domain assignment.

    Returns (eligible, pairing_or_None, rationale).
    All three conditions from Section 5 of the rubric must be met.
    """
    if tier != Tier.A:
        trace.append("SPLIT-DOMAIN: Not eligible — Tier A required")
        return False, None, "Split-domain requires Tier A. Author is Tier {}.".format(tier.value)

    if author.hours_per_week_confirmed < 8:
        trace.append(f"SPLIT-DOMAIN: Not eligible — only {author.hours_per_week_confirmed} hrs/week confirmed (need 8+)")
        return (
            False,
            None,
            f"Split-domain requires 8+ hrs/week. Author confirmed {author.hours_per_week_confirmed} hrs/week.",
        )

    if primary_domain is None:
        trace.append("SPLIT-DOMAIN: No primary domain assigned, cannot evaluate pairing")
        return False, None, "No primary domain assigned."

    # Check if any adjacent pairing is eligible
    for pair in ADJACENT_PAIRINGS:
        if primary_domain not in pair:
            continue
        other_domain = pair[0] if pair[1] == primary_domain else pair[1]

        # Red flag: either domain in the pair has modifier -2 (sparse sources)
        if primary_domain in SPARSE_SOURCE_DOMAINS or other_domain in SPARSE_SOURCE_DOMAINS:
            trace.append(
                f"SPLIT-DOMAIN: Pairing ({primary_domain},{other_domain}) flagged — "
                f"one domain has source readiness modifier -2"
            )
            continue

        other_eligibility = domain_eligibilities.get(other_domain)
        if other_eligibility is None or not other_eligibility.eligible:
            continue

        # Author must score 20+ for BOTH domains — we check adjusted score threshold.
        # A rough proxy: if both domains yield adjusted_score >= 16 (equivalent to Tier A
        # performance on the per-domain scale), the pairing is viable.
        primary_elig = domain_eligibilities.get(primary_domain)
        if (
            primary_elig
            and primary_elig.adjusted_assignment_score >= 16
            and other_eligibility.adjusted_assignment_score >= 16
        ):
            trace.append(
                f"SPLIT-DOMAIN: Eligible — Tier A, {author.hours_per_week_confirmed} hrs/wk, "
                f"adjacent pairing ({primary_domain},{other_domain}), both scores >=16"
            )
            return (
                True,
                (primary_domain, other_domain),
                (
                    f"Tier A author with {author.hours_per_week_confirmed} hrs/week confirmed. "
                    f"Adjacent pairing ({primary_domain},{other_domain}) approved. "
                    f"Both domain scores above threshold."
                ),
            )

    trace.append("SPLIT-DOMAIN: No eligible adjacent pairing found")
    return (
        False,
        None,
        "No approved adjacent pairing found for primary domain {} where both domains score >=16.".format(
            primary_domain
        ),
    )


# ---------------------------------------------------------------------------
# Onboarding configuration
# ---------------------------------------------------------------------------

ONBOARDING_CONFIG = {
    Tier.A: {
        "depth": "Scope document + annotated bibliography, no extra scaffolding notes.",
        "checkin_cadence": "Formal checkpoints only (T+7, T+14, T+21). No T+3 check-in unless author posts a question.",
        "scope_word_count_range": "8,000–10,000 words (solo) or 14,000–18,000 words total (split-domain)",
    },
    Tier.B: {
        "depth": "Scope document + introductory note on key scope constraints. Peer review protocol primer at T+7.",
        "checkin_cadence": "Formal checkpoints (T+7, T+14, T+21) plus T+3 light check-in: 'How is outline going?'",
        "scope_word_count_range": "8,000–10,000 words. Project lead spot-checks Section 1 (citations) before final submission.",
    },
    Tier.C: {
        "depth": (
            "Scope consultation June 14 (15-min async exchange to narrow scope). "
            "Reduced word count target. T+3 check-in mandatory. "
            "Peer review paired with Tier A or B author. "
            "Project lead light editorial pass at T+14."
        ),
        "checkin_cadence": "Weekly check-ins. T+3 mandatory: confirm author has started outline.",
        "scope_word_count_range": "2,500–3,500 words. Sections reduced accordingly.",
    },
    Tier.HOLD: {
        "depth": "Do not onboard. Resolve blocking flags first.",
        "checkin_cadence": "N/A — hold until flags resolved.",
        "scope_word_count_range": "N/A",
    },
}


# ---------------------------------------------------------------------------
# Main matching engine
# ---------------------------------------------------------------------------

def process_author(author: AuthorIntakeRecord) -> AuthorMatchResult:
    """Run the full matching algorithm for a single author.

    Implements the 5-step algorithm from Section 3 of AUTHOR_DOMAIN_MAPPING_RUBRIC.md,
    plus override rules (Section 2), conflict detection, and onboarding configuration.
    """
    trace: list[str] = []
    all_flags: list[ConflictFlag] = []

    trace.append(f"=== PROCESSING AUTHOR: {author.name} ({author.author_id}) ===")

    # Step 0: Compute total score and provisional tier
    total_score = compute_author_total_score(author)
    provisional_tier, tier_justification = compute_tier_from_score(total_score)
    trace.append(f"Total score: {total_score}/25 → Provisional tier: {provisional_tier.value} ({tier_justification})")

    # Step 1 + 2 + 3: Score all domains and compute eligibilities
    trace.append("--- Domain eligibility and assignment scores ---")
    domain_eligibilities: dict[int, DomainEligibility] = {}
    for domain_id in sorted(DOMAINS.keys()):
        elig = score_author_for_domain(author, domain_id, trace)
        domain_eligibilities[domain_id] = elig

    # Apply override rules per eligible domain and collect flags
    effective_tier = provisional_tier
    for domain_id, elig in domain_eligibilities.items():
        if not elig.eligible:
            continue
        ds = next(
            (s for s in author.domain_scores if s.domain_id == domain_id),
            DomainScores(domain_id=domain_id, d1_domain_knowledge=0, d5_practitioner_grounding=0),
        )
        override_tier, override_flags = apply_override_rules(author, ds, effective_tier, trace)
        # The most restrictive override wins globally
        tier_order = [Tier.A, Tier.B, Tier.C, Tier.HOLD]
        if tier_order.index(override_tier) > tier_order.index(effective_tier):
            effective_tier = override_tier
        all_flags.extend(override_flags)

    if effective_tier != provisional_tier:
        tier_justification += f" | Overridden to {effective_tier.value} by rule-based constraint"
    trace.append(f"Effective tier after override rules: {effective_tier.value}")

    # Check operational conflicts
    operational_flags = check_operational_conflicts(author, trace)
    all_flags.extend(operational_flags)

    # Step 4: Rank eligible domains
    eligible_domains_scored = [
        (domain_id, elig.adjusted_assignment_score)
        for domain_id, elig in domain_eligibilities.items()
        if elig.eligible and elig.tier_ceiling != Tier.HOLD
    ]
    ranked_eligible_domains = [
        domain_id
        for domain_id, _ in sorted(eligible_domains_scored, key=lambda x: x[1], reverse=True)
    ]

    trace.append(f"Ranked eligible domains (best fit first): {ranked_eligible_domains}")

    # Determine primary domain recommendation
    primary_domain = ranked_eligible_domains[0] if ranked_eligible_domains else None
    if primary_domain is not None:
        trace.append(f"Primary domain recommendation: Domain {primary_domain} "
                     f"({DOMAINS[primary_domain]['short']}), "
                     f"adjusted score {domain_eligibilities[primary_domain].adjusted_assignment_score}")

    # Step 5: Check split-domain eligibility
    split_eligible, split_pairing, split_rationale = check_split_domain_eligibility(
        author, effective_tier, primary_domain, domain_eligibilities, trace
    )

    # Onboarding configuration
    onboard = ONBOARDING_CONFIG[effective_tier]

    return AuthorMatchResult(
        author_id=author.author_id,
        name=author.name,
        email=author.email,
        total_score=total_score,
        tier=effective_tier,
        tier_justification=tier_justification,
        domain_eligibilities=list(domain_eligibilities.values()),
        ranked_eligible_domains=ranked_eligible_domains,
        primary_domain_recommendation=primary_domain,
        split_domain_recommendation=split_pairing,
        split_domain_eligible=split_eligible,
        split_domain_rationale=split_rationale,
        conflict_flags=all_flags,
        onboarding_depth=onboard["depth"],
        checkin_cadence=onboard["checkin_cadence"],
        scope_word_count_range=onboard["scope_word_count_range"],
        decision_trace=trace,
    )


# ---------------------------------------------------------------------------
# Pool-level matching and conflict resolution
# ---------------------------------------------------------------------------

def resolve_domain_conflicts(
    results: list[AuthorMatchResult],
) -> list[DomainAssignmentPlan]:
    """Apply Step 5 conflict resolution across the full author pool.

    When two authors compete for the same domain:
    - Higher Tier author takes priority
    - If same tier, higher D5 (practitioner grounding) wins
    - Loser reassigned to their second-ranked eligible domain
    """
    # Build a mapping: domain_id → list of (author_result, domain_eligibility)
    domain_candidates: dict[int, list[tuple[AuthorMatchResult, DomainEligibility]]] = {
        d: [] for d in DOMAINS
    }

    for result in results:
        if result.tier == Tier.HOLD:
            continue
        if result.primary_domain_recommendation is None:
            continue
        elig = next(
            (e for e in result.domain_eligibilities
             if e.domain_id == result.primary_domain_recommendation),
            None,
        )
        if elig:
            domain_candidates[result.primary_domain_recommendation].append((result, elig))

    tier_rank = {Tier.A: 0, Tier.B: 1, Tier.C: 2, Tier.HOLD: 3}

    plans: list[DomainAssignmentPlan] = []
    assigned_authors: set[str] = set()

    for domain_id in sorted(DOMAINS.keys()):
        candidates = domain_candidates[domain_id]
        notes: list[str] = []

        if not candidates:
            plans.append(DomainAssignmentPlan(
                domain_id=domain_id,
                domain_name=DOMAINS[domain_id]["name"],
                assigned_authors=[],
                assignment_type="unassigned",
                confidence=0.0,
                notes=["No eligible authors in current pool for this domain."],
                contingency=(
                    "Assign the highest-scoring eligible Tier C author with project lead "
                    "co-research support. Flag for additional source sprint before production."
                ),
            ))
            continue

        # Sort by tier, then D5 descending
        candidates.sort(key=lambda x: (tier_rank[x[0].tier], -x[1].d5_score))

        winner_result, winner_elig = candidates[0]
        assigned_authors.add(winner_result.author_id)

        # Confidence: Tier A with high score = high confidence
        score_pct = winner_elig.adjusted_assignment_score / 22  # 22 = theoretical max adjusted
        confidence = round(min(score_pct, 1.0), 2)

        if len(candidates) > 1:
            loser_result, _ = candidates[1]
            notes.append(
                f"Conflict resolved: {winner_result.name} (Tier {winner_result.tier.value}, "
                f"D5={winner_elig.d5_score}) preferred over {loser_result.name} "
                f"(Tier {loser_result.tier.value})."
            )
            notes.append(
                f"{loser_result.name} reassigned to second-ranked eligible domain "
                f"(see their individual result)."
            )

        assignment_type = "solo"
        # Check if winner is doing split-domain
        if winner_result.split_domain_eligible and winner_result.split_domain_recommendation:
            pair = winner_result.split_domain_recommendation
            if domain_id in pair:
                assignment_type = "split"
                other = pair[0] if pair[1] == domain_id else pair[1]
                notes.append(
                    f"Split-domain assignment: {winner_result.name} covers both "
                    f"Domain {domain_id} and Domain {other}."
                )

        plans.append(DomainAssignmentPlan(
            domain_id=domain_id,
            domain_name=DOMAINS[domain_id]["name"],
            assigned_authors=[winner_result.author_id],
            assignment_type=assignment_type,
            confidence=confidence,
            notes=notes,
            contingency=(
                "If author withdraws: reassign from ranked-eligible pool. "
                f"Current second choice: {candidates[1][0].name if len(candidates) > 1 else 'None — source sprint required'}."
            ),
        ))

    return plans


def build_onboarding_sequence(
    results: list[AuthorMatchResult],
    domain_plans: list[DomainAssignmentPlan],
) -> list[dict]:
    """Produce the prioritized onboarding sequence.

    Ordering logic:
    1. HOLD-tier authors first (needs resolution before June 12)
    2. Tier A authors with assignments to high-criticality domains (60, 62 — sparse sources)
    3. Tier A authors with standard domains
    4. Tier B authors ordered by domain criticality
    5. Tier C authors last (need scope consultation first)
    """
    # Build domain criticality map (lower source readiness = higher criticality)
    domain_criticality = {
        d: (100 - info["source_readiness_pct"])
        for d, info in DOMAINS.items()
    }

    tier_order = {Tier.HOLD: 0, Tier.A: 1, Tier.B: 2, Tier.C: 3}

    sequence = []
    for result in results:
        domain_id = result.primary_domain_recommendation
        criticality = domain_criticality.get(domain_id, 0) if domain_id else 0

        # Count blocking conflict flags
        blocker_count = sum(1 for f in result.conflict_flags if f.severity == "blocker")
        warning_count = sum(1 for f in result.conflict_flags if f.severity == "warning")

        sequence.append({
            "author_id": result.author_id,
            "name": result.name,
            "tier": result.tier.value,
            "primary_domain": domain_id,
            "primary_domain_name": DOMAINS[domain_id]["short"] if domain_id else "Unassigned",
            "split_domain": result.split_domain_recommendation,
            "total_score": result.total_score,
            "domain_criticality": criticality,
            "blocker_count": blocker_count,
            "warning_count": warning_count,
            "onboarding_depth": result.onboarding_depth,
            "checkin_cadence": result.checkin_cadence,
            "scope_word_count_range": result.scope_word_count_range,
            "conflict_flags": [
                {"severity": f.severity, "rule": f.rule, "description": f.description,
                 "resolution": f.resolution}
                for f in result.conflict_flags
            ],
            # Sort keys — lower = earlier in sequence
            "_sort_tier": tier_order[result.tier],
            "_sort_criticality": -criticality,  # negate: higher criticality first
            "_sort_blockers": -blocker_count,   # negate: blockers first (need resolution)
        })

    # Sort: HOLD first, then by tier, then by domain criticality descending
    sequence.sort(key=lambda x: (x["_sort_tier"], x["_sort_blockers"], x["_sort_criticality"]))

    # Add sequence number and remove internal sort keys
    for i, entry in enumerate(sequence):
        entry["onboarding_sequence_number"] = i + 1
        entry["onboarding_action"] = _derive_onboarding_action(entry)
        for k in list(entry.keys()):
            if k.startswith("_sort"):
                del entry[k]

    return sequence


def _derive_onboarding_action(entry: dict) -> str:
    """Generate a concise first action for this author in the onboarding sequence."""
    if entry["tier"] == "HOLD":
        return (
            "HOLD — resolve all blocker flags before proceeding. "
            "Do not send onboarding kit until flags cleared."
        )
    if entry["blocker_count"] > 0:
        return (
            f"URGENT: {entry['blocker_count']} blocker flag(s) require resolution before June 12. "
            "Do not assign domain until cleared."
        )
    if entry["tier"] == "C":
        return (
            "Schedule 15-minute scope consultation June 14. "
            "Reduce word count target to 2,500-3,500. "
            "Send onboarding kit after scope consultation."
        )
    if entry["tier"] == "A":
        if entry["split_domain"]:
            return (
                f"Send scope document + annotated bibliography for Domains "
                f"{entry['split_domain'][0]} and {entry['split_domain'][1]}. "
                "No extra scaffolding required."
            )
        return (
            f"Send scope document + annotated bibliography for Domain "
            f"{entry['primary_domain']} ({entry['primary_domain_name']}). "
            "No extra scaffolding required."
        )
    # Tier B
    if entry["warning_count"] > 0:
        return (
            f"Send scope document with scope constraint note for Domain "
            f"{entry['primary_domain']} ({entry['primary_domain_name']}). "
            f"Address {entry['warning_count']} warning flag(s) explicitly in onboarding communication. "
            "Schedule T+3 check-in."
        )
    return (
        f"Send scope document + scope constraint intro note for Domain "
        f"{entry['primary_domain']} ({entry['primary_domain_name']}). "
        "Schedule T+3 check-in."
    )


# ---------------------------------------------------------------------------
# Report assembly and output
# ---------------------------------------------------------------------------

def build_report(
    authors: list[AuthorIntakeRecord],
    results: list[AuthorMatchResult],
    domain_plans: list[DomainAssignmentPlan],
    onboarding_seq: list[dict],
) -> MatchingReport:
    unassigned_domains = [
        p.domain_id for p in domain_plans if p.assignment_type == "unassigned"
    ]

    tier_counts = {t.value: 0 for t in Tier}
    for r in results:
        tier_counts[r.tier.value] += 1

    blocker_authors = [r.author_id for r in results if any(f.severity == "blocker" for f in r.conflict_flags)]

    orchestrator_notes = []
    if unassigned_domains:
        orchestrator_notes.append(
            f"CRITICAL: {len(unassigned_domains)} domain(s) have no eligible author in current pool: "
            f"{[DOMAINS[d]['name'] for d in unassigned_domains]}. "
            "Activate secondary recruitment or self-execute fallback for these domains."
        )
    if blocker_authors:
        orchestrator_notes.append(
            f"URGENT: {len(blocker_authors)} author(s) have unresolved blocker flags: "
            f"{blocker_authors}. Must be resolved before June 12 onboarding deadline."
        )
    if tier_counts.get("HOLD", 0) > 0:
        orchestrator_notes.append(
            f"{tier_counts['HOLD']} author(s) in HOLD status. "
            "Review and either resolve or release their slot before June 12."
        )

    split_domain_count = sum(
        1 for r in results if r.split_domain_eligible and r.split_domain_recommendation
    )
    if split_domain_count:
        orchestrator_notes.append(
            f"{split_domain_count} author(s) are eligible for split-domain assignment. "
            "Project lead must confirm bandwidth with each before June 14 matching session."
        )

    return MatchingReport(
        generated_date=str(date.today()),
        authors_processed=len(authors),
        domains_covered=len(DOMAINS) - len(unassigned_domains),
        domains_unassigned=unassigned_domains,
        author_results=results,
        domain_assignment_plan=domain_plans,
        prioritized_onboarding_sequence=onboarding_seq,
        summary_stats={
            "tier_distribution": tier_counts,
            "split_domain_eligible": split_domain_count,
            "domains_with_conflict": sum(1 for p in domain_plans if len(p.notes) > 0),
            "authors_with_blockers": len(blocker_authors),
        },
        orchestrator_notes=orchestrator_notes,
    )


def print_report(report: MatchingReport) -> None:
    """Print a human-readable summary of the matching report to stdout."""
    sep = "=" * 72

    print(sep)
    print("WAVE 2 AUTHOR-DOMAIN MATCHING REPORT")
    print(f"Generated: {report.generated_date}")
    print(sep)
    print(f"Authors processed: {report.authors_processed}")
    print(f"Domains covered:   {report.domains_covered}/6")
    if report.domains_unassigned:
        print(f"Domains UNASSIGNED: {[DOMAINS[d]['short'] for d in report.domains_unassigned]}")
    print()

    if report.orchestrator_notes:
        print("ORCHESTRATOR NOTES (action required before June 12):")
        for note in report.orchestrator_notes:
            print(f"  >> {note}")
        print()

    print("SUMMARY STATISTICS:")
    for k, v in report.summary_stats.items():
        print(f"  {k}: {v}")
    print()

    print(sep)
    print("DOMAIN ASSIGNMENT PLAN")
    print(sep)
    for plan in sorted(report.domain_assignment_plan, key=lambda p: p.domain_id):
        status_icon = {
            "solo": "[SOLO]",
            "split": "[SPLIT]",
            "unassigned": "[UNASSIGNED]",
            "tier_c_with_support": "[TIER-C+SUPPORT]",
        }.get(plan.assignment_type, "[?]")
        authors_str = ", ".join(plan.assigned_authors) if plan.assigned_authors else "NONE"
        print(f"\nDomain {plan.domain_id}: {plan.domain_name}")
        print(f"  Status: {status_icon}  Assigned: {authors_str}  Confidence: {plan.confidence:.0%}")
        for note in plan.notes:
            print(f"  NOTE: {note}")
        print(f"  Contingency: {plan.contingency}")

    print()
    print(sep)
    print("AUTHOR RESULTS (by tier)")
    print(sep)
    for result in sorted(report.author_results, key=lambda r: (r.tier.value, -r.total_score)):
        print(f"\n{result.name} ({result.author_id})")
        print(f"  Tier: {result.tier.value}  |  Score: {result.total_score}/25")
        print(f"  Primary domain recommendation: "
              f"{result.primary_domain_recommendation} "
              f"({DOMAINS[result.primary_domain_recommendation]['short'] if result.primary_domain_recommendation else 'None'})")
        if result.split_domain_eligible:
            print(f"  Split-domain eligible: YES — Pair {result.split_domain_recommendation}")
        if result.conflict_flags:
            for flag in result.conflict_flags:
                icon = {"blocker": "[BLOCKER]", "warning": "[WARNING]", "note": "[NOTE]"}.get(flag.severity, "[?]")
                print(f"  {icon} {flag.rule}: {flag.description}")
                print(f"    Resolution: {flag.resolution}")
        else:
            print("  No conflict flags.")

    print()
    print(sep)
    print("PRIORITIZED ONBOARDING SEQUENCE (June 12-14 execution order)")
    print(sep)
    for entry in report.prioritized_onboarding_sequence:
        tier_label = f"Tier {entry['tier']}"
        domain_label = f"Domain {entry['primary_domain']} ({entry['primary_domain_name']})" if entry['primary_domain'] else "No domain"
        flags_label = ""
        if entry['blocker_count']:
            flags_label = f"  [{entry['blocker_count']} BLOCKER(S)]"
        elif entry['warning_count']:
            flags_label = f"  [{entry['warning_count']} WARNING(S)]"
        print(f"\n{entry['onboarding_sequence_number']}. {entry['name']} | {tier_label} | {domain_label}{flags_label}")
        print(f"   Score: {entry['total_score']}/25")
        print(f"   Action: {entry['onboarding_action']}")
        print(f"   Scope: {entry['scope_word_count_range']}")
        print(f"   Check-ins: {entry['checkin_cadence']}")


# ---------------------------------------------------------------------------
# Sample test data (synthetic authors covering all edge cases)
# ---------------------------------------------------------------------------

SAMPLE_AUTHORS: list[AuthorIntakeRecord] = [
    # Author A — Tier A, ecosystem restoration + economic resilience split candidate
    AuthorIntakeRecord(
        author_id="author_001",
        name="Dr. Maya Chen",
        email="mchen@uwmadison.edu",
        background_type="academic",
        zone5_familiarity="direct",
        d2_writing=5,
        d3_markdown=4,
        d4_research=5,
        domain_scores=[
            DomainScores(domain_id=63, d1_domain_knowledge=5, d5_practitioner_grounding=5),
            DomainScores(domain_id=64, d1_domain_knowledge=4, d5_practitioner_grounding=4),
        ],
        hours_per_week_confirmed=10,
        sprint_conflicts=[],
        conflict_in_t7_window=False,
        conflict_in_peer_review_window=False,
        scope_flexibility_preference="confident",
        response_time="same_day",
        anticipated_challenge="calibrating for practitioner audience",
        writing_sample_titles=["Agroecology Field Manual (12,000 words)", "Soil Restoration Protocols for Zone 5"],
    ),

    # Author B — Tier A, governance and institutional learning, no split (only one eligible domain)
    AuthorIntakeRecord(
        author_id="author_002",
        name="Thomas Rivera",
        email="t.rivera@commonslab.org",
        background_type="practitioner",
        zone5_familiarity="adjacent",
        d2_writing=4,
        d3_markdown=3,
        d4_research=4,
        domain_scores=[
            DomainScores(domain_id=65, d1_domain_knowledge=5, d5_practitioner_grounding=5),
            DomainScores(domain_id=64, d1_domain_knowledge=3, d5_practitioner_grounding=3),
        ],
        hours_per_week_confirmed=6,
        sprint_conflicts=["June 20-22 (family travel)"],
        conflict_in_t7_window=False,
        conflict_in_peer_review_window=False,
        scope_flexibility_preference="confident",
        response_time="within_24h",
        anticipated_challenge="source quality prioritization",
    ),

    # Author C — Tier B, infrastructure interdependencies, D4 < 3 override
    AuthorIntakeRecord(
        author_id="author_003",
        name="Sandra Kowalczyk",
        email="s.kowalczyk@permadesign.net",
        background_type="practitioner",
        zone5_familiarity="direct",
        d2_writing=4,
        d3_markdown=3,
        d4_research=2,  # triggers D4<3 override → cap at Tier B
        domain_scores=[
            DomainScores(domain_id=62, d1_domain_knowledge=4, d5_practitioner_grounding=4),
            DomainScores(domain_id=63, d1_domain_knowledge=3, d5_practitioner_grounding=4),
        ],
        hours_per_week_confirmed=5,
        sprint_conflicts=[],
        conflict_in_t7_window=False,
        conflict_in_peer_review_window=True,  # warning flag
        scope_flexibility_preference="reduce_scope",
        response_time="within_24h",
        anticipated_challenge="citation verification",
    ),

    # Author D — Tier B, international coordination (difficult domain)
    AuthorIntakeRecord(
        author_id="author_004",
        name="Amara Osei",
        email="amara.osei@diasporanet.org",
        background_type="mixed",
        zone5_familiarity="limited",  # note flag
        d2_writing=3,
        d3_markdown=2,
        d4_research=3,
        domain_scores=[
            DomainScores(domain_id=60, d1_domain_knowledge=4, d5_practitioner_grounding=4),
            DomainScores(domain_id=65, d1_domain_knowledge=3, d5_practitioner_grounding=2),  # D5<3 → Tier C only
        ],
        hours_per_week_confirmed=5,
        sprint_conflicts=["June 24-25 (conference)"],
        conflict_in_t7_window=False,
        conflict_in_peer_review_window=True,
        scope_flexibility_preference="extension",
        response_time="within_48h",
        anticipated_challenge="Zone 5 regional calibration",
    ),

    # Author E — Tier C, intergenerational knowledge, limited domain grounding
    AuthorIntakeRecord(
        author_id="author_005",
        name="Kenji Watanabe",
        email="kenji.w@4hnetwork.org",
        background_type="organizer",
        zone5_familiarity="direct",
        d2_writing=3,
        d3_markdown=2,
        d4_research=2,
        domain_scores=[
            DomainScores(domain_id=61, d1_domain_knowledge=3, d5_practitioner_grounding=3),
        ],
        hours_per_week_confirmed=4,
        sprint_conflicts=[],
        conflict_in_t7_window=False,
        conflict_in_peer_review_window=False,
        scope_flexibility_preference="reduce_scope",
        response_time="within_48h",
        anticipated_challenge="research synthesis with limited sources",
    ),

    # Author F — HOLD: D2=1 (cannot write long-form)
    AuthorIntakeRecord(
        author_id="author_006",
        name="Patricia Dunmore",
        email="p.dunmore@ruralext.edu",
        background_type="academic",
        zone5_familiarity="direct",
        d2_writing=1,  # triggers D2=1 override → HOLD
        d3_markdown=2,
        d4_research=4,
        domain_scores=[
            DomainScores(domain_id=63, d1_domain_knowledge=5, d5_practitioner_grounding=4),
        ],
        hours_per_week_confirmed=6,
        sprint_conflicts=[],
        conflict_in_t7_window=False,
        conflict_in_peer_review_window=False,
        scope_flexibility_preference="confident",
        response_time="same_day",
        anticipated_challenge="long-form prose structure",
        additional_notes="Strong domain expert but no practitioner writing experience. Referred for writing support.",
    ),

    # Author G — Tier A, competing with Author A for Domain 63 (conflict resolution test)
    AuthorIntakeRecord(
        author_id="author_007",
        name="Luz Esperanza",
        email="luz.e@agroecology.coop",
        background_type="practitioner",
        zone5_familiarity="adjacent",
        d2_writing=4,
        d3_markdown=4,
        d4_research=4,
        domain_scores=[
            DomainScores(domain_id=63, d1_domain_knowledge=5, d5_practitioner_grounding=4),  # competing for 63
            DomainScores(domain_id=61, d1_domain_knowledge=3, d5_practitioner_grounding=3),
        ],
        hours_per_week_confirmed=8,
        sprint_conflicts=[],
        conflict_in_t7_window=False,
        conflict_in_peer_review_window=False,
        scope_flexibility_preference="confident",
        response_time="same_day",
        anticipated_challenge="peer review feedback",
    ),

    # Author H — batch communicator (warning flag test)
    AuthorIntakeRecord(
        author_id="author_008",
        name="Finn Holbrook",
        email="finn.holbrook@commons.net",
        background_type="academic",
        zone5_familiarity="adjacent",
        d2_writing=4,
        d3_markdown=3,
        d4_research=4,
        domain_scores=[
            DomainScores(domain_id=64, d1_domain_knowledge=4, d5_practitioner_grounding=3),
        ],
        hours_per_week_confirmed=5,
        sprint_conflicts=[],
        conflict_in_t7_window=False,
        conflict_in_peer_review_window=False,
        scope_flexibility_preference="confident",
        response_time="batch_weekly",  # warning flag
        anticipated_challenge="timeline alongside other commitments",
    ),
]


# ---------------------------------------------------------------------------
# CLI entry point
# ---------------------------------------------------------------------------

def load_authors_from_json(path: str) -> list[AuthorIntakeRecord]:
    """Load and validate author intake records from a JSON file.

    Expected JSON format: list of objects matching AuthorIntakeRecord fields.
    domain_scores is a list of objects with domain_id, d1_domain_knowledge, d5_practitioner_grounding.
    """
    with open(path, "r") as fh:
        raw = json.load(fh)

    authors = []
    for i, obj in enumerate(raw):
        try:
            domain_scores = [
                DomainScores(**ds) for ds in obj.get("domain_scores", [])
            ]
            obj_clean = {k: v for k, v in obj.items() if k != "domain_scores"}
            author = AuthorIntakeRecord(**obj_clean, domain_scores=domain_scores)
            authors.append(author)
        except (TypeError, KeyError) as exc:
            print(f"ERROR: Could not parse author record at index {i}: {exc}", file=sys.stderr)
            sys.exit(1)

    return authors


def _dataclass_to_dict(obj):
    """Recursively convert dataclasses and Enums to JSON-serializable types."""
    if hasattr(obj, "__dataclass_fields__"):
        return {k: _dataclass_to_dict(v) for k, v in asdict(obj).items()}
    elif isinstance(obj, Enum):
        return obj.value
    elif isinstance(obj, list):
        return [_dataclass_to_dict(i) for i in obj]
    elif isinstance(obj, tuple):
        return [_dataclass_to_dict(i) for i in obj]
    elif isinstance(obj, dict):
        return {k: _dataclass_to_dict(v) for k, v in obj.items()}
    return obj


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Wave 2 Author-Domain Matching Automation (Systems Resilience Phase 6)"
    )
    parser.add_argument(
        "--input", "-i",
        help="Path to JSON file containing list of author intake records.",
    )
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run with built-in synthetic test data (8 authors, all edge cases).",
    )
    parser.add_argument(
        "--output", "-o",
        help="Path to write JSON output. If omitted, human-readable report goes to stdout.",
    )
    parser.add_argument(
        "--trace",
        action="store_true",
        help="Include full decision trace in stdout output (verbose).",
    )
    args = parser.parse_args()

    if args.demo:
        authors = SAMPLE_AUTHORS
        print(f"Running with {len(authors)} synthetic test authors...\n")
    elif args.input:
        authors = load_authors_from_json(args.input)
        print(f"Loaded {len(authors)} authors from {args.input}\n")
    else:
        parser.print_help()
        sys.exit(0)

    # Process each author
    results: list[AuthorMatchResult] = [process_author(a) for a in authors]

    # Resolve pool-level domain conflicts
    domain_plans = resolve_domain_conflicts(results)

    # Build onboarding sequence
    onboarding_seq = build_onboarding_sequence(results, domain_plans)

    # Assemble and output report
    report = build_report(authors, results, domain_plans, onboarding_seq)

    if args.output:
        report_dict = _dataclass_to_dict(report)
        with open(args.output, "w") as fh:
            json.dump(report_dict, fh, indent=2, default=str)
        print(f"JSON report written to {args.output}")

    print_report(report)

    if args.trace:
        print()
        print("=" * 72)
        print("FULL DECISION TRACES")
        print("=" * 72)
        for result in results:
            for line in result.decision_trace:
                print(line)
            print()


if __name__ == "__main__":
    main()
