"""
Publish a new release to the update server.
Signs the manifest with Ed25519 private key.
Uploads to S3. CloudFront invalidates automatically via S3 trigger.

Usage:
    python publish_release.py \\
        --version 1.2.0 \\
        --changelog "## v1.2.0 ..." \\
        --agentcore-image /path/to/agentcore-1.2.0.tar.gz \\
        --wizard-image /path/to/wizard-1.2.0.tar.gz

Requires env vars:
    AWS_ACCESS_KEY_ID         — AWS credentials
    AWS_SECRET_ACCESS_KEY     — AWS credentials
    AWS_REGION                — e.g. us-east-1  (default: us-east-1)
    S3_BUCKET                 — e.g. agentcore-updates
    CLOUDFRONT_DISTRIBUTION   — CloudFront distribution ID (for manual invalidation if needed)
    UPDATE_SIGNING_KEY        — Ed25519 private key, 32 bytes hex (64 chars)
"""
import click
import hashlib
import json
import logging
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import boto3
from botocore.exceptions import BotoCoreError, ClientError
from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
from cryptography.hazmat.primitives.serialization import Encoding, PrivateFormat, NoEncryption

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
logger = logging.getLogger(__name__)

S3_MANIFEST_KEY = "manifest.json"
S3_RELEASES_PREFIX = "releases"
S3_MODELS_PREFIX = "models"

MANIFEST_SCHEMA_VERSION = 1


# ---------------------------------------------------------------------------
# Cryptography helpers
# ---------------------------------------------------------------------------

def _load_signing_key() -> Ed25519PrivateKey:
    """Load Ed25519 private key from UPDATE_SIGNING_KEY env var (32 bytes hex)."""
    raw = os.environ.get("UPDATE_SIGNING_KEY", "").strip()
    if not raw:
        raise EnvironmentError(
            "UPDATE_SIGNING_KEY environment variable is not set. "
            "Set it to the 32-byte Ed25519 private key encoded as 64 hex characters."
        )
    if len(raw) != 64:
        raise ValueError(f"UPDATE_SIGNING_KEY must be exactly 64 hex chars. Got {len(raw)}.")
    try:
        key_bytes = bytes.fromhex(raw)
    except ValueError as exc:
        raise ValueError(f"UPDATE_SIGNING_KEY is not valid hex: {exc}") from exc
    return Ed25519PrivateKey.from_private_bytes(key_bytes)


