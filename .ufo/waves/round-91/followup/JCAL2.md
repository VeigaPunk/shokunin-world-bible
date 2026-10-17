# JCAL2 — discrimination judge, r91 follow-up wave

Delivered tree: `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` (work commits `6332115` + `c2ab3d0`, baseline `a7c6a17`). All verdict evidence below is from the delivered tree; `/tmp/lore-r91-JCAL2` was scratch only. No commit, no push; repo writes limited to this report and `JCAL2-receipts.json`.

## Work performed

- Wait protocol (two checks, 60 s apart, one tool call): `waitcheck 1 2026-10-17T08:33:55-03:00 c2ab3d0 / dirty_lines=1`; `waitcheck 2 2026-10-17T08:34:55-03:00 c2ab3d0 / dirty_lines=1`; `TERMINAL waitchecks_done`. HEAD stayed at `c2ab3d0`; the single untracked porcelain line is the sibling follow-up directory `.ufo/waves/round-91/followup/` (H3/H4/JCAL5/JDEP3/K1 artifacts). No tracked drift; proceeded with what exists.
- Built scratch checkers: e97613c via `git show`, delivered via `cp`, X3-revert and X2-revert via `patch --batch --fuzz=0 -R -p1` of the round-90 gate patches. Wrote two scratch drivers (`measure.py`, `census2.py`).
- Ran: the four paired differential runs; three 166-directory censuses (e97613c vs delivered; delivered vs X3-revert; delivered vs X2-revert); the C9 watch's "Reproducible boundary probe" verbatim; the falsification-trigger probe block verbatim and substituted.
- Cross-checks (read-only): `B3-before-state.json`, `C10.md`, `C5.md`, `C8.md`, `X1.md`, `S1.md`.

## Before → after measurements

**Checker identities.** Exact commands and observed output:

```sh
sha256sum corpus/fixtures/check_bible.py
git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | sha256sum
git show a7c6a17:corpus/fixtures/check_bible.py | sha256sum
git diff --stat a7c6a17..c2ab3d0 -- corpus/fixtures/check_bible.py
```

```text
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556  -
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  -
(empty diff output; exit 0)
```

The r91 commits did not touch the checker; the delivered hash equals the C9 watch's pinned hash and the r90-closure hash.

**Paired differential.** Scratch checkers: `checker-e97613c.py` (e2bb9639…), `checker-delivered.py` (ff9fd2aa…). Command: `python3 /tmp/lore-r91-JCAL2/measure.py diff`, each run `python3 <checker> corpus/fixtures/<fixture>` with cwd `lore-shokunin/`. Observed (stdout SHA-256, exit, stderr):

```text
r91-c1-null-chain      e97613c: exit=1 stderr_empty=YES sha=3a337ba4bba9c829f9b2bba9657e61d8838ad491d44c0861fa1d6f9d40e05c89
r91-c1-null-chain      delivered: exit=1 stderr_empty=YES sha=615dc0564f531352a574ef2f53c48be42f4e53ad1fac4aa88756e4bba2fada5b
r91-c1-tick-unresolved e97613c: exit=1 stderr_empty=YES sha=71b4ea433d85ba52f11482a5d089c564641702989763ced39d61c5eee3748e85
r91-c1-tick-unresolved delivered: exit=1 stderr_empty=YES sha=d754e96f7c01e6fb6eff12168a732d5a6125f428a9207bd74fc49bbdcbb25d88
```

Diff per fixture — exactly one line replaced in a 2-line (null) / 4-line (tick) output, on the declared repaired line:

```diff
--- r91-c1-null-chain@e97613c
+++ r91-c1-null-chain@delivered
@@ -1,2 +1,2 @@
-VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'mira'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
+VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'mira', got None
 1 violation(s); no canon changed
```

```diff
--- r91-c1-tick-unresolved@e97613c
+++ r91-c1-tick-unresolved@delivered
@@ -1,4 +1,4 @@
 VIOLATION: entities[1].first_appearance: required nonempty str
-VIOLATION: entities[4].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); provenance tick 1 must be greater than previous tick 3
+VIOLATION: entities[4].provenance[1].tick: provenance tick 1 must be greater than previous tick 3
 VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
 3 violation(s); no canon changed
```

