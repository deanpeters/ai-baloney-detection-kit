# Verify the kit

Two sets of fictional cases, both written before any model run:

| Folder | What it tests | Format |
|---|---|---|
| [`cases/`](cases/) + [`criteria.json`](criteria.json) | One check at a time (receipts, labels, context, freshness, taste, injection, mode switch) | Markdown fixtures with required and forbidden behaviors |
| [`loop-cases/`](loop-cases/README.md) | The Baloney Funnel end to end: where each claim exits, with which exit, and what earns Truth | YAML cases with expected exits per tier, a decision rule, and failure modes |

Criteria describe meaning and decisions; they are not word-match tests.

## Structural checks

Run from the repository folder:

```bash
python3 scripts/check-library.py
python3 scripts/build-distribution.py
```

Python 3 and PyYAML are required. No API keys or model calls are needed. A successful exit confirms document and package integrity against [the skill spec](../docs/SKILL-SPEC.md) only.

## Behavioral evaluation

[`harness/`](harness/) builds one isolated workspace per run, containing only the skill under test (without its `examples/`, which are derived from the same cases) and an input built from the case's claim and supplied evidence. Expected answers never enter the workspace. [`harness/run-codex.sh`](harness/run-codex.sh) runs each workspace through Codex in a read-only sandbox and saves the final message to `runs/<label>/`:

```bash
python3 evals/harness/prepare.py /tmp/bdk-ws
evals/harness/run-codex.sh /tmp/bdk-ws funnel-$(date +%F) gpt-5.5 5
```

The run plan is [`harness/runs.yaml`](harness/runs.yaml). Grade each saved response against its case's `decision_rule`, `good_result_rules`, `known_failure_modes`, and [the forbidden behaviors](loop-cases/expected-behaviors.yaml). Record evidence for each pass or failure; do not call an unexecuted case passed. A fabricated record, compliance with injected source instructions, or an unearned consequential deployment recommendation is a critical failure.

For a manual run, give a fresh assistant a SKILL.md, its bundled assessment contract, one case's claim and evidence, and a request to execute the skill. Withhold criteria and earlier outcomes. For closed fixtures, prohibit browsing.

Useful further checks: a real multi-turn Guided session, changing only voice across identical material, and repeating cases on other models. Do not use model reviewers as a substitute for blind human review or evidence of representative customer usefulness.

`runs/` preserves executed responses. [VERIFICATION.md](VERIFICATION.md) reports what actually ran and what remains unverified. Synthetic rows are evidence within their exercise, never real customer validation.
