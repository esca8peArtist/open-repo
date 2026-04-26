#!/usr/bin/env python3
"""
init_admin.py — Create the initial admin user in Open WebUI on first boot.
Containerized AI Agents — v1.0

Called by the setup wizard at step 12 ("Go live") after all services are healthy.
Uses the Open WebUI REST API to create the admin account only when no users exist.

Environment variables (set in .env / wizard output):
    WEBUI_URL              Base URL of Open WebUI (default: http://open-webui:3000)
    WEBUI_ADMIN_EMAIL      Admin account email address
    WEBUI_ADMIN_PASSWORD   Admin account password (min 8 chars required by Open WebUI)
    WEBUI_ADMIN_NAME       Display name for the admin account (default: Admin)

Exit codes:
    0  — Admin created successfully, or admin already exists (idempotent).
    1  — Fatal error: missing env vars, API unreachable, or unexpected failure.
"""

import os
import sys
import json
import time
import urllib.request
import urllib.error

# ---------------------------------------------------------------------------
# Configuration from environment
# ---------------------------------------------------------------------------
WEBUI_URL = os.environ.get("WEBUI_URL", "http://open-webui:3000").rstrip("/")
ADMIN_EMAIL = os.environ.get("WEBUI_ADMIN_EMAIL", "")
ADMIN_PASSWORD = os.environ.get("WEBUI_ADMIN_PASSWORD", "")
ADMIN_NAME = os.environ.get("WEBUI_ADMIN_NAME", "Admin")

SIGNUP_ENDPOINT = f"{WEBUI_URL}/api/v1/auths/signup"
USERS_ENDPOINT = f"{WEBUI_URL}/api/v1/users"

MAX_RETRIES = 10
RETRY_DELAY_SECONDS = 5


def log(msg: str) -> None:
    print(f"[init_admin] {msg}", flush=True)


def check_env() -> bool:
    """Validate required environment variables are present."""
    missing = []
    if not ADMIN_EMAIL:
        missing.append("WEBUI_ADMIN_EMAIL")
    if not ADMIN_PASSWORD:
        missing.append("WEBUI_ADMIN_PASSWORD")
    if missing:
        log(f"ERROR: Missing required environment variables: {', '.join(missing)}")
        return False
    return True


def http_get_json(url: str, token: str | None = None) -> tuple[int, dict]:
    """
    Perform a GET request and return (status_code, parsed_json).
    Returns ({}, status_code) on JSON parse failure.
    """
    req = urllib.request.Request(url, method="GET")
    req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=10) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8") if exc.fp else ""
        try:
            return exc.code, json.loads(body)
        except json.JSONDecodeError:
            return exc.code, {"detail": body}


def http_post_json(url: str, payload: dict, token: str | None = None) -> tuple[int, dict]:
    """
    Perform a POST request with a JSON body and return (status_code, parsed_json).
    """
    data = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(url, data=data, method="POST")
    req.add_header("Content-Type", "application/json")
    if token:
        req.add_header("Authorization", f"Bearer {token}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            body = resp.read().decode("utf-8")
            return resp.status, json.loads(body)
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8") if exc.fp else ""
        try:
            return exc.code, json.loads(body)
        except json.JSONDecodeError:
            return exc.code, {"detail": body}


def wait_for_webui() -> bool:
    """
    Poll the Open WebUI /health endpoint until it returns 200 or retries are exhausted.
    Returns True if WebUI is ready, False otherwise.
    """
    health_url = f"{WEBUI_URL}/health"
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = urllib.request.Request(health_url, method="GET")
            with urllib.request.urlopen(req, timeout=5) as resp:
                if resp.status == 200:
                    log(f"Open WebUI is healthy (attempt {attempt})")
                    return True
        except Exception as exc:  # noqa: BLE001
            log(f"Waiting for Open WebUI... attempt {attempt}/{MAX_RETRIES}: {exc}")
        time.sleep(RETRY_DELAY_SECONDS)
    log("ERROR: Open WebUI did not become healthy in time.")
    return False


def users_exist() -> bool:
    """
    Check whether any users are registered in Open WebUI yet.
    Open WebUI returns an empty list at /api/v1/users when no users exist
    (the endpoint is publicly accessible before any admin is created).
    Returns True if at least one user exists, False if the list is empty.
    """
    status, body = http_get_json(USERS_ENDPOINT)
    if status == 200:
        users = body if isinstance(body, list) else body.get("users", [])
        return len(users) > 0
    # If the endpoint requires auth (meaning admin already exists), treat as "exists".
    if status in (401, 403):
        log("Users endpoint returned 401/403 — admin already exists.")
        return True
    log(f"WARN: Unexpected status {status} from users endpoint. Assuming users exist to be safe.")
    return True


def create_admin() -> bool:
    """
    POST /api/v1/auths/signup with admin credentials.
    Open WebUI treats the first signup as the admin account automatically.
    Returns True on success, False on failure.
    """
    payload = {
        "name": ADMIN_NAME,
        "email": ADMIN_EMAIL,
        "password": ADMIN_PASSWORD,
    }
    log(f"Creating admin account: {ADMIN_EMAIL} (name: {ADMIN_NAME})")
    status, body = http_post_json(SIGNUP_ENDPOINT, payload)

    if status in (200, 201):
        log(f"Admin account created successfully (HTTP {status}).")
        return True

    # Open WebUI may return 400 with "User already exists" if run twice.
    detail = body.get("detail", "")
    if status == 400 and "already" in detail.lower():
        log(f"Admin account already exists (HTTP {status}: {detail}). Skipping.")
        return True

    log(f"ERROR: Failed to create admin account. HTTP {status}: {detail or body}")
    return False


def main() -> int:
    log(f"Starting admin initialisation against {WEBUI_URL}")

    if not check_env():
        return 1

    if not wait_for_webui():
        return 1

    if users_exist():
        log("Users already exist — skipping admin creation (idempotent).")
        return 0

    if not create_admin():
        return 1

    log("Admin initialisation complete.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
