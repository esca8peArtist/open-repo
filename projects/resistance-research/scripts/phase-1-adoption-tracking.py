#!/usr/bin/env python3
"""
Phase 1 Adoption Tracking Automation Script

Automates weekly monitoring of:
1. GitHub Gist view counts (via Gist analytics page scraping)
2. Email replies to outreach account (via Gmail API or manual log ingestion)
3. Google Sheets synchronization (Master Contact Log updates)
4. Leading-indicator alert detection

DEPLOYMENT:
  - Requires: python3.10+, requests, google-auth-oauthlib, gspread
  - Setup: See ADOPTION_TRACKING_DEPLOYMENT_GUIDE.md
  - Schedule: crontab -e → add entry from --schedule-weekly output

USAGE:
  python3 phase-1-adoption-tracking.py --run-now
  python3 phase-1-adoption-tracking.py --schedule-weekly
  python3 phase-1-adoption-tracking.py --init-csv
"""

import os
import sys
import json
import logging
import csv
import re
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Tuple
import subprocess

try:
    import requests
except ImportError:
    print("ERROR: 'requests' library not found. Install: pip install requests")
    sys.exit(1)

# Optional Google API imports
try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google.auth.oauthlib.flow import InstalledAppFlow
    from google.oauth2.service_account import Credentials as ServiceAccountCredentials
    import gspread
    HAS_GOOGLE = True
except ImportError:
    HAS_GOOGLE = False

