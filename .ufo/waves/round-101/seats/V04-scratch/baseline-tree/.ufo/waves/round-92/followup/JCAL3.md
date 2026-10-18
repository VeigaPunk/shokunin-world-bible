# JCAL3 — Census-note judge (r92 follow-up, world-bible lane)

Judgment surface: committed tree at `c4d4823b9a8165a88e8199af136e62d6e961b6b9`
(`git status --short` empty). Checker `corpus/fixtures/check_bible.py` SHA-256
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` (matches the C9 pin).
Both judged notes are tracked and clean vs HEAD.

Judged artifacts and claims:

- `corpus/fixtures/README.md` lines 1046–1062 (`### Repo-relative census invocation`) and
  `corpus/knowledge/r91-c9-watch.md` lines 205–206 (`Census path convention` / `B1 tuple assumption`).
- **Claim A** — the five argv-embedding fixtures are exactly `r5-missing-file`, `r62-missing`,
  `r67-claim-source-unavailable-control`, `r67-claim-source-unavailable-empty`,
  `r67-claim-source-unavailable-whitespace`.
- **Claim B** — the repo-relative invocation guidance is accurate (one absolute-vs-relative
  stdout diff demonstrated), and the notes' operative spelling rule reproduces the captured
  census manifests.

## Work performed

- Read both notes in place at the committed tree; read B1/B2 work-wave census receipts
  (`.ufo/waves/round-92/patches/B1-tuples.json`, `B2-tuples.json`) as the manifests the notes
  tell you to replay.
- Independent exhaustive two-spelling census over all 166 direct fixture directories: ran the
  delivered checker twice per fixture from cwd `lore-shokunin/` — canonical
  `corpus/fixtures/<name>` argv vs absolute argv — comparing stdout bytes, exit code, and
  stderr. No scratch files (inline drivers, `python3 -I`).
- Replay linkage: compared every repo-relative run's stdout SHA-256 against the B1 receipt rows.
- Path-echo scan: every stdout line of every repo-relative run containing a path string.
- Structural scan: for each of the 166 dirs, which of the five section files
  (`sources.json`, `entities.json`, `relations.json`, `timeline.json`, `contradictions.json`)
  are absent; plus a bounded scan of `corpus/live/` (32 dirs) for fixture-like dirs with a
  JSON file and a missing section.
- Spelling matrix for `r5-missing-file`: canonical relative, absolute, `./`-prefixed,
  trailing-slash, and parent-dir-prefixed (cwd = shokunin root).
- Per-fixture receipt table for the five: repo-relative hash vs receipt vs absolute hash.

## Before → after measurements

**1. Exhaustive argv-diff census (Claim A).** Exact driver (run from `lore-shokunin/`; the
`b1` load compares the repo-relative run against the r92 work-wave receipt):

```sh
python3 -I - <<'PY'
import hashlib, json, pathlib, subprocess
root = pathlib.Path.cwd()
fix = root / 'corpus/fixtures'
names = sorted(p.name for p in fix.iterdir() if p.is_dir())
b1 = json.loads((root / '.ufo/waves/round-92/patches/B1-tuples.json').read_text(encoding='utf-8'))
print('dirs=', len(names))
diffs = []
mismatch_b1 = []
for name in names:
    rel = f'corpus/fixtures/{name}'
    ab = str(fix / name)
    a = subprocess.run(['python3','-I','corpus/fixtures/check_bible.py', rel], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    b = subprocess.run(['python3','-I','corpus/fixtures/check_bible.py', ab], cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    sha_a = hashlib.sha256(a.stdout).hexdigest()
    if b1.get(rel, {}).get('stdout_sha256') != sha_a:
        mismatch_b1.append(rel)
    if (a.stdout, a.returncode, a.stderr) != (b.stdout, b.returncode, b.stderr):
        diffs.append(rel)
print('argv_diff_set_count=', len(diffs))
print('argv_diff_set=', diffs)
print('b1_replay_sha_mismatches=', len(mismatch_b1), mismatch_b1[:10])
PY
```

Observed output:

```text
dirs= 166
argv_diff_set_count= 5
argv_diff_set= ['corpus/fixtures/r5-missing-file', 'corpus/fixtures/r62-missing', 'corpus/fixtures/r67-claim-source-unavailable-control', 'corpus/fixtures/r67-claim-source-unavailable-empty', 'corpus/fixtures/r67-claim-source-unavailable-whitespace']
b1_replay_sha_mismatches= 0 []
```

The diff set is exactly the claimed five; no earlier/later facet differs. All five also agree
on exit code (`1` both spellings) and empty stderr — only the echoed path line moves.

**2. Diff content (Claim A detail, Claim B core).** Exact per-fixture compare (driver printed
the differing lines and each fixture's file list). Observed:

```text
=== corpus/fixtures/r5-missing-file exit rel=1 abs=1 stderr rel=0 abs=0
  line0: rel=VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r5-missing-file/contradictions.json'
  line0: abs=VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r5-missing-file/contradictions.json'
  files=['entities.json', 'relations.json', 'sources.json', 'timeline.json']
=== corpus/fixtures/r62-missing exit rel=1 abs=1 stderr rel=0 abs=0
  line0: rel=VIOLATION: timeline.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r62-missing/timeline.json'
  line0: abs=VIOLATION: timeline.json: cannot load JSON: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r62-missing/timeline.json'
  files=['contradictions.json', 'entities.json', 'relations.json', 'sources.json']
=== corpus/fixtures/r67-claim-source-unavailable-control exit rel=1 abs=1 stderr rel=0 abs=0
  line0: rel=VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r67-claim-source-unavailable-control/sources.json'
  line0: abs=VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r67-claim-source-unavailable-control/sources.json'
  files=['contradictions.json', 'entities.json', 'relations.json', 'timeline.json']
=== corpus/fixtures/r67-claim-source-unavailable-empty exit rel=1 abs=1 stderr rel=0 abs=0
  line0: rel=VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r67-claim-source-unavailable-empty/sources.json'
  line0: abs=VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r67-claim-source-unavailable-empty/sources.json'
  files=['contradictions.json', 'entities.json', 'relations.json', 'timeline.json']
=== corpus/fixtures/r67-claim-source-unavailable-whitespace exit rel=1 abs=1 stderr rel=0 abs=0
  line0: rel=VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r67-claim-source-unavailable-whitespace/sources.json'
  line0: abs=VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r67-claim-source-unavailable-whitespace/sources.json'
  files=['contradictions.json', 'entities.json', 'relations.json', 'timeline.json']
```

Each fixture has exactly one differing stdout line, and it is the `OSError` message built from
`directory / '<section>.json'` — i.e. the argv path is echoed inside the message. Findings,
exit code, and stderr bytes are unchanged.

**3. Path-echo scan (explains "exactly").** Exact driver (repo-relative run of every fixture,
printing stdout lines that contain the path string). Observed:

```text
fixtures_with_path_echo_lines= 5
  r5-missing-file: VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r5-missing-file/contradictions.json'
  r62-missing: VIOLATION: timeline.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r62-missing/timeline.json'
  r67-claim-source-unavailable-control: VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r67-claim-source-unavailable-control/sources.json'
  r67-claim-source-unavailable-empty: VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r67-claim-source-unavailable-empty/sources.json'
  r67-claim-source-unavailable-whitespace: VIOLATION: sources.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r67-claim-source-unavailable-whitespace/sources.json'
```

No fixture other than the five prints any path string under the canonical spelling.

**4. Structural cause and scope.** Exact scan (missing section files across the 166 dirs, plus
`corpus/live/`). Observed:

```text
dirs_with_missing_section_files= 5
  r5-missing-file: missing=['contradictions.json']
  r62-missing: missing=['timeline.json']
  r67-claim-source-unavailable-control: missing=['sources.json']
  r67-claim-source-unavailable-empty: missing=['sources.json']
  r67-claim-source-unavailable-whitespace: missing=['sources.json']
```

(`corpus/live/` scan printed nothing: no fixture-like live dir has a JSON file plus a missing
section.) The five argv-embedding fixtures are exactly the five dirs with a missing section
file — consistent with the watch note's phrase "the five missing-file fixtures". Contrast the
content-malformed unavailability fixtures `r60-unavailable` and `r61-direct-unavailable`: both
have all five section files present (invalid-JSON / duplicate-member / non-array cases), and
their diagnostics go through the `path.name` branches (`<file>: cannot load JSON: <exc>` /
`duplicate object member` / `expected array`), which never print the constructed path — hence
they cannot be argv-embedding. This is checker code at `corpus/fixtures/check_bible.py:49–57`
(basename branches) vs the `OSError` string that carries the full joined path.

**5. Spelling matrix, one absolute-vs-relative demonstration (Claim B).** Exact driver for
`r5-missing-file` (canonical relative, absolute, `./`-prefixed, trailing slash, parent-dir
prefixed from the shokunin root). Observed:

```text
canonical rel  (cwd=lore-shokunin): exit=1 stdout_sha256=430d8efb9e124261fbfadb4a2b2a7295bcb9385316e994c012c2f03e3dbf8755 matches_canonical=True stderr_bytes=0
   echo: VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r5-missing-file/contradictions.json'
absolute       (cwd=lore-shokunin): exit=1 stdout_sha256=7a81d5020245c2e6c95b53b8ef6a1ed41e96ea9da638cd57d3226c673a18026b matches_canonical=False stderr_bytes=0
   echo: VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/r5-missing-file/contradictions.json'
dot-rel ./     (cwd=lore-shokunin): exit=1 stdout_sha256=430d8efb9e124261fbfadb4a2b2a7295bcb9385316e994c012c2f03e3dbf8755 matches_canonical=True stderr_bytes=0
trailing slash (cwd=lore-shokunin): exit=1 stdout_sha256=430d8efb9e124261fbfadb4a2b2a7295bcb9385316e994c012c2f03e3dbf8755 matches_canonical=True stderr_bytes=0
parent-prefixed(cwd=shokunin): exit=1 stdout_sha256=c3f3dfe5bdfe7254e98f624fccc357ab4f30ca15bcbad16b35692c4173812c12 matches_canonical=False stderr_bytes=0
   echo: VIOLATION: contradictions.json: cannot load JSON: [Errno 2] No such file or directory: 'lore-shokunin/corpus/fixtures/r5-missing-file/contradictions.json'
```

Absolute and ancestor-prefixed spellings alter stdout while exit code (`1`) and the finding
set are unchanged — exactly the README's stated rationale. The checker still resolves the
fixture correctly from a foreign cwd when given the prefixed path (only the echo spelling
moves). The canonical relative spelling is the one that reproduces the captured manifests.

**6. Replay linkage per fixture (Claim B, manifest replay).** Exact driver (repo-relative run
hash vs B1 receipt vs absolute run hash for the five). Observed:

```text
B1==B2 parsed=True
r5-missing-file: receipt=430d8efb9e124261 rel_run=430d8efb9e124261 rel_matches_receipt=True abs_run=7a81d5020245c2e6 abs_matches_receipt=False
r62-missing: receipt=f440ca4a0dab465d rel_run=f440ca4a0dab465d rel_matches_receipt=True abs_run=a96b823cda6825d9 abs_matches_receipt=False
r67-claim-source-unavailable-control: receipt=0bbc1b1cbade5b48 rel_run=0bbc1b1cbade5b48 rel_matches_receipt=True abs_run=b38074b66abe86ed abs_matches_receipt=False
r67-claim-source-unavailable-empty: receipt=983af74ff7867c56 rel_run=983af74ff7867c56 rel_matches_receipt=True abs_run=f6b3f765522ce373 abs_matches_receipt=False
r67-claim-source-unavailable-whitespace: receipt=ffc2b180d2945525 rel_run=ffc2b180d2945525 rel_matches_receipt=True abs_run=b3235e6483055012 abs_matches_receipt=False
```

All 166 repo-relative runs matched their B1 receipt row (measurement 1,
`b1_replay_sha_mismatches= 0`); the five absolute runs do not. This is the concrete
"keep that spelling when replaying the manifests" justification.

**7. Tree identity checks.** Exact command and observed output:

```sh
git status --short && git rev-parse HEAD && \
  git ls-tree -r --name-only HEAD -- corpus/fixtures/README.md corpus/knowledge/r91-c9-watch.md corpus/fixtures/check_bible.py && \
  sha256sum corpus/fixtures/check_bible.py && \
  git diff --quiet HEAD -- corpus/fixtures/README.md corpus/knowledge/r91-c9-watch.md corpus/fixtures/check_bible.py && echo NOTES_AND_CHECKER_CLEAN_VS_HEAD=PASS
```

```text
c4d4823b9a8165a88e8199af136e62d6e961b6b9
corpus/fixtures/README.md
corpus/fixtures/check_bible.py
corpus/knowledge/r91-c9-watch.md
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
NOTES_AND_CHECKER_CLEAN_VS_HEAD=PASS
```

(`git status --short` printed nothing — tree clean before and after all probe runs; no
fixture file is written by the checker or by my runs.)

## Findings & named debt

- **Claim A (exact five): CONFIRMED.** The exhaustive 166-dir two-spelling census yields
  exactly `r5-missing-file`, `r62-missing`, `r67-claim-source-unavailable-control`,
  `r67-claim-source-unavailable-empty`, `r67-claim-source-unavailable-whitespace` and no
  other dir. Independent corroboration: the same five are exactly the dirs with a missing
  section file, and exactly the five whose stdout carries the argv-built `OSError` message.
  Exit codes and stderr are identical across spellings; only the echoed path moves.
- **Claim B (guidance accurate): CONFIRMED.** Running from `lore-shokunin/` with
  `corpus/fixtures/<name>` reproduces the captured B1/B2 stdout hashes on all 166 rows; the
  absolute-vs-relative demo above shows the stdout divergence (and unchanged exits/findings)
  the note describes; the parent-dir-prefixed spelling diverges the same way. The watch's
  "five missing-file fixtures echo that argv path" and "absolute or differently prefixed paths
  alter the five captured stdout hashes" both hold under direct measurement.
- **Precision note (non-blocking):** pathlib normalization is applied before the message, so
  `./corpus/fixtures/<name>` and `corpus/fixtures/<name>/` are byte-equivalent to the canonical
  spelling (hashes `430d8efb…` in all three). The note's "differently prefixed" clause is
  therefore best read as prefixes that survive into the joined path (absolute, ancestor-dir):
  those do alter stdout, as demonstrated. No wording repair is required for the rule to be
  safe — the operative instruction ("keep that spelling when replaying the manifests") is
  exactly right.
- **Sentinel context (not a gap in the judged surface):** `followup/SF1-freeze.json` records
  HEAD `396c568` with `overall=FAIL` — that is SF1's snapshot of the transient uncommitted
  integration the mission description already accounts for. The landings at `c4d4823` make the
  committed tree clean; all measurements above come from that committed tree.
- **Scope statement:** the census scope is the 166 direct `corpus/fixtures/` directories (the
  B1/B2 manifest scope). `corpus/live/` (32 dirs) contains no additional missing-section
  fixture-like directory, so no out-of-scope argv-embedding fixture is left unlisted.
- **Debt: none raised by this seat.** No checker change, note repair, or follow-up fixture is
  proposed.

## Handoff

- Report: `.ufo/waves/round-92/followup/JCAL3.md` (this file). Evidence table:
  `.ufo/waves/round-92/followup/JCAL3-evidence.json`.
- Verdicts for the parent: Claim A **confirmed exactly**; Claim B **confirmed** (with one
  non-blocking precision note on `./`/trailing-slash normalization). Both path-convention
  notes can stand as written.
- Reproduce the core check: from `lore-shokunin/`, run the driver in measurement 1 (about 8s;
  332 subprocess checker runs, no scratch files). Expected: `argv_diff_set_count= 5`,
  `b1_replay_sha_mismatches= 0 []`.
- No commit, no push, no tracked-file changes. This seat's only repo writes are the two
  follow-up files above; no `/tmp` scratch was created; sibling repos untouched.