# V46 — cross-gates-r97 (round 97)

- Seat: V46 cross-gates-r97 (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`; all commands from the lane repo root with `python3`.
- Task as briefed: on a scratch copy with the tick-13 `depends_on` dropped, tabulate `check_bible` / `support_check` / `map_obligations` / `dependency_freeze` exits — freeze must catch it (BR-01 class on the new fixture), others must not; quote.
- Writes: this report plus `.ufo/waves/round-97/seats/V46-scratch/` (mutator, foreign copy, mirror root) only. No commits, no pushes, no network, no nested agents. Absolute paths used throughout; the seats dir realpath was verified as `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-97/seats` before writing.

## Revision pinned for every measurement (hashes identical before and after my runs)

```
b06275f3bbdeabaab615138b3004703fce701a786af882d3b732828b37722130  corpus/tools/dependency_freeze.py          (R3, matches R3's report)
27273be27d33ad864f06d656f28dca8eabc9d76f6ebe62583372a88c9e64e781  corpus/tools/dependency-freeze-contract.json (R3, matches)
86b529496214493f918836e908fe1c2e57c9561da06a088f03500b9a943a74a9  corpus/tools/map_obligations.py            (R1)
2142b9917694dbec7d2d3f925720bc5a03ca8c861789de3f9b68a6ddf1db2c41  corpus/tools/map-obligations-contract.json (R2, 25 cases)
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  corpus/fixtures/r97-crossing-acknowledgment/timeline.json
```

## 0. Poll-wait record

First inspection ~18:42: no r97 fixture, no producer reports. Fixture files landed 18:44:16–18:44:30; producer reports landed R1 18:48:43 (re-written 18:52:25), R2 18:49:31, R4 18:50:14, R5 18:51:25, R6 18:53:37, R3 18:56:23; the final dependency-freeze contract (16 self-test cases, mtime 18:55:14) was present before I ran anything. Every measurement below was taken after all six producer reports existed (first run ~18:59), against the hash-pinned revision above. No result comes from a mid-flight revision.

## 1. Scratch copy and the mutation

Mutator `.ufo/waves/round-97/seats/V46-scratch/mutate.py` mirrors the r96 self-test mechanics: `record["depends_on"] = [dep for dep in record["depends_on"] if dep != DEP]`.

```
$ python3 .ufo/waves/round-97/seats/V46-scratch/mutate.py corpus/fixtures/r97-crossing-acknowledgment \
    .ufo/waves/round-97/seats/V46-scratch/r97-depdropped acknowledgment-aru-records response-evin-salt-court
event=acknowledgment-aru-records before=['response-evin-salt-court'] after=[]
```

Surgical check — all nine non-timeline files byte-identical; the only diff is the tick-13 edge:

```
IDENTICAL entities.json / relations.json / contradictions.json / inspiration-note.md / source-excerpt.md /
          sources.json / fictional-excerpts.md / README.md / claim-excerpt-map.md
$ diff -u <pristine>/timeline.json <copy>/timeline.json
@@ -56,9 +56,7 @@
-    "depends_on": [
-      "response-evin-salt-court"
-    ],
+    "depends_on": [],
timeline.json sha: 73063a86… → 37a425b97af658d71b8dc8904f43fd75859905bac326489a71adb67004004eb1
```

The key stays present as `[]` — the faithful BR-01 class (edge dropped, event kept). `check_bible`'s schema requires the key present as a list but accepts an empty list (`check_bible.py:78`: `field not in row or type(row[field]) is not expected or (expected is str and not row[field].strip())`), so this mutation is invisible to schema validation; deleting the key instead would trip it (r96 V14 P1a: `required nonempty list`), which is a different class.

## 2. Cross-gate table — delivered contract (the literal seat ask)

All four gates on the same mutated bytes (`.ufo/.../V46-scratch/r97-depdropped`, foreign path), delivered revision:

| gate | exit | output class |
|---|---|---|
| `check_bible.py` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| `support_check.py` | 0 | `RESULT PASS` (`INVENTORY … 17/17; 2/2; 19/19`, `VALIDATED-ROWS 19/19`) |
| `map_obligations.py` | 0 | `OBLIGATIONS raw=17 mapped=17` … `RESULT PASS` |
| `dependency_freeze.py` | **2** | `FINDING UNPINNED-FIXTURE` — **not** a BR-01 catch |

Quotes:

```
$ python3 corpus/fixtures/check_bible.py .ufo/waves/round-97/seats/V46-scratch/r97-depdropped
CLEAN: schema, citations, relations, timeline; 0 violations                                   EXIT=0
$ python3 corpus/tools/support_check.py .ufo/waves/round-97/seats/V46-scratch/r97-depdropped
… RESULT PASS                                                                                 EXIT=0
$ python3 corpus/tools/map_obligations.py .ufo/waves/round-97/seats/V46-scratch/r97-depdropped
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                                                                   EXIT=0
$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-97/seats/V46-scratch/r97-depdropped
FINDING UNPINNED-FIXTURE: no pin for 'r97-depdropped' in corpus/tools/dependency-freeze-contract.json
(pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])
RESULT ERROR                                                                                  EXIT=2
```

Control on the **intact** delivered fixture, same contract — freeze is exit 2 there too, i.e. the exit is a pin-registration fact, not a mutation detection:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FINDING UNPINNED-FIXTURE: no pin for 'r97-crossing-acknowledgment' in corpus/tools/dependency-freeze-contract.json
(pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response'])
RESULT ERROR                                                                                  EXIT=2
```

## 3. Finding — the delivered contract does not pin the new fixture

`corpus/tools/dependency-freeze-contract.json` (`27273be2…`) pins exactly four fixtures; `r97-crossing-acknowledgment` is not among them (`r97 in delivered pins? False`). R3's report records this explicitly (residual note 2):

> "**`r97-crossing-acknowledgment` is not pinned** — the chain stays the four fixtures the claim declares (`--self-test`/chain receipts above). Running the tool on it gives `UNPINNED-FIXTURE` exit 2 by design. Pinning it is a candidate for r98 (it has one new `depends_on` edge the BR-01 class covers)."

Consequence for this seat's bar ("freeze must catch it — BR-01 class on the new fixture"): on the **delivered** revision freeze does not catch the tick-13 drop — it never evaluates the fixture (exit 2 `UNPINNED-FIXTURE` on intact and mutated bytes alike; no `REDUCTION-DETECTED`). The other three gates correctly stay green. The BR-01 catch is therefore demonstrated below as a capability under an explicit pin, in a scratch mirror, with the delivered tool/contract bytes.

## 4. BR-01 catch with the fixture pinned (scratch mirror, delivered tool bytes)

Mirror root `.ufo/waves/round-97/seats/V46-scratch/mirror/` holding byte-identical copies of the delivered tool + contract (sha checks above) and the fixture at its pinned repo-relative path `corpus/fixtures/r97-crossing-acknowledgment`. Pinning through the delivered guarded `--freeze` (in-mirror; the delivered contract is never written):

```
$ python3 <mirror>/corpus/tools/dependency_freeze.py --freeze <mirror>/corpus/fixtures/r97-crossing-acknowledgment
FROZEN r97-crossing-acknowledgment: events 6; dependency-edges 5; relations 1
DIGEST 3c922d20a01bbd3f7941ed64f5c8796a619699197ae89fb10fca317cf83abea6
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
RESULT PASS                                                                                   EXIT=0
$ python3 <mirror>/corpus/tools/dependency_freeze.py <mirror>/corpus/fixtures/r97-crossing-acknowledgment   # intact, separate run
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
RESULT PASS                                                                                   EXIT=0
```

Then the same tick-13 drop in the mirror copy (timeline sha `37a425b9…`, identical bytes to §2's copy):

```
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL                                                                                   EXIT=1
```

The other three gates on these same mutated mirror bytes stay green: `check_bible` `CLEAN … 0 violations` EXIT=0; `support_check` `RESULT PASS` EXIT=0; `map_obligations` `OBLIGATIONS raw=17 mapped=17` / `RESULT PASS` EXIT=0.

So the BR-01 class **does** cover the new fixture's new edge — the catch is exactly one integration-time pin away (`REDUCTION-DETECTED`, edge count `4/5`), and the mutation is invisible to every other delivered gate either way.

## 5. Write audit

Delivered artifact hashes re-checked after all runs: unchanged (six gate-file shas above; fixture timeline still `73063a86…`; contract still `27273be2…`, `r97 in delivered pins? False`). `git status --porcelain` shows only producer-owned modifications and the untracked round dirs; nothing under `corpus/` was written by this seat. My writes live under `.ufo/waves/round-97/seats/V46-scratch/` (`mutate.py`, `r97-depdropped/`, `mirror/`) plus this report.

## Bottom line

**FAIL** — against the delivered revision the seat's bar is not met: with the tick-13 `depends_on` dropped, `dependency_freeze` does not catch it as BR-01 (`FINDING UNPINNED-FIXTURE`, exit 2, on intact and mutated bytes alike — `r97-crossing-acknowledgment` is not in the frozen chain, which stays 4/4 per R3's report), while `check_bible`/`support_check`/`map_obligations` correctly stay green (exit 0); the BR-01 catch reproduces (`FINDING REDUCTION-DETECTED … lost depends_on ['response-evin-salt-court']`, exit 1) only once the fixture is pinned through the delivered guarded `--freeze` in a scratch mirror, with the other three gates still green on the same bytes.
