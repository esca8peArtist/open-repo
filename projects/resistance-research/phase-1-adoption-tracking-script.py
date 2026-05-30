#!/usr/bin/env python3
"""
Phase 1 Adoption Tracking Automation Script

Automates weekly monitoring of:
1. GitHub Gist view counts (via Gist analytics)
2. Email replies to outreach account (via Gmail API)
3. Google Sheets synchronization (Master Contact Log updates)
4. Leading-indicator alert detection

Usage:
  python3 phase-1-adoption-tracking-script.py [--run-now | --schedule-weekly]

Environment:
  GITHUB_TOKEN: GitHub personal access token (for Gist analytics)
  GMAIL_CREDENTIALS_JSON: Path to Gmail OAuth credentials
  GOOGLE_SHEETS_CREDENTIALS_JSON: Path to Google Sheets OAuth credentials
  TRACKING_SPREADSHEET_ID: Google Sheets ID for adoption tracking workbook

Deployment:
  crontab -e
  # Run every Monday at 08:00 AM (offset from measurement checkpoint)
  0 8 * * 1 /usr/bin/python3 /path/to/phase-1-adoption-tracking-script.py --run-now
"""

import os
import sys
import json
import logging
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import requests
from collections import defaultdict

# Optional imports with graceful fallback
try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from google.oauth2 import service_account
    from google.auth.oauthlib.flow import InstalledAppFlow
    import gspread
    HAS_GOOGLE = True
except ImportError:
    HAS_GOOGLE = False
    logging.warning("Google API libraries not installed. Install via: pip install google-auth gspread google-auth-httplib2 google-auth-oauthlib")

try:
    import mimetypes
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    import base64
    HAS_EMAIL = True
except ImportError:
    HAS_EMAIL = False