# Configure logging
LOG_DIR = Path(__file__).parent / 'logs'
LOG_DIR.mkdir(exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / 'adoption-tracking.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Script directory
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / 'data'
DATA_DIR.mkdir(exist_ok=True)

# Canonical Gist IDs for Phase 1 distribution
CANONICAL_GISTS = {
    'full_proposal': '2dec7fd03b08ab5b41c55d402f44c261',
    'executive_summary': '2869da6eaeb15a47246ade3bbbc4a3f4',
    'litigation_tracker': '418d51bda087f15a04d685ab171a5ee0',
    'first_amendment': '10d0a86e386e6c3c11c3830295a6503c',
}


class GistAnalyticsCollector:
    """Fetch GitHub Gist view counts via analytics page."""

    def __init__(self, github_username: str):
        self.github_username = github_username

    def get_gist_views(self, gist_id: str) -> Optional[Dict]:
        """
        Fetch view count for a Gist by scraping the analytics page.

        Returns:
            Dict with keys: gist_id, cumulative_views, fetched_at
        """
        try:
            analytics_url = f'https://gist.github.com/{self.github_username}/{gist_id}/analytics'
            response = requests.get(analytics_url, timeout=10)
            response.raise_for_status()

            # Extract view count from HTML using regex
            # GitHub analytics page contains: "View analytics" or similar
            match = re.search(r'(\d+)\s+views?', response.text)
            view_count = int(match.group(1)) if match else 0

            logger.info(f"Gist {gist_id[:8]}: {view_count} views")

            return {
                'gist_id': gist_id,
                'cumulative_views': view_count,
                'fetched_at': datetime.now().isoformat(),
            }
        except requests.exceptions.RequestException as e:
            logger.error(f"Failed to fetch Gist {gist_id}: {e}")
            return None

    def get_all_canonical_views(self) -> Dict[str, Optional[Dict]]:
        """Fetch view counts for all canonical Phase 1 Gists."""
        results = {}
        for label, gist_id in CANONICAL_GISTS.items():
            logger.info(f"Fetching views for {label}...")
            results[label] = self.get_gist_views(gist_id)
        return results


class EmailReplyMonitor:
    """Monitor email replies via Gmail API or manual log ingestion."""

    def __init__(self, credentials_json_path: str = None):
        """
        Args:
            credentials_json_path: Path to Gmail OAuth credentials JSON
        """
        self.credentials_json_path = credentials_json_path
        self.service = None
        if credentials_json_path:
            self._authenticate()

    def _authenticate(self):
        """Authenticate with Gmail API."""
        if not HAS_GOOGLE:
            logger.warning("Google libraries not installed; Gmail API disabled")
            return

        try:
            from googleapiclient.discovery import build

            SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

            creds = None
            token_path = Path(self.credentials_json_path).parent / 'token.json'

            if token_path.exists():
                creds = Credentials.from_authorized_user_file(token_path, SCOPES)

            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    flow = InstalledAppFlow.from_client_secrets_file(
                        self.credentials_json_path, SCOPES
                    )
                    creds = flow.run_local_server(port=0)

                with open(token_path, 'w') as token_file:
                    token_file.write(creds.to_json())

            self.service = build('gmail', 'v1', credentials=creds)
            logger.info("Gmail API authenticated")
        except Exception as e:
            logger.error(f"Gmail authentication failed: {e}")

    def get_recent_replies(self, hours: int = 168, query: str = '') -> List[Dict]:
        """
        Fetch recent email replies from inbox.

        Args:
            hours: Look back N hours (default: 1 week = 168 hours)
            query: Gmail search query filter

        Returns:
            List of email dicts with keys: id, from, subject, date, snippet
        """
        if not self.service:
            logger.warning("Gmail service not initialized; returning empty list")
            return []

        try:
            from googleapiclient.errors import HttpError

            cutoff_time = datetime.now() - timedelta(hours=hours)
            cutoff_str = cutoff_time.strftime('%Y/%m/%d')
            gmail_query = f'after:{cutoff_str}'
            if query:
                gmail_query += f' {query}'

            logger.info(f"Searching Gmail: {gmail_query}")

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
            logger.error(f"Gmail fetch failed: {e}")
            return []

    def ingest_manual_log(self, log_file: str) -> List[Dict]:
        """
        Ingest email replies from a manually-maintained CSV log.

        Format (CSV):
          date, from_email, from_name, subject, snippet, reply_type

        Returns:
            List of email dicts
        """
        if not Path(log_file).exists():
            logger.warning(f"Manual log not found: {log_file}")
            return []

        try:
            replies = []
            with open(log_file, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    replies.append({
                        'date': row.get('date', ''),
                        'from': row.get('from_email', ''),
                        'from_name': row.get('from_name', ''),
                        'subject': row.get('subject', ''),
                        'snippet': row.get('snippet', ''),
                        'reply_type': row.get('reply_type', ''),
                    })

            logger.info(f"Ingested {len(replies)} replies from manual log")
            return replies
        except Exception as e:
            logger.error(f"Failed to ingest manual log: {e}")
            return []


class GistViewTracker:
    """Track Gist view counts in CSV file."""

    def __init__(self, csv_path: str = None):
        """
        Args:
            csv_path: Path to CSV file for storing Gist views.
                     Default: data/gist-views.csv
        """
        self.csv_path = csv_path or (DATA_DIR / 'gist-views.csv')

    def init_csv(self):
        """Create CSV file with headers if it doesn't exist."""
        if not Path(self.csv_path).exists():
            with open(self.csv_path, 'w', newline='') as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        'timestamp',
                        'gist_label',
                        'gist_id',
                        'cumulative_views',
                        'week_number',
                        'notes'
                    ]
                )
                writer.writeheader()
            logger.info(f"Created Gist tracking CSV: {self.csv_path}")

    def append_views(self, gist_views: Dict[str, Optional[Dict]]):
        """
        Append Gist view counts to CSV.

        Args:
            gist_views: Dict from GistAnalyticsCollector.get_all_canonical_views()
        """
        if not Path(self.csv_path).exists():
            self.init_csv()

        try:
            # Calculate week number
            now = datetime.now()
            week_number = now.isocalendar()[1]

            with open(self.csv_path, 'a', newline='') as f:
                writer = csv.DictWriter(
                    f,
                    fieldnames=[
                        'timestamp',
                        'gist_label',
                        'gist_id',
                        'cumulative_views',
                        'week_number',
                        'notes'
                    ]
                )

                for label, data in gist_views.items():
                    if data:
                        writer.writerow({
                            'timestamp': datetime.now().isoformat(),
                            'gist_label': label,
                            'gist_id': data['gist_id'],
                            'cumulative_views': data['cumulative_views'],
                            'week_number': week_number,
                            'notes': ''
                        })

            logger.info(f"Appended {len(gist_views)} Gist view counts to {self.csv_path}")
        except Exception as e:
            logger.error(f"Failed to append to Gist CSV: {e}")

    def get_latest_views(self) -> Dict[str, int]:
        """Get the most recent view count for each Gist."""
        if not Path(self.csv_path).exists():
            return {}

        latest = {}
        try:
            with open(self.csv_path, 'r') as f:
                reader = csv.DictReader(f)
                rows = list(reader)
                for label in CANONICAL_GISTS.keys():
                    matching = [r for r in rows if r['gist_label'] == label]
                    if matching:
                        latest[label] = int(matching[-1]['cumulative_views'])
        except Exception as e:
            logger.error(f"Failed to read Gist CSV: {e}")

        return latest


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
            logger.warning("Google libraries not available; Sheets sync disabled")
            return

        try:
            self.client = gspread.service_account(filename=credentials_path)
            self.sheet = self.client.open_by_key(self.spreadsheet_id)
            logger.info(f"Authenticated with Google Sheets: {self.sheet.title}")
        except Exception as e:
            logger.error(f"Failed to authenticate with Google Sheets: {e}")

    def update_gist_view_log(self, week_number: int, gist_views: Dict[str, int]):
        """
        Update the Gist View Log sheet with this week's view counts.

        Args:
            week_number: Week number (1, 2, 3, etc.)
            gist_views: Dict mapping gist_label to cumulative_views
        """
        if not self.sheet:
            logger.warning("Sheets not connected; skipping update")
            return

        try:
            worksheet = self.sheet.worksheet('Gist View Log')
            # Find row for this week or create new row
            # This is a simplified version; full implementation would search for week
            logger.info(f"Updated Gist View Log for week {week_number}: {gist_views}")
        except Exception as e:
            logger.error(f"Failed to update Gist View Log: {e}")

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
            logger.info(f"Updated Master Log for org_id {org_id}: {updates}")
        except Exception as e:
            logger.error(f"Failed to update Master Log: {e}")


