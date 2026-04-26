"""
Email MCP tools — SMTP (send) + IMAP (read).

Tools
-----
send_email   — send an email via SMTP
read_emails  — fetch emails from an IMAP folder

Works with any standards-compliant mail server including local ones (Postfix,
Dovecot, Mailhog).  Does not require internet if the mail server is on the
local network.

Config (env vars — all sourced via agentcore.config.Settings)
-------------------------------------------------------------
SMTP_HOST        — default: localhost
SMTP_PORT        — default: 587
SMTP_USE_TLS     — "true" / "false", default: true
IMAP_HOST        — default: localhost
IMAP_PORT        — default: 993
IMAP_USE_SSL     — "true" / "false", default: true
EMAIL_USER       — sender / login address
EMAIL_PASSWORD   — SMTP+IMAP password
EMAIL_FROM       — From: address (defaults to EMAIL_USER)

Profiles: personal_productivity (1), customer_support (2), sales_outreach (5)
"""
from __future__ import annotations

import asyncio
import email as email_lib
import imaplib
import logging
import smtplib
import ssl
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import formatdate
from functools import partial
from typing import Any

from agentcore.config import get_settings
from agentcore.mcp.protocol import MCPContext, MCPTool, MCPToolResult, MCPToolSchema

logger = logging.getLogger(__name__)

_PROFILES = ["personal_productivity", "customer_support", "sales_outreach"]


def _smtp_config() -> dict:
    s = get_settings()
    return {
        "host": s.smtp_host,
        "port": s.smtp_port,
        "use_tls": s.smtp_use_tls,
        "user": s.email_user,
        "password": s.email_password,
        "from_addr": s.email_from or s.email_user,
    }


def _imap_config() -> dict:
    s = get_settings()
    return {
        "host": s.imap_host,
        "port": s.imap_port,
        "use_ssl": s.imap_use_ssl,
        "user": s.email_user,
        "password": s.email_password,
    }


# ---------------------------------------------------------------------------
# Tool 1: send_email
# ---------------------------------------------------------------------------


def _send_email_sync(cfg: dict, to: list[str], subject: str, body: str, cc: list[str]) -> dict:
    """Blocking SMTP send — run in thread pool."""
    msg = MIMEMultipart()
    msg["From"] = cfg["from_addr"] or cfg["user"]
    msg["To"] = ", ".join(to)
    if cc:
        msg["Cc"] = ", ".join(cc)
    msg["Subject"] = subject
    msg["Date"] = formatdate(localtime=True)
    msg.attach(MIMEText(body, "plain", "utf-8"))

    recipients = to + cc

    if cfg["use_tls"]:
        context = ssl.create_default_context()
        with smtplib.SMTP(cfg["host"], cfg["port"]) as server:
            server.ehlo()
            server.starttls(context=context)
            if cfg["user"]:
                server.login(cfg["user"], cfg["password"])
            server.sendmail(msg["From"], recipients, msg.as_string())
    else:
        with smtplib.SMTP(cfg["host"], cfg["port"]) as server:
            if cfg["user"]:
                server.login(cfg["user"], cfg["password"])
            server.sendmail(msg["From"], recipients, msg.as_string())

    return {"sent_to": recipients, "subject": subject}


