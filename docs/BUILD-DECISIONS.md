# Unattended build decisions

Build date: 2026-10-10. Scope authorized by Dean: execute the six-skill plan using the listed local repositories, with best judgment and non-destructive workarounds. No commit or publication was requested.

## Baseline

The workspace had no `.git` repository, no test runner, and two existing skills: `bdk-value-or-theater` and `bdk-skill-sorter`. Those entrypoints and existing fixtures are preserved. The main skills named in SKILLS.md did not exist at inspection. CLAUDE.md's old note about another agent did not identify an active build or candidate files; the user explicitly authorized this build.

## Decisions and assumptions

| Decision | Basis and reversal |
|---|---|
| Six core skills, no new utility skills *(superseded 2026-10-11: seven funnel skills and one utility; see below)* | The five specialist jobs are distinct; a shared contract removes behavioral duplication. Extract a utility only after repeated use establishes its need. |
| Canonical source remains `.claude/skills/` *(superseded 2026-10-11: canonical source is `skills/`, with a `.claude/skills` symlink)* | Existing project convention. Generated ZIPs support portable use without changing canonical locations or installing anything on Dean's behalf. |
| Shared contract bundled into each core folder | Standalone use needs labels, modes, voice, accountability, ratings, and capture rules. Copies are generated and checked for freshness. |
| Three initial Guided questions | ASSUMPTION: a useful default to prevent an endless interview. It is overridable and never an evidence threshold. Unattended instructions bypass waiting. |
| Qualitative per-check ratings | Preserve BALONEY-SCALE.md. No average, fixed source count, or invented numerical confidence formula. |
| Pursue names the investment | A small experiment can be earned while deployment remains unearned. Recommendations are not approvals. |
| No universal expiry or sample-size rule | Freshness and test sufficiency depend on decision, consequence, and change rate. Proposed thresholds are labeled assumptions. |
| Reuse methods selectively | Original AI-BDK prose; no private books, confidential strategy text, assets, or raw research captures copied into distribution. |
| Existing quick checks remain intact *(revised 2026-10-11: updated to deck 9 vocabulary; names and stage output shape kept)* | Their keynote behavior is a separate contract. New skills do not silently rewrite them. |

## Workarounds and boundaries

- No Git baseline: work stayed local; no initialization, commit, or publication. A verification manifest records final file hashes for later comparisons.
- No existing test framework: standard-library scripts check structural and packaging integrity. Authored behavioral criteria are separate from executed model outputs.
- Reference repositories remain read-only. Public GitHub availability is irrelevant to inspecting these authorized local copies.
- Closed synthetic cases use their supplied evidence. No invented external lookup is needed to assess a fictional vendor.
- The existing quick checks have Claude-only `argument-hint` frontmatter. Their canonical demo files remain unchanged; portable ZIP copies move that field under `metadata` and include a license field. Extracted files are checked with the Codex skill validator separately.
- Independent model smoke tests can expose behavior failures, but are correlated model evidence, not blind human grading or representative user research.

## Acceptance criteria

All six skills have actionable instructions, direct-input entry, four evidence labels, three modes, five voices, explicit unattended behavior, and standalone contracts. The detector covers all five checks and all three damage dimensions. Examples include strong as well as weak evidence. Mechanical checks and clean package extraction pass. Behavior runs are preserved and reviewed against the prewritten criteria. Remaining limitations are stated in the handoff.

---

# Revision: 2026-10-11, the Baloney Funnel

Scope authorized by Dean: update the repository without his input, using best judgment, until the skills are written, shaped like his other skill repos (ADLC, Precedents, Market Intelligence, Discovery Lab), and tested. The full change list and every decision made on his behalf are in [UPDATE-LOG.md](UPDATE-LOG.md); the plan is [UPDATE-PLAN.md](UPDATE-PLAN.md).

| Decision | Basis and reversal |
|---|---|
| Canonical skills in `skills/`; `.claude/skills` is a symlink | Matches every sibling repo; the symlink keeps the keynote's `/bdk-…` stage commands working. Reverse by moving the folder back. |
| Funnel of four tiers, not six numbered steps | Dean's presentation outline: a process of elimination, Chaos → Confusion → Crapola → Considered → Truth. |
| Skills keep check names, tier in frontmatter | Projector-readable on stage; a deliberate departure from Precedents' `stepN` naming, recorded in SKILL-SPEC. |
| Sell-By in the Chaos tier | Cheapest sifts first. Alternative (curve order) is recorded as D1 in UPDATE-LOG. |
| Four risks with Dean's questions verbatim, Usable included | Dean, 2026-10-11; the Monday-grid 2×2 from deck 9. The check script enforces verbatim wording. |
| New `bdk-four-risks` (Considered) | The decision deserved its own skill and gate rather than living at the end of the detector. |
| One utility (`bdk-util-slice-the-pitch`), ceiling of six | The funnel needs claims, not documents. Other candidates wait for a case that fails without them. |
| "Move the bet, not just the request" | Added after test runs F02, F04, F04C punted rollouts that should have been Pivots. |
| Behavior tests on a different model family | Codex `gpt-5.5` in isolated read-only workspaces without the skills' examples; reduces, but does not remove, correlated-model bias. The headless Claude CLI was unavailable (no API credit). |
| PyYAML is now required by the scripts | Rich frontmatter and YAML cases need a real parser. |
