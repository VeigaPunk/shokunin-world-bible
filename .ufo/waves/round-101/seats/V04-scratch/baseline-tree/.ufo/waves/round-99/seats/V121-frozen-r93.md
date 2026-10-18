# V121 c1-frozen-r93-still — round 99

Seat: V121 (verifier). Claim checked: `map_obligations --frozen` r93 replay still passes, untouched by the r99 freeze-payload work (cross-tool isolation). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). Working-tree HEAD `337f0fa52b02626b7687eedbb2d99fab30446fe4`. Commands from the lane root with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Exclusive writes: this report and `.ufo/waves/round-99/seats/V121-scratch/` (`poll-start.txt`, `poll.log`, `replay-early.txt`, `replay.stdout`, `replay.stderr`, `final-evidence.txt`). Nothing else written. Did not run `dependency_freeze.py --freeze` or `--self-test` (those write the contract or a temp tree under the repo root).

Axes named, not scored: (1) frozen r93 replay receipt and exit; (2) byte identity of the map tool, its contract, and the snapshot against `4265df5`; (3) no import, subprocess call, or write from the freeze tool into those paths.

## Poll

Required before the concluding run: the frozen snapshot (present since round 94) and S1's producer report, so the replay is judged against a finished freeze turn rather than a plan.

S1 was absent through the logged window. `V121-scratch/poll.log` tries 1–30, `2026-10-18T01:17:03Z` through `2026-10-18T01:26:43Z`, each 20 s: reports only `S3-fixture-author.md` and `S4-fixture-docs.md`; contract mtime/size stable at epoch `1792285726` / 25987 bytes; `dependency_freeze.py` stable at epoch `1792285653` / 29104 bytes. That background poll was killed at its 600 s cap before a 40th try (`POLL EXHAUSTED` was not written). Earlier manual polls (`01:03Z`–`01:05Z`) saw the contract still moving (19291 → 20382 → 21007 bytes, then schema 2 / 18 cases). Stall-escape recorded: not filed ABSENT at the cap, because the freeze bytes were still an in-flight producer turn and this seat's subject is the map replay, not a line review of S1.

S1 report then landed: `.ufo/waves/round-99/seats/S1-full-file-pins.md`, 11971 bytes, mtime `2026-10-17 22:48:57 -0300`. Read in full. It is a finished producer report (chain 6/6, self-test 18/18, trailing `PASS:` line), not a plan. It states the tracked diff is only the two owned files and that it did not write the map tool. That claim was re-checked below; it was not taken as the isolation proof.

## Replay (after S1)

Same hashes before and after the read (`01:53:37Z` capture in `final-evidence.txt`; re-run `2026-10-18T02:04:48Z`):

```
$ python3 corpus/tools/map_obligations.py --frozen .ufo/waves/round-94/frozen/map-obligations-r93 ; echo EXIT:$?
SNAPSHOT inputs=4 digests=verified
OBLIGATIONS raw=12 mapped=12
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15
FROZEN expected=PASS/0 findings=none matched
RESULT PASS
EXIT:0
```

stderr empty (`wc -c` of `V121-scratch/replay.stderr` = 0). Receipt matches the tools README line for this command (`SNAPSHOT` digests verified, `RESULT PASS`, exit 0) and the r98 closure wording `SNAPSHOT inputs=4 digests=verified` / `FROZEN expected=PASS/0 findings=none matched`. Obligations 12/12 is the frozen r93 count. `expected.json` pins those four input digests and `exit_code` 0 / `PASS` / empty `finding_ids`; the tool's own `digests=verified` line is the pin check. An independent sha256 of the four inputs against `expected.json` at `01:22:15Z` (`replay-early.txt`) was MATCH on all four.

## Untouched vs baseline

`git diff --stat 4265df5 --` and `git diff --stat HEAD --` on `corpus/tools/map_obligations.py`, `corpus/tools/map-obligations-contract.json`, and `.ufo/waves/round-94/frozen/map-obligations-r93` were empty. `git status --porcelain` on those paths was empty.

`git show 4265df5:$f | cmp -s - $f` at `2026-10-18T02:04:48Z`:

```
MATCH corpus/tools/map_obligations.py
MATCH corpus/tools/map-obligations-contract.json
MATCH .ufo/waves/round-94/frozen/map-obligations-r93/expected.json
MATCH .ufo/waves/round-94/frozen/map-obligations-r93/entities.json
MATCH .ufo/waves/round-94/frozen/map-obligations-r93/relations.json
MATCH .ufo/waves/round-94/frozen/map-obligations-r93/timeline.json
MATCH .ufo/waves/round-94/frozen/map-obligations-r93/claim-excerpt-map.md
```

Live sha256 of the tool: `86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9`. Identical to `git show 4265df5:corpus/tools/map_obligations.py | sha256sum`. Because the tool bytes and the four pinned inputs match the baseline, this replay is the baseline tool on the baseline snapshot, not a rewritten checker.

Freeze payload did change, and only those two paths, relative to `4265df5`:

```
$ git diff --name-only 4265df5 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/map_obligations.py corpus/tools/map-obligations-contract.json .ufo/waves/round-94/frozen/map-obligations-r93
corpus/tools/dependency-freeze-contract.json
corpus/tools/dependency_freeze.py

$ git diff --stat 4265df5 -- corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
 corpus/tools/dependency-freeze-contract.json | 163 ++++++++++++++++++++++++---
 corpus/tools/dependency_freeze.py            |  67 ++++++++++-
 2 files changed, 207 insertions(+), 23 deletions(-)
```

That stat matches S1's own `git diff --stat` (contract +163, tool +67, 207 insertions, 23 deletions). Delivered contract at the replay: `schema_version` 2, `payload_schema_version` 2, 18 self-test cases, `markdown_tamper` present, ten `pinned_files`. sha256 `dependency_freeze.py` `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`; contract `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`. Same pair at `01:53:37Z` and `02:04:48Z`.

## Cross-tool

`map_obligations.py` contains no `dependency_freeze` and no `dependency-freeze-contract`. Its only `subprocess.run` re-invokes itself during `--self-test` (`command = [sys.executable, str(Path(__file__).resolve())]`). It does not read the freeze contract.

`dependency_freeze.py` mentions `map_obligations` once, a pre-existing docstring comparison of the exit-2 class (`freeze:20: matching map_obligations.py`), not an import or call. Its subprocess uses are `git rev-parse HEAD` and a self re-exec. The only contract write is `CONTRACT_PATH.write_text` inside `freeze()` (`corpus/tools/dependency-freeze-contract.json`). Self-test writes stay under `TemporaryDirectory` mirrors. Neither path is the map tool or `.ufo/waves/round-94/frozen/map-obligations-r93/`.

S1's ownership is those two freeze files. The map tool and the frozen snapshot are not producer-owned this round. The landed freeze diff does not include them, and the replay after that diff still exits 0.

## Bound

This does not re-run the freeze self-test, does not prove the ten-file pin is correct, and does not claim S2's README/SKILL freeze row or S5's knowledge notes (not required for this replay). It does not claim the replay would still pass if a later seat violated ownership and edited `map_obligations.py` or the snapshot. At `02:04:48Z` those files were still baseline bytes.

PASS — frozen r93 replay exits 0 (`SNAPSHOT inputs=4 digests=verified`, `OBLIGATIONS raw=12 mapped=12`, `FROZEN expected=PASS/0 findings=none matched`, `RESULT PASS`, empty stderr) after S1's full-file pin landed; map tool, map contract, and snapshot are byte-identical to `4265df5`; the freeze diff does not touch or call them.
