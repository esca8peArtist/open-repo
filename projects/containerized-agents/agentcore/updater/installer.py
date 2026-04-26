"""
Update installer — downloads and applies a verified update.
Verifies SHA256 before applying.
Keeps previous version for 24h rollback window.
Restarts services gracefully.
"""
import asyncio
import hashlib
import json
import logging
import os
import shutil
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Callable, Awaitable

import httpx

from .update_checker import UpdateInfo

logger = logging.getLogger(__name__)

# Where downloaded artifacts are staged before being applied
_STAGING_DIR = Path(os.environ.get("AGENTCORE_UPDATE_STAGING", "/var/lib/agentcore/updates/staging"))

# Where the previous version is kept for rollback
_ROLLBACK_DIR = Path(os.environ.get("AGENTCORE_ROLLBACK_DIR", "/var/lib/agentcore/updates/rollback"))

# Path to the docker-compose file
_COMPOSE_FILE = Path(os.environ.get("AGENTCORE_COMPOSE_FILE", "/opt/agentcore/docker-compose.yml"))

# Rollback TTL in hours
_ROLLBACK_TTL_HOURS = 24

# Health check endpoint (must return 200 after update)
_HEALTH_URL = "http://localhost:8080/api/health"
_HEALTH_TIMEOUT = 60  # seconds to wait for services to come up after restart

# Progress callback type
ProgressCallback = Callable[[str, float], Awaitable[None]] | None


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

async def download_component(url: str, expected_sha256: str, dest: Path) -> bool:
    """Download with progress tracking. Verify SHA256. Returns False if mismatch.

    Downloads to dest.tmp then renames to dest on success, so dest is never
    left in a partially-written state.
    """
    dest.parent.mkdir(parents=True, exist_ok=True)
    tmp_path = dest.with_suffix(dest.suffix + ".tmp")

    try:
        async with httpx.AsyncClient(timeout=None, follow_redirects=True) as client:
            async with client.stream("GET", url) as response:
                response.raise_for_status()
                total = int(response.headers.get("content-length", 0))
                downloaded = 0
                h = hashlib.sha256()

                with tmp_path.open("wb") as fh:
                    async for chunk in response.aiter_bytes(chunk_size=1 << 20):  # 1 MB
                        fh.write(chunk)
                        h.update(chunk)
                        downloaded += len(chunk)
                        if total:
                            pct = downloaded / total * 100
                            logger.debug("Download %s: %.1f%%", dest.name, pct)
    except Exception as exc:
        logger.error("Download failed for %s: %s", url, exc)
        _safe_remove(tmp_path)
        return False

    # Verify SHA-256
    actual_sha256 = h.hexdigest()
    if actual_sha256 != expected_sha256.lower():
        logger.error(
            "SHA-256 mismatch for %s: expected %s, got %s",
            dest.name, expected_sha256, actual_sha256,
        )
        _safe_remove(tmp_path)
        return False

    tmp_path.rename(dest)
    logger.info("Downloaded and verified: %s (sha256=%s)", dest.name, actual_sha256[:16])
    return True


