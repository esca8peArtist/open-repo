"""
Hardware detection and benchmarking.

Used by: setup wizard step 9, dashboard resources page, agentcore startup.
"""
from __future__ import annotations

import asyncio
import logging
import platform
import shutil
import subprocess
import time
from dataclasses import dataclass, field
from pathlib import Path
from statistics import median
from typing import Optional

import httpx

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Data classes
# ---------------------------------------------------------------------------


@dataclass
class HardwareInfo:
    ram_gb: float
    vram_gb: float           # 0 if no GPU
    cpu_cores: int
    cpu_model: str
    gpu_model: str           # "" if no GPU
    is_apple_silicon: bool
    tpm_available: bool
    storage_gb: float        # free space on /
    detected_tier: int       # 1-4 based on RAM


@dataclass
class BenchmarkResult:
    tokens_per_second: float
    model_used: str
    ram_used_gb: float
    inference_latency_ms: float
    detected_tier: int
    compatible_profiles: list[int]   # profile numbers that can run on this hardware
    warnings: list[str]              # e.g. "RAM borderline for Profile 4"


# ---------------------------------------------------------------------------
# Tier mapping
# ---------------------------------------------------------------------------


def get_tier_for_ram(ram_gb: float) -> int:
    """Map RAM to hardware tier per requirements Section 9.

    Tier 1 — Entry  (<12 GB)    : Profiles 1, 2
    Tier 2 — Mid    (12–32 GB)  : Profiles 1–4
    Tier 3 — Pro    (32–80 GB)  : Profiles 4, 5
    Tier 4 — Ent    (80 GB+)    : Profile 6
    """
    if ram_gb < 12:
        return 1
    if ram_gb < 32:
        return 2
    if ram_gb < 80:
        return 3
    return 4


# ---------------------------------------------------------------------------
# GPU detection helpers
# ---------------------------------------------------------------------------


async def check_gpu_availability() -> dict:
    """Check GPU/accelerator availability.

    Returns a dict with keys:
        type:     "nvidia" | "apple" | "none"
        vram_gb:  float (0 if not applicable)
        driver:   str (driver/Metal version, or "")
    """
    # -- Apple Silicon check (cheap, synchronous) ---------------------------
    if platform.machine() == "arm64" and platform.system() == "Darwin":
        # Apple Silicon: unified memory — VRAM == system RAM via Metal
        try:
            result = await asyncio.get_running_loop().run_in_executor(
                None,
                lambda: subprocess.run(
                    ["system_profiler", "SPDisplaysDataType", "-json"],
                    capture_output=True,
                    timeout=10,
                ),
            )
            metal_version = ""
            if result.returncode == 0:
                import json
                try:
                    data = json.loads(result.stdout)
                    displays = data.get("SPDisplaysDataType", [])
                    if displays:
                        metal_version = displays[0].get("spdisplays_metal", "")
                except Exception:
                    pass
            return {"type": "apple", "vram_gb": 0.0, "driver": metal_version}
        except Exception as exc:
            logger.debug("Apple GPU check error: %s", exc)
            return {"type": "apple", "vram_gb": 0.0, "driver": ""}

    # -- NVIDIA via nvidia-smi -----------------------------------------------
    try:
        result = await asyncio.get_running_loop().run_in_executor(
            None,
            lambda: subprocess.run(
                [
                    "nvidia-smi",
                    "--query-gpu=memory.total,driver_version,gpu_name",
                    "--format=csv,noheader,nounits",
                ],
                capture_output=True,
                timeout=10,
            ),
        )
        if result.returncode == 0:
            lines = result.stdout.decode().strip().splitlines()
            if lines:
                parts = [p.strip() for p in lines[0].split(",")]
                vram_mib = float(parts[0]) if parts[0].isdigit() or parts[0].replace(".", "").isdigit() else 0.0
                driver = parts[1] if len(parts) > 1 else ""
                return {
                    "type": "nvidia",
                    "vram_gb": round(vram_mib / 1024, 1),
                    "driver": driver,
                }
    except FileNotFoundError:
        pass  # nvidia-smi not installed — expected on non-NVIDIA systems
    except Exception as exc:
        logger.debug("NVIDIA GPU check error: %s", exc)

    return {"type": "none", "vram_gb": 0.0, "driver": ""}


