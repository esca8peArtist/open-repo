"""
On-device update checker.
Called when user clicks "Check for Updates" in admin dashboard.
Only runs if internet is available. Fails gracefully if offline.
Verifies manifest signature with Ed25519 public key (embedded in agentcore).
"""
import json
import logging
from dataclasses import dataclass, field
from packaging.version import Version, InvalidVersion

import httpx
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PublicKey
from cryptography.exceptions import InvalidSignature

from agentcore.config import get_settings

logger = logging.getLogger(__name__)

MANIFEST_URL = "https://updates.agentcore.io/manifest.json"

# Connectivity probe — HEAD request to a well-known reliable endpoint.
_CONNECTIVITY_PROBE_URL = "https://dns.google"
_HTTP_TIMEOUT = 30.0  # seconds


@dataclass
class UpdateInfo:
    available: bool
    current_version: str
    latest_version: str
    changelog: str
    components: list[dict] = field(default_factory=list)
    manifest: dict = field(default_factory=dict)
    error: str = ""


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def check_for_updates(current_version: str) -> UpdateInfo:
    """
    Fetch and verify update manifest.
    Returns UpdateInfo with available=False if offline or already up to date.
    Never raises — always returns gracefully.
    """
    no_update = UpdateInfo(
        available=False,
        current_version=current_version,
        latest_version=current_version,
        changelog="",
    )

    if not await is_internet_available():
        logger.info("Update check skipped — no internet connectivity.")
        no_update.error = "offline"
        return no_update

    public_key_hex = get_settings().update_public_key_hex.strip()
    if not public_key_hex:
        logger.error(
            "UPDATE_PUBLIC_KEY_HEX is not set — cannot verify update manifest. "
            "This is a build configuration issue."
        )
        no_update.error = "UPDATE_PUBLIC_KEY_HEX not configured"
        return no_update

    try:
        manifest = await _fetch_manifest()
    except Exception as exc:
        logger.warning("Failed to fetch update manifest: %s", exc)
        no_update.error = f"fetch error: {exc}"
        return no_update

    try:
        sig_ok = await verify_manifest_signature(manifest, public_key_hex)
    except Exception as exc:
        logger.error("Manifest signature verification raised: %s", exc)
        no_update.error = f"signature error: {exc}"
        return no_update

    if not sig_ok:
        logger.error("Update manifest signature INVALID — ignoring manifest.")
        no_update.error = "signature invalid"
        return no_update

    # Compare versions
    try:
        current_ver = Version(current_version)
        latest_str = manifest.get("latest", {}).get("version", current_version)
        latest_ver = Version(latest_str)
    except InvalidVersion as exc:
        logger.warning("Version parse error: %s", exc)
        no_update.error = f"version parse error: {exc}"
        return no_update

    if latest_ver <= current_ver:
        logger.info("No update available (current=%s, latest=%s)", current_version, latest_str)
        return UpdateInfo(
            available=False,
            current_version=current_version,
            latest_version=latest_str,
            changelog="",
            manifest=manifest,
        )

    # Find the matching release entry for the latest version
    releases = manifest.get("releases", [])
    latest_release = next((r for r in releases if r.get("version") == latest_str), None)
    if not latest_release:
        logger.warning("Latest version %s not found in releases list", latest_str)
        no_update.error = f"release {latest_str} not in manifest"
        return no_update

    # Check min_version constraint
    min_version_str = latest_release.get("min_version", "")
    if min_version_str:
        try:
            if current_ver < Version(min_version_str):
                logger.warning(
                    "Update %s requires min version %s; current is %s — update path not available",
                    latest_str, min_version_str, current_version,
                )
                no_update.error = (
                    f"Update {latest_str} requires version >= {min_version_str}. "
                    f"Current version {current_version} cannot upgrade directly."
                )
                return no_update
        except InvalidVersion:
            pass  # Non-fatal — proceed

    # Collect components to download
    components = _extract_components(latest_release)
    changelog = latest_release.get("changelog", "")

    logger.info(
        "Update available: %s → %s (%d components)",
        current_version, latest_str, len(components),
    )

    return UpdateInfo(
        available=True,
        current_version=current_version,
        latest_version=latest_str,
        changelog=changelog,
        components=components,
        manifest=manifest,
    )


async def verify_manifest_signature(manifest: dict, public_key_hex: str) -> bool:
    """Verify Ed25519 signature on manifest. Returns False if invalid."""
    if not public_key_hex:
        logger.error("No public key provided for manifest verification.")
        return False

    signature_hex = manifest.get("signature", "")
    if not signature_hex:
        logger.error("Manifest has no signature field.")
        return False

    try:
        sig_bytes = bytes.fromhex(signature_hex)
        key_bytes = bytes.fromhex(public_key_hex)
    except ValueError as exc:
        logger.error("Hex decode error during signature verification: %s", exc)
        return False

    # Reconstruct the canonical JSON that was signed
    canonical = json.dumps(
        {k: v for k, v in sorted(manifest.items()) if k != "signature"},
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")

    try:
        public_key = Ed25519PublicKey.from_public_bytes(key_bytes)
        public_key.verify(sig_bytes, canonical)
        logger.debug("Manifest Ed25519 signature verified OK.")
        return True
    except InvalidSignature:
        logger.error("Manifest Ed25519 signature INVALID.")
        return False
    except Exception as exc:
        logger.error("Signature verification error: %s", exc)
        return False


async def is_internet_available() -> bool:
    """Quick connectivity check (HEAD request to known reliable endpoint)."""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.head(_CONNECTIVITY_PROBE_URL)
            return response.status_code < 500
    except Exception:
        return False


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

async def _fetch_manifest() -> dict:
    """Download manifest.json from the update server. Raises on HTTP/network error."""
    async with httpx.AsyncClient(timeout=_HTTP_TIMEOUT, follow_redirects=True) as client:
        response = await client.get(MANIFEST_URL)
        response.raise_for_status()
        return response.json()


def _extract_components(release: dict) -> list[dict]:
    """Flatten the components dict into a list for easier iteration by the installer."""
    result = []
    components = release.get("components", {})

    for name in ("agentcore", "wizard"):
        comp = components.get(name)
        if comp:
            result.append({
                "type": name,
                "image_url": comp["image_url"],
                "sha256": comp["sha256"],
                "size_bytes": comp.get("size_bytes", 0),
                "docker_tag": comp.get("docker_tag", ""),
            })

    for model in components.get("models", []):
        result.append({
            "type": "model",
            "name": model.get("name", ""),
            "version": model.get("version", ""),
            "tiers": model.get("tiers", []),
            "download_url": model.get("download_url", ""),
            "sha256": model.get("sha256", ""),
            "size_bytes": model.get("size_bytes", 0),
            "optional": model.get("optional", False),
        })

    return result
