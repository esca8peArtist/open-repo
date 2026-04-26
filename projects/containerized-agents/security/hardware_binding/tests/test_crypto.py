"""Tests for the crypto module (key derivation and AES-GCM encryption)."""
import os
import pytest
from ..crypto import (
    generate_salt,
    derive_key,
    encrypt,
    decrypt,
    PBKDF2_ITERATIONS,
    KEY_LENGTH,
)


# ---------------------------------------------------------------------------
# generate_salt
# ---------------------------------------------------------------------------

class TestGenerateSalt:
    def test_returns_32_bytes(self):
        salt = generate_salt()
        assert isinstance(salt, bytes)
        assert len(salt) == 32

    def test_two_salts_are_different(self):
        """Salts must be unique — collision would be astronomically unlikely."""
        assert generate_salt() != generate_salt()


# ---------------------------------------------------------------------------
# derive_key
# ---------------------------------------------------------------------------

class TestDeriveKey:
    def _fingerprint(self) -> bytes:
        return b"\xde\xad\xbe\xef" * 8  # 32 bytes

    def _salt(self) -> bytes:
        return b"\xca\xfe\xba\xbe" * 8  # 32 bytes

    def test_returns_32_byte_key(self):
        key = derive_key(self._fingerprint(), self._salt())
        assert isinstance(key, bytes)
        assert len(key) == KEY_LENGTH  # 32 bytes = AES-256

    def test_derivation_is_deterministic(self):
        """Same fingerprint + salt must always produce the same key."""
        key1 = derive_key(self._fingerprint(), self._salt())
        key2 = derive_key(self._fingerprint(), self._salt())
        assert key1 == key2

    def test_different_fingerprints_produce_different_keys(self):
        salt = self._salt()
        key1 = derive_key(b"hardware_A" * 3, salt)
        key2 = derive_key(b"hardware_B" * 3, salt)
        assert key1 != key2

    def test_different_salts_produce_different_keys(self):
        fp = self._fingerprint()
        key1 = derive_key(fp, b"salt_one" * 4)
        key2 = derive_key(fp, b"salt_two" * 4)
        assert key1 != key2

    def test_uses_correct_iterations(self):
        """PBKDF2_ITERATIONS should meet NIST 2023 minimum of 600,000."""
        assert PBKDF2_ITERATIONS >= 600_000


# ---------------------------------------------------------------------------
# encrypt / decrypt round-trip
# ---------------------------------------------------------------------------

class TestEncryptDecrypt:
    def _key(self) -> bytes:
        return os.urandom(KEY_LENGTH)

    def test_encrypt_returns_bytes(self):
        key = self._key()
        ciphertext = encrypt(b"hello world", key)
        assert isinstance(ciphertext, bytes)

    def test_encrypt_output_longer_than_plaintext(self):
        """nonce (12) + ciphertext + tag (16) > plaintext."""
        key = self._key()
        plaintext = b"short"
        ciphertext = encrypt(plaintext, key)
        # nonce=12 + len(plaintext) + tag=16
        assert len(ciphertext) == 12 + len(plaintext) + 16

    def test_round_trip(self):
        key = self._key()
        plaintext = b"This is a secret system prompt."
        ciphertext = encrypt(plaintext, key)
        recovered = decrypt(ciphertext, key)
        assert recovered == plaintext

    def test_round_trip_empty_plaintext(self):
        key = self._key()
        ciphertext = encrypt(b"", key)
        assert decrypt(ciphertext, key) == b""

    def test_round_trip_large_plaintext(self):
        key = self._key()
        plaintext = os.urandom(100_000)
        assert decrypt(encrypt(plaintext, key), key) == plaintext

    def test_different_encryptions_of_same_plaintext_differ(self):
        """Each call generates a fresh random nonce, so output must differ."""
        key = self._key()
        plaintext = b"same content"
        c1 = encrypt(plaintext, key)
        c2 = encrypt(plaintext, key)
        assert c1 != c2

    def test_wrong_key_raises_value_error(self):
        key1 = self._key()
        key2 = self._key()
        ciphertext = encrypt(b"secret", key1)
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt(ciphertext, key2)

    def test_tampered_ciphertext_raises_value_error(self):
        key = self._key()
        ciphertext = bytearray(encrypt(b"secret data", key))
        # Flip a bit in the ciphertext body (after the 12-byte nonce)
        ciphertext[20] ^= 0xFF
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt(bytes(ciphertext), key)

    def test_tampered_nonce_raises_value_error(self):
        key = self._key()
        ciphertext = bytearray(encrypt(b"secret data", key))
        # Flip a bit in the nonce
        ciphertext[0] ^= 0x01
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt(bytes(ciphertext), key)

    def test_tampered_tag_raises_value_error(self):
        key = self._key()
        ciphertext = bytearray(encrypt(b"secret", key))
        # Flip the last byte (part of the GCM tag)
        ciphertext[-1] ^= 0xFF
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt(bytes(ciphertext), key)

    def test_truncated_ciphertext_raises_value_error(self):
        key = self._key()
        # Only provide 5 bytes — shorter than the 12-byte nonce
        with pytest.raises(ValueError):
            decrypt(b"\x00" * 5, key)

    def test_encrypt_rejects_wrong_key_length(self):
        with pytest.raises(ValueError):
            encrypt(b"data", b"tooshortkey")

    def test_decrypt_rejects_wrong_key_length(self):
        with pytest.raises(ValueError):
            decrypt(b"\x00" * 40, b"tooshortkey")


# ---------------------------------------------------------------------------
# Key derivation + encrypt/decrypt integration
# ---------------------------------------------------------------------------

class TestKeyDerivationWithEncryption:
    def test_derived_key_can_encrypt_and_decrypt(self):
        fingerprint = b"hardware_fingerprint_sha256_32_byte"[:32]
        salt = generate_salt()
        key = derive_key(fingerprint, salt)

        plaintext = b'{"system_prompt": "You are a helpful assistant.", "api_key": "sk-secret"}'
        ciphertext = encrypt(plaintext, key)
        recovered = decrypt(ciphertext, key)
        assert recovered == plaintext

    def test_different_hardware_cannot_decrypt(self):
        """Simulates image copied to different hardware: new fingerprint → new key → decrypt fails."""
        salt = generate_salt()

        original_hardware = b"original_machine_fingerprint___"
        other_hardware = b"attacker_machine_fingerprint___"

        original_key = derive_key(original_hardware, salt)
        other_key = derive_key(other_hardware, salt)

        ciphertext = encrypt(b"sensitive config data", original_key)
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt(ciphertext, other_key)

    def test_different_salt_cannot_decrypt(self):
        """Simulates losing TPM-sealed salt: same fingerprint + different salt → different key."""
        fingerprint = b"stable_hardware_fingerprint_____"
        salt1 = generate_salt()
        salt2 = generate_salt()

        key1 = derive_key(fingerprint, salt1)
        key2 = derive_key(fingerprint, salt2)

        ciphertext = encrypt(b"sensitive data", key1)
        with pytest.raises(ValueError, match="Decryption failed"):
            decrypt(ciphertext, key2)
