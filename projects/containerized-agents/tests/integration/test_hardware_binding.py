"""
Integration tests for TPM hardware binding and license key system.

Tests the full binding pipeline:
- Fingerprint collection (mocked at the OS-call level)
- License generation at purchase time
- License validation at boot time
- Hardware mismatch detection
- TPM seal/unseal flow (simulated)
"""
from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest

from security.hardware_binding.crypto import decrypt, derive_key, encrypt, generate_salt
from security.hardware_binding.fallback_license import (
    generate_license,
    load_license_from_file,
    validate_license,
)
from security.hardware_binding.fingerprint import HardwareFingerprint, collect_fingerprint


# ===========================================================================
# Full license round-trip: purchase → boot validation
# ===========================================================================


class TestLicenseRoundTrip:
    """Simulate the full lifecycle: purchase-time generation → first-boot validation."""

    def _generate_test_fingerprint_hex(self) -> str:
        """Generate a deterministic 64-char hex fingerprint for test machines."""
        return "a1b2c3d4" * 8  # 64 chars

    def test_full_lifecycle_correct_hardware(self):
        """
        Simulate: generate license on machine A, validate on same machine A.
        Must succeed.
        """
        signing_key = os.urandom(32)
        machine_fingerprint_hex = self._generate_test_fingerprint_hex()

        # Step 1: At purchase time, generate the license
        license_b64 = generate_license(
            fingerprint_hex=machine_fingerprint_hex,
            tier=2,
            signing_key=signing_key,
        )

        # Step 2: At first boot, validate against the actual hardware
        mock_fp = MagicMock()
        mock_fp.is_valid.return_value = True
        mock_fp.sha256_fingerprint.return_value = bytes.fromhex(machine_fingerprint_hex)

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=mock_fp,
        ):
            is_valid, reason = validate_license(license_b64, signing_key)

        assert is_valid is True, f"Expected valid license, got: {reason}"
        assert "tier 2" in reason.lower() or "valid" in reason.lower()

    def test_full_lifecycle_wrong_hardware(self):
        """
        Simulate: generate license on machine A, validate on machine B.
        Must fail with fingerprint mismatch.
        """
        signing_key = os.urandom(32)
        machine_a_fp = "aaaa" * 16  # 64 chars
        machine_b_fp = "bbbb" * 16  # different machine

        license_b64 = generate_license(machine_a_fp, tier=1, signing_key=signing_key)

        mock_fp = MagicMock()
        mock_fp.is_valid.return_value = True
        mock_fp.sha256_fingerprint.return_value = bytes.fromhex(machine_b_fp)

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=mock_fp,
        ):
            is_valid, reason = validate_license(license_b64, signing_key)

        assert is_valid is False
        assert "fingerprint" in reason.lower() or "hardware" in reason.lower()

    def test_license_preserves_tier(self):
        """The tier stored in the license must be reported in the success message."""
        signing_key = os.urandom(32)
        fp_hex = "cccc" * 16

        for expected_tier in range(1, 5):
            license_b64 = generate_license(fp_hex, tier=expected_tier, signing_key=signing_key)

            mock_fp = MagicMock()
            mock_fp.is_valid.return_value = True
            mock_fp.sha256_fingerprint.return_value = bytes.fromhex(fp_hex)

            with patch(
                "security.hardware_binding.fallback_license.collect_fingerprint",
                return_value=mock_fp,
            ):
                is_valid, reason = validate_license(license_b64, signing_key)

            assert is_valid is True
            assert str(expected_tier) in reason


# ===========================================================================
# Hardware-derived encryption key
# ===========================================================================


class TestHardwareDerivedKey:
    """
    Verify that configuration data encrypted with the hardware-derived key
    can only be decrypted with the same hardware present.
    """

    def test_config_encrypted_with_derived_key_is_recoverable(self):
        """Encrypt config with hardware-derived key, decrypt with same hardware key."""
        fingerprint_bytes = b"test machine fingerprint bytes!!"
        salt = generate_salt()

        key = derive_key(fingerprint_bytes, salt)
        config_data = b'{"system_prompt": "You are a secret business assistant"}'

        ciphertext = encrypt(config_data, key)
        plaintext = decrypt(ciphertext, key)

        assert plaintext == config_data

    def test_config_encrypted_with_derived_key_unreadable_on_different_hardware(self):
        """Config encrypted on machine A must fail to decrypt on machine B."""
        salt = generate_salt()

        fingerprint_a = b"hardware fingerprint for machine A"
        fingerprint_b = b"hardware fingerprint for machine B"

        key_a = derive_key(fingerprint_a, salt)
        key_b = derive_key(fingerprint_b, salt)

        assert key_a != key_b

        config_data = b'{"api_key": "secret-key-value"}'
        ciphertext = encrypt(config_data, key_a)

        with pytest.raises(ValueError):
            decrypt(ciphertext, key_b)

    def test_different_salt_means_different_key(self):
        """Even with the same hardware fingerprint, different salts produce different keys."""
        fingerprint = b"same hardware fingerprint data!!"
        salt_1 = os.urandom(32)
        salt_2 = os.urandom(32)

        key_1 = derive_key(fingerprint, salt_1)
        key_2 = derive_key(fingerprint, salt_2)

        assert key_1 != key_2


