# Grades: deck 11 stage demo, 2026-10-15

The live demo in deck 11 (slide 51) is `/bdk-receipts @examples/deck-fatigue-index.md`.
- **What the slides need next:**
  - Slide 52: "Busted by my own tool."
  - Slide 53: Claim (412 slides seen today) → Challenge (Where'd that number come from?) → Evidence (None. I made it up.) → Better decision (Keep the joke. Drop the stat.)
- **Constraint:** the output must read on a projector in under a minute.
- **The skill change being tested:** `bdk-receipts` gained a default **stage card** (≤ 200 words, no tables) that always ends on Claim / Challenge / Evidence / Better decision. The full ledger is now given on request.
- **How the runs were made:** Claude Code 2.1.301, default model, `claude -p "/bdk-receipts @examples/deck-fatigue-index.md"` from the repo root (the exact stage command), read-only tools, a fresh session each run.
- **Grading:** by the authoring assistant, not blind and not human, against `notes/deck-fatigue-index-expected.md` in the keynote repo.

| Runs | Fixture | Words | Stage card | Headline claim | Rating | Ending |
|---|---|---|---|---|---|---|
| [R1](first-fixture/R1.md)–[R3](first-fixture/R3.md) | First draft, no named headline | 142–163 | 3 of 3 | "Deck fatigue syndrome" in 2 of 3 | Total Crapola, 3 of 3 | Four lines, 3 of 3; "label it a joke" in 3 of 3 |
| [R4](R4.md)–[R6](R6.md) | **Final:** `**Headline:** 412 slides seen today.` added | 144–163 | **3 of 3** | **"412 slides seen today," 3 of 3** | **Total Crapola, 3 of 3** | **Four lines, 3 of 3.** Better decision: "Run it as a joke, or count" / "call it a guess" / "call it a bit" |

**Result for the shipping configuration:**
- The stage card every time.
- The headline and rating every time.
- An ending that sets up slide 53 every time.
- **Variance:** the exact "Better decision" wording varies. Dean's slide 53 line ("Keep the joke. Drop the stat.") lands as the callback whichever wording appears.
- **Every run also SENDS BACK the "agentic" count.** The fixture says "still counting" but the method says "not counted." That's a fair catch, and a bonus laugh line on stage.

**Not run:** a cross-model check. `codex exec` refused both its configured default and `gpt-5.5` for this ChatGPT account. The stage runs Claude Code, so this doesn't block the demo.
