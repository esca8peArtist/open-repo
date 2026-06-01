#!/usr/bin/env python3
"""
Domain 58 Trump v. Barbara SCOTUS Opinion Monitor

Autonomously monitors for Trump v. Barbara (No. 25-365) Supreme Court ruling.
Polls SCOTUS opinions API hourly during court term (June-July 2026).
Triggers Domain 58 rapid-response workflow upon ruling issuance.
Integrates with phase-1-adoption-tracking-script.py for message routing.

Usage:
  python3 domain-58-scotus-monitor.py [--run-now | --continuous]

Environment:
  DISCORD_WEBHOOK_URL: Discord webhook for ruling alerts
  GITHUB_TOKEN: GitHub token for Gist update (optional, for announcement)

Deployment:
  crontab -e
  # Poll hourly during court term (June 1 - July 31)
  0 * * 6-7 /usr/bin/python3 /path/to/domain-58-scotus-monitor.py --run-now
"""

import os
import sys
import json
import logging
import requests
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional, Tuple
import re

# Configure logging
log_dir = Path(__file__).parent / 'logs'
log_dir.mkdir(exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(log_dir / 'scotus-monitor.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

class SCOTUSMonitor:
    """Monitor for Trump v. Barbara ruling on SCOTUS opinions API."""

    # Supreme Court opinions API endpoint
    SCOTUS_API = "https://www.supremecourt.gov/opinions/slipopinion.aspx"

    # Case identifiers
    CASE_NUMBER = "25-365"
    CASE_NAME = "Trump v. Barbara"
    DOCKET_URL = "https://www.supremecourt.gov/docket/25-365"

    # Monitoring state file
    STATE_FILE = Path(__file__).parent / 'domain-58-scotus-state.json'

    def __init__(self):
        """Initialize monitor with state tracking."""
        self.state = self._load_state()
        self.discord_webhook = os.getenv('DISCORD_WEBHOOK_URL')
        self.github_token = os.getenv('GITHUB_TOKEN')

    def _load_state(self) -> Dict:
        """Load monitoring state from file."""
        if self.STATE_FILE.exists():
            try:
                with open(self.STATE_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {
            'last_check': None,
            'ruling_found': False,
            'ruling_date': None,
            'ruling_url': None,
            'alerts_sent': 0
        }

    def _save_state(self) -> None:
        """Persist monitoring state."""
        self.state['last_check'] = datetime.now().isoformat()
        with open(self.STATE_FILE, 'w') as f:
            json.dump(self.state, f, indent=2)

    def check_supremecourt_gov(self) -> Optional[Tuple[str, str]]:
        """
        Check SCOTUS website for recent opinions.
        Returns: (opinion_url, opinion_text) or None
        """
        try:
            # Fetch SCOTUS slip opinion page
            response = requests.get(
                "https://www.supremecourt.gov/opinions/slipopinion/",
                timeout=10,
                headers={'User-Agent': 'Mozilla/5.0 (research automation)'}
            )
            response.raise_for_status()

            # Parse for Trump v. Barbara mentions
            # SCOTUS publishes opinions with case name and docket number
            patterns = [
                rf'Trump v\. Barbara.*?25-365',
                r'25-365.*?Trump v\. Barbara',
                r'Trump.*?Barbara.*?25-365',
            ]

            for pattern in patterns:
                if re.search(pattern, response.text, re.IGNORECASE | re.DOTALL):
                    # Look for PDF link in vicinity
                    pdf_pattern = r'href=["\']([^"\']*\.pdf)["\']'
                    pdf_match = re.search(pdf_pattern, response.text)
                    if pdf_match:
                        pdf_url = pdf_match.group(1)
                        if not pdf_url.startswith('http'):
                            pdf_url = 'https://www.supremecourt.gov' + pdf_url
                        return (pdf_url, response.text)

            return None

        except requests.RequestException as e:
            logger.error(f"Failed to check SCOTUS.gov: {e}")
            return None

    def check_scotusblog(self) -> Optional[str]:
        """
        Check SCOTUSBlog for case updates (live blog format).
        Returns: announcement URL if ruling found
        """
        try:
            # SCOTUSBlog has real-time live blog for major cases
            blog_url = "https://www.scotusblog.com/case-files/cases/trump-v-barbara/"
            response = requests.get(
                blog_url,
                timeout=10,
                headers={'User-Agent': 'Mozilla/5.0 (research automation)'}
            )
            response.raise_for_status()

            # Look for "decision issued" or "ruling handed down" markers
            decision_markers = [
                'decision issued',
                'ruling handed down',
                'opinion released',
                'Court has decided',
                '25-365'
            ]

            text_lower = response.text.lower()
            if any(marker in text_lower for marker in decision_markers):
                # Extract ruling timestamp from blog
                timestamp_pattern = r'(\d{4}-\d{2}-\d{2})|(\w+ \d{1,2}, \d{4})'
                timestamps = re.findall(timestamp_pattern, response.text)
                if timestamps:
                    return blog_url

            return None

        except requests.RequestException as e:
            logger.warning(f"Failed to check SCOTUSBlog: {e}")
            return None

    def check_narf_tribal_tracker(self) -> Optional[str]:
        """
        Check NARF Supreme Court Tribal Project for case updates.
        Native American Rights Fund tracks tribal cases in real-time.
        Returns: tracker URL if ruling found
        """
        try:
            tracker_url = "https://sct.narf.org/"
            response = requests.get(
                tracker_url,
                timeout=10,
                headers={'User-Agent': 'Mozilla/5.0 (research automation)'}
            )
            response.raise_for_status()

            # Look for Trump v. Barbara in tracker
            if 'Trump v. Barbara' in response.text and '25-365' in response.text:
                # Check if ruling date is mentioned
                if any(marker in response.text for marker in ['decided', 'issued', '2026']):
                    return tracker_url

            return None

        except requests.RequestException as e:
            logger.warning(f"Failed to check NARF tracker: {e}")
            return None

    def detect_ruling(self) -> Optional[Dict]:
        """
        Detect Trump v. Barbara ruling across sources.
        Returns: ruling info dict with date, holding, source URLs
        """
        logger.info(f"Checking for {self.CASE_NAME} ruling (Case No. {self.CASE_NUMBER})")

        # Check all sources in parallel
        sources_found = []

        scotus_result = self.check_supremecourt_gov()
        if scotus_result:
            sources_found.append(('SCOTUS.gov', scotus_result[0]))

        blog_result = self.check_scotusblog()
        if blog_result:
            sources_found.append(('SCOTUSBlog', blog_result))

        narf_result = self.check_narf_tribal_tracker()
        if narf_result:
            sources_found.append(('NARF Tracker', narf_result))

        if sources_found:
            logger.info(f"✅ RULING DETECTED! Confirmed on {len(sources_found)} source(s)")
            return {
                'detected': True,
                'case': self.CASE_NAME,
                'case_no': self.CASE_NUMBER,
                'detection_date': datetime.now().isoformat(),
                'sources': sources_found,
                'docket_url': self.DOCKET_URL
            }
        else:
            logger.info(f"⏳ No ruling detected yet. Last check: {datetime.now().isoformat()}")
            return None

    def send_discord_alert(self, ruling_info: Dict) -> bool:
        """Send Discord notification for ruling detection."""
        if not self.discord_webhook:
            logger.warning("DISCORD_WEBHOOK_URL not set — skipping notification")
            return False

        try:
            # Build Discord message
            sources_text = '\n'.join([
                f"  • {source}: {url}"
                for source, url in ruling_info['sources']
            ])

            payload = {
                'content': f"🚨 **SCOTUS RULING DETECTED: {ruling_info['case']}**",
                'embeds': [{
                    'title': f"{ruling_info['case']} (No. {ruling_info['case_no']})",
                    'description': "The Supreme Court has issued its ruling in this case. Domain 58 rapid-response protocol activated.",
                    'color': 16711680,  # Red
                    'fields': [
                        {
                            'name': 'Detection Sources',
                            'value': sources_text,
                            'inline': False
                        },
                        {
                            'name': 'Next Steps',
                            'value': "1. Verify ruling via `domain-58-rapid-response-checklist.md`\n2. Execute routing decision from `TRUMP_V_BARBARA_RAPID_RESPONSE_PROTOCOL.md`\n3. Update `domains/domain-58-tribal-sovereignty.md` per checklist\n4. Activate distribution via `domain-58-execution-checklist.md`",
                            'inline': False
                        },
                        {
                            'name': 'Docket',
                            'value': ruling_info['docket_url'],
                            'inline': False
                        }
                    ],
                    'timestamp': ruling_info['detection_date']
                }]
            }

            response = requests.post(
                self.discord_webhook,
                json=payload,
                timeout=10
            )
            response.raise_for_status()

            logger.info(f"✅ Discord alert sent successfully")
            self.state['alerts_sent'] += 1
            return True

        except requests.RequestException as e:
            logger.error(f"Failed to send Discord alert: {e}")
            return False

    def activate_rapid_response(self, ruling_info: Dict) -> None:
        """
        Activate Domain 58 rapid-response workflow.
        Records ruling detection state and queues rapid-response tasks.
        """
        logger.info("Activating Domain 58 rapid-response workflow...")

        # Update state with ruling info
        self.state['ruling_found'] = True
        self.state['ruling_date'] = ruling_info['detection_date']
        self.state['ruling_sources'] = [s[0] for s in ruling_info['sources']]

        # Create rapid-response activation file
        activation_file = Path(__file__).parent.parent / 'domain-58-rapid-response-ACTIVATED.json'
        with open(activation_file, 'w') as f:
            json.dump({
                'status': 'ACTIVATED',
                'case': ruling_info['case'],
                'case_no': ruling_info['case_no'],
                'detection_timestamp': ruling_info['detection_date'],
                'sources': ruling_info['sources'],
                'next_action': 'Execute domain-58-rapid-response-checklist.md steps 0-1 to verify ruling',
                'decision_tree': 'See TRUMP_V_BARBARA_RAPID_RESPONSE_PROTOCOL.md for outcome routing'
            }, f, indent=2)

        logger.info(f"✅ Rapid-response activated. State file: {activation_file}")
        logger.info(f"📋 Next step: Review domain-58-rapid-response-checklist.md for verification and routing")

    def run(self) -> int:
        """Execute monitoring check."""
        logger.info(f"=== Domain 58 SCOTUS Monitor started ({self.CASE_NAME}) ===")

        # Skip if already detected
        if self.state.get('ruling_found'):
            logger.info(f"✅ Ruling already detected on {self.state.get('ruling_date')}. Monitor complete.")
            return 0

        # Check for ruling
        ruling_info = self.detect_ruling()

        if ruling_info:
            # Send alerts
            self.send_discord_alert(ruling_info)

            # Activate rapid-response workflow
            self.activate_rapid_response(ruling_info)

            # Update state
            self._save_state()

            logger.info(f"=== Domain 58 Ruling Detection Complete ===")
            return 0
        else:
            # Save checkpoint for next run
            self._save_state()
            return 0

def main():
    """Entry point."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Monitor for Trump v. Barbara SCOTUS ruling'
    )
    parser.add_argument(
        '--run-now',
        action='store_true',
        help='Run check immediately'
    )
    parser.add_argument(
        '--continuous',
        action='store_true',
        help='Run continuously (for testing only)'
    )
    args = parser.parse_args()

    monitor = SCOTUSMonitor()

    if args.continuous:
        logger.info("Running in continuous mode (for testing)")
        while True:
            monitor.run()
            logger.info("Sleeping 3600 seconds until next check...")
            __import__('time').sleep(3600)
    else:
        return monitor.run()

if __name__ == '__main__':
    sys.exit(main())
