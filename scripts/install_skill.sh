#!/usr/bin/env bash
set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SRC="$REPO_DIR/skills/book-transfer-converter"
DEST_ROOT="${HOME}/.codex/skills"
DEST="$DEST_ROOT/book-transfer-converter"

mkdir -p "$DEST_ROOT"
rm -rf "$DEST"
cp -R "$SRC" "$DEST"

echo "Installed skill: $DEST"
echo "Updated at: $(date '+%Y-%m-%d %H:%M:%S')"
