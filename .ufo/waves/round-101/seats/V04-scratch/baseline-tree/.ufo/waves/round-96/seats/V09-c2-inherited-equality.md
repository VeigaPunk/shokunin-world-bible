# V09 — c2-inherited-equality: r96 inherited rows vs r95 (parsed-value + byte checks)

Seat: V09, round 96, lore-shokunin lane. Scope: parsed-value equality (key-order
sensitive) of every inherited row in `corpus/fixtures/r96-crossing-response/`
against `corpus/fixtures/r95-crossing-aftermath/` — entities (5), relations (1),
`timeline[:4]`, `sources[:4]`, contradictions (0) — plus (a) r95 dir byte-untouched
vs baseline `dcb2d92` and (b) `cmp` byte-prefix claims for `fictional-excerpts.md`
and `source-excerpt.md`.

All commands run from `/home/vgpnk/Projects/shokunin/lore-shokunin`. Scratch:
`.ufo/waves/round-96/seats/V09-c2-inherited-equality.scratch/` (comparator,
controls, mutation copies). No writes outside my report + scratch.

## Poll record (protocol)

Q4 target absent at 17:38; poll loop (20 s cadence) found the producer report
`.ufo/waves/round-96/seats/Q4-fixture-json.md` after 9 tries (written 17:42).
All 8 Q4-owned files existed from 17:38/17:40 onward. Verdict taken only after the
producer report landed; the delivered hashes it declares match my own freeze
measurement byte-for-byte (no post-report drift):

```
$ sha256sum -c .../V09-c2-inherited-equality.scratch/r96-snapshot-1.sha256
corpus/fixtures/r96-crossing-response/{contradictions,entities,fictional-excerpts,
inspiration-note,relations,source-excerpt,sources,timeline}: OK   (8/8)
```

Frozen r96 hashes used for every check below (`r96-final-freeze.sha256`):

| file | sha256 |
|---|---|
| entities.json | `026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b` |
| relations.json | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` |
| contradictions.json | `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570` |
| sources.json | `9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d` |
| timeline.json | `ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9` |
| fictional-excerpts.md | `06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3` |
| inspiration-note.md | `58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37` |
| source-excerpt.md | `b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd` |

Observed motion during my window (reported, not a defect): my 17:39 inventory saw
`sources.json` 1742 B / `timeline.json` 1678 B; both were rewritten at 17:40:16
(1741 B / 1677 B), which Q4's report documents as its mid-seat comma-placement
correction ("Mid-seat correction"). **Every result below is against the corrected,
frozen bytes** (my first equality run on the intermediate bytes also passed; the
run on the frozen bytes is the evidence).

## A. Parsed-value equality, key-order sensitive — PASS

Method: `json.load(..., object_pairs_hook=list)` preserves document key order;
rows are compared as order-preserving canonical text (not `dict.__eq__`, which is
order-insensitive), paired by stable key (`entities.id`, `relations.from`,
`timeline.id`, `sources.id`).

```
$ python3 .ufo/waves/round-96/seats/V09-c2-inherited-equality.scratch/compare_inherited.py
== entities: r95 n=5 r96 n=5
== relations: r95 n=1 r96 n=1
== timeline: r95 n=4 r96 n=5
== sources: r95 n=4 r96 n=5
== contradictions: r95 n=0 r96 n=0
...
== FAILURES: 0 ==
VERDICT: PASS
```

Per-row results (all `ORDER-SENSITIVE EQUAL`, and also plain `dict`-equal):

- entities: `aru`, `evin`, `quiet-rise`, `salt-court`, `chalk-stair` — 5/5 equal
- relations: `aru -> evin` (`agreed_co_stewardship_for_this_crossing`) — 1/1 equal
- timeline[:4]: `aru-ninth-bell`, `evin-ninth-bell`, `paired-crossing-decision`,
  `aftermath-missing-evin` — 4/4 equal (including nested `depends_on` arrays)
- sources[:4]: `veil-verse`, `paired-clock`, `crossing-minute`, `aru-aftermath-note`
  — 4/4 equal
- contradictions: `[] == []` — equal

Order/placement: inherited rows are an exact **index-prefix** in all four tables
(`entities order`, `relations order`, `timeline order`, `sources order` all
"inherited rows are an exact index-prefix (new rows appended)"). New rows sit at
the tail: `timeline[4] = response-evin-salt-court`, `sources[4] = evin-response-note`.
No duplicate keys; no inherited key dropped or added (order-sensitive equality
covers key set, key order, and values recursively).

## B. Falsifiability controls — PASS (a comparator that cannot fail is not evidence)

Synthetic control (`control_comparator.py`, mutating in-memory copies):

```
identical                detected-as-equal=True  expected=True  OK
key-order-only change    detected-as-equal=False expected=False OK
value change             detected-as-equal=False expected=False OK
extra key                detected-as-equal=False expected=False OK
dropped key              detected-as-equal=False expected=False OK
nested key-order change  detected-as-equal=False expected=False OK
CONTROL: PASS
```

Positive control on the **delivered fixture** (`mutation_control.py`; copies in
scratch, comparator re-pointed at the copy):

```
CONTROL 0: unmutated delivered fixture      exit=0 VERDICT: PASS
MUTATION entities-key-order                 exit=1 VERDICT: FAIL
    FAIL entities[id=aru]: ORDER-SENSITIVE DIFF but order-INSENSITIVE equal
         -> key-order-only drift; first divergence at char 2
