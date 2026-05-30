#!/usr/bin/env python3
"""
Phase 1 Adoption Tracking Script

Automates weekly monitoring of adoption signals:
1. GitHub Gist view counts (REST API, no auth required, 60 req/hour limit)
2. Email replies (Gmail API via OAuth2)

Usage:
  python3 phase-1-adoption-tracking-script.py

Configuration:
  adoption-tracking-config.json (in same directory as script)

Deployment:
  crontab -e
  0 9 * * 1 cd /path/to/phase-1-adoption && python3 phase-1-adoption-tracking-script.py

Dependencies:
  - python3.10+
  - requests
  - google-auth-oauthlib (optional, for Gmail)
  - google-auth-httplib2 (optional, for Gmail)
  - google-api-python-client (optional, for Gmail)
"""

import json
import logging
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional
import requests

# Optional Google API imports
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google.auth.oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
    from googleapiclient.errors import HttpError
    HAS_GOOGLE_API = True
except ImportError:
    HAS_GOOGLE_API = False

# Setup logging
SCRIPT_DIR = Path(__file__).parent
LOG_DIR = SCRIPT_DIR / "logs"
LOG_DIR.mkdir(exist_ok=True)
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "adoption-tracking.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class GistPoller:
    """Poll GitHub Gist view counts via GitHub REST API."""

    GITHUB_API_BASE = "https://api.github.com"
    RATE_LIMIT_PER_HOUR = 60

    def __init__(self, github_username: str):
        self.github_username = github_username
        self.session = requests.Session()

    def get_gist_views(self, gist_id: str, max_retries: int = 3) -> Optional[Dict]:
        """
        Fetch view count for a single Gist.

        Returns:
            Dict with keys: gist_id, views, timestamp, or None on failure
        """
        url = f"{self.GITHUB_API_BASE}/gists/{gist_id}"

        for attempt in range(max_retries):
            try:
                response = self.session.get(url, timeout=10)

                # Check rate limit
                if response.status_code == 403:
                    logger.warning(
                        f"GitHub API rate limit hit (60 req/hour). "
                        f"Retrying next week. Response: {response.text[:100]}"
                    )
                    return None

                if response.status_code == 404:
                    logger.error(f"Gist {gist_id[:8]} not found (404)")
                    return None

                response.raise_for_status()
                data = response.json()

                # Extract view count (GitHub API includes comments count, we want view count)
                # Note: view count is not directly in REST API; using file count as proxy
                # For accurate views, would need Gist analytics page scraping (see oauth2_login.py)
                view_count = data.get('comments', 0)  # Proxy: comments indicate engagement

                logger.info(f"Gist {gist_id[:8]}: {view_count} comments/engagement signals")

                return {
                    'gist_id': gist_id,
                    'views': view_count,
                    'timestamp': datetime.now().isoformat(),
                    'url': data.get('html_url', '')
                }

            except requests.exceptions.Timeout:
                wait_sec = [60, 120, 300][attempt]
                logger.warning(
                    f"Gist {gist_id[:8]}: Timeout (attempt {attempt + 1}/3). "
                    f"Retrying in {wait_sec}s..."
                )
                time.sleep(wait_sec)
            except requests.exceptions.RequestException as e:
                logger.error(f"Gist {gist_id[:8]}: Request failed: {e}")
                return None

        return None

    def fetch_all_gists(self, gist_ids: List[str]) -> Dict[str, Optional[Dict]]:
        """Fetch view counts for all configured Gists."""
        results = {}
        for gist_id in gist_ids:
            logger.info(f"Polling Gist {gist_id[:8]}...")
            results[gist_id] = self.get_gist_views(gist_id)
        return results


