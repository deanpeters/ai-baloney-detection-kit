#!/bin/bash
# Screenshot one HTML card to a 1600×900 PNG with headless Chrome.
# Usage: bash evals/scenarios/seagull-monday/snap.sh <card.html> <out.png>
set -euo pipefail
in="$1"; out="$2"
CHROME="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
abs="$(cd "$(dirname "$in")" && pwd)/$(basename "$in")"
mkdir -p "$(dirname "$out")"
"$CHROME" --headless=new --disable-gpu --hide-scrollbars --force-device-scale-factor=1 \
  --window-size=1600,900 --screenshot="$out" "file://$abs" >/dev/null 2>&1
[ -s "$out" ] && echo "snap: $out" || { echo "snap failed: $in" >&2; exit 1; }
