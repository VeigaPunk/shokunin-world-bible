# V56 — crosscheck-depth (round 96)

Seat: V56 `verdict-crosscheck-depth`. Scope per seat spec: **independently derive the
DEPTH verdict from evidence only** (own runs; no reliance on other seats' summaries or
plans), then **compare with V32** (`verdict-depth`). Baseline r95 closure `dcb2d92`;
lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` for every command below; all
commands run from there with `python3`. Writes: this report plus
`.ufo/waves/round-96/seats/V56-scratch/` (`census_v56.py`, `rowcmp.py`,
`r96-freeze.sha256`, `probe/`). No commits, no pushes, no network, no nested agents, no
corpus writes.

Method note: my verdict was derived **before** reading V32's report (poll cadence below);
the comparison in §5 was made against the already-formed verdict.

## 1. Poll record (producer artifacts)

- 17:38 fixture dir first sighted (8/10 files, Q4 mid-write; `sources.json`/`timeline.json`
  at the pre-correction seam, rewritten by Q4 at ~17:40:16 — my first read at ~17:38–39
  caught the intermediate).
- 17:41–17:43 Q5's `README.md` transiently appeared then vanished mid-rewrite;
  `claim-excerpt-map.md` + `README.md` landed 17:43. Q4 report 17:42; Q5 report ~17:46;
  Q6 note + report ~17:45–46.
- All verification below ran only after the relevant producer report existed (Q4 report
  for the 8 tables, Q5 report for the 2 docs). Nothing verified from a plan; nothing
  ABSENT in my scope.
- V32's report landed ~17:47, after my full battery and verdict formulation.
- Tool-revision flux: `map_obligations.py` moved during the round; my samples are pinned
  below. Q2's contract was still at the 22-case revision at report time.

## 2. Frozen revision (my own capture, re-verified 10/10 just before this report)

```
$ sha256sum -c .ufo/waves/round-96/seats/V56-scratch/r96-freeze.sha256
claim-excerpt-map.md: OK   contradictions.json: OK   entities.json: OK
fictional-excerpts.md: OK  inspiration-note.md: OK   README.md: OK
relations.json: OK         source-excerpt.md: OK     sources.json: OK
timeline.json: OK          → 10/10 OK
```

Key hashes: `sources.json 9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d`,
`timeline.json ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9`,
`fictional-excerpts.md 06b11bec…`, map `5093d72e…`, `README.md ff52ced4…` — equal to
Q4's/Q5's declared delivered hashes (not the 17:38 intermediate).

Tool revisions at my receipts:

```
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c  corpus/tools/support_check.py
c2c284c0118cf66bed019c43dde87caabcdce8ccda957a82230d7c5b35d029da  corpus/tools/map_obligations.py   (battery run)
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py   (later re-run)
8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db  corpus/tools/map-obligations-contract.json  (still 22-case revision)
```

## 3. Independent evidence (my own runs)

### 3.1 Gates on the delivered r96 fixture

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0

$ python3 corpus/tools/support_check.py corpus/fixtures/r96-crossing-response
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
… PASS J16: source-support; mode=verbatim; anchor=found; 37:> Tick 12: I was at Salt Court through the same agreed bell.
SOURCE-SUPPORT 16/16; EDITORIAL-ANCHORS 2/2; MODES 18/18; VALIDATED-ROWS 18/18
RESULT PASS
exit=0

$ python3 corpus/tools/map_obligations.py corpus/fixtures/r96-crossing-response   # at c2c284c0 and again at 2b0ba815
OBLIGATIONS raw=16 mapped=16
INVENTORY JSON-FACTS 16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18
RESULT PASS
exit=0
```

Both gates fail closed with the map missing (observed earlier while Q5 was pending:
`FINDING map_missing … RESULT ERROR exit=2` / `FAIL: claim-to-excerpt map not found
RESULT ERROR exit=2`) — no false green.

### 3.2 Preservation of the r95 continuation

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp -s r95-crossing-aftermath/$f r96-crossing-response/$f && echo BYTE-IDENTICAL: $f || echo DIFFERS: $f; done
BYTE-IDENTICAL: entities.json / relations.json / contradictions.json / inspiration-note.md / source-excerpt.md

