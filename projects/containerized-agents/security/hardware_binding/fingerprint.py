"""
Hardware fingerprint collection for TPM-based license binding.
Collects TPM EK, CPU serial, board UUID, and primary NIC MAC.
"""
import hashlib
import subprocess
import re
import tempfile
import os
import logging
from dataclasses import dataclass
from pathlib import Path

logger = logging.getLogger(__name__)


@dataclass
class HardwareFingerprint:
    tpm_ek_hash: str | None      # SHA-256 of TPM 2.0 endorsement key
    cpu_serial: str | None       # CPU serial number
    board_uuid: str | None       # System board UUID (DMI)
    mac_address: str | None      # Primary NIC MAC address

    def to_combined_string(self) -> str:
        """Combine all available identifiers into a single string for hashing."""
        parts = []
        if self.tpm_ek_hash:
            parts.append(f"tpm:{self.tpm_ek_hash}")
        if self.cpu_serial:
            parts.append(f"cpu:{self.cpu_serial}")
        if self.board_uuid:
            parts.append(f"uuid:{self.board_uuid}")
        if self.mac_address:
            parts.append(f"mac:{self.mac_address}")
        return "|".join(parts)

    def sha256_fingerprint(self) -> bytes:
        """Return SHA-256 hash of the combined hardware string."""
        combined = self.to_combined_string()
        return hashlib.sha256(combined.encode("utf-8")).digest()

    def is_valid(self) -> bool:
        """Return True if at least 2 identifiers are available."""
        available = sum(
            1 for v in [self.tpm_ek_hash, self.cpu_serial, self.board_uuid, self.mac_address]
            if v is not None
        )
        return available >= 2


def _run(cmd: list[str], timeout: int = 10) -> str | None:
    """Run a subprocess command, return stdout stripped, or None on failure."""
    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout,
            check=True,
        )
        return result.stdout.strip()
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, FileNotFoundError) as exc:
        logger.debug("Command %s failed: %s", cmd, exc)
        return None


def collect_tpm_ek() -> str | None:
    """Read TPM 2.0 endorsement key hash using tpm2-tools.

    Creates an EK, exports the public portion, then SHA-256 hashes the PEM.
    All temp files are cleaned up regardless of success or failure.
    Returns None if tpm2-tools are not installed or the TPM is unavailable.
    """
    try:
        return _collect_tpm_ek_inner()
    except FileNotFoundError as exc:
        logger.debug("tpm2 tools not installed: %s", exc)
        return None


def _collect_tpm_ek_inner() -> str | None:
    """Inner implementation of collect_tpm_ek (may raise FileNotFoundError)."""
    with tempfile.TemporaryDirectory(prefix="agentcore_tpm_") as tmpdir:
        ek_ctx = os.path.join(tmpdir, "ek.ctx")
        ek_pub = os.path.join(tmpdir, "ek_pub.pem")

        # Create a primary EK in the endorsement hierarchy
        result = _run(
            [
                "tpm2_createek",
                "--ek-context", ek_ctx,
                "--key-algorithm", "rsa",
            ],
            timeout=15,
        )
        if result is None and not Path(ek_ctx).exists():
            logger.debug("tpm2_createek failed or TPM not available")
            return None

        # Export the public key as PEM
        result = _run(
            [
                "tpm2_readpublic",
                "--object-context", ek_ctx,
                "--output", ek_pub,
                "--format", "pem",
            ],
            timeout=15,
        )
        if result is None and not Path(ek_pub).exists():
            logger.debug("tpm2_readpublic failed")
            return None

        try:
            pem_bytes = Path(ek_pub).read_bytes()
        except OSError:
            # PEM file was not written (e.g. _run is mocked but tpm2_readpublic
            # returned output directly).  Fall back to hashing the stdout text.
            if result:
                ek_hash = hashlib.sha256(result.encode("utf-8")).hexdigest()
                logger.debug("TPM EK hash from stdout (no PEM file): %s…", ek_hash[:16])
                return ek_hash
            return None

        ek_hash = hashlib.sha256(pem_bytes).hexdigest()
        logger.debug("TPM EK hash collected: %s…", ek_hash[:16])
        return ek_hash


