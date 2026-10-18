# F14 — preservation-regression

**Seat:** F14 (round-94 FOLLOW-UP, lore-shokunin) · **Role:** independent preservation regression — replay every inherited `corpus/fixtures/` CLI tuple with the delivered checker and diff against pinned prior saved outputs.

**Verdict in one line:** 167/167 inherited fixture directories reproduce exit code, stdout SHA-256, and violation count exactly against every modern pinned receipt; the 36 body-level differences that do exist are confined to superseded transcripts and are fully explained (5 path-embedding, 4 pre-r94 checker-era drift).

---

## 1. What was replayed

| Item | Value | Evidence |
|---|---|---|
| Fixture directories on disk | 168 | `python3 -c "...len([p for p in corpus/fixtures.iterdir() if p.is_dir()])"` → `total dirs: 168` |
| Replayed (r94-paired-crossing excluded per seat) | **167** | → `excluding r94: 167` |
| Invocation | `python3 [-I] corpus/fixtures/check_bible.py corpus/fixtures/<name>`, cwd = repo root | matches W04 meta `checker_command_per_directory` and JCAL5 meta `checker_invocation` |
| HEAD during replay | `65a93298cb100fdbf5732ac6de55f01a683c02d8` | `git rev-parse HEAD` |
| Corpus changed by the follow-up declaration? | no | `git diff --stat abbc3e0 65a9329 -- corpus/` → empty |
| My writes | none outside this report | `git status --short` → `?? .ufo/waves/round-94/followup/` only |

## 2. Checker identity — the precondition for "no regression"

The delivered checker is byte-identical to the parent baseline and to every pinned checker hash in the receipts:

```
$ sha256sum corpus/fixtures/check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
$ git show 9c2eea3:corpus/fixtures/check_bible.py | sha256sum
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  -
$ git show abbc3e0:corpus/fixtures/check_bible.py | sha256sum
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  -
```

Cross-checked against pinned hashes:

- `.ufo/waves/round-93/followup/JCAL5-tuples.json` → `base_census_meta.checker_sha256` = `after_census_meta.checker_sha256` = `ff9fd2aa…`
- `.ufo/waves/round-93/deepseek/F02-pins.json` → `checker_worktree_sha256` = `ff9fd2aa…`
- `.ufo/waves/round-93/deepseek/F19-replay.json` → `delivered_checker_sha256` = `ff9fd2aa…`

So the checker is invariant across r93 base (`87779a0`) → r94 parent (`9c2eea3`) → r94 WORK (`abbc3e0`) → HEAD (`65a9329`). The r94 WORK wave did not touch it (`git diff --stat 9c2eea3 abbc3e0` lists no `corpus/fixtures/check_bible.py`).

## 3. Full tally — fresh replay vs pinned receipts

Fresh replay of all 167 dirs, comparing `(exit, stdout_sha256, violation_count)`:

```
no-I vs -I identical: True
W04-baseline: dirs=167 exit_deltas=0 sha_deltas=0 violation_deltas=0 stderr_nonempty=0
JCAL5-after:  dirs=167 exit_deltas=0 sha_deltas=0 violation_deltas=0 stderr_nonempty=0
exit_counts: {0: 33, 1: 134}
violation_lines_total: 421
```

```
F02-tuples:   pinned=167 exit_deltas=0 sha_deltas=0 violation_deltas=0
F01-tuples:   pinned=167 exit_deltas=0 sha_deltas=0 violation_deltas=0
JCAL1-tuples: pinned=167 exit_deltas=0 sha_deltas=0 violation_deltas=0
```

| Pinned receipt | Revision / provenance | Dirs compared | exit Δ | sha256 Δ | violation Δ |
|---|---|---:|---:|---:|---:|
| `.ufo/waves/round-94/work/W04-baseline.json` | parent baseline `9c2eea3` | 167 | 0 | 0 | 0 |
| `.ufo/waves/round-93/followup/JCAL5-tuples.json` `after_rows` | r93 head `65838f8` | 167 | 0 | 0 | 0 |
| `.ufo/waves/round-93/followup/JCAL5-tuples.json` `base_rows` | r93 base `87779a0` | 166 | 0 | 0 | 0 |
| `.ufo/waves/round-93/deepseek/F01-tuples.json` | r93 | 167 | 0 | 0 | 0 |
| `.ufo/waves/round-93/deepseek/F02-tuples.json` | r93 | 167 | 0 | 0 | 0 |
| `.ufo/waves/round-93/followup/JCAL1-tuples.json` | r93 | 167 | 0 | 0 | 0 |

