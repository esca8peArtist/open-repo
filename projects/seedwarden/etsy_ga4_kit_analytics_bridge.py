#!/usr/bin/env python3
"""
Seedwarden Phase 2 Analytics Bridge — Automated Data Fetching

Fetches daily metrics from Etsy API, Google Analytics 4, and Kit API,
then outputs a CSV row ready to paste into the Daily Dashboard Google Sheet.

Usage:
    python etsy_ga4_kit_analytics_bridge.py --date 2026-06-01
    python etsy_ga4_kit_analytics_bridge.py --date 2026-06-01 --output daily-metrics.csv

Requirements:
    - Etsy API key (set ETSY_API_KEY env var or save to config/etsy-api-key.txt)
    - GA4 credentials (save service account JSON to config/ga4-credentials.json)
    - Kit API token (set KIT_API_TOKEN env var or save to config/kit-api-token.txt)
    - Python packages: requests, google-analytics-data (installed via requirements.txt)

Output:
    CSV row with columns: date, day_of_week, kit_signups, etsy_orders, etsy_revenue,
    email_open_rate, ig_followers, tiktok_followers, pinterest_followers, status, notes
"""

import os
import sys
import json
import csv
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, Optional, List
import requests

# Optional: Google Analytics imports (only loaded if GA4 setup is detected)
try:
    from google.analytics.data_v1beta import BetaAnalyticsDataClient
    from google.analytics.data_v1beta.types import RunReportRequest
    from google.oauth2.service_account import Credentials
    GA4_AVAILABLE = True
except ImportError:
    GA4_AVAILABLE = False
    print("⚠️  Warning: google-analytics-data not installed. GA4 fetching disabled.")
    print("   To enable: pip install google-analytics-data")


class EtsyAnalyticsFetcher:
    """Fetch Etsy orders and shop statistics via Etsy API."""

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://openapi.etsy.com/v3"
        self.session = requests.Session()
        self.session.headers.update({"x-api-key": api_key})

    def get_orders_since(self, start_date: datetime) -> Dict:
        """
        Fetch cumulative orders since a given date.

        Returns: {
            'total_orders': int,
            'total_revenue': float,
            'orders': List[{order_id, date, total, items}]
        }
        """
        try:
            # Etsy API: GET /v3/application/shops/{shop_id}/orders
            # Requires shop_id (retrieve from Shop > Settings)
            # Note: This endpoint requires OAuth, not just API key.
            # For now, return placeholder.
            print("⚠️  Note: Etsy API orders fetch requires OAuth setup (not yet implemented).")
            print("   Workaround: Manually enter Etsy orders from Shop Manager > Orders")
            return {
                'total_orders': None,
                'total_revenue': None,
                'orders': [],
                'note': 'Manual entry required'
            }
        except Exception as e:
            print(f"❌ Etsy API error: {e}")
            return {'error': str(e)}

    def get_shop_listings_stats(self) -> Dict:
        """
        Fetch listing view/favorite stats.
        Note: Requires shop_id and listing_ids.
        """
        # Placeholder: full implementation requires shop setup
        return {'note': 'Manual entry recommended for listing-level stats'}


class GA4AnalyticsFetcher:
    """Fetch Google Analytics 4 data via GA4 API."""

    def __init__(self, credentials_path: str):
        """Initialize with service account credentials JSON."""
        if not GA4_AVAILABLE:
            print("⚠️  GA4 fetching unavailable (google-analytics-data not installed)")
            return

        try:
            self.credentials = Credentials.from_service_account_file(credentials_path)
            self.client = BetaAnalyticsDataClient(credentials=self.credentials)
            self.property_id = os.getenv("GA4_PROPERTY_ID", "PROPERTY_ID_HERE")
            print(f"✓ GA4 client initialized (property: {self.property_id})")
        except Exception as e:
            print(f"❌ GA4 initialization error: {e}")
            self.client = None

    def get_traffic_by_source(self, date: datetime) -> Dict:
        """
        Fetch traffic for a given date, grouped by utm_source.

        Returns: {
            'kit': int,  # Kit email signups
            'instagram': int,
            'tiktok': int,
            'pinterest': int,
            'direct': int,
            'organic_search': int,
            'total': int
        }
        """
        if not self.client:
            return {'note': 'GA4 not configured'}

        try:
            date_str = date.strftime("%Y-%m-%d")
            request = RunReportRequest(
                property=f"properties/{self.property_id}",
                date_ranges=[{"start_date": date_str, "end_date": date_str}],
                dimensions=[{"name": "sessionSource"}],  # e.g., "google", "direct", "kit.com"
                metrics=[{"name": "sessions"}, {"name": "conversions"}],
            )
            response = self.client.run_report(request)

            traffic = {
                'kit': 0,
                'instagram': 0,
                'tiktok': 0,
                'pinterest': 0,
                'direct': 0,
                'organic_search': 0,
            }

            for row in response.rows:
                source = row.dimensions[0].value.lower()
                sessions = int(row.metric_values[0].value)
                conversions = int(row.metric_values[1].value)

                if 'kit' in source:
                    traffic['kit'] += conversions
                elif 'instagram' in source:
                    traffic['instagram'] += conversions
                elif 'tiktok' in source:
                    traffic['tiktok'] += conversions
                elif 'pinterest' in source:
                    traffic['pinterest'] += conversions
                elif 'direct' in source or 'self referrer' in source:
                    traffic['direct'] += sessions
                elif 'google' in source or 'organic' in source:
                    traffic['organic_search'] += sessions

            traffic['total'] = sum(traffic.values())
            return traffic

        except Exception as e:
            print(f"❌ GA4 query error: {e}")
            return {'error': str(e)}

    def get_email_metrics(self, date: datetime) -> Dict:
        """
        Fetch email engagement (open rate, click rate) for a given date.
        Note: Kit broadcasts may not appear in GA4 — prefer Kit API.
        """
        # Placeholder: Kit API is more reliable for email metrics
        return {'note': 'Use Kit API for email metrics (more accurate)'}


