#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../../.." && pwd)"
UI_DIR="$ROOT_DIR/scripts/install/ui"
VENV_DIR="$ROOT_DIR/.venv-installer"
PORT="${PANTHEON_INSTALLER_PORT:-8090}"
HOST="${PANTHEON_INSTALLER_HOST:-0.0.0.0}"

echo "Pantheon OS Installer UI"
echo "Root: $ROOT_DIR"
echo "Host: $HOST"
echo "Port: $PORT"

cd "$ROOT_DIR"

if ! command -v python3 >/dev/null 2>&1; then
  echo "ERROR: python3 is required."
  exit 1
fi

if [ ! -d "$VENV_DIR" ]; then
  echo "Creating installer virtual environment..."
  python3 -m venv "$VENV_DIR"
fi

# shellcheck source=/dev/null
source "$VENV_DIR/bin/activate"

python -m pip install --upgrade pip >/dev/null
python -m pip install -r "$UI_DIR/requirements.txt"

echo ""
echo "Open: http://NAS_IP:$PORT"
echo "Local: http://localhost:$PORT"
echo ""

exec python "$UI_DIR/installer_api.py"