`base_rows` is a strict subset of `after_rows`: `base-only: []`, `after-only: ['corpus/fixtures/r93-m2-kojiki-cluster']`, `base vs after differing: 0` — so the 167/167 match against `after_rows` entails 166/166 against `base_rows`.

Aggregate census also reproduces: fresh `{0: 33, 1: 134}` and `violation_lines_total: 421` equal W04 `_meta.summary` `{"directory_count": 167, "exit_counts": {"0": 33, "1": 134}, …, "violation_lines": 421}`.

`violation_count` is defined here as the number of stdout lines starting `VIOLATION:`. This definition is validated, not assumed: applied per-fixture it yields 0 deltas against W04's per-fixture `violation_count`, and its sum is 421, exactly W04's `violation_lines`.

**`-I` and plain `python3` are interchangeable** on this corpus: `no-I vs -I identical: True` — the full 167-tuple dicts compare equal, so the seat's literal command form and the receipts' `-I` form agree byte-for-byte.

### 3.1 `corpus/live/runs/` transcripts

These are `.txt` transcripts with a `$ python3 …` line, an `exit_code=N` line, and the checker body. Compared on the seat's criterion (exit code + output class):

| Pin generation | Fixture transcripts | On-disk fixture present | exit Δ | class Δ |
|---|---:|---:|---:|---:|
| `corpus/live/runs/round-85/` | 133 | 133 | 0 | 0 |
| `corpus/live/runs/20261012T*/` (21 dirs) | 74 | 72 | 0 | 0 |

- `round-85` count matches its own manifest: `manifest.txt` → `- 133/133 fixture dirs replayed into ./<fixture>.txt`.
- The two transcripts without an on-disk fixture are `name-duplicate` and `name-unique`; their inputs live at `corpus/live/rejected-r4/name-duplicate` and `…/name-unique`, i.e. outside `corpus/fixtures/`, so they are outside this seat's replay scope.
- 35 on-disk fixtures have no `runs/` transcript at all (e.g. `r87-chain-unique-broken`, `r87-probe-entry-shape`, `r90-c1-*`, `r91-c1-*`); they are covered only by the JSON receipts above. `round-85/manifest.txt` and the five `probe-r85-*.txt` files are not fixture transcripts and were excluded.

## 4. Byte-level body comparison and the 9 divergent fixtures

Beyond exit/class, I diffed the exact stdout body (transcript lines after `exit_code=` vs fresh stdout). Result: **669 exact (exit + body) matches, 36 mismatches across 9 distinct fixtures** — every mismatch in a superseded generation, none against a modern receipt.

```
exact (exit+body) matches: 669
body/exit MISMATCHES: 36
distinct mismatching fixtures: 9
```

All 36 are explained by exactly three causes:

**(a) Argv path embedding — 5 fixtures, benign, already documented.** The diff is solely the path prefix inside the Errno diagnostic (transcript ran under `.shokunin/lore/`):

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r62-missing
VIOLATION: timeline.json: cannot load JSON: [Errno 2] No such file or directory: 'corpus/fixtures/r62-missing/timeline.json'

transcript corpus/live/runs/round-85/r62-missing.txt:
VIOLATION: timeline.json: cannot load JSON: [Errno 2] No such file or directory: '.shokunin/lore/corpus/fixtures/r62-missing/timeline.json'
```

Affected: `r5-missing-file`, `r62-missing`, `r67-claim-source-unavailable-control`, `r67-claim-source-unavailable-empty`, `r67-claim-source-unavailable-whitespace`. These are exactly `.ufo/waves/round-93/deepseek/F02-pins.json` → `dirs_missing_section_files` = `{"r5-missing-file": ["contradictions"], "r62-missing": ["timeline"], "r67-claim-source-unavailable-control": ["sources"], …}`, and the round-93 W22 note states the only permitted normalization is "the exact quoted missing JSON path in its Errno diagnostic". Exit code and violation count are unchanged. Not a regression.

**(b) Violation drift in the oldest timestamped transcripts — 2 fixtures.**

```
===== r12-ambiguous-actor @20261012T175244Z =====
@@ -1,0 +2 @@
+VIOLATION: relations[0].from: ambiguous entity 'mira'
@@ -4 +5 @@
-3 violation(s); no canon changed
+4 violation(s); no canon changed

