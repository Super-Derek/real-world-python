#!/usr/bin/env bash
set -euo pipefail

CHDIR="${1:-}"
[ -z "$CHDIR" ] && { echo "Usage: $0 <chapter_dir>"; exit 1; }
[ ! -d "$CHDIR" ] && { echo "Error: directory '$CHDIR' does not exist."; exit 1; }

cd "$CHDIR"

# 1) venv
python3 -m venv .venv
# shellcheck disable=SC1091
source .venv/bin/activate

# 2) tooling
python -m pip install --upgrade pip
pip install black ruff pytest

# 3) seed files (idempotent)
[ -f requirements.txt ] || cat > requirements.txt <<'REQ'
black
ruff
pytest
REQ

[ -d src ] || mkdir src
[ -f src/__init__.py ] || touch src/__init__.py

[ -f .env.example ] || cat > .env.example <<'ENV'
# Put chapter-specific environment variables here
ENV

[ -d .vscode ] || mkdir .vscode
cat > .vscode/settings.json <<'JSON'
{
  "python.defaultInterpreterPath": "${workspaceFolder}/.venv/bin/python",
  "editor.formatOnSave": true,
  "python.testing.pytestEnabled": true
}
JSON

echo "✅ Scaffolding complete in $(pwd)"
