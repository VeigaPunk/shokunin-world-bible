# V01 — c1-before-after (round 95)

Seat: V01 `c1-before-after`. Scope: prove the BR-02 schema-drift blind spot on the
baseline tool, then prove the delivered tool closes it with a stable `schema_drift`
FINDING, and that no other current fixture trips `schema_drift`.

Baseline: r94 closure `fb118c4`. Working tree tool at seat start:
`corpus/tools/map_obligations.py` md5 `882eeebdeb2ac6ea05a8cdb1afff7ba3`, verified
identical (same md5) to `git show fb118c4:corpus/tools/map_obligations.py`.
Scratch (declared seat scratch): `.ufo/waves/round-95/seats/V01-scratch/`.

## Phase 1 — BEFORE (baseline tool): blind spot and isolating controls

Old tool copy: `.ufo/waves/round-95/seats/V01-scratch/map_obligations_OLD.py`
(691 lines, `git show fb118c4:corpus/tools/map_obligations.py`).

Builder `.ufo/waves/round-95/seats/V01-scratch/build_br02.py` produced three
independent copies (`br02-old`, `br02-new`, `br02-new-2`) of
`corpus/fixtures/r94-paired-crossing/`, each with exactly two edits:
1. `entities.json` entity index 4 (`chalk-stair`): key `claims` renamed to
   `assertions`, value content preserved;
2. map row `entities.json#/4/claims/0` (J10) removed.

`diff` vs the r94 source shows exactly two hunks:

```
55c55
<     "claims": [
---
>     "assertions": [
31d30
< | J10 | `entities.json#/4/claims/0` (`statement`, `source_id`) | `crossing-minute` | ...
```

All three copies byte-identical per file — entities sha256 `8c0f9fba…f6226`,
relations `c279254b…c4a6ff9`, timeline `f0209f90…60533c`, map `e4143f36…bacf896`;
builder printed `IDENTICAL=True (1 distinct digest sets across 3 copies)`.

Command + observed output (OLD tool, mutated cluster):

```
$ python3 .ufo/waves/round-95/seats/V01-scratch/map_obligations_OLD.py .ufo/waves/round-95/seats/V01-scratch/br02-old
OBLIGATIONS raw=13 mapped=13
RESULT PASS
exit=0
```

→ BR-02 reproduces exactly as claimed: silent PASS, exit 0, no finding.

Isolating controls (which half of the pair is silent):

```
$ .../map_obligations_OLD.py .../ctrl-rowonly        # J10 row removed, claims key intact
OBLIGATIONS raw=14 mapped=13
FINDING missing_obligation: entities.json#/4/claims/0 has no map row
RESULT FAIL
exit=1

