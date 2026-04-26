"""
Wizard tests: hardware benchmark (step 9) — mock Ollama, test benchmark result
and tier detection logic.
"""
from __future__ import annotations

from pathlib import Path
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from wizard.steps.step9_hardware import (
    _detect_ram_gb,
    _ram_to_tier,
    benchmark_hardware,
)


class TestRamToTier:
    """_ram_to_tier boundary condition tests."""

    def test_below_16gb_is_tier1(self):
        assert _ram_to_tier(8.0) == 1

    def test_exactly_16gb_is_tier2(self):
        assert _ram_to_tier(16.0) == 2

    def test_just_below_16gb_is_tier1(self):
        assert _ram_to_tier(15.9) == 1

    def test_just_above_16gb_is_tier2(self):
        assert _ram_to_tier(16.1) == 2

    def test_exactly_24gb_is_tier3(self):
        assert _ram_to_tier(24.0) == 3

    def test_just_below_24gb_is_tier2(self):
        assert _ram_to_tier(23.9) == 2

    def test_exactly_64gb_is_tier4(self):
        assert _ram_to_tier(64.0) == 4

    def test_just_below_64gb_is_tier3(self):
        assert _ram_to_tier(63.9) == 3

    def test_128gb_is_tier4(self):
        assert _ram_to_tier(128.0) == 4

    def test_zero_ram_is_tier1(self):
        """Unknown RAM (0.0 from failed detection) must be tier 1."""
        assert _ram_to_tier(0.0) == 1


class TestDetectRamGb:
    """_detect_ram_gb tests with mocked /proc/meminfo."""

    def test_reads_meminfo_correctly(self, tmp_path):
        """_detect_ram_gb must correctly parse /proc/meminfo MemTotal."""
        fake_meminfo = "MemTotal:       33554432 kB\nMemFree:        16777216 kB\n"
        meminfo_path = tmp_path / "meminfo"
        meminfo_path.write_text(fake_meminfo)

        with patch("builtins.open", return_value=open(meminfo_path)):
            ram = _detect_ram_gb()

        # 33554432 kB = 32 GB (33554432 / 1048576 = 32.0)
        assert ram == pytest.approx(32.0, abs=0.1)

    def test_meminfo_not_found_returns_zero(self):
        """If /proc/meminfo cannot be read, must return 0.0."""
        with patch("builtins.open", side_effect=OSError("No such file")):
            ram = _detect_ram_gb()
        assert ram == 0.0


