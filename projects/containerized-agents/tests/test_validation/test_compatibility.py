"""
Tests for agentcore.validation.compatibility

Pure logic tests — no mocking required.
"""
from __future__ import annotations

import pytest

from agentcore.validation.compatibility import (
    COMPATIBILITY_MATRIX,
    ProfileCompatibility,
    get_compatible_profiles,
    get_compatibility_warnings,
    select_optimal_model,
)


# ---------------------------------------------------------------------------
# COMPATIBILITY_MATRIX integrity
# ---------------------------------------------------------------------------


class TestCompatibilityMatrixIntegrity:
    def test_matrix_has_six_profiles(self):
        assert len(COMPATIBILITY_MATRIX) == 6

    def test_profile_ids_are_unique(self):
        ids = [p.profile_id for p in COMPATIBILITY_MATRIX]
        assert len(ids) == len(set(ids))

    def test_profile_ids_are_1_through_6(self):
        ids = sorted(p.profile_id for p in COMPATIBILITY_MATRIX)
        assert ids == [1, 2, 3, 4, 5, 6]

    def test_min_tier_lte_recommended_tier(self):
        for p in COMPATIBILITY_MATRIX:
            assert p.min_tier <= p.recommended_tier, (
                f"Profile {p.profile_id}: min_tier ({p.min_tier}) > recommended_tier ({p.recommended_tier})"
            )

    def test_all_tiers_are_valid(self):
        for p in COMPATIBILITY_MATRIX:
            assert 1 <= p.min_tier <= 4
            assert 1 <= p.recommended_tier <= 4

    def test_profile_1_min_tier_is_1(self):
        p = next(x for x in COMPATIBILITY_MATRIX if x.profile_id == 1)
        assert p.min_tier == 1

    def test_profile_6_min_tier_is_4(self):
        p = next(x for x in COMPATIBILITY_MATRIX if x.profile_id == 6)
        assert p.min_tier == 4

    def test_profile_models_are_non_empty(self):
        for p in COMPATIBILITY_MATRIX:
            assert p.primary_model, f"Profile {p.profile_id} has no primary_model"

    def test_min_ram_positive(self):
        for p in COMPATIBILITY_MATRIX:
            assert p.min_ram_gb > 0


# ---------------------------------------------------------------------------
# get_compatible_profiles
# ---------------------------------------------------------------------------


class TestGetCompatibleProfiles:
    def test_tier1_returns_profiles_1_2_and_3(self):
        # Profile 3 (Sales Outreach) has min_tier=1 with a 7B fallback model,
        # so it is technically compatible with Tier 1 hardware per the requirements.
        profiles = get_compatible_profiles(1)
        ids = {p.profile_id for p in profiles}
        assert {1, 2, 3}.issubset(ids)
        # Profile 4 (min_tier=2) must NOT be present
        assert 4 not in ids

    def test_tier2_returns_profiles_1_to_4(self):
        profiles = get_compatible_profiles(2)
        ids = {p.profile_id for p in profiles}
        assert ids == {1, 2, 3, 4}

    def test_tier3_returns_profiles_1_to_5(self):
        profiles = get_compatible_profiles(3)
        ids = {p.profile_id for p in profiles}
        assert ids == {1, 2, 3, 4, 5}

    def test_tier4_returns_all_6_profiles(self):
        profiles = get_compatible_profiles(4)
        ids = {p.profile_id for p in profiles}
        assert ids == {1, 2, 3, 4, 5, 6}

    def test_all_returned_profiles_are_compatible_objects(self):
        for tier in range(1, 5):
            for p in get_compatible_profiles(tier):
                assert isinstance(p, ProfileCompatibility)

    def test_compatibility_is_cumulative(self):
        """Higher tiers must include all profiles from lower tiers."""
        prev_ids: set[int] = set()
        for tier in range(1, 5):
            current_ids = {p.profile_id for p in get_compatible_profiles(tier)}
            assert prev_ids.issubset(current_ids), (
                f"Tier {tier} is missing profiles that Tier {tier - 1} supported: "
                f"{prev_ids - current_ids}"
            )
            prev_ids = current_ids


