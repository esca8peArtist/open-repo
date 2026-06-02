#!/usr/bin/env python3
"""
Coalition Email Routing & Tagging Monitor

Extends Gmail OAuth2 monitoring to auto-tag incoming Phase 1 response emails
by domain expertise keywords. Routes responses to domain-specific labels for
easy filtering in CHECKIN.md synthesis.

Usage:
  python3 coalition_email_router.py --auth          # OAuth2 setup
  python3 coalition_email_router.py --run-now       # Single sync
  python3 coalition_email_router.py --continuous    # Polling loop

Environment:
  GMAIL_CREDENTIALS_JSON: Path to Gmail OAuth2 credentials.json (if using service account)

Configuration (adoption-tracking-config.json):
  gmail_enabled: true
  gmail_credentials: path/to/credentials.json (OAuth2 client secret JSON)
  gmail_label: phase-1-responses (base label)
  email_lookback_hours: 168 (1 week default)
"""

import os
import sys
import json
import logging
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Optional, List, Tuple
import base64
import re
from dataclasses import dataclass, asdict
from time import sleep

# Optional Google API imports
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google.auth.oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    HAS_GOOGLE = True
except ImportError:
    HAS_GOOGLE = False

# Configure logging
log_dir = Path(__file__).parent.parent.parent / "phase-1-adoption" / "logs"
log_dir.mkdir(exist_ok=True, parents=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_dir / "coalition_email_router.log"),
        logging.StreamHandler(sys.stdout),
    ],
)
logger = logging.getLogger(__name__)


@dataclass
class CoalitionEmail:
    """Coalition response email with domain tagging."""
    message_id: str
    sender: str
    subject: str
    body_snippet: str
    received_date: str
    detected_domains: List[str]  # List of matching domain IDs
    confidence_scores: Dict[str, float]  # Domain ID -> confidence
    labels_applied: List[str] = None  # Gmail label IDs applied


