"""
License manager — loaded at AgentCore startup.
Validates license on every boot for Docker Compose SKU.
For OS image SKU, defers to TPM binding (hardware_binding.binding).
"""
import logging
import os
from enum import Enum
from pathlib import Path

logger = logging.getLogger(__name__)

# Path where the signing key is stored on-device.
# For Docker Compose SKU this is injected via environment variable at container start.
# The key must match the one used at license generation time.
_ENV_SIGNING_KEY = "LICENSE_SIGNING_KEY"

# Default license file location (can be overridden via env var for testing)
_DEFAULT_LICENSE_PATH = "/etc/agentcore/license.key"


class LicenseType(Enum):
    TPM_BOUND = "tpm"           # OS image SKU
    KEY_BOUND = "key"           # Docker Compose SKU
    UNLICENSED = "unlicensed"   # First boot, not yet activated


class LicenseStatus(Enum):
    VALID = "valid"
    INVALID = "invalid"
    EXPIRED = "expired"
    HARDWARE_MISMATCH = "mismatch"
    NOT_FOUND = "not_found"


class LicenseError(Exception):
    """Raised when license validation fails and the system must not continue."""


class LicenseManager:
    """On-device license validation for AgentCore.

    At startup, call require_valid() to gate execution on a valid license.
    For TPM-bound (OS image) SKUs the TPM binding is checked; for Docker
    Compose SKUs the offline key file is validated against this machine's
    hardware fingerprint.
    """

    def __init__(self, license_path: str = _DEFAULT_LICENSE_PATH) -> None:
        self._license_path = Path(
            os.environ.get("AGENTCORE_LICENSE_PATH", license_path)
        )
        self._cached_status: tuple[LicenseStatus, str] | None = None
        self._cached_tier: int | None = None

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def detect_license_type(self) -> LicenseType:
        """Check if TPM available → TPM_BOUND; else check for license.key → KEY_BOUND."""
        if self._tpm_available():
            logger.debug("TPM detected — OS image SKU")
            return LicenseType.TPM_BOUND

        if self._license_path.exists():
            logger.debug("License file found at %s — Docker Compose SKU", self._license_path)
            return LicenseType.KEY_BOUND

        logger.debug("No TPM and no license file — UNLICENSED state")
        return LicenseType.UNLICENSED

    def validate(self) -> tuple[LicenseStatus, str]:
        """Validate license. Returns (status, reason_string).

        Results are cached for the lifetime of this LicenseManager instance
        so that repeated calls (e.g. health-check endpoints) are cheap.
        """
        if self._cached_status is not None:
            return self._cached_status

        license_type = self.detect_license_type()

        if license_type == LicenseType.TPM_BOUND:
            status, reason = self._validate_tpm()
        elif license_type == LicenseType.KEY_BOUND:
            status, reason = self._validate_key()
        else:
            status = LicenseStatus.NOT_FOUND
            reason = (
                "No license found. "
                "For Docker Compose SKU: place your license.key at "
                f"{self._license_path} or set AGENTCORE_LICENSE_PATH."
            )

        self._cached_status = (status, reason)
        return status, reason

    def get_tier(self) -> int:
        """Return licensed hardware tier (1–4). Returns 1 if unknown."""
        if self._cached_tier is not None:
            return self._cached_tier

        status, _ = self.validate()
        if status != LicenseStatus.VALID:
            return 1

        # Tier was populated by _validate_key / _validate_tpm during validate()
        return self._cached_tier or 1

    def require_valid(self) -> None:
        """Called at startup. Raises LicenseError if invalid. Logs clear error message."""
        status, reason = self.validate()
        if status == LicenseStatus.VALID:
            logger.info("License check PASSED (tier %s)", self._cached_tier)
            return

        message = self._user_facing_error(status, reason)
        logger.error("License check FAILED: [%s] %s", status.value, reason)
        logger.error(message)
        raise LicenseError(message)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------

    @staticmethod
    def _tpm_available() -> bool:
        """Return True if a TPM 2.0 device is present and accessible."""
        # Standard Linux TPM device nodes
        tpm_devices = [Path("/dev/tpm0"), Path("/dev/tpmrm0")]
        return any(p.exists() for p in tpm_devices)

    def _validate_tpm(self) -> tuple[LicenseStatus, str]:
        """Delegate to the hardware_binding module for TPM validation."""
        try:
            from security.hardware_binding.binding import validate_tpm_binding  # type: ignore
            ok, reason = validate_tpm_binding()
            if ok:
                self._cached_tier = self._read_tier_from_tpm()
                return LicenseStatus.VALID, reason
            return LicenseStatus.HARDWARE_MISMATCH, reason
        except ImportError:
            logger.warning("hardware_binding.binding not available; falling back to key validation")
            return self._validate_key()
        except Exception as exc:
            logger.exception("TPM validation raised an unexpected error")
            return LicenseStatus.INVALID, f"TPM validation error: {exc}"

    def _validate_key(self) -> tuple[LicenseStatus, str]:
        """Validate the offline license key file against this machine's hardware."""
        # Load the license file
        try:
            from security.hardware_binding.fallback_license import (  # type: ignore
                load_license_from_file,
                validate_license,
            )
        except ImportError as exc:
            return LicenseStatus.INVALID, f"License module import error: {exc}"

        license_b64 = load_license_from_file(str(self._license_path))
        if not license_b64:
            return LicenseStatus.NOT_FOUND, f"License file not found or empty: {self._license_path}"

        # Load signing key
        signing_key = self._load_signing_key()
        if signing_key is None:
            return (
                LicenseStatus.INVALID,
                "LICENSE_SIGNING_KEY environment variable is not set. "
                "This is required for Docker Compose SKU license validation.",
            )

        ok, reason = validate_license(license_b64, signing_key)
        if ok:
            self._cached_tier = self._extract_tier_from_license(license_b64)
            return LicenseStatus.VALID, reason

        # Map reason strings to specific status codes
        if "hardware fingerprint mismatch" in reason.lower():
            return LicenseStatus.HARDWARE_MISMATCH, reason
        if "expired" in reason.lower():
            return LicenseStatus.EXPIRED, reason

        return LicenseStatus.INVALID, reason

    @staticmethod
    def _load_signing_key() -> bytes | None:
        """Load HMAC signing key from environment. Returns None if not set."""
        raw = os.environ.get(_ENV_SIGNING_KEY, "").strip()
        if not raw or len(raw) != 64:
            return None
        try:
            return bytes.fromhex(raw)
        except ValueError:
            return None

    def _extract_tier_from_license(self, license_b64: str) -> int:
        """Decode tier from the license payload. Returns 1 on any error."""
        import base64
        import json
        try:
            payload = json.loads(base64.b64decode(license_b64).decode("utf-8"))
            tier = int(payload.get("product_tier", 1))
            return tier if tier in range(1, 5) else 1
        except Exception:
            return 1

    @staticmethod
    def _read_tier_from_tpm() -> int:
        """Read tier from TPM sealed storage. Returns 1 if not found."""
        try:
            from security.hardware_binding.binding import read_sealed_tier  # type: ignore
            return read_sealed_tier() or 1
        except Exception:
            return 1

    @staticmethod
    def _user_facing_error(status: LicenseStatus, reason: str) -> str:
        """Produce a clear, actionable error message for the given status."""
        base = "\n" + "=" * 60 + "\n  AgentCore LICENSE ERROR\n" + "=" * 60
        if status == LicenseStatus.NOT_FOUND:
            return (
                f"{base}\n"
                "  No license file found.\n\n"
                "  If you purchased the Docker Compose SKU:\n"
                "    1. Collect your hardware fingerprint:\n"
                "       agentcore-binding fingerprint --json\n"
                "    2. Email fingerprint to support@agentcore.io\n"
                "       to receive your license.key file.\n"
                "    3. Place license.key at /etc/agentcore/license.key\n"
                "       (or set AGENTCORE_LICENSE_PATH)\n"
                "    4. Restart AgentCore.\n"
                + "=" * 60
            )
        if status == LicenseStatus.HARDWARE_MISMATCH:
            return (
                f"{base}\n"
                "  License hardware mismatch.\n\n"
                "  This license was issued for different hardware.\n"
                "  If you replaced hardware, contact support@agentcore.io\n"
                "  with your order number and new hardware fingerprint.\n"
                + "=" * 60
            )
        if status == LicenseStatus.EXPIRED:
            return (
                f"{base}\n"
                "  License has expired.\n\n"
                "  Contact support@agentcore.io to renew.\n"
                + "=" * 60
            )
        return (
            f"{base}\n"
            f"  License validation failed: {reason}\n\n"
            "  Contact support@agentcore.io with this error message.\n"
            + "=" * 60
        )
