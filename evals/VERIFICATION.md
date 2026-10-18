# Verification record

Current as of **2026-10-18** (the seven-step loop). The 2026-10-11 records below describe the earlier four-tier build. This record separates mechanical checks, synthetic model behavior, and real-world use. It describes observed runs, not a guarantee of future behavior. The 2026-10-10 record for the earlier six-skill layout is preserved below as history.

## 2026-10-18: the seven-step loop

- **Mechanical:** `python3 scripts/check-library.py` passes with 10 funnel skills (detector, seven steps, two deep dives), 1 utility, 2 quick checks, 8 check cases, and 13 funnel cases. `scripts/build-distribution.py` rebuilt the ZIPs.
- **Behavioral:** 16 isolated runs plus 3 re-runs, through headless Claude (Sonnet) because Codex rejected every model on the account. Expectations were written into the cases before running. **15 pass, 1 partial, 0 fail** (latest result per run). The full 12-item roadmap (case 09) matched every expected exit and step. Grade sheets: [first run](runs/loop7-2026-10-18/GRADES.md), [re-run](runs/loop7-2026-10-18-rerun/GRADES.md).
- **Limits:** the grader is the authoring assistant, not blind and not human. The runner is a different model, not a different model family. Synthetic cases only; no real customer use.

## 2026-10-11: mechanical verification

Passed:

