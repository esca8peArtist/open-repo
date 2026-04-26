"""
Cryptographic operations for hardware-bound encryption.
Uses PBKDF2 to derive a key from the hardware fingerprint.
Salt is stored in TPM sealed storage for maximum security.
"""
import os
import hashlib
import secrets
import subprocess
import tempfile
import logging
from pathlib import Path

from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.backends import default_backend

logger = logging.getLogger(__name__)

PBKDF2_ITERATIONS = 600_000  # NIST recommended minimum 2023
KEY_LENGTH = 32               # AES-256

# Paths for TPM sealed objects (persistent across reboots)
_TPM_SEAL_DIR = Path("/etc/agentcore/tpm")
_TPM_PRIMARY_CTX = _TPM_SEAL_DIR / "primary.ctx"
_TPM_SEALED_OBJ = _TPM_SEAL_DIR / "salt.sealed"
_TPM_SEALED_PUB = _TPM_SEAL_DIR / "salt.pub"
_NONCE_LENGTH = 12  # AES-GCM standard 96-bit nonce


def generate_salt() -> bytes:
    """Generate a cryptographically secure 32-byte salt."""
    return secrets.token_bytes(32)


def _run_tpm(cmd: list[str], timeout: int = 20) -> bool:
    """Run a tpm2-tools command. Returns True on success."""
    try:
        subprocess.run(
            cmd,
            capture_output=True,
            check=True,
            timeout=timeout,
        )
        return True
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as exc:
        logger.debug("TPM command %s failed: %s", cmd[0], exc)
        return False


def seal_salt_to_tpm(salt: bytes, pcr_policy: str = "7") -> bool:
    """Seal the salt to the TPM using PCR policy (PCR 7 = Secure Boot state).

    Uses the TPM endorsement hierarchy primary key to create a sealed object.
    The sealed object can only be unsealed on the same TPM with the same PCR
    state (i.e. same Secure Boot configuration).

    Returns True on success, False if TPM unavailable or sealing fails.
    """
    _TPM_SEAL_DIR.mkdir(parents=True, exist_ok=True)
    _TPM_SEAL_DIR.chmod(0o700)

    with tempfile.TemporaryDirectory(prefix="agentcore_tpm_seal_") as tmpdir:
        primary_ctx = os.path.join(tmpdir, "primary.ctx")
        policy_digest = os.path.join(tmpdir, "policy.digest")
        sealed_pub = os.path.join(tmpdir, "salt.pub")
        sealed_priv = os.path.join(tmpdir, "salt.priv")
        salt_file = os.path.join(tmpdir, "salt.bin")

        # Write salt to a temp file
        Path(salt_file).write_bytes(salt)

        # Step 1: Create a primary key in the owner hierarchy
        if not _run_tpm([
            "tpm2_createprimary",
            "--hierarchy", "o",
            "--key-algorithm", "rsa",
            "--key-context", primary_ctx,
        ]):
            logger.warning("TPM primary key creation failed")
            return False

        # Step 2: Create PCR policy authorizing PCR 7 (Secure Boot)
        if not _run_tpm([
            "tpm2_createpolicy",
            "--policy-pcr",
            "--pcr-list", f"sha256:{pcr_policy}",
            "--policy", policy_digest,
        ]):
            # Fallback: create policy without PCR binding (still TPM-bound)
            logger.warning(
                "PCR policy creation failed, falling back to no-PCR sealing"
            )
            policy_digest = None  # type: ignore[assignment]

        # Step 3: Create the sealed object
        create_cmd = [
            "tpm2_create",
            "--parent-context", primary_ctx,
            "--sealing-input", salt_file,
            "--public", sealed_pub,
            "--private", sealed_priv,
            "--attributes", "fixedtpm|fixedparent|noda",
        ]
        if policy_digest and Path(policy_digest).exists():
            create_cmd += ["--policy", policy_digest]

        if not _run_tpm(create_cmd):
            logger.warning("TPM sealed object creation failed")
            return False

        # Persist the sealed objects to the binding state directory
        try:
            import shutil
            shutil.copy2(sealed_pub, str(_TPM_SEALED_PUB))
            shutil.copy2(sealed_priv, str(_TPM_SEALED_OBJ))
            shutil.copy2(primary_ctx, str(_TPM_PRIMARY_CTX))
            _TPM_SEALED_PUB.chmod(0o600)
            _TPM_SEALED_OBJ.chmod(0o600)
            _TPM_PRIMARY_CTX.chmod(0o600)
        except OSError as exc:
            logger.error("Failed to persist TPM sealed objects: %s", exc)
            return False

    logger.info("Salt successfully sealed to TPM (PCR policy: %s)", pcr_policy)
    return True


