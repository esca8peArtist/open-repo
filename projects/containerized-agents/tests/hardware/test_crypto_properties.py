"""
Hardware tests: PBKDF2 key derivation determinism and AES-GCM auth tag verification.
"""
from __future__ import annotations

import os

import pytest

from security.hardware_binding.crypto import decrypt, derive_key, encrypt, generate_salt


class TestAesGcmProperties:
    """AES-256-GCM encryption/decryption property tests."""

    def test_encrypt_decrypt_roundtrip(self):
        """Encrypt then decrypt must recover original plaintext."""
        key = os.urandom(32)
        plaintext = b"agent configuration data"
        ciphertext = encrypt(plaintext, key)
        assert decrypt(ciphertext, key) == plaintext

    def test_encrypt_nonces_are_random(self):
        """Two encryptions of the same plaintext must produce different ciphertexts."""
        key = os.urandom(32)
        plaintext = b"same data"
        ct1 = encrypt(plaintext, key)
        ct2 = encrypt(plaintext, key)
        assert ct1 != ct2

    def test_wrong_key_raises_valueerror(self):
        """Decryption with a different key must raise ValueError."""
        key1 = os.urandom(32)
        key2 = os.urandom(32)
        ct = encrypt(b"secret", key1)
        with pytest.raises(ValueError):
            decrypt(ct, key2)

    def test_tampered_ciphertext_raises_valueerror(self):
        """A single flipped byte in the ciphertext must cause auth failure."""
        key = os.urandom(32)
        ct = bytearray(encrypt(b"important data", key))
        ct[20] ^= 0xFF
        with pytest.raises(ValueError):
            decrypt(bytes(ct), key)

    def test_truncated_ciphertext_raises_valueerror(self):
        """Ciphertext shorter than the nonce must raise ValueError."""
        key = os.urandom(32)
        with pytest.raises(ValueError):
            decrypt(b"\x00" * 4, key)

    def test_wrong_key_length_raises_on_encrypt(self):
        """Key not 32 bytes must raise ValueError on encrypt."""
        with pytest.raises(ValueError):
            encrypt(b"data", os.urandom(16))  # AES-128 key

    def test_wrong_key_length_raises_on_decrypt(self):
        """Key not 32 bytes must raise ValueError on decrypt."""
        with pytest.raises(ValueError):
            decrypt(b"\x00" * 28, os.urandom(16))

    def test_empty_plaintext_roundtrip(self):
        """Encrypting empty bytes must work and round-trip correctly."""
        key = os.urandom(32)
        ct = encrypt(b"", key)
        assert decrypt(ct, key) == b""

    def test_large_plaintext_roundtrip(self):
        """1 MB plaintext must round-trip correctly."""
        key = os.urandom(32)
        data = os.urandom(1024 * 1024)
        ct = encrypt(data, key)
        assert decrypt(ct, key) == data

    def test_auth_tag_prevents_bit_flipping(self):
        """Flipping bits in various positions of the ciphertext must cause failure."""
        key = os.urandom(32)
        ct = bytearray(encrypt(b"payload", key))
        # Try flipping at several positions
        for pos in [12, 13, len(ct) // 2, len(ct) - 1]:
            if pos < len(ct):
                tampered = bytearray(ct)
                tampered[pos] ^= 0x01
                with pytest.raises(ValueError):
                    decrypt(bytes(tampered), key)


class TestPbkdf2DeriveKey:
    """PBKDF2 key derivation tests."""

    def test_deterministic(self):
        """Same fingerprint + salt must always produce the same key."""
        fp = b"test hardware fingerprint"
        salt = b"test salt 32bytes padded to fill"
        k1 = derive_key(fp, salt)
        k2 = derive_key(fp, salt)
        assert k1 == k2

    def test_different_salts_produce_different_keys(self):
        """Different salts must produce different keys."""
        fp = b"same fingerprint"
        k1 = derive_key(fp, b"salt_one_32chars_padded_exactly!!")
        k2 = derive_key(fp, b"salt_two_32chars_padded_exactly!!")
        assert k1 != k2

    def test_different_fingerprints_produce_different_keys(self):
        """Different fingerprints must produce different keys."""
        salt = b"same salt padded to 32 bytes!!!!!"
        k1 = derive_key(b"hardware_A_fingerprint", salt)
        k2 = derive_key(b"hardware_B_fingerprint", salt)
        assert k1 != k2

    def test_derived_key_is_32_bytes(self):
        """Derived key must be 32 bytes (AES-256)."""
        k = derive_key(b"fp", b"salt_32bytes_padded_to_exactly_32")
        assert len(k) == 32

    def test_generate_salt_returns_32_bytes(self):
        """generate_salt must return 32 random bytes."""
        salt = generate_salt()
        assert len(salt) == 32

    def test_generate_salt_is_random(self):
        """Two generate_salt calls must return different values."""
        s1 = generate_salt()
        s2 = generate_salt()
        assert s1 != s2

    def test_derive_key_high_entropy_output(self):
        """Derived key must not be all-zeros (trivial sanity check)."""
        k = derive_key(b"test_fp", b"test_salt_32_bytes_padded_ok!!!!")
        assert k != b"\x00" * 32