class KitAnalyticsFetcher:
    """Fetch Kit analytics via Kit API."""

    def __init__(self, api_token: str):
        self.api_token = api_token
        self.base_url = "https://api.kit.com/v4"
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"Bearer {api_token}",
            "Content-Type": "application/json"
        })

    def get_subscriber_count(self) -> Optional[int]:
        """Fetch total subscriber count."""
        try:
            response = self.session.get(f"{self.base_url}/subscribers/count")
            if response.status_code == 200:
                return response.json().get('count', 0)
            else:
                print(f"❌ Kit API error: {response.status_code}")
                return None
        except Exception as e:
            print(f"❌ Kit API error: {e}")
            return None

    def get_email_metrics(self) -> Dict:
        """
        Fetch email broadcast metrics (open rate, click rate).
        Note: Only works for recent broadcasts (API limitations).
        """
        try:
            # Simplified: returns most recent broadcast metrics
            response = self.session.get(f"{self.base_url}/broadcasts")
            if response.status_code == 200:
                broadcasts = response.json().get('broadcasts', [])
                if broadcasts:
                    latest = broadcasts[0]
                    return {
                        'open_rate': latest.get('open_rate', 0) * 100,  # Convert to %
                        'click_rate': latest.get('click_rate', 0) * 100,
                        'subject': latest.get('subject', 'N/A')
                    }
            return {'open_rate': None, 'click_rate': None}
        except Exception as e:
            print(f"❌ Kit email metrics error: {e}")
            return {'error': str(e)}

    def get_subscriber_tags(self) -> Dict[str, int]:
        """Fetch subscriber count by tag (zone-3, zone-4, etc.)."""
        try:
            response = self.session.get(f"{self.base_url}/tags")
            if response.status_code == 200:
                tags = response.json().get('tags', [])
                tag_counts = {}
                for tag in tags:
                    tag_name = tag.get('name', 'unknown')
                    subscriber_count = tag.get('subscriber_count', 0)
                    tag_counts[tag_name] = subscriber_count
                return tag_counts
            return {}
        except Exception as e:
            print(f"❌ Kit tags error: {e}")
            return {}


class SocialMediaAnalyticsFetcher:
    """
    Placeholder for social media follower counts.
    These require OAuth setup with each platform (manual for now).
    """

    @staticmethod
    def manual_entry_reminder():
        print("\n📱 Social Media Metrics (Requires Manual Entry)")
        print("   • Instagram: Go to Insights > Followers")
        print("   • TikTok: Go to Creator Center > Analytics > Followers")
        print("   • Pinterest: Go to Analytics > Overview > Followers")
        print("\nSave these values to config/social-baseline.json for tracking")


def load_config():
    """Load API credentials from environment or config files."""
    config = {
        'etsy_api_key': os.getenv('ETSY_API_KEY') or _read_config_file('etsy-api-key.txt'),
        'kit_api_token': os.getenv('KIT_API_TOKEN') or _read_config_file('kit-api-token.txt'),
        'ga4_credentials': _read_config_file('ga4-credentials.json') or 'config/ga4-credentials.json',
    }
    return config


def _read_config_file(filename: str) -> Optional[str]:
    """Read config from projects/seedwarden/config/{filename}."""
    path = Path('config') / filename
    if path.exists():
        with open(path, 'r') as f:
            return f.read().strip()
    return None


