# V51 — relation-scope (round 95)

Seat: V51 relation-scope. Task: after P3, (a) `corpus/fixtures/r95-crossing-aftermath/relations.json`
byte-identical to r94's, scope bound preserved verbatim; (b) the map's relation row anchor unchanged;
(c) confirm no new relation semantics anywhere.

Baseline: HEAD `fb118c42038ed27a747eec704b9aab41bb4b2ebe` (r94 closure `fb118c4`).
Poll-wait: P3 fixture JSON present ~16:18, P4 map/README + report at 16:21; verification ran
16:22–16:29 -03:00 on stable bytes (relations.json sha256 re-checked identical at 16:29).

Revisions inspected (sha256, this seat's own reads):

| Artifact | sha256 | Notes |
|---|---|---|
| `corpus/fixtures/r95-crossing-aftermath/relations.json` | `c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9` | delivered, unchanged through verification |
| `corpus/fixtures/r95-crossing-aftermath/claim-excerpt-map.md` | `30281ff1a497bbe66f23cbd8a49befb3319595f20990718a0ffe8050741a874a` | md5 `a872889e86a10127750ba0647e4829ff` == P4's declared hash |
| `corpus/fixtures/r94-paired-crossing/claim-excerpt-map.md` (control) | `ed9527c551049a6964adc872fbff722b4bdd6a53aa8713fbb6a5d92254e89a47` | git blob `7edafa24aef9f789ccbe7ed7a9aebec5584c6321` |
| `corpus/tools/map_obligations.py` (P1, settled) | `d1c239ccb21404490bfe120a8c8de45af89265437d5be53fb712ff27e4212108` | stable ≥10 polls before use |
| `corpus/tools/map-obligations-contract.json` (P2, in flight) | `8173bb97592a377716866737e8fcb4043014c9814e77a6248500d301a39170db` | stable ≥8 polls; P2 report not yet written at 16:29 |
| `corpus/tools/support_check.py` | `55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c` | r94 revision, unchanged |
| `corpus/fixtures/check_bible.py` | `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` | r94 revision, unchanged |

## 1. relations.json byte-identical to r94 (claim (a)) — CONFIRMED

```
$ sha256sum corpus/fixtures/r94-paired-crossing/relations.json corpus/fixtures/r95-crossing-aftermath/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r94-paired-crossing/relations.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r95-crossing-aftermath/relations.json

$ cmp corpus/fixtures/r94-paired-crossing/relations.json corpus/fixtures/r95-crossing-aftermath/relations.json && echo "CMP: IDENTICAL"
CMP: IDENTICAL

$ git hash-object corpus/fixtures/r95-crossing-aftermath/relations.json
2804ae91240dbf34753bf955d4fab9ffeab0a8df          # == git ls-tree fb118c4 r94 blob, same object
```

Both files are 139 bytes. The scope bound is carried verbatim in the delivered bytes:

```
$ cat corpus/fixtures/r95-crossing-aftermath/relations.json
[
  {
    "from": "aru",
    "to": "evin",
    "type": "agreed_co_stewardship_for_this_crossing",
    "source_id": "crossing-minute"
  }
]
```

`type` still encodes "for this crossing only"; no endpoint, type, or `source_id` changed.
Re-checked at 16:29 (`cmp` → `STILL_IDENTICAL`) after P1/P2/P5 landed.

Related inherited byte copies in the same fixture (my own `cmp`): `entities.json`,
`contradictions.json`, `inspiration-note.md`, `source-excerpt.md` all `IDENTICAL` to r94.

## 2. Map relation row anchor (claim (b)) — CONFIRMED (one necessary cell change)

r95 map line 32 (`claim-excerpt-map.md:32`):

```
| J11 | `relations.json#/0` (`from`, `to`, `type`, `source_id`) | `crossing-minute` | `r95-crossing-aftermath:crossing-minute` | `fictional-excerpts.md` | 19 | `verbatim` | `There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.` |
```

Cell-by-cell against r94 map line 32 (python3 parse of both delivered files):

```
SAME  ID                       'J11'
SAME  pointer+fields           '`relations.json#/0` (`from`, `to`, `type`, `source_id`)'
SAME  in-world source ID       '`crossing-minute`'
DIFF  qualified namespace      r94='`r94-paired-crossing:crossing-minute`' r95='`r95-crossing-aftermath:crossing-minute`'
SAME  excerpt path             '`fictional-excerpts.md`'
SAME  line span                '19'
SAME  R9 mode                  '`verbatim`'
SAME  exact anchor             '`There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.`'
anchor byte-equal: True
cells equal except index 3 (namespace): True
```

The anchor cell itself is byte-identical; so are the pointer, in-world source ID, excerpt path,
span (19), and mode. The only differing cell is the path-qualification column, which the map's own
scope rule requires to name this fixture's cluster path (map line 3: "`source_id` values remain
cluster-local in JSON and are qualified in the map as `(cluster path, source ID)` pairs"), and which
is applied identically to all 14 inherited rows (map line 18: "The 14 inherited rows carry the r94
JSON pointers, excerpt anchors, spans, and delivery modes unchanged; only the path-qualification
column names this fixture's cluster path."). This is a naming/qualification change, not an anchor or
semantic change.

Anchor resolves in the delivered excerpt bytes and passes the lexical receipt:

```
$ grep -nF 'There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.' corpus/fixtures/r95-crossing-aftermath/fictional-excerpts.md
19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.

$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath | grep -E "J11|RESULT"
PASS J11: source-support; mode=verbatim; anchor=found; 19:> There, they agreed, for this crossing only, to share stewardship of the Chalk Stair.
RESULT PASS                                        # exit 0
```

Line 19 is the same line number as in r94 because the r95 excerpt file is a strict byte-prefix
extension (first 1116 bytes identical; aftermath appended at lines 22–31), so no inherited anchor
shifted.

## 3. No new relation semantics anywhere (claim (c)) — CONFIRMED

- **Repo-wide relation census** (python3 over all `corpus/fixtures/*/relations.json`):
  excluding r95: 155 rows / 10 distinct types; including r95: 156 rows / 10 distinct types;
  new types added: `[]`. The single added row is the byte copy above; `agreed_co_stewardship_for_this_crossing` count 1 → 2 (same type, second path-qualified occurrence).
- **No tracked relations file modified in the round**: `git diff fb118c4 --name-only | grep -i relation` → `NONE`. No other fixture's relations changed.
- **The new tick-11 row is a timeline event, not a relation**: `timeline.json#/3` `aftermath-missing-evin`, `depends_on: ["paired-crossing-decision"]` — an event dependency. `relations.json` still holds exactly 1 record.
- **Map scope unchanged in kind**: r95 map line 3 still reads "one relation" (r94 line 3 likewise); r95 map line 49 still bounds it: "The new relation encodes only the agreement for this crossing, not perpetual performance or alliance."
- **Checker**: `python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath` → `CLEAN: schema, citations, relations, timeline; 0 violations`, exit 0 (control r94 same). check_bible's relation rules (schema, endpoint existence, `allied_with` reciprocity) are unchanged (`check_bible.py` sha256 == r94 revision).
- **Tool surface (P1 revision `d1c239cc…`)**: the only added line containing "relation" in the whole diff is the legacy-dialect token regex `r"^(entities|relations|timeline)\[([0-9]+)\]"`, which translates `relations[i]` → `relations.json#/i` before comparison (same canonical semantics; a pointer-syntax generalization for the r88 map form). No new relation validation, typing, or edge rules were added; `raw_obligations_values` still reads relations as `{from,to,type,source_id}` records exactly as at r94.
- **Contract (P2 revision `8173bb97…`)**: its only relation token is the new `legacy_pointer_dialect.pointer` description listing the same translated field-path tokens; no relation semantics added.
- **Docs/notes**: r95 `README.md:3` says the "one inherited relation" is copied by JSON value; `README.md:11` and `corpus/knowledge/r95-aftermath-scope-note.md:22` repeat the crossing-only bound; the new source `sources.json#/3` reliability note disclaims "a breach, a continuing duty, a perpetual obligation". The new event description references "the agreement" (the existing relation) — it asserts no new relation and no duty beyond the crossing.
- **Receipts with the settled tool**: `map_obligations.py corpus/fixtures/r95-crossing-aftermath` → `OBLIGATIONS raw=15 mapped=15` / `RESULT PASS` exit 0 (control r94 `14/14 PASS` exit 0).

## 4. Observations and flags (reported exactly, not hidden)

1. **Stale adjective in the map's normalization note.** r95 map line 49 retains r94's sentence
   "The new relation encodes only the agreement for this crossing, not perpetual performance or
   alliance." (identical sentence at r94 map line 48) although the same r95 map (line 18) frames
   J01–J14 as inherited and the fixture adds no relation. The word "new" is a carryover; the bound
   it states is unchanged and accurate. Wording staleness only — not new relation semantics, and it
   does not touch the J11 anchor. Flagged for the round's doc-fidelity/consistency seats.
2. **Strict-reading caveat for claim (b).** The J11 row as a whole is not byte-identical (one cell,
   the path qualification, differs). If a verifier reads "the map's relation row anchor unchanged"
   as requiring the full row to be byte-identical, that stronger reading fails; the anchor cell
   itself and all other cells are byte-identical, and the differing cell is mandated by the map's
   own declared qualification rule.
3. P3's own flag (`"kind": "fictional first-person note"` vs the spec's "(kind note)") is not
   relation-relevant; noted for the parent only.

## 5. Bottom line

PASS — r95 `relations.json` is byte-identical to r94's (sha256/cmp/git blob), the map's J11 relation
row keeps its pointer, source ID, span 19, mode, and anchor cell byte-identical (only the required
path-qualification cell changes), and no new relation semantics appear anywhere in the round's
deliverables or tool diff; two non-blocking observations (stale "new relation" adjective; strict
full-row byte-identity reading fails on the namespace cell) are documented above.