class CoalitionEmailRouter:
    """Routes Phase 1 response emails to domain-specific labels."""

    # Gmail API scopes
    SCOPES = ["https://www.googleapis.com/auth/gmail.modify"]

    # Domain keyword mappings
    DOMAIN_KEYWORDS = {
        "domain_1": {
            "keywords": [
                "voting",
                "voting rights",
                "voter suppression",
                "ballot",
                "election",
                "franchise",
                "suffrage",
            ],
            "weight": 1.0,
        },
        "domain_39": {
            "keywords": [
                "medicaid",
                "healthcare",
                "health insurance",
                "disenrollment",
                "coverage",
                "patient",
                "hospital",
                "clinic",
                "prescription",
            ],
            "weight": 1.0,
        },
        "domain_40": {
            "keywords": [
                "election",
                "surveillance",
                "deepfake",
                "disinformation",
                "voting integrity",
                "election security",
                "poll worker",
                "election official",
            ],
            "weight": 1.0,
        },
        "domain_56": {
            "keywords": [
                "civil service",
                "federal employee",
                "government job",
                "merit system",
                "civil service protection",
                "schedule f",
                "appointment",
            ],
            "weight": 1.0,
        },
        "domain_58": {
            "keywords": [
                "tribal",
                "native american",
                "indigenous",
                "citizenship",
                "birthright",
                "indian country",
                "reservation",
                "tribal sovereignty",
            ],
            "weight": 1.0,
        },
    }

    # Monitoring state file
    STATE_FILE = Path(__file__).parent.parent.parent / "phase-1-adoption" / "data" / "email-router-state.json"

    def __init__(self, config: Optional[Dict] = None):
        """Initialize email router with optional config override."""
        if not HAS_GOOGLE:
            logger.warning("Google API libraries not installed; email routing disabled")
        self.config = config or self._load_config()
        self.state = self._load_state()
        self.gmail_service = None
        self.gmail_user_id = "me"
        self.base_label = self.config.get("gmail_label", "phase-1-responses")
        self.lookback_hours = self.config.get("email_lookback_hours", 168)
        self.polling_interval = self.config.get("email_polling_interval_minutes", 60)
        logger.info(f"Email Router initialized (lookback={self.lookback_hours}h, poll={self.polling_interval}m)")

    def _load_config(self) -> Dict:
        """Load configuration from adoption-tracking-config.json."""
        config_path = Path(__file__).parent.parent.parent / "phase-1-adoption" / "adoption-tracking-config.json"
        if config_path.exists():
            try:
                with open(config_path) as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load config: {e}; using defaults")
        return {}

    def _load_state(self) -> Dict:
        """Load state from file."""
        self.STATE_FILE.parent.mkdir(exist_ok=True, parents=True)
        if self.STATE_FILE.exists():
            try:
                with open(self.STATE_FILE, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load state: {e}; using defaults")
        return {
            "last_check": None,
            "messages_processed": 0,
            "messages_tagged": 0,
            "last_message_id": None,
            "labels_cache": {},  # Gmail label ID cache
        }

    def _save_state(self) -> None:
        """Persist state to file."""
        self.state["last_check"] = datetime.now(timezone.utc).isoformat()
        self.STATE_FILE.parent.mkdir(exist_ok=True, parents=True)
        with open(self.STATE_FILE, "w") as f:
            json.dump(self.state, f, indent=2)
        logger.debug(f"Saved state to {self.STATE_FILE}")

    def authenticate(self, credentials_path: Optional[str] = None) -> bool:
        """
        Authenticate to Gmail API via OAuth2.
        Creates browser-based auth flow if needed.
        """
        if not HAS_GOOGLE:
            logger.error("Google API libraries not available")
            return False

        try:
            # Use provided credentials path or config
            creds_path = credentials_path or self.config.get("gmail_credentials")
            if not creds_path:
                logger.error("Gmail credentials path not configured")
                return False

            creds_file = Path(creds_path)
            token_file = creds_file.parent / "gmail-token.json"

            # Try to load existing token
            if token_file.exists():
                creds = Credentials.from_authorized_user_file(str(token_file), self.SCOPES)
                if creds.expired and creds.refresh_token:
                    creds.refresh(Request())
            else:
                # Create new OAuth2 flow
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(creds_file),
                    self.SCOPES
                )
                creds = flow.run_local_server(port=0)
                # Save token for future use
                with open(token_file, "w") as f:
                    f.write(creds.to_json())
                logger.info(f"Saved Gmail token to {token_file}")

            self.gmail_service = build("gmail", "v1", credentials=creds)
            logger.info("Gmail authentication successful")
            return True

        except Exception as e:
            logger.error(f"Gmail authentication failed: {e}")
            return False

    def _get_or_create_label(self, label_name: str) -> Optional[str]:
        """
        Get Gmail label ID or create if not exists.
        Returns: Label ID or None
        """
        if not self.gmail_service:
            logger.error("Gmail service not authenticated")
            return None

        try:
            # Check cache first
            if label_name in self.state.get("labels_cache", {}):
                return self.state["labels_cache"][label_name]

            # List existing labels
            results = self.gmail_service.users().labels().list(userId=self.gmail_user_id).execute()
            labels = results.get("labels", [])

            for label in labels:
                if label["name"] == label_name:
                    self.state.setdefault("labels_cache", {})[label_name] = label["id"]
                    return label["id"]

            # Create label if not found
            label_body = {
                "name": label_name,
                "labelListVisibility": "labelShow",
                "messageListVisibility": "show",
            }
            created = self.gmail_service.users().labels().create(
                userId=self.gmail_user_id,
                body=label_body
            ).execute()
            label_id = created["id"]
            self.state.setdefault("labels_cache", {})[label_name] = label_id
            logger.info(f"Created label: {label_name} (ID: {label_id})")
            return label_id

        except HttpError as e:
            logger.error(f"Failed to get/create label: {e}")
            return None

    def _extract_body_text(self, message: Dict) -> str:
        """Extract readable text from Gmail message."""
        try:
            if "parts" in message["payload"]:
                for part in message["payload"]["parts"]:
                    if part["mimeType"] == "text/plain":
                        data = part["body"].get("data", "")
                        if data:
                            return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
            else:
                data = message["payload"]["body"].get("data", "")
                if data:
                    return base64.urlsafe_b64decode(data).decode("utf-8", errors="ignore")
        except Exception as e:
            logger.debug(f"Failed to extract body: {e}")
        return ""

    def analyze_email(self, message: Dict) -> CoalitionEmail:
        """
        Analyze email for domain relevance.
        Returns: CoalitionEmail with detected domains
        """
        # Extract headers
        headers = message["payload"]["headers"]
        sender = next((h["value"] for h in headers if h["name"] == "From"), "unknown")
        subject = next((h["value"] for h in headers if h["name"] == "Subject"), "")
        received_date = next((h["value"] for h in headers if h["name"] == "Date"), "")

        # Extract body snippet
        body_snippet = message.get("snippet", "")[:200]

        # Extract full body for analysis
        body_text = self._extract_body_text(message)

        # Analyze for domain matches
        combined_text = f"{subject} {body_text}".lower()

        domain_scores: Dict[str, float] = {}
        for domain_id, config in self.DOMAIN_KEYWORDS.items():
            score = 0.0
            weight = config["weight"]
            keyword_count = 0

            for keyword in config["keywords"]:
                if keyword.lower() in combined_text:
                    keyword_count += 1

            if keyword_count > 0:
                # Normalize score: more keywords = higher confidence
                score = min(keyword_count / len(config["keywords"]), 1.0) * weight
                domain_scores[domain_id] = score

        # Filter to domains above confidence threshold
        detected_domains = [d for d, score in domain_scores.items() if score > 0.3]

        return CoalitionEmail(
            message_id=message["id"],
            sender=sender,
            subject=subject,
            body_snippet=body_snippet,
            received_date=received_date,
            detected_domains=detected_domains,
            confidence_scores=domain_scores,
        )

    def tag_email(self, email: CoalitionEmail) -> bool:
        """
        Apply domain-specific labels to email.
        Returns: True if labels applied successfully
        """
        if not self.gmail_service or not email.detected_domains:
            return False

        try:
            label_ids = []
            for domain_id in email.detected_domains:
                label_name = f"{self.base_label}/{domain_id}"
                label_id = self._get_or_create_label(label_name)
                if label_id:
                    label_ids.append(label_id)

            if label_ids:
                self.gmail_service.users().messages().modify(
                    userId=self.gmail_user_id,
                    id=email.message_id,
                    body={"addLabelIds": label_ids},
                ).execute()
                email.labels_applied = label_ids
                logger.info(f"Tagged email from {email.sender}: {', '.join(email.detected_domains)}")
                self.state["messages_tagged"] += 1
                return True

        except HttpError as e:
            logger.error(f"Failed to tag email: {e}")
        return False

    def sync_emails(self) -> List[CoalitionEmail]:
        """
        Sync Phase 1 response emails and apply domain tags.
        Returns: List of tagged emails
        """
        if not self.gmail_service:
            logger.error("Gmail service not authenticated")
            return []

        tagged_emails = []

        try:
            logger.info(f"Syncing emails from {self.base_label} (lookback {self.lookback_hours}h)...")

            # Build query
            lookback_date = datetime.now(timezone.utc) - timedelta(hours=self.lookback_hours)
            query = f'label:{self.base_label} after:{lookback_date.strftime("%Y/%m/%d")}'

            # List messages
            results = self.gmail_service.users().messages().list(
                userId=self.gmail_user_id,
                q=query,
                maxResults=100,
            ).execute()

            messages = results.get("messages", [])
            logger.info(f"Found {len(messages)} messages to process")

            for msg in messages:
                # Get full message
                message = self.gmail_service.users().messages().get(
                    userId=self.gmail_user_id,
                    id=msg["id"],
                    format="full",
                ).execute()

                # Analyze and tag
                email = self.analyze_email(message)
                if email.detected_domains:
                    if self.tag_email(email):
                        tagged_emails.append(email)

                self.state["messages_processed"] += 1
                self.state["last_message_id"] = email.message_id

            logger.info(f"Sync complete: {len(tagged_emails)} emails tagged")
            self._save_state()
            return tagged_emails

        except HttpError as e:
            logger.error(f"Gmail sync failed: {e}")
            return []

    def generate_routing_report(self, emails: List[CoalitionEmail]) -> str:
        """
        Generate markdown report for CHECKIN.md insertion.
        Returns: Markdown formatted routing summary
        """
        if not emails:
            return ""

        # Group by domain
        by_domain: Dict[str, List[CoalitionEmail]] = {}
        for email in emails:
            for domain in email.detected_domains:
                if domain not in by_domain:
                    by_domain[domain] = []
                by_domain[domain].append(email)

        report = "### Email Routing Report\n\n"
        report += f"Generated: {datetime.now(timezone.utc).isoformat()}\n\n"

        for domain_id in sorted(by_domain.keys()):
            domain_emails = by_domain[domain_id]
            report += f"#### {domain_id} ({len(domain_emails)} responses)\n\n"

            for email in domain_emails[:5]:  # Show top 5 per domain
                report += f"- **From**: {email.sender}\n"
                report += f"  **Subject**: {email.subject}\n"
                report += f"  **Confidence**: {max(email.confidence_scores.values()) * 100:.0f}%\n"
                report += f"  **Snippet**: {email.body_snippet}\n\n"

            if len(domain_emails) > 5:
                report += f"... and {len(domain_emails) - 5} more\n\n"

        return report

    def run_check(self) -> bool:
        """Single synchronization cycle."""
        logger.info("=" * 60)
        logger.info("Coalition Email Router sync cycle")
        logger.info("=" * 60)

        if not self.gmail_service:
            logger.error("Not authenticated; skipping sync")
            return False

        emails = self.sync_emails()
        if emails:
            report = self.generate_routing_report(emails)
            logger.info(f"Routing report:\n{report}")

        return len(emails) > 0

    def run_continuous(self, duration_hours: Optional[int] = None):
        """
        Run monitor continuously in polling loop.
        Args:
            duration_hours: Stop after N hours (None = run indefinitely)
        """
        if not self.gmail_service:
            logger.error("Not authenticated; cannot run continuous")
            return

        start_time = datetime.now(timezone.utc)
        logger.info(f"Starting continuous sync (interval={self.polling_interval}m)")

        try:
            while True:
                if duration_hours:
                    elapsed = (datetime.now(timezone.utc) - start_time).total_seconds() / 3600
                    if elapsed > duration_hours:
                        logger.info(f"Duration limit reached ({duration_hours}h); stopping")
                        break

                self.run_check()

                logger.info(f"Next sync in {self.polling_interval} minutes...")
                sleep(self.polling_interval * 60)

        except KeyboardInterrupt:
            logger.info("Router stopped by user")
            self._save_state()


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Coalition Email Router")
    parser.add_argument("--auth", action="store_true", help="Run Gmail OAuth2 authentication")
    parser.add_argument("--run-now", action="store_true", help="Run single sync cycle")
    parser.add_argument("--continuous", action="store_true", help="Run continuous polling")
    parser.add_argument("--duration-hours", type=int, help="Stop after N hours (with --continuous)")
    parser.add_argument("--config", type=str, help="Config file path")
    parser.add_argument("--credentials", type=str, help="Gmail credentials.json path")

    args = parser.parse_args()

    # Load config if specified
    config = None
    if args.config:
        try:
            with open(args.config) as f:
                config = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            logger.error(f"Failed to load config: {e}")
            sys.exit(1)

    router = CoalitionEmailRouter(config=config)

    if args.auth:
        creds_path = args.credentials or (config.get("gmail_credentials") if config else None)
        if router.authenticate(creds_path):
            logger.info("Authentication successful")
            sys.exit(0)
        else:
            logger.error("Authentication failed")
            sys.exit(1)

    elif args.run_now:
        if not router.gmail_service:
            creds_path = args.credentials or (config.get("gmail_credentials") if config else None)
            if not router.authenticate(creds_path):
                logger.error("Not authenticated; use --auth first")
                sys.exit(1)

        if router.run_check():
            sys.exit(0)
        sys.exit(1)

    elif args.continuous:
        if not router.gmail_service:
            creds_path = args.credentials or (config.get("gmail_credentials") if config else None)
            if not router.authenticate(creds_path):
                logger.error("Not authenticated; use --auth first")
                sys.exit(1)

        router.run_continuous(duration_hours=args.duration_hours)
        sys.exit(0)

    else:
        parser.print_help()
        sys.exit(1)


if __name__ == "__main__":
    main()
