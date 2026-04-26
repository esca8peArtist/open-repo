"""
AgentCore configuration — all settings sourced from environment variables.
"""
from __future__ import annotations

import logging
import sys
from functools import lru_cache

from pydantic import field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

logger = logging.getLogger(__name__)

# Sentinel values that must not be used in production.
_FORBIDDEN_SECRET_VALUES: frozenset[str] = frozenset(
    {
        "changeme",
        "change_me",
        "CHANGE_ME_BEFORE_PRODUCTION",
        "secret",
        "password",
        "admin",
        "",
    }
)


class Settings(BaseSettings):
    """
    All settings are read from environment variables (or .env file).
    Environment variable names are the uppercase versions of the field names.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    # ---------------------------------------------------------------------------
    # Ollama (inference)
    # ---------------------------------------------------------------------------
    ollama_base_url: str = "http://ollama:11434"
    ollama_timeout: int = 300

    # ---------------------------------------------------------------------------
    # Database
    # REQUIRED — must be provided via environment variables; no insecure defaults.
    # Set POSTGRES_URL (full DSN) or ensure POSTGRES_PASSWORD is non-empty.
    # ---------------------------------------------------------------------------
    postgres_url: str  # e.g. postgresql+asyncpg://agentcore:<password>@postgres:5432/agentcore
    redis_url: str     # e.g. redis://:<password>@redis:6379/0
    chroma_url: str = "http://chromadb:8000"
    chroma_host: str = "chromadb"
    chroma_port: int = 8000

    # ---------------------------------------------------------------------------
    # AgentCore server
    # ---------------------------------------------------------------------------
    agentcore_port: int = 8080
    agentcore_host: str = "0.0.0.0"
    agentcore_base_url: str = "http://localhost:8080"
    max_concurrent_requests: int = 10
    request_timeout: int = 120

    # ---------------------------------------------------------------------------
    # Hardware tier (set by setup wizard, 1-4)
    # 1 = low-end (8 GB RAM, CPU-only)
    # 2 = mid-range (16 GB, integrated GPU)
    # 3 = high-end (32 GB, discrete GPU)
    # 4 = server (64+ GB, multi-GPU)
    # ---------------------------------------------------------------------------
    hardware_tier: int = 1

    # ---------------------------------------------------------------------------
    # Security
    # REQUIRED — set API_SECRET_KEY to a strong random value before first start.
    # Generate one with: python -c "import secrets; print(secrets.token_urlsafe(32))"
    # ---------------------------------------------------------------------------
    api_secret_key: str  # no default — must be set via env var

    @field_validator("api_secret_key")
    @classmethod
    def api_secret_key_must_be_strong(cls, v: str) -> str:
        if v.strip().lower() in {s.lower() for s in _FORBIDDEN_SECRET_VALUES}:
            raise ValueError(
                "API_SECRET_KEY is set to a known-weak placeholder value. "
                "Set a strong random secret before starting the server. "
                "Generate one with: python -c \"import secrets; print(secrets.token_urlsafe(32))\""
            )
        if len(v) < 16:
            raise ValueError(
                "API_SECRET_KEY must be at least 16 characters long. "
                "Generate a strong one with: python -c \"import secrets; print(secrets.token_urlsafe(32))\""
            )
        return v

    @field_validator("postgres_url")
    @classmethod
    def postgres_url_must_not_contain_weak_password(cls, v: str) -> str:
        """Reject DSNs that embed known-weak passwords."""
        lower = v.lower()
        for bad in ("changeme", "change_me", ":password@", ":secret@", ":admin@"):
            if bad in lower:
                raise ValueError(
                    f"POSTGRES_URL contains a known-weak credential ({bad!r}). "
                    "Replace the password with a strong random value."
                )
        return v

    @field_validator("redis_url")
    @classmethod
    def redis_url_must_not_contain_weak_password(cls, v: str) -> str:
        """Reject DSNs that embed known-weak passwords."""
        lower = v.lower()
        for bad in ("changeme", "change_me", ":password@", ":secret@", ":admin@"):
            if bad in lower:
                raise ValueError(
                    f"REDIS_URL contains a known-weak credential ({bad!r}). "
                    "Replace the password with a strong random value."
                )
        return v

    # ---------------------------------------------------------------------------
    # Connectivity check
    # ---------------------------------------------------------------------------
    connectivity_check_url: str = "https://1.1.1.1"
    connectivity_cache_ttl: int = 30  # seconds to cache online/offline status

    # ---------------------------------------------------------------------------
    # Telegram channel (optional — leave empty to disable)
    # ---------------------------------------------------------------------------
    telegram_bot_token: str = ""
    telegram_agent_id: str = "default"
    telegram_allowed_chat_ids: str = ""  # comma-separated int chat IDs, empty = allow all

    # ---------------------------------------------------------------------------
    # Twilio SMS / WhatsApp channels (optional — all must be set to enable)
    # ---------------------------------------------------------------------------
    twilio_account_sid: str = ""
    twilio_auth_token: str = ""
    twilio_sms_phone_number: str = ""       # E.164, e.g. +12025551234; empty = disable SMS
    twilio_whatsapp_phone_number: str = ""  # E.164 for WhatsApp number; empty = disable WhatsApp
    twilio_agent_id: str = "default"
    twilio_webhook_base_url: str = ""       # Public base URL for Twilio webhooks

    # ---------------------------------------------------------------------------
    # Web search (optional)
    # ---------------------------------------------------------------------------
    tavily_api_key: str = ""  # Tavily search API key; falls back to DuckDuckGo if empty

    # ---------------------------------------------------------------------------
    # GitHub integration (optional)
    # ---------------------------------------------------------------------------
    github_token: str = ""  # Personal access token or fine-grained token with repo scope

    # ---------------------------------------------------------------------------
    # CRM (optional — SQLite file path)
    # ---------------------------------------------------------------------------
    crm_db_path: str = "/data/crm.db"

    # ---------------------------------------------------------------------------
    # Database tool (optional — additional query targets beyond main postgres_url)
    # ---------------------------------------------------------------------------
    db_sqlite_path: str = ""       # Path to a SQLite file for the query_database tool
    db_postgres_url: str = ""      # PostgreSQL DSN for the query_database tool
    db_mysql_url: str = ""         # MySQL DSN (mysql+pymysql://user:pass@host/db)

    # ---------------------------------------------------------------------------
    # Email (IMAP/SMTP) — optional; leave blank to disable
    # ---------------------------------------------------------------------------
    smtp_host: str = "localhost"
    smtp_port: int = 587
    smtp_use_tls: bool = True
    imap_host: str = "localhost"
    imap_port: int = 993
    imap_use_ssl: bool = True
    email_user: str = ""             # sender / login address
    email_password: str = ""         # SMTP + IMAP password
    email_from: str = ""             # From: address (defaults to email_user at send time)

    # ---------------------------------------------------------------------------
    # Filesystem tool (optional)
    # ---------------------------------------------------------------------------
    filesystem_allowed_paths: str = ""  # Colon-separated allowlist; defaults to /data:/workspace

    # ---------------------------------------------------------------------------
    # CalDAV calendar (optional)
    # ---------------------------------------------------------------------------
    caldav_url: str = ""
    caldav_username: str = ""
    caldav_password: str = ""

    # ---------------------------------------------------------------------------
    # PDF report output directory (optional)
    # ---------------------------------------------------------------------------
    report_output_dir: str = "/data/reports"

    # ---------------------------------------------------------------------------
    # Scheduler database (optional — falls back to db_postgres_url, then SQLite)
    # ---------------------------------------------------------------------------
    scheduler_db_url: str = ""  # PostgreSQL DSN for the scheduled_tasks table

    # ---------------------------------------------------------------------------
    # Update verification (set at build time by the build pipeline)
    # ---------------------------------------------------------------------------
    # Ed25519 public key (hex) used to verify signed update manifests.
    # Set via environment variable or .env file — do NOT hardcode in source.
    # Generate a key pair with openssl:
    #   openssl genpkey -algorithm ed25519 -out update_private.pem
    #   openssl pkey -in update_private.pem -pubout -out update_public.pem
    #   openssl pkey -in update_public.pem -pubin -outform DER \
    #     | dd bs=1 skip=12 2>/dev/null | xxd -p -c 256
    # Or use the security/hardware_binding/ tooling available in this project.
    update_public_key_hex: str = ""

    # ---------------------------------------------------------------------------
    # Logging
    # ---------------------------------------------------------------------------
    log_level: str = "INFO"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    """Return the cached global Settings instance.

    Performs startup validation and exits with a fatal log message if required
    environment variables are missing or contain known-weak placeholder values.
    """
    try:
        return Settings()
    except Exception as exc:
        logger.critical(
            "FATAL: AgentCore cannot start due to invalid configuration: %s\n"
            "Set the required environment variables in your .env file and restart.",
            exc,
        )
        sys.exit(1)