# ===========================================================================
# License file I/O
# ===========================================================================


class TestLicenseFileIO:
    def test_load_license_from_nonexistent_file_returns_none(self):
        """Loading a license from a path that doesn't exist must return None."""
        result = load_license_from_file("/tmp/agentcore_test_nonexistent_license_1234567.key")
        assert result is None

    def test_load_license_from_file_roundtrip(self, tmp_path):
        """A license written to a file must be loadable from that file."""
        signing_key = os.urandom(32)
        fp_hex = "e5f6" * 16
        license_b64 = generate_license(fp_hex, tier=1, signing_key=signing_key)

        license_file = tmp_path / "license.key"
        license_file.write_text(license_b64 + "\n")  # Trailing newline is common

        loaded = load_license_from_file(str(license_file))
        assert loaded is not None
        assert loaded == license_b64  # Stripped of trailing newline

    def test_load_empty_license_file_returns_none(self, tmp_path):
        """An empty license file must return None, not an empty string."""
        empty_file = tmp_path / "empty.key"
        empty_file.write_text("")

        result = load_license_from_file(str(empty_file))
        assert result is None

    def test_load_whitespace_only_license_file_returns_none(self, tmp_path):
        """A whitespace-only license file must return None."""
        ws_file = tmp_path / "whitespace.key"
        ws_file.write_text("   \n\t\n  ")

        result = load_license_from_file(str(ws_file))
        assert result is None


# ===========================================================================
# Fingerprint collection integration
# ===========================================================================


class TestFingerprintCollectionIntegration:
    def test_collect_fingerprint_returns_hardware_fingerprint(self):
        """collect_fingerprint must always return a HardwareFingerprint object."""
        fp = collect_fingerprint()
        assert isinstance(fp, HardwareFingerprint)

    def test_collect_fingerprint_with_mocked_identifiers(self):
        """All four identifiers collected correctly must produce a valid fingerprint."""
        with (
            patch("security.hardware_binding.fingerprint.collect_tpm_ek", return_value="tpm_hash_value"),
            patch("security.hardware_binding.fingerprint.collect_cpu_serial", return_value="cpu_serial_value"),
            patch("security.hardware_binding.fingerprint.collect_board_uuid", return_value="board_uuid_value"),
            patch("security.hardware_binding.fingerprint.collect_mac_address", return_value="00:11:22:33:44:55"),
        ):
            fp = collect_fingerprint()

        assert fp.is_valid() is True
        assert fp.tpm_ek_hash == "tpm_hash_value"
        assert fp.cpu_serial == "cpu_serial_value"
        assert fp.board_uuid == "board_uuid_value"
        assert fp.mac_address == "00:11:22:33:44:55"

        # Fingerprint must be 32 bytes (SHA-256)
        digest = fp.sha256_fingerprint()
        assert len(digest) == 32

        # Hex representation must be 64 chars
        hex_fp = digest.hex()
        assert len(hex_fp) == 64

    def test_fingerprint_hex_suitable_for_license_generation(self):
        """
        The fingerprint hex produced by sha256_fingerprint().hex() must be
        usable directly in generate_license().
        """
        with (
            patch("security.hardware_binding.fingerprint.collect_tpm_ek", return_value="tpm"),
            patch("security.hardware_binding.fingerprint.collect_cpu_serial", return_value="cpu"),
            patch("security.hardware_binding.fingerprint.collect_board_uuid", return_value=None),
            patch("security.hardware_binding.fingerprint.collect_mac_address", return_value="mac"),
        ):
            fp = collect_fingerprint()

        hex_fp = fp.sha256_fingerprint().hex()
        signing_key = os.urandom(32)

        # Must not raise
        license_b64 = generate_license(hex_fp, tier=1, signing_key=signing_key)
        assert isinstance(license_b64, str)
        assert len(license_b64) > 0
