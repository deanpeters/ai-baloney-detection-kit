# AI-BDK skill handoff

Updated 2026-10-15 (keynote sync below). Ten skills: seven **funnel skills** (the Baloney Funnel's four tiers plus the whole-funnel `bdk-detector`), one **utility**, and the two **keynote quick checks**. Canonical skills are in `skills/` (`.claude/skills` is a symlink to it). Shared behavior is authored in [the assessment contract](../reference/assessment-contract.md). What changed today and why: [UPDATE-LOG.md](UPDATE-LOG.md).

## First use

Open the repository in your assistant. In Claude Code use `/bdk-detector` and attach or paste your input; for one tier use its skill (see [the catalog](../catalog/INDEX.md)). Other capable assistants can read the entrypoint and bundled reference directly. For example:

> Read `skills/bdk-detector/SKILL.md` and its linked assessment contract. DUMP + BOSS: run the claims and supplied evidence in `evals/loop-cases/loop-09-roadmap-funnel.yaml` through the funnel. Use the supplied synthetic evidence only, work unattended, and give me the funnel report.

A tier skill works without a detector run or an upstream artifact. See [the skill catalog](../catalog/INDEX.md) and [usage instructions](../INSTRUCTIONS.md).

## Maintenance

1. Follow [the skill spec](SKILL-SPEC.md). Preserve established terms, Dean's four questions verbatim, and the quick checks' names and stage output.
2. For shared behavior, edit `reference/assessment-contract.md`, then run `python3 scripts/check-library.py --sync`. Bundled copies are generated.
3. Run `python3 scripts/check-library.py` and `python3 scripts/build-distribution.py` (Python 3 + PyYAML).
4. Re-run affected behavioral cases with fresh context (`evals/harness/`), preserve outputs under `evals/runs/`, and update [the verification record](../evals/VERIFICATION.md). A green structural check does not establish good model behavior.

Generated ZIPs in `dist/` are reproducible outputs; do not hand-edit them. Each is self-contained: portable frontmatter, a generated `agents/openai.yaml`, linked teaching cases under `references/linked/`, and the license. Plugin manifests are in `.claude-plugin/` and `.codex-plugin/`; plugin installation has not been verified.

Adding a utility: it must supplement a named tier, keep `depends-on` empty, say it does not continue into the funnel, and stay within the ceiling of six. The check script enforces all four.

[Build decisions](BUILD-DECISIONS.md) explain defaults and workarounds. [Provenance](PROVENANCE.md) maps the local reference set. [Verification](../evals/VERIFICATION.md) gives executed evidence and limitations.

## Keynote sync (deck 11, 2026-10-15)

The keynote's working deck is now **deck 11, The Question Machine** (`~/Code/chaos-confusion-and-crapola/slides/condensed/11-the-question-machine.pptx`; read that repo's `slides/HANDOFF.md`). Deck 9, which this repo's 2026-10-11 work tracked, is superseded. What deck 11 uses from the kit:

| Where in deck 11 | Uses | Status here |
|---|---|---|
| Slide 43 | "The AI Baloney Detection Kit" (metal-detector art) | ✓ |
| Slides 45–49, funnel walk | Each tier's two commands on cards: `/bdk-receipts` "Where'd this come from?" + `/bdk-sell-by` "Is it still true?" (Chaos) · `/bdk-labels` "Fact? Or a guess in a nice suit?" + `/bdk-context-pantry` "Does it apply to us?" (Confusion) · `/bdk-taste-test` "Would reality disagree?" + `/bdk-four-risks` "Pursue, pivot, or punt?" (Crapola) → Punt / Pivot / Pursue + "No evidence yet? Send it back." | Names match. The deck heads each tier with its **missing question** (Chaos: "What are the unknown unknowns?" · Confusion: "What decision is this actually for?" · Crapola: "Yes, we can. But should we?") rather than the kit's sift questions. Both are kept: the kit's questions do the sifting, and the deck's questions say why. |
| Slide 51, live | `/bdk-receipts @examples/deck-fatigue-index.md`: the kit busts Dean's own made-up slide 3 stats | ✓ **Ready (2026-10-15).** The fixture exists (mirrored from the keynote's `demos/fixtures/`), and `bdk-receipts` now prints a default **stage card** ending on Claim / Challenge / Evidence / Better decision. 3 of 3 final runs: 144–163 words, "412 slides seen today," Total Crapola ([grades](../evals/runs/stage-demo-2026-10-15/GRADES.md)). Still to do: record the backup video, in the keynote repo. |
| Slides 55–56, hidden | `/bdk-value-or-theater @examples/pitch-theater.md` | Optional; exists |
| Slide 38, the Sort 2x2 | Busywork · Beige · Theater · **Leverage** | **Drift:** `bdk-skill-sorter` says **Truth** ("formerly Leverage"). Dean to decide; don't change the skill until he does. |
| Slides 63–64 | The 7 Arrrguments, two shown | The mapping to the Constitution is in [CONSTITUTION.md](../CONSTITUTION.md#the-pm-code-the-stage-edition). The full seven are in Dean's Substack article "AI Orchestrator or Pirate Captain?" |
| Hidden | Peak Baloney (the Curve, pins mode) and the cost paradox | The `assets/` exports stay; the slides are only hidden. |

**Vocabulary rules from this round:** always "better questions, better decisions" (never "judgment" as the pitch); "Is the ORANGE worth the squeeze?" (never "juice"; fixed in CONSTITUTION.md and CLAUDE.md on 2026-10-15).

No Git initialization, commits, or publication occurred. The reference repositories and the keynote repository were not edited.
