"""
Unit tests for the license system and cryptographic primitives.

Covers:
- generate_license / validate_license round-trip (crypto only, not hardware check)
- Tampered license fails validation
- Wrong signing key fails validation
- AES-256-GCM encrypt / decrypt round-trip
- Wrong key raises ValueError
- Tampered ciphertext raises ValueError
- derive_key determinism
- HardwareFingerprint.is_valid() minimum identifier threshold
- HardwareFingerprint.sha256_fingerprint() consistency
"""
from __future__ import annotations

import os
from unittest.mock import MagicMock, patch

import pytest

from security.hardware_binding.crypto import decrypt, derive_key, encrypt, generate_salt
from security.hardware_binding.fallback_license import generate_license, validate_license
from security.hardware_binding.fingerprint import HardwareFingerprint


# ===========================================================================
# License generation & validation
# ===========================================================================


class TestLicenseGeneration:
    """Crypto round-trip tests — hardware fingerprint check is patched out."""

    def _make_fp(self, hex_char: str = "a") -> str:
        """Return a valid 64-character hex fingerprint."""
        return hex_char * 64

    def test_generate_returns_nonempty_base64(self):
        """generate_license must return a non-empty base64 string."""
        key = os.urandom(32)
        license_b64 = generate_license(self._make_fp("a"), tier=1, signing_key=key)
        assert isinstance(license_b64, str)
        assert len(license_b64) > 0

    def test_invalid_tier_raises(self):
        """generate_license must raise ValueError for out-of-range tiers."""
        key = os.urandom(32)
        with pytest.raises(ValueError, match="tier"):
            generate_license(self._make_fp("a"), tier=0, signing_key=key)
        with pytest.raises(ValueError, match="tier"):
            generate_license(self._make_fp("a"), tier=5, signing_key=key)

    def test_short_fingerprint_raises(self):
        """generate_license must raise ValueError if fingerprint is not 64 hex chars."""
        key = os.urandom(32)
        with pytest.raises(ValueError):
            generate_license("tooshort", tier=1, signing_key=key)

    def test_generate_and_crypto_validate_roundtrip(self):
        """Signature verification must pass on an unmodified license with the same key."""
        key = os.urandom(32)
        fingerprint = "c" * 64
        license_b64 = generate_license(fingerprint, tier=1, signing_key=key)

        # Patch the hardware fingerprint check so we can test crypto in isolation
        mock_fp = MagicMock()
        mock_fp.is_valid.return_value = True
        mock_fp.sha256_fingerprint.return_value = bytes.fromhex(fingerprint)

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=mock_fp,
        ):
            is_valid, reason = validate_license(license_b64, key)

        assert is_valid is True
        assert "valid" in reason.lower()

    def test_tampered_license_fails_validation(self):
        """Flipping characters at the end of the license b64 must cause validation failure."""
        key = os.urandom(32)
        license_b64 = generate_license("b" * 64, tier=2, signing_key=key)

        # Tamper: replace last 4 chars with X's
        tampered = license_b64[:-4] + "XXXX"

        mock_fp = MagicMock()
        mock_fp.is_valid.return_value = True
        mock_fp.sha256_fingerprint.return_value = bytes.fromhex("b" * 64)

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=mock_fp,
        ):
            is_valid, reason = validate_license(tampered, key)

        assert is_valid is False

    def test_wrong_signing_key_fails(self):
        """Validating a license with a different signing key must fail."""
        key1 = os.urandom(32)
        key2 = os.urandom(32)
        assert key1 != key2  # Sanity check

        license_b64 = generate_license("c" * 64, tier=1, signing_key=key1)

        mock_fp = MagicMock()
        mock_fp.is_valid.return_value = True
        mock_fp.sha256_fingerprint.return_value = bytes.fromhex("c" * 64)

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=mock_fp,
        ):
            is_valid, _ = validate_license(license_b64, key2)

        assert is_valid is False

    def test_hardware_mismatch_fails(self):
        """If the hardware fingerprint doesn't match the one in the license, validation must fail."""
        key = os.urandom(32)
        license_fp = "a" * 64
        current_fp = "b" * 64  # Different machine

        license_b64 = generate_license(license_fp, tier=1, signing_key=key)

        mock_fp = MagicMock()
        mock_fp.is_valid.return_value = True
        mock_fp.sha256_fingerprint.return_value = bytes.fromhex(current_fp)

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=mock_fp,
        ):
            is_valid, reason = validate_license(license_b64, key)

        assert is_valid is False
        assert "fingerprint" in reason.lower() or "hardware" in reason.lower()

    def test_insufficient_hardware_ids_fails(self):
        """If the current machine cannot produce a valid fingerprint, validation must fail."""
        key = os.urandom(32)
        license_b64 = generate_license("d" * 64, tier=1, signing_key=key)

        mock_fp = MagicMock()
        mock_fp.is_valid.return_value = False  # Not enough hardware identifiers

        with patch(
            "security.hardware_binding.fallback_license.collect_fingerprint",
            return_value=mock_fp,
        ):
            is_valid, reason = validate_license(license_b64, key)

        assert is_valid is False

    def test_all_tiers_generate_valid_licenses(self):
        """All valid tiers (1-4) must produce a license that passes crypto validation."""
        for tier in range(1, 5):
            key = os.urandom(32)
            fp = os.urandom(32).hex()  # 64 hex chars
            license_b64 = generate_license(fp, tier=tier, signing_key=key)

            mock_fp = MagicMock()
            mock_fp.is_valid.return_value = True
            mock_fp.sha256_fingerprint.return_value = bytes.fromhex(fp)

            with patch(
                "security.hardware_binding.fallback_license.collect_fingerprint",
                return_value=mock_fp,
            ):
                is_valid, reason = validate_license(license_b64, key)

            assert is_valid is True, f"Tier {tier} license failed: {reason}"