async def apply_update(
    update: UpdateInfo,
    progress_callback: ProgressCallback = None,
) -> bool:
    """
    Apply update:
    1. Download all components (with SHA256 verification)
    2. Save current version to rollback directory
    3. Apply new images via docker compose pull + up
    4. Verify new version is running (health check)
    5. Return True on success
    """
    if not update.available:
        logger.warning("apply_update called with no available update.")
        return False

    await _progress(progress_callback, "Preparing update staging area...", 0.0)
    _STAGING_DIR.mkdir(parents=True, exist_ok=True)

    # --- Step 1: Download all components ---
    components = [c for c in update.components if c.get("type") in ("agentcore", "wizard")]
    total_components = len(components)
    if total_components == 0:
        logger.warning("No downloadable components in update.")
        return False

    downloaded_paths: list[tuple[dict, Path]] = []
    for idx, comp in enumerate(components):
        comp_type = comp["type"]
        url = comp.get("image_url", comp.get("download_url", ""))
        expected_sha256 = comp["sha256"]
        filename = _url_basename(url) or f"{comp_type}-{update.latest_version}.tar.gz"
        dest = _STAGING_DIR / filename

        progress_pct = (idx / total_components) * 0.6  # downloads = 0–60%
        await _progress(progress_callback, f"Downloading {comp_type} ({idx+1}/{total_components})...", progress_pct)

        ok = await download_component(url, expected_sha256, dest)
        if not ok:
            logger.error("Download/verification failed for component: %s", comp_type)
            await _progress(progress_callback, f"Download failed for {comp_type}.", progress_pct)
            _cleanup_staging()
            return False

        downloaded_paths.append((comp, dest))

    # --- Step 2: Save current state for rollback ---
    await _progress(progress_callback, "Saving current version for rollback...", 0.62)
    try:
        _save_rollback_state(update.current_version)
    except Exception as exc:
        logger.error("Failed to save rollback state: %s", exc)
        # Non-fatal — proceed but warn
        logger.warning("Update will proceed without rollback capability.")

    # --- Step 3: Load new images into Docker ---
    await _progress(progress_callback, "Loading new container images...", 0.70)
    for comp, image_path in downloaded_paths:
        docker_tag = comp.get("docker_tag", "")
        ok = await _docker_load_image(image_path, docker_tag)
        if not ok:
            logger.error("docker load failed for %s", image_path.name)
            await _progress(progress_callback, f"Failed to load {image_path.name}.", 0.70)
            return False

    # --- Step 4: docker compose up ---
    await _progress(progress_callback, "Restarting services...", 0.85)
    ok = await _docker_compose_up()
    if not ok:
        logger.error("docker compose up failed — attempting rollback.")
        await _progress(progress_callback, "Service restart failed. Rolling back...", 0.87)
        await rollback()
        return False

    # --- Step 5: Health check ---
    await _progress(progress_callback, "Verifying new version is healthy...", 0.92)
    healthy = await _wait_for_health(timeout=_HEALTH_TIMEOUT)
    if not healthy:
        logger.error("Health check failed after update — rolling back.")
        await _progress(progress_callback, "Health check failed. Rolling back...", 0.95)
        await rollback()
        return False

    # Cleanup staging
    _cleanup_staging()
    await _progress(progress_callback, f"Update to {update.latest_version} complete.", 1.0)
    logger.info("Update to %s applied successfully.", update.latest_version)
    return True


async def rollback() -> bool:
    """Restore previous version from rollback directory."""
    rollback_meta_path = _ROLLBACK_DIR / "rollback_meta.json"
    if not rollback_meta_path.exists():
        logger.error("No rollback state found at %s", _ROLLBACK_DIR)
        return False

    try:
        meta = json.loads(rollback_meta_path.read_text(encoding="utf-8"))
    except Exception as exc:
        logger.error("Cannot read rollback metadata: %s", exc)
        return False

    saved_at = meta.get("saved_at", "")
    prev_version = meta.get("version", "unknown")

    # Check rollback TTL
    if saved_at:
        try:
            saved_dt = datetime.fromisoformat(saved_at)
            age_hours = (datetime.now(tz=timezone.utc) - saved_dt).total_seconds() / 3600
            if age_hours > _ROLLBACK_TTL_HOURS:
                logger.error(
                    "Rollback state is %.1f hours old (TTL is %dh). Cannot rollback.",
                    age_hours, _ROLLBACK_TTL_HOURS,
                )
                return False
        except Exception:
            pass  # Cannot parse timestamp — proceed anyway

    logger.info("Rolling back to version %s...", prev_version)

    # Load previous images
    image_files = list((_ROLLBACK_DIR / "images").glob("*.tar.gz"))
    if not image_files:
        logger.error("No saved images in rollback directory.")
        return False

    for image_path in image_files:
        ok = await _docker_load_image(image_path, docker_tag=None)
        if not ok:
            logger.error("docker load failed for rollback image %s", image_path.name)
            return False

    # Restart with previous images
    ok = await _docker_compose_up()
    if not ok:
        logger.error("docker compose up failed during rollback.")
        return False

    healthy = await _wait_for_health(timeout=_HEALTH_TIMEOUT)
    if not healthy:
        logger.error("Health check failed after rollback. Manual intervention required.")
        return False

    logger.info("Rollback to %s successful.", prev_version)
    return True


# ---------------------------------------------------------------------------
# Internal helpers
# ---------------------------------------------------------------------------

async def _progress(callback: ProgressCallback, message: str, pct: float) -> None:
    """Fire progress callback if provided. Always logs."""
    logger.info("[%.0f%%] %s", pct * 100, message)
    if callback is not None:
        try:
            await callback(message, pct)
        except Exception:
            pass  # Progress reporting failure is never fatal