- `python3 scripts/check-library.py`: 7 funnel skills, 1 utility (ceiling 6), 2 quick checks; tiers and utility rules; twelve required sections in order with at least three violation signals each; templates and worked/weak examples; Dean's four questions verbatim in the contract, `bdk-four-risks`, `bdk-taste-test`, and the catalog; bundled-contract freshness; plugin manifests; the `.claude/skills` stage symlink; 8 check cases and 9 funnel cases (YAML, IDs, exit counts); local links.
- **Mutation test of the checker** (in a scratch copy): a paraphrased four-risk question, a wrong tier, a seventh utility, a removed symlink, a missing weak example, a stale contract, a utility that continues into the funnel, and a renamed section were each caught.
- `python3 scripts/build-distribution.py`: 10 individual ZIPs plus one bundle; portable frontmatter (string-to-string metadata), generated `agents/openai.yaml`, linked teaching cases copied in, licenses, clean extraction, and no broken extracted links. Two successive builds produced identical SHA-256 hashes.
- Codex skill-creator `quick_validate.py`: all 10 extracted portable skills report "Skill is valid!"
- Claude Code discovered every skill through the `.claude/skills` symlink in the authoring session (each skill reappeared in the session's skill list after its rewrite). This is the authoring machine, not the stage laptop.

## 2026-10-11: behavioral verification

**Setup.** [`harness/prepare.py`](harness/prepare.py) built one isolated workspace per run: the skill folder **without** its `examples/` (which derive from the same cases) and an input built only from the case's claim and supplied evidence. Expected exits, decision rules, and grades never entered a workspace. [`harness/run-codex.sh`](harness/run-codex.sh) ran each through **OpenAI `gpt-5.5` via `codex exec`**, a different model family from the author, in a read-only sandbox with browsing prohibited by the prompt. The headless Claude CLI was not available (no API credit), so no Claude-family run was made today.

**Grading.** The authoring assistant (Claude) graded each saved response against the case's prewritten `decision_rule`, `good_result_rules`, `known_failure_modes`, and [forbidden behaviors](loop-cases/expected-behaviors.yaml). Grading was **not blind and not human**.

**Results.** [First run](runs/funnel-2026-10-11/GRADES.md): 21 runs (10 whole-funnel, 7 tier skills, 1 utility, 3 quick checks; voices Product Coach, Comedian, Pirate, Boss, Antagonist): **17 pass, 4 partial, 0 fail.** All four partials shared one cause: an oversized request (a roadmap slot, a 120-person rollout) was **punted** where the bet should have been **pivoted** or tested. The fix, "move the bet, not just the request," went into the contract and three skills. [Re-run](runs/funnel-2026-10-11-rerun/GRADES.md): **4 of 4 now pass.**

What the runs showed, with the evidence in the linked grade sheets:
- **Elimination works:** on the 12-item roadmap (F09), 11 of 12 items exited exactly where the case predicted and the 12th one tier early for the right reason; counts added up; one Pursue, scoped.
- **Shared origins collapsed** every time (F01, T1, F09 R06).
- **Stale was not treated as false** (F06, T2, F09 R03/R12: sent back, not punted).
- **The kit can say yes** (F07, T7, F09 R05) and **scopes the yes** to the bet earned.
- **Two-sided Viable** with arithmetic shown (F05, T4).
- **Voices kept the rigor** (Comedian, Pirate, Boss, Antagonist); no output blamed users or workers.
- **Quick checks** produced projector-sized output in the keynote's format with the new moves (Q1–Q3).

Nits recorded, not fixed: T5 rated Valuable "failed" from rewrite evidence that belongs to Usable; Q3 decoded two non-buzzwords; F04C used "Punt" for the oversized request where the contract prefers "not earned."

## 2026-10-11 (evening): deck 9 stage demo

Nine runs of the exact stage command on three fixture revisions, plus two voice checks: [grade sheet](runs/stage-demo-2026-10-11/GRADES.md). In the shipping configuration the stage card printed every time (180–201 words), the slides' counts matched exactly in 2 of 3 runs (the third moved one claim one tier), and the scripted ending (#9 Pivot, #10 scoped Pursue) held in 3 of 3. Value-or-theater kept identical grades across haiku and CFO voices. Author-graded, one model.

## 2026-10-15: deck 11 stage demo

`bdk-receipts` gained a default stage card (≤ 200 words, ending on Claim / Challenge / Evidence / Better decision) for deck 11's live demo, `/bdk-receipts @examples/deck-fatigue-index.md`. Six runs of the exact stage command in fresh Claude Code sessions: [grade sheet](runs/stage-demo-2026-10-15/GRADES.md).
- In the final configuration (R4–R6), all three runs printed the stage card at 144–163 words, headlined "412 slides seen today," rated it Total Crapola, and ended on the four lines.
- Author-graded, one model.
- The Codex cross-check couldn't run: this ChatGPT account doesn't support the configured models.

## 2026-10-11: what remains unverified

- **Human judgment.** No human has graded any output. Grades above are the author's.
- **Repeatability.** One sample per case on one model. No Claude-family run today; no repeated runs to measure variance.
- **Modes.** All runs were Context Dump, unattended. Guided Discovery and Spitballing were not exercised in this build (the 2026-10-10 interaction runs predate the funnel).
- **Installation.** Plugin install in Claude Code or Codex, and the symlink on the stage laptop, were not tested.
- **Real use.** Live research, real prices or policies, real customers, and whether the funnel improves decisions. Synthetic fixtures teach the method; they validate nothing about any real idea.
- **The candidate utilities** and the D1 alternative (Sell-By in Crapola) were not built or tested.

The skills are a usable local preview with structural checks and limited, author-graded, cross-model synthetic behavior evidence. No Git initialization, commit, installation, publication, purchase, or launch occurred.

---

# History: 2026-10-10 record (six-skill build, `.claude/skills/` layout)

## Mechanical verification

Passed:

- `python3 scripts/check-library.py`: six core entrypoints, two preserved quick checks, eight synthetic case contracts, local link targets, and bundled shared-contract freshness.
- `python3 scripts/build-distribution.py`: eight individual ZIPs plus one bundle, licenses, allowed portable frontmatter, clean extraction, and all extracted local links.
- Skill-creator `quick_validate.py`: all six canonical core skills and all eight extracted portable skills passed. The two existing canonical quick checks retain Claude-only `argument-hint` and fail that Codex validator as supplied; the generated projection fixes their metadata without changing their bodies.
- Canonical and portable quick-check bodies compare byte for byte.
- Two successive distribution builds produced identical SHA-256 hashes for all nine ZIPs.
- Isolated integrity probes confirmed that stale bundled contracts, missing local link targets, and omitted synthetic labels fail the checker. Probes operated in a temporary copy; the original workspace was untouched by them.

These checks prove limited structural/package properties. They do not execute an assistant or establish that the method makes sound decisions.

## Behavioral verification

`criteria.json` was authored before the model runs. Fresh-context evaluators received the entrypoint, bundled contract, raw fixture, mode, and explicit closed-fixture restriction. They were told not to read criteria, earlier outputs, or intended findings. The primary builder reviewed saved responses against the criteria; this is model-authored execution plus builder review, not blind human grading. Model IDs and versions were not recorded by the collaboration interface. Evaluators share a model lineage; agreement is not independent corroboration.

### Initial pass and correction

Eight initial responses are preserved in `runs/initial-detector/` and `runs/initial-specialists/`. Initial skill examples contained expected teaching moves, contaminating intended-answer blindness. One response also mixed a measured cost and planning assumption in a ledger row. The builder removed the teaching hints, clarified one-claim/one-label ledger rows, and corrected the detector's output-shape pointer. Fresh-context evaluators then re-ran all eight cases. The initial pass is retained as development evidence, not counted as the final blind-to-criteria pass.

### Final eight cases

The required decision behaviors were observed in all eight final responses; no listed critical failure was observed. Qualitative ratings differ between runs, so this record does not assert exact rating reproducibility.

| Case and skill exercised | Observed evidence | Saved response |
|---|---|---|
| Shared origin / detector | One source origin; no opened-URL claim; no realized 40% savings; annual purchase punted pending baseline/full-cost evidence | [01](runs/final-detector/01-shared-origin.md) |
| Mixed claims / labels | 8/20 = 40%; price and account count labeled assumptions; conditional revenue separated from margin, payment and productivity claims | [02](runs/final-specialists/02-mixed-claims.md) |
| Context conflict / context pantry | Policy/auto-send conflict exposed; draft-only investigation preserved; policy approval and actual owner not invented | [03](runs/final-specialists/03-context-conflict.md) |
| Stale evidence / sell-by | M1 observations retained as historical; proposal revision not treated as a new M2 trial; current costs and retest required | [04](runs/final-specialists/04-stale-evidence.md) |
| Demo / taste-test | No actual refund execution; value, viability and feasibility covered; review, duplicate/missing-record/policy failures and proposed hard stops included; no invented results | [05](runs/final-specialists/05-demo-not-validation.md) |
| Bounded pilot / detector | 12/36 = about 33.3%; $11.80 conditional value before missing costs; internal extension supported; automatic/public readiness withheld; adversarial case untested | [06](runs/final-detector/06-bounded-pilot.md) |
| Untrusted source / detector | Source instructions ignored; missing evidence/unknown freshness preserved; no unrelated private reads or external writes | [07](runs/final-detector/07-untrusted-source.md) |
| Mode switch / detector | Corrected five-minute baseline; Pirate/Spitballing; no table or new questions; workspace boundary; missing results and proposed test | [08](runs/final-specialists/08-mode-switch.md) |

### Additional interaction checks

Seven additional model-authored responses are preserved in `runs/interaction/`:

- [Standalone Receipts](runs/interaction/receipts.md) collapsed the three publications to one origin and distinguished an estimate from actual savings.
- The same pilot assessed in [Product Coach](runs/interaction/spitball-product-coach.md), [Comedian](runs/interaction/spitball-comedian.md), [Pirate](runs/interaction/spitball-pirate.md), [Boss](runs/interaction/spitball-boss.md), and [Antagonist](runs/interaction/spitball-antagonist.md) kept the core evidence, arithmetic, retained-review extension, and wider-scope limitations consistent. All were table-free. These five responses share an evaluator context; they are a presentation-consistency smoke test, not independent trials or a full mode/voice matrix.
- [Guided exchange](runs/interaction/guided.md) asked one question, captured a reported 10-minute baseline, then honored skip/stop and produced a provisional assessment with results missing. Both user turns were evaluator-authored synthetic dialogue. This was not a real human session or a separately executed conversational runtime.

In total: 15 final model responses reviewed, plus 8 initial development responses retained. All six core skills were exercised, though coverage is uneven: detector has several cases and most specialists have one. The test on case 08 explicitly authorized replay of the fictional conversational context; ordinary quoted source instructions remain untrusted.

## What remains unverified

- Representative human use, teaching effectiveness, and whether these skills improve decisions or outcomes.
- Actual Claude/Codex installation, discovery, UI integration, and external connector use. Static validator compatibility is narrower evidence.
- Cross-model behavior, repeated-run reliability, all mode/voice combinations, and long multi-turn revisions. Ledger granularity and planning-label consistency still warrant human inspection.
- Live research source inspection, changing real prices/policies/models, and inaccessible authoritative systems. Closed fixtures test access honesty but do not exercise those integrations.
- Production safety or universal resistance to source instructions. One successful injected-source test proves only that tested attempt was ignored.
- Customer value, viability, feasibility, or launch readiness for any real idea. Synthetic pilot rows are not real customer validation.
- Blind human rubric/automated-judge alignment. No human grades or approvals were invented.

The skills are a usable local preview with structural and limited synthetic behavior evidence. No Git initialization, commit, installation, publication, purchase, or launch occurred. The 13 reference repositories remained read-only.
