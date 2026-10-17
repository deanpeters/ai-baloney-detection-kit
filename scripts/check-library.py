#!/usr/bin/env python3
"""Check packaging and document integrity against docs/SKILL-SPEC.md; this does not grade model behavior."""
import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:  # pragma: no cover
    sys.exit('FAIL: PyYAML is required (pip install pyyaml)')

ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / 'skills'
FUNNEL = {
    'bdk-detector': 'funnel',
    'bdk-receipts': '1-chaos',
    'bdk-sell-by': '1-chaos',
    'bdk-labels': '2-confusion',
    'bdk-context-pantry': '2-confusion',
    'bdk-taste-test': '3-crapola',
    'bdk-four-risks': '4-considered',
}
TIERS = ('1-chaos', '2-confusion', '3-crapola', '4-considered')
QUICK = ('bdk-value-or-theater', 'bdk-skill-sorter')
MAX_UTILITIES = 6
SECTIONS = ('Purpose', 'When to use it', 'Inputs', 'Key concepts', 'Outputs', 'Method', 'Human decision gate',
            'Evidence expectations', 'Mode behavior', 'Voice behavior', 'Failure modes', 'Assets and examples')
REQUIRED_KEYS = ('name', 'description', 'license', 'argument-hint', 'intent', 'theme', 'status', 'best-for',
                 'scenarios', 'produces', 'depends-on', 'combine-with', 'interface')
FOUR_QUESTIONS = (
    '"Is this something someone would buy?"',
    '"Will users trust and adopt it?"',
    '"Is this good business?"',
    '"Can we even do this with what we know and have?"',
)
LICENSE = 'CC-BY-NC-SA-4.0'
LINK = re.compile(r'!?\[[^\]\n]*\]\(([^)]+)\)')


def utilities():
    return sorted(p.name for p in SKILLS.glob('bdk-util-*') if p.is_dir())


def all_skills():
    return list(FUNNEL) + utilities() + list(QUICK)


def split_skill(path):
    text = path.read_text()
    parts = text.split('---', 2)
    if len(parts) != 3 or parts[0].strip():
        raise ValueError('missing YAML frontmatter')
    return yaml.safe_load(parts[1]) or {}, parts[2]


def local_link_errors(path):
    # Inline links, including image links. Anchors and external links are excluded.
    errors = []
    for raw in LINK.findall(path.read_text()):
        target = raw.strip().split(' "', 1)[0].strip('<>')
        if target.startswith('#') or re.match(r'[a-zA-Z][\w+.-]*:', target):
            continue
        target = target.split('#', 1)[0]
        if target and not (path.parent / target).exists():
            errors.append(f'{path.relative_to(ROOT)}: missing local target {target}')
    return errors


def check_rich_skill(name, data, body, errors):
    folder = SKILLS / name
    for key in REQUIRED_KEYS:
        if key not in data:
            errors.append(f'{name}: frontmatter missing {key}')
    if data.get('theme') != 'baloney-detection':
        errors.append(f'{name}: theme must be baloney-detection')
    for key in ('best-for', 'scenarios', 'produces', 'depends-on', 'combine-with'):
        if key in data and not isinstance(data[key], list):
            errors.append(f'{name}: {key} must be a list')
    interface = data.get('interface') or {}
    short = str(interface.get('short_description', ''))
    if not 25 <= len(short) <= 64:
        errors.append(f'{name}: interface.short_description must be 25-64 characters ({len(short)})')
    if f'${name}' not in str(interface.get('default_prompt', '')):
        errors.append(f'{name}: interface.default_prompt must name ${name}')
    for key in ('display_name', 'brand_color', 'allow_implicit_invocation'):
        if key not in interface:
            errors.append(f'{name}: interface missing {key}')
    headings = re.findall(r'^## (.+)$', body, re.M)
    if [h for h in headings if h in SECTIONS] != list(SECTIONS):
        errors.append(f'{name}: required sections missing or out of order')
    if body.count('*Violation signal:*') < 3:
        errors.append(f'{name}: Key concepts need at least three *Violation signal:* lines')
    if 'references/assessment-contract.md' not in body:
        errors.append(f'{name}: must link the bundled assessment contract')
    for rel in ('template.md', 'examples/worked-example.md', 'examples/weak-example.md'):
        if not (folder / rel).exists():
            errors.append(f'{name}: missing {rel}')
    weak = folder / 'examples/weak-example.md'
    if weak.exists() and 'Anti-pattern' not in weak.read_text():
        errors.append(f'{name}: weak example must be marked Anti-pattern')
    for example in folder.glob('examples/*.md'):
        if 'Synthetic' not in example.read_text():
            errors.append(f'{name}: {example.name} must be marked Synthetic')


