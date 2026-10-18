#!/usr/bin/env python3
"""Prepare isolated behavior-test workspaces: one folder per run with only the skill under test and its input.

Expected answers never enter a workspace. Inputs are built from evals/loop-cases/*.yaml using only the
claim, the supplied evidence, and any referenced input file; the skill's examples/ folder is left out
because its worked examples are derived from the same cases.

Usage: python3 evals/harness/prepare.py <workspace-root> [RUN_ID ...]   (no IDs = every run)
"""
import shutil
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT / 'evals/loop-cases'
PLAN = Path(__file__).with_name('runs.yaml')


def case_input(case_id):
    case = yaml.safe_load((CASES / f'{case_id}.yaml').read_text())
    lines = [f'# {case["title"]}', '',
             'Synthetic teaching fixture. All organizations, people, figures, and dates are fictional.',
             f'Assessment date: {case["assessment_date"]}.', '']
    if case.get('input'):
        lines += [(CASES / case['input']).resolve().read_text().strip(), '']
    if isinstance(case.get('claim'), str) and not case['claim'].startswith('See the input file'):
        lines += ['## The claim', '', case['claim'].strip(), '']
    elif case.get('claim'):
        lines += ['## The ask', '', case['claim'].replace('See the input file. ', '').strip(), '']
    if case.get('supplied_evidence'):
        lines += ['## Supplied evidence', '']
        lines += [f'- **{key}:** {value}' for key, value in case['supplied_evidence'].items()]
    return '\n'.join(lines) + '\n'


def main():
    out = Path(sys.argv[1])
    plan = yaml.safe_load(PLAN.read_text())
    only = set(sys.argv[2:])
    runs = [r for r in plan['runs'] if not only or r['id'] in only]
    for run in runs:
        workspace = out / run['id']
        if workspace.exists():
            shutil.rmtree(workspace)
        skill = ROOT / 'skills' / run['skill']
        shutil.copytree(skill, workspace / 'skill', ignore=shutil.ignore_patterns('examples', '.DS_Store'))
        date = '2026-10-11'
        if run['input'].startswith('loop-'):
            text = case_input(run['input'])
            date = str(yaml.safe_load((CASES / f"{run['input']}.yaml").read_text())['assessment_date'])
        else:
            text = (ROOT / run['input']).read_text()
        (workspace / 'input.md').write_text(text)
        (workspace / 'prompt.txt').write_text(plan['prompts'][run['prompt']].format(date=date, **run))
    print(f'Prepared {len(runs)} workspaces in {out}')


if __name__ == '__main__':
    main()