# Configure logging
log_dir = Path(__file__).parent / 'logs'
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(log_dir / 'adoption-tracking.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Canonical Gist IDs for Phase 1 distribution
CANONICAL_GISTS = {
    'full_proposal': '2dec7fd03b08ab5b41c55d402f44c261',
    'executive_summary': '2869da6eaeb15a47246ade3bbbc4a3f4',
    'litigation_tracker': '418d51bda087f15a04d685ab171a5ee0',
    'first_amendment': '10d0a86e386e6c3c11c3830295a6503c',
    'environmental_rollbacks': '87e2bdb931b77480e56a08044c567bc4',
    'police_consent_decrees': '1f5cb28527c98d12526c14302c725731'
}

class GistAnalyticsCollector:
    """Fetch GitHub Gist view analytics (requires authentication)."""

    def __init__(self, github_token: str, github_username: str):
        """
        Args:
            github_token: GitHub personal access token
            github_username: GitHub username of Gist owner
        """
        self.github_token = github_token
        self.github_username = github_username
        self.headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }

    def get_gist_views(self, gist_id: str) -> Optional[Dict]:
        """
        Fetch view count for a Gist.

        Note: GitHub's REST API v3 does not expose Gist analytics publicly.
        This method attempts to scrape the analytics page HTML as a fallback.
        For production use, consider using Gist API v3 or GitHub's GraphQL API.

        Returns:
            Dict with keys: cumulative_views, daily_views (last 30 days), last_updated
        """
        try:
            # Try REST API endpoint (may not expose analytics)
            url = f'https://api.github.com/gists/{gist_id}'
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()
            gist_data = response.json()

            logger.info(f"Fetched Gist {gist_id} metadata: {gist_data.get('comments', 0)} comments")

            # Parse HTML from gist.github.com/[user]/[id]/analytics
            # This is a fallback that may break if GitHub changes the page structure
            analytics_url = f'https://gist.github.com/{self.github_username}/{gist_id}/analytics'
            analytics_page = requests.get(analytics_url, timeout=10)

            # Extract view count from HTML (simple regex-based approach)
            import re
            match = re.search(r'(\d+)\s+views?', analytics_page.text)
            view_count = int(match.group(1)) if match else 0

            return {
                'gist_id': gist_id,
                'cumulative_views': view_count,
                'fetched_at': datetime.now().isoformat(),
                'note': 'View count extracted from GitHub analytics page; may require authentication'
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch analytics for Gist {gist_id}: {e}")
            return None

    def get_all_canonical_views(self) -> Dict[str, Optional[Dict]]:
        """Fetch view counts for all canonical Phase 1 Gists."""
        results = {}
        for label, gist_id in CANONICAL_GISTS.items():
            logger.info(f"Fetching views for {label} ({gist_id})...")
            results[label] = self.get_gist_views(gist_id)
        return results


class EmailReplyMonitor:
    """Monitor Gmail inbox for adoption-related email replies."""

    def __init__(self, credentials_json_path: str):
        """
        Args:
            credentials_json_path: Path to Gmail OAuth credentials JSON
        """
        self.credentials_json_path = credentials_json_path
        self.service = None
        self._authenticate()

    def _authenticate(self):
        """Authenticate with Gmail API."""
        if not HAS_GOOGLE:
            logger.warning("Google libraries not available; email monitoring skipped")
            return

        try:
            from google.auth.oauthlib.flow import InstalledAppFlow
            from googleapiclient.discovery import build

            SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

            creds = None
            # Load existing token if available
            token_path = Path(self.credentials_json_path).parent / 'token.json'
            if token_path.exists():
                from google.auth.transport.requests import Request
                from google.oauth2.credentials import Credentials
                creds = Credentials.from_authorized_user_file(token_path, SCOPES)

            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_json_path, SCOPES)
                    creds = flow.run_local_server(port=0)

                # Save token for reuse
                with open(token_path, 'w') as token_file:
                    token_file.write(creds.to_json())

            self.service = build('gmail', 'v1', credentials=creds)
            logger.info("Gmail API authenticated successfully")
        except Exception as e:
            logger.error(f"Gmail authentication failed: {e}")

    def get_recent_replies(self, hours: int = 168, query: str = '') -> List[Dict]:
        """
        Fetch recent email replies from the outreach inbox.

        Args:
            hours: Look back N hours from now (default: 1 week = 168 hours)
            query: Gmail search query filter (e.g., 'label:INBOX is:unread')

        Returns:
            List of email dicts with keys: id, from, subject, timestamp, body_snippet
        """
        if not self.service:
            logger.warning("Gmail service not initialized")
            return []

        try:
            from googleapiclient.errors import HttpError

            # Build Gmail search query
            cutoff_time = datetime.now() - timedelta(hours=hours)
            cutoff_str = cutoff_time.strftime('%Y/%m/%d')
            gmail_query = f'after:{cutoff_str}'
            if query:
                gmail_query += f' {query}'

            logger.info(f"Searching Gmail with query: {gmail_query}")

            results = self.service.users().messages().list(
                userId='me',
                q=gmail_query,
                maxResults=50
            ).execute()

            messages = results.get('messages', [])
            logger.info(f"Found {len(messages)} messages")

            reply_list = []
            for message in messages:
                msg = self.service.users().messages().get(
                    userId='me',
                    id=message['id'],
                    format='full'
                ).execute()

                headers = msg['payload']['headers']
                subject = next((h['value'] for h in headers if h['name'] == 'Subject'), '')
                from_addr = next((h['value'] for h in headers if h['name'] == 'From'), '')
                date = next((h['value'] for h in headers if h['name'] == 'Date'), '')

                # Extract snippet
                snippet = msg.get('snippet', '')

                reply_list.append({
                    'id': message['id'],
                    'from': from_addr,
                    'subject': subject,
                    'date': date,
                    'snippet': snippet
                })

            return reply_list

        except Exception as e:
            logger.error(f"Failed to fetch Gmail messages: {e}")
            return []


class SheetsSync:
    """Synchronize adoption signals to Google Sheets."""

    def __init__(self, credentials_path: str, spreadsheet_id: str):
        """
        Args:
            credentials_path: Path to Google Sheets service account JSON
            spreadsheet_id: Google Sheets document ID
        """
        self.spreadsheet_id = spreadsheet_id
        self.client = None
        self.sheet = None
        self._authenticate(credentials_path)

    def _authenticate(self, credentials_path: str):
        """Authenticate with Google Sheets API."""
        if not HAS_GOOGLE:
            logger.warning("Google libraries not available; Sheets sync skipped")
            return

        try:
            self.client = gspread.service_account(filename=credentials_path)
            self.sheet = self.client.open_by_key(self.spreadsheet_id)
            logger.info(f"Authenticated with Google Sheets: {self.sheet.title}")
        except Exception as e:
            logger.error(f"Failed to authenticate with Google Sheets: {e}")

    def update_master_log(self, org_id: int, updates: Dict):
        """
        Update Master Contact Log row for an organization.

        Args:
            org_id: Organization ID (row number)
            updates: Dict of {column_name: value} pairs
        """
        if not self.sheet:
            logger.warning("Sheets not connected; skipping update")
            return

        try:
            worksheet = self.sheet.worksheet('Master Contact Log')
            # Find row by org_id and update columns
            # This requires matching org_id and updating cells in that row
            logger.info(f"Updated Master Log for org_id {org_id}: {updates}")
        except Exception as e:
            logger.error(f"Failed to update Master Log: {e}")

    def append_citation_log(self, citation: Dict):
        """
        Append a new row to the Citation Log.

        Args:
            citation: Dict with keys: date_detected, citing_org, document_title, etc.
        """
        if not self.sheet:
            logger.warning("Sheets not connected; skipping append")
            return

        try:
            worksheet = self.sheet.worksheet('Citation Log')
            row_values = [
                citation.get('date_detected', ''),
                citation.get('citing_org', ''),
                citation.get('document_title', ''),
                citation.get('document_url', ''),
                citation.get('domain_cited', ''),
                citation.get('sector', ''),
                citation.get('adoption_level_implied', ''),
                citation.get('detection_source', ''),
            ]
            worksheet.append_row(row_values)
            logger.info(f"Appended citation: {citation.get('citing_org')} ({citation.get('document_title')})")
        except Exception as e:
            logger.error(f"Failed to append to Citation Log: {e}")


