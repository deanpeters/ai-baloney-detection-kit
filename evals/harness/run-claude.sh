#!/usr/bin/env bash
# Run every prepared workspace through headless Claude Code (`claude -p`) with read-only tools,
# a few at a time, and copy final messages into evals/runs/<label>/. Use when Codex is unavailable;
# prefer a model other than the one that authored the skills.
# Usage: evals/harness/run-claude.sh <workspace-root> <label> [model] [parallel]
set -euo pipefail
WS="$1"; LABEL="$2"; MODEL="${3:-sonnet}"; PAR="${4:-4}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$REPO/evals/runs/$LABEL"
mkdir -p "$OUT"
rm -f "$WS/failures.txt"

run_one() {
  local dir="$1" id
  id="$(basename "$dir")"
  (cd "$dir" && env -u ANTHROPIC_API_KEY claude -p "$(cat prompt.txt)" --model "$MODEL" \
    --allowedTools "Read" "Glob" "Grep" \
    --disallowedTools "Bash" "Write" "Edit" "WebFetch" "WebSearch" "Agent" \
    > output.md 2> log.txt) || echo "FAILED $id" >> "$WS/failures.txt"
  echo "done $id"
}
export -f run_one
export MODEL WS

ls -d "$WS"/*/ | xargs -P "$PAR" -I{} bash -c 'run_one "{}"'

for dir in "$WS"/*/; do
  id="$(basename "$dir")"
  [ -s "$dir/output.md" ] || continue
  {
    echo "<!-- Run $id · model $MODEL via claude -p · read-only tools · $(date +%Y-%m-%d) -->"
    echo "<!-- Prompt: $(tr '\n' ' ' < "$dir/prompt.txt") -->"
    echo
    cat "$dir/output.md"
  } > "$OUT/$id.md"
done
echo "Outputs in $OUT"
