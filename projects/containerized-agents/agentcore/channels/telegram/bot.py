"""
Telegram bot channel for AgentCore.

Always included on all profiles. Works when internet is available.
Degrades gracefully when offline — agent still handles web chat and voice.

Uses python-telegram-bot v21+ (async-native). Bot token is configured
during the first-boot setup wizard (Step 4 — Communication channels).

Message flow (inbound):
    Telegram servers  →  polling loop  →  _handle_message()
    →  handle_inbound()  →  ChannelMessage  →  message_router
    →  agent LLM  →  send_message()  →  Telegram servers

Voice notes:
    Telegram voice note  →  _handle_voice_message()
    →  download OGG bytes  →  POST /v1/audio/transcriptions
    →  ChannelMessage(content=<transcript>)  →  message_router
"""

from __future__ import annotations

import asyncio
import io
import logging
import math
from typing import TYPE_CHECKING, Any, Callable, Coroutine

import httpx
from telegram import Bot, Update, Voice
from telegram.constants import ChatAction, ParseMode
from telegram.error import NetworkError, TelegramError
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from ..base import BaseChannel, ChannelMessage

if TYPE_CHECKING:
    pass

logger = logging.getLogger(__name__)

from agentcore.config import get_settings


def _stt_endpoint() -> str:
    """Return the AgentCore STT endpoint URL (resolved from settings)."""
    return f"{get_settings().agentcore_base_url.rstrip('/')}/v1/audio/transcriptions"

# Greeting shown when a user sends /start.
_START_TEXT = (
    "Hello! I'm your AI assistant. Send me a message or a voice note and I'll help you out.\n\n"
    "Type /help for a list of commands."
)

# Help text shown on /help.
_HELP_TEXT = (
    "Available commands:\n"
    "/start  — Welcome message\n"
    "/help   — This help text\n"
    "/status — Agent status\n\n"
    "You can also send text messages or voice notes — I'll respond to all of them."
)


