#!/usr/bin/env python3
"""Build deterministic, self-contained skill ZIPs from skills/ without changing canonical skills or installing them.

Canonical SKILL.md files keep rich frontmatter (see docs/SKILL-SPEC.md). The portable copy keeps only
name, description, and license at the top level, moves every other key into a string-to-string
metadata map, and generates agents/openai.yaml from the interface block. Local links that leave a
skill folder are copied into references/linked/ and rewritten, so each ZIP extracts cleanly alone.
"""
import importlib.util
import json
import os
import re
import sys
import tempfile
import zipfile
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('bdk_library_checks', Path(__file__).with_name('check-library.py'))
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)
PORTABLE_KEYS = {'name', 'description', 'license', 'allowed-tools', 'metadata'}
FIXED_TIME = (2026, 10, 11, 0, 0, 0)


def flatten(value):
    if isinstance(value, list):
        return ' | '.join(str(v) for v in value)
    if isinstance(value, bool):
        return 'true' if value else 'false'
    return ' '.join(str(value).split())


def portable_entry(text):
    data, body = split(text)
    interface = data.pop('interface', None)
    top = {key: data.pop(key) for key in ('name', 'description', 'license') if key in data}
    lines = ['---']
    for key, value in top.items():
        lines.append(f'{key}: {json.dumps(flatten(value))}')
    if data:
        lines.append('metadata:')
        for key, value in data.items():
            lines.append(f'  {key}: {json.dumps(flatten(value))}')
    lines.append('---')
    return '\n'.join(lines) + body, top['name'], interface


def split(text):
    parts = text.split('---', 2)
    return yaml.safe_load(parts[1]) or {}, parts[2]


def openai_yaml(name, interface):
    return '\n'.join([
        f'# Generated from skills/{name}/SKILL.md by scripts/build-distribution.py. Do not edit by hand.',
        'interface:',
        f'  display_name: {json.dumps(interface["display_name"])}',
        f'  short_description: {json.dumps(interface["short_description"])}',
        f'  brand_color: {json.dumps(interface["brand_color"])}',
        f'  default_prompt: {json.dumps(interface["default_prompt"])}',
        'policy:',
        f'  allow_implicit_invocation: {flatten(interface["allow_implicit_invocation"])}',
        '',
    ])


def localize_links(folder, files):
    """Copy targets of links that leave the skill folder into references/linked/ and rewrite the links.

    Copies go one level deep. Inside a copied file, links are kept when they point at something
    also packaged, and otherwise become plain text naming the repository path.
    """
    origin = {}  # packaged path -> original absolute path

    def packaged_name(absolute):
        return 'references/linked/' + absolute.relative_to(ROOT).as_posix().replace('/', '--')

    for rel in [r for r in files if r.endswith('.md')]:
        source_dir = (folder / rel).parent

        def rewrite(match):
            target, _, anchor = match.group(3).partition('#')
            if not target or re.match(r'[a-zA-Z][\w+.-]*:', target):
                return match.group(0)
            absolute = (source_dir / target).resolve()
            if absolute.is_relative_to(folder.resolve()):
                return match.group(0)
            if not absolute.is_file():
                raise ValueError(f'{folder.name}/{rel}: cannot package link target {target}')
            packaged = packaged_name(absolute)
            files.setdefault(packaged, absolute.read_bytes())
            origin[packaged] = absolute
            new = os.path.relpath(folder / packaged, source_dir) + (('#' + anchor) if anchor else '')
            return f'{match.group(1)}[{match.group(2)}]({new})'

        files[rel] = LINK_PATTERN.sub(rewrite, files[rel].decode()).encode()

    for packaged, absolute in origin.items():
        if not packaged.endswith('.md'):
            continue

        def delink(match):
            target, _, anchor = match.group(3).partition('#')
            if not target or re.match(r'[a-zA-Z][\w+.-]*:', target):
                return match.group(0)
            resolved = (absolute.parent / target).resolve()
            if resolved.is_relative_to(folder.resolve()):
                new = os.path.relpath(resolved, (folder / packaged).parent)
            elif packaged_name(resolved) in files if resolved.is_relative_to(ROOT) else False:
                new = os.path.relpath(folder / packaged_name(resolved), (folder / packaged).parent)
            else:
                where = resolved.relative_to(ROOT).as_posix() if resolved.is_relative_to(ROOT) else target
                return f'{match.group(2)} (`{where}` in the AI-BDK repository)'
            return f'{match.group(1)}[{match.group(2)}]({new}' + (('#' + anchor) if anchor else '') + ')'

        files[packaged] = LINK_PATTERN.sub(delink, files[packaged].decode()).encode()