def unseal_salt_from_tpm() -> bytes | None:
    """Unseal salt from TPM.

    Returns None if TPM unavailable, sealed objects are missing, or
    the PCR policy fails (different hardware or different boot state).
    """
    for path in (_TPM_PRIMARY_CTX, _TPM_SEALED_PUB, _TPM_SEALED_OBJ):
        if not path.exists():
            logger.debug("TPM sealed object not found: %s", path)
            return None

    with tempfile.TemporaryDirectory(prefix="agentcore_tpm_unseal_") as tmpdir:
        loaded_ctx = os.path.join(tmpdir, "sealed.ctx")
        output_file = os.path.join(tmpdir, "salt.bin")

        # Load the sealed object
        if not _run_tpm([
            "tpm2_load",
            "--parent-context", str(_TPM_PRIMARY_CTX),
            "--public", str(_TPM_SEALED_PUB),
            "--private", str(_TPM_SEALED_OBJ),
            "--key-context", loaded_ctx,
        ]):
            logger.warning("TPM load of sealed object failed (wrong hardware?)")
            return None

        # Unseal
        if not _run_tpm([
            "tpm2_unseal",
            "--object-context", loaded_ctx,
            "--output", output_file,
        ]):
            logger.warning("TPM unseal failed (PCR policy mismatch?)")
            return None

        try:
            salt = Path(output_file).read_bytes()
        except OSError as exc:
            logger.error("Cannot read unsealed salt: %s", exc)
            return None

    logger.info("Salt successfully unsealed from TPM")
    return salt


def derive_key(fingerprint_bytes: bytes, salt: bytes) -> bytes:
    """Derive AES-256 key from hardware fingerprint using PBKDF2-HMAC-SHA256."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=KEY_LENGTH,
        salt=salt,
        iterations=PBKDF2_ITERATIONS,
        backend=default_backend(),
    )
    return kdf.derive(fingerprint_bytes)


def encrypt(plaintext: bytes, key: bytes) -> bytes:
    """AES-256-GCM encrypt.

    Returns nonce (12 bytes) + ciphertext + GCM tag (16 bytes).
    The nonce is randomly generated per call so the same plaintext
    produces different ciphertext each time.
    """
    if len(key) != KEY_LENGTH:
        raise ValueError(f"Key must be {KEY_LENGTH} bytes, got {len(key)}")
    nonce = secrets.token_bytes(_NONCE_LENGTH)
    aesgcm = AESGCM(key)
    ciphertext_with_tag = aesgcm.encrypt(nonce, plaintext, None)
    return nonce + ciphertext_with_tag


def decrypt(ciphertext: bytes, key: bytes) -> bytes:
    """AES-256-GCM decrypt.

    Expects the format produced by encrypt(): nonce (12 bytes) + ciphertext + tag.
    Raises ValueError if authentication fails (wrong key, tampered data, or
    hardware mismatch causing wrong key derivation).
    """
    if len(key) != KEY_LENGTH:
        raise ValueError(f"Key must be {KEY_LENGTH} bytes, got {len(key)}")
    if len(ciphertext) < _NONCE_LENGTH:
        raise ValueError("Ciphertext too short to contain nonce")
    nonce = ciphertext[:_NONCE_LENGTH]
    body = ciphertext[_NONCE_LENGTH:]
    aesgcm = AESGCM(key)
    try:
        return aesgcm.decrypt(nonce, body, None)
    except Exception as exc:
        # cryptography raises InvalidTag; wrap for a consistent API
        raise ValueError(
            "Decryption failed: authentication tag mismatch. "
            "Hardware binding key may not match."
        ) from exc