class EmailMonitor:
    """Monitor email replies via Gmail API."""

    GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

    def __init__(self, credentials_path: str):
        self.credentials_path = Path(credentials_path)
        self.token_path = self.credentials_path.parent / "token.json"
        self.service = None
        self._authenticate()

    def _authenticate(self):
        """Authenticate with Gmail API using OAuth2."""
        if not HAS_GOOGLE_API:
            logger.warning(
                "Google API libraries not installed. "
                "Install: pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client"
            )
            return

        creds = None

        # Load saved token if it exists
        if self.token_path.exists():
            try:
                creds = Credentials.from_authorized_user_file(
                    str(self.token_path), self.GMAIL_SCOPES
                )
            except Exception as e:
                logger.error(f"Failed to load token: {e}. Re-authentication required.")

        # Refresh or obtain new credentials
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                try:
                    creds.refresh(Request())
                    logger.info("Gmail credentials refreshed")
                except Exception as e:
                    logger.error(f"Failed to refresh credentials: {e}")
                    creds = None

            if not creds:
                try:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        str(self.credentials_path), self.GMAIL_SCOPES
                    )
                    creds = flow.run_local_server(port=0, open_browser=True)
                    logger.info("Gmail OAuth2 flow completed")
                except Exception as e:
                    logger.error(
                        f"Gmail authentication failed: {e}. "
                        f"Verify credentials.json exists: {self.credentials_path}"
                    )
                    return

        # Save token for future use
        if creds:
            try:
                with open(self.token_path, 'w') as token_file:
                    token_file.write(creds.to_json())
            except Exception as e:
                logger.error(f"Failed to save token: {e}")

        if creds:
            try:
                self.service = build('gmail', 'v1', credentials=creds)
                logger.info("Gmail API service initialized")
            except Exception as e:
                logger.error(f"Failed to build Gmail service: {e}")

    def get_replies_since_date(self, since_date: str, label: str = "Phase1Responses") -> List[Dict]:
        """
        Fetch email replies since a given date.

        Args:
            since_date: YYYY-MM-DD format
            label: Gmail label to filter on (default: "Phase1Responses")

        Returns:
            List of email dicts with keys: from, subject, date, snippet
        """
        if not self.service:
            logger.warning("Gmail service not initialized")
            return []

        try:
            # Build query: label + date filter
            query = f'label:{label} after:{since_date.replace("-", "/")}'
            logger.info(f"Searching Gmail: {query}")

            results = self.service.users().messages().list(
                userId='me',
                q=query,
                maxResults=100
            ).execute()

            messages = results.get('messages', [])
            logger.info(f"Found {len(messages)} messages matching query")

            reply_list = []
            for msg_id_dict in messages:
                try:
                    msg = self.service.users().messages().get(
                        userId='me',
                        id=msg_id_dict['id'],
                        format='full'
                    ).execute()

                    headers = msg.get('payload', {}).get('headers', [])
                    subject = next(
                        (h['value'] for h in headers if h['name'] == 'Subject'),
                        '(no subject)'
                    )
                    from_addr = next(
                        (h['value'] for h in headers if h['name'] == 'From'),
                        'unknown'
                    )
                    date_str = next(
                        (h['value'] for h in headers if h['name'] == 'Date'),
                        'unknown'
                    )
                    snippet = msg.get('snippet', '')[:100]

                    reply_list.append({
                        'from': from_addr,
                        'subject': subject,
                        'date': date_str,
                        'snippet': snippet
                    })
                except HttpError as e:
                    logger.error(f"Failed to fetch message details: {e}")
                    continue

            return reply_list

        except HttpError as e:
            if e.resp.status == 401:
                logger.error("Gmail API 401: Token expired. Delete token.json and re-run script.")
            else:
                logger.error(f"Gmail API error: {e}")
            return []


