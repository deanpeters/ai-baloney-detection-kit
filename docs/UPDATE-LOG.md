# Update log: 2026-10-11, the Baloney Funnel build

What changed, why, and what was decided on Dean's behalf. Dean asked for the repository to be updated **without his input**, using best judgment, until the skills were written, shaped like his other skill repos, and tested. Every judgment call is listed in §3 so it can be reversed. The plan this executes is [UPDATE-PLAN.md](UPDATE-PLAN.md) (revision 2); the evidence is in [VERIFICATION.md](../evals/VERIFICATION.md).

**Not done, on purpose:** no `git init`, commit, publish, or install; nothing in `~/Code/chaos-confusion-and-crapola` (the keynote repo) was edited; no real company or person appears in any new example.

---

## 1. What changed

### Layout (now matches ADLC, Precedents, Market Intelligence, Discovery Lab)

| Before | After |
|---|---|
| `.claude/skills/<name>/` | `skills/<name>/`, with `.claude/skills` → `../skills` as a symlink so `/bdk-…` still works from this folder (the keynote's stage commands) |
| No plugin manifests | `.claude-plugin/plugin.json` + `marketplace.json`; `.codex-plugin/plugin.json` (plugin name `bdk`, version 0.2.0, `"skills": "./skills/"`) |
| No catalog | [`catalog/INDEX.md`](../catalog/INDEX.md): funnel tiers, then utilities ("these are not tiers"), then quick checks, then hand-offs |
| No authoring spec | [`docs/SKILL-SPEC.md`](SKILL-SPEC.md): tiers, the utility rule (max six), required sections, frontmatter, examples |
| `SKILL.md` + bundled contract only | Every funnel skill and utility also has `template.md`, `examples/worked-example.md`, `examples/weak-example.md`; quick checks have both examples |
| Minimal frontmatter | Rich canonical frontmatter (intent, tier, sift question, best-for, scenarios, produces, interface…), projected to the strict portable shape and a generated `agents/openai.yaml` in the ZIPs |

### The method: the Baloney Funnel

The five checks now run as a **process of elimination by tiers**, cheapest first (from Dean's presentation outline):

| Tier | Question | Skills |
|---|---|---|
| 1 Chaos | Is it real, and is it still true? | `bdk-receipts`, `bdk-sell-by` |
| 2 Confusion | What do we actually know, and does it apply to us? | `bdk-labels`, `bdk-context-pantry` |
| 3 Crapola | Would reality disagree? | `bdk-taste-test` |
| 4 Considered | Pursue, pivot, or punt? | `bdk-four-risks` (**new**) |
| — | Whole funnel, one claim or many | `bdk-detector` (reworked: funnel report) |

- **Four exits** from any tier: Pass · Sifted out · Send back · Pivot. Missing is not failed; stale is not false.
- **The four risks** with Dean's exact questions on the Monday-grid 2×2 (Should we? / Can we? × For them / For us). **Usable** is now a full risk everywhere the kit listed three.
- **Feasible-only flag** when a demo is the only evidence: "AI made building cheap. The demo proves buildable, not feasible."
- **Decision record** for every move: scope, deciding square, owner role, by-when, what would change it, where it goes next, re-check triggers. Truth has a sell-by date.
- **Move the bet, not just the request** (added after the first test run; §4): a failed Can-we or Viable square with a nameable fix is a Pivot, never a Punt.

### Skills

| Skill | Status |
|---|---|
| `bdk-receipts`, `bdk-sell-by`, `bdk-labels`, `bdk-context-pantry` | Reworked: tier, sift question, key concepts with violation signals, human decision gate with exits, four-risk squares, template, worked and weak examples. Their proven methods were kept. |
| `bdk-taste-test` | Reworked as above, plus Usable as a full risk, riskiest-square-first test selection, and the feasible-only flag |
| `bdk-detector` | Reworked into the whole-funnel runner with a funnel report |
| `bdk-four-risks` | **New.** The Considered tier: grid, scoped moves, decision record |
| `bdk-util-slice-the-pitch` | **New utility.** Turns a deck, release, or roadmap into atomic claims for the funnel; never judges |
| `bdk-skill-sorter` | Updated to deck 9: **Truth** replaces Leverage (with a "formerly Leverage" note), each square's question, a move per item, a projector-sized 2×2, Hired · Fired · Promoted mapped to the grid, and Monday as the four-risk moves |
| `bdk-value-or-theater` | Light update: the move under each verdict (VALUE → PURSUE, THEATER → PUNT, NOT YET → PIVOT) and the PASS-OFF note for chores |

### Shared contract (`reference/assessment-contract.md`)

Added: the funnel and exits, the two families (work vs. claims), the four risks and grid-reading rules, move-the-bet rule, decision record, and the hand-off list. Regenerated into every funnel skill and utility.

### Documents

- **README:** two families and the bridge line; a Baloney Funnel section; four risks in check 5; Curve ↔ Funnel ↔ Scale equivalence; repo map; ProductFest table rows for the funnel, the skills in pairs, the Monday grid, and the Sort grid; closing line is now *Chaos → Confusion → Crapola → Considered → Truth*.
- **CLAUDE.md:** vocabulary for the funnel, exits, four risks, two families, Truth/pass-off, three lenses; skills location and inventory.
- **CONSTITUTION.md** Article VI, **AGENTS.md** §8–9, **BALONEY-SCALE.md**: Usable added. (The decks quote Articles II, VIII, IX, XI, XV, not VI.)
- **BALONEY-CURVE.md:** stop 5 gains Usable; new "Curve vs. Funnel" section; notes the missing return arrow in the curve art.
- **SKILLS.md, INSTRUCTIONS.md, evals/README.md, docs/HANDOFF.md, docs/BUILD-DECISIONS.md:** rewritten or updated for the new layout and method.

### Tooling

- `scripts/check-library.py` now enforces the spec: inventory, tiers, the six-utility ceiling, the utility rule, required sections in order, at least three violation signals, required files, the four questions verbatim in four places, contract freshness, plugin manifests, the stage symlink, case YAML, and local links. Mutation-tested: each of eight deliberate breaks was caught.
- `scripts/build-distribution.py` builds ten self-contained ZIPs and a bundle: portable frontmatter, generated `agents/openai.yaml`, linked teaching cases copied in, and clean-extraction checks. All ten extracted skills pass Codex's `quick_validate.py`.
- `evals/harness/`: `prepare.py` builds isolated test workspaces (skill without its examples, plus an input with expected answers stripped); `run-codex.sh` runs them through Codex in a read-only sandbox; `runs.yaml` is the plan.

---

## 2. Testing

See [VERIFICATION.md](../evals/VERIFICATION.md) for every run, its grade, and its limits. In short: 21 runs on a different model family (OpenAI `gpt-5.5` via Codex) in isolated read-only workspaces: 17 pass, 4 partial, 0 fail. The four partials exposed one real gap ("Punt the rollout" where the bet should Pivot, plus an unnamed hand-off), which was fixed in the contract and skills; all four re-runs pass. Grade sheets: [first run](../evals/runs/funnel-2026-10-11/GRADES.md), [re-run](../evals/runs/funnel-2026-10-11-rerun/GRADES.md).

The model-graded verdicts were assigned by the authoring assistant (Claude), so they are not blind or human.

---

## 3. Decisions made on Dean's behalf

Each was an open decision in UPDATE-PLAN §12. Reverse any of them by telling the next session.

| # | Decision | What was done | Why | To reverse |
|---|---|---|---|---|
| D1 | Sell-By's tier | **Chaos** (with Receipts) | A date check is cheap; cheapest sifts run first | Move `bdk-sell-by` to `tier: 3-crapola`; update the contract table, catalog, README; cases 01, 05, 06, 09 change |
| D2 | Stage commands | Kept every skill name; `.claude/skills` symlink; plugin also shipped | The keynote quotes `/bdk-skill-sorter` and `/bdk-value-or-theater` 80+ times | n/a. **Test on the stage laptop** that the symlink resolves |
| D3 | Curve vs. Funnel | Kept both: the Curve is one claim's journey, the Funnel sorts many | The curve art and decks already exist | Retire BALONEY-CURVE.md if the talk drops it |
| D4 | PASS-OFF for claims | **No.** Claims get Pursue/Pivot/Punt; work gets all four | "Hand it to the robot" isn't a verdict on a vendor's claim | Edit the contract's "Two families" paragraph and `expected-behaviors.yaml` |
| D5 | Sorter in the talk | **Updated now** to deck 9 vocabulary (Truth, moves, Monday grid) | If it's on stage, it had a rehearsal deadline; if not, the kit should still match deck 9 | Restore from `dist/` of an earlier build, or rename Truth back to Leverage |
| D6 | Decks 1–8 say "leverage" | Added "(formerly Leverage)" to the sorter | Keeps old decks intelligible without keeping the old word. **Risk:** all eight `slides/arc/showrun/` scripts say Leverage, and the live sorter now prints 🎯 Truth. If Dean presents one of decks 1–8, either say "Truth, formerly Leverage" on stage or rename the square back in `skills/bdk-skill-sorter/SKILL.md` | Delete the note when decks 1–8 retire |
| D7 | Considered skill's name | `bdk-four-risks` | Reads on a projector; names what it does | Rename the folder and `name:`, then update the catalog, CLAUDE.md, README, SKILLS.md, and the check script |
| D8 | "PM Code" vs "Constitution" | **Not changed.** Still CONSTITUTION.md | It's a stage name decision; renaming breaks deck quotes | Add "the PM Code" as an alias line in CONSTITUTION.md |
| D9 | Chaos/Confusion/Crapola definitions | README keeps the damage definitions and adds the funnel reading | Waiting on Dean's three definition panels | Paste the panel wording into README lines 9–13 |
| D10 | Utilities | Built only `bdk-util-slice-the-pitch` | The funnel needs claims, not documents; others wait for a failing case | Candidates are listed in the catalog |

Other calls:
- **Plugin name `bdk`**, version **0.2.0**, homepage `github.com/deanpeters/ai-baloney-detection-kit`. ASSUMPTION: that's where the repo will live; it isn't published.
- **Brand color `#00E874`** (Productside green), matching the keynote's style guide and the Productside repos.
- **Funnel skills keep their check names** rather than `bdk-stepN-…` (a deliberate departure from Precedents, recorded in SKILL-SPEC).
- **`expected_path` keys in the cases** were renamed to tier names; file names keep `loop-` because the return chute still makes it a loop.
- **Case 05's expected exit** was widened to "Confusion or Crapola" after the first run showed the context-pantry arithmetic correctly catches it a tier early.

---

## 4. Still open for Dean

1. **Stage laptop:** confirm `/bdk-skill-sorter` and `/bdk-value-or-theater` resolve through the `.claude/skills` symlink, on venue Wi-Fi and a hotspot.
2. **Keynote repo** (not edited here): `slides/HANDOFF.md` line 71 still says "another agent builds these"; `notes/bdk-update-plan.md` should point to this repo's `docs/UPDATE-PLAN.md`; the curve art needs the return arrow.
3. **D8 and D9** above: the PM Code name and the definition panels.
4. **Human review** of the test runs. No human has graded any output.
5. **Plugin install** in Claude Code and Codex has not been tried.

---

## 5. Addendum: deck 9 check (later, 2026-10-11)

- Copied `launch-week.md` from the keynote's `demos/fixtures/` into `examples/` (the documented mirror direction); the deck 9 demo runs `/bdk-detector @examples/launch-week.md`.
- Ran that demo twice on Codex with the fixture's answer key removed: [evals/runs/stage-demo-2026-10-11/](../evals/runs/stage-demo-2026-10-11/D1.md). Both runs agree with each other (10 → 5 → 2 → 1 → Truth 1) but not with the slides (10 → 6 → 3 → 1), and each output is 1,600–2,100 words, far too long for a one-minute projector read. Findings and options were reported to Dean; nothing else was changed.

## 6. Deck 9 fixes 1–7 (2026-10-11, evening)

Dean asked for all seven recommended fixes, unattended, including the keynote repo.

| # | Fix | Where | Done |
|---|---|---|---|
| 1 | Detector prints a **stage card** (≤ 200 words) by default; full report on request; explicit counting rule | `skills/bdk-detector/SKILL.md`, catalog; harness prompts now ask for the full report | ✓ |
| 2 | Slide counts aligned to the kit (**10 → 6 → 2 → 1**; ROI exits at Confusion as "a guess in a nice suit"); fixture claims 2, 5, 7, 9 made unambiguous | keynote `demos/fixtures/launch-week.md` → mirrored to `examples/`; `build-9-the-funnel.js` funnel slides | ✓ |
| 3 | Answer key moved out of the fixture | keynote `notes/launch-week-expected.md`; BDK case `evals/loop-cases/loop-10-launch-week.yaml` | ✓ |
| 4 | Four-risk paraphrases replaced with a faithful **stage shorthand**: "Would they buy it? Would they trust it? Would it pay, both sides? Can we do it with what we've got?" | contract (re-synced), CLAUDE.md; deck kit slide, Considered slide, survey Q4 options and gag | ✓ |
| 5 | PM Code slides now show their real 1722 lines (Roberts' articles: game for money · equal vote · defraud → marooned) with "vs. Chaos/Confusion/Crapola" on the label; CONSTITUTION.md gains a "PM Code (stage edition)" mapping to Articles VII/VIII, IX, II | `build-9-the-funnel.js`; `CONSTITUTION.md`; CLAUDE.md | ✓ |
| 6 | `bdk-value-or-theater` accepts any voice, incl. CFO mode, haiku verdict, rate my LinkedIn; grades and verdict never change | skill + VOICES.md | ✓ |
| 7 | README carries the three definition panels verbatim (resolves D9) | README | ✓ |

Deck 9 was rebuilt with `SHOWRUN=1 node build-9-the-funnel.js` (55 slides, ~41.7 min; .pptx and showrun regenerated). Backups of the pre-edit build script, .pptx, and showrun were kept in the session scratchpad. The deck plan `outline/deck-9-the-funnel.md` is now v0.4. Test evidence: [stage-demo grades](../evals/runs/stage-demo-2026-10-11/GRADES.md): stage card every run; exact slide counts in 2 of 3 final runs, the scripted ending in 3 of 3; a recovery line for an off-by-one count is in the deck notes.

Not changed: the keynote's `slides/HANDOFF.md` line 71 (still says another agent builds the main skills); decks 1–8 still say "Leverage."

## 7. Keynote sync to deck 11 (2026-10-15)

Docs only. No skill behavior changed.

- **CONSTITUTION.md:** "juice" → **"Is the ORANGE worth the squeeze?"** (Dean's standing correction). Added the deck 11 "7 Arrrguments" mapping under the PM Code.
- **CLAUDE.md:**
  - The missing-question framing of the three C's and the "better questions, better decisions" throughline.
  - What deck 11 runs from this repo (`/bdk-receipts` live; value-or-theater optional and hidden).
  - The Leverage/Truth drift and the ORANGE fix.
- **docs/HANDOFF.md:** a new "Keynote sync" section with the slide-by-slide map and the open items.

**Open for Dean:**
1. Leverage or Truth on the Sort 2x2. Deck 11 says Leverage; `bdk-skill-sorter` says Truth.
2. Write `deck-fatigue-index.md` and test `/bdk-receipts` on it for the stage. It needs a one-minute projector read, the same constraint as the deck 9 stage card.

## 8. `bdk-receipts` stage card (2026-10-15)

Dean asked for it, for deck 11's live demo.
- **`skills/bdk-receipts/SKILL.md`:** Outputs now come in two sizes.
  - A default **stage card**: ≤ 200 words, one line per claim, the Receipts rating, then **Claim / Challenge / Evidence / Better decision**. That ending mirrors deck 11's slide 53.
  - The full Receipts Ledger, on request.
  - Method step 9 and the decision gate are updated to match (Better decision is a recommendation; the human decides). The frontmatter `produces` lists the card.
  - The template is unchanged; it's the full report.
- **`examples/deck-fatigue-index.md`:** new, mirrored from the keynote's `demos/fixtures/`. The answer key is in the keynote's `notes/deck-fatigue-index-expected.md`.
- **Evidence:** [runs and grades](../evals/runs/stage-demo-2026-10-15/GRADES.md), and [VERIFICATION.md](../evals/VERIFICATION.md) has the summary.
- **Checks:** `check-library.py` PASS; `build-distribution.py` regenerated `dist/`.
- **Open for Dean:** Leverage or Truth on the Sort 2x2 (unchanged from section 7).

## 9. The seven-step loop (2026-10-18)

Dean redesigned the funnel: **outcome first**, then evidence for that outcome. His words: "MAKE IT WORK FIRST, then we can rename the tier labels," and "DO NOT LET THE SLIDE DECKS determine the efficacy of the library." He updates the decks.

| Step | Skill | Tier | Change |
|---|---|---|---|
| 1 | `bdk-outcomes` | Chaos | **New.** Shapes a pitch into [direction] [metric] [by how much] [by when] for [beneficiary] in [context], or sifts out outputs ("an AI interface") and vanity metrics ("feel 50% more confident") |
| 2 | `bdk-receipts` | Chaos | Now looks for evidence about the outcome's metric and direction. Stage card unchanged (keynote live demo) |
| 3 | `bdk-labels` | Confusion | Moved up; labels the receipts and reports the label mix |
| 4 | `bdk-sell-by` | Confusion | Moved from Chaos; also checks evidence against the outcome's by-when |
| 5 | `bdk-relevance` | Confusion | **New.** Direct, adjacent, or analog relevance to our pantry of product, user, business, and market data (precedent thinking for analogs) |
| 6 | `bdk-taste-test` | Crapola | The tiniest test that returns the most brutal truth; thresholds from the outcome's target |
| 7 | `bdk-pivot-punt-pursue` | Considered | **New.** The recommendation and its why |

- **Kept as deep dives:** `bdk-context-pantry` (beside step 5) and `bdk-four-risks` (beside step 7). Nothing was deleted.
- **Dean's definitions, in the contract:** the four risks keep their verbatim questions and gain his meanings (Valuable: money out of their wallets into ours; Usable: expands adoption, removes obstacles, makes advocates; Viable: a good business model for us, where AI usage cost can make each added user lose money; Feasible: people, process, culture, capital). **Pursue** = so much proof we go forward as planned; **Pivot** = adjust based on the data and discoveries; **Punt** = the orange is not worth the squeeze.
- **One rule changed meaning:** "Pursue the cheapest test" (missing squares) is now **Pivot to the tiny test first**, because Pursue now means going forward as planned.
- **Tier labels:** Dean liked Chaos (1–2) · Confusion (3–5) · Crapola (6) · Considered (7) and may rename them later.
- **Plugin version:** 0.2.0 → 0.3.0.
- **Evals:** new cases 12 (vanity outcome) and 13 (output to outcome); case 09's expected exits revised for the new order; an `expected_outcome` added to cases 01–08. All written before any run. Results: [first run](../evals/runs/loop7-2026-10-18/GRADES.md), [re-run after the step-1 fix](../evals/runs/loop7-2026-10-18-rerun/GRADES.md).
- **Harness:** Codex rejected every model on the ChatGPT account, so [`run-claude.sh`](../evals/harness/run-claude.sh) runs the same workspaces through headless Claude (Sonnet). The eval prompt now takes each case's own assessment date.
- **Keynote impact (for Dean):** deck 11's funnel slides show the old six commands and the old tier pairs. `/bdk-receipts` (the live demo) still works and prints the same stage card.

## 10. Sourcing, the solution hypothesis, and guardrails (2026-10-18, later)

Dean shared two Productside worksheets (measuring the four risks; the solution hypothesis) and the sourcing rules from his TAM/SAM/SOM prompt, and asked for the whole plan to run unattended. The Productside PDFs are licensed for internal use only, so the kit borrows ideas, not wording, and credits the source in the README.

- **Sourcing (contract, AGENTS.md, Receipts):** research public facts yourself and ask only for private ones (never browse a fictional fixture or stage demo); a ranked list of credible source classes, with analyst reports counted only when their method and sponsor are named; bottom-up beats top-down; ranges with reasons.
- **Outcome statement:** an optional guardrail, "without [a health metric] crossing [a limit]"; targets built bottom-up or labeled ASSUMPTION.
- **Taste Test:** writes a solution hypothesis (If we / for / then we will [the outcome] · at least two tiny acts of discovery tagged by square · valid if within [timeframe] we observe a quantitative measure, a qualitative measure, and a hard stop, written first), with a menu of tiny acts and hard-to-fake measures per square. Hand-offs: `adlc-util-solution-hypothesis`, `dlab-step07-solution-hypothesis`; market sizing goes to `dlab-step02-segment`.
- **Detector:** splits the claim from the need at intake, after case 01's first run let a dead vendor claim hide a live need.
- **Evals:** new case 14 (top-down market claim). 10 runs plus 2 re-runs: **10 pass, 0 fail** (latest per run). [Grade sheet](../evals/runs/sourcing-2026-10-18/GRADES.md).
- **Defaults chosen for Dean:** the guardrail is optional; case 02's open question (stale demo data: Send back at Sell-By or held for the Taste Test) is left for him.

## 11. Spoken order (2026-10-18)

Dean's rule: when these are written or said as a list, it's always **Chaos, Confusion, Crapola** · **Pivot, Punt, Pursue** · **Hired, Fired, Promoted**. They're written to ring for humans. Processing order is free: decision tables and grid-reading rules may still check Pursue first.

- About 50 listed sequences reordered across the skills, contract, templates, frontmatter, plugin manifests, README, catalog, AGENTS, INSTRUCTIONS, SKILLS, the spec, and the Seagull runbook. The step-7 question is now "Pivot, punt, or pursue, and why?"
- Work-family moves read **Pass-off · Pivot · Punt · Pursue**.
- `bdk-value-or-theater`'s output lines now read "Verdict: ⏳ NOT YET / 🎭 THEATER / 🎯 VALUE" and "Move: PIVOT / PUNT / PURSUE", reordered together so each verdict still sits above its move.
- Chaos, Confusion, Crapola and Hired, Fired, Promoted were already in order everywhere.
- Left as is: history (eval runs, earlier log sections), and the HANDOFF quote of deck 11's slide ("Punt / Pivot / Pursue"), now annotated with the spoken order for Dean's slide pass.
