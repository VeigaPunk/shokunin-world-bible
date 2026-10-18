#!/usr/bin/env python3
"""Count immutable lore CLI/JSON preservation; a measurement, not a closure gate."""
import argparse
import io
import json
from pathlib import Path
import subprocess
import tarfile
import tempfile

REPO = Path(__file__).resolve().parents[2]


def snapshot(revision, destination):
    commit = subprocess.run(
        ['git', 'rev-parse', '--verify', revision + '^{commit}'],
        cwd=REPO, check=True, capture_output=True, text=True,
    ).stdout.strip()
    content = subprocess.run(
        ['git', 'archive', commit, 'corpus'], cwd=REPO,
        check=True, capture_output=True,
    ).stdout
    destination.mkdir()
    with tarfile.open(fileobj=io.BytesIO(content)) as archive:
        archive.extractall(destination, filter='data')
    return commit


def cli(root, name):
    result = subprocess.run(
        ['python3', 'corpus/fixtures/check_bible.py', 'corpus/fixtures/' + name],
        cwd=root, capture_output=True, text=True,
    )
    return dict(returncode=result.returncode, stdout=result.stdout, stderr=result.stderr)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('before')
    parser.add_argument('after')
    args = parser.parse_args()
    with tempfile.TemporaryDirectory(prefix='lore-preservation-') as temporary:
        before, after = (Path(temporary) / name for name in ('before', 'after'))
        baseline = snapshot(args.before, before)
        measured = snapshot(args.after, after)
        names = sorted(path.name for path in (before / 'corpus/fixtures').iterdir() if path.is_dir())
        runs = []
        for name in names:
            old, new = cli(before, name), cli(after, name)
            runs.append(dict(case=name, same=old == new, before=old, after=new))
        old_json = sorted((before / 'corpus').rglob('*.json'))
        changed = []
        for path in old_json:
            relative = path.relative_to(before)
            target = after / relative
            if not target.is_file() or path.read_bytes() != target.read_bytes():
                changed.append(str(relative))
        print(json.dumps(dict(
            baseline_commit=baseline, measured_after=measured,
            fixture_count=len(runs), same_cli_triples=sum(row['same'] for row in runs),
            baseline_exit_counts={str(code): sum(row['before']['returncode'] == code for row in runs) for code in (0, 1)},
            empty_stderr_both=sum(not row['before']['stderr'] and not row['after']['stderr'] for row in runs),
            inherited_corpus_json_count=len(old_json), changed_inherited_json=changed,
            runs=runs,
        ), indent=2))


if __name__ == '__main__':
    main()
