"""
Structured logging configuration for AgentCore.

Call configure_logging() once at application startup (before any log output).
Set LOG_FORMAT=json (default) for structured JSON logs in production.
Leave LOG_FORMAT unset or set to anything else for Python's default plain-text
format during local development.
"""
from __future__ import annotations

import logging
import os


def configure_logging() -> None:
    """
    Configure the root logger.

    When LOG_FORMAT=json (the default), every log record is emitted as a
    single-line JSON object via python-json-logger.  This format is expected
    by log aggregators (Loki, CloudWatch, Datadog, etc.).

    For local development set LOG_FORMAT=text to get the familiar coloured
    plain-text output from Python's default StreamHandler.
    """
    log_format = os.getenv("LOG_FORMAT", "json").lower()

    if log_format == "json":
        from pythonjsonlogger import jsonlogger

        handler = logging.StreamHandler()
        formatter = jsonlogger.JsonFormatter(
            fmt="%(asctime)s %(levelname)s %(name)s %(message)s",
            datefmt="%Y-%m-%dT%H:%M:%S",
        )
        handler.setFormatter(formatter)

        root = logging.getLogger()
        root.handlers.clear()
        root.addHandler(handler)
        root.setLevel(logging.INFO)
    # else: leave Python default logging in place for local dev
