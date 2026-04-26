"""
Profile/hardware tier compatibility matrix.

Determines which profiles can run on which hardware tiers.
Source of truth: requirements.md Section 9 (Hardware Tiers) and Section 4 (Profiles).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass
class ProfileCompatibility:
    profile_id: int
    profile_name: str
    min_tier: int
    recommended_tier: int
    min_ram_gb: float
    primary_model: str
    notes: str


# ---------------------------------------------------------------------------
# Compatibility matrix (all 6 profiles)
# ---------------------------------------------------------------------------

COMPATIBILITY_MATRIX: list[ProfileCompatibility] = [
    ProfileCompatibility(
        profile_id=1,
        profile_name="Personal Productivity",
        min_tier=1,
        recommended_tier=1,
        min_ram_gb=8,
        primary_model="qwen2.5:7b-instruct",
        notes="",
    ),
    ProfileCompatibility(
        profile_id=2,
        profile_name="Customer Support",
        min_tier=1,
        recommended_tier=1,
        min_ram_gb=8,
        primary_model="qwen2.5:7b-instruct",
        notes="",
    ),
    ProfileCompatibility(
        profile_id=3,
        profile_name="Sales Outreach",
        min_tier=1,
        recommended_tier=2,
        min_ram_gb=8,
        primary_model="qwen2.5:14b-instruct",
        notes="Uses 7B fallback on Tier 1",
    ),
    ProfileCompatibility(
        profile_id=4,
        profile_name="Developer Assistant",
        min_tier=2,
        recommended_tier=3,
        min_ram_gb=16,
        primary_model="qwen3-coder:30b-a3b",
        notes="MoE model, 3B active params",
    ),
    ProfileCompatibility(
        profile_id=5,
        profile_name="Business Intelligence",
        min_tier=3,
        recommended_tier=3,
        min_ram_gb=32,
        primary_model="deepseek-r1:14b",
        notes="Requires reasoning model",
    ),
    ProfileCompatibility(
        profile_id=6,
        profile_name="Enterprise Orchestrator",
        min_tier=4,
        recommended_tier=4,
        min_ram_gb=64,
        primary_model="qwen3:72b",
        notes="Requires Tier 4 hardware",
    ),
]

# Tier-based fallback model overrides for sub-optimal tier combinations
# Key: (profile_id, tier) → model to use instead of primary_model
_TIER_MODEL_OVERRIDES: dict[tuple[int, int], str] = {
    (3, 1): "qwen2.5:7b-instruct",         # Profile 3 on Tier 1 — 7B fallback
    (4, 2): "deepseek-coder-v2-lite:7b",    # Profile 4 on Tier 2 — 7B coder fallback
}


# ---------------------------------------------------------------------------
# Lookup helpers
# ---------------------------------------------------------------------------


def _get_profile(profile_id: int) -> Optional[ProfileCompatibility]:
    """Return the ProfileCompatibility entry for the given profile_id, or None."""
    for p in COMPATIBILITY_MATRIX:
        if p.profile_id == profile_id:
            return p
    return None


def get_compatible_profiles(tier: int) -> list[ProfileCompatibility]:
    """Return all profiles that can run on the given hardware tier.

    A profile is compatible if ``tier >= profile.min_tier``.
    """
    return [p for p in COMPATIBILITY_MATRIX if tier >= p.min_tier]


def get_compatibility_warnings(tier: int, selected_profile_id: int) -> list[str]:
    """Return warning messages if the selected profile is suboptimal for the tier.

    Possible warnings:
    - Profile requires a higher tier than available (hard incompatibility)
    - Profile can run but is below the recommended tier (degraded performance)
    - RAM borderline relative to profile minimum
    """
    warnings: list[str] = []
    profile = _get_profile(selected_profile_id)

    if profile is None:
        warnings.append(f"Unknown profile ID {selected_profile_id}.")
        return warnings

    if tier < profile.min_tier:
        warnings.append(
            f"Profile {profile.profile_id} ({profile.profile_name}) requires at least "
            f"Tier {profile.min_tier} hardware. Current hardware is Tier {tier}. "
            f"This profile cannot run on this machine."
        )
    elif tier < profile.recommended_tier:
        fallback = _TIER_MODEL_OVERRIDES.get((profile.profile_id, tier))
        fallback_note = f" A lighter model ({fallback}) will be used automatically." if fallback else ""
        warnings.append(
            f"Profile {profile.profile_id} ({profile.profile_name}) runs best on "
            f"Tier {profile.recommended_tier} hardware. Performance may be reduced on Tier {tier}.{fallback_note}"
        )

    if profile.notes:
        warnings.append(f"Note: {profile.notes}")

    return warnings


def select_optimal_model(profile_id: int, tier: int) -> str:
    """Return the best model name for the given profile/tier combination.

    - Uses a tier-specific override if one exists in ``_TIER_MODEL_OVERRIDES``.
    - Falls back to the profile's ``primary_model`` otherwise.
    - Returns an empty string if the profile is unknown.
    """
    profile = _get_profile(profile_id)
    if profile is None:
        return ""

    override = _TIER_MODEL_OVERRIDES.get((profile_id, tier))
    if override:
        return override

    return profile.primary_model
