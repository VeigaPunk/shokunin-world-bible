# V26 — operability (round 99)

Seat: V26 operability. Exclusive writes: this report and
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V26-scratch/`
(`poll.sh`, `poll.log`, `s4-replay.txt`, `s4-*.out`, `s4-*.err`, `final-snapshot.txt`).
No product file written, no commit, no push, no network, no nested agents.
All commands from the lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` with
`python3` (3.14.7). Baseline: r98 closure `4265df5`; HEAD at seat time
`337f0fa` (blocked-dispatch note only; `git diff 4265df5` is LOG.md +
SCORECARD.md). Session cwd is the parent repo; every path below is absolute
or lane-root-relative and was re-checked.

Task: after producers, run every documented command in S4's README, S5's
notes, and the tools README addendum exactly as written. Never verify a plan.

Axes named for this seat: presence (the documenting surface exists), fidelity
(the command text is the one run), exit contract (observed exit is the one
the surface states or implies), non-harm (no corpus write, no invented
command). The S4 replay is the only move kept: it improves fidelity evidence
and harms none. Declaration-implied freeze/self-test commands were not run:
that would verify a plan.

## 0. Poll-wait

Own poll, 20 s cadence, 40 tries, watching producer reports `S1*.md`…`S5*.md`,
the r99 fixture README and map (not the r98 byte-copy placeholder), both S5
knowledge files, and a Round-99 marker in `corpus/tools/README.md`. Log:
`V26-scratch/poll.log`. ENDGAME: the poll waited on the five producer reports
only, not on all seats and not on SELF.

| Try | Time (local -03) | Result |
|---|---|---|
| 1 | 22:02:46 | fixture dir present as r98 byte copies; no producer reports |
| 5 | 22:04:06 | S4 report present; README/map no longer r98 copies |
| 14 | 22:07:06 | still missing S1/S2/S5 reports, both S5 notes, tools addendum |
| gap | 22:07:06–22:16:43 | first poll process killed by the host 300 s cap (TaskStop wall 267 s); resume delayed until 22:16:43. Recorded stall, not a 41st try |
| 15 | 22:16:43 | same missing set |
| 40 | 22:25:04 | `ABSENT-AFTER-40` — `S1-report S2-report S5-report r99-gate-blind-spot-table.md r99-lapse-scope-note.md tools-README-no-Round-99` |
| confirm | 22:27:42 and 22:29:58 | still absent. `find` for those two knowledge names under the lane and under `/home/vgpnk/Projects/shokunin` (maxdepth 3) returned nothing. `S2-scratch` empty. No `S5*` path |

Producer reports present at confirm: `S3-fixture-author.md` (22:01:40, 5069 bytes), `S4-fixture-docs.md` (22:03:54, 9303 bytes). S1 bytes did land without a report: `dependency_freeze.py` mtime 22:07:33 sha256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067`; contract mtime 22:08:46 sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`. `corpus/tools/README.md` and `SKILL.md` are unmodified versus HEAD (README sha256 `294dd56f29ce1fd40be3a80d365b33724c9cd1969d3f7b7abb271fd1adaaa207`; tail is still the Round-98 dated correction). No Round-99 heading, no `r99` string in the tools README.

## 1. S4 README — three commands, run as written

Surface: `corpus/fixtures/r99-window-lapse/README.md` lines 23–29, the only fenced block in the file (`grep -n '```'` → lines 25 and 29 only). sha256 `b93209417a918a88231dc12ba72b7314db5bf24eeaa52fbab761acadbe777049`, matching S4's report. Unchanged from the 22:05:13 replay through the 22:29:58 snapshot. `claim-excerpt-map.md` sha256 `d2fe20e581d1c29bdc22f9018f4bcc111c425c64132227d2868ff15cf1476e3d` (also S4's cited hash); `grep -c '```'` → 0; no `python3` / `sha256sum` line. Zero documented commands in the map.

Checker revisions at the replay (and still at 22:29:58; none of these three are in `git status`):

```
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
```

Transcript: `V26-scratch/s4-replay.txt` (stdout files `s4-bible.out`, `s4-support.out`, `s4-map.out`; all three stderr files 0 bytes). No pipeline on the tool itself.

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r99-window-lapse
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23; DISTINCT-ANCHORS 19/19
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J21 (J21: 70:> Tick 15: The crossing-window named in the original minute has closed.)
PASS S01; PASS S02
RECEIPT JSON-FACTS 21; EDITORIAL-ROWS 2; TOTAL-ROWS 23
SOURCE-SUPPORT 21/21; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 23/23; VALIDATED-ROWS 23/23
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r99-window-lapse
OBLIGATIONS raw=21 mapped=21
INVENTORY JSON-FACTS 21/21; EDITORIAL-ROWS 2/2; TOTAL-ROWS 23/23
RESULT PASS
exit=0
```

The README does not quote those receipt lines; it only documents the three commands. The observed exits are 0 and the terminal lines are `CLEAN` / `RESULT PASS`. Count claims in the README that these receipts touch: line 3 `6 entities / 1 relation / 8 events / 8 sources` was not re-parsed by this seat beyond the tools' own inventory; line 21's "21 source-attributed JSON pointer obligations" matches `raw=21 mapped=21` and `JSON-FACTS 21/21`. Fixture data mtimes are all ≤ 22:03:19, before the replay, so the receipts are on the same bytes S4 gated.

## 2. S5 notes — ABSENT

`corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md` do not exist. No S5 report. No documented command to run. Not substituted from the round declaration or from r98's note.

## 3. Tools README addendum — ABSENT

`corpus/tools/README.md` has no Round-99 addendum. Last heading class is the Round-98 dated correction. `SKILL.md` freeze row is likewise unmodified versus HEAD (still "17 cases", "five JSON tables", chain ending at `r98-clerk-filing`). No documented r99 command to run. S1's modified `dependency_freeze.py` / contract were not exercised: there is no delivered command block that names them, and running `--self-test` or a chain loop from the declaration would be verifying a plan.

## 4. Residue

`git status --porcelain` at 22:29:58:

```
 M corpus/tools/dependency-freeze-contract.json
 M corpus/tools/dependency_freeze.py
?? .ufo/waves/round-99/
?? corpus/fixtures/r99-window-lapse/
```

This seat added only files under `.ufo/waves/round-99/seats/V26-scratch/` and this report. No corpus modification.

## Bottom line

ABSENT — after 40 poll tries (confirm 22:29:58) S5's two notes and the tools README Round-99 addendum do not exist, so their documented commands cannot be run; S4's three README commands did run as written (check_bible CLEAN, support_check 21/21, map_obligations raw=21 mapped=21, all exit 0, stderr empty) and that subset is not a full-surface pass.