# ===========================================================================
# AES-256-GCM encrypt / decrypt
# ===========================================================================


class TestCrypto:
    def test_encrypt_decrypt_roundtrip(self):
        """Encrypt then decrypt must recover the original plaintext."""
        key = os.urandom(32)
        plaintext = b"sensitive agent config data"
        ciphertext = encrypt(plaintext, key)
        assert decrypt(ciphertext, key) == plaintext

    def test_encrypt_produces_different_ciphertext_each_call(self):
        """Two encryptions of the same plaintext with the same key must produce different output."""
        key = os.urandom(32)
        plaintext = b"same plaintext"
        ct1 = encrypt(plaintext, key)
        ct2 = encrypt(plaintext, key)
        assert ct1 != ct2  # Nonces differ

    def test_wrong_key_raises_valueerror(self):
        """Decrypting with the wrong key must raise ValueError."""
        key1 = os.urandom(32)
        key2 = os.urandom(32)
        ciphertext = encrypt(b"test data", key1)
        with pytest.raises(ValueError):
            decrypt(ciphertext, key2)

    def test_tampered_ciphertext_raises_valueerror(self):
        """Flipping a byte in the ciphertext must cause authentication failure."""
        key = os.urandom(32)
        ciphertext = bytearray(encrypt(b"test data", key))
        # Flip a byte in the body (after the 12-byte nonce)
        ciphertext[20] ^= 0xFF
        with pytest.raises(ValueError):
            decrypt(bytes(ciphertext), key)

    def test_short_ciphertext_raises_valueerror(self):
        """Ciphertext shorter than the nonce length must raise ValueError."""
        key = os.urandom(32)
        with pytest.raises(ValueError):
            decrypt(b"\x00" * 4, key)  # Shorter than 12-byte nonce

    def test_wrong_key_length_raises_on_encrypt(self):
        """Passing a key of wrong length to encrypt must raise ValueError."""
        short_key = os.urandom(16)  # AES-128, not AES-256
        with pytest.raises(ValueError):
            encrypt(b"test", short_key)

    def test_wrong_key_length_raises_on_decrypt(self):
        """Passing a key of wrong length to decrypt must raise ValueError."""
        short_key = os.urandom(16)
        with pytest.raises(ValueError):
            decrypt(b"\x00" * 28, short_key)  # 12 nonce + 16 body

    def test_empty_plaintext_roundtrip(self):
        """Encrypting an empty byte string must work and round-trip correctly."""
        key = os.urandom(32)
        ciphertext = encrypt(b"", key)
        assert decrypt(ciphertext, key) == b""

    def test_large_plaintext_roundtrip(self):
        """A 1 MB plaintext must round-trip correctly."""
        key = os.urandom(32)
        plaintext = os.urandom(1024 * 1024)
        ciphertext = encrypt(plaintext, key)
        assert decrypt(ciphertext, key) == plaintext


# ===========================================================================
# derive_key — PBKDF2 determinism
# ===========================================================================