def fetch_daily_metrics(date: datetime) -> Dict:
    """
    Fetch all available metrics for a given date.

    Returns a dict with keys matching Daily Dashboard columns.
    """
    config = load_config()
    metrics = {
        'date': date.strftime("%m/%d"),
        'day_of_week': date.strftime("%A"),
        'kit_signups': None,
        'kit_new': None,
        'etsy_orders': None,
        'etsy_new': None,
        'etsy_revenue': None,
        'etsy_daily_revenue': None,
        'aov': None,
        'email_open_rate': None,
        'email_click_rate': None,
        'ig_followers': None,
        'ig_new': None,
        'tiktok_followers': None,
        'tiktok_new': None,
        'tiktok_views': None,
        'pinterest_followers': None,
        'pinterest_new': None,
        'status': 'MANUAL_ENTRY_REQUIRED',
        'notes': 'Partial data available'
    }

    # Fetch Kit data
    if config['kit_api_token']:
        print("🔄 Fetching Kit metrics...")
        kit = KitAnalyticsFetcher(config['kit_api_token'])
        kit_subs = kit.get_subscriber_count()
        if kit_subs:
            metrics['kit_signups'] = kit_subs

        email = kit.get_email_metrics()
        if 'open_rate' in email:
            metrics['email_open_rate'] = email.get('open_rate')
            metrics['email_click_rate'] = email.get('click_rate')

        tags = kit.get_subscriber_tags()
        print(f"   ✓ Subscriber tags: {tags}")

    # Fetch GA4 data
    if config['ga4_credentials'] and GA4_AVAILABLE:
        print("🔄 Fetching GA4 metrics...")
        ga4 = GA4AnalyticsFetcher(config['ga4_credentials'])
        traffic = ga4.get_traffic_by_source(date)
        # Note: GA4 tracks sessions, not direct conversion. Manual Etsy order entry recommended.

    # Placeholder for Etsy (requires OAuth)
    print("⚠️  Etsy metrics require manual entry (OAuth setup needed)")
    SocialMediaAnalyticsFetcher.manual_entry_reminder()

    return metrics


def format_csv_row(metrics: Dict) -> str:
    """Format metrics dict as CSV row."""
    row = [
        metrics.get('date', ''),
        metrics.get('day_of_week', ''),
        metrics.get('kit_signups', ''),
        metrics.get('kit_new', ''),
        metrics.get('etsy_orders', ''),
        metrics.get('etsy_new', ''),
        metrics.get('etsy_revenue', ''),
        metrics.get('etsy_daily_revenue', ''),
        metrics.get('aov', ''),
        metrics.get('email_open_rate', ''),
        metrics.get('email_click_rate', ''),
        metrics.get('ig_followers', ''),
        metrics.get('ig_new', ''),
        metrics.get('tiktok_followers', ''),
        metrics.get('tiktok_new', ''),
        metrics.get('tiktok_views', ''),
        metrics.get('pinterest_followers', ''),
        metrics.get('pinterest_new', ''),
        metrics.get('status', ''),
        metrics.get('notes', ''),
    ]
    return ','.join(str(v) if v is not None else '' for v in row)


def main():
    parser = argparse.ArgumentParser(
        description='Fetch Seedwarden Phase 2 analytics for a given date'
    )
    parser.add_argument('--date', required=True, help='Date (YYYY-MM-DD)')
    parser.add_argument('--output', help='Output CSV file (default: stdout)')
    args = parser.parse_args()

    try:
        date = datetime.strptime(args.date, "%Y-%m-%d")
    except ValueError:
        print("❌ Invalid date format. Use YYYY-MM-DD")
        sys.exit(1)

    print(f"\n📊 Fetching metrics for {date.strftime('%A, %B %d, %Y')}")
    print("=" * 60)

    metrics = fetch_daily_metrics(date)

    print("\n📋 Metrics Summary:")
    for key, value in metrics.items():
        if value is not None:
            print(f"   {key}: {value}")

    csv_row = format_csv_row(metrics)

    if args.output:
        with open(args.output, 'a', newline='') as f:
            f.write(csv_row + '\n')
        print(f"\n✓ Saved to {args.output}")
    else:
        print(f"\n📄 CSV Row (paste into Daily Dashboard):")
        print(csv_row)

    print("\n⚠️  Reminder: Complete manual entries in Daily Dashboard:")
    print("   • Etsy orders, revenue (from Etsy Shop Manager > Orders)")
    print("   • Social media followers (from platform analytics)")
    print("   • Email open rate (if Kit API not connected)")


if __name__ == '__main__':
    main()
