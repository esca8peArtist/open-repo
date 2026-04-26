"""
Telegram bot setup helpers — used by the first-boot setup wizard (Step 4).

All functions are async-safe and use httpx for HTTP calls. They return
structured results so the wizard UI can display meaningful feedback to the
operator without exposing raw exceptions.

Telegram Bot API base URL: https://api.telegram.org/bot<token>/<method>
"""

from __future__ import annotations

import logging

import httpx

logger = logging.getLogger(__name__)

_TELEGRAM_API_BASE = "https://api.telegram.org/bot"

# Commands to register with Telegram's command list (shown in the chat UI).
_BOT_COMMANDS = [
    {"command": "start", "description": "Start chatting with the agent"},
    {"command": "help", "description": "Show available commands"},
    {"command": "status", "description": "Check agent status"},
]


async def validate_bot_token(token: str) -> tuple[bool, str]:
    """Validate a Telegram bot token by calling the getMe API method.

    Performs a real HTTP request to the Telegram Bot API. Should be called
    during wizard Step 4 before saving the token to config.

    Args:
        token: Bot token string from BotFather (e.g. "123456:ABC-DEF…").

    Returns:
        A tuple ``(is_valid, message)`` where:
        - ``is_valid`` is True if the token is accepted by Telegram.
        - ``message`` is the bot's ``@username`` on success, or a
          human-readable error description on failure.
    """
    token = token.strip()
    if not token or ":" not in token:
        return False, "Token format is invalid — expected '123456:ABC-DEF…'"

    url = f"{_TELEGRAM_API_BASE}{token}/getMe"
    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.get(url)

        data = resp.json()
        if resp.status_code == 200 and data.get("ok"):
            username = data["result"].get("username", "<unknown>")
            return True, f"@{username}"

        # Telegram returns a description field on error.
        description = data.get("description", f"HTTP {resp.status_code}")
        return False, f"Token rejected by Telegram: {description}"

    except httpx.TimeoutException:
        return False, "Request timed out — check your internet connection"
    except httpx.RequestError as exc:
        return False, f"Network error: {exc}"
    except Exception as exc:
        logger.exception("Unexpected error validating Telegram token: %s", exc)
        return False, f"Unexpected error: {exc}"


async def set_bot_commands(token: str) -> bool:
    """Register the standard command list with Telegram.

    This populates the command menu shown to users in the Telegram client.
    Registers: /start, /help, /status.

    Args:
        token: Validated bot token.

    Returns:
        True if commands were set successfully, False otherwise.
    """
    token = token.strip()
    url = f"{_TELEGRAM_API_BASE}{token}/setMyCommands"
    payload = {"commands": _BOT_COMMANDS}

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.post(url, json=payload)

        data = resp.json()
        if resp.status_code == 200 and data.get("ok"):
            logger.info("Telegram bot commands registered successfully")
            return True

        logger.warning(
            "setMyCommands failed: HTTP %s — %s",
            resp.status_code,
            data.get("description", "unknown error"),
        )
        return False

    except httpx.RequestError as exc:
        logger.error("Network error setting bot commands: %s", exc)
        return False
    except Exception as exc:
        logger.exception("Unexpected error setting bot commands: %s", exc)
        return False


async def get_bot_info(token: str) -> dict:
    """Return metadata about the bot for display in the wizard.

    Calls getMe and returns a flat dict with keys: ``id``, ``username``,
    ``first_name``, ``can_join_groups``, ``supports_inline_queries``.
    Returns an empty dict on any error.

    Args:
        token: Bot token string.

    Returns:
        Dict with bot metadata, or empty dict on failure.
    """
    token = token.strip()
    url = f"{_TELEGRAM_API_BASE}{token}/getMe"

    try:
        async with httpx.AsyncClient(timeout=15.0) as client:
            resp = await client.get(url)

        data = resp.json()
        if resp.status_code != 200 or not data.get("ok"):
            logger.warning(
                "get_bot_info: getMe failed — %s",
                data.get("description", f"HTTP {resp.status_code}"),
            )
            return {}

        result = data.get("result", {})
        return {
            "id": result.get("id"),
            "username": result.get("username", ""),
            "first_name": result.get("first_name", ""),
            "can_join_groups": result.get("can_join_groups", False),
            "supports_inline_queries": result.get("supports_inline_queries", False),
        }

    except httpx.RequestError as exc:
        logger.error("Network error in get_bot_info: %s", exc)
        return {}
    except Exception as exc:
        logger.exception("Unexpected error in get_bot_info: %s", exc)
        return {}
