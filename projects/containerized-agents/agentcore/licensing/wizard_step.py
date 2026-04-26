"""
Setup wizard — Step 10: License Binding.
For OS image SKU: runs TPM binding init.
For Docker Compose SKU: prompts user to enter their license key.
"""
import logging
import os
from pathlib import Path

from fastapi import APIRouter
from pydantic import BaseModel

from .license_manager import LicenseManager, LicenseStatus, LicenseType

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/wizard/license", tags=["wizard"])

# Where to write the license key when the user pastes it in via the wizard.
_LICENSE_INSTALL_PATH = Path(
    os.environ.get("AGENTCORE_LICENSE_PATH", "/etc/agentcore/license.key")
)


# ---------------------------------------------------------------------------
# Request / Response models
# ---------------------------------------------------------------------------

class LicenseBindRequest(BaseModel):
    license_key: str | None = None  # None for TPM path


class LicenseBindResponse(BaseModel):
    success: bool
    type: str = ""          # "tpm" | "key"
    tier: int = 0
    error: str = ""


class LicenseStatusResponse(BaseModel):
    bound: bool
    type: str               # "tpm" | "key" | "unlicensed"
    status: str             # LicenseStatus value
    tier: int
    reason: str


# ---------------------------------------------------------------------------
# Endpoints
# ---------------------------------------------------------------------------

@router.post("/bind", response_model=LicenseBindResponse)
async def bind_license(req: LicenseBindRequest) -> LicenseBindResponse:
    """
    Attempt license binding.

    For OS image SKU (TPM detected, no license_key supplied): initialises TPM binding.
    For Docker Compose SKU (license_key supplied): validates and installs the key.

    Returns {"success": true, "type": "tpm"|"key", "tier": 1-4}
    or {"success": false, "error": "reason"}.
    """
    manager = LicenseManager()
    detected_type = manager.detect_license_type()

    # --- TPM path ---
    if detected_type == LicenseType.TPM_BOUND and req.license_key is None:
        return await _bind_tpm(manager)

    # --- Key path ---
    if req.license_key is not None:
        return await _bind_key(req.license_key.strip())

    # --- Ambiguous: user on TPM machine sent a key anyway — honour the key ---
    if req.license_key is not None:
        return await _bind_key(req.license_key.strip())

    # Nothing to do
    return LicenseBindResponse(
        success=False,
        error=(
            "No license_key provided and no TPM detected. "
            "Paste your license key to activate the Docker Compose SKU."
        ),
    )


@router.get("/status", response_model=LicenseStatusResponse)
async def license_status() -> LicenseStatusResponse:
    """Return current license status for wizard UI polling."""
    manager = LicenseManager()
    license_type = manager.detect_license_type()
    status, reason = manager.validate()
    tier = manager.get_tier() if status == LicenseStatus.VALID else 0

    return LicenseStatusResponse(
        bound=(status == LicenseStatus.VALID),
        type=license_type.value,
        status=status.value,
        tier=tier,
        reason=reason,
    )


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

async def _bind_tpm(manager: LicenseManager) -> LicenseBindResponse:
    """Run TPM binding initialisation via hardware_binding module."""
    try:
        from security.hardware_binding.binding import init_tpm_binding  # type: ignore
        ok, reason = init_tpm_binding()
    except ImportError:
        return LicenseBindResponse(
            success=False,
            error="TPM binding module not available on this installation.",
        )
    except Exception as exc:
        logger.exception("TPM init_tpm_binding raised")
        return LicenseBindResponse(success=False, error=f"TPM binding error: {exc}")

    if not ok:
        return LicenseBindResponse(success=False, error=reason)

    # Re-validate to get tier
    status, reason = manager.validate()
    tier = manager.get_tier() if status == LicenseStatus.VALID else 0
    return LicenseBindResponse(success=True, type="tpm", tier=tier)


async def _bind_key(license_key: str) -> LicenseBindResponse:
    """Validate a license key then persist it to the license file path."""
    if not license_key:
        return LicenseBindResponse(success=False, error="License key is empty.")

    # Pre-validate cryptography + hardware match before writing to disk
    signing_key_raw = os.environ.get("LICENSE_SIGNING_KEY", "").strip()
    if not signing_key_raw or len(signing_key_raw) != 64:
        return LicenseBindResponse(
            success=False,
            error=(
                "LICENSE_SIGNING_KEY is not configured in this container. "
                "This is a server misconfiguration — contact support."
            ),
        )

    try:
        signing_key = bytes.fromhex(signing_key_raw)
    except ValueError:
        return LicenseBindResponse(
            success=False,
            error="LICENSE_SIGNING_KEY environment variable is not valid hex.",
        )

    try:
        from security.hardware_binding.fallback_license import validate_license  # type: ignore
    except ImportError as exc:
        return LicenseBindResponse(
            success=False,
            error=f"License module import error: {exc}",
        )

    ok, reason = validate_license(license_key, signing_key)
    if not ok:
        logger.warning("License bind attempt rejected: %s", reason)
        return LicenseBindResponse(success=False, error=reason)

    # Write license key to disk
    try:
        _LICENSE_INSTALL_PATH.parent.mkdir(parents=True, exist_ok=True)
        _LICENSE_INSTALL_PATH.write_text(license_key + "\n", encoding="utf-8")
        # Restrict read permissions — only root/agentcore user should read this
        _LICENSE_INSTALL_PATH.chmod(0o640)
    except OSError as exc:
        logger.error("Failed to write license file: %s", exc)
        return LicenseBindResponse(
            success=False,
            error=f"Cannot save license file: {exc}",
        )

    # Read back tier for the response
    manager = LicenseManager()
    tier = manager.get_tier()

    logger.info("License key installed at %s (tier %s)", _LICENSE_INSTALL_PATH, tier)
    return LicenseBindResponse(success=True, type="key", tier=tier)
