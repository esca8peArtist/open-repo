"""
Twilio channel configuration model.

Covers SMS, WhatsApp, and Voice (ConversationRelay). Stored in the agent's
YAML config file after the setup wizard completes Step 4.

The ``webhook_base_url`` must be publicly reachable by Twilio's servers.
During wizard setup this is discovered automatically (e.g. via ngrok tunnel
for dev, or the machine's public IP / reverse-proxy URL for production).
"""

from pydantic import BaseModel, Field


class TwilioConfig(BaseModel):
    """Runtime configuration for all Twilio-backed channels.

    Attributes:
        account_sid:        Twilio Account SID (starts with "AC…").
        auth_token:         Twilio Auth Token (used for API calls and
                            webhook signature validation).
        phone_number:       Twilio phone number in E.164 format (+12025551234).
        whatsapp_enabled:   Enable the WhatsApp channel (same credentials,
                            prefixes numbers with "whatsapp:").
        voice_enabled:      Enable Twilio ConversationRelay voice calls.
        webhook_base_url:   Public base URL where Twilio can POST webhooks.
                            Example: "https://agent.example.com"
        rate_limit_per_minute: Max outbound messages per minute per recipient.
    """

    account_sid: str = Field(..., description="Twilio Account SID (AC…)")
    auth_token: str = Field(..., description="Twilio Auth Token")
    phone_number: str = Field(
        ...,
        description="Twilio phone number in E.164 format (e.g. +12025551234)",
    )
    whatsapp_enabled: bool = Field(
        default=False,
        description="Enable WhatsApp channel via Twilio",
    )
    voice_enabled: bool = Field(
        default=False,
        description="Enable inbound voice calls via Twilio ConversationRelay",
    )
    webhook_base_url: str = Field(
        ...,
        description="Public base URL reachable by Twilio (e.g. https://agent.example.com)",
    )
    rate_limit_per_minute: int = Field(
        default=10,
        ge=1,
        description="Max outbound messages per recipient per minute",
    )