class TestBenchmarkHardware:
    """benchmark_hardware() integration tests with mocked Ollama."""

    @pytest.mark.asyncio
    async def test_benchmark_with_ollama_available(self, tmp_path):
        """When Ollama is available, benchmark must return tokens_per_second > 0."""
        # Mock /api/tags returning a model list
        tags_response = MagicMock()
        tags_response.status_code = 200
        tags_response.json.return_value = {"models": [{"name": "phi4-mini:latest"}]}

        # Mock /api/generate returning inference stats
        generate_response = MagicMock()
        generate_response.status_code = 200
        generate_response.json.return_value = {
            "eval_count": 20,
            "eval_duration": 1000000000,  # 1 second in nanoseconds (unused)
        }

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(return_value=tags_response)
        mock_client.post = AsyncMock(return_value=generate_response)

        with (
            patch("wizard.steps.step9_hardware._detect_ram_gb", return_value=32.0),
            patch("wizard.state.STATE_FILE", tmp_path / "state.json"),
            patch("wizard.state._state", None),
            patch("httpx.AsyncClient", return_value=mock_client),
            patch("time.monotonic", side_effect=[0.0, 0.5]),  # 0.5s elapsed
        ):
            result = await benchmark_hardware()

        assert result["tier"] == 3  # 32GB → tier 3
        assert result["ram_gb"] == 32.0
        assert result["benchmark_model"] == "phi4-mini:latest"
        assert result["tokens_per_second"] > 0

    @pytest.mark.asyncio
    async def test_benchmark_without_ollama(self, tmp_path):
        """When Ollama is offline, benchmark must still return tier info."""
        import httpx

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(side_effect=httpx.ConnectError("refused"))

        with (
            patch("wizard.steps.step9_hardware._detect_ram_gb", return_value=16.0),
            patch("wizard.state.STATE_FILE", tmp_path / "state.json"),
            patch("wizard.state._state", None),
            patch("httpx.AsyncClient", return_value=mock_client),
        ):
            result = await benchmark_hardware()

        assert result["tier"] == 2  # 16GB → tier 2
        assert result["tokens_per_second"] == 0.0
        assert result["benchmark_model"] == "none"

    @pytest.mark.asyncio
    async def test_benchmark_no_models_available(self, tmp_path):
        """When Ollama has no models, benchmark_model must be 'none'."""
        tags_response = MagicMock()
        tags_response.status_code = 200
        tags_response.json.return_value = {"models": []}

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(return_value=tags_response)

        with (
            patch("wizard.steps.step9_hardware._detect_ram_gb", return_value=8.0),
            patch("wizard.state.STATE_FILE", tmp_path / "state.json"),
            patch("wizard.state._state", None),
            patch("httpx.AsyncClient", return_value=mock_client),
        ):
            result = await benchmark_hardware()

        assert result["benchmark_model"] == "none"
        assert result["tokens_per_second"] == 0.0

    @pytest.mark.asyncio
    async def test_benchmark_compatible_profile_1(self, tmp_path):
        """Profile 1 (8 GB min) on a 16 GB machine must be compatible."""
        state_file = tmp_path / "state.json"

        import httpx

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(side_effect=httpx.ConnectError("offline"))

        with (
            patch("wizard.steps.step9_hardware._detect_ram_gb", return_value=16.0),
            patch("wizard.state.STATE_FILE", state_file),
            patch("wizard.state._state", None),
            patch("httpx.AsyncClient", return_value=mock_client),
        ):
            # Default state has selected_profile=None → defaults to 1
            result = await benchmark_hardware()

        assert result["compatible"] is True

    @pytest.mark.asyncio
    async def test_benchmark_incompatible_profile_4(self, tmp_path):
        """Profile 4 (24 GB min) on an 8 GB machine must flag incompatible."""
        from wizard.state import WizardState, save_state, get_state
        import wizard.state as ws

        state_file = tmp_path / "state.json"
        ws._state = None

        import httpx

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(side_effect=httpx.ConnectError("offline"))

        with (
            patch("wizard.steps.step9_hardware._detect_ram_gb", return_value=8.0),
            patch("wizard.state.STATE_FILE", state_file),
            patch("httpx.AsyncClient", return_value=mock_client),
        ):
            ws._state = None
            state = get_state()
            state.selected_profile = 4
            save_state(state)
            result = await benchmark_hardware()

        # Profile 4 requires 24 GB min, machine has 8 GB → incompatible
        assert result["compatible"] is False

    @pytest.mark.asyncio
    async def test_benchmark_result_structure(self, tmp_path):
        """benchmark_hardware() must always return all expected keys."""
        import httpx

        mock_client = AsyncMock()
        mock_client.__aenter__ = AsyncMock(return_value=mock_client)
        mock_client.__aexit__ = AsyncMock(return_value=False)
        mock_client.get = AsyncMock(side_effect=httpx.ConnectError("offline"))

        with (
            patch("wizard.steps.step9_hardware._detect_ram_gb", return_value=0.0),
            patch("wizard.state.STATE_FILE", tmp_path / "state.json"),
            patch("wizard.state._state", None),
            patch("httpx.AsyncClient", return_value=mock_client),
        ):
            result = await benchmark_hardware()

        required_keys = {"ram_gb", "tier", "tokens_per_second", "benchmark_model", "compatible", "min_ram_required"}
        assert required_keys.issubset(result.keys())