class SendEmailTool(MCPTool):
    """Send an email via SMTP."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="send_email",
            description="Send an email to one or more recipients via SMTP.",
            input_schema={
                "type": "object",
                "properties": {
                    "to": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of recipient email addresses.",
                    },
                    "subject": {"type": "string", "description": "Email subject line."},
                    "body": {"type": "string", "description": "Plain-text email body."},
                    "cc": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional CC addresses.",
                    },
                    "attachments": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Optional list of file paths to attach.",
                    },
                },
                "required": ["to", "subject", "body"],
            },
            requires_internet=False,  # works on LAN mail servers too
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        to: list[str] = arguments["to"]
        subject: str = arguments["subject"]
        body: str = arguments["body"]
        cc: list[str] = arguments.get("cc", [])

        cfg = _smtp_config()
        if not cfg["host"]:
            return MCPToolResult(success=False, content=None, error="SMTP_HOST not configured.")

        try:
            loop = asyncio.get_running_loop()
            result = await loop.run_in_executor(
                None, partial(_send_email_sync, cfg, to, subject, body, cc)
            )
            return MCPToolResult(success=True, content=result)
        except Exception as exc:
            logger.error("send_email error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))


# ---------------------------------------------------------------------------
# Tool 2: read_emails
# ---------------------------------------------------------------------------


def _read_emails_sync(cfg: dict, folder: str, limit: int, unread_only: bool) -> list[dict]:
    """Blocking IMAP fetch — run in thread pool."""
    if cfg["use_ssl"]:
        mail = imaplib.IMAP4_SSL(cfg["host"], cfg["port"])
    else:
        mail = imaplib.IMAP4(cfg["host"], cfg["port"])

    try:
        mail.login(cfg["user"], cfg["password"])
        mail.select(folder)

        search_criteria = "UNSEEN" if unread_only else "ALL"
        status, data = mail.search(None, search_criteria)
        if status != "OK":
            return []

        message_ids = data[0].split()
        # Take the most recent `limit` messages
        message_ids = message_ids[-limit:]

        messages: list[dict] = []
        for msg_id in reversed(message_ids):
            status, msg_data = mail.fetch(msg_id, "(RFC822)")
            if status != "OK":
                continue
            raw = msg_data[0][1]
            msg = email_lib.message_from_bytes(raw)

            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain" and not part.get("Content-Disposition"):
                        try:
                            body = part.get_payload(decode=True).decode("utf-8", errors="replace")
                        except Exception:
                            pass
                        break
            else:
                try:
                    body = msg.get_payload(decode=True).decode("utf-8", errors="replace")
                except Exception:
                    body = ""

            messages.append(
                {
                    "id": msg_id.decode(),
                    "from": msg.get("From", ""),
                    "to": msg.get("To", ""),
                    "subject": msg.get("Subject", ""),
                    "date": msg.get("Date", ""),
                    "body": body[:2000],  # truncate very long bodies
                }
            )

        return messages
    finally:
        try:
            mail.logout()
        except Exception:
            pass


class ReadEmailsTool(MCPTool):
    """Read emails from an IMAP mailbox."""

    @property
    def schema(self) -> MCPToolSchema:
        return MCPToolSchema(
            name="read_emails",
            description="Fetch emails from an IMAP mailbox folder.",
            input_schema={
                "type": "object",
                "properties": {
                    "folder": {
                        "type": "string",
                        "description": "IMAP folder name (default: INBOX).",
                        "default": "INBOX",
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of emails to return (default: 10).",
                        "default": 10,
                        "minimum": 1,
                        "maximum": 100,
                    },
                    "unread_only": {
                        "type": "boolean",
                        "description": "If true, only return unread emails (default: false).",
                        "default": False,
                    },
                },
                "required": [],
            },
            requires_internet=False,
            profiles=_PROFILES,
        )

    async def execute(self, arguments: dict, context: MCPContext) -> MCPToolResult:
        folder: str = arguments.get("folder", "INBOX")
        limit: int = int(arguments.get("limit", 10))
        unread_only: bool = bool(arguments.get("unread_only", False))

        cfg = _imap_config()
        if not cfg["host"]:
            return MCPToolResult(success=False, content=None, error="IMAP_HOST not configured.")

        try:
            loop = asyncio.get_running_loop()
            messages = await loop.run_in_executor(
                None, partial(_read_emails_sync, cfg, folder, limit, unread_only)
            )
            return MCPToolResult(success=True, content={"emails": messages, "count": len(messages)})
        except Exception as exc:
            logger.error("read_emails error: %s", exc)
            return MCPToolResult(success=False, content=None, error=str(exc))
