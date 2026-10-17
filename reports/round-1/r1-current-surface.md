# Round 1 — surface scout (R1Surface): affected fixture and documentation surfaces

Scope: map the corpus/ and reports/round-85 surfaces that the holder-disclosure
move can touch, name the smallest immutable replay inventory, and record the
existing standalone-path documentation drift relevant to the new guide.

Evidence status: **read-only static inspection only.** No checker, script, test,
build, linter, or formatter was invoked; no file under `corpus/` was written.
Commands used are `read`/`grep`/`glob`, directory listings, `git ls-tree`,
`git cat-file`/`git show` at `5eb9451baff217c19d5786405f9b2aa500b7c1b7` (== `HEAD`
at scan time, == the declared baseline), `sha256sum`, `sed -n`, `wc`. Line
citations for the checker are pinned to the **committed** blob
`5eb9451:corpus/fixtures/check_bible.py` because the worktree copy changed
during this scan (see §8 observation). All fixture prose and test values are
invented and unverified; nothing below is a canon, truth, rights, promotion, or
external-verifier claim.

## 0. Bounded scan method (reproducible, no runs)

| Question | Command | Result |
|---|---|---|
| Active fixture set at baseline | `git ls-tree -r --name-only 5eb9451:corpus/fixtures \| awk -F/ 'NF==2{print $1}' \| sort -u` | 133 dirs (756 files) |
| Fixtures asserting provenance | `grep -rl '"provenance"' corpus/fixtures --include=entities.json` | 5 dirs |
| Fixtures with repeated entity id | `grep -o '"id": "[^"]*"' corpus/fixtures/*/entities.json \| sort \| uniq -d` | 13 dirs |
| Fixtures with repeated source id | `…*/sources.json` same pipeline | 5 dirs |
| Recorded tuple channel | `sed -n 2p corpus/live/runs/round-85/<fixture>.txt` | 133/133 present, 28 `exit_code=0`, 105 `exit_code=1` |
| Probe input digests | `sha256sum corpus/live/runs/round-85/probe-inputs/*/*.json` | 5 entities digests match `manifest.txt`; 4 non-entity files identical across all 5 probes and identical to `item-chain-valid`'s counterparts |
| Immutable references | `git rev-parse 5eb9451:corpus/fixtures`, `…:corpus/live/runs/round-85`, `git cat-file -p 5eb9451:corpus/fixtures/check_bible.py \| sha256sum` | `07375a56…`, `01c5fc96…`, `88c9b1d0…` |

Bounded: this scan covers `corpus/` (all fixture dirs at path level; the 5
provenance fixtures and 13 duplicate-id fixtures at byte level; the round-85
telemetry dir) and `reports/round-85/` plus the inherited `reports/round-1/`
files. It does **not** claim whole-domain coverage: the ~1,200 non-fixture
corpus files were not read, and the effect of the new diagnostics on inputs that
do not exist in the repository is unassessed by construction.

## 1. `corpus/fixtures` (active bibles) vs `corpus/live` (telemetry)

Observed distinction, already established in-repo and load-bearing for every
count below:

- `corpus/fixtures/` = **active** bibles + the single checker script. Indexed in
  `corpus/README.md:5-9` (itemised list) and documented in
  `corpus/fixtures/README.md` (1002 lines, 47 `## Round …` sections spanning
  Round 3 → Round 83).
  Any addition here changes the 133-dir count that `corpus/README.md`,
  `SCORECARD.md`, and `reports/r84-independent-verifier.md:15` reuse.
- `corpus/live/` = **preserved evidence**: `runs/<timestamp>/` (older rounds),
  `runs/round-85/` (164 files: 133 fixture tuples + 5 probe tuples +
  `manifest.txt` + 25 probe-input files), and `rejected-r4/`, `rejected-r14/`,
  `rejected-r38/` (experiments explicitly *not* active fixtures,
  `corpus/README.md:9`).