The tick fixture's qualified chain-break line is byte-identical across checkers; the deliberate invalid-duplicate schema diagnostic (`entities[1].first_appearance`) and summary lines are unchanged. All four actual outputs match the README-declared blocks byte-for-byte (`readme_match_e97613c=true`, `readme_match_delivered=true` for both fixtures). My four stdout hashes equal C10's recorded receipts exactly, and the four full outputs match C8's recorded stdout blocks.

**166-directory census, e97613c vs delivered.** Command: `python3 /tmp/lore-r91-JCAL2/measure.py census`; per directory runs each checker once and compares `(exit, stdout SHA-256, stderr)`:

```text
total_dirs=166
changed_e97613c_vs_delivered = [r91-c1-null-chain, r91-c1-tick-unresolved]
exit_changes_e97613c_vs_delivered = []
stderr_changes_e97613c_vs_delivered = []
```

0 of the 164 pre-existing fixture directories changed; only the two new fixtures differ. This reproduces the claimed "0 changed + 2 new of 166".

**Simulated X3-revert (tick gate).**

```sh
mkdir -p /tmp/lore-r91-JCAL2/revert/corpus/fixtures
cp /tmp/lore-r91-JCAL2/checker-delivered.py /tmp/lore-r91-JCAL2/revert/corpus/fixtures/check_bible.py
cd /tmp/lore-r91-JCAL2/revert
patch --dry-run --batch --fuzz=0 -R -p1 < .../lore-shokunin/.ufo/waves/round-90/patches/X3-c1-tickonly.patch
patch --batch --fuzz=0 -R -p1 < .../lore-shokunin/.ufo/waves/round-90/patches/X3-c1-tickonly.patch
sha256sum /tmp/lore-r91-JCAL2/revert/corpus/fixtures/check_bible.py
```

Observed: both the dry-run and the apply printed `Hunk #1 succeeded at 321 (offset 2 lines).`; reverted checker SHA-256 `87d7f2b503172497d7727d81a0563051e1bc5248e738b3fd8249241185fda3f4`. Running it on the tick fixture flipped exactly line index 1 back to the hedged form, left the chain-break line byte-identical, and its full stdout (SHA-256 `71b4ea43…`) is byte-identical to the e97613c checker's output for that fixture. The null-chain fixture output was unchanged by the revert (`revert_changed_line_indexes=[]`). Census `delivered vs x3revert` over 166 dirs:

```text
changed_delivered_vs_x3revert = [r91-c1-tick-unresolved]
```

**Simulated X2-revert (null gate), extra for the "either gate" wording.**

```sh
patch --batch --fuzz=0 -R -p1 -d /tmp/lore-r91-JCAL2/x2revert < .../round-90/patches/X2-c1-nullonly.patch
sha256sum /tmp/lore-r91-JCAL2/x2revert/corpus/fixtures/check_bible.py   # 2cc5db538cb69574a002097dba26d4fe5fc6303e71070d6e3bc2defe17a4a264
```

Reversed null-gate output for `r91-c1-null-chain` returned to the hedged e97613c line byte-for-byte (stdout SHA-256 `3a337ba4…`); the tick fixture was unchanged. Census `delivered vs x2revert`: `changed = [r91-c1-null-chain]` only. Each gate's revert flips exactly its own fixture, and only that fixture.

**C9 watch pin and probe block.** `git ls-files corpus/knowledge/r91-c9-watch.md` → tracked; `git log --oneline -- corpus/knowledge/r91-c9-watch.md` → landed in `6332115`. The watch's probe block, run verbatim from `lore-shokunin/`:

```sh
sha256sum corpus/fixtures/check_bible.py
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-null-chain
python3 corpus/fixtures/check_bible.py corpus/fixtures/r91-c1-tick-unresolved
```

Observed: hash line `ff9fd2aa… corpus/fixtures/check_bible.py` (equals the pinned hash); null-chain exit 1, one violation, exact declared line; tick fixture exit 1, three violations including the declared invalid-duplicate diagnostic, tick line definite and chain-break line qualified — all as the watch requires. The watch's B3 cross-reference is a tracked file and does hedge both lines (read at the delivered tree).