class TelegramChannel(BaseChannel):
    """Telegram Bot API channel backed by python-telegram-bot v21+.

    Runs a long-polling loop in a background asyncio task. All inbound
    messages (text and voice) are routed through the agent's message_router
    callable, which returns a reply string that is sent back to the chat.

    Args:
        bot_token:      Telegram Bot API token from BotFather.
        agent_id:       AgentCore agent identifier (passed to router).
        message_router: Async callable ``(ChannelMessage) -> str`` that
                        processes a message and returns the reply text.
        config:         Optional TelegramConfig; defaults are used if None.
    """

    channel_name = "telegram"
    requires_internet = True

    def __init__(
        self,
        bot_token: str,
        agent_id: str,
        message_router: Callable[[ChannelMessage], Coroutine[Any, Any, str]],
        *,
        allowed_chat_ids: list[int] | None = None,
        max_message_length: int = 4096,
        voice_enabled: bool = True,
        typing_indicator: bool = True,
        rate_limit_per_minute: int = 20,
    ) -> None:
        self.bot_token = bot_token
        self.agent_id = agent_id
        self.router = message_router
        self.allowed_chat_ids: set[int] = set(allowed_chat_ids or [])
        self.max_message_length = max_message_length
        self.voice_enabled = voice_enabled
        self.typing_indicator = typing_indicator
        self.rate_limit_per_minute = rate_limit_per_minute

        self.app: Application | None = None
        self._running = False
        self._poll_task: asyncio.Task[None] | None = None

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    async def start(self) -> None:
        """Start the Telegram polling loop in a background asyncio task.

        Initialises the Application, registers handlers, and starts polling.
        Non-blocking — the polling loop runs as a daemon task.

        Raises:
            TelegramError: If the bot token is invalid (caught during first
                           getMe call inside Application.initialize()).
        """
        if self._running:
            logger.warning("TelegramChannel.start() called but already running")
            return

        logger.info("Starting Telegram channel (agent_id=%s)", self.agent_id)

        self.app = (
            Application.builder()
            .token(self.bot_token)
            .build()
        )

        # Register command handlers.
        self.app.add_handler(CommandHandler("start", self._handle_start_command))
        self.app.add_handler(CommandHandler("help", self._handle_help_command))
        self.app.add_handler(CommandHandler("status", self._handle_status_command))

        # Register text message handler.
        self.app.add_handler(
            MessageHandler(filters.TEXT & ~filters.COMMAND, self._handle_message)
        )

        # Register voice message handler (if enabled).
        if self.voice_enabled:
            self.app.add_handler(
                MessageHandler(filters.VOICE, self._handle_voice_message)
            )

        # Initialise the application (validates token via getMe).
        await self.app.initialize()
        await self.app.start()

        self._running = True

        # Start polling in a background task so start() returns immediately.
        self._poll_task = asyncio.create_task(
            self._run_polling(), name="telegram-polling"
        )
        logger.info("Telegram polling started")

    async def stop(self) -> None:
        """Stop the polling loop and clean up resources gracefully."""
        if not self._running:
            return

        logger.info("Stopping Telegram channel")
        self._running = False

        if self._poll_task and not self._poll_task.done():
            self._poll_task.cancel()
            try:
                await self._poll_task
            except asyncio.CancelledError:
                pass

        if self.app is not None:
            try:
                await self.app.updater.stop()  # type: ignore[union-attr]
                await self.app.stop()
                await self.app.shutdown()
            except Exception as exc:
                logger.warning("Error during Telegram app shutdown: %s", exc)

        logger.info("Telegram channel stopped")

    async def _run_polling(self) -> None:
        """Run the updater polling loop.  Handles reconnection on network errors."""
        assert self.app is not None
        try:
            await self.app.updater.start_polling(  # type: ignore[union-attr]
                allowed_updates=Update.ALL_TYPES,
                drop_pending_updates=True,
            )
            # Block until cancelled.
            while self._running:
                await asyncio.sleep(1)
        except asyncio.CancelledError:
            pass
        except NetworkError as exc:
            logger.warning("Telegram network error (offline?): %s", exc)
        except Exception as exc:
            logger.exception("Unexpected error in Telegram polling loop: %s", exc)

    # ------------------------------------------------------------------
    # Outbound messaging
    # ------------------------------------------------------------------

    async def send_message(
        self,
        recipient_id: str,
        text: str,
        **kwargs: Any,
    ) -> bool:
        """Send a text message to a Telegram chat.

        Handles Markdown formatting and splits messages that exceed
        Telegram's 4096-character limit into multiple consecutive messages.

        Args:
            recipient_id: String representation of the Telegram chat ID.
            text:         Message body. Supports MarkdownV2 by default.
            **kwargs:     Forwarded to Bot.send_message() (e.g. parse_mode).

        Returns:
            True on success, False on any error (network, bot error, etc.).
        """
        if self.app is None:
            logger.error("send_message called before channel was started")
            return False

        chat_id_int: int
        try:
            chat_id_int = int(recipient_id)
        except ValueError:
            logger.error("Invalid recipient_id (not an integer): %s", recipient_id)
            return False

        # Use Markdown by default unless caller overrides.
        parse_mode = kwargs.pop("parse_mode", ParseMode.MARKDOWN)

        # Split into chunks if the message exceeds the Telegram limit.
        chunks = _split_message(text, self.max_message_length)

        try:
            bot: Bot = self.app.bot
            for chunk in chunks:
                await bot.send_message(
                    chat_id=chat_id_int,
                    text=chunk,
                    parse_mode=parse_mode,
                    **kwargs,
                )
            return True
        except TelegramError as exc:
            # Retry once without parse_mode in case the Markdown is malformed.
            logger.warning(
                "Telegram send failed with parse_mode=%s, retrying as plain text: %s",
                parse_mode,
                exc,
            )
            try:
                bot = self.app.bot
                for chunk in chunks:
                    await bot.send_message(chat_id=chat_id_int, text=chunk)
                return True
            except TelegramError as exc2:
                logger.error(
                    "Failed to send Telegram message to %s: %s", recipient_id, exc2
                )
                return False
        except Exception as exc:
            logger.error(
                "Unexpected error sending Telegram message to %s: %s", recipient_id, exc
            )
            return False

    # ------------------------------------------------------------------
    # Inbound message parsing
    # ------------------------------------------------------------------

    async def handle_inbound(self, raw_payload: dict[str, Any]) -> ChannelMessage:
        """Parse a raw Telegram Update dict into a ChannelMessage.

        This method is provided for the webhook / test-injection path.
        The polling path calls _handle_message() directly via PTB handlers.

        Args:
            raw_payload: JSON-decoded Telegram Update object.

        Returns:
            Normalised ChannelMessage.

        Raises:
            ValueError: If the payload cannot be parsed into a usable message.
        """
        update = Update.de_json(raw_payload, self.app.bot if self.app else None)  # type: ignore[arg-type]
        if update is None or update.effective_message is None:
            raise ValueError("Cannot parse Telegram Update — no effective_message")

        msg = update.effective_message
        chat_id = str(msg.chat_id)
        text = msg.text or msg.caption or ""

        return ChannelMessage(
            channel=self.channel_name,
            sender_id=chat_id,
            content=text,
            metadata={
                "update_id": update.update_id,
                "message_id": msg.message_id,
                "from_user": msg.from_user.to_dict() if msg.from_user else {},
                "chat": msg.chat.to_dict(),
                "date": msg.date.isoformat() if msg.date else None,
            },
        )

    # ------------------------------------------------------------------
    # Internal PTB handler callbacks
    # ------------------------------------------------------------------

    async def _handle_message(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Handle inbound text messages.

        1. Validates the sender is in the allow-list (if configured).
        2. Shows typing indicator.
        3. Builds a ChannelMessage and routes to the agent.
        4. Sends the reply.
        """
        if update.effective_message is None or update.effective_chat is None:
            return

        chat_id = update.effective_chat.id
        if not self._is_allowed(chat_id):
            logger.info("Ignoring message from unauthorised chat_id=%s", chat_id)
            return

        text = update.effective_message.text or ""
        if not text.strip():
            return

        if self.typing_indicator:
            try:
                await update.effective_chat.send_action(ChatAction.TYPING)
            except TelegramError:
                pass  # Non-critical

        channel_msg = ChannelMessage(
            channel=self.channel_name,
            sender_id=str(chat_id),
            content=text,
            metadata={
                "update_id": update.update_id,
                "message_id": update.effective_message.message_id,
                "from_user": (
                    update.effective_message.from_user.to_dict()
                    if update.effective_message.from_user
                    else {}
                ),
                "chat": update.effective_chat.to_dict(),
                "date": (
                    update.effective_message.date.isoformat()
                    if update.effective_message.date
                    else None
                ),
            },
        )

        try:
            reply_text = await self.router(channel_msg)
        except Exception as exc:
            logger.exception("Agent router raised an exception: %s", exc)
            reply_text = "I encountered an error processing your message. Please try again."

        await self.send_message(str(chat_id), reply_text)

    async def _handle_start_command(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Handle /start command — send welcome message."""
        if update.effective_chat is None:
            return
        chat_id = update.effective_chat.id
        if not self._is_allowed(chat_id):
            return
        await self.send_message(str(chat_id), _START_TEXT, parse_mode=None)

    async def _handle_help_command(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Handle /help command — send help text."""
        if update.effective_chat is None:
            return
        chat_id = update.effective_chat.id
        if not self._is_allowed(chat_id):
            return
        await self.send_message(str(chat_id), _HELP_TEXT, parse_mode=None)

    async def _handle_status_command(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Handle /status command — report agent liveness."""
        if update.effective_chat is None:
            return
        chat_id = update.effective_chat.id
        if not self._is_allowed(chat_id):
            return
        status_text = f"Agent *{self.agent_id}* is online and ready."
        await self.send_message(str(chat_id), status_text)

    async def _handle_voice_message(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ) -> None:
        """Handle Telegram voice notes (OGG/Opus audio).

        Downloads the voice file, posts it to the AgentCore STT endpoint
        (/v1/audio/transcriptions), and routes the transcript as a normal
        text ChannelMessage.

        If the STT endpoint is unreachable or transcription fails, the user
        receives a friendly error rather than a silent drop.
        """
        if update.effective_message is None or update.effective_chat is None:
            return

        chat_id = update.effective_chat.id
        if not self._is_allowed(chat_id):
            return

        voice: Voice | None = update.effective_message.voice
        if voice is None:
            return

        if self.typing_indicator:
            try:
                await update.effective_chat.send_action(ChatAction.TYPING)
            except TelegramError:
                pass

        try:
            # Download the voice file bytes from Telegram's servers.
            assert self.app is not None
            tg_file = await self.app.bot.get_file(voice.file_id)
            audio_bytes = await tg_file.download_as_bytearray()
        except TelegramError as exc:
            logger.error("Failed to download Telegram voice file: %s", exc)
            await self.send_message(
                str(chat_id),
                "Sorry, I couldn't download your voice message. Please try again.",
                parse_mode=None,
            )
            return

        # Transcribe via local AgentCore STT endpoint.
        transcript = await self._transcribe_audio(bytes(audio_bytes), fmt="ogg")
        if transcript is None:
            await self.send_message(
                str(chat_id),
                "Sorry, I couldn't transcribe your voice message. Please try typing instead.",
                parse_mode=None,
            )
            return

        logger.info(
            "Transcribed voice note from chat_id=%s (%d chars)", chat_id, len(transcript)
        )

        channel_msg = ChannelMessage(
            channel=self.channel_name,
            sender_id=str(chat_id),
            content=transcript,
            metadata={
                "voice": True,
                "duration": voice.duration,
                "file_id": voice.file_id,
                "mime_type": voice.mime_type,
                "update_id": update.update_id,
                "message_id": update.effective_message.message_id,
            },
        )

        try:
            reply_text = await self.router(channel_msg)
        except Exception as exc:
            logger.exception("Agent router raised an exception for voice message: %s", exc)
            reply_text = "I encountered an error processing your voice message. Please try again."

        await self.send_message(str(chat_id), reply_text)

    # ------------------------------------------------------------------
    # Helpers
    # ------------------------------------------------------------------

    def _is_allowed(self, chat_id: int) -> bool:
        """Return True if the chat_id is permitted to use the bot.

        When allowed_chat_ids is empty (default), all chats are permitted.
        """
        if not self.allowed_chat_ids:
            return True
        return chat_id in self.allowed_chat_ids

    async def _transcribe_audio(self, audio_bytes: bytes, fmt: str = "ogg") -> str | None:
        """POST audio bytes to the local AgentCore STT endpoint.

        Args:
            audio_bytes: Raw audio data.
            fmt:         File extension for the audio format.

        Returns:
            Transcript string on success, None on failure.
        """
        try:
            async with httpx.AsyncClient(timeout=60.0) as client:
                response = await client.post(
                    _stt_endpoint(),
                    files={"file": (f"voice.{fmt}", io.BytesIO(audio_bytes), "audio/ogg")},
                    data={"model": "whisper-1", "response_format": "json"},
                )
                response.raise_for_status()
                data = response.json()
                return data.get("text", "").strip() or None
        except httpx.HTTPStatusError as exc:
            logger.error("STT endpoint returned error %s: %s", exc.response.status_code, exc)
            return None
        except httpx.RequestError as exc:
            logger.error("STT endpoint unreachable: %s", exc)
            return None
        except Exception as exc:
            logger.exception("Unexpected error calling STT endpoint: %s", exc)
            return None


# ---------------------------------------------------------------------------
# Utilities
# ---------------------------------------------------------------------------


def _split_message(text: str, max_length: int) -> list[str]:
    """Split a message into chunks that fit within max_length characters.

    Attempts to split on newline boundaries first, then word boundaries,
    and falls back to hard splitting if necessary. Keeps each chunk at or
    below max_length.

    Args:
        text:       Full message text.
        max_length: Maximum characters per chunk.

    Returns:
        List of non-empty chunks.
    """
    if len(text) <= max_length:
        return [text]

    chunks: list[str] = []
    remaining = text

    while len(remaining) > max_length:
        # Try to split on the last newline within the limit.
        split_at = remaining.rfind("\n", 0, max_length)
        if split_at == -1:
            # Fall back to last space within the limit.
            split_at = remaining.rfind(" ", 0, max_length)
        if split_at == -1:
            # Hard split.
            split_at = max_length

        chunks.append(remaining[:split_at].rstrip())
        remaining = remaining[split_at:].lstrip()

    if remaining:
        chunks.append(remaining)

    return [c for c in chunks if c]
