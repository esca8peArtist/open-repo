#!/usr/bin/env python3
"""
Gmail OAuth2 Setup Helper

One-time script to obtain Google OAuth2 credentials for Gmail API access.

Prerequisites:
  1. Create a Google Cloud project: https://console.cloud.google.com
  2. Enable Gmail API
  3. Create OAuth2 desktop app credentials
  4. Download credentials.json to this directory

Usage:
  python3 oauth2_login.py

This script will:
  1. Prompt you for the path to your credentials.json
  2. Open a browser for Gmail API consent flow
  3. Create token.json (saved credentials for future runs)
  4. Print instructions for configuring adoption-tracking-config.json
"""

import sys
from pathlib import Path
from datetime import datetime

try:
    from google.auth.transport.requests import Request
    from google.oauth2.credentials import Credentials
    from google.auth.oauthlib.flow import InstalledAppFlow
    HAS_GOOGLE = True
except ImportError:
    HAS_GOOGLE = False
    print("ERROR: Google libraries not installed.")
    print("Run: pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    sys.exit(1)


GMAIL_SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Run OAuth2 authentication flow."""
    print("=" * 70)
    print("Gmail OAuth2 Setup for Phase 1 Adoption Tracking")
    print("=" * 70)
    print()

    # Locate credentials.json
    script_dir = Path(__file__).parent
    credentials_path = script_dir / "credentials.json"

    if not credentials_path.exists():
        print("Credentials file not found at:", credentials_path)
        print()
        print("To set up Gmail monitoring:")
        print("  1. Visit: https://console.cloud.google.com")
        print("  2. Create a new project")
        print("  3. Enable 'Gmail API'")
        print("  4. Create OAuth2 credentials (Desktop app)")
        print("  5. Download as 'credentials.json'")
        print("  6. Save to:", script_dir)
        print()
        sys.exit(1)

    print(f"Found credentials: {credentials_path}")
    print()

    # Run OAuth2 flow
    print("Opening browser for Gmail API authorization...")
    print()

    try:
        flow = InstalledAppFlow.from_client_secrets_file(
            str(credentials_path),
            GMAIL_SCOPES
        )
        creds = flow.run_local_server(port=0, open_browser=True)

        # Save token
        token_path = script_dir / "token.json"
        with open(token_path, 'w') as token_file:
            token_file.write(creds.to_json())

        print()
        print("=" * 70)
        print("SUCCESS!")
        print("=" * 70)
        print()
        print(f"✓ Credentials saved to: {token_path}")
        print()
        print("Next steps:")
        print()
        print("1. Update adoption-tracking-config.json:")
        print()
        print('   "gmail_enabled": true,')
        print(f'   "gmail_credentials_path": "{credentials_path}",')
        print()
        print("2. The script will now monitor email replies in your inbox")
        print("   (searches label: Phase1Responses, since June 1, 2026)")
        print()
        print("3. Test the configuration:")
        print("   python3 phase-1-adoption-tracking-script.py")
        print()
        print("Note: Token expires periodically. If you see 401 errors,")
        print("delete token.json and re-run this script.")
        print()

    except Exception as e:
        print()
        print("ERROR: Authentication failed")
        print(f"Details: {e}")
        print()
        print("Troubleshooting:")
        print("  - Verify credentials.json is valid (from Google Cloud Console)")
        print("  - Ensure browser auto-opened for authorization")
        print("  - Check internet connection")
        print()
        sys.exit(1)


if __name__ == '__main__':
    main()
