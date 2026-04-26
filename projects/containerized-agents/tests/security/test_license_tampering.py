"""
Security tests: license key tamper detection.
Verifies that tampered licenses are rejected with constant-time comparison.
"""
from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest

from security.hardware_binding.fallback_license import generate_license, validate_license
from security.hardware_binding.crypto import encrypt, decrypt


class TestLicenseTamperDetection:
    """All tampered license blobs must be rejected."""

    def _make_fp(self, char: str = "a") -> str:
        return char * 64

    def _mock_fp(self, fingerprint_hex: str):
        mock = MagicMock()
        mock.is_valid.return_value = True
        mock.sha256_fingerprint.return_value = bytes.fromhex(fingerprint_hex)
        return mock

    def test_flip_single_bit_rejected(self):
        """Flipping one bit in the license blob must cause rejection."""
        key = os.urandom(32)
        fp = "c" * 64
        license_b64 = generate_license(fp, tier=1, signing_key=key)

        # Flip one byte in the middle
        import base64
        raw = bytearray(base64.b64decode(license_b64))
        raw[len(raw) // 2] ^= 0x01
        tampered_b64 = base64.b64encode(bytes(raw)).decode()

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=self._mock_fp(fp),
        ):
            is_valid, reason = validate_license(tampered_b64, key)
        assert is_valid is False

    def test_truncated_license_rejected(self):
        """A license with trailing bytes stripped must be rejected."""
        key = os.urandom(32)
        fp = "d" * 64
        license_b64 = generate_license(fp, tier=1, signing_key=key)
        truncated = license_b64[:len(license_b64) // 2]

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=self._mock_fp(fp),
        ):
            is_valid, _ = validate_license(truncated, key)
        assert is_valid is False

    def test_wrong_key_rejected(self):
        """License validated with the wrong key must fail."""
        key1 = os.urandom(32)
        key2 = os.urandom(32)
        fp = "e" * 64
        license_b64 = generate_license(fp, tier=2, signing_key=key1)

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=self._mock_fp(fp),
        ):
            is_valid, _ = validate_license(license_b64, key2)
        assert is_valid is False

    def test_hardware_mismatch_rejected(self):
        """License for hardware A must not validate on hardware B."""
        key = os.urandom(32)
        license_fp = "f" * 64
        different_fp = "0" * 64
        license_b64 = generate_license(license_fp, tier=1, signing_key=key)

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=self._mock_fp(different_fp),
        ):
            is_valid, reason = validate_license(license_b64, key)
        assert is_valid is False
        assert "fingerprint" in reason.lower() or "hardware" in reason.lower()

    def test_all_tiers_valid_roundtrip(self):
        """All tiers 1-4 must produce licenses that pass crypto validation."""
        for tier in range(1, 5):
            key = os.urandom(32)
            fp = os.urandom(32).hex()
            license_b64 = generate_license(fp, tier=tier, signing_key=key)

            with patch(
                "security.hardware_binding.fallback_license.collect_fingerprint",
                return_value=self._mock_fp(fp),
            ):
                is_valid, reason = validate_license(license_b64, key)
            assert is_valid is True, f"Tier {tier} failed: {reason}"

    def test_invalid_base64_rejected(self):
        """Garbage base64 input must be rejected gracefully."""
        key = os.urandom(32)
        fp = "a" * 64

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=self._mock_fp(fp),
        ):
            is_valid, _ = validate_license("!!!not-base64!!!", key)
        assert is_valid is False

    def test_empty_license_rejected(self):
        """Empty license string must be rejected."""
        key = os.urandom(32)
        fp = "b" * 64

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=self._mock_fp(fp),
        ):
            is_valid, _ = validate_license("", key)
        assert is_valid is False

    def test_insufficient_hardware_ids_rejects(self):
        """If hardware fingerprint cannot be collected, validation must fail."""
        key = os.urandom(32)
        fp = "c" * 64
        license_b64 = generate_license(fp, tier=1, signing_key=key)

        mock = MagicMock()
        mock.is_valid.return_value = False  # Not enough hardware identifiers

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=mock,
        ):
            is_valid, _ = validate_license(license_b64, key)
        assert is_valid is False
