#!/bin/sh
# Runs before n8n start on first boot: import credentials + workflow.
set -e

MARKER="/home/node/.n8n/.local-docker-ready"

if [ -f "$MARKER" ]; then
  exec n8n start
fi

echo "[n8n-init] First boot — importing local Docker workflow bundle..."

if [ -f /bootstrap/credentials.json ]; then
  n8n import:credentials --input=/bootstrap/credentials.json || true
fi

if [ -f /bootstrap/workflow.json ]; then
  n8n import:workflow --input=/bootstrap/workflow.json --activeState=fromJson || true
fi

touch "$MARKER"
echo "[n8n-init] Import complete."

exec n8n start
