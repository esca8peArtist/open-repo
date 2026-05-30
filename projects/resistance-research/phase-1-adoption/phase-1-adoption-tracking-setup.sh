#!/bin/bash
# Phase 1 Adoption Tracking Setup Script
#
# Sets up directory structure, dependencies, and cron scheduling
# for Phase 1 adoption tracking automation.
#
# Usage:
#   bash phase-1-adoption-tracking-setup.sh

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$(dirname "$SCRIPT_DIR")")"

echo "=========================================="
echo "Phase 1 Adoption Tracking Setup"
echo "=========================================="
echo ""

# 1. Create directory structure
echo "[1/4] Creating directory structure..."
mkdir -p "$SCRIPT_DIR/data"
mkdir -p "$SCRIPT_DIR/logs"
mkdir -p "$SCRIPT_DIR/config"
echo "✓ Created: data/, logs/, config/"
echo ""

# 2. Copy config template
echo "[2/4] Setting up configuration..."
if [ ! -f "$SCRIPT_DIR/adoption-tracking-config.json" ]; then
    if [ -f "$SCRIPT_DIR/adoption-tracking-config.json.template" ]; then
        cp "$SCRIPT_DIR/adoption-tracking-config.json.template" "$SCRIPT_DIR/adoption-tracking-config.json"
        echo "✓ Created adoption-tracking-config.json from template"
        echo "  → Edit this file with your GitHub username and Gist IDs"
    else
        echo "⚠ Template not found. Creating basic config..."
        cat > "$SCRIPT_DIR/adoption-tracking-config.json" <<'EOF'
{
  "github_username": "YOUR-GITHUB-USERNAME",
  "github_gist_ids": [
    "GIST-ID-1",
    "GIST-ID-2"
  ],
  "organization_contacts": [
    {
      "name": "organization-name",
      "email": "contact@org.org",
      "sector": "law-school"
    }
  ],
  "gmail_enabled": false,
  "gmail_credentials_path": "/path/to/credentials.json",
  "log_dir": "./logs",
  "data_dir": "./data"
}
EOF
        echo "✓ Created basic adoption-tracking-config.json"
        echo "  → Edit this file with your GitHub username and Gist IDs"
    fi
else
    echo "✓ adoption-tracking-config.json already exists"
fi
echo ""

# 3. Install Python dependencies
echo "[3/4] Installing Python dependencies..."
echo ""

# Check if pip3/python3 is available
if ! command -v python3 &> /dev/null; then
    echo "✗ Python 3 not found. Please install Python 3.10+"
    exit 1
fi

echo "Installing: requests (required)"
python3 -m pip install --quiet requests 2>/dev/null || {
    echo "⚠ pip install failed; trying --user flag..."
    python3 -m pip install --quiet --user requests
}

echo "Installing: Google API libraries (optional, for Gmail monitoring)"
python3 -m pip install --quiet google-auth-oauthlib google-auth-httplib2 google-api-python-client 2>/dev/null || {
    echo "  → Skipped (optional; needed only if using Gmail monitoring)"
}

echo "✓ Dependencies installed"
echo ""

# 4. Verify script is executable
echo "[4/4] Setting up cron scheduling..."
chmod +x "$SCRIPT_DIR/phase-1-adoption-tracking-script.py"
echo "✓ Script is executable"
echo ""

# Print cron setup instructions
cat << 'EOF'
=========================================="
Setup Complete!
=========================================="

Next steps:

1. Configure your tracking:
   Edit adoption-tracking-config.json with:
   - github_username: Your GitHub username
   - github_gist_ids: List of Gist IDs to track

   Example:
     "github_username": "my-org",
     "github_gist_ids": ["2dec7fd03b08ab5b41c55d402f44c261"],

2. (Optional) Enable Gmail monitoring:
   If you want to track email replies via Gmail API:
   - Run: python3 oauth2_login.py
   - Follow the browser login flow
   - Set "gmail_enabled": true in config.json

3. Schedule weekly collection:
   The script runs every Monday at 09:00 UTC.
   To install the cron entry:

   crontab -e
   # Add this line:
   0 9 * * 1 cd SCRIPT_PATH && python3 phase-1-adoption-tracking-script.py

   Replace SCRIPT_PATH with: EOF
echo "   $SCRIPT_DIR"
cat << 'EOF'

4. Test the script:
   python3 phase-1-adoption-tracking-script.py

   Should complete without errors and log to:
   - logs/adoption-tracking.log
   - data/gist-view-tracking.json
   - data/email-replies.json (if Gmail enabled)

Questions?
See PHASE_1_ADOPTION_TRACKING_DEPLOYMENT.md for detailed documentation.
EOF

echo ""
