"""
Telegram channel configuration model.

Validated by Pydantic on load. The setup wizard writes these values to
the agent's YAML config file; AgentCore reads them at startup.
"""

from pydantic import BaseModel, Field


class TelegramConfig(BaseModel):
    """Runtime configuration for TelegramChannel.

    Attributes:
        bot_token:            BotFather token (format: 123456:ABC-DEF...).
        agent_id:             AgentCore agent identifier routing messages.
        allowed_chat_ids:     Whitelist of Telegram chat IDs that can message
                              the bot. Empty list means all chats are allowed.
        max_message_length:   Telegram's hard limit is 4096 UTF-16 code units.
                              Outbound messages longer than this are split.
        voice_enabled:        Whether to handle voice note messages.
        typing_indicator:     Show "typing…" action while the agent processes.
        rate_limit_per_minute: Max outbound messages per minute per chat.
    """

    bot_token: str = Field(..., description="Telegram Bot API token from BotFather")
    agent_id: str = Field(..., description="AgentCore agent identifier")
    allowed_chat_ids: list[int] = Field(
        default_factory=list,
        description="Whitelist of allowed chat IDs — empty means allow all",
    )
    max_message_length: int = Field(
        default=4096,
        ge=1,
        le=4096,
        description="Max characters per outbound Telegram message",
    )
    voice_enabled: bool = Field(
        default=True,
        description="Transcribe and handle voice notes",
    )
    typing_indicator: bool = Field(
        default=True,
        description="Show typing action while agent is processing",
    )
    rate_limit_per_minute: int = Field(
        default=20,
        ge=1,
        description="Max outbound messages per chat per minute",
    )