def _sign_manifest(manifest: dict, private_key: Ed25519PrivateKey) -> str:
    """Sign the canonical JSON of the manifest (excluding 'signature') with Ed25519.

    Returns the hex-encoded signature.
    """
    canonical = json.dumps(
        {k: v for k, v in sorted(manifest.items()) if k != "signature"},
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    sig_bytes = private_key.sign(canonical)
    return sig_bytes.hex()


# ---------------------------------------------------------------------------
# File hashing
# ---------------------------------------------------------------------------

def _sha256_file(path: Path) -> str:
    """Compute SHA-256 hex digest of a file."""
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


# ---------------------------------------------------------------------------
# S3 helpers
# ---------------------------------------------------------------------------

def _s3_client():
    return boto3.client(
        "s3",
        region_name=os.environ.get("AWS_REGION", "us-east-1"),
    )


def _upload_file(s3, bucket: str, local_path: Path, s3_key: str) -> str:
    """Upload a file to S3. Returns the HTTPS URL."""
    logger.info("Uploading %s → s3://%s/%s (%d bytes)", local_path.name, bucket, s3_key, local_path.stat().st_size)
    s3.upload_file(
        str(local_path),
        bucket,
        s3_key,
        ExtraArgs={"ContentType": "application/octet-stream"},
    )
    region = os.environ.get("AWS_REGION", "us-east-1")
    return f"https://{bucket}.s3.{region}.amazonaws.com/{s3_key}"


def _download_existing_manifest(s3, bucket: str) -> dict | None:
    """Download the current manifest from S3. Returns None if it doesn't exist."""
    try:
        response = s3.get_object(Bucket=bucket, Key=S3_MANIFEST_KEY)
        return json.loads(response["Body"].read().decode("utf-8"))
    except ClientError as exc:
        if exc.response["Error"]["Code"] == "NoSuchKey":
            logger.info("No existing manifest found — creating fresh.")
            return None
        raise


def _upload_manifest(s3, bucket: str, manifest: dict) -> None:
    """Upload the signed manifest JSON to S3 with public-read + max-age=60."""
    manifest_bytes = json.dumps(manifest, indent=2, sort_keys=False).encode("utf-8")
    logger.info("Uploading manifest (%d bytes) → s3://%s/%s", len(manifest_bytes), bucket, S3_MANIFEST_KEY)
    s3.put_object(
        Bucket=bucket,
        Key=S3_MANIFEST_KEY,
        Body=manifest_bytes,
        ContentType="application/json",
        CacheControl="max-age=60, must-revalidate",
    )


def _invalidate_cloudfront(distribution_id: str) -> None:
    """Create a CloudFront invalidation for /manifest.json."""
    if not distribution_id:
        logger.info("No CLOUDFRONT_DISTRIBUTION set — skipping manual invalidation.")
        return
    cf = boto3.client("cloudfront")
    caller_ref = f"publish-{datetime.now(tz=timezone.utc).strftime('%Y%m%dT%H%M%SZ')}"
    cf.create_invalidation(
        DistributionId=distribution_id,
        InvalidationBatch={
            "Paths": {"Quantity": 1, "Items": ["/manifest.json"]},
            "CallerReference": caller_ref,
        },
    )
    logger.info("CloudFront invalidation created for distribution %s", distribution_id)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

@click.command()
@click.option("--version", required=True, help="Release version (semver, e.g. 1.2.0)")
@click.option("--changelog", required=True, help="Markdown changelog text for this release")
@click.option(
    "--agentcore-image",
    type=click.Path(exists=True),
    default=None,
    help="Path to agentcore Docker image tar.gz",
)
@click.option(
    "--wizard-image",
    type=click.Path(exists=True),
    default=None,
    help="Path to wizard Docker image tar.gz",
)
@click.option("--min-version", default="", help="Minimum installed version that can upgrade to this")
@click.option("--critical", is_flag=True, default=False, help="Mark this as a critical security update")
@click.option("--dry-run", is_flag=True, default=False, help="Build and sign manifest but do NOT upload to S3")
def main(
    version: str,
    changelog: str,
    agentcore_image: str | None,
    wizard_image: str | None,
    min_version: str,
    critical: bool,
    dry_run: bool,
) -> None:
    """Publish a new AgentCore release to the update server (S3 + CloudFront)."""
    # Validate semver loosely
    parts = version.split(".")
    if len(parts) != 3 or not all(p.isdigit() for p in parts):
        click.echo(f"ERROR: --version must be semver (e.g. 1.2.0). Got: {version}", err=True)
        sys.exit(1)

    bucket = os.environ.get("S3_BUCKET", "")
    if not bucket and not dry_run:
        click.echo("ERROR: S3_BUCKET environment variable is not set.", err=True)
        sys.exit(1)

    distribution_id = os.environ.get("CLOUDFRONT_DISTRIBUTION", "")

    # Load signing key early — fail fast before doing any uploads
    try:
        private_key = _load_signing_key()
    except (EnvironmentError, ValueError) as exc:
        click.echo(f"ERROR: {exc}", err=True)
        sys.exit(1)

    s3 = _s3_client() if not dry_run else None

    # Build components dict
    components: dict = {}
    now_iso = datetime.now(tz=timezone.utc).isoformat()

    if agentcore_image:
        ag_path = Path(agentcore_image)
        ag_sha256 = _sha256_file(ag_path)
        ag_size = ag_path.stat().st_size
        if not dry_run:
            s3_key = f"{S3_RELEASES_PREFIX}/{version}/{ag_path.name}"
            ag_url = _upload_file(s3, bucket, ag_path, s3_key)
        else:
            ag_url = f"https://{bucket or 'BUCKET'}.s3.amazonaws.com/{S3_RELEASES_PREFIX}/{version}/{ag_path.name}"
        components["agentcore"] = {
            "image_url": ag_url,
            "sha256": ag_sha256,
            "size_bytes": ag_size,
            "docker_tag": f"agentcore:{version}",
        }
        logger.info("agentcore image: sha256=%s size=%d", ag_sha256, ag_size)

    if wizard_image:
        wz_path = Path(wizard_image)
        wz_sha256 = _sha256_file(wz_path)
        wz_size = wz_path.stat().st_size
        if not dry_run:
            s3_key = f"{S3_RELEASES_PREFIX}/{version}/{wz_path.name}"
            wz_url = _upload_file(s3, bucket, wz_path, s3_key)
        else:
            wz_url = f"https://{bucket or 'BUCKET'}.s3.amazonaws.com/{S3_RELEASES_PREFIX}/{version}/{wz_path.name}"
        components["wizard"] = {
            "image_url": wz_url,
            "sha256": wz_sha256,
            "size_bytes": wz_size,
            "docker_tag": f"agentcore-wizard:{version}",
        }
        logger.info("wizard image: sha256=%s size=%d", wz_sha256, wz_size)

    # Build new release record
    new_release: dict = {
        "version": version,
        "published_at": now_iso,
        "changelog": changelog,
        "critical": critical,
        "components": components,
    }
    if min_version:
        new_release["min_version"] = min_version

    # Fetch existing manifest and prepend new release
    if not dry_run:
        existing_manifest = _download_existing_manifest(s3, bucket)
    else:
        existing_manifest = None

    if existing_manifest:
        releases = existing_manifest.get("releases", [])
        # Remove any existing entry for this version (idempotent re-publish)
        releases = [r for r in releases if r.get("version") != version]
        releases.insert(0, new_release)
    else:
        releases = [new_release]

    manifest: dict = {
        "schema_version": MANIFEST_SCHEMA_VERSION,
        "published_at": now_iso,
        "latest": {
            "version": version,
            "tier1": version,
            "tier2": version,
            "tier3": version,
            "tier4": version,
        },
        "releases": releases,
        "signature": "",  # placeholder, filled below
    }

    # Sign
    manifest["signature"] = _sign_manifest(manifest, private_key)
    logger.info("Manifest signed with Ed25519 key.")

    if dry_run:
        click.echo("DRY RUN — manifest NOT uploaded. Signed manifest JSON:")
        click.echo(json.dumps(manifest, indent=2))
        return

    # Upload manifest
    try:
        _upload_manifest(s3, bucket, manifest)
    except (BotoCoreError, ClientError) as exc:
        click.echo(f"ERROR: S3 upload failed: {exc}", err=True)
        sys.exit(1)

    # CloudFront invalidation (best-effort — S3 event trigger is primary mechanism)
    try:
        _invalidate_cloudfront(distribution_id)
    except Exception as exc:
        logger.warning("CloudFront invalidation failed (non-fatal): %s", exc)

    click.echo(f"Release {version} published successfully.")
    click.echo(f"  Manifest: https://updates.agentcore.io/{S3_MANIFEST_KEY}")
    click.echo(f"  Bucket:   s3://{bucket}/{S3_MANIFEST_KEY}")


if __name__ == "__main__":
    main()
