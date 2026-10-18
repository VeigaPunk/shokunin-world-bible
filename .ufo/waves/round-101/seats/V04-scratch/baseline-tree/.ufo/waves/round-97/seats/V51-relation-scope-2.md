# V51 — relation-scope-2 (round 97)

- **Seat:** V51 relation-scope-2 (verifier). Lane repo: `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo; every path below is lane-relative, every command run from the lane repo root with `python3`).
- **Baseline:** r96 closure `f3e09f9` (HEAD `2393934`). Round-97 wave spec in `LOG.md` tail (C1/C2/C3).
- **Seat claim under test:** `corpus/fixtures/r97-crossing-acknowledgment/relations.json` is byte-identical r96→r97; the map relation row is unchanged; no new relation semantics.
- **Writes:** this report only, plus scratch `.ufo/waves/round-97/seats/V51-scratch/` (`poll.sh`, `poll.log`, `census.py`, `r96-map-baseline.md`). No commits, no network, no nested agents.
- **Poll-wait:** r97 directory absent at 18:42–18:44; first appearance 18:44:16 (`stat`), R4's authored files 18:44:30, R5's map 18:48:56 / README 18:49:14, R4 report 18:50:28, R5 report ~18:51. Verified only against on-disk artifacts and producer reports (R1/R2/R4/R5 reports present and read; R6's report was still absent at my last check — R6's artifact `corpus/knowledge/r97-acknowledgment-scope-note.md` exists and is read below).

## Verdict on the seat claim

| Sub-claim | Verdict | One-line evidence |
|---|---|---|
| `relations.json` byte-identical r96→r97 | **CONFIRMED** | sha256 `c279254b…` for r97 == r96 worktree == r96 baseline `f3e09f9`; `cmp` IDENTICAL; 139 bytes |
| Map relation row unchanged | **CONFIRMED (bounded)** | J11 row parsed-equal to r96 in all 7 cells except the path-qualified namespace cell (`r96-crossing-response:` → `r97-crossing-acknowledgment:`), the same transformation r96 applied to r95's row |
| No new relation semantics | **CONFIRMED (bounded)** | exactly 1 relation row in the r97 map; J17 is the only added row (a timeline event); type census 10 types unchanged; no relation-type string beyond the inherited one anywhere in the fixture; contract change is only the `dual_pointer` pointer-grammar case |

## 1. `relations.json` byte-identity (r96 → r97, and across the arc)

```
$ sha256sum corpus/fixtures/r97-crossing-acknowledgment/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r97-crossing-acknowledgment/relations.json
$ git show f3e09f9:corpus/fixtures/r96-crossing-response/relations.json | sha256sum
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  -
$ cmp corpus/fixtures/r96-crossing-response/relations.json corpus/fixtures/r97-crossing-acknowledgment/relations.json && echo CMP-IDENTICAL
CMP-IDENTICAL
$ wc -c corpus/fixtures/r97-crossing-acknowledgment/relations.json
139 corpus/fixtures/r97-crossing-acknowledgment/relations.json
$ cat -A corpus/fixtures/r97-crossing-acknowledgment/relations.json
[$
  {$
    "from": "aru",$
    "to": "evin",$
    "type": "agreed_co_stewardship_for_this_crossing",$
    "source_id": "crossing-minute"$
  }$
]$
```

Wider check — all four crossing-arc fixtures carry the same 139-byte file, and r94/r95 are untouched versus baseline:

```
$ sha256sum corpus/fixtures/r94-paired-crossing/relations.json corpus/fixtures/r95-crossing-aftermath/relations.json \
            corpus/fixtures/r96-crossing-response/relations.json corpus/fixtures/r97-crossing-acknowledgment/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r94-paired-crossing/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r95-crossing-aftermath/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r96-crossing-response/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r97-crossing-acknowledgment/relations.json
$ for f in r94-paired-crossing r95-crossing-aftermath; do a=$(git show f3e09f9:corpus/fixtures/$f/relations.json | sha256sum | cut -d' ' -f1); b=$(sha256sum corpus/fixtures/$f/relations.json | cut -d' ' -f1); [ "$a" = "$b" ] && echo "$f: worktree == baseline ($a)"; done
r94-paired-crossing: worktree == baseline (c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9)
r95-crossing-aftermath: worktree == baseline (c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9)
```

## 2. Map relation row

Cell-by-cell comparison of every `J##` row of the r96 and r97 maps (script in scratch; rows split on `|`):

