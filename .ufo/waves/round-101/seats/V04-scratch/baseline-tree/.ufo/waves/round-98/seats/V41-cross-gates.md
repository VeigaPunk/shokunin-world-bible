# V41 — cross-gates-r98 (round 98)

- Seat: V41 cross-gates-r98 (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r97 closure `9a3d648` (HEAD `dd4df1b`; wave tree uncommitted during the round). All commands from the lane repo root with `python3`.
- Task as briefed: on a scratch copy with the tick-14 `depends_on` edge dropped, tabulate all five gates — `dependency_freeze` must catch it (pinned now, C2), the others stay green (by design); quote.
- Five-gate set per the r96 V49 precedent (`round-96/seats/V49-gates-cross.md`): `check_bible`, `support_check`, `map_obligations`, `dependency_freeze`, `boundary_doc_check`.
- Writes: this report plus `.ufo/waves/round-98/seats/V41-scratch/` only (mutator, poll harness, foreign copy, mirror roots, transcripts). No commits, no pushes, no network, no nested agents. The seats dir realpath was verified as `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-98/seats` before writing; the report path was written absolutely.

## 0. Poll-wait record

18 tries at 20 s cadence (23:29:52 → 23:35:32 UTC), ALL-LANDED on try 18 (`.ufo/waves/round-98/seats/V41-scratch/poll.log`): all five producer reports present, `corpus/tools/dependency_freeze.py` + contract modified, and `r97-crossing-acknowledgment` + `r98-clerk-filing` both in the contract pins. Report landings (first seen at the 20 s poll, so known to within one cadence): S3 23:31:12, S4 23:32:12, S5 23:33:52, S2 23:34:52, S1 23:35:32. Every measurement below was taken after ALL-LANDED on the hash-pinned revision in §1; tool/contract hashes were re-checked stable over a 15 s interval before the run and re-checked unchanged after it. No result comes from a mid-flight revision (S1's tool was still being edited at tries 6–9; nothing was measured then).

## 1. Revision pinned for every measurement

```
03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b  corpus/tools/dependency_freeze.py
153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947  corpus/tools/dependency-freeze-contract.json
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py
ebb6a0843e67bfaa3118eda7fbf69bac124aca8f5b87cd0b9721b5e6346b0053  corpus/tools/boundary_doc_check.py
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  corpus/fixtures/r98-clerk-filing/timeline.json
```

The tool and contract shas are the delivered revision declared by the producer report (`S1-freeze-hygiene.md:9,11`: tool `03d04365…`, contract `153ebc5b…`); the other four gate files are unchanged from r97 delivery.

Pin state (delivered contract, read in the same run):

```
pins: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing']
r97 pinned: True
r98 pinned: True
r98 pin fixture path: corpus/fixtures/r98-clerk-filing
r98 pin counts: {'events': 7, 'dependency_edges': 6, 'relations': 1, 'entities': 6, 'sources': 7}
```

The r98 pin's recorded edge set includes the tick-14 edge (`clerk-filing-open: ['acknowledgment-aru-records']`, from the contract's `pins` object). Controls on the intact delivered bytes — all five gates green, and the frozen chain verifies 6/6:

```
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do echo "-- $f"; python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f; echo "EXIT=$?"; done
-- r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS
EXIT=0
-- r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS
EXIT=0
-- r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS
EXIT=0
-- r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS
EXIT=0
-- r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
RESULT PASS
EXIT=0
-- r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 59a0f4fa3d4a47e03649a54d1815c45ee1eef641b63a59ebe7210bc9d9b9b133
RESULT PASS
EXIT=0
```

(`59a0f4fa…` is exactly the r98 pin digest S1's report declares.) `python3 corpus/tools/dependency_freeze.py --self-test` → `SELF-TEST 17/17` / `RESULT PASS` / exit 0, with the persisted case `self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok` (C1a's pinned case) among the 17.

## 2. Mutation under test (BR-01 class, byte-minimal)

Mutator `.ufo/waves/round-98/seats/V41-scratch/mutate.py` mirrors the r96/r97 self-test mechanics: `row["depends_on"] = [dep for dep in row["depends_on"] if dep != DEP]` (key kept as `[]`).

```
$ python3 .ufo/waves/round-98/seats/V41-scratch/mutate.py corpus/fixtures/r98-clerk-filing \
    .ufo/waves/round-98/seats/V41-scratch/r98-depdropped clerk-filing-open acknowledgment-aru-records
event=clerk-filing-open before=['acknowledgment-aru-records'] after=[]
```

Surgical check — across the fixture's 10 files the only differing file is `timeline.json`:

```
$ diff -rq corpus/fixtures/r98-clerk-filing .ufo/…/V41-scratch/r98-depdropped
Files corpus/fixtures/r98-clerk-filing/timeline.json and …/r98-depdropped/timeline.json differ
$ diff -u corpus/fixtures/r98-clerk-filing/timeline.json …/r98-depdropped/timeline.json
@@ -67,9 +67,7 @@
     "tick": 14,
     "entity_id": "clerk-maren",
     "place_id": "chalk-stair",
-    "depends_on": [
-      "acknowledgment-aru-records"
-    ],
+    "depends_on": [],
```

`timeline.json` sha256: `eb24e084…` → `ddec7a072fa21919ca1faeae49f7ee7b7f1eae20bcd36653942eee58cceec34f`. The key stays present as `[]` — the faithful BR-01 class (edge dropped, event kept), which `check_bible`'s schema accepts (type `list`, `check_bible.py:30`).

## 3. Cross-gate tabulation — the literal seat ask

All five gates on the same mutated bytes. `check_bible` / `support_check` / `map_obligations` ran on the foreign copy (`…/V41-scratch/r98-depdropped`); `dependency_freeze` ran in a mirror root (`…/V41-scratch/mirror-r98/`) holding byte-identical copies of the delivered tool + contract (shas re-verified equal to §1) with the mutated fixture at the pin's recorded repo-relative path `corpus/fixtures/r98-clerk-filing`; `boundary_doc_check` is repo-level and takes no fixture input. The mutated `timeline.json` is byte-identical in the foreign and mirror copies (`ddec7a07…` both).

| gate | exit | output class | catches? |
|---|---|---|---|
| `check_bible.py` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` | No |
| `support_check.py` | 0 | `RESULT PASS` (`SOURCE-SUPPORT 20/20; … VALIDATED-ROWS 22/22`) | No |
| `map_obligations.py` | 0 | `OBLIGATIONS raw=20 mapped=20` … `RESULT PASS` | No |
| `dependency_freeze.py` | **1** | `FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']` (`dependency-edges 5/6`) | **YES** |
| `boundary_doc_check.py` (default) | 0 | `CERTIFIED (bounded: …)` | No (out of scope by construction) |

Quotes (full transcripts: `.ufo/waves/round-98/seats/V41-scratch/final-tabulation.txt`):

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-98/seats/V41-scratch/r98-depdropped
CLEAN: schema, citations, relations, timeline; 0 violations                                   EXIT=0
$ python3 corpus/tools/support_check.py .ufo/waves/round-98/seats/V41-scratch/r98-depdropped
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; … MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                                                   EXIT=0
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-98/seats/V41-scratch/r98-depdropped
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                                                   EXIT=0
$ python3 .ufo/waves/round-98/seats/V41-scratch/mirror-r98/corpus/tools/dependency_freeze.py \
    .ufo/waves/round-98/seats/V41-scratch/mirror-r98/corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL                                                                                   EXIT=1
$ python3 corpus/tools/boundary_doc_check.py
CHECK pinned inputs: PASS … CHECK document structure: PASS
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
                                                                                              EXIT=0
```

Mirror necessity, quoted: the delivered tool enforces path binding, so the same-named copy at a foreign path is refused rather than evaluated — the mirror is the only way to put the mutation in front of the delivered pin:

```
$ python3 corpus/tools/dependency_freeze.py .ufo/…/V41-scratch/mirror-r98/corpus/fixtures/r98-clerk-filing
FINDING PATH-MISMATCH: pin r98-clerk-filing names corpus/fixtures/r98-clerk-filing (resolves to …/lore-shokunin/corpus/fixtures/r98-clerk-filing); invoked fixture resolves to …/V41-scratch/mirror-r98/corpus/fixtures/r98-clerk-filing
RESULT ERROR                                                                                  EXIT=2
```

Controls on the intact delivered fixture: `check_bible` exit 0 CLEAN; `support_check` exit 0 `RESULT PASS` (identical receipt lines to the mutated run); `map_obligations` exit 0 `raw=20 mapped=20` / `RESULT PASS`; `dependency_freeze` exit 0 `… 6/6 … DIGEST 59a0f4fa…` / `RESULT PASS`; `boundary_doc_check` exit 0 `CERTIFIED`. So the exit-1 is attributable to the dropped edge alone, and the same fixture at the same bytes passes when intact.

## 4. Why the other four are blind (mechanism, quoted from delivered bytes)

- `check_bible.py:393-414` validates `depends_on` member *shape and properties* — self dependency, repeated member, unknown/ambiguous event ID, tick inversion — and never holds an expected edge set. Removing one well-formed member trips none of those checks; the empty list still satisfies the schema (`check_bible.py:30`).
- `map_obligations.py:485-494` compares the raw obligation **pointer set** and per-pointer `source_id` only (`duplicate_mapping` / `phantom_obligation` / `source_id_mismatch` / `missing_obligation`); field *values* are never compared, so `depends_on` content is invisible.
- `support_check.py` validates map-declared rows, anchors, spans, and modes against the excerpt text; the mutation touches no anchor text or span (J14/J20 anchors and spans byte-identical between intact and mutated runs; receipts differ only in the invoked path line).
- `boundary_doc_check.py` takes no fixture input — `--help` lists only `--doc`, `--checker`, `--self-test` — so its repo-level default is identical before and after any fixture mutation.

## 5. Write audit

Post-run hashes unchanged: tool `03d04365…`, contract `153ebc5b…`, r98 `timeline.json` `eb24e084…` (re-checked after every run). `git status --porcelain` shows only producer-owned modifications (`LOG.md`, r95 map repair, r95/r96 scope notes, tools README, freeze tool + contract) and untracked round paths (`.ufo/waves/round-98/`, `corpus/fixtures/r98-clerk-filing/`, `corpus/knowledge/r98-clerk-scope-note.md`). Nothing under `corpus/` was written by this seat; no stray landed outside my scratch (the root-level `v05-self-test-scratch/` belongs to V05, is gitignored `*-self-test-*/`, and predates this seat's runs). My writes live only under `.ufo/waves/round-98/seats/V41-scratch/` (`mutate.py`, `poll.sh`, `poll.log`, `run.sh`, `final-tabulation.txt`, `r98-depdropped/`, `mirror-r98/`, plus harness-validation dirs `dryrun-r98-depdropped/` and `mirror-dryrun/`) plus this report.

## Scope of this evidence

What is shown: at the revision pinned by sha256 in §1 (tool/contract equal to S1's declared delivered bytes; all five producer reports landed before measurement) the tick-14 `depends_on` drop is caught by `dependency_freeze` alone (`FINDING REDUCTION-DETECTED`, `dependency-edges 5/6`, exit 1) and the other four gates correctly stay green; the same fixture intact passes all five; the chain is pinned 6/6 and the tool self-test is 17/17. What is not shown: that the frozen inventories are semantically correct beyond the pin, that chronology/entailment/canon claims are true (the tool's own scope line disclaims this), or the other seats' C1/C2/C3 claims beyond the pin/chain/self-test observations quoted here.

## Bottom line

**PASS** — with the tick-14 edge dropped (`clerk-filing-open.depends_on` `["acknowledgment-aru-records"]` → `[]`, byte-minimal), `dependency_freeze` catches it on the delivered revision (`FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']`, `dependency-edges 5/6`, exit 1) now that the C2 re-freeze pins `r98-clerk-filing` (chain 6/6, r98 intact `RESULT PASS` digest `59a0f4fa…`), while `check_bible` / `support_check` / `map_obligations` / `boundary_doc_check` all exit 0 on the same mutated bytes exactly as designed (mechanisms quoted).