# ---------------------------------------------------------------------------
# get_compatibility_warnings
# ---------------------------------------------------------------------------


class TestGetCompatibilityWarnings:
    def test_no_warnings_when_optimal(self):
        """Profile 1 on Tier 1 (recommended) — no warnings."""
        warnings = get_compatibility_warnings(1, 1)
        # May include notes from profile.notes, but must not warn about tier
        tier_warnings = [w for w in warnings if "requires" in w.lower() or "reduced" in w.lower()]
        assert not tier_warnings

    def test_warning_when_below_min_tier(self):
        """Profile 6 (min_tier=4) on Tier 1 should produce a hard incompatibility warning."""
        warnings = get_compatibility_warnings(1, 6)
        assert any("cannot run" in w or "requires" in w for w in warnings)

    def test_warning_when_below_recommended_tier(self):
        """Profile 4 on Tier 2 (below recommended Tier 3) — performance warning."""
        warnings = get_compatibility_warnings(2, 4)
        assert any("reduced" in w.lower() or "best on" in w.lower() for w in warnings)

    def test_no_reduced_warning_at_recommended_tier(self):
        """Profile 4 on Tier 3 (recommended) — no performance reduction warning."""
        warnings = get_compatibility_warnings(3, 4)
        perf_warnings = [w for w in warnings if "reduced" in w.lower()]
        assert not perf_warnings

    def test_unknown_profile_id_returns_warning(self):
        """Invalid profile ID should produce a warning, not crash."""
        warnings = get_compatibility_warnings(2, 99)
        assert warnings
        assert any("unknown" in w.lower() or "99" in w for w in warnings)

    def test_profile_notes_included_in_warnings(self):
        """Profiles with non-empty notes should include them in the warnings list."""
        # Profile 3 has notes: "Uses 7B fallback on Tier 1"
        warnings = get_compatibility_warnings(1, 3)
        notes_warnings = [w for w in warnings if "7B" in w or "fallback" in w.lower()]
        assert notes_warnings

    def test_profile6_tier4_no_incompatibility_warning(self):
        """Profile 6 on Tier 4 (the required tier) must NOT produce a 'cannot run' warning."""
        warnings = get_compatibility_warnings(4, 6)
        hard_warnings = [w for w in warnings if "cannot run" in w]
        assert not hard_warnings


# ---------------------------------------------------------------------------
# select_optimal_model
# ---------------------------------------------------------------------------


class TestSelectOptimalModel:
    def test_profile1_tier1_returns_primary(self):
        model = select_optimal_model(1, 1)
        assert model == "qwen2.5:7b-instruct"

    def test_profile3_tier1_returns_fallback(self):
        """Profile 3 on Tier 1 should use the 7B fallback, not the 14B primary."""
        model = select_optimal_model(3, 1)
        assert "7b" in model.lower()

    def test_profile3_tier2_returns_primary(self):
        """Profile 3 on Tier 2 (recommended) — use the primary 14B model."""
        model = select_optimal_model(3, 2)
        assert "14b" in model.lower()

    def test_profile4_tier2_returns_fallback(self):
        """Profile 4 on Tier 2 (below recommended) — lighter coder model."""
        model = select_optimal_model(4, 2)
        assert model  # non-empty
        # Should NOT be the 30B MoE primary
        assert "30b" not in model.lower()

    def test_profile4_tier3_returns_moe_primary(self):
        model = select_optimal_model(4, 3)
        assert "30b" in model.lower() or "coder" in model.lower()

    def test_profile6_tier4_returns_primary(self):
        model = select_optimal_model(6, 4)
        assert "72b" in model.lower()

    def test_unknown_profile_returns_empty_string(self):
        model = select_optimal_model(99, 2)
        assert model == ""

    def test_all_profiles_tier4_return_non_empty(self):
        """On Tier 4 hardware, every profile should have a model."""
        for profile_id in range(1, 7):
            model = select_optimal_model(profile_id, 4)
            assert model, f"Profile {profile_id} on Tier 4 returned empty model"
