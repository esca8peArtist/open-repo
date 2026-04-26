#!/bin/bash
# Persistent chat session — runs inside tmux, restarts claude if it exits

cd /home/awank/dev/SuperClaude_Framework
[ -f "$HOME/.claude_env" ] && source "$HOME/.claude_env"

while true; do
  claude --dangerously-skip-permissions -n "Pi Chat" --remote-control-session-name-prefix "pi-chat"
  echo "[$(date)] Claude chat session ended. Restarting in 10 seconds..."
  sleep 10
done
