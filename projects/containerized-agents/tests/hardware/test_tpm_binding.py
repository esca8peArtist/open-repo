"""
Hardware tests: TPM fingerprint collection — mock tpm2-tools subprocess calls.
"""
from __future__ import annotations

from unittest.mock import MagicMock, patch

import pytest

from security.hardware_binding.fingerprint import (
    HardwareFingerprint,
    collect_fingerprint,
    collect_tpm_ek,
)


class TestTPMFingerprint:
    """TPM-related fingerprint collection tests."""

    def test_collect_tpm_ek_success(self):
        """collect_tpm_ek must return a hex hash when tpm2 tools succeed."""
        fake_stdout = (
            "publickey:\n"
            "  exponent: 65537 (0x10001)\n"
            "  unique:\n"
            "    e0:b2:11:22:33:44:55:66:77:88:99:aa:bb:cc:dd:ee\n"
        )
        with patch("security.hardware_binding.fingerprint._run", return_value=fake_stdout):
            result = collect_tpm_ek()
        # Should return a non-empty string (hash or raw)
        assert result is not None
        assert len(result) > 0

    def test_collect_tpm_ek_missing_returns_none(self):
        """collect_tpm_ek must return None when tpm2 command is unavailable."""
        with patch("security.hardware_binding.fingerprint._run", return_value=None):
            result = collect_tpm_ek()
        assert result is None

    def test_collect_tpm_ek_subprocess_error_returns_none(self):
        """collect_tpm_ek must return None when subprocess raises FileNotFoundError."""
        with patch("security.hardware_binding.fingerprint._run", side_effect=FileNotFoundError("tpm2 not found")):
            result = collect_tpm_ek()
        assert result is None

    def test_collect_fingerprint_with_tpm_success(self):
        """collect_fingerprint with TPM available must include tpm_ek_hash."""
        with (
            patch("security.hardware_binding.fingerprint.collect_tpm_ek", return_value="tpm_hash_abc123"),
            patch("security.hardware_binding.fingerprint.collect_cpu_serial", return_value="cpu123"),
            patch("security.hardware_binding.fingerprint.collect_board_uuid", return_value="uuid-1234"),
            patch("security.hardware_binding.fingerprint.collect_mac_address", return_value="aa:bb:cc:dd:ee:ff"),
        ):
            fp = collect_fingerprint()

        assert fp.tpm_ek_hash == "tpm_hash_abc123"
        assert fp.is_valid() is True

    def test_collect_fingerprint_without_tpm(self):
        """collect_fingerprint must still work with TPM unavailable."""
        with (
            patch("security.hardware_binding.fingerprint.collect_tpm_ek", return_value=None),
            patch("security.hardware_binding.fingerprint.collect_cpu_serial", return_value="cpu123"),
            patch("security.hardware_binding.fingerprint.collect_board_uuid", return_value="uuid-abc"),
            patch("security.hardware_binding.fingerprint.collect_mac_address", return_value="00:11:22:33:44:55"),
        ):
            fp = collect_fingerprint()

        assert fp.tpm_ek_hash is None
        assert fp.is_valid() is True  # still valid with 3 other identifiers

    def test_tpm_only_not_valid_fingerprint(self):
        """TPM alone (1 identifier) must not produce a valid fingerprint."""
        fp = HardwareFingerprint(
            tpm_ek_hash="abc",
            cpu_serial=None,
            board_uuid=None,
            mac_address=None,
        )
        assert fp.is_valid() is False


class TestHardwareFingerprinting:
    """HardwareFingerprint data class tests."""

    def test_sha256_fingerprint_is_32_bytes(self):
        """sha256_fingerprint must be exactly 32 bytes."""
        fp = HardwareFingerprint(
            tpm_ek_hash="tpm",
            cpu_serial="cpu",
            board_uuid="uuid",
            mac_address="mac",
        )
        assert len(fp.sha256_fingerprint()) == 32

    def test_sha256_fingerprint_is_deterministic(self):
        """Same identifiers must always produce the same fingerprint."""
        fp = HardwareFingerprint(
            tpm_ek_hash="tpm_val",
            cpu_serial="cpu_val",
            board_uuid="uuid_val",
            mac_address="mac_val",
        )
        h1 = fp.sha256_fingerprint()
        h2 = fp.sha256_fingerprint()
        assert h1 == h2

    def test_different_identifiers_produce_different_fingerprints(self):
        """Different hardware must produce different fingerprints."""
        fp1 = HardwareFingerprint(tpm_ek_hash="aaa", cpu_serial="111", board_uuid=None, mac_address=None)
        fp2 = HardwareFingerprint(tpm_ek_hash="bbb", cpu_serial="222", board_uuid=None, mac_address=None)
        assert fp1.sha256_fingerprint() != fp2.sha256_fingerprint()

    def test_combined_string_format(self):
        """to_combined_string must format identifiers with known prefix:value|... pattern."""
        fp = HardwareFingerprint(
            tpm_ek_hash="tval",
            cpu_serial="cval",
            board_uuid=None,
            mac_address="mval",
        )
        combined = fp.to_combined_string()
        assert "tpm:tval" in combined
        assert "cpu:cval" in combined
        assert "mac:mval" in combined
