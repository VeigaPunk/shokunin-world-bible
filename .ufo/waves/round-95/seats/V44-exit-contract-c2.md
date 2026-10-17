# V44 — exit-contract-c2 (round 95)

Seat V44 `exit-contract-c2` (leaf, verifier). Task: after P3 lands, probe
`check_bible` edge classes on scratch copies of the r95 fixture — negative tick,
missing actor, wrong-kind place — and check the prior r16–r20 calibration
semantics reproduce. Baseline: r94 closure `fb118c4`. Declared scratch dir:
`.ufo/waves/round-95/seats/V44-scratch/` (probes, logs, scripts). No corpus
writes, no commits, no network.

## 1. Target artifact and poll record

- At 16:16–16:17 the target `corpus/fixtures/r95-crossing-aftermath/` was
  absent (`ls` empty; no `^P3` seat report). A background poll
  (`V44-scratch/poll-p3.sh`: the 8 P3-owned files present + `timeline.json`
  sha256 stable across two 20 s checks) returned on try 1:
  `READY try=1 p3report_files=0 timeline_sha256=3c0faad6bf32f944f9f2a20f3bd15829044afa04f1a8837601903433b00ea177`
  (the `^P3` counter read 0 at that instant; the P3 seat report
  `P3-fixture-json.md` was present by the time probing started and was read —
  it quotes checker pin `ff9fd2aa…`, matching §2).
- Delivered fixture (mtimes 16:18, 8 P3-owned files): `contradictions.json`,
  `entities.json`, `fictional-excerpts.md`, `inspiration-note.md`,
  `relations.json`, `source-excerpt.md`, `sources.json`, `timeline.json`.
- Counts: entities 5 / relations 1 / sources 4 / timeline 4 / contradictions 0.
- Timeline rows (`id tick entity place depends_on source`):
  `aru-ninth-bell 9 aru quiet-rise [] paired-clock`;
  `evin-ninth-bell 9 evin salt-court [] paired-clock`;
  `paired-crossing-decision 10 aru chalk-stair [aru-ninth-bell, evin-ninth-bell] crossing-minute`;
  `aftermath-missing-evin 11 aru chalk-stair [paired-crossing-decision] aru-aftermath-note`.
- sha256 recorded in `V44-scratch/fixture-hashes.txt`; e.g. `timeline.json`
  `3c0faad6…`, `entities.json` `026af0bc…`.
- Base run — command:
  `python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath`
  → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0.

## 2. Checker under test