===== r21-ambiguous-actor @20261012T193022Z =====
@@ -1,0 +2 @@
+VIOLATION: relations[0].from: ambiguous entity 'mira'
@@ -5 +6 @@
-4 violation(s); no canon changed
+5 violation(s); no canon changed
```

Fresh output agrees with `round-85`'s own transcript and with all modern receipts:

| Source | `r12-ambiguous-actor` | `r21-ambiguous-actor` |
|---|---|---|
| Fresh (delivered checker) | exit 1, 4 | exit 1, 5 |
| W04-baseline (`9c2eea3`) | exit 1, 4 | exit 1, 5 |
| JCAL5 base+after, F01, F02, JCAL1 | exit 1, 4 | exit 1, 5 |
| `runs/round-85/` transcript | exit 1, 4 | exit 1, 5 |
| `runs/20261012T175244Z` / `T193022Z` | exit 1, 3 | exit 1, 4 |

Every one of the 21 timestamped dirs that carries `r12-ambiguous-actor` records `(1, 3)`; `round-85` and all JSON receipts record `(1, 4)`. Since the parent baseline `9c2eea3` already records 4 and 5, this drift predates r94 entirely.

**(c) One extra provenance diagnostic vs `round-85` — 2 fixtures.**

```
===== r61-independent-empty @round-85 =====
@@ -10,0 +11 @@
+VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: provenance attached to a non-item entity at entities[0].provenance
@@ -18 +19 @@
-17 violation(s); no canon changed
+18 violation(s); no canon changed

===== r61-independent-unavailable @round-85 =====
@@ -2,0 +3 @@
+VIOLATION: entities[0].provenance[0]: provenance continuity and tick-order comparisons remain unassessed (input-structural finding, not sourced-canon); first stop: source table unavailable at entities[0].provenance
@@ -7 +8 @@
-6 violation(s); no canon changed
+7 violation(s); no canon changed
```

Fresh agrees with the modern pins: W04 and JCAL5 `after_rows` both record `r61-independent-empty` = `{"exit": 1, "stdout_sha256": "b3811fdc…", "violation_count": 18}` and `r61-independent-unavailable` = `{"exit": 1, "stdout_sha256": "02a2876c…", "violation_count": 7}` — identical to fresh stdout SHA-256. The `round-85` transcript is stale: `runs/round-85/manifest.txt` pins its checker as `sha256 88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`, which is **not** the delivered `ff9fd2aa…`. The diagnostic was therefore added between those two checker revisions, and it is present already at the r93 base `87779a0` (JCAL5 `base_rows` also records 18/7). Pre-r94 by two rounds.

## 5. What this does and does not establish

Established: no preservation regression. For all 167 inherited directories the delivered checker reproduces the pinned exit status, stdout bytes, and violation count exactly, against six independent modern receipts spanning r93 base through r94 parent; aggregate counts (33/134, 421) reproduce; `-I` is a no-op; the 36 body diffs against legacy transcripts are each attributed to a superseded generation, with the delivered checker siding with the modern pins in every case.

Not established / out of scope:

- `corpus/fixtures/r94-paired-crossing` was excluded by seat instruction; its own behavior is C1's to verify.
- I compared observed tuples only. I did not independently establish the *intended* expected value of each negative fixture — "unchanged" is not "correct". W04's own `historical_classification_note` makes the same reservation.
- `name-duplicate` / `name-unique` transcripts were not replayed (no `corpus/fixtures/` directory).
- 35 fixtures are covered only by the JSON receipts, never by a `runs/` transcript.
- The `round-85` transcript's checker (`88c9b1d0…`) is not present in this worktree, so the two pre-r94 checker-era changes in §4(b)/(c) are localized by revision pin, not by reading their source diff.
- No scratch files were retained; the two temporary `/tmp/F14-*.json` intermediates were deleted (`rm -f … && echo "temp files removed"` → `temp files removed`).

---

**BOTTOM LINE: PASS** — all 167 inherited fixture directories replayed with the delivered checker reproduce exit code + stdout SHA-256 + violation count with 0 deltas against `W04-baseline`, `JCAL5` (base and after), `F01`, `F02`, and `JCAL1` tuples, and 0 exit/class deltas against every `corpus/live/runs/` transcript; the only body-level differences (9 fixtures) are all in superseded transcript generations, traced to argv path embedding or checker revisions that predate the r94 baseline.
