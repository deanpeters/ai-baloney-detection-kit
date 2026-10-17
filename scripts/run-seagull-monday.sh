#!/bin/bash
# Run the Seagull Monday scenario in a fresh Claude Code session and capture it.
#   scripts/run-seagull-monday.sh          unattended (claude -p): records everything, opens session.html at the end
#   scripts/run-seagull-monday.sh --live   interactive: watch it run in your terminal (on stage, or the morning of)
# Output: evals/runs/seagull-monday-<stamp>/ with stage files, cards/, shots/, SESSION.md, session.html, transcript.
set -euo pipefail
cd "$(dirname "$0")/.."
STAMP=$(date +%Y-%m-%d-%H%M)
SESSION="evals/runs/seagull-monday-$STAMP"
mkdir -p "$SESSION/cards" "$SESSION/shots"
PROMPT=$(sed "s#{{SESSION}}#$SESSION#g" evals/scenarios/seagull-monday/RUNBOOK.md)
TOOLS="Skill,Read,Write,Edit,Glob,Grep,Bash(bash evals/scenarios/seagull-monday/snap.sh:*),Bash(ls:*),Bash(mkdir:*)"   # one quoted, comma-separated argument
echo "Session: $SESSION"
if [ "${1:-}" = "--live" ]; then
  claude --permission-mode acceptEdits --allowedTools "$TOOLS" -- "$PROMPT"
else
  claude -p --permission-mode acceptEdits --allowedTools "$TOOLS" --output-format stream-json --verbose -- "$PROMPT" > "$SESSION/transcript.jsonl"
fi
python3 evals/scenarios/seagull-monday/build-session.py "$SESSION"
open "$SESSION/session.html" 2>/dev/null || true
