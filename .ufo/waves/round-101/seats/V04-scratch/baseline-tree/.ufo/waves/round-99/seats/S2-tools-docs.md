# S2 tools-docs — round-99 seat report

Seat: S2 (tools-docs), leaf, single-wave r99 re-dispatch. No nested agents, no commits, no pushes, no network.
Owned bytes: `corpus/tools/README.md` (append only) and the `dependency_freeze` row in `SKILL.md` (self-test count, pinned-values path, scope). Plus this report and scratch under `.ufo/waves/round-99/seats/S2-scratch/`.
Baseline: r98 closure `4265df5`. HEAD at dispatch `337f0fa` (blocked-attempt note; those two tool files were identical to `4265df5` before S1 wrote). Wave tree uncommitted.

## Poll

S1 artifacts and `S1-full-file-pins.md` were both required. 40 tries, 20 s apart, from `2026-10-17T22:00:49-03:00`.

Try 1 (`22:00:49`): `dependency_freeze.py` mtime `20:31:49` size 26644 (baseline), contract mtime `20:33:36` size 19291, no S1 report.
Try 4 (`22:01:49`): tool size moved to 27338. Try 12 (`22:04:29`): contract size 21007. Try 25 (`22:08:49`): contract size 25987 (mtime `22:08:46`). Tool settled at size 29104 mtime `22:07:33`, then a later message-string edit (mtime `22:38:11`, size 29110, sha `fb9bb9ff…`).
Try 40 (`22:13:49`): still no `S1*.md`. Log line: `POLL_ABSENT`.

Stall-escape (recorded, not fatal): the tool and contract were on disk and stable, and leaving the r98 sentence "BR-01's markdown/prose half remains open" would have been false on those bytes. Documented the delivered files, not the declaration alone. `S1-full-file-pins.md` appeared by the `22:53:25` recheck, after the first doc write. Read it. It agrees on schema 2, the ten files, self-test 18/18, the six digests, and the unpinned `symbolism-clause-map.md`. Its support_check contradiction is the same class I then measured on the r95 scratch copy (below) and added to the addendum.

## Deliverable

```
$ git diff --stat -- SKILL.md corpus/tools/README.md
 SKILL.md               |  6 ++---
 corpus/tools/README.md | 73 ++++++++++++++++++++++++++++++++++++++++++++++++++
 2 files changed, 76 insertions(+), 3 deletions(-)
```

README is a pure append (Round-99 addendum). The three SKILL deletions are the replaced freeze-row bullets (self-test, pinned-values path, scope). No other SKILL row touched. Did not write `dependency_freeze.py` or the contract.

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json corpus/tools/README.md SKILL.md
fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
837a7f5dfe913047530c7f92f3dd6b3df1b1a83c77ede12ba0c349cc134a049c  corpus/tools/README.md
e0bcb61ab909146e34773dd56219cb1631070c1700a2481f8ad1181f3d864443  SKILL.md
```

Tool and contract hashes were unchanged across the doc edits (`live_contract` still `8c2561b0…` after scratch probes). No commit.

## Claim verification

Cwd for live commands: `/home/vgpnk/Projects/shokunin/lore-shokunin`. Quoted outputs are from these runs, not from S1's report.

### Self-test 18

```
$ python3 corpus/tools/dependency_freeze.py --self-test
CASE clean: exit=0 expected=0 findings=[] ok
CASE reduction_edge_drop: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE addition_edge_phantom: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE event_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE event_endpoint_change: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_endpoint_flip: exit=1 expected=1 findings=['ENDPOINT-CHANGE'] ok
CASE relation_removed: exit=1 expected=1 findings=['REDUCTION-DETECTED'] ok
CASE relation_added: exit=1 expected=1 findings=['ADDITION-DETECTED'] ok
CASE digest_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
CASE malformed_json: exit=2 expected=2 findings=['MALFORMED-JSON'] ok
CASE missing_timeline: exit=2 expected=2 findings=['FILE-MISSING'] ok
CASE unpinned_fixture: exit=2 expected=2 findings=['UNPINNED-FIXTURE'] ok
CASE missing_fixture: exit=2 expected=2 findings=['FIXTURE-MISSING'] ok
CASE invalid_arguments: exit=2 expected=2 findings=['INVALID-ARGUMENTS'] ok
CASE scope_refused: exit=2 expected=2 findings=['SCOPE-REFUSED'] ok
CASE path_mismatch: exit=2 expected=2 findings=['PATH-MISMATCH'] ok
CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
CASE markdown_tamper: exit=2 expected=2 findings=['DIGEST-MISMATCH'] ok
SELF-TEST 18/18
RESULT PASS
```

exit 0. Re-run after the README/SKILL edits: same `SELF-TEST 18/18` / `RESULT PASS` / exit 0.

### Chain 6/6

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
         r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
  python3 corpus/tools/dependency_freeze.py "corpus/fixtures/$f"; echo "$f exit=$?"
done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
r88-m3-maya-cluster exit=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
r94-paired-crossing exit=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
r95-crossing-aftermath exit=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
r96-crossing-response exit=0
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
r97-crossing-acknowledgment exit=0
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
r98-clerk-filing exit=0
```