$ python3 (my own check)
sources.json r95 len 4 r96 len 5 prefix parsed-equal: True
timeline.json r95 len 4 r96 len 5 prefix parsed-equal: True
sources.json core byte-prefix-equal: True   (1225 -> 1741 B)
timeline.json core byte-prefix-equal: True  (1254 -> 1677 B)
fictional-excerpts.md core byte-prefix-equal: True (1845 -> 2588 B; diff on 33-line windows: 31a32,33 only)
```

Counts: entities 5 / relations 1 / timeline 5 / sources 5 / contradictions 0. New records
exactly as declared: `response-evin-salt-court` (tick 12, `evin`, `salt-court`,
`depends_on ["aftermath-missing-evin"]`, `evin-response-note`) and source
`evin-response-note` (fictional first-person note).

### 3.3 Map-row inheritance (my own column-level parse, `V56-scratch/rowcmp.py`)

- J01–J15 present in both maps; the **only differing cell in every row is index 2, the
  path-qualification column** (`r95-crossing-aftermath:…` → `r96-crossing-response:…`);
  pointer, source ID, span, mode, anchor cells all identical.
- S01/S02 editorial rows: **zero differing cells**.
- Exactly one added row: J16 (`timeline.json#/4`, span 33-42, anchor
  `Tick 12: I was at Salt Court through the same agreed bell.`).

### 3.4 Census — fresh implementation (git-archive materialization + SHA-256), baseline dcb2d92

```
$ python3 .ufo/waves/round-96/seats/V56-scratch/census_v56.py dcb2d92
{ "baseline_top_dirs": 169, "work_top_dirs": 170, "baseline_files": 1000, "work_files": 1010,
  "modified": [], "deleted": [], "new": [10 files, all under r96-crossing-response/],
  "new_top_dirs": ["r96-crossing-response"], "verdict": "PASS" }
```

169→170 confirmed; zero inherited modifications/deletions; r95 fixture byte-untouched.

### 3.5 Semantic bounds (hand review + greps)

- `contradictions.json` = `[]` (3 bytes on disk: `[]\n`; content `[]`).
- Every occurrence of accusation/winner/breach/duty/alliance/perpetual is inside a
  negating or scoping clause; no unscoped mention in any of the 10 files.
- Note text (`fictional-excerpts.md:37-40`): "Tick 12: I was at Salt Court through the
  same agreed bell. / I make no accusation against Aru. / I select no winner between our
  two accounts. / Both accounts stand unresolved."
- "Same occasion" is record-bounded: "the same agreed bell" plus the editorial
  `depends_on` edge to the tick-11 report; no external chronology asserted.

### 3.6 Blind-spot replay (my own scratch copy; V14 P1b / V32 bound 5 crosscheck)

```
$ cp -r corpus/fixtures/r96-crossing-response .ufo/waves/round-96/seats/V56-scratch/probe/
$ python3  # timeline[4].depends_on -> []
$ python3 corpus/fixtures/check_bible.py …/probe/r96-crossing-response
CLEAN: schema, citations, relations, timeline; 0 violations      # exit=0
$ python3 corpus/tools/map_obligations.py …/probe/r96-crossing-response
OBLIGATIONS raw=16 mapped=16 … RESULT PASS                        # exit=0
$ python3 corpus/tools/dependency_freeze.py …/probe/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 3/4; relations 1/1
FINDING REDUCTION-DETECTED: event response-evin-salt-court lost depends_on ['aftermath-missing-evin']
RESULT FAIL                                                       # exit=1
```

The emptied-dependency blind spot is real for the pre-existing gates and closed by the
C3 gate on the same copy.

### 3.7 Novelty bound (V32's §5 claim, independently reproduced)

Scan of `corpus/fixtures/*/sources.json` for sources whose `kind` contains
"first-person": **23 fixtures have ≥2 such sources; 22 carry a non-empty
`contradictions.json`; the only empty ledger among them is `r96-crossing-response`.**

### 3.8 Environment