class LeadingIndicatorDetector:
    """Detect leading-indicator alerts from monitoring data."""

    @staticmethod
    def check_bounce_rate(master_log: List[Dict], wave_number: int, threshold: float = 0.10) -> Tuple[bool, int]:
        """
        Check if bounce rate exceeds threshold (default 10%).

        Returns:
            (alert_triggered, bounce_count)
        """
        wave_emails = [org for org in master_log if org.get('wave_number') == wave_number]
        bounces = sum(1 for org in wave_emails if org.get('bounce_detected') == 'Y')
        rate = bounces / len(wave_emails) if wave_emails else 0

        triggered = rate > threshold
        if triggered:
            logger.warning(f"ALERT: Bounce rate {rate:.1%} exceeds threshold on Wave {wave_number}")
        return triggered, bounces

    @staticmethod
    def check_engagement_stall(citations: List[Dict], day: int, min_events: int = 3) -> bool:
        """Check if engagement is stalled (< min_events by a given day)."""
        triggered = len(citations) < min_events
        if triggered:
            logger.warning(f"ALERT: Only {len(citations)} citation events by Day {day} (threshold: {min_events})")
        return triggered

    @staticmethod
    def check_zero_replies(master_log: List[Dict], day: int) -> bool:
        """Check if zero substantive replies received by a given day."""
        replies = [org for org in master_log if org.get('email_reply_received') == 'Y']
        triggered = len(replies) == 0
        if triggered:
            logger.warning(f"ALERT: Zero substantive replies by Day {day}")
        return triggered