# ---------------------------------------------------------------------------
# RAM detection helpers
# ---------------------------------------------------------------------------


def _read_ram_linux() -> float:
    """Read total RAM from /proc/meminfo (Linux)."""
    try:
        with open("/proc/meminfo") as f:
            for line in f:
                if line.startswith("MemTotal:"):
                    kb = int(line.split()[1])
                    return round(kb / 1_048_576, 1)
    except Exception:
        pass
    return 0.0


def _read_ram_macos() -> float:
    """Read total RAM via sysctl hw.memsize (macOS)."""
    try:
        result = subprocess.run(
            ["sysctl", "-n", "hw.memsize"],
            capture_output=True,
            timeout=5,
        )
        if result.returncode == 0:
            bytes_total = int(result.stdout.decode().strip())
            return round(bytes_total / (1024 ** 3), 1)
    except Exception:
        pass
    return 0.0


def _detect_ram() -> float:
    if platform.system() == "Darwin":
        return _read_ram_macos()
    return _read_ram_linux()


# ---------------------------------------------------------------------------
# CPU detection helpers
# ---------------------------------------------------------------------------


def _detect_cpu() -> tuple[int, str]:
    """Return (core_count, cpu_model_string)."""
    cores = 1
    model = ""

    system = platform.system()

    if system == "Linux":
        try:
            with open("/proc/cpuinfo") as f:
                content = f.read()
            for line in content.splitlines():
                if line.startswith("model name") and not model:
                    model = line.split(":", 1)[1].strip()
            cores = content.count("processor\t:")
        except Exception:
            pass
    elif system == "Darwin":
        try:
            result = subprocess.run(
                ["sysctl", "-n", "machdep.cpu.brand_string"],
                capture_output=True,
                timeout=5,
            )
            if result.returncode == 0:
                model = result.stdout.decode().strip()
            result2 = subprocess.run(
                ["sysctl", "-n", "hw.logicalcpu"],
                capture_output=True,
                timeout=5,
            )
            if result2.returncode == 0:
                cores = int(result2.stdout.decode().strip())
        except Exception:
            pass

    if not model:
        model = platform.processor() or "Unknown"
    if cores < 1:
        try:
            import os
            cores = os.cpu_count() or 1
        except Exception:
            cores = 1

    return cores, model


# ---------------------------------------------------------------------------
# TPM detection
# ---------------------------------------------------------------------------


def _detect_tpm() -> bool:
    """Check for TPM 2.0 device nodes on Linux, or Secure Enclave on macOS."""
    if platform.system() == "Linux":
        return Path("/dev/tpm0").exists() or Path("/dev/tpmrm0").exists()
    if platform.system() == "Darwin":
        # Apple Silicon has Secure Enclave — treat as equivalent
        return platform.machine() == "arm64"
    return False


# ---------------------------------------------------------------------------
# Main detection entry point
# ---------------------------------------------------------------------------