`df -i /tmp` → `1048576 1048576 0 100%` — inode exhaustion confirmed (V32's §8 note).

## 4. Independent DEPTH verdict

**DEPTH — IMPROVED (bounded).** Before (r95): 5 entities / 1 relation / 4 events /
4 sources, 15 map obligations, one first-person account (Aru's tick-11 report). After
(r96): 5/1/5, 5 sources, 16 obligations (15 inherited rows unchanged modulo the declared
namespace re-qualification + new row J16), `check_bible` CLEAN exit 0, `map_obligations`
16/16 PASS exit 0, `support_check` 18/18 PASS exit 0, census 169→170 with zero inherited
modifications. The added content is the second participant's own account of the same
agreed-bell occasion with the unresolved status asserted in-record (no accusation, no
winner, no contradiction asserted; empty ledger). This is a real, measurable depth
increment over r95's single-account state, and no harm is visible in my scope.

Named bounds: authored fixture (not external evidence); gates validate
structure/lexical anchors, not testimony truth; "unresolved" is a prose assertion, not a
gate-enforced property; the two accounts sit at different actors/places (no ledger row);
the tick-12→tick-11 edge is visible to the new C3 gate but not to `check_bible`.

## 5. Comparison with V32 (`verdict-depth`)

Agreements (my independent runs vs V32's report):

| Item | V32 | V56 (independent) |
|---|---|---|
| Verdict | improved (bounded) | improved (bounded) — same |
| Frozen revision | 10/10 hashes; `ea0225f9…`/`9f973f63…` | 10/10 `sha256sum -c` OK; same hashes |
| Counts | 5/1/5/5/0 | 5/1/5/5/0 |
| Gates | CLEAN / 16/16 PASS / 18/18 PASS | identical receipts (map tool at 2 extra revisions) |
| Preservation | 5 copies identical; parsed prefixes; excerpt 1845 B prefix | identical results (cmp + my prefix script) |
| Map rows | 17 inherited rows, zero cell diffs modulo namespace; +J16 | J01–J15 differ only at namespace cell; S01/S02 zero diffs; +J16 |
| Census | 169→170, zero inherited changes | 169→170, modified=[] deleted=[] (git-archive SHA-256) |
| Novelty | 23 multi-note fixtures, 22 non-empty ledgers, r96 first empty | reproduced exactly (23/22/1) |
| Blind spot | emptied `depends_on` stays CLEAN (V14 P1b) | replayed: check_bible 0 + map_obligations 0; C3 gate exit 1 REDUCTION-DETECTED |
| V15 §5 stale note | flagged | independently found (final bytes `},\n  {`; `grep -n '^\s*,$'` rc=1) |
| `/tmp` inodes | 100% exhausted | `df -i` 0 free, 100% — confirmed |

Discrepancies found (all trivial, none verdict-affecting):

1. V32 §5 writes `contradictions.json` = "`[]` (2 B, byte-identical to r95)". On disk it
   is **3 bytes** (`[]\n`; `ls -la` = 3; content `[]`). Cosmetic.
2. V32 §6 lists V11 as ABSENT at 17:47; V11's report has since landed (PASS — "all 16 JSON
   anchors (J01–J16) + 2 editorial anchors resolve in-span … zero drift"). Timing only.
3. My tool samples extend V32's revision table (`d1c239cc…6634e176` → plus `c2c284c0`,
   `2b0ba815`): r96 gives 16/16 PASS at both; no contradiction with V32.

No evidence found that contradicts V32's verdict, bounds, or evidence; my derivation is a
corroboration, not a divergence.

## 6. Limits of this crosscheck

Same-lane replica review on the delivered bytes; structural/lexical plus hand clause
analysis. Not source authentication, canon truth, rights, or permission review. I did not
run `map_obligations --self-test` (C1's axis; its scratch prefix lands in the lane root —
BR-05 — and I avoid polluting shared paths). C1/C3 verdicts are other seats' remit.

## Bottom line

**PASS — DEPTH verdict independently derived as improved (bounded), identical to V32's** —
on the frozen 10-file revision, gates are green (CLEAN / 16/16 / 18/18), preservation and
census hold (169→170, zero inherited changes), the novelty and blind-spot bounds replay,
and the only differences from V32 are two trivial items (3 B vs "2 B" for
`contradictions.json`; V11 timing) that do not affect the verdict.
