"""
Hardware binding orchestration.
Ties together fingerprinting, TPM sealing, and config encryption.
"""
import json
import logging
import os
from pathlib import Path

from .fingerprint import collect_fingerprint
from .crypto import (
    generate_salt,
    seal_salt_to_tpm,
    unseal_salt_from_tpm,
    derive_key,
    encrypt,
    decrypt,
)

logger = logging.getLogger(__name__)

BINDING_STATE_PATH = Path("/etc/agentcore/binding.json")
_BINDING_STATE_DIR = BINDING_STATE_PATH.parent


class BindingError(Exception):
    """Raised when hardware binding verification fails."""
    pass


def _load_binding_state() -> dict:
    """Load the binding state JSON. Raises BindingError if missing or corrupt."""
    if not BINDING_STATE_PATH.exists():
        raise BindingError(
            f"Binding state not found at {BINDING_STATE_PATH}. "
            "Run 'agentcore-binding init' to initialize hardware binding."
        )
    try:
        return json.loads(BINDING_STATE_PATH.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError) as exc:
        raise BindingError(f"Cannot read binding state: {exc}") from exc


def _save_binding_state(state: dict) -> None:
    """Persist binding state to disk with restricted permissions."""
    _BINDING_STATE_DIR.mkdir(parents=True, exist_ok=True)
    _BINDING_STATE_DIR.chmod(0o700)
    tmp_path = BINDING_STATE_PATH.with_suffix(".json.tmp")
    tmp_path.write_text(json.dumps(state, indent=2), encoding="utf-8")
    tmp_path.chmod(0o600)
    tmp_path.rename(BINDING_STATE_PATH)
    logger.debug("Binding state written to %s", BINDING_STATE_PATH)


def _get_derived_key() -> bytes:
    """Reconstruct the hardware-derived AES key.

    1. Collect current hardware fingerprint.
    2. Unseal salt from TPM.
    3. Derive key via PBKDF2.
    Raises BindingError on any failure.
    """
    fp = collect_fingerprint()
    if not fp.is_valid():
        raise BindingError(
            "Insufficient hardware identifiers collected. "
            "At least 2 of TPM EK, CPU serial, board UUID, and MAC address are required."
        )

    salt = unseal_salt_from_tpm()
    if salt is None:
        raise BindingError(
            "Cannot unseal salt from TPM. This machine may not be the licensed hardware, "
            "or the TPM may be unavailable / in a different boot state."
        )

    key = derive_key(fp.sha256_fingerprint(), salt)
    logger.debug("Hardware-derived key reconstructed successfully")
    return key


def initialize_binding() -> bool:
    """First-boot: collect fingerprint, generate+seal salt, write binding state.

    Steps:
    1. Collect hardware fingerprint.
    2. Validate at least 2 identifiers are present.
    3. Generate random salt.
    4. Seal salt to TPM.
    5. Derive key from fingerprint + salt.
    6. Write binding state (fingerprint hex, sealed object references).

    Returns True on success. Called by the setup wizard at step 10.
    """
    logger.info("Initializing hardware binding…")

    if BINDING_STATE_PATH.exists():
        logger.warning(
            "Binding state already exists at %s. "
            "Re-initializing will invalidate previously encrypted configs.",
            BINDING_STATE_PATH,
        )

    fp = collect_fingerprint()
    if not fp.is_valid():
        logger.error(
            "Cannot initialize binding: insufficient hardware identifiers. "
            "Got: tpm=%s cpu=%s uuid=%s mac=%s",
            bool(fp.tpm_ek_hash),
            bool(fp.cpu_serial),
            bool(fp.board_uuid),
            bool(fp.mac_address),
        )
        return False

    fingerprint_hex = fp.sha256_fingerprint().hex()
    logger.info("Hardware fingerprint: %s…", fingerprint_hex[:16])

    salt = generate_salt()

    if not seal_salt_to_tpm(salt):
        logger.error("Failed to seal salt to TPM. Hardware binding aborted.")
        return False

    state = {
        "version": 1,
        "fingerprint_hex": fingerprint_hex,
        "identifiers": {
            "has_tpm_ek": fp.tpm_ek_hash is not None,
            "has_cpu_serial": fp.cpu_serial is not None,
            "has_board_uuid": fp.board_uuid is not None,
            "has_mac_address": fp.mac_address is not None,
        },
        "tpm_sealed": True,
    }
    _save_binding_state(state)
    logger.info("Hardware binding initialized successfully")
    return True


def verify_binding() -> bool:
    """Every boot: verify hardware matches binding.

    Attempts to reconstruct the derived key by re-collecting the hardware
    fingerprint and unsealing the salt from TPM. Returns True only if both
    succeed and the current fingerprint matches the stored one.

    Called at agentcore.service startup.
    """
    logger.info("Verifying hardware binding…")
    try:
        state = _load_binding_state()
    except BindingError as exc:
        logger.error("Binding verification failed: %s", exc)
        return False

    stored_fingerprint = state.get("fingerprint_hex")
    if not stored_fingerprint:
        logger.error("Binding state is missing fingerprint_hex")
        return False

    fp = collect_fingerprint()
    if not fp.is_valid():
        logger.error("Hardware fingerprint collection returned insufficient identifiers")
        return False

    current_fingerprint = fp.sha256_fingerprint().hex()
    if current_fingerprint != stored_fingerprint:
        logger.error(
            "Hardware fingerprint mismatch! "
            "Stored: %s… Current: %s…",
            stored_fingerprint[:16],
            current_fingerprint[:16],
        )
        return False

    # Try to unseal the salt — this will fail on different hardware
    salt = unseal_salt_from_tpm()
    if salt is None:
        logger.error(
            "TPM unseal failed. This is not the licensed hardware or TPM state changed."
        )
        return False

    logger.info("Hardware binding verified successfully")
    return True


def encrypt_config(config_dict: dict) -> bytes:
    """Encrypt a config dict using the hardware-derived key.

    Raises BindingError if the hardware binding cannot be resolved
    (e.g. TPM unavailable, insufficient identifiers).
    """
    try:
        key = _get_derived_key()
    except BindingError:
        raise

    plaintext = json.dumps(config_dict, ensure_ascii=False).encode("utf-8")
    ciphertext = encrypt(plaintext, key)
    logger.debug("Config encrypted (%d bytes → %d bytes)", len(plaintext), len(ciphertext))
    return ciphertext


def decrypt_config(encrypted: bytes) -> dict:
    """Decrypt config. Raises BindingError if hardware mismatch.

    Decryption will fail with a ValueError from the crypto layer if the key
    does not match (wrong hardware, tampered ciphertext). This is re-raised
    as a BindingError for consistent error handling in callers.
    """
    try:
        key = _get_derived_key()
    except BindingError:
        raise

    try:
        plaintext = decrypt(encrypted, key)
    except ValueError as exc:
        raise BindingError(
            "Config decryption failed. Hardware may not match the licensed machine."
        ) from exc

    try:
        return json.loads(plaintext.decode("utf-8"))
    except (json.JSONDecodeError, UnicodeDecodeError) as exc:
        raise BindingError(f"Decrypted data is not valid JSON: {exc}") from exc