- `sha256sum corpus/fixtures/check_bible.py` →
  `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
  (matches the r94 closure pin quoted in LOG.md and in P3's report).
- `git hash-object corpus/fixtures/check_bible.py` →
  `20c56dbb90d9f59ca4fb85971154c0774f5ce0d0`, equal to
  `git show fb118c4:corpus/fixtures/check_bible.py | git hash-object --stdin`;
  `git status --porcelain corpus/fixtures/check_bible.py` empty → unchanged
  since baseline. The probes therefore exercise the delivered revision's checker.

## 3. Method

- Scratch copies only (`copytree` of the delivered fixture) under
  `V44-scratch/probes/<name>/`; mutations append rows to `timeline.json`.
  Per-probe sha256 comparison against the delivered fixture shows **only
  `timeline.json` DIFFERS**; every other file byte-identical. Example appended
  rows (wrong-kind probe): `v44-wrong-a tick 13 aru place_id evin`,
  `v44-wrong-b tick 13 aru quiet-rise`, `v44-wrong-c tick 13 aru salt-court`
  (all `source_id paired-clock`, unique).
- Control: unmutated copy → `CLEAN … 0 violations`, exit 0.
- Raw stdout/stderr/exit per probe saved under `V44-scratch/logs/`
  (`<name>.stdout.txt`, `<name>.stderr.txt`; all stderr empty).
- Builder: `V44-scratch/build_and_probe.py` (expectation checks in code;
  `summary.json` records them).

## 4. Probe results (all on scratch r95 copies)

Command (per probe): `python3 corpus/fixtures/check_bible.py <probe dir>`

| probe | class (canonical round) | raw stdout | exit | verdict |
|---|---|---|---|---|
| control | unmutated | `CLEAN: schema, citations, relations, timeline; 0 violations` | 0 | PASS |
| neg-tick | r19-negative-tick | `VIOLATION: timeline[4].tick: must be nonnegative` / `VIOLATION: timeline[5].tick: must be nonnegative` / `2 violation(s); no canon changed` | 1 | PASS |
| neg-dep | r20-both-negative | same two `must be nonnegative` lines / `2 violation(s)` | 1 | PASS |
| missing-actor | r13-missing-actor | `VIOLATION: timeline[4].entity_id: dangling entity 'unlisted'` / `VIOLATION: timeline[5].entity_id: dangling entity 'unlisted'` / `2 violation(s)` | 1 | PASS |
| missing-place | r16-missing-place | `VIOLATION: timeline[4].place_id: dangling entity 'unlisted-place'` / `1 violation(s)` | 1 | PASS |
| wrong-kind | r17-wrong-first | `VIOLATION: timeline[4].place_id: not a place 'evin'` / `VIOLATION: timeline[6]: double-booked 'aru' at tick 13 in timeline[5] ('quiet-rise') and 'salt-court'` / `2 violation(s)` | 1 | PASS |

Class expectations, all met:

- **negative tick (r19):** same unique actor (`aru`) at two valid places at
  tick −1 → exactly two `must be nonnegative` lines and **no** `double-booked`
  (negative ticks excluded from occupancy, r19 guard).
- **negative dependency (r20):** dependent tick −1 on prereq tick −2 → two
  `must be nonnegative` lines and **no** `timeline inversion` (r20 both-negative
  guard).
- **missing actor (r13):** absent actor at one tick, two valid places → two
  `dangling entity 'unlisted'` lines only, **no** `double-booked` (r13 guard
  `actor_id_count == 1`).
- **missing place (r16):** absent place plus one valid place, same actor/tick →
  one dangling line only, **no** `double-booked` (r16 guard
  `place_id_count != 0`).
- **wrong-kind place (r17):** `place_id` pointing at character `evin` → one
  `not a place 'evin'`; the wrong-kind row is excluded from occupancy and the
  double-booked pair is the two valid places (`quiet-rise`/`salt-court`), exactly
  the r17-wrong-first shape.

## 5. Canonical r13/r16/r17/r19/r20 reference runs (same checker, same session)

From `V44-scratch/references.txt` (checker sha `20c56dbb…` = fb118c4):

- `r13-missing-actor`: two `timeline[i].entity_id: dangling entity 'unlisted'`,
  `2 violation(s)`, exit 1 — probe matches.
- `r16-missing-first`: one `timeline[0].place_id: dangling entity 'unlisted'`,
  `1 violation(s)`, exit 1 — probe matches.
- `r17-wrong-first`: `timeline[0].place_id: not a place 'mira'` +
  `timeline[2]: double-booked 'mira' at tick 7 in timeline[1] ('harbor') and 'tower'`,
  `2 violation(s)`, exit 1 — probe reproduces the shape with `evin`.
- `r19-negative-tick`: two `must be nonnegative`, `2 violation(s)`, exit 1 — probe matches.
- `r20-both-negative`: two `must be nonnegative`, no inversion — probe matches;
  also `r20-negative-dependent` / `r20-negative-prereq` each emit only the
  `must be nonnegative` line (1 violation), and `r20-valid-order` stays CLEAN.

## 6. Rehearsal control

The same probe suite run against a copy of `r94-paired-crossing` (same five
entities/kinds, one fewer event, CLEAN) returned `ALL_OK` — every class
expectation held there too (`V44-scratch/probes-r94/`, `logs-r94/`), so the
reproduction is not an artifact of the r95 addition.

## 7. Limits / non-claims

- Covers only the named edge classes; does not test `map_obligations` (C1/C3),
  `support_check`, or the fixture's claim content.
- "r16–r20 semantics" = behavior of the current delivered checker on the
  canonical r13/r16/r17/r19/r20 fixtures, captured above and reproduced on r95
  scratch copies; no claim about intermediate historical revisions.
- Mutations are input-structural only; no canon, source-text, or
  identity inference. Poll completeness signal is file presence + 20 s hash
  stability, not process inspection.
- `git status --porcelain corpus/` shows only the untracked
  `corpus/fixtures/r95-crossing-aftermath/` (P3's); my only writes are under
  `V44-scratch/`.

## Artifacts

`V44-scratch/{build_and_probe.py, poll-p3.sh, references.txt, fixture-hashes.txt,
probes/, probes-r94/, logs/, logs-r94/}`.

Bottom line: **PASS** — on scratch copies of the delivered r95 fixture (checker sha256 `ff9fd2aa…`, unchanged from `fb118c4`), the negative-tick (r19/r20), missing-actor (r13), missing-place (r16), and wrong-kind-place (r17) calibration classes all reproduce with exact exit codes and violation lines; unmutated base CLEAN exit 0.