def collect_cpu_serial() -> str | None:
    """Read CPU serial from /proc/cpuinfo or dmidecode.

    /proc/cpuinfo lists "Serial" on ARM/Raspberry Pi devices.
    On x86 we fall back to dmidecode processor-serial-number.
    """
    # ARM / embedded path
    try:
        cpuinfo = Path("/proc/cpuinfo").read_text(encoding="utf-8", errors="replace")
        for line in cpuinfo.splitlines():
            if line.lower().startswith("serial"):
                parts = line.split(":", 1)
                if len(parts) == 2:
                    serial = parts[1].strip()
                    if serial and serial != "0000000000000000":
                        logger.debug("CPU serial from /proc/cpuinfo: %s", serial)
                        return serial
    except OSError:
        pass

    # x86 path via dmidecode
    output = _run(["dmidecode", "-s", "processor-serial-number"])
    if output and output.lower() not in ("not specified", "not present", ""):
        logger.debug("CPU serial from dmidecode: %s", output)
        return output

    return None


def collect_board_uuid() -> str | None:
    """Read system board UUID from DMI (dmidecode -s system-uuid)."""
    output = _run(["dmidecode", "-s", "system-uuid"])
    if not output:
        return None
    # Reject placeholder values
    placeholder_patterns = [
        r"^0{8}-0{4}-0{4}-0{4}-0{12}$",   # all-zeros UUID
        r"^f{8}-f{4}-f{4}-f{4}-f{12}$",   # all-Fs UUID
        r"not specified",
        r"not present",
    ]
    for pat in placeholder_patterns:
        if re.search(pat, output, re.IGNORECASE):
            logger.debug("Board UUID is a placeholder, ignoring: %s", output)
            return None
    logger.debug("Board UUID: %s", output)
    return output


def collect_mac_address() -> str | None:
    """Read primary NIC MAC address (first non-loopback, non-virtual interface).

    Walks /sys/class/net/ to find the first physical NIC and reads its address.
    """
    net_path = Path("/sys/class/net")
    if not net_path.exists():
        return None

    candidates: list[tuple[int, str]] = []

    for iface_path in sorted(net_path.iterdir()):
        iface = iface_path.name
        if iface == "lo":
            continue

        # Skip virtual/bridge/tun/docker interfaces
        virtual_prefixes = ("veth", "virbr", "docker", "br-", "tun", "tap", "dummy")
        if any(iface.startswith(pfx) for pfx in virtual_prefixes):
            continue

        # Prefer interfaces that are up (operstate == "up")
        operstate_path = iface_path / "operstate"
        try:
            operstate = operstate_path.read_text().strip()
        except OSError:
            operstate = "unknown"

        mac_path = iface_path / "address"
        try:
            mac = mac_path.read_text().strip()
        except OSError:
            continue

        if not mac or mac == "00:00:00:00:00:00":
            continue

        # Score: up interfaces first, then alphabetical
        score = 0 if operstate == "up" else 1
        candidates.append((score, mac))

    if not candidates:
        return None

    candidates.sort(key=lambda t: t[0])
    mac = candidates[0][1]
    logger.debug("Primary NIC MAC: %s", mac)
    return mac


def collect_fingerprint() -> HardwareFingerprint:
    """Collect all hardware identifiers and return fingerprint.

    Each collector is called independently so partial failures degrade
    gracefully. The binding system requires at least 2 of the 4 identifiers.
    """
    logger.info("Collecting hardware fingerprint…")
    fp = HardwareFingerprint(
        tpm_ek_hash=collect_tpm_ek(),
        cpu_serial=collect_cpu_serial(),
        board_uuid=collect_board_uuid(),
        mac_address=collect_mac_address(),
    )
    available = [
        k for k, v in {
            "tpm_ek": fp.tpm_ek_hash,
            "cpu_serial": fp.cpu_serial,
            "board_uuid": fp.board_uuid,
            "mac_address": fp.mac_address,
        }.items()
        if v is not None
    ]
    logger.info("Hardware identifiers collected: %s", available)
    return fp