async def detect_hardware() -> HardwareInfo:
    """Detect hardware specifications of the current machine.

    Detection logic:
    - RAM: /proc/meminfo (Linux) or ``sysctl hw.memsize`` (macOS)
    - VRAM: nvidia-smi (NVIDIA) or system_profiler (Apple Silicon unified memory)
    - CPU: /proc/cpuinfo or sysctl
    - TPM: check /dev/tpm0 or /dev/tpmrm0 existence (or Apple Secure Enclave)
    - Storage: shutil.disk_usage("/")
    - Tier: mapped from RAM per Section 9 thresholds
    """
    # Run GPU check concurrently with synchronous detections
    gpu_task = asyncio.create_task(check_gpu_availability())

    ram_gb = _detect_ram()
    cpu_cores, cpu_model = _detect_cpu()
    tpm_available = _detect_tpm()

    try:
        usage = shutil.disk_usage("/")
        storage_gb = round(usage.free / (1024 ** 3), 1)
    except Exception:
        storage_gb = 0.0

    gpu_info = await gpu_task
    is_apple_silicon = gpu_info["type"] == "apple"
    vram_gb = gpu_info["vram_gb"]

    # For Apple Silicon, VRAM is shared with system RAM — report it separately
    # as 0 (not double-counting) since unified memory is already in ram_gb.
    gpu_model = ""
    if gpu_info["type"] == "nvidia":
        # Pull GPU name from nvidia-smi
        try:
            result = await asyncio.get_running_loop().run_in_executor(
                None,
                lambda: subprocess.run(
                    ["nvidia-smi", "--query-gpu=gpu_name", "--format=csv,noheader"],
                    capture_output=True,
                    timeout=10,
                ),
            )
            if result.returncode == 0:
                gpu_model = result.stdout.decode().strip().splitlines()[0]
        except Exception:
            gpu_model = "NVIDIA GPU"
    elif is_apple_silicon:
        # Use sysctl to get chip name
        try:
            result = await asyncio.get_running_loop().run_in_executor(
                None,
                lambda: subprocess.run(
                    ["sysctl", "-n", "machdep.cpu.brand_string"],
                    capture_output=True,
                    timeout=5,
                ),
            )
            if result.returncode == 0:
                gpu_model = result.stdout.decode().strip()  # e.g. "Apple M4 Pro"
        except Exception:
            gpu_model = "Apple Silicon GPU"

    tier = get_tier_for_ram(ram_gb)

    return HardwareInfo(
        ram_gb=ram_gb,
        vram_gb=vram_gb,
        cpu_cores=cpu_cores,
        cpu_model=cpu_model,
        gpu_model=gpu_model,
        is_apple_silicon=is_apple_silicon,
        tpm_available=tpm_available,
        storage_gb=storage_gb,
        detected_tier=tier,
    )


# ---------------------------------------------------------------------------
# Benchmark
# ---------------------------------------------------------------------------

_FALLBACK_MODEL = "qwen2.5:7b"
_BENCHMARK_PROMPT = "Explain briefly what a transformer neural network is."
_BENCHMARK_PREDICT_TOKENS = 30
_BENCHMARK_ITERATIONS = 3


async def _single_inference(
    client: httpx.AsyncClient,
    ollama_url: str,
    model: str,
) -> tuple[float, float]:
    """Run one inference pass.

    Returns (tokens_per_second, latency_ms).
    Raises on HTTP error or timeout.
    """
    payload = {
        "model": model,
        "prompt": _BENCHMARK_PROMPT,
        "stream": False,
        "options": {"num_predict": _BENCHMARK_PREDICT_TOKENS},
    }
    t0 = time.monotonic()
    resp = await client.post(f"{ollama_url}/api/generate", json=payload, timeout=120.0)
    elapsed = time.monotonic() - t0
    resp.raise_for_status()

    data = resp.json()
    eval_count: int = data.get("eval_count", 0)
    latency_ms = elapsed * 1000.0

    if elapsed > 0 and eval_count > 0:
        tps = round(eval_count / elapsed, 2)
    else:
        tps = 0.0

    return tps, round(latency_ms, 1)