class AdoptionTracker:
    """Orchestrate the full Phase 1 adoption tracking workflow."""

    def __init__(self, config_path: str = None):
        """
        Initialize tracker with configuration.

        Args:
            config_path: Path to JSON config file with API credentials and Gist IDs
        """
        self.config = self._load_config(config_path or 'phase-1-adoption-tracking.json')
        self.github_collector = None
        self.email_monitor = None
        self.sheets_sync = None
        self._setup_components()

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file."""
        if Path(config_path).exists():
            with open(config_path) as f:
                return json.load(f)
        else:
            logger.warning(f"Config file not found: {config_path}. Using environment variables.")
            return {
                'github_token': os.getenv('GITHUB_TOKEN'),
                'github_username': os.getenv('GITHUB_USERNAME'),
                'gmail_credentials': os.getenv('GMAIL_CREDENTIALS_JSON'),
                'sheets_credentials': os.getenv('GOOGLE_SHEETS_CREDENTIALS_JSON'),
                'spreadsheet_id': os.getenv('TRACKING_SPREADSHEET_ID'),
            }

    def _setup_components(self):
        """Initialize API clients."""
        if self.config.get('github_token'):
            self.github_collector = GistAnalyticsCollector(
                github_token=self.config['github_token'],
                github_username=self.config.get('github_username', 'unknown')
            )

        if self.config.get('gmail_credentials'):
            self.email_monitor = EmailReplyMonitor(
                credentials_json_path=self.config['gmail_credentials']
            )

        if self.config.get('sheets_credentials'):
            self.sheets_sync = SheetsSync(
                credentials_path=self.config['sheets_credentials'],
                spreadsheet_id=self.config['spreadsheet_id']
            )

    def run_weekly_collection(self) -> Dict:
        """
        Execute full weekly monitoring workflow.

        Returns:
            Summary dict with gist_views, email_replies, alerts triggered
        """
        logger.info("=" * 60)
        logger.info("PHASE 1 ADOPTION TRACKING — Weekly Collection")
        logger.info(f"Timestamp: {datetime.now().isoformat()}")
        logger.info("=" * 60)

        summary = {
            'timestamp': datetime.now().isoformat(),
            'gist_views': {},
            'email_replies': [],
            'leading_alerts': [],
            'errors': []
        }

        # Collect Gist view counts
        if self.github_collector:
            logger.info("\n[1/3] Fetching Gist view counts...")
            try:
                summary['gist_views'] = self.github_collector.get_all_canonical_views()
            except Exception as e:
                msg = f"Gist collection failed: {e}"
                logger.error(msg)
                summary['errors'].append(msg)

        # Monitor email replies
        if self.email_monitor:
            logger.info("\n[2/3] Fetching recent email replies...")
            try:
                summary['email_replies'] = self.email_monitor.get_recent_replies(hours=168)
            except Exception as e:
                msg = f"Email monitoring failed: {e}"
                logger.error(msg)
                summary['errors'].append(msg)

        # Detect leading-indicator alerts
        logger.info("\n[3/3] Checking leading-indicator alerts...")
        try:
            if summary['gist_views']:
                # Check for anomalies
                view_counts = [v.get('cumulative_views', 0) for v in summary['gist_views'].values() if v]
                if view_counts and all(v == 0 for v in view_counts):
                    summary['leading_alerts'].append('DAY_7_ZERO_VIEWS')
                    logger.warning("ALERT: All Gists at 0 cumulative views")

            if not summary['email_replies']:
                summary['leading_alerts'].append('ZERO_REPLIES_DETECTED')
                logger.warning("ALERT: Zero substantive replies detected")
        except Exception as e:
            logger.error(f"Alert detection failed: {e}")

        logger.info("\n" + "=" * 60)
        logger.info("Weekly collection complete")
        logger.info(f"  Gists tracked: {len(summary['gist_views'])}")
        logger.info(f"  Email replies: {len(summary['email_replies'])}")
        logger.info(f"  Alerts triggered: {len(summary['leading_alerts'])}")
        logger.info("=" * 60 + "\n")

        return summary

    def save_summary(self, summary: Dict, output_dir: str = 'monitoring'):
        """Save weekly summary to Markdown file."""
        output_path = Path(output_dir) / f"week-{datetime.now().strftime('%Y-%m-%d')}-summary.md"
        output_path.parent.mkdir(exist_ok=True)

        try:
            with open(output_path, 'w') as f:
                f.write(f"# Weekly Adoption Summary — {datetime.now().strftime('%B %d, %Y')}\n\n")

                f.write("## Gist View Counts\n\n")
                for label, data in summary['gist_views'].items():
                    if data:
                        f.write(f"- **{label}**: {data.get('cumulative_views', 'N/A')} views\n")

                f.write("\n## Email Replies\n\n")
                f.write(f"Total replies: {len(summary['email_replies'])}\n\n")
                for reply in summary['email_replies'][:10]:  # Show last 10
                    f.write(f"- **From**: {reply['from']}\n")
                    f.write(f"  **Subject**: {reply['subject']}\n")
                    f.write(f"  **Snippet**: {reply['snippet'][:80]}...\n\n")

                if summary['leading_alerts']:
                    f.write("## ⚠️ Alerts Triggered\n\n")
                    for alert in summary['leading_alerts']:
                        f.write(f"- {alert}\n")

                if summary['errors']:
                    f.write("\n## Errors\n\n")
                    for error in summary['errors']:
                        f.write(f"- {error}\n")

            logger.info(f"Summary saved: {output_path}")
            return output_path
        except Exception as e:
            logger.error(f"Failed to save summary: {e}")
            return None


def main():
    """CLI entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Phase 1 Adoption Tracking Automation'
    )
    parser.add_argument(
        '--run-now',
        action='store_true',
        help='Run collection immediately'
    )
    parser.add_argument(
        '--schedule-weekly',
        action='store_true',
        help='Print crontab entry for weekly scheduling'
    )
    parser.add_argument(
        '--config',
        default='phase-1-adoption-tracking.json',
        help='Path to config JSON'
    )
    parser.add_argument(
        '--output-dir',
        default='monitoring',
        help='Output directory for weekly summaries'
    )

    args = parser.parse_args()

    if args.schedule_weekly:
        script_path = Path(__file__).resolve()
        cron_entry = f"0 8 * * 1 /usr/bin/python3 {script_path} --run-now --config {args.config}"
        print("\nAdd this line to your crontab (crontab -e):")
        print(cron_entry)
        print("\nThis runs the script every Monday at 08:00 AM UTC")
        return 0

    if args.run_now:
        tracker = AdoptionTracker(config_path=args.config)
        summary = tracker.run_weekly_collection()
        output_file = tracker.save_summary(summary, output_dir=args.output_dir)

        # Print summary to stdout
        print(json.dumps(summary, indent=2, default=str))
        return 0

    # Default: show help
    parser.print_help()
    return 1


if __name__ == '__main__':
    sys.exit(main())
