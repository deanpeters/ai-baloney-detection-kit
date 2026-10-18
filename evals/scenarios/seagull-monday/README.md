# Scenario: Seagull Monday

The keynote's recorded agent loop. A fictional SVP swoops into Slack on Monday with a roadmap tool he vibe-coded over the weekend and seven confident claims. A fresh Claude Code session walks the claims through the seven-step Baloney Funnel (outcome first) with the kit's own skills, reads the code as evidence, snaps a projector-style card at each stage, and writes him a reply.

| File | What it is |
|---|---|
| `../../../examples/seagull-monday.md` and `../../../examples/seagull-monday/roadmapgpt/` | The input: the Slack message and the weekend code (mirrored from the keynote's `demos/fixtures/`) |
| `RUNBOOK.md` | The prompt the session runs (stages, skills, cards, rules) |
| `card.css`, `snap.sh` | Card style and the headless-Chrome screenshot helper |
| `build-session.py` | Turns a run folder into `session.html` (scrollable) and `transcript.md` |
| `../../loop-cases/loop-11-seagull-monday.yaml` | The expected outcome, written before any run. Grade against it; never give it to the session. |

Run it from the repo root:

```bash
scripts/run-seagull-monday.sh          # unattended; opens session.html when done
scripts/run-seagull-monday.sh --live   # interactive, in your terminal
```

Each run lands in `evals/runs/seagull-monday-<stamp>/`. The morning of the keynote, run it unattended and keep that session open in a browser tab as the backup.
