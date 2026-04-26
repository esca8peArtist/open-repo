"""
Tests for agentcore.validation.hardware

Tests mock all subprocess calls and httpx requests so the test suite runs
without real hardware or a running Ollama instance.
"""
from __future__ import annotations

import asyncio
import platform
from statistics import median
from unittest.mock import AsyncMock, MagicMock, patch

import pytest

from agentcore.validation.hardware import (
    BenchmarkResult,
    HardwareInfo,
    _compatible_profiles_for_tier,
    check_gpu_availability,
    detect_hardware,
    get_tier_for_ram,
    run_benchmark,
)


# ---------------------------------------------------------------------------
# get_tier_for_ram — no mocking needed, pure function
# ---------------------------------------------------------------------------


class TestGetTierForRam:
    def test_tier1_low(self):
        assert get_tier_for_ram(4.0) == 1

    def test_tier1_boundary(self):
        # 11.9 is still Tier 1 (< 12)
        assert get_tier_for_ram(11.9) == 1

    def test_tier2_lower_boundary(self):
        assert get_tier_for_ram(12.0) == 2

    def test_tier2_mid(self):
        assert get_tier_for_ram(16.0) == 2

    def test_tier2_upper_boundary(self):
        # 31.9 is Tier 2 (< 32)
        assert get_tier_for_ram(31.9) == 2

    def test_tier3_lower_boundary(self):
        assert get_tier_for_ram(32.0) == 3

    def test_tier3_mid(self):
        assert get_tier_for_ram(64.0) == 3

    def test_tier3_upper_boundary(self):
        # 79.9 is Tier 3 (< 80)
        assert get_tier_for_ram(79.9) == 3

    def test_tier4_lower_boundary(self):
        assert get_tier_for_ram(80.0) == 4

    def test_tier4_high(self):
        assert get_tier_for_ram(128.0) == 4

    def test_zero_ram(self):
        # Unknown RAM defaults to Tier 1
        assert get_tier_for_ram(0.0) == 1


# ---------------------------------------------------------------------------
# _compatible_profiles_for_tier — pure function
# ---------------------------------------------------------------------------


class TestCompatibleProfilesForTier:
    def test_tier1_profiles(self):
        assert _compatible_profiles_for_tier(1) == [1, 2]

    def test_tier2_profiles(self):
        assert _compatible_profiles_for_tier(2) == [1, 2, 3, 4]

    def test_tier3_profiles(self):
        assert _compatible_profiles_for_tier(3) == [1, 2, 3, 4, 5]

    def test_tier4_profiles(self):
        assert _compatible_profiles_for_tier(4) == [1, 2, 3, 4, 5, 6]


# ---------------------------------------------------------------------------
# check_gpu_availability — mocks subprocess
# ---------------------------------------------------------------------------


class TestCheckGpuAvailability:
    @pytest.mark.asyncio
    async def test_no_gpu_nvidia_smi_missing(self):
        """FileNotFoundError from nvidia-smi → type 'none'."""
        with patch("agentcore.validation.hardware.platform") as mock_platform:
            mock_platform.machine.return_value = "x86_64"
            mock_platform.system.return_value = "Linux"

            async def fake_run_in_executor(_executor, fn):
                raise FileNotFoundError("nvidia-smi not found")

            loop = asyncio.get_running_loop()
            with patch.object(loop, "run_in_executor", side_effect=fake_run_in_executor):
                result = await check_gpu_availability()

        assert result["type"] == "none"
        assert result["vram_gb"] == 0.0

    @pytest.mark.asyncio
    async def test_nvidia_detected(self):
        """nvidia-smi returns clean output → type 'nvidia'."""
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = b"8192, 535.86.10, NVIDIA GeForce RTX 4090\n"

        with patch("agentcore.validation.hardware.platform") as mock_platform:
            mock_platform.machine.return_value = "x86_64"
            mock_platform.system.return_value = "Linux"

            async def fake_run_in_executor(_executor, fn):
                return mock_result

            loop = asyncio.get_running_loop()
            with patch.object(loop, "run_in_executor", side_effect=fake_run_in_executor):
                result = await check_gpu_availability()

        assert result["type"] == "nvidia"
        assert result["vram_gb"] == 8.0
        assert "535" in result["driver"]

    @pytest.mark.asyncio
    async def test_apple_silicon_detected(self):
        """arm64 + Darwin → type 'apple'."""
        mock_result = MagicMock()
        mock_result.returncode = 0
        mock_result.stdout = b'{"SPDisplaysDataType": [{"spdisplays_metal": "Metal 3"}]}'

        with patch("agentcore.validation.hardware.platform") as mock_platform:
            mock_platform.machine.return_value = "arm64"
            mock_platform.system.return_value = "Darwin"

            async def fake_run_in_executor(_executor, fn):
                return mock_result

            loop = asyncio.get_running_loop()
            with patch.object(loop, "run_in_executor", side_effect=fake_run_in_executor):
                result = await check_gpu_availability()

        assert result["type"] == "apple"


