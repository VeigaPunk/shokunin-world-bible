# F31 — census-replica-2 (independent second preservation census)

Seat: F31, round-94 FOLLOW-UP leaf. Role: fully independent second preservation census of
`corpus/fixtures` (and, as secondary scope, all of `corpus/`) against a **git archive of
baseline `9c2eea3`** — not against F13's artifacts. Read-only on `corpus/`; the only writes
are this report and `.ufo/waves/round-94/followup/F31-scratch/`.

## Method (fresh and independent)

- Fresh script written for this seat: `.ufo/waves/round-94/followup/F31-scratch/census.py`,
  sha256 `12e9ed87f2a18f9510bd94598d7920aa2be06463d8ffde1ce6c87cc455aa6ad5`.
  Stdlib only; extracts `git archive 9c2eea3b58a090f8820c7a723d2f6a22b46ae52b corpus`
  (2,744,320 tar bytes) into `F31-scratch/baseline/`, sha256-hashes every file
  (symlinks as `link:<target>` markers), and compares against the live working tree.
  It does not read F13's scripts or JSON outputs.
- Live state at census time: HEAD `65a93298cb100fdbf5732ac6de55f01a683c02d8`; the
  working tree is clean for corpus (`git status --porcelain -- corpus/` → empty), so
  live bytes == committed deliverable bytes.
- Command: `python3 .ufo/waves/round-94/followup/F31-scratch/census.py`
  → **exit 0**, `RESULT CLEAN`. Full output persisted at
  `F31-scratch/census.out` (sha256 `6a020da1fe4c9c68a1e30679c2cb716c613847b74eeaa58795a7e98fab1a0670`).
  The script was re-run three times; all preservation numbers below were stable across runs.

## Result 1 — directory census: 168 fixture dirs (expected 168)

Observed output (from `census.out`):

```
fixtures_baseline_topdirs=167
fixtures_live_topdirs=168
fixtures_new_topdirs=['r94-paired-crossing']
fixtures_lost_topdirs=[]
fixtures_live_dirs_recursive=168
fixtures_baseline_dirs_recursive=167
```

- Live top-level fixture dirs: **168** (167 inherited + 1 new `r94-paired-crossing`),
  0 lost. Recursive count equals top-level count (no nested dirs).
- Independent cross-method confirmation, outside my script:
  - `find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l` → `168`
  - `git ls-tree -d 9c2eea3:corpus/fixtures | wc -l` → `167`

## Result 2 — new paths (all enumerated)

Primary scope: exactly **10 new files**, all in the new fixture and all tracked at HEAD:

```
NEW  r94-paired-crossing/README.md [tracked@HEAD]
NEW  r94-paired-crossing/claim-excerpt-map.md [tracked@HEAD]
NEW  r94-paired-crossing/contradictions.json [tracked@HEAD]
NEW  r94-paired-crossing/entities.json [tracked@HEAD]
NEW  r94-paired-crossing/fictional-excerpts.md [tracked@HEAD]
NEW  r94-paired-crossing/inspiration-note.md [tracked@HEAD]
NEW  r94-paired-crossing/relations.json [tracked@HEAD]
NEW  r94-paired-crossing/source-excerpt.md [tracked@HEAD]
NEW  r94-paired-crossing/sources.json [tracked@HEAD]
NEW  r94-paired-crossing/timeline.json [tracked@HEAD]
```

Secondary scope (whole `corpus/`, live vs archive): the same 10 plus
`knowledge/r94-cross-myth-design-comparison.md`, `tools/map-obligations-contract.json`,
`tools/map_obligations.py` (all `[tracked@HEAD]`), plus ignored runtime bytecode
`tools/__pycache__/*.pyc` (`[ignored]`; `git check-ignore -v` →
`.gitignore:2:__pycache__/ corpus/tools/__pycache__/support_check.cpython-314.pyc`,
and `git log --all -- corpus/tools/__pycache__` → 0 commits). The `__pycache__` set
fluctuated between runs (2/2/3 `.pyc` files: `boundary_doc_check`, `map_obligations`,
`support_check`) as concurrent seats ran the corpus checkers — build noise, not
deliverable content.

## Result 3 — inherited bytes: 0 changes, 0 removals

Observed output:

```
fixtures_baseline_files=980   fixtures_live_files=990
fixtures_inherited_modified=0
fixtures_inherited_missing=0
corpus_inherited_modified=0
corpus_inherited_missing=0
baseline_files_total=1767 live_files_total=1782
```

- All 980 inherited fixture files are byte-identical (sha256) to the `9c2eea3` archive;
  all 1767 inherited `corpus/` files likewise; nothing missing anywhere in `corpus/`.
- Corroboration by git-native methods (not my script):
  `git diff --numstat 9c2eea3 HEAD -- corpus/fixtures` → 10 rows, every one `N 0`
  (additions only, no modified/deleted rows); `git ls-tree -r` file counts 980 → 990
  (baseline → HEAD).

## Cross-check against F13 (preservation census replica)

- During my census runs, F13's report file was not yet present in
  `.ufo/waves/round-94/followup/` (`ls .ufo/waves/round-94/followup/ | grep -i F13`
  → only `F13-scratch`), so I first cross-checked against its scratch artifacts
  (read-only). F13's report `F13-preservation-census.md` landed afterwards; I read it
  and compared it in full.
- F13 scratch (`F13-scratch/census-bytes.json`, `census-tuples.json`):
  `top_level_dirs_baseline_count` 167 / `top_level_dirs_head_count` 168,
  `tracked_files_baseline` 980 / `tracked_files_head` 990, `dirs_added`
  `['r94-paired-crossing']`, `dirs_removed` `[]`, `paths_added` = the same 10 fixture
  files, `paths_deleted` `[]`, `paths_modified` `[]`, `disk_dirty_vs_head` `[]`,
  `disk_missing_vs_head` `[]`, `disk_untracked_under_fixtures` `[]`; tuples census:
  `baseline_dirs` 167, `delivered_dirs` 168, `inherited` 167,
  `changed_tuple_count` 0, `added_dirs ['r94-paired-crossing']`, `removed_dirs []`.
- F13 report (`.ufo/waves/round-94/followup/F13-preservation-census.md`) states the
  same: 980→990 tracked files, 167→168 dirs, the same 10 added paths, 0 modified/0
  deleted (blob-level and worktree-level), 0 changed behavioral tuples, fixture-scope
  line delta 10 files / 247 added / 0 deleted. I re-observed two of its numbers directly:
  `git ls-tree -r HEAD -- corpus/fixtures/r94-paired-crossing/` returns exactly the 10
  blob hashes F13 lists (all ten match), and
  `git diff --numstat 9c2eea3 HEAD -- corpus/fixtures | awk '{a+=$1;d+=$2;n++} END{...}'`
  → `rows=10 added=247 deleted=0`.
- **No disagreement on any comparable number.** Methods differ (F13: git blob hashes
  baseline-vs-HEAD plus worktree check plus behavioral per-dir checker tuples with a
  path-normalization control; mine: sha256 of the extracted `9c2eea3` archive vs the live
  tree plus whole-`corpus/` scope), so the agreement is independent convergence, not
  shared tooling. Scoped differences: (a) F13's `paths_added` covers `corpus/fixtures`
  (10 files); my secondary whole-`corpus/` scope additionally enumerates
  `knowledge/r94-cross-myth-design-comparison.md` and the two `tools/` files (also
  additions). (b) Both seats observed transient runtime artifacts in the live tree —
  F13 a `map-obligations-self-test-*` directory at repo root (auto-removed), me
  fluctuating `corpus/tools/__pycache__/*.pyc` (gitignored); neither is a committed
  deliverable change and neither affects the census numbers.

## Auxiliary observation (outside the core census mandate)

Parse-level counts of the new fixture, for the parent's convenience (lexical, not the
C1 verdict): `entities.json` 5 items, `relations.json` 1, `timeline.json` 3,
`sources.json` 3, `contradictions.json` 0; `claim-excerpt-map.md` contains 14 lines with
canonical `*.json#/` pointers. This is consistent with the declared 5/1/3 and 14
obligations, but source support and semantics are other seats' claims, not mine.

## Bottom line

**PASS** — fixture dirs 167→168 (+`r94-paired-crossing`, 0 lost), 10 new fixture files all
tracked at HEAD, 0 inherited byte changes or removals across all 980 inherited fixture
files and all 1767 inherited `corpus/` files vs the `9c2eea3` archive; full agreement with
F13's preservation census (scratch artifacts and the report that landed after my runs; no
disagreement).