```
r96 J-rows: 16  r97 J-rows: 17
r97-only: ['J17']  r96-only: []
J01: cells=7/7 diffs=[(2, '`r96-crossing-response:paired-clock`', '`r97-crossing-acknowledgment:paired-clock`')]
… (J02–J10 same single-cell diff) …
J11: cells=7/7 diffs=[(2, '`r96-crossing-response:crossing-minute`', '`r97-crossing-acknowledgment:crossing-minute`')]
… (J12–J16 same single-cell diff) …
ALL 16 inherited J-rows (J01..J16) parsed-equal to r96 in all 7 cells except cell 3 (path-qualified namespace): True
J11 relation row identical outside namespace cell: True
new rows: ['J17']
```

Raw J11 rows (r96 repaired map `:32`, r97 map `:32`):

```
| J11 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `crossing-minute` | `r96-crossing-response:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` |
| J11 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `crossing-minute` | `r97-crossing-acknowledgment:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` |
```

Precedent (the identical single-cell transformation happened r95→r96):

```
| J11 | `relations.json#/0` (…) | `crossing-minute` | `r95-crossing-aftermath:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, …` |
| J11 | `relations.json#/0` (…) | `crossing-minute` | `r96-crossing-response:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, …` |
```

The r96 repair did not touch the relation row. My own `git diff -U0` against the baseline shows exactly two hunks, neither on a `J##` row:

```
@@ -44 +44 @@  -|---|---|---|---|---|---:|---|---|   +|---|---|---|---|---:|---|---|
@@ -50 +50 @@  -The inherited tick-9 … The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.
             +The inherited tick-9 … The new tick-12 event encodes only Evin's second account … not perpetual performance or alliance.
```

R5's own declared hashes match mine: r97 map `49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f`, README `d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f`.

## 3. No new relation semantics

- **Exactly one relation row in the map:** `grep -c "relations.json#"` on the r97 map → `1` (the J11 row). The only added row is J17 = `timeline.json#/5` (event `acknowledgment-aru-records`, source `aru-acknowledgment-note`, span 44-53).
- **Type census (baseline vs worktree, `corpus/fixtures/**`):**

```
BASELINE corpus/fixtures @f3e09f9: 170 files, 157 rows, 10 types
WORKTREE:                          171 files, 158 rows, 10 types
  135 carries / 9 allied_with / 4 agreed_co_stewardship_for_this_crossing / 3 consults / 2 records_departure /
  1 annotates / 1 filed_at / 1 keeps_watch_with / 1 records_at / 1 wields
```

  Same 10-type set; the only count change is `agreed_co_stewardship_for_this_crossing` 3→4, produced solely by the new fixture carrying the byte-identical inherited file. No new type string anywhere.
