"""
agentcore.validation — Hardware detection, health checks, and compatibility.

Used by:
  - Setup wizard step 9 (hardware benchmark)
  - Setup wizard step 11 (health checks)
  - Dashboard resources page
  - AgentCore startup
  - /api/validation/* endpoints

Sub-modules are imported lazily here to avoid pulling in heavy dependencies
(httpx, redis) when only a lightweight sub-module is needed.
"""

# Expose the public API but defer the actual imports so that importing
# ``agentcore.validation.compatibility`` alone does not force httpx/redis
# to be installed in test environments that only test pure-logic modules.

__all__ = [
    # hardware
    "HardwareInfo",
    "BenchmarkResult",
    "detect_hardware",
    "run_benchmark",
    "check_gpu_availability",
    "get_tier_for_ram",
    # health
    "HealthStatus",
    "ServiceHealth",
    "SystemHealth",
    "run_all_health_checks",
    "check_internet_connectivity",
    # compatibility
    "ProfileCompatibility",
    "COMPATIBILITY_MATRIX",
    "get_compatible_profiles",
    "get_compatibility_warnings",
    "select_optimal_model",
]


def __getattr__(name: str):
    """Lazy attribute access — imports the right sub-module on first use."""
    _hardware = {
        "HardwareInfo", "BenchmarkResult", "detect_hardware",
        "run_benchmark", "check_gpu_availability", "get_tier_for_ram",
    }
    _health = {
        "HealthStatus", "ServiceHealth", "SystemHealth",
        "run_all_health_checks", "check_internet_connectivity",
    }
    _compat = {
        "ProfileCompatibility", "COMPATIBILITY_MATRIX",
        "get_compatible_profiles", "get_compatibility_warnings", "select_optimal_model",
    }

    if name in _hardware:
        from agentcore.validation import hardware as _hw
        return getattr(_hw, name)
    if name in _health:
        from agentcore.validation import health as _hl
        return getattr(_hl, name)
    if name in _compat:
        from agentcore.validation import compatibility as _co
        return getattr(_co, name)

    raise AttributeError(f"module 'agentcore.validation' has no attribute {name!r}")
