"""
License key generator — runs on our fulfillment server at purchase time.
Takes a hardware fingerprint (from buyer running `agentcore-binding fingerprint --json`)
and generates a signed license key to email/download to the customer.

Usage:
    python generate_license.py --fingerprint <hex> --tier <1-4> --output license.key

The SIGNING_KEY is loaded from environment variable LICENSE_SIGNING_KEY (32 bytes, hex).
Never hardcoded.
"""
import click
import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

# Support running directly from this directory
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))

from security.hardware_binding.fallback_license import generate_license

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)
logger = logging.getLogger(__name__)

AUDIT_LOG_PATH = Path(os.environ.get("LICENSE_AUDIT_LOG", "/var/log/agentcore/license_audit.jsonl"))


def _load_signing_key() -> bytes:
    """Load the HMAC signing key from environment. Raises if missing or malformed."""
    raw = os.environ.get("LICENSE_SIGNING_KEY", "")
    if not raw:
        raise EnvironmentError(
            "LICENSE_SIGNING_KEY environment variable is not set. "
            "Set it to the 32-byte HMAC key encoded as 64 hex characters."
        )
    raw = raw.strip()
    if len(raw) != 64:
        raise ValueError(
            f"LICENSE_SIGNING_KEY must be exactly 64 hex characters (32 bytes). Got {len(raw)} chars."
        )
    try:
        return bytes.fromhex(raw)
    except ValueError as exc:
        raise ValueError(f"LICENSE_SIGNING_KEY is not valid hex: {exc}") from exc


def _write_audit_log(entry: dict) -> None:
    """Append a JSONL audit record. Creates parent directories if needed."""
    try:
        AUDIT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        with AUDIT_LOG_PATH.open("a", encoding="utf-8") as fh:
            fh.write(json.dumps(entry, separators=(",", ":")) + "\n")
    except OSError as exc:
        # Audit logging failure is non-fatal but must be visible.
        logger.error("AUDIT LOG WRITE FAILED: %s — entry: %s", exc, entry)


@click.command()
@click.option("--fingerprint", required=True, help="Hardware fingerprint hex from buyer (64-char SHA-256 hex)")
@click.option(
    "--tier",
    type=click.Choice(["1", "2", "3", "4"]),
    required=True,
    help="Product tier (1=Entry, 2=Mid, 3=Pro, 4=Enterprise)",
)
@click.option("--output", default="license.key", show_default=True, help="Output file path for the license key")
@click.option("--customer-id", default="", help="Customer ID or order number for audit log")
def main(fingerprint: str, tier: str, output: str, customer_id: str) -> None:
    """Generate a hardware-bound license key for a customer.

    Loads LICENSE_SIGNING_KEY from the environment, generates a cryptographically
    signed license key, writes it to --output, and appends an audit record.
    """
    fingerprint = fingerprint.strip().lower()
    tier_int = int(tier)

    # Validate fingerprint format before doing anything else
    if len(fingerprint) != 64:
        click.echo(
            f"ERROR: --fingerprint must be a 64-character SHA-256 hex string. Got {len(fingerprint)} chars.",
            err=True,
        )
        sys.exit(1)
    try:
        bytes.fromhex(fingerprint)
    except ValueError:
        click.echo("ERROR: --fingerprint contains non-hex characters.", err=True)
        sys.exit(1)

    # Load signing key
    try:
        signing_key = _load_signing_key()
    except (EnvironmentError, ValueError) as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(1)

    # Generate license
    try:
        license_b64 = generate_license(fingerprint, tier_int, signing_key)
    except Exception as exc:
        click.echo(f"ERROR: License generation failed: {exc}", err=True)
        logger.exception("License generation error")
        sys.exit(1)

    # Write license to output file
    output_path = Path(output)
    try:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(license_b64 + "\n", encoding="utf-8")
    except OSError as exc:
        click.echo(f"ERROR: Cannot write license file to {output}: {exc}", err=True)
        sys.exit(1)

    # Audit log entry
    audit_entry = {
        "event": "license_generated",
        "timestamp": datetime.now(tz=timezone.utc).isoformat(),
        "customer_id": customer_id or "UNSET",
        "hardware_fingerprint": fingerprint,
        "tier": tier_int,
        "output_file": str(output_path.resolve()),
    }
    _write_audit_log(audit_entry)

    click.echo(f"License generated successfully.")
    click.echo(f"  Tier:        {tier_int}")
    click.echo(f"  Fingerprint: {fingerprint[:16]}...{fingerprint[-8:]}")
    click.echo(f"  Output:      {output_path.resolve()}")
    click.echo(f"  Audit log:   {AUDIT_LOG_PATH}")
    logger.info(
        "License issued: customer_id=%s tier=%s fingerprint=%s...",
        customer_id or "UNSET",
        tier_int,
        fingerprint[:16],
    )


if __name__ == "__main__":
    main()