Compared each pin's five JSON file digests to `git show 4265df5:corpus/tools/dependency-freeze-contract.json`: `json_digests_unchanged True` for all six. Each delivered pin has `payload_schema_version` 2 and 10 files. Contract `schema_version` 2, `payload_schema_version` 2, `revision` `337f0fa52b02626b7687eedbb2d99fab30446fe4`. Did not re-run `--freeze` on the delivered contract (it rewrites the pin file). A scratch copy of the delivered tool+contract, `--freeze corpus/fixtures/r95-crossing-aftermath`, printed `FROZEN` / `DIGEST 97cffd7bfe6e0c92…` / `RESULT PASS`, exit 0, and left the delivered contract hash unchanged.

### Prose-edit detectability, not semantics proof

Scratch mirrors under `S2-scratch/before-r95` (tool+contract from `git show 4265df5:…`) and `S2-scratch/after-r95` (delivered tool+contract). Both hold a copy of `corpus/fixtures/r95-crossing-aftermath`. Tamper: removed the first `depends on` from `fictional-excerpts.md`. Live fixtures not edited.

Before, cwd `S2-scratch/before-r95`:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
before_exit=0
```

After, cwd `S2-scratch/after-r95`, re-run after the doc edit (scratch tool sha `fb9bb9ff…`, same as delivered):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
FINDING DIGEST-MISMATCH: content digest 892d17d3a9a91aab99f1da6aaac66e3854d286dcba9a2178e3a0b8b034d011b8 != pin 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710; changed: fictional-excerpts.md (sha256 0ef6734ae52d28656e75869d942d6b1e8e324b116977a2811b3b36dc0880b282 -> 4b13096081476ac2d92694ee26830d981c5095e786f06b64d67b34f9d4ce37fd); pinned-file bytes changed outside the semantic inventory
RESULT ERROR
after_exit=2
```

Census: trailing newline on each of the ten pinned files, each in its own scratch copy of r95, exit 2 `DIGEST-MISMATCH` naming that file only (`entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`).

Extra-file bound, scratch copy of r88: appending a marker to `symbolism-clause-map.md` still printed `RESULT PASS`, digest `acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae`, exit 0. That file is outside the declared ten.

Schema/missing-file probes, scratch only, delivered contract hash unchanged:

```
FINDING CONTRACT-INVALID: pin r95-crossing-aftermath payload_schema_version 1 != 2 (full-file pin of 10 files)
RESULT ERROR
exit 2
```

```
FINDING FILE-MISSING: --freeze refuses corpus/fixtures/r95-crossing-aftermath: pinned file(s) missing: inspiration-note.md
RESULT ERROR
exit 2
```

### Contradiction with "invisible to every gate"

The same r95 wording removal is an anchored sentence. From the repository root, unpiped:

```
$ python3 corpus/tools/support_check.py .ufo/waves/round-99/seats/S2-scratch/before-r95/corpus/fixtures/r95-crossing-aftermath
SOURCE-SUPPORT 14/15; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 17/17; VALIDATED-ROWS 16/17
FAIL: J14: source-support anchor missing
RESULT FAIL
support_exit=1
```

```
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-99/seats/S2-scratch/before-r95/corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
map_exit=0
```

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-99/seats/S2-scratch/before-r95/corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
bible_exit=0
```

So the r98 freeze gate missed the edit; `support_check` did not. The delivered freeze gate names the file. That is edit detection, not a proof that the remaining prose still states the dependency. S1 reported the same split on an r94 copy (J14). The addendum states this bound. Do not read the r99 close as "every prior gate was blind."

## Docs now say

README Round-99 addendum (2026-10-17): ten-file payload, `schema_version` 2 / `payload_schema_version` 2, dated supersession of the r97/r98 "five JSON tables only / prose half remains open" sentences and of the 17-case count, Markdown-tamper detectability with the not-semantics-provable bound, self-test 18, chain 6/6, extra-file bound, support_check J14 bound. SKILL freeze row: pinned-values path is the ten-file schema-2 payload; scope is prose-edit detectability, not dependency-semantics proof, with the r88 extra file unpinned; self-test count 18 so the same row does not still say 17.

PASS — tools README r99 addendum and SKILL.md freeze row match observed CLI (self-test 18/18 exit 0, chain 6/6 exit 0, prose edit exit 2 DIGEST-MISMATCH naming fictional-excerpts.md); S1 report absent through the 40-try poll, stall-escape recorded, then reconciled.