class TestDeriveKey:
    def test_derive_key_is_deterministic(self):
        """Same fingerprint + salt must always produce the same key."""
        fingerprint = b"test hardware fingerprint bytes"
        salt = b"test salt value for derivation!!"
        key1 = derive_key(fingerprint, salt)
        key2 = derive_key(fingerprint, salt)
        assert key1 == key2

    def test_derive_key_different_salt_different_key(self):
        """Different salts must produce different derived keys."""
        fingerprint = b"same fingerprint"
        key1 = derive_key(fingerprint, b"salt_one_32chars_padded_to_fill!!")
        key2 = derive_key(fingerprint, b"salt_two_32chars_padded_to_fill!!")
        assert key1 != key2

    def test_derive_key_different_fingerprint_different_key(self):
        """Different hardware fingerprints must produce different derived keys."""
        salt = b"same salt 32chars padded to fill"
        key1 = derive_key(b"hardware_a_fingerprint", salt)
        key2 = derive_key(b"hardware_b_fingerprint", salt)
        assert key1 != key2

    def test_derive_key_is_32_bytes(self):
        """Derived key must be 32 bytes (AES-256)."""
        key = derive_key(b"fingerprint", b"salt_32bytes_padded_to_exactly_32")
        assert len(key) == 32

    def test_generate_salt_returns_32_bytes(self):
        """generate_salt must return 32 random bytes."""
        salt = generate_salt()
        assert len(salt) == 32
        # Should not be all zeros
        assert salt != b"\x00" * 32


# ===========================================================================
# HardwareFingerprint
# ===========================================================================


class TestHardwareFingerprint:
    def test_is_valid_with_two_identifiers(self):
        """Fingerprint with 2 of 4 identifiers must be considered valid."""
        fp = HardwareFingerprint(
            tpm_ek_hash="abc123",
            cpu_serial=None,
            board_uuid="uuid-value",
            mac_address=None,
        )
        assert fp.is_valid() is True

    def test_is_valid_with_one_identifier_false(self):
        """Fingerprint with only 1 identifier must NOT be valid."""
        fp = HardwareFingerprint(
            tpm_ek_hash="abc123",
            cpu_serial=None,
            board_uuid=None,
            mac_address=None,
        )
        assert fp.is_valid() is False

    def test_is_valid_all_four_identifiers(self):
        """All four identifiers present must be valid."""
        fp = HardwareFingerprint(
            tpm_ek_hash="tpm_hash",
            cpu_serial="cpu_serial",
            board_uuid="board_uuid",
            mac_address="00:11:22:33:44:55",
        )
        assert fp.is_valid() is True

    def test_is_valid_no_identifiers_false(self):
        """No identifiers at all must be invalid."""
        fp = HardwareFingerprint(
            tpm_ek_hash=None,
            cpu_serial=None,
            board_uuid=None,
            mac_address=None,
        )
        assert fp.is_valid() is False

    def test_sha256_fingerprint_deterministic(self):
        """Same identifiers must always hash to the same fingerprint."""
        fp = HardwareFingerprint(
            tpm_ek_hash="abc",
            cpu_serial="123",
            board_uuid="uuid1",
            mac_address="aa:bb:cc:dd:ee:ff",
        )
        h1 = fp.sha256_fingerprint()
        h2 = fp.sha256_fingerprint()
        assert h1 == h2

    def test_sha256_fingerprint_is_32_bytes(self):
        """SHA-256 fingerprint must be exactly 32 bytes."""
        fp = HardwareFingerprint(
            tpm_ek_hash="tpm",
            cpu_serial="cpu",
            board_uuid=None,
            mac_address=None,
        )
        digest = fp.sha256_fingerprint()
        assert len(digest) == 32

    def test_different_identifiers_different_fingerprint(self):
        """Different hardware must produce different fingerprints."""
        fp1 = HardwareFingerprint(tpm_ek_hash="aaa", cpu_serial="111", board_uuid=None, mac_address=None)
        fp2 = HardwareFingerprint(tpm_ek_hash="bbb", cpu_serial="222", board_uuid=None, mac_address=None)
        assert fp1.sha256_fingerprint() != fp2.sha256_fingerprint()

    def test_to_combined_string_excludes_none_values(self):
        """to_combined_string must skip None identifiers."""
        fp = HardwareFingerprint(
            tpm_ek_hash=None,
            cpu_serial="cpu_serial_value",
            board_uuid=None,
            mac_address="mac_address_value",
        )
        combined = fp.to_combined_string()
        assert "cpu:cpu_serial_value" in combined
        assert "mac:mac_address_value" in combined
        assert "tpm:" not in combined
        assert "uuid:" not in combined