# ---------------------------------------------------------------------------
# detect_hardware — mocks subprocess + shutil
# ---------------------------------------------------------------------------


class TestDetectHardware:
    @pytest.mark.asyncio
    async def test_linux_16gb_tier2(self):
        """16 GB Linux machine → Tier 2."""
        meminfo = "MemTotal:       16777216 kB\nMemFree: 8000000 kB\n"

        with (
            patch("builtins.open", MagicMock(return_value=MagicMock(
                __enter__=MagicMock(return_value=iter(meminfo.splitlines(keepends=True))),
                __exit__=MagicMock(return_value=False),
            ))),
            patch("agentcore.validation.hardware.platform") as mock_platform,
            patch("agentcore.validation.hardware.shutil") as mock_shutil,
            patch("agentcore.validation.hardware._detect_tpm", return_value=True),
            patch("agentcore.validation.hardware.check_gpu_availability", new_callable=AsyncMock,
                  return_value={"type": "none", "vram_gb": 0.0, "driver": ""}),
        ):
            mock_platform.system.return_value = "Linux"
            mock_platform.machine.return_value = "x86_64"
            mock_platform.processor.return_value = "Intel Core i7"
            mock_shutil.disk_usage.return_value = MagicMock(free=500 * 1024 ** 3)

            with patch("agentcore.validation.hardware._detect_ram", return_value=16.0), \
                 patch("agentcore.validation.hardware._detect_cpu", return_value=(8, "Intel Core i7-12700")):
                info = await detect_hardware()

        assert info.detected_tier == 2
        assert info.ram_gb == 16.0
        assert info.tpm_available is True
        assert info.is_apple_silicon is False

    @pytest.mark.asyncio
    async def test_96gb_tier4(self):
        """96 GB machine → Tier 4."""
        with (
            patch("agentcore.validation.hardware.check_gpu_availability", new_callable=AsyncMock,
                  return_value={"type": "none", "vram_gb": 0.0, "driver": ""}),
            patch("agentcore.validation.hardware._detect_ram", return_value=96.0),
            patch("agentcore.validation.hardware._detect_cpu", return_value=(32, "AMD EPYC")),
            patch("agentcore.validation.hardware._detect_tpm", return_value=False),
            patch("agentcore.validation.hardware.shutil") as mock_shutil,
            patch("agentcore.validation.hardware.platform") as mock_platform,
        ):
            mock_platform.system.return_value = "Linux"
            mock_platform.machine.return_value = "x86_64"
            mock_shutil.disk_usage.return_value = MagicMock(free=1000 * 1024 ** 3)
            info = await detect_hardware()

        assert info.detected_tier == 4
        assert info.ram_gb == 96.0

    @pytest.mark.asyncio
    async def test_8gb_tier1(self):
        """8 GB machine → Tier 1."""
        with (
            patch("agentcore.validation.hardware.check_gpu_availability", new_callable=AsyncMock,
                  return_value={"type": "none", "vram_gb": 0.0, "driver": ""}),
            patch("agentcore.validation.hardware._detect_ram", return_value=8.0),
            patch("agentcore.validation.hardware._detect_cpu", return_value=(4, "Intel Celeron")),
            patch("agentcore.validation.hardware._detect_tpm", return_value=False),
            patch("agentcore.validation.hardware.shutil") as mock_shutil,
            patch("agentcore.validation.hardware.platform") as mock_platform,
        ):
            mock_platform.system.return_value = "Linux"
            mock_platform.machine.return_value = "x86_64"
            mock_shutil.disk_usage.return_value = MagicMock(free=200 * 1024 ** 3)
            info = await detect_hardware()

        assert info.detected_tier == 1

    @pytest.mark.asyncio
    async def test_storage_populated(self):
        """storage_gb should be populated from shutil.disk_usage."""
        with (
            patch("agentcore.validation.hardware.check_gpu_availability", new_callable=AsyncMock,
                  return_value={"type": "none", "vram_gb": 0.0, "driver": ""}),
            patch("agentcore.validation.hardware._detect_ram", return_value=32.0),
            patch("agentcore.validation.hardware._detect_cpu", return_value=(16, "AMD Ryzen")),
            patch("agentcore.validation.hardware._detect_tpm", return_value=False),
            patch("agentcore.validation.hardware.shutil") as mock_shutil,
            patch("agentcore.validation.hardware.platform") as mock_platform,
        ):
            mock_platform.system.return_value = "Linux"
            mock_platform.machine.return_value = "x86_64"
            # 256 GiB free
            mock_shutil.disk_usage.return_value = MagicMock(free=256 * 1024 ** 3)
            info = await detect_hardware()

        assert info.storage_gb == 256.0


