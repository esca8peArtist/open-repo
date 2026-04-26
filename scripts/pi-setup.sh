#!/bin/bash
# Pi 5 Setup Script — Autonomous Claude Orchestrator
# Run this on the Raspberry Pi after SSH-ing in
# Usage: bash pi-setup.sh
#
# Prerequisites:
#   - Raspberry Pi OS (64-bit) or Ubuntu Server installed
#   - Internet connection
#   - You are logged in as a non-root user (e.g., 'anya' or 'pi')

set -e

echo "=== Claude Orchestrator Pi Setup ==="
echo "Running as: $(whoami) on $(hostname)"
echo ""

# ── 1. System packages ──────────────────────────────────────────────────────
echo "[1/8] Updating system packages..."
sudo apt-get update -qq
sudo apt-get install -y -qq tmux git curl wget build-essential

# ── 2. Node.js 20 (required for Claude Code CLI) ────────────────────────────
echo "[2/8] Installing Node.js 20..."
if ! command -v node &>/dev/null || [[ $(node -v | cut -d. -f1 | tr -d 'v') -lt 18 ]]; then
  curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
  sudo apt-get install -y nodejs
fi
echo "Node: $(node -v), npm: $(npm -v)"

# ── 3. Claude Code CLI ───────────────────────────────────────────────────────
echo "[3/8] Installing Claude Code..."
sudo npm install -g @anthropic-ai/claude-code
echo "Claude Code: $(claude --version)"

# ── 4. uv (Python package manager) ──────────────────────────────────────────
echo "[4/8] Installing uv..."
if ! command -v uv &>/dev/null; then
  curl -LsSf https://astral.sh/uv/install.sh | sh
  export PATH="$HOME/.cargo/bin:$PATH"
fi
echo "uv: $(uv --version)"

# ── 5. Environment variables ─────────────────────────────────────────────────
echo "[5/8] Setting up environment variables..."
ENV_FILE="$HOME/.claude_env"

if [ ! -f "$ENV_FILE" ]; then
  cat > "$ENV_FILE" << 'ENVEOF'
# Claude Orchestrator Environment
# Fill in the values below then run: source ~/.claude_env

export ANTHROPIC_API_KEY=""         # Your Anthropic API key
export DISCORD_WEBHOOK_URL=""       # Discord webhook URL for notifications
export CLAUDE_WORKSPACE="/home/$(whoami)/dev/SuperClaude_Framework"
ENVEOF
  echo ""
  echo "  IMPORTANT: Edit $ENV_FILE and fill in:"
  echo "    ANTHROPIC_API_KEY — from console.anthropic.com"
  echo "    DISCORD_WEBHOOK_URL — from Discord channel settings > Integrations > Webhooks"
  echo ""
else
  echo "  $ENV_FILE already exists, skipping."
fi

# Add to .bashrc if not already there
if ! grep -q "claude_env" "$HOME/.bashrc"; then
  echo "" >> "$HOME/.bashrc"
  echo "# Claude orchestrator environment" >> "$HOME/.bashrc"
  echo "[ -f ~/.claude_env ] && source ~/.claude_env" >> "$HOME/.bashrc"
fi

# ── 6. Clone / sync the workspace ────────────────────────────────────────────
echo "[6/8] Setting up workspace..."
WORKSPACE_DIR="$HOME/dev/SuperClaude_Framework"
mkdir -p "$HOME/dev"

if [ ! -d "$WORKSPACE_DIR" ]; then
  echo "  Workspace not found at $WORKSPACE_DIR"
  echo "  You need to either:"
  echo "    a) git clone your repo here: git clone <your-repo-url> $WORKSPACE_DIR"
  echo "    b) Or sync files from your dev machine via rsync:"
  echo "       rsync -avz /path/on/dev-machine/ pi@<PI_IP>:$WORKSPACE_DIR/"
  echo ""
  echo "  After setting up the workspace, re-run this script or continue manually."
else
  echo "  Workspace found at $WORKSPACE_DIR"
fi

# ── 7. tmux config ────────────────────────────────────────────────────────────
echo "[7/8] Setting up tmux..."
TMUX_CONF="$HOME/.tmux.conf"
if [ ! -f "$TMUX_CONF" ]; then
  cat > "$TMUX_CONF" << 'TMUXEOF'
# Keep sessions alive
set -g history-limit 50000
set -g display-time 4000
set -g status-interval 5
set -g default-terminal "screen-256color"

# Mouse support
set -g mouse on

# Prevent accidental session exit
bind-key q confirm-before kill-session
TMUXEOF
fi

# ── 8. systemd user service ───────────────────────────────────────────────────
echo "[8/8] Installing systemd user service..."

SYSTEMD_DIR="$HOME/.config/systemd/user"
mkdir -p "$SYSTEMD_DIR"

cat > "$SYSTEMD_DIR/claude-orchestrator.service" << SERVICEEOF
[Unit]
Description=Claude Autonomous Orchestrator
After=network.target

[Service]
Type=simple
WorkingDirectory=%h/dev/SuperClaude_Framework
EnvironmentFile=%h/.claude_env
ExecStart=/usr/bin/tmux new-session -d -s claude-auto -x 220 -y 50 '%h/dev/SuperClaude_Framework/scripts/start-orchestrator.sh'
ExecStop=/usr/bin/tmux kill-session -t claude-auto
Restart=on-failure
RestartSec=30

[Install]
WantedBy=default.target
SERVICEEOF

# Enable lingering so service runs before login
loginctl enable-linger "$(whoami)" 2>/dev/null || true

# Enable the service
systemctl --user daemon-reload
systemctl --user enable claude-orchestrator.service

echo ""
echo "=== Setup Complete ==="
echo ""
echo "Next steps:"
echo "  1. Edit ~/.claude_env and fill in ANTHROPIC_API_KEY and DISCORD_WEBHOOK_URL"
echo "  2. Set up workspace: clone your repo or rsync files to ~/dev/SuperClaude_Framework"
echo "  3. Authenticate Claude Code: cd ~/dev/SuperClaude_Framework && claude (then login)"
echo "  4. Test the orchestrator manually first: bash ~/dev/SuperClaude_Framework/scripts/start-orchestrator.sh"
echo "  5. Once working, start the service: systemctl --user start claude-orchestrator.service"
echo "  6. Check status: systemctl --user status claude-orchestrator.service"
echo "  7. Watch it run: tmux attach -t claude-auto"
echo ""
echo "To detach from tmux without stopping it: Ctrl+B then D"
echo "To reattach later: tmux attach -t claude-auto"
echo "To view logs: journalctl --user -u claude-orchestrator.service -f"
