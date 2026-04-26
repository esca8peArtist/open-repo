"""
Offline license key system for Docker Compose SKU.
Used when TPM is not available (customer's own hardware).
License key is generated at purchase time and tied to hardware fingerprint.
Validated locally — no internet required.
"""
import hashlib
import hmac
import base64
import json
import logging
from dataclasses import dataclass, asdict
from datetime import datetime, timezone
from pathlib import Path

from .fingerprint import collect_fingerprint

logger = logging.getLogger(__name__)

LICENSE_VERSION = 1

# NOTE: In production, LICENSE_SIGNING_KEY is generated per-sale and
# embedded in the license file (NOT hardcoded here).


@dataclass
class LicenseKey:
    version: int
    hardware_fingerprint: str    # SHA-256 hex of hardware at purchase time
    issued_at: str               # ISO8601 timestamp
    product_tier: int            # 1-4
    signature: str               # HMAC-SHA256 signature


def _compute_signature(payload: dict, signing_key: bytes) -> str:
    """Compute HMAC-SHA256 over the canonical JSON of the payload fields.

    The signature is computed over all fields except 'signature' itself,
    sorted by key to ensure determinism.
    """
    canonical = json.dumps(
        {k: v for k, v in sorted(payload.items()) if k != "signature"},
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hmac.new(signing_key, canonical, hashlib.sha256).hexdigest()


def generate_license(fingerprint_hex: str, tier: int, signing_key: bytes) -> str:
    """Generate a license key for the given hardware fingerprint.

    Called on our license server at purchase time.
    Returns a base64-encoded JSON license string that the customer enters
    during the setup wizard (or drops into /etc/agentcore/license.key).

    Args:
        fingerprint_hex: Hex-encoded SHA-256 hardware fingerprint collected
                         from the customer's machine at purchase time.
        tier:            Product tier (1–4 matching hardware tiers).
        signing_key:     HMAC signing key held by the license server.

    Returns:
        Base64-encoded license string.
    """
    if tier not in range(1, 5):
        raise ValueError(f"Invalid product tier {tier!r}. Must be 1–4.")
    if len(fingerprint_hex) != 64:
        raise ValueError("fingerprint_hex must be a 64-character SHA-256 hex string")

    payload: dict = {
        "version": LICENSE_VERSION,
        "hardware_fingerprint": fingerprint_hex,
        "issued_at": datetime.now(tz=timezone.utc).isoformat(),
        "product_tier": tier,
    }
    payload["signature"] = _compute_signature(payload, signing_key)

    license_json = json.dumps(payload, separators=(",", ":")).encode("utf-8")
    return base64.b64encode(license_json).decode("ascii")


def validate_license(license_b64: str, signing_key: bytes) -> tuple[bool, str]:
    """Validate a license key against the current hardware.

    Checks:
    1. License can be decoded and parsed.
    2. Version field is recognized.
    3. HMAC signature is valid (license has not been tampered with).
    4. Hardware fingerprint in the license matches the current machine.

    Returns:
        (is_valid: bool, reason: str)
    No internet required.
    """
    # --- Decode ---
    try:
        license_bytes = base64.b64decode(license_b64)
        payload = json.loads(license_bytes.decode("utf-8"))
    except Exception as exc:
        return False, f"License decode error: {exc}"

    # --- Version ---
    version = payload.get("version")
    if version != LICENSE_VERSION:
        return False, f"Unsupported license version: {version!r}"

    # --- Required fields ---
    required = {"hardware_fingerprint", "issued_at", "product_tier", "signature"}
    missing = required - payload.keys()
    if missing:
        return False, f"License is missing required fields: {missing}"

    # --- Signature verification (constant-time comparison) ---
    expected_sig = _compute_signature(payload, signing_key)
    provided_sig = payload.get("signature", "")
    if not hmac.compare_digest(expected_sig, provided_sig):
        return False, "License signature verification failed (tampered or wrong signing key)"

    # --- Hardware fingerprint check ---
    fp = collect_fingerprint()
    if not fp.is_valid():
        return False, (
            "Cannot validate license: insufficient hardware identifiers collected. "
            "At least 2 of TPM EK, CPU serial, board UUID, and MAC address are required."
        )

    current_fingerprint = fp.sha256_fingerprint().hex()
    license_fingerprint = payload.get("hardware_fingerprint", "")

    if not hmac.compare_digest(current_fingerprint, license_fingerprint):
        return False, (
            "Hardware fingerprint mismatch. "
            "This license was issued for different hardware."
        )

    tier = payload.get("product_tier")
    logger.info("License validated successfully: tier=%s issued_at=%s", tier, payload.get("issued_at"))
    return True, f"License valid (tier {tier}, issued {payload.get('issued_at')})"


def load_license_from_file(path: str = "/etc/agentcore/license.key") -> str | None:
    """Load license key from the filesystem.

    Returns the license string (base64), or None if the file does not exist
    or cannot be read. The license string is stripped of surrounding whitespace
    so it can be pasted with trailing newlines without issue.
    """
    license_path = Path(path)
    if not license_path.exists():
        logger.debug("License file not found: %s", path)
        return None
    try:
        content = license_path.read_text(encoding="utf-8").strip()
        if not content:
            logger.warning("License file is empty: %s", path)
            return None
        logger.debug("License loaded from %s", path)
        return content
    except OSError as exc:
        logger.error("Cannot read license file %s: %s", path, exc)
        return None