async def _pick_benchmark_model(ollama_url: str) -> Optional[str]:
    """Return the name of the best (smallest available) model for benchmarking."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            resp = await client.get(f"{ollama_url}/api/tags")
            if resp.status_code != 200:
                return None
            models = resp.json().get("models", [])
            if not models:
                return None

        # Preference order for fast benchmarks: smaller models first
        preference = ["phi4-mini", "phi", "qwen2.5:7b", "llama3.2:1b", "llama3.2:3b"]
        names = [m.get("name", "") for m in models]

        for pref in preference:
            for name in names:
                if pref in name:
                    return name

        # Fall back to whichever model is first in the list
        return names[0]
    except Exception as exc:
        logger.warning("Could not fetch model list from Ollama: %s", exc)
        return None


def _build_warnings(ram_gb: float, tier: int) -> list[str]:
    """Generate advisory warnings based on detected tier/RAM."""
    warnings: list[str] = []

    # Borderline thresholds
    if 11 <= ram_gb < 12:
        warnings.append(f"RAM ({ram_gb} GB) is borderline for Tier 1 — consider 16 GB for stability.")
    if 15 <= ram_gb < 16:
        warnings.append(f"RAM ({ram_gb} GB) is borderline for Tier 2 — some Profile 3/4 models may swap.")
    if 30 <= ram_gb < 32:
        warnings.append(f"RAM ({ram_gb} GB) is borderline for Tier 3 — Profile 5 may be slow.")
    if 78 <= ram_gb < 80:
        warnings.append(f"RAM ({ram_gb} GB) is borderline for Tier 4 — Profile 6 concurrent workloads may swap.")

    if tier == 1:
        warnings.append("Tier 1 hardware: only Profiles 1 and 2 are fully supported.")
    elif tier == 2:
        warnings.append("Tier 2 hardware: Profiles 3 and 4 use lighter fallback models.")

    return warnings


def _compatible_profiles_for_tier(tier: int) -> list[int]:
    """Return list of profile IDs that can run on the given tier."""
    # Derived from requirements Section 9 and compatibility matrix
    matrix = {1: [1, 2], 2: [1, 2, 3, 4], 3: [1, 2, 3, 4, 5], 4: [1, 2, 3, 4, 5, 6]}
    return matrix.get(tier, [1, 2])


async def run_benchmark(ollama_url: str = "http://ollama:11434") -> BenchmarkResult:
    """Run a quick LLM inference benchmark against a running Ollama instance.

    Strategy:
    1. Query /api/tags for loaded models; pick smallest (fastest) for the test.
    2. Fall back to ``qwen2.5:7b`` if no model is available.
    3. Run 3 inference iterations and take the median tokens/second.
    4. Also record cold-start latency (first iteration is warmup).
    5. Map results to hardware tier and compatible profiles.
    """
    ram_gb = _detect_ram()
    tier = get_tier_for_ram(ram_gb)

    model = await _pick_benchmark_model(ollama_url)
    if not model:
        logger.warning("No Ollama model available for benchmark — using placeholder.")
        return BenchmarkResult(
            tokens_per_second=0.0,
            model_used=_FALLBACK_MODEL,
            ram_used_gb=ram_gb,
            inference_latency_ms=0.0,
            detected_tier=tier,
            compatible_profiles=_compatible_profiles_for_tier(tier),
            warnings=["Ollama not reachable — benchmark skipped."] + _build_warnings(ram_gb, tier),
        )

    tps_samples: list[float] = []
    latency_samples: list[float] = []

    async with httpx.AsyncClient() as client:
        for i in range(_BENCHMARK_ITERATIONS):
            try:
                tps, lat = await _single_inference(client, ollama_url, model)
                tps_samples.append(tps)
                latency_samples.append(lat)
                logger.debug("Benchmark iteration %d: %.1f tok/s, %.0f ms", i + 1, tps, lat)
            except Exception as exc:
                logger.warning("Benchmark iteration %d failed: %s", i + 1, exc)

    if not tps_samples:
        return BenchmarkResult(
            tokens_per_second=0.0,
            model_used=model,
            ram_used_gb=ram_gb,
            inference_latency_ms=0.0,
            detected_tier=tier,
            compatible_profiles=_compatible_profiles_for_tier(tier),
            warnings=["All benchmark iterations failed."] + _build_warnings(ram_gb, tier),
        )

    median_tps = round(median(tps_samples), 2)
    # Latency: use the non-first-iteration median (first = cold start)
    warmup_latency = latency_samples[0]
    steady_latency = round(median(latency_samples[1:] or latency_samples), 1)

    warnings = _build_warnings(ram_gb, tier)
    if warmup_latency > 10_000:
        warnings.append(f"Cold-start latency is high ({warmup_latency:.0f} ms) — model may not be pre-loaded.")

    return BenchmarkResult(
        tokens_per_second=median_tps,
        model_used=model,
        ram_used_gb=ram_gb,
        inference_latency_ms=steady_latency,
        detected_tier=tier,
        compatible_profiles=_compatible_profiles_for_tier(tier),
        warnings=warnings,
    )