- `reports/round-85/r85-author.md` §"Per-axis verdict claim" states the
  round-85 probes are telemetry, not active fixtures, and that fixture/output
  counts are not axis gain. That is the precedent for placing new gate inputs.

Consequence for this move: new gate inputs belong under telemetry (or in the
measurement script's isolated temp trees), **not** under `corpus/fixtures/`,
or the 133-dir inventory and its README/SCORECARD citations silently change.

## 2. Class A — active fixtures asserting `provenance` (5), with recorded tuples

| fixture | provenance location | holders (from→to) | duplicated entity id present? | recorded tuple (`corpus/live/runs/round-85/<f>.txt`) |
|---|---|---|---|---|
| `item-chain-valid` | `entities[3].provenance` (item `seal`) | null→mira, mira→harbor, harbor→tower | no | `exit_code=0`, `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `item-chain-broken` | `entities[3].provenance` | null→mira, mira→harbor, **mira**→tower | no | `exit_code=1`, `entities[3].provenance[2]: provenance chain break; expected from_holder 'harbor', got 'mira'` |
| `r7-item-ambiguous` | `entities[3].provenance` (same 3 records as valid) | null→mira, mira→harbor, harbor→tower | no (`archive-ledger` **source** id repeated instead) | `exit_code=1`, 7 lines: `sources[2].id: duplicate sources id 'archive-ledger'` + 6 `ambiguous in-world source` lines, incl. `entities[3].provenance[1]`/`[2].source_id` |
| `r61-independent-empty` | `entities[0].provenance` on a **non-item** entity | ghost→nobody (both dangling) | no | `exit_code=1`, 17 lines incl. `entities[0].provenance: only valid on item entities`, `…[0].to_holder: dangling entity 'nobody'`, `…[0].from_holder: dangling entity 'ghost'` |
| `r61-independent-unavailable` | `entities[0].provenance` on a non-item entity | ghost→nobody (both dangling) | no | `exit_code=1`, 6 lines incl. same two dangling holder lines; `sources.json` unloadable |

Observed (static): **no active fixture combines `provenance` with a holder that
resolves to a repeated entity id.** Class A ∩ Class B = ∅. Independently stated
as an UNKNOWN by `reports/round-85/r85-author.md` ("expected none today because
no active fixture combines provenance with a duplicated holder") and reserved by
`reports/round-85/r85-axis-adjudicator.md` §"Checker repair and r86" as
requiring mandatory replay of all 133 pinned tuples.

Expected **intended-output delta on these five tuples: zero added lines** — with
two near-collisions that the implementation must not disturb:

1. `r7-item-ambiguous` is the only fixture with provenance **and** an ambiguity,
   but its ambiguity is in `source_id`, i.e. the existing
   `chain_has_ambiguous_source` prefix path
   (`check_bible.py:225-233`, prefix emitted at `:241,243,245`). The new notice
   must not be keyed to `chain_has_ambiguous_source`, and must not add a second
   ambiguity notice for that item.
2. `r61-independent-empty` / `r61-independent-unavailable` are the
   **dangling-holder** substrates: both fields report explicitly today
   (`check_bible.py:213`, `:221`). Gates 3 must keep those messages and
   must not relabel a dangling holder as ambiguous.

## 3. Class B — active fixtures with a repeated entity id, no provenance (13)

New holder diagnostics cannot fire here (no `provenance` object exists in these
files). Recorded first violation line, all `exit_code=1`:

```
r11-character-place         entities[2].id: duplicate entities id 'harbor'
r11-place-character         entities[2].id: duplicate entities id 'harbor'
r12-ambiguous-actor         entities[4].id: duplicate entities id 'mira'
r18-duplicate-first-known   entities[4].id: duplicate entities id 'harbor'
r18-duplicate-pair          entities[4].id: duplicate entities id 'harbor'
r18-duplicate-reverse       entities[4].id: duplicate entities id 'harbor'
r18-known-through-ambiguous entities[4].id: duplicate entities id 'harbor'
r18-mixed-kind              entities[4].id: duplicate entities id 'harbor'
r21-ambiguous-actor         entities[4].id: duplicate entities id 'mira'
r25-to-ambiguous            entities[4].id: duplicate entities id 'seal'
r26-to-malformed            entities[4].name: required nonempty str   (duplicate 'seal' row is malformed)
r27-both-ambiguous          entities[4].id: duplicate entities id 'seal'
r27-target-only             entities[4].id: duplicate entities id 'seal'
```

Related, also unchanged by this move: repeated **source** ids live in
`r7-item-ambiguous`, `r7-ally-reverse-ambiguous`, `r31-source-ambiguous`,
`r32-source-malformed`, `r61-direct-ambiguous`.

Preservation risk from this move on Class B: none statically (no holder path);
identity semantics for relations/timeline ambiguity (`check_bible.py:160-168`,
`:279,281,313`) stay the existing code path and must not be merged with the holder
diagnostics.

## 4. Five-gate substrate map: what the repository already contains and what it does not

| gate | inherited substrate at `5eb9451` | recorded evidence | gap |
|---|---|---|---|
| 1 clean chain | `item-chain-valid` | `exit 0`, CLEAN | none |
| 2 unique-holder real break | `item-chain-broken`; `probe-inputs/r85-unique-break-control` (`vault` unique) | break at `provenance[2]` | none |
| 3 dangling-holder explicitness, both fields | `r61-independent-empty`, `r61-independent-unavailable` | `to_holder: dangling entity 'nobody'` **and** `from_holder: dangling entity 'ghost'` in the same run | none |
| 4 ambiguous-`to` local + downstream scope, no definite comparison | `probe-inputs/r85-masked-ambiguous` (`provenance[1].to_holder = 'vault'` duplicated; later `provenance[2].from_holder = 'harbor'`) | baseline tuple: `entities[5].id: duplicate entities id 'vault'` only | **partial.** No inherited input has a downstream record whose *tick* would be a definite finding if comparisons were resumed: `provenance[2].tick = 4 > 3`, and the last admitted predecessor tick is 0 or 3, so a naive resume yields a continuity line and never a tick line. `probe-inputs/r85-isolated-ambiguous` puts the ambiguity in the **terminal** record (`provenance[2]`), so it cannot evidence downstream suppression at all. |
| 5 ambiguous-`from` symmetric | **none** | — | No inherited input resolves an ambiguous `from_holder`. The branch is symmetric in committed code (`:223-224`) but unexercised; `reports/round-85/r85-axis-adjudicator.md` states this explicitly ("the `from_holder` silent branch … is symmetric in code but unexercised by this pair"). |

Structural consequence (inference, from the contract's "checker AND input data
from requested git revision"): if gate inputs are read *as committed files* from
the requested revision, gates 4 and 5 cannot execute at `5eb9451` — gate 5 has
no input there and gate 4's tick component has no input there either, so the
baseline side of the 5-gate score could not be produced from the same artifact.
Deterministic derivation in isolated temp trees from a base fixture that exists
at both revisions (`item-chain-valid`; probe inputs are byte-identical to it
apart from `entities.json`, verified in §0) is the only shape that makes the
two-revision comparison apples-to-apples. This is a design constraint the new
guide must state; it is not a checker defect.

## 5. Smallest immutable replay inventory

Everything needed to reproduce the preservation claims, and nothing more:

| component | immutable reference | contents |
|---|---|---|
| checker (pre-change) | blob `5eb9451:corpus/fixtures/check_bible.py`, sha256 `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81` | 330 lines |
| active fixture inputs | tree `07375a56d996f574cefc06756bad61a9da1a75f6` (`5eb9451:corpus/fixtures`) | 756 files / **133** dirs |
| active fixture expected tuples | `corpus/live/runs/round-85/<fixture>.txt` | 133 files; 28 × `exit_code=0`, 105 × `exit_code=1`, all `stderr` empty |
| probe inputs | `5eb9451:corpus/live/runs/round-85/probe-inputs/` | 5 dirs / 25 files; `entities.json` digests `fc1d000f…`, `ea80058a…`, `6ccaf656…`, `69dc7fd1…`, `59655ce3…` (match `manifest.txt`); the other 4 files are one identical quadruple across all 5 probes and equal `item-chain-valid`'s four files |
| probe expected tuples | `corpus/live/runs/round-85/probe-r85-*.txt` | 5 files (control `exit 0`; four `exit 1`) |

The remaining corpus files (knowledge docs, `runs/<timestamp>/` history,
`rejected-*` inputs, prose) are **not** required for CLI-tuple preservation.
Two cautions:

- Do not write new probe outputs over `corpus/live/runs/round-85/`: that tree is
  committed evidence at `5eb9451` (tree `01c5fc96…`) and is the pre-change
  baseline of record. New outputs belong in a new round directory.
- Path convention is part of the tuple. All **138** recorded tuple files invoke
  `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/…`
  (parent-mount argv), while the inherited `reports/round-1/current-baseline.json`
  records `python3 corpus/fixtures/check_bible.py corpus/live/runs/round-85/probe-inputs/{case}`
  (lane-root argv). A replay with a different prefix is not byte-comparable with
  the recorded tuples.

## 6. Existing documentation drift relevant to the new guide

1. **Standalone-path convention, header.** `corpus/fixtures/README.md:3-6` says
   "From the repo root, run:" and then uses `.shokunin/lore/corpus/fixtures/…`
   (86 occurrences of `.shokunin/lore/` in that file). Here "repo root" is the
   *parent* mount, not this standalone lane repository's root. `SCORECARD.md:5-8`
   cites counting commands the same way; `corpus/knowledge/2026-10-12-malformed-error-patterns.md:6`
   does too, and additionally pins an older checker commit (`:9`). The new guide
   must state which root its commands assume, because the measurement entry
   point is lane-root relative (`python3 corpus/fixtures/measure_holder_disclosure.py`).
2. **The authoritative provenance prose is the README, and it is now
   incomplete.** `corpus/fixtures/README.md:96-119` ("Round 6") is the only
   round-doc that describes `provenance`, and at `:112-114` it currently says a
   present malformed list, "ambiguous duplicate IDs, or equal/reversed ticks are
   not silently interpreted as a valid chain." That sentence is precisely what
   the move refines: a duplicated *holder* is excluded from chain interpretation
   with no local message. The README has **no** Round 56 section and **no**
   Round 85 section (sections jump 43 → 59), so holder ambiguity, the r56
   rejection, and the r85 masked pair are undocumented there.
3. **Round 7 wording interacts.** `corpus/fixtures/README.md:140-144` states a
   structural holder-chain finding "refers to input fields, not sourced canon
   when citations are ambiguous." The new notice and the two field-local
   messages must be described consistently with that boundary.
4. **Index surfaces.** `corpus/README.md:5-9` lists knowledge docs and fixtures;
   `:10` lists `live/runs/` coverage (currently rounds up to ~22 plus rejected
   round 4 — itself already stale). A new knowledge document
   (`corpus/knowledge/holder-assessment-boundary.md`) and/or new probe dirs
   require index edits; both files are parent-owned per the contract.
5. **Probe inputs are referenced by no corpus document.** `probe-inputs/` and
   the masked/unique matched pair appear only in
   `corpus/live/runs/round-85/manifest.txt` and `reports/round-85/r85-author.md`.
   The new guide should link those rather than restate them (restating risks the
   drift in item 2).
6. **Script-name drift between inherited and current dispatch.**
   `reports/round-1/dispatch.json` names the artifact
   `corpus/fixtures/measure_holder_calibration.py`;
   `reports/round-1/current-dispatch.json` and this session's contract name
   `corpus/fixtures/measure_holder_disclosure.py`. Neither exists in the
   worktree. The inherited file predates this session and must be preserved, not
   corrected; the guide and measurement must use the current name.
7. **No precedent for a revision-parameterised tool.** `check_bible.py` is the
   only script under `corpus/fixtures/`; no corpus document describes a
   `--revision` argv, temp-tree isolation, or where a measurement JSON lands. The
   new guide defines that convention rather than inheriting one.
8. **Adjacent (lane README, bounded observation).** `README.md` lists
   `SKILL.md`, `corpus/lessons/`, and `corpus/QUALITY.md`; none of the three
   exists in this repository (`corpus/` contains only `README.md`, `fixtures/`,
   `knowledge/`, `live/`). Reported as an adjacent drift surface, not as part of
   this move.

## 7. Expected intended-output delta vs preservation risk

| surface | intended delta (static expectation, not a run) | preservation risk to control |
|---|---|---|
| 133 active fixture tuples | none — no active fixture has a duplicated holder (§2, §3) | any new line on any of the 133 invalidates the move; the class-A near-collisions in §2 are where an over-broad condition would show |
| 5 provenance fixtures | none; neither the notice nor the two field-local messages may appear | `r7-item-ambiguous` (source-ambiguity prefix path) and `r61-independent-*` (dangling branch) must keep byte-identical output |
| 13 duplicate-id fixtures | none | do not extend the notice to timeline/relation ambiguity sites |
| 5 round-85 probe tuples | **intentionally changed** for `r85-masked-ambiguous` and `r85-isolated-ambiguous` (new field line(s) + one notice); control/`harbor-repro`/`unique-break-control` unchanged | telemetry, so no index impact; write new outputs under a new round dir, never over `round-85` |
| new gate inputs (gates 4/5) | new files, expected to fail at baseline and pass at the new revision | placing them under `corpus/fixtures/` changes the 133 count; revision-sourced inputs make the baseline side unmeasurable (§4) |
| docs | README Round 6 sentence + `corpus/README.md` index entries | guide duplicating README prose instead of linking it |

Additional mechanism risks visible from the committed code and worth surfacing
to the checker/measure owners (no judgment, just the affected edges):
`check_bible.py:215-216` and `:223-224` are two independent silent branches;
`:234-237` clears the gate and previous values on any invalidity; `:238-245`
holds **both** comparisons; `:246-247` updates previous values after a valid
record without re-enabling the gate. A notice guarded only by `can_check_chain`
would vanish when an earlier malformed/dangling record already stopped
comparisons, and a single global (rather than per-item) notice flag would silence
a second affected item — both are called out in the inherited
`reports/round-1/critic.md` falsifier table.

## 8. Observations about concurrent state (no judgment)

The worktree `corpus/fixtures/check_bible.py` was modified **during** this scan
(grew from 330 to 339 lines, `git diff --stat` = `9 +++++++`, uncommitted), which
is why every checker line citation above is pinned to the committed blob at
`5eb9451`. Other uncommitted worktree changes at scan time: `LOG.md`,
`PROVINCE.md`, `SCORECARD.md`, `SHONEN.md`, and the untracked
`reports/round-1/`. I made no edit outside this report.

## 9. Unknowns and confidence

- **Unknown (not statically observable):** whether any naive-resume
  implementation would emit a definite finding on an inherited input. No
  inherited input combines an ambiguous holder with a downstream reversed or
  equal tick, so tick-suppression evidence must come from a new input; the
  isolated probe's ambiguity is terminal and cannot evidence downstream scope.
- **Unverified:** every recorded tuple above is read from the round-85 files
  produced by the *old* checker; I did not re-run the checker, and the peer's
  in-flight edit changes the worktree, so these are transcribed observations,
  not reproductions.
- **Bounded confidence:** the 133-dir inventory, the 5 provenance fixtures, the
  13 duplicate-id fixtures, the 25 probe-input files, and the 138 recorded
  tuples were enumerated exhaustively at `5eb9451` (path-set and digest level).
  No claim is made about coverage of the corpus as a whole, about any fixture's
  fictional content, or about behaviour on inputs outside this repository.