- **Only relation-type occurrence in the r97 fixture:** `grep -rn "agreed_co_stewardship\|relations" corpus/fixtures/r97-crossing-acknowledgment/` matches only `relations.json:5` (`"type": "agreed_co_stewardship_for_this_crossing"`) and the map's J11 row. Nothing in README/timeline/sources/notes asserts a second or differently-typed relation.
- **Tooling side (adjacent, bounded):** the contract `scope` string is unchanged (still the generic "…first_appearance values, entity claims, relations, and timeline records…"), the only contract diff is the added `{"id": "dual_pointer", "exit": 1, "finding_ids": ["dual_pointer"]}` case (24→25, order preserved, no shared case changed), and R1's tool diff adds only the `dual_pointer` case plumbing + the loader tightening (`set(CORE_SELF_TEST_CASES)` → `set(SELF_TEST_CASES)`). The `dual_pointer` fixture is a legacy-dialect pointer-grammar probe (`entities[0].first_appearance` cell naming a second token); its `relations[0]` row is test scaffolding, not a corpus relation.
- **Receipts (my own runs, on the delivered revision):**

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS
EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
EXIT=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT=0
```

  (I ran these; they are read-only on fixtures — no fixture byte changed; see §5 hash stability.)

## 4. Bounded observations (reported, not failures)

1. **The repaired r96 map's prose no longer names the relation bound in its normalization section.** Baseline `claim-excerpt-map.md:50` ended "…The new relation encodes only the agreement for this crossing, not perpetual performance or alliance." The repaired line replaces it with a tick-12 *event* sentence ending "…adds no duty beyond this crossing, not perpetual performance and alliance." Consequence: `grep -c "relation"` on the repaired r96 map = 2 (scope line + J11 row) vs 3 at baseline, and the r97 map (which inherits the repaired base) has no occurrence of "agreement for this crossing" or "perpetual" in its prose. The bound itself is not lost: the J11 row's anchor quotes it verbatim ("for this crossing only"), and it is stated in `r96-crossing-response/README.md:11` ("the agreement covered this crossing only… It is not evidence of an alliance, a continuing practice, perpetual performance…"), `sources.json` `crossing-minute.reliability_note` ("not evidence of continuing performance, a standing alliance…"), `corpus/knowledge/r96-response-scope-note.md:23`, and for r97 in `README.md:11` plus `corpus/knowledge/r97-acknowledgment-scope-note.md:24` ("Scope bound (inherited, unchanged) | …relations.json#/0, byte-identical to r96…"). So: a prose-level bound statement moved from map to README/scope-note; no data row, pointer, anchor, span, or mode changed, and no relation semantic was added or altered. R4/R5/R6 all document this repair as cosmetic and the declaration mandates the sentence fix — flagged only so the closure pass can decide whether the map should retain an explicit relation-bound sentence.
2. **Transient temp-dir leakage at the repo root (host hygiene, not residue):** `git status` twice showed an untracked `map-obligations-self-test-<random>/` at the lane root (18:42 `…b84jmmpi`, ~18:45 `…vw2etmyr`); each vanished within seconds (the tool's `TemporaryDirectory(prefix="map-obligations-self-test-", dir=ROOT)`). Final `ls -d map-obligations-self-test-*` → `No such file or directory`; no residue.
3. **Census text drift (read-only for me):** `corpus/fixtures/README.md` still states the r96 census while `ls -d corpus/fixtures/*/ | wc -l` = 171. Already flagged by R5; closure doc item.

## 5. Hash stability and hygiene (final pass 18:51:47)

```
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r97-crossing-acknowledgment/relations.json
49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  corpus/fixtures/r97-crossing-acknowledgment/claim-excerpt-map.md
d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  corpus/fixtures/r97-crossing-acknowledgment/README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r96-crossing-response/relations.json
e851f068cfd7ed02c97054df18729c4c5a9b8bf60d99d7c9116f427d765440de  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json
```

Every hash equals the producer-declared value (R1 §delivered, R2 §delivered, R4 §repair, R5 §deliverables), and the r97 fixture's relation-relevant bytes were stable across my checks 18:44:16 → 18:51:47. `git status --porcelain` at the final pass shows only producers' tracked edits (LOG.md, r96 map, tools README, dependency_freeze.py, contract, map_obligations.py) and the r97 untracked additions — no stray write from this seat.

## Non-claims

I verified relation bytes, the map relation row, the relation-type surface, and the two tool receipts above. I did not judge C1's loader/self-test behavior beyond the contract diff, C2's `dependency_freeze` guard, R4's fixture narrative quality, or entailment/canon/chronology questions.

## Bottom line

**PASS** — `relations.json` is byte-identical r96→r97 (sha256 `c279254b…`, `cmp` IDENTICAL, 139 B, identical across r94–r97 and unchanged vs baseline), the map's J11 relation row is unchanged in all cells except the declared path-qualified namespace column (same transformation as r95→r96), and no new relation semantics exist (single relation row; J17 is the only added row and is a timeline event; 10-type census unchanged; contract/tool changes are pointer-grammar only) — with one bounded prose observation: the mandated r96 repair removed the map's standalone relation-bound sentence, the bound surviving in the J11 anchor plus README/sources/scope-note.