LINK_PATTERN = re.compile(r'(!?)\[([^\]\n]*)\]\(([^)\s]+)\)')


def package_files(name):
    folder = checker.SKILLS / name
    files = {p.relative_to(folder).as_posix(): p.read_bytes() for p in folder.rglob('*')
             if p.is_file() and p.name != '.DS_Store'}
    entry, _, interface = portable_entry(files['SKILL.md'].decode())
    files['SKILL.md'] = entry.encode()
    if interface:
        files['agents/openai.yaml'] = openai_yaml(name, interface).encode()
    localize_links(folder, files)
    files['LICENSE'] = (ROOT / 'LICENSE').read_bytes()
    return files


def write_zip(path, files):
    # Fail safely if a user placed unrelated content at an output filename.
    if path.exists() and not zipfile.is_zipfile(path):
        raise ValueError(f'Refusing to replace non-ZIP file: {path}')
    with zipfile.ZipFile(path, 'w', compression=zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            info = zipfile.ZipInfo(name, date_time=FIXED_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, data)


def validate_zip(path):
    with tempfile.TemporaryDirectory(prefix='bdk-package-check-') as temp:
        directory = Path(temp)
        with zipfile.ZipFile(path) as archive:
            for entry in archive.namelist():
                if entry.startswith('/') or '..' in Path(entry).parts:
                    raise ValueError(f'Unsafe archive path: {entry}')
            archive.extractall(directory)
        for doc in directory.rglob('SKILL.md'):
            data, _ = split(doc.read_text())
            if not set(data) <= PORTABLE_KEYS:
                raise ValueError(f'{path.name}: unsupported portable frontmatter {set(data) - PORTABLE_KEYS}')
            if not all(isinstance(v, str) for v in (data.get('metadata') or {}).values()):
                raise ValueError(f'{path.name}: metadata must be string-to-string')
        for doc in directory.rglob('*.md'):
            for raw in checker.LINK.findall(doc.read_text()):
                target = raw.split('#', 1)[0]
                if not target or re.match(r'[a-zA-Z][\w+.-]*:', target):
                    continue
                if not (doc.parent / target).exists():
                    raise ValueError(f'{path.name}: broken extracted link {target} in {doc.relative_to(directory)}')


def main():
    errors, _, _ = checker.check()
    if errors:
        print('\n'.join(errors))
        return 1
    output = ROOT / 'dist'
    output.mkdir(exist_ok=True)
    names = checker.all_skills()
    bundle = {}
    for stale in output.glob('*.zip'):
        if stale.stem not in names and stale.stem != 'ai-bdk-skills':
            stale.unlink()
    for name in names:
        files = package_files(name)
        individual = {f'{name}/{key}': value for key, value in files.items()}
        write_zip(output / f'{name}.zip', individual)
        validate_zip(output / f'{name}.zip')
        bundle.update(individual)
    write_zip(output / 'ai-bdk-skills.zip', bundle)
    validate_zip(output / 'ai-bdk-skills.zip')
    print(f'PASS: {len(names)} individual ZIPs and one bundle; portable frontmatter, generated agents/openai.yaml, '
          'clean extraction, licenses, and self-contained links checked.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