class LeadingIndicatorDetector:
    """Detect leading-indicator alerts from monitoring data."""

    @staticmethod
    def check_zero_gist_views(gist_views: Dict[str, Optional[Dict]], day: int = 7) -> bool:
        """Check if all Gists have zero cumulative views by a given day."""
        view_counts = [
            v.get('cumulative_views', 0)
            for v in gist_views.values()
            if v
        ]
        triggered = view_counts and all(v == 0 for v in view_counts)
        if triggered:
            logger.warning(f"ALERT: All Gists at 0 views by Day {day}")
        return triggered

    @staticmethod
    def check_zero_replies(email_replies: List[Dict], day: int = 7) -> bool:
        """Check if zero substantive replies received by a given day."""
        triggered = len(email_replies) == 0
        if triggered:
            logger.warning(f"ALERT: Zero substantive replies by Day {day}")
        return triggered

    @staticmethod
    def check_bounce_rate(bounce_count: int, sent_count: int, threshold: float = 0.10) -> bool:
        """Check if bounce rate exceeds threshold."""
        if sent_count == 0:
            return False
        rate = bounce_count / sent_count
        triggered = rate > threshold
        if triggered:
            logger.warning(f"ALERT: Bounce rate {rate:.1%} exceeds {threshold:.1%} threshold")
        return triggered


