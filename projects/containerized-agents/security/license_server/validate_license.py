"""
License key validator — validates a customer's license key.
Useful for support: paste a license key, see if it's valid and what it's bound to.
Does NOT need hardware — just checks cryptographic validity and metadata.

Usage:
    python validate_license.py --license-key <base64_key>
    python validate_license.py --license-file /path/to/license.key

Requires env var: LICENSE_SIGNING_KEY (32 bytes, hex)
"""
import base64
import click
import hmac
import hashlib
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Support running directly from this directory
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

TIER_NAMES = {
    1: "Entry (~$400–600)",
    2: "Mid (~$800–1,400)",
    3: "Pro (~$2,400–3,500)",
    4: "Enterprise (~$4,000–8,000)",
}


def _load_signing_key() -> bytes:
    raw = os.environ.get("LICENSE_SIGNING_KEY", "").strip()
    if not raw:
        raise EnvironmentError("LICENSE_SIGNING_KEY environment variable is not set.")
    if len(raw) != 64:
        raise ValueError(f"LICENSE_SIGNING_KEY must be 64 hex chars. Got {len(raw)}.")
    return bytes.fromhex(raw)


def _compute_signature(payload: dict, signing_key: bytes) -> str:
    """Re-compute HMAC-SHA256 over canonical JSON (excluding 'signature' key)."""
    canonical = json.dumps(
        {k: v for k, v in sorted(payload.items()) if k != "signature"},
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    return hmac.new(signing_key, canonical, hashlib.sha256).hexdigest()


def validate_license_cryptography(license_b64: str, signing_key: bytes) -> dict:
    """
    Validate a license key's cryptographic integrity and metadata.

    Does NOT check hardware fingerprint (no hardware access needed).
    Returns a result dict with keys:
        valid: bool
        reason: str
        metadata: dict | None  (decoded payload fields if decodable)
    """
    result: dict = {"valid": False, "reason": "", "metadata": None}

    # Decode
    try:
        license_bytes = base64.b64decode(license_b64.strip())
        payload = json.loads(license_bytes.decode("utf-8"))
    except Exception as exc:
        result["reason"] = f"License decode error: {exc}"
        return result

    # Version check
    version = payload.get("version")
    if version != 1:
        result["reason"] = f"Unsupported license version: {version!r} (expected 1)"
        result["metadata"] = payload
        return result

    # Required fields
    required = {"hardware_fingerprint", "issued_at", "product_tier", "signature"}
    missing = required - payload.keys()
    if missing:
        result["reason"] = f"License is missing required fields: {sorted(missing)}"
        result["metadata"] = payload
        return result

    # Signature verification (constant-time)
    expected_sig = _compute_signature(payload, signing_key)
    provided_sig = payload.get("signature", "")
    if not hmac.compare_digest(expected_sig, provided_sig):
        result["reason"] = "Signature verification FAILED — license is tampered or wrong signing key."
        result["metadata"] = {
            k: v for k, v in payload.items() if k != "signature"
        }
        return result

    # All checks passed
    result["valid"] = True
    result["reason"] = "Signature valid."
    result["metadata"] = {
        "version": payload["version"],
        "hardware_fingerprint": payload["hardware_fingerprint"],
        "issued_at": payload["issued_at"],
        "product_tier": payload["product_tier"],
        "tier_name": TIER_NAMES.get(payload["product_tier"], "Unknown"),
    }
    return result


def _print_result(result: dict, raw_key: str) -> None:
    """Pretty-print validation results to stdout."""
    if result["valid"]:
        click.echo(click.style("VALID", fg="green", bold=True))
    else:
        click.echo(click.style("INVALID", fg="red", bold=True))

    click.echo(f"  Reason:    {result['reason']}")

    meta = result.get("metadata")
    if meta:
        click.echo("  Metadata:")
        for k, v in meta.items():
            if k == "hardware_fingerprint" and isinstance(v, str) and len(v) == 64:
                # Truncate for readability
                v = f"{v[:16]}...{v[-8:]} (64 hex chars)"
            click.echo(f"    {k}: {v}")

    click.echo(f"  Raw key length: {len(raw_key)} chars")


@click.command()
@click.option("--license-key", default="", help="Base64-encoded license key string")
@click.option("--license-file", default="", type=click.Path(exists=False), help="Path to license.key file")
def main(license_key: str, license_file: str) -> None:
    """Validate a customer license key (cryptographic check only — no hardware required).

    Provide either --license-key <base64> or --license-file <path>.
    """
    if not license_key and not license_file:
        click.echo("ERROR: Provide --license-key or --license-file.", err=True)
        sys.exit(1)

    if license_file:
        path = Path(license_file)
        if not path.exists():
            click.echo(f"ERROR: File not found: {license_file}", err=True)
            sys.exit(1)
        license_key = path.read_text(encoding="utf-8").strip()

    if not license_key:
        click.echo("ERROR: License key is empty.", err=True)
        sys.exit(1)

    # Load signing key
    try:
        signing_key = _load_signing_key()
    except (EnvironmentError, ValueError) as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(1)

    result = validate_license_cryptography(license_key, signing_key)
    _print_result(result, license_key)

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
