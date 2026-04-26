"""
Update system tests: Ed25519 manifest signature verification.
"""
from __future__ import annotations

import json
import os
from unittest.mock import AsyncMock, patch

import pytest

from agentcore.updater.update_checker import verify_manifest_signature, check_for_updates


def _sign_manifest(private_key, manifest: dict) -> str:
    """Sign the canonical manifest with an Ed25519 private key."""
    canonical = json.dumps(
        {k: v for k, v in sorted(manifest.items()) if k != "signature"},
        separators=(",", ":"),
        sort_keys=True,
    ).encode("utf-8")
    sig_bytes = private_key.sign(canonical)
    return sig_bytes.hex()


class TestManifestSignatureVerification:
    """Ed25519 manifest signature tests."""

    @pytest.mark.asyncio
    async def test_valid_signature_accepted(self, ed25519_keypair, sample_manifest):
        """Manifest with a valid Ed25519 signature must pass verification."""
        private_key, public_key = ed25519_keypair
        sig_hex = _sign_manifest(private_key, sample_manifest)
        sample_manifest["signature"] = sig_hex

        pub_hex = public_key.public_bytes_raw().hex()
        result = await verify_manifest_signature(sample_manifest, pub_hex)
        assert result is True

    @pytest.mark.asyncio
    async def test_tampered_manifest_rejected(self, ed25519_keypair, sample_manifest):
        """Manifest with a field changed after signing must fail verification."""
        private_key, public_key = ed25519_keypair
        sig_hex = _sign_manifest(private_key, sample_manifest)
        sample_manifest["signature"] = sig_hex

        # Tamper: change the version after signing
        sample_manifest["latest"]["version"] = "99.99.99"

        pub_hex = public_key.public_bytes_raw().hex()
        result = await verify_manifest_signature(sample_manifest, pub_hex)
        assert result is False

    @pytest.mark.asyncio
    async def test_wrong_public_key_rejected(self, ed25519_keypair, sample_manifest):
        """Manifest signed with one key must fail against a different public key."""
        from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey
        private_key, _ = ed25519_keypair
        sig_hex = _sign_manifest(private_key, sample_manifest)
        sample_manifest["signature"] = sig_hex

        # Different key pair
        different_private = Ed25519PrivateKey.generate()
        different_public = different_private.public_key()
        wrong_pub_hex = different_public.public_bytes_raw().hex()

        result = await verify_manifest_signature(sample_manifest, wrong_pub_hex)
        assert result is False

    @pytest.mark.asyncio
    async def test_missing_signature_field_rejected(self, ed25519_keypair, sample_manifest):
        """Manifest without a signature field must fail verification."""
        _, public_key = ed25519_keypair
        # No signature field added
        pub_hex = public_key.public_bytes_raw().hex()
        result = await verify_manifest_signature(sample_manifest, pub_hex)
        assert result is False

    @pytest.mark.asyncio
    async def test_empty_public_key_rejected(self, sample_manifest):
        """Empty public key must cause verification to return False."""
        sample_manifest["signature"] = "a" * 128
        result = await verify_manifest_signature(sample_manifest, "")
        assert result is False

    @pytest.mark.asyncio
    async def test_invalid_hex_signature_rejected(self, ed25519_keypair, sample_manifest):
        """Non-hex signature string must cause verification to return False."""
        _, public_key = ed25519_keypair
        sample_manifest["signature"] = "not-valid-hex!!!"
        pub_hex = public_key.public_bytes_raw().hex()
        result = await verify_manifest_signature(sample_manifest, pub_hex)
        assert result is False

    @pytest.mark.asyncio
    async def test_check_for_updates_offline_returns_gracefully(self):
        """check_for_updates must return gracefully when offline (no exception)."""
        with patch("agentcore.updater.update_checker.is_internet_available", new=AsyncMock(return_value=False)):
            result = await check_for_updates("1.0.0")
        assert result.available is False
        assert result.error == "offline"

    @pytest.mark.asyncio
    async def test_check_for_updates_no_public_key_configured(self):
        """check_for_updates must return gracefully if UPDATE_PUBLIC_KEY_HEX is not set."""
        with (
            patch("agentcore.updater.update_checker.is_internet_available", new=AsyncMock(return_value=True)),
            patch.dict(os.environ, {"UPDATE_PUBLIC_KEY_HEX": ""}),
        ):
            result = await check_for_updates("1.0.0")
        assert result.available is False
        assert "not configured" in result.error.lower() or "UPDATE_PUBLIC_KEY_HEX" in result.error
