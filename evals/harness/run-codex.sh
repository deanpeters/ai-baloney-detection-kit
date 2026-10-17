#!/usr/bin/env bash
# Run every prepared workspace through Codex (a different model family from the author) in a
# read-only sandbox, a few at a time, and copy final messages into evals/runs/<label>/.
# Usage: evals/harness/run-codex.sh <workspace-root> <label> [model] [parallel]
set -euo pipefail
WS="$1"; LABEL="$2"; MODEL="${3:-gpt-5.5}"; PAR="${4:-5}"
REPO="$(cd "$(dirname "$0")/../.." && pwd)"
OUT="$REPO/evals/runs/$LABEL"
mkdir -p "$OUT"

run_one() {
  local dir="$1" id
  id="$(basename "$dir")"
  codex exec -m "$MODEL" -s read-only --skip-git-repo-check --ephemeral -C "$dir" \
    -o "$dir/output.md" "$(cat "$dir/prompt.txt")" > "$dir/log.txt" 2>&1 || echo "FAILED $id" >> "$WS/failures.txt"
  echo "done $id"
}
export -f run_one
export MODEL WS

ls -d "$WS"/*/ | xargs -P "$PAR" -I{} bash -c 'run_one "{}"'

for dir in "$WS"/*/; do
  id="$(basename "$dir")"
  [ -s "$dir/output.md" ] || continue
  {
    echo "<!-- Run $id · model $MODEL via codex exec · read-only sandbox · $(date +%Y-%m-%d) -->"
    echo "<!-- Prompt: $(tr '\n' ' ' < "$dir/prompt.txt") -->"
    echo
    cat "$dir/output.md"
  } > "$OUT/$id.md"
done
echo "Outputs in $OUT"