def check(sync=False):
    errors = []
    link = ROOT / '.claude/skills'
    if not (link.is_symlink() and link.resolve() == SKILLS.resolve()):
        errors.append('.claude/skills must be a symlink to ../skills (keynote stage commands)')
    contract = (ROOT / 'reference/assessment-contract.md').read_bytes()
    for question in FOUR_QUESTIONS:
        for doc in ('reference/assessment-contract.md', 'skills/bdk-four-risks/SKILL.md',
                    'skills/bdk-taste-test/SKILL.md', 'catalog/INDEX.md'):
            if question not in (ROOT / doc).read_text():
                errors.append(f'{doc}: four-risk question not verbatim: {question}')

    utils = utilities()
    if len(utils) > MAX_UTILITIES:
        errors.append(f'Utility ceiling exceeded: {len(utils)} > {MAX_UTILITIES}')
    actual = {p.parent.name for p in SKILLS.glob('*/SKILL.md')}
    if actual != set(all_skills()):
        errors.append(f'Unexpected skill inventory: {sorted(actual ^ set(all_skills()))}')

    for name in all_skills():
        entry = SKILLS / name / 'SKILL.md'
        if not entry.exists():
            errors.append(f'Missing skill: {name}')
            continue
        try:
            data, body = split_skill(entry)
        except ValueError as exc:
            errors.append(f'{name}: {exc}')
            continue
        if data.get('name') != name or not data.get('description'):
            errors.append(f'{name}: invalid name/description')
        if len(str(data.get('description', ''))) > 1024:
            errors.append(f'{name}: description over 1,024 characters')
        if data.get('license') != LICENSE:
            errors.append(f'{name}: license must be {LICENSE}')
        if '```mermaid' in entry.read_text():
            errors.append(f'{name}: no mermaid diagrams under skills/')
        if name in QUICK:
            if data.get('family') not in ('work', 'claims') or 'argument-hint' not in data:
                errors.append(f'{name}: quick checks need family and argument-hint')
            for rel in ('examples/worked-example.md', 'examples/weak-example.md'):
                if not (entry.parent / rel).exists():
                    errors.append(f'{name}: missing {rel}')
            continue
        check_rich_skill(name, data, body, errors)
        if name in FUNNEL:
            if data.get('tier') != FUNNEL[name]:
                errors.append(f'{name}: tier must be {FUNNEL[name]}')
            if 'supplements' in data or not data.get('sift-question'):
                errors.append(f'{name}: funnel skills declare tier and sift-question, not supplements')
        else:
            if 'tier' in data or data.get('supplements') not in TIERS:
                errors.append(f'{name}: utilities declare supplements (a tier), never tier')
            if data.get('depends-on'):
                errors.append(f'{name}: utility depends-on must be empty')
            if 'not continue into' not in body:
                errors.append(f'{name}: utility must state it does not continue into the funnel')
        copy = entry.parent / 'references/assessment-contract.md'
        if sync:
            copy.parent.mkdir(parents=True, exist_ok=True)
            copy.write_bytes(contract)
        if not copy.exists() or copy.read_bytes() != contract:
            errors.append(f'{name}: shared contract is stale; run --sync')

    manifests = {}
    for rel in ('.claude-plugin/plugin.json', '.claude-plugin/marketplace.json', '.codex-plugin/plugin.json'):
        try:
            manifests[rel] = json.loads((ROOT / rel).read_text())
        except (OSError, ValueError) as exc:
            errors.append(f'{rel}: {exc}')
    if len(manifests) == 3:
        claude, market, codex = manifests.values()
        versions = {claude.get('version'), codex.get('version'), market['metadata'].get('version'),
                    market['plugins'][0].get('version')}
        if len(versions) != 1:
            errors.append(f'Plugin versions disagree: {versions}')
        for label, data in (('claude', claude), ('codex', codex), ('marketplace', market['plugins'][0])):
            if data.get('license') != LICENSE or data.get('name') != 'bdk':
                errors.append(f'{label} manifest: name must be bdk and license {LICENSE}')
        if claude.get('skills') != './skills/' or codex.get('skills') != './skills/':
            errors.append('Plugin manifests must point skills at ./skills/')

    criteria = json.loads((ROOT / 'evals/criteria.json').read_text())
    seen = set()
    for case in criteria['cases']:
        if case['id'] in seen:
            errors.append(f'Duplicate case ID: {case["id"]}')
        seen.add(case['id'])
        fixture = ROOT / 'evals/cases' / (case['id'] + '.md')
        if not fixture.exists() or 'Synthetic teaching fixture.' not in fixture.read_text():
            errors.append(f'{case["id"]}: fixture missing or not marked synthetic')
        if not case['required'] or not case['forbidden'] or not set(case['skills']) <= set(FUNNEL):
            errors.append(f'{case["id"]}: incomplete behavioral criteria')

    loop_cases = sorted((ROOT / 'evals/loop-cases').glob('loop-*.yaml'))
    for path in loop_cases:
        try:
            case = yaml.safe_load(path.read_text())
        except yaml.YAMLError as exc:
            errors.append(f'{path.name}: invalid YAML ({exc})')
            continue
        if case.get('id') != path.stem or case.get('synthetic') is not True:
            errors.append(f'{path.name}: id must match file name and synthetic must be true')
        for key in ('targets', 'exits_at', 'decision_rule', 'good_result_rules', 'known_failure_modes'):
            if not case.get(key):
                errors.append(f'{path.name}: missing {key}')
        if 'expected_exits' in case:
            total = sum(len(v) for v in case['expected_exits'].values())
            if total != case['expected_counts']['entered']:
                errors.append(f'{path.name}: expected exits ({total}) do not add up to entered')
    yaml.safe_load((ROOT / 'evals/loop-cases/expected-behaviors.yaml').read_text())

    for path in ROOT.rglob('*.md'):
        parts = path.relative_to(ROOT).parts
        if 'dist' not in parts and parts[:2] != ('.claude', 'skills'):
            errors.extend(local_link_errors(path))
    return errors, len(loop_cases), len(criteria['cases'])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--sync', action='store_true', help='Refresh only generated bundled assessment contracts')
    args = parser.parse_args()
    errors, loops, cases = check(args.sync)
    for error in errors:
        print('FAIL:', error)
    if errors:
        return 1
    print(f'PASS: {len(FUNNEL)} funnel skills, {len(utilities())} utilit{'y' if len(utilities()) == 1 else 'ies'} (max {MAX_UTILITIES}), '
          f'{len(QUICK)} quick checks, {cases} check cases, {loops} funnel cases, plugin manifests, '
          'stage symlink, local links, bundled contract freshness.')
    print('Mechanical checks only; consult evals/VERIFICATION.md for behavior evidence.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
