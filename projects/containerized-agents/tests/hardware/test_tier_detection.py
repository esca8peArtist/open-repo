"""
Hardware tests: RAM → tier mapping edge cases and boundary conditions.
"""
from __future__ import annotations

from unittest.mock import patch

import pytest


def _ram_to_tier(ram_gb: float) -> int:
    """Replicate the tier detection logic used by the wizard."""
    if ram_gb < 12:
        return 1
    elif ram_gb < 24:
        return 2
    elif ram_gb < 48:
        return 3
    else:
        return 4


class TestRamToTierMapping:
    """Hardware tier detection edge cases (< 12 GB boundary = Tier 1, etc.)."""

    def test_8gb_is_tier_1(self):
        assert _ram_to_tier(8.0) == 1

    def test_11_9gb_is_tier_1(self):
        """11.9 GB (just below 12) must be Tier 1."""
        assert _ram_to_tier(11.9) == 1

    def test_12gb_is_tier_2(self):
        """Exactly 12 GB is the Tier 2 boundary."""
        assert _ram_to_tier(12.0) == 2

    def test_12_1gb_is_tier_2(self):
        """12.1 GB (just above 12) must be Tier 2."""
        assert _ram_to_tier(12.1) == 2

    def test_16gb_is_tier_2(self):
        assert _ram_to_tier(16.0) == 2

    def test_23_9gb_is_tier_2(self):
        """23.9 GB (just below 24) must be Tier 2."""
        assert _ram_to_tier(23.9) == 2

    def test_24gb_is_tier_3(self):
        """Exactly 24 GB is the Tier 3 boundary."""
        assert _ram_to_tier(24.0) == 3

    def test_32gb_is_tier_3(self):
        assert _ram_to_tier(32.0) == 3

    def test_47_9gb_is_tier_3(self):
        """47.9 GB (just below 48) must be Tier 3."""
        assert _ram_to_tier(47.9) == 3

    def test_48gb_is_tier_4(self):
        """Exactly 48 GB is the Tier 4 boundary."""
        assert _ram_to_tier(48.0) == 4

    def test_64gb_is_tier_4(self):
        assert _ram_to_tier(64.0) == 4

    def test_128gb_is_tier_4(self):
        assert _ram_to_tier(128.0) == 4

    def test_0gb_is_tier_1(self):
        """Zero RAM (error case) must default to Tier 1."""
        assert _ram_to_tier(0.0) == 1


class TestHardwareSettingsTierConfig:
    """Settings hardware_tier field tests."""

    def test_default_hardware_tier_is_1(self):
        """Default hardware_tier must be 1."""
        from agentcore.config import Settings
        s = Settings(
            ollama_base_url="http://localhost:11434",
            api_secret_key="test-key-that-is-long-enough-here",
        )
        assert s.hardware_tier == 1

    def test_hardware_tier_2(self):
        from agentcore.config import Settings
        s = Settings(
            ollama_base_url="http://localhost:11434",
            api_secret_key="test-key-that-is-long-enough-here",
            hardware_tier=2,
        )
        assert s.hardware_tier == 2

    def test_hardware_tier_3(self):
        from agentcore.config import Settings
        s = Settings(
            ollama_base_url="http://localhost:11434",
            api_secret_key="test-key-that-is-long-enough-here",
            hardware_tier=3,
        )
        assert s.hardware_tier == 3

    def test_hardware_tier_4(self):
        from agentcore.config import Settings
        s = Settings(
            ollama_base_url="http://localhost:11434",
            api_secret_key="test-key-that-is-long-enough-here",
            hardware_tier=4,
        )
        assert s.hardware_tier == 4