# ---------------------------------------------------------------------------
# run_benchmark — mocks httpx
# ---------------------------------------------------------------------------


class TestRunBenchmark:
    @pytest.mark.asyncio
    async def test_no_ollama_returns_zero_tps(self):
        """If Ollama is unreachable, benchmark returns 0 tokens/sec and a warning."""
        import httpx

        with patch("agentcore.validation.hardware._pick_benchmark_model", new_callable=AsyncMock,
                   return_value=None), \
             patch("agentcore.validation.hardware._detect_ram", return_value=16.0):
            result = await run_benchmark(ollama_url="http://ollama:11434")

        assert result.tokens_per_second == 0.0
        assert any("not reachable" in w or "skipped" in w for w in result.warnings)

    @pytest.mark.asyncio
    async def test_successful_benchmark(self):
        """3 successful inference calls → median tokens/sec computed correctly."""
        fake_tps_values = [30.0, 32.0, 31.0]
        fake_latency_values = [800.0, 750.0, 760.0]

        call_count = 0

        async def fake_single_inference(_client, _url, _model):
            nonlocal call_count
            tps = fake_tps_values[call_count % len(fake_tps_values)]
            lat = fake_latency_values[call_count % len(fake_latency_values)]
            call_count += 1
            return tps, lat

        with patch("agentcore.validation.hardware._pick_benchmark_model", new_callable=AsyncMock,
                   return_value="qwen2.5:7b"), \
             patch("agentcore.validation.hardware._single_inference", side_effect=fake_single_inference), \
             patch("agentcore.validation.hardware._detect_ram", return_value=16.0):
            result = await run_benchmark()

        assert result.model_used == "qwen2.5:7b"
        assert result.tokens_per_second == 31.0  # median of [30, 32, 31]
        assert result.detected_tier == 2          # 16 GB → Tier 2
        assert 3 in result.compatible_profiles
        assert 4 in result.compatible_profiles

    @pytest.mark.asyncio
    async def test_benchmark_tier1_warnings(self):
        """Tier 1 hardware emits a warning about limited profile support."""
        async def fake_single_inference(_client, _url, _model):
            return 15.0, 1200.0

        with patch("agentcore.validation.hardware._pick_benchmark_model", new_callable=AsyncMock,
                   return_value="phi4-mini:3b"), \
             patch("agentcore.validation.hardware._single_inference", side_effect=fake_single_inference), \
             patch("agentcore.validation.hardware._detect_ram", return_value=8.0):
            result = await run_benchmark()

        assert result.detected_tier == 1
        assert any("Tier 1" in w for w in result.warnings)
        assert result.compatible_profiles == [1, 2]