MUTATION timeline-value                     exit=1 VERDICT: FAIL
    FAIL timeline[id=aftermath-missing-evin]: ORDER-SENSITIVE DIFF and value differs
MUTATION sources-drop-row                   exit=1 VERDICT: FAIL
    FAIL sources[id=crossing-minute]: MISSING in r96
CONTROL: PASS (clean exit 0; each mutation exit 1)
```

So the "key-order sensitive" claim is load-bearing: a key-order-only change in an
inherited r96 row is caught, and the delivered fixture is not in that state.

## C. r95 dir byte-untouched vs `dcb2d92` — PASS

```
$ git diff dcb2d92 -- corpus/fixtures/r95-crossing-aftermath/     -> (empty)
$ git diff dcb2d92 --stat -- corpus/fixtures/r95-crossing-aftermath/ -> (no files)
$ git status --porcelain --untracked-files=all -- corpus/fixtures/r95-crossing-aftermath/ -> (empty)
$ git ls-files corpus/fixtures/r95-crossing-aftermath/ | wc -l   -> 10
$ find corpus/fixtures/r95-crossing-aftermath/ -type f | wc -l   -> 10
```

Stronger per-file check — working-tree sha256 vs the `dcb2d92` blob, all 10 files:

```
OK corpus/fixtures/r95-crossing-aftermath/{README,claim-excerpt-map,contradictions,
entities,fictional-excerpts,inspiration-note,relations,source-excerpt,sources,timeline}
```

and the 10 hashes I captured at 17:38 re-verify at freeze
(`sha256sum -c r95-baseline.sha256` -> 10/10 OK). No untracked file appeared inside
the r95 dir, and no file disappeared (10 tracked = 10 on disk).

## D. `cmp` byte-prefix / byte-identity claims — PASS

```
fictional-excerpts.md: r95 1845 B is a byte prefix of r96 2588 B   (cmp -n 1845 -> 0)
                       full cmp differs (append-only; no `-` line in diff -u)
source-excerpt.md:     BYTE-IDENTICAL (640 B)                       (cmp -> 0)
inspiration-note.md:   BYTE-IDENTICAL (1956 B)   [Q4-declared byte copy; bonus]
sources.json:   inherited region byte-identical — r95 1225 B minus trailing 6 B
                (`  }\n]\n`) is a byte prefix of r96 1741 B
timeline.json:  inherited region byte-identical — r95 1254 B minus trailing 6 B
                is a byte prefix of r96 1677 B
```

`diff -u` of both grown JSON tables shows a pure insertion (zero `-` lines; the
only added text is `,\n  {\n … \n  }` plus the new object). Appended excerpt tail
begins `\n## Round 96 response note (2026-10-17)`; the r95 section is byte-preserved
in place. The 5 declared byte copies are sha256-identical to r95 (section A table
hashes match r95's `026af0bc…`, `c279254b…`, `37517e5f…`, `58f5390e…`, `b5edc2fd…`).

## E. Secondary observations (context, outside this seat's verdict scope)

- Referential integrity of the delivered r96 tables: **no unresolved references**
  (every `entity_id`/`place_id`/`source_id`/`depends_on`/relation endpoint/claim
  source resolves). Counts `5/1/5/5/0`; new event `depends_on
  ["aftermath-missing-evin"]` resolves and tick 12 > dependency tick 11.
- Fixture completeness at report time: `claim-excerpt-map.md` (Q5) landed ~17:44;
  `README.md` (Q5) still absent — the fixture is 9/10 files. My PASS covers Q4's 8
  files; end-to-end fixture completeness (map/README, `map_obligations` receipt) is
  other seats' remit.
- Environment flag: a temp-file prefix check of mine first reported a false
  "inherited region BYTE DIFFERS" because `/tmp` transiently returned
  `No space left on device` (16 G tmpfs, 8.5 G free when re-checked); re-run with
  process substitution (no temp files) gave the true PREFIX MATCH. Seats that stage
  scratch in `/tmp` may report false negatives this round.

## Findings / contradictions

None. Every sub-claim of this seat verified on the frozen bytes. The only
non-conformity observed is procedural and self-reported by Q4 (intermediate comma
placement rewritten at 17:40:16, before its receipts).

## Bottom line

**PASS** — all inherited r96 rows (5 entities, 1 relation, `timeline[:4]`,
`sources[:4]`, contradictions) are key-order-sensitively value-identical to r95 with
new rows appended, r95 is byte-untouched vs `dcb2d92` (empty git diff, 10/10 blob
hashes), and both `cmp` prefix claims hold (`fictional-excerpts.md` 1845 B prefix;
`source-excerpt.md` byte-identical) — proven falsifiable by mutation controls.