$ .../map_obligations_OLD.py .../ctrl-renameonly     # claims key renamed, J10 row kept
OBLIGATIONS raw=13 mapped=14
FINDING phantom_obligation: entities.json#/4/claims/0 is not a raw source-attributed obligation
RESULT FAIL
exit=1
```

→ Neither edit alone is silent; only the pair yields exit 0, because the raw
obligation leaves the raw set while its map row leaves the map, leaving nothing to
compare. That is the exact class BR-02 names.

Baseline exits for the sweep set (OLD tool), saved `old-full-sweep.txt`:

```
r87-myth-cluster            exit=2 RESULT ERROR  (unsupported_map: table needs one JSON fact pointer and one source-ID column)
r88-m3-maya-cluster         exit=2 RESULT ERROR  (unsupported_map)
r89-inspiration-paraphrase  exit=2 RESULT ERROR  (unsupported_map)
r93-m2-kojiki-cluster       exit=0 RESULT PASS   (12/12)
r94-paired-crossing         exit=0 RESULT PASS   (14/14)
```

## Phase 2 — AFTER (delivered tool)

Delivery was watched live. The tool was written repeatedly 16:22:31–16:26:39; two
stable revisions were tested, both passing every check in this seat:

- intermediate: md5 `bcea56042588acfc444ac6629d6d7ce2` (sha256 `9224a684…7bb70`, 728 lines)
- **final (verdict revision): md5 `d31b8182953e9088a155f4ed2978af5b`,
  sha256 `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108`,
  809 lines, 33320 bytes, `git diff --numstat` = `130 12`** — unchanged from 16:26:39
  through 16:29:58 (re-verified after all runs).

The BR-02 output is byte-identical across the two revisions (`diff` empty), so the
verdict does not depend on which of the two landed revisions is taken.

**BR-02 mutation through the delivered tool** (`run_after.py`; outputs in
`V01-scratch/after/new-br02-run*.out`, intermediate-revision outputs preserved in
`V01-scratch/after-rev-bcea5604/`):

```
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-95/seats/V01-scratch/br02-new
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
FINDING schema_drift: entities.json#/4: 1 sourced-claim-shaped record(s) under unexpected key 'assertions'
RESULT FAIL
exit=1
```

Stability: three runs over three independent byte-identical copies (`br02-new` twice,
`br02-new-2` once) produced byte-identical stdout — md5
`9b9b1c7c907c769e1130b9cc21b5be62` for all three files, both `diff`s empty. The
FINDING ID `schema_drift` is stable, and the detail string is stable too (naming the
exact entity index and the unexpected key). Note the mutation is also reflected in the
inventory receipt (`13/14`, `MISMATCH`), but the decisive signal is the exit-1
`schema_drift` finding.

**Sweep through the delivered tool** (`after/sweep-*.out`):

| fixture | exit | full output |
|---|---:|---|
| r87-myth-cluster | 2 | `FINDING unsupported_map: pointer cells must contain one canonical inline-code pointer` / `RESULT ERROR` |
| r87-chain-unique-valid | 2 | `FINDING map_missing: expected exactly one conventional claim-to-excerpt map` / `RESULT ERROR` |
| r88-m3-maya-cluster | 0 | `OBLIGATIONS raw=10 mapped=10` / `INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12` / `RESULT PASS` |
| r89-inspiration-paraphrase | 2 | `FINDING unsupported_map: table needs one JSON fact pointer and one source-ID column` / `RESULT ERROR` |
| r93-m2-kojiki-cluster | 0 | `OBLIGATIONS raw=12 mapped=12` / `INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15` / `RESULT PASS` |
| r94-paired-crossing | 0 | `OBLIGATIONS raw=14 mapped=14` / `INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16` / `RESULT PASS` |
| r95-crossing-aftermath | 0 | `OBLIGATIONS raw=15 mapped=15` / `INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17` / `RESULT PASS` |

Notes: r87-myth-cluster and r89-inspiration-paraphrase stay exit 2 `unsupported_map`
(the message for r87 moved from the header check to the pointer check, but the code and
fail-closed behavior are unchanged); r87-chain-unique-valid has no map at all and stays
exit 2 `map_missing`; r93/r94 keep 12/12 and 14/14 PASS with no corpus modification.
r88's dialect now parses to `TOTAL-ROWS 12/12` PASS with zero corpus modification
(`git status --porcelain` shows no modification under `corpus/fixtures/r88-m3-maya-cluster/`).

**No stray schema_drift:** exhaustive sweep of all 169 fixture directories under
`corpus/fixtures/` through the delivered tool (run on both revisions, same result):

```
fixtures run: 169
exit distribution: {0: 4, 2: 165}
schema_drift fixtures: none
```

(4 PASS = r88, r93, r94, r95; the 165 exit-2 are pre-existing map_missing /
unsupported_map / malformed-input classes, none schema_drift.) The only cluster in this
round that produces `schema_drift` is the BR-02 mutation copy under the seat scratch.

**Adjacent observation (context for C1, not my verdict):** at 16:26 on the intermediate
revision `--self-test` failed with `FINDING self_test_contract: contract self-test cases
do not match the implemented cases` because the tool already implemented 22 cases while
P2's contract still listed 20. P2 landed the contract (md5 `d2a77aa09e5cd38d73d772bb11a5914e`,
22 cases) at 16:27; on the final revision:

```
$ python3 corpus/tools/map_obligations.py --self-test
... 22 SELF-TEST PASS lines, including:
SELF-TEST PASS map_missing exit=2 findings=['map_missing']
SELF-TEST PASS invalid_arguments exit=2 findings=['invalid_arguments']
RESULT PASS
exit=0
```

## Poll outcome

Target: P1's tool + report. Both landed (tool stable revision above; report
`.ufo/waves/round-95/seats/P1-tool-code.md`, 13759 bytes, present from 16:27:39).
No ABSENT artifact remains for this seat's targets.

## Bottom line

PASS — the BR-02 class reproduces as a silent exit-0 blind spot on the baseline tool
(with isolating controls showing only the key-rename + row-removal pair is silent), the
delivered revision (md5 `d31b8182…`) turns the identical mutation into exit 1
`schema_drift` with byte-identical output across three independent copies and two
delivered revisions, and no other current fixture (all 169 swept) trips `schema_drift`;
r87/r89 stay fail-closed exit 2, r88 now 12/12 PASS, r93 12/12 and r94 14/14 unchanged,
r95-crossing-aftermath 15/15 PASS.