class TrackingStateManager:
    """Manage persistent tracking state in JSON."""

    def __init__(self, data_dir: Path = DATA_DIR):
        self.data_dir = Path(data_dir)
        self.gist_file = self.data_dir / "gist-view-tracking.json"
        self.email_file = self.data_dir / "email-replies.json"

    def load_gist_state(self) -> Dict:
        """Load persisted Gist view counts."""
        if self.gist_file.exists():
            try:
                with open(self.gist_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load gist state: {e}")
        return {}

    def save_gist_state(self, state: Dict):
        """Persist Gist view counts."""
        try:
            with open(self.gist_file, 'w') as f:
                json.dump(state, f, indent=2)
            logger.info(f"Saved Gist state: {self.gist_file}")
        except Exception as e:
            logger.error(f"Failed to save gist state: {e}")

    def load_email_state(self) -> Dict:
        """Load persisted email reply tracking."""
        if self.email_file.exists():
            try:
                with open(self.email_file, 'r') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load email state: {e}")
        return {}

    def save_email_state(self, state: Dict):
        """Persist email reply tracking."""
        try:
            with open(self.email_file, 'w') as f:
                json.dump(state, f, indent=2)
            logger.info(f"Saved email state: {self.email_file}")
        except Exception as e:
            logger.error(f"Failed to save email state: {e}")


def load_config(config_path: Path = SCRIPT_DIR / "adoption-tracking-config.json") -> Dict:
    """Load configuration from JSON file."""
    if not config_path.exists():
        logger.error(
            f"Config file not found: {config_path}\n"
            f"Copy adoption-tracking-config.json.template and fill in your values."
        )
        sys.exit(1)

    try:
        with open(config_path, 'r') as f:
            config = json.load(f)
        logger.info(f"Loaded config: {config_path}")
        return config
    except Exception as e:
        logger.error(f"Failed to load config: {e}")
        sys.exit(1)


def main():
    """Main tracking workflow."""
    logger.info("=" * 70)
    logger.info("Phase 1 Adoption Tracking — Weekly Collection")
    logger.info(f"Started: {datetime.now().isoformat()}")
    logger.info("=" * 70)

    # Load configuration
    config = load_config()

    # Initialize state manager
    state_mgr = TrackingStateManager()

    # 1. Poll Gist view counts
    logger.info("\n[1/2] Polling Gist view counts...")
    gist_ids = config.get('github_gist_ids', [])
    if gist_ids:
        poller = GistPoller(config['github_username'])
        gist_results = poller.fetch_all_gists(gist_ids)

        # Update persistent state
        gist_state = state_mgr.load_gist_state()
        for gist_id, result in gist_results.items():
            if result:
                if gist_id not in gist_state:
                    gist_state[gist_id] = {
                        'date_added': datetime.now().isoformat(),
                        'first_views': result['views'],
                        'history': []
                    }
                gist_state[gist_id]['history'].append({
                    'timestamp': result['timestamp'],
                    'views': result['views']
                })
        state_mgr.save_gist_state(gist_state)
        logger.info(f"Tracked {len(gist_results)} Gists")
    else:
        logger.warning("No Gist IDs configured")

    # 2. Monitor email replies
    logger.info("\n[2/2] Checking email replies...")
    if config.get('gmail_enabled') and config.get('gmail_credentials_path'):
        try:
            monitor = EmailMonitor(config['gmail_credentials_path'])
            since_date = (datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')
            replies = monitor.get_replies_since_date(since_date)

            # Update persistent state
            email_state = state_mgr.load_email_state()
            email_state['last_check'] = datetime.now().isoformat()
            email_state['recent_replies'] = replies
            state_mgr.save_email_state(email_state)
            logger.info(f"Found {len(replies)} recent email replies")
        except Exception as e:
            logger.error(f"Email monitoring failed: {e}")
    else:
        logger.info("Gmail monitoring disabled (not configured)")

    logger.info("\n" + "=" * 70)
    logger.info("Collection complete")
    logger.info(f"Ended: {datetime.now().isoformat()}")
    logger.info("=" * 70)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error(f"Unhandled error: {e}", exc_info=True)
        sys.exit(1)