**Falsification trigger.** Verbatim with the placeholder in place, `python3 corpus/fixtures/check_bible.py corpus/fixtures/<counterexample>` is a bash syntax error (exit 2, `syntax error near unexpected token ';'`) — `<…>` must be substituted, as the trigger's own wording requires ("after adding such a durable counterexample"). Substituted (`<counterexample>`=`r91-c1-tick-unresolved`, control `r91-c1-null-chain`), the block runs and yields a complete record: `sha256sum` ff9fd2aa…; counterexample run rc=1, 4 stdout lines, 0 stderr bytes; control rc=1, 2 lines, 0 stderr; the second checker hash is recordable via the pinned form `git show e97613cc276f5fa9cac49ff1900798cf6863c020:corpus/fixtures/check_bible.py | sha256sum` → e2bb9639… The four gates are concrete, checkable statements (uniquely identified valid item + nonnegative ticks; unresolved non-null holder with raw/resolved counts + paired control; independently reviewable sequence-scope evidence; delivered checker's definite inversion rendered indeterminate).

**Repository boundary.** `git rev-parse HEAD` = `c2ab3d07eaa86ce58f3f9c7fdff702f4b91ea7b7` throughout; `git diff --quiet HEAD -- corpus/fixtures corpus/knowledge` → clean. The only untracked path before my writes was the sibling `followup/` directory.

## Findings & named debt

- **C1 calibration, discrimination — improved (bounded).** The durable pair now discriminates both r90-repaired gates on the delivered tree: each fixture's output differs between e97613c and delivered on exactly its declared line, all README blocks match byte-for-byte, and a silent revert of either gate flips exactly that gate's fixture back to the hedged e97613c text (restoring the e97613c stdout hash byte-identically). Bounded to fixture scaffolding plus the adjudicated C9 integer-ordering ruling; no canon claim.
- **Non-interference census — unchanged.** 164/164 pre-existing fixture directories are byte-identical in stdout hash, exit, and stderr across the two checkers. The two r91 fixtures are the only deltas, and revert censuses touch only their own fixture.
- **Watch pin integrity — improved.** The pinned `ff9fd2aa…` equals the delivered checker and the r90-closure checker; the watch and both fixtures are tracked (landed in `6332115`); the checker is unchanged across `a7c6a17..c2ab3d0`.
- **Falsification trigger — concrete and runnable.** Commands execute; the recording requirements (complete stdout/stderr/exit, tick/holder mappings, two checker hashes) are all reachable with the pinned command forms. Named nuance: the probe block is a template — the `<counterexample>` placeholder must be substituted before the shell can parse the line (verbatim run is a bash syntax error, not a checker finding). Low severity; the trigger text already conditions on adding the counterexample.
- **Named debt:** (1) the trigger block restates the delivered `sha256sum` but not the e97613c command; it is replayable from the same document's pinned B3 reference — a future counterexample report should use the `git show e97613cc…` form above. (2) Context, not debt: C8 (work wave) noted X1's shared record IDs across fixtures; the census is per-directory, so this does not affect discrimination or census results.
- No harmed axis found. No trade in the delivered change within its declared scope; reopening the underlying ruling is the trigger's own four-gate procedure.

## Handoff

- `.ufo/waves/round-91/followup/JCAL2.md` — this report.
- `.ufo/waves/round-91/followup/JCAL2-receipts.json` — machine-readable receipts (hashes, census lists, revert evidence, probe outputs).
- Scratch `/tmp/lore-r91-JCAL2` retained for replay (checkers incl. both reverted builds, `measure.py`, `census2.py`, run outputs; 15 files, 168K); reconstruction commands are in this report (`git show` extraction, `patch -R` rebuilds, `measure.py diff|census`, `census2.py`).
- Gaps: none for this seat's five mission items (both fixtures under both checkers; X3-revert flip; hash pin; trigger runnability — all verified). Sibling follow-up artifacts exist untracked in `followup/` (H3/H4/JCAL5/JDEP3/K1); they were not read as evidence and did not affect the measurements. No commit or push was made.