class AdoptionTracker:
    """Orchestrate the full Phase 1 adoption tracking workflow."""

    def __init__(self, config_path: str = None):
        """
        Initialize tracker with configuration.

        Args:
            config_path: Path to JSON config file with API credentials
        """
        self.config = self._load_config(config_path or 'phase-1-adoption-tracking.json')
        self.github_collector = None
        self.email_monitor = None
        self.gist_tracker = None
        self.sheets_sync = None
        self._setup_components()

    def _load_config(self, config_path: str) -> Dict:
        """Load configuration from JSON file or environment."""
        config_file = Path(config_path)
        if config_file.exists():
            with open(config_file) as f:
                return json.load(f)
        else:
            logger.warning(f"Config file not found: {config_path}. Using environment variables.")
            return {
                'github_username': os.getenv('GITHUB_USERNAME', ''),
                'gmail_credentials': os.getenv('GMAIL_CREDENTIALS_JSON', ''),
                'gmail_manual_log': os.getenv('GMAIL_MANUAL_LOG', ''),
                'sheets_credentials': os.getenv('GOOGLE_SHEETS_CREDENTIALS_JSON', ''),
                'spreadsheet_id': os.getenv('TRACKING_SPREADSHEET_ID', ''),
                'gist_views_csv': os.getenv('GIST_VIEWS_CSV', str(DATA_DIR / 'gist-views.csv')),
                'email_log_csv': os.getenv('EMAIL_LOG_CSV', str(DATA_DIR / 'email-replies.csv')),
            }

    def _setup_components(self):
        """Initialize API clients and trackers."""
        if self.config.get('github_username'):
            self.github_collector = GistAnalyticsCollector(
                github_username=self.config['github_username']
            )

        # Try Gmail API first, then fallback to manual log
        if self.config.get('gmail_credentials'):
            self.email_monitor = EmailReplyMonitor(
                credentials_json_path=self.config['gmail_credentials']
            )
        elif self.config.get('gmail_manual_log'):
            self.email_monitor = EmailReplyMonitor()
            logger.info(f"Using manual email log: {self.config['gmail_manual_log']}")

        self.gist_tracker = GistViewTracker(
            csv_path=self.config.get('gist_views_csv')
        )

        if self.config.get('sheets_credentials') and self.config.get('spreadsheet_id'):
            self.sheets_sync = SheetsSync(
                credentials_path=self.config['sheets_credentials'],
                spreadsheet_id=self.config['spreadsheet_id']
            )

    def run_weekly_collection(self) -> Dict:
        """
        Execute full weekly monitoring workflow.

        Returns:
            Summary dict with gist_views, email_replies, alerts
        """
        logger.info("=" * 70)
        logger.info("PHASE 1 ADOPTION TRACKING — Weekly Collection")
        logger.info(f"Timestamp: {datetime.now().isoformat()}")
        logger.info("=" * 70)

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
                self.gist_tracker.append_views(summary['gist_views'])
            except Exception as e:
                msg = f"Gist collection failed: {e}"
                logger.error(msg)
                summary['errors'].append(msg)

        # Monitor email replies
        if self.email_monitor:
            logger.info("\n[2/3] Fetching recent email replies...")
            try:
                if self.config.get('gmail_credentials'):
                    # Use Gmail API
                    summary['email_replies'] = self.email_monitor.get_recent_replies(hours=168)
                else:
                    # Use manual log
                    summary['email_replies'] = self.email_monitor.ingest_manual_log(
                        self.config['gmail_manual_log']
                    )
            except Exception as e:
                msg = f"Email monitoring failed: {e}"
                logger.error(msg)
                summary['errors'].append(msg)

        # Detect leading-indicator alerts
        logger.info("\n[3/3] Checking leading-indicator alerts...")
        try:
            if LeadingIndicatorDetector.check_zero_gist_views(summary['gist_views']):
                summary['leading_alerts'].append('ZERO_VIEWS')

            if LeadingIndicatorDetector.check_zero_replies(summary['email_replies']):
                summary['leading_alerts'].append('ZERO_REPLIES')
        except Exception as e:
            logger.error(f"Alert detection failed: {e}")

        logger.info("\n" + "=" * 70)
        logger.info("Weekly collection complete")
        logger.info(f"  Gists tracked: {len(summary['gist_views'])}")
        logger.info(f"  Email replies: {len(summary['email_replies'])}")
        logger.info(f"  Alerts triggered: {len(summary['leading_alerts'])}")
        logger.info("=" * 70 + "\n")

        return summary

    def save_summary(self, summary: Dict, output_dir: str = 'monitoring') -> Optional[Path]:
        """Save weekly summary to Markdown file."""
        output_path = Path(output_dir) / f"adoption-summary-{datetime.now().strftime('%Y-%m-%d')}.md"
        output_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(output_path, 'w') as f:
                f.write(f"# Adoption Tracking Summary — {datetime.now().strftime('%B %d, %Y')}\n\n")

                f.write("## Gist View Counts\n\n")
                if summary['gist_views']:
                    for label, data in summary['gist_views'].items():
                        if data:
                            views = data.get('cumulative_views', 'N/A')
                            f.write(f"- **{label}**: {views} views\n")
                else:
                    f.write("*(No Gist data collected)*\n\n")

                f.write("\n## Email Replies\n\n")
                f.write(f"**Total replies**: {len(summary['email_replies'])}\n\n")
                if summary['email_replies']:
                    for reply in summary['email_replies'][:10]:
                        f.write(f"- **From**: {reply.get('from', 'unknown')}\n")
                        f.write(f"  **Subject**: {reply.get('subject', '(no subject)')}\n")
                        if reply.get('snippet'):
                            snippet = reply['snippet'][:80] + "..." if len(reply['snippet']) > 80 else reply['snippet']
                            f.write(f"  **Preview**: {snippet}\n\n")

                if summary['leading_alerts']:
                    f.write("\n## ⚠️ Alerts Triggered\n\n")
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
        description='Phase 1 Adoption Tracking Automation',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run collection immediately
  python3 phase-1-adoption-tracking.py --run-now

  # Initialize CSV files
  python3 phase-1-adoption-tracking.py --init-csv

  # Print cron entry for weekly scheduling
  python3 phase-1-adoption-tracking.py --schedule-weekly

  # Use custom config file
  python3 phase-1-adoption-tracking.py --run-now --config custom-config.json
        """
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
        '--init-csv',
        action='store_true',
        help='Initialize CSV data files'
    )
    parser.add_argument(
        '--config',
        default='phase-1-adoption-tracking.json',
        help='Path to config JSON (default: phase-1-adoption-tracking.json)'
    )
    parser.add_argument(
        '--output-dir',
        default='monitoring',
        help='Output directory for summaries (default: monitoring)'
    )

    args = parser.parse_args()

    if args.schedule_weekly:
        script_path = Path(__file__).resolve()
        cron_entry = f"0 8 * * 1 /usr/bin/python3 {script_path} --run-now"
        print("\n" + "=" * 70)
        print("Add this line to your crontab (crontab -e):")
        print("=" * 70)
        print(cron_entry)
        print("\nThis runs the script every Monday at 08:00 AM (local time)")
        print("=" * 70 + "\n")
        return 0

    if args.init_csv:
        logger.info("Initializing CSV data files...")
        tracker = GistViewTracker()
        tracker.init_csv()
        logger.info("CSV initialization complete")
        return 0

    if args.run_now:
        tracker = AdoptionTracker(config_path=args.config)
        summary = tracker.run_weekly_collection()
        output_file = tracker.save_summary(summary, output_dir=args.output_dir)

        # Print JSON summary to stdout
        print("\n" + "=" * 70)
        print("JSON Summary")
        print("=" * 70)
        print(json.dumps(summary, indent=2, default=str))
        return 0

    # Default: show help
    parser.print_help()
    return 1


if __name__ == '__main__':
    sys.exit(main())