def _save_rollback_state(current_version: str) -> None:
    """Export currently-running Docker images to the rollback directory."""
    rollback_images_dir = _ROLLBACK_DIR / "images"
    rollback_images_dir.mkdir(parents=True, exist_ok=True)

    # Export running agentcore and wizard images
    for service in ("agentcore", "agentcore-wizard"):
        image_tag = _get_running_image_tag(service)
        if not image_tag:
            logger.warning("Could not determine running image for service %s — skipping rollback save", service)
            continue
        output_path = rollback_images_dir / f"{service}-rollback.tar.gz"
        try:
            result = subprocess.run(
                ["docker", "save", image_tag, "-o", str(output_path)],
                capture_output=True, text=True, timeout=300,
            )
            if result.returncode != 0:
                logger.warning("docker save %s failed: %s", image_tag, result.stderr)
        except Exception as exc:
            logger.warning("docker save raised for %s: %s", service, exc)

    # Write metadata
    meta = {
        "version": current_version,
        "saved_at": datetime.now(tz=timezone.utc).isoformat(),
        "expires_at": "",  # informational only
    }
    (_ROLLBACK_DIR / "rollback_meta.json").write_text(
        json.dumps(meta, indent=2), encoding="utf-8"
    )
    logger.info("Rollback state saved for version %s", current_version)


def _get_running_image_tag(service_name: str) -> str | None:
    """Get the Docker image tag currently used by a compose service."""
    try:
        result = subprocess.run(
            ["docker", "compose", "-f", str(_COMPOSE_FILE), "images", "--format", "json"],
            capture_output=True, text=True, timeout=15,
        )
        if result.returncode == 0:
            images = json.loads(result.stdout)
            for img in images:
                if img.get("Service") == service_name:
                    repo = img.get("Repository", "")
                    tag = img.get("Tag", "")
                    return f"{repo}:{tag}" if repo and tag else None
    except Exception as exc:
        logger.debug("Could not get running image tag for %s: %s", service_name, exc)
    return None


async def _docker_load_image(image_path: Path, docker_tag: str | None) -> bool:
    """Load a Docker image tar.gz file. Returns True on success."""
    cmd = ["docker", "load", "-i", str(image_path)]
    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=600)
        if proc.returncode != 0:
            logger.error("docker load failed: %s", stderr.decode())
            return False
        logger.info("docker load: %s", stdout.decode().strip())

        # Tag the image if a specific tag was requested
        if docker_tag:
            # docker load prints "Loaded image: <tag>" — parse it
            loaded_line = stdout.decode().strip()
            if "Loaded image:" in loaded_line:
                loaded_tag = loaded_line.split("Loaded image:", 1)[1].strip()
                if loaded_tag != docker_tag:
                    tag_proc = await asyncio.create_subprocess_exec(
                        "docker", "tag", loaded_tag, docker_tag,
                        stdout=asyncio.subprocess.PIPE,
                        stderr=asyncio.subprocess.PIPE,
                    )
                    await tag_proc.communicate()
        return True
    except asyncio.TimeoutError:
        logger.error("docker load timed out for %s", image_path.name)
        return False
    except Exception as exc:
        logger.error("docker load raised: %s", exc)
        return False


async def _docker_compose_up() -> bool:
    """Run docker compose up --detach. Returns True on success."""
    if not _COMPOSE_FILE.exists():
        logger.error("docker-compose file not found: %s", _COMPOSE_FILE)
        return False

    cmd = ["docker", "compose", "-f", str(_COMPOSE_FILE), "up", "--detach", "--remove-orphans"]
    try:
        proc = await asyncio.create_subprocess_exec(
            *cmd,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        stdout, stderr = await asyncio.wait_for(proc.communicate(), timeout=300)
        if proc.returncode != 0:
            logger.error("docker compose up failed:\n%s", stderr.decode())
            return False
        logger.info("docker compose up OK.")
        return True
    except asyncio.TimeoutError:
        logger.error("docker compose up timed out.")
        return False
    except Exception as exc:
        logger.error("docker compose up raised: %s", exc)
        return False


async def _wait_for_health(timeout: int = 60) -> bool:
    """Poll the health endpoint until it returns 200 or timeout is exceeded."""
    import httpx
    loop = asyncio.get_running_loop()
    deadline = loop.time() + timeout
    while loop.time() < deadline:
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                response = await client.get(_HEALTH_URL)
                if response.status_code == 200:
                    logger.info("Health check passed.")
                    return True
        except Exception:
            pass  # Not up yet
        await asyncio.sleep(3)
    logger.error("Health check timed out after %ds.", timeout)
    return False


def _cleanup_staging() -> None:
    """Remove all files in the staging directory."""
    try:
        if _STAGING_DIR.exists():
            shutil.rmtree(_STAGING_DIR)
            _STAGING_DIR.mkdir(parents=True, exist_ok=True)
    except Exception as exc:
        logger.warning("Staging cleanup failed (non-fatal): %s", exc)


def _safe_remove(path: Path) -> None:
    try:
        if path.exists():
            path.unlink()
    except Exception:
        pass


def _url_basename(url: str) -> str:
    """Extract filename from a URL path."""
    return url.rstrip("/").split("/")[-1] if url else ""
