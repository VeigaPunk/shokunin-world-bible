# F06 — c1-continuity (round-94 FOLLOW-UP verification seat)

Role: independent non-author verification of the C1 continuity clause. Repo root `/home/vgpnk/Projects/shokunin/lore-shokunin`; all commands run from repo root with `python3`. No corpus byte was written by this seat; this report is the only file this seat authored.

Pins observed: `git rev-parse HEAD` → `65a93298cb100fdbf5732ac6de55f01a683c02d8` (follow-up declaration `65a9329`), candidate `abbc3e0`, baseline `9c2eea3`.

Claim under test (from `.ufo/waves/round-94/wave-spec.md:11,15`): the new fixture `corpus/fixtures/r94-paired-crossing/` is an explicit continuation of `r88-m3-maya-cluster`, with shared referents and source IDs intentionally path-qualified, inherited tick-9 accounts unchanged, the two tick-9 places not conflated, the new occasion not rewriting old accounts, and the relation recording a supported agreement/co-stewardship only.

## 1. Continuation and counts

```
$ python3 - <<'EOF' ... json.load ... EOF
r94 entities count 5 r94 relations count 1 r94 timeline count 3
r88 entities count 4 r88 relations count 0 r88 timeline count 2
```

Matches the declared 4/0/2 → 5/1/3. The fifth entity is `chalk-stair` (`entities.json#/4`, `first_appearance: crossing-minute`); the relation is `relations.json#/0`; the third event is `timeline.json#/2`.

## 2. Inherited tick-9 accounts unchanged

Same command as above:

```
inherited entities prefix-equal: True
 entity 0 aru equal: True
 entity 1 evin equal: True
 entity 2 quiet-rise equal: True
 entity 3 salt-court equal: True
inherited timeline prefix-equal: True
 event aru-ninth-bell equal: True
 event evin-ninth-bell equal: True
r88 sources all present & equal in r94: True r94 extra sources: ['crossing-minute']
```

`r94e[:4]==r88e` and `r94t[:2]==r88t` compare whole JSON objects by value, so the four inherited entities (including each claim's `statement`/`source_id`) and both tick-9 events are value-identical, not merely similar. `r88-m3-maya-cluster/sources.json` is a value-equal subset of the r94 source table; the only added source is `crossing-minute`.

Byte-level preservation:

```
$ cmp r88-m3-maya-cluster/source-excerpt.md r94-paired-crossing/source-excerpt.md  → IDENTICAL
$ cmp r88-m3-maya-cluster/inspiration-note.md r94-paired-crossing/inspiration-note.md → IDENTICAL
$ cmp r88-m3-maya-cluster/contradictions.json r94-paired-crossing/contradictions.json → IDENTICAL
$ python3 - <<'EOF' (startswith on raw bytes)
r94 starts with r88 bytes: True
prefix len r88 484 r94 1116
```

The appended tail of `fictional-excerpts.md` is exactly the minute block (blank line + minute lead-in + 4 quoted lines); the inherited verse (lines 7–8) and register (lines 12–13) bytes are untouched.

Git-level: no existing corpus byte changed between baseline and candidate.

```
$ git diff --name-status 9c2eea3 abbc3e0 -- corpus/
A  corpus/fixtures/r94-paired-crossing/…  (10 files, all A)
A  corpus/knowledge/r94-cross-myth-design-comparison.md
A  corpus/tools/map-obligations-contract.json
A  corpus/tools/map_obligations.py
$ git diff --name-only 9c2eea3 abbc3e0 -- corpus/fixtures/r88-m3-maya-cluster
(empty)
$ git diff 9c2eea3 abbc3e0 -- corpus/fixtures/r88-m3-maya-cluster | wc -l
0
```

Every corpus change in the candidate is an addition (`A`); no `M`/`D` row exists, and the r88 fixture is byte-identical across the two commits.

## 3. The two tick-9 places are NOT conflated

```
$ python3 -c "… place ids/names, event places …"
quiet-rise | Quiet Rise | first_appearance: paired-clock
salt-court | Salt Court | first_appearance: paired-clock
chalk-stair | Chalk Stair | first_appearance: crossing-minute
--- event places ---
aru-ninth-bell tick 9 entity aru place quiet-rise depends_on []
evin-ninth-bell tick 9 entity evin place salt-court depends_on []
paired-crossing-decision tick 10 entity aru place chalk-stair depends_on ['aru-ninth-bell', 'evin-ninth-bell']
names ['Quiet Rise', 'Salt Court', 'Chalk Stair'] unique True
ids ['quiet-rise', 'salt-court', 'chalk-stair'] unique True
```

Three distinct ids, three distinct names, and the two tick-9 events keep different `place_id` values; the new tick-10 event sits at a third place and names both prerequisites. The minute text keeps them apart rather than merging them (`fictional-excerpts.md:17` — “the named rain-dark crossing between Quiet Rise and Salt Court”; `:20` — “Aru's north-lantern entry at Quiet Rise and Evin's south-bell entry at Salt Court”). A grep of the whole fixture directory for conflation phrasing (`same place`, `both at Quiet Rise`, `both at Salt Court`, `single place`) returned no hits, and the r88 near-miss framing is restated at `r94-paired-crossing/README.md:9` (“remain distinct tick-9 events … it does not change the earlier locations or turn their near-miss into a contradiction”).

`check_bible.py` independently resolves and orders these dependencies (`check_bible.py:393-414`: `unknown event` for unresolvable ids, `timeline inversion` when a dependency tick is not earlier), and the run is clean, so both named tick-9 entries are real resolvable earlier events:

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations
check_bible exit=0
```

## 4. The new occasion does not rewrite the old accounts

```
$ python3 - <<'EOF' (compare old events to new events, then test the minute restatement)
aru-ninth-bell fields identical across fixtures: True
evin-ninth-bell fields identical across fixtures: True
  Aru paired with north lantern : True
  Aru paired with Quiet Rise : True
  Evin paired with south bell : True
  Evin paired with Salt Court : True
  no swapped actor/place pairing : True
  bounded to this crossing : True
```

The only place the new minute restates the old entries is `fictional-excerpts.md:20`, and that restatement keeps each actor with the same object and place as the inherited register (`:12`/`:13`), with no swapped pairing. The minute describes the new occasion as “After both Tick 9 entries above” (`:18`), i.e. as a consequence added after the inherited accounts, not as a revision of them; `README.md:3` states the same (“not a rewrite of that snapshot”). No file in the fixture asserts a different place, actor, or tick for `aru-ninth-bell`/`evin-ninth-bell`.

## 5. Shared referents and source IDs are intentionally path-qualified

Explicit statements: `r94-paired-crossing/README.md:7` (“Source IDs are cluster-local. Compare them as path-qualified pairs, for example `(r88-m3-maya-cluster, paired-clock)` and `(r94-paired-crossing, paired-clock)`, not by bare ID alone”); `claim-excerpt-map.md:3` (“qualified in the map as `(cluster path, source ID)` pairs”) and `:11,:18`; `corpus/knowledge/r94-cross-myth-design-comparison.md:23` (“distinct path-qualified references, not identity evidence”).

Mechanically:

```
$ python3 - <<'EOF' (parse the map's JSON-facts table)
JSON fact rows: 14 IDs: ['J01'…'J14']
Editorial rows: 2 IDs: ['S01', 'S02']
rows whose namespace column is path-qualified: 14 / 14
rows lacking canonical file.json#/pointer syntax: none
inherited-pointer rows (entities 0-3 or timeline 0-1): 10
```

All 14 obligation rows carry a `Path-qualified source namespace` value of the form `r94-paired-crossing:<id>`, and every row uses `file.json#/pointer` syntax. The JSON itself keeps bare cluster-local `source_id` values, which is exactly what the qualification note describes; `python3 -c` over the three JSON files shows only `['crossing-minute', 'paired-clock']` referenced, with no `veil-verse` reference (as in r88).

## 6. The relation records the supported agreement only

`relations.json#/0`:

```json
{"from": "aru", "to": "evin", "type": "agreed_co_stewardship_for_this_crossing", "source_id": "crossing-minute"}
```

The type wording is a direct encoding of the delivered minute at `fictional-excerpts.md:19` (“they agreed, for this crossing only, to share stewardship of the Chalk Stair”): agreement + co-stewardship + an explicit one-crossing scope qualifier, with no alliance or durability term. The bounds are asserted, not merely implied:

- `README.md:9` — “The relation records only the source-supported agreement between Aru and Evin to share stewardship for this crossing. It is not evidence of an alliance, a continuing practice, or perpetual performance.”
- `sources.json:18` (`crossing-minute` reliability_note) — “…not evidence of continuing performance, a standing alliance, or an external historical fact.”
- `claim-excerpt-map.md:48` — “The new relation encodes only the agreement for this crossing, not perpetual performance or alliance.”
- `knowledge/r94-cross-myth-design-comparison.md:35` — “This is not an alliance or proof of later performance.”
- A grep for `alliance|allied|perpetual|permanent|forever|standing` across the fixture returns hits only in those denying/limiting statements (plus `claim-excerpt-map.md:48`), never as an assertion.

The checker's only relation-type-specific rule is for `allied_with` (`check_bible.py:347` builds `allied = [row … if row['type'] == 'allied_with']`; `:352,:360,:365` impose the faction/reciprocity rules on that type). The chosen type is not `allied_with`, so no alliance semantics are asserted structurally, and `check_bible.py` resolving this relation's endpoints and source (lines 177-185) is part of the clean run in §3.

## 7. Independent tool receipts (re-run by this seat)

```
$ python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16; DISTINCT-ANCHORS 12/12
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 16/16; VALIDATED-ROWS 16/16
RESULT PASS   (exit 0)
```

The declared 14 obligations (five first-appearance pointers, five claims, one relation, three events) are present and one-to-one in the map; J11 anchors at line 19 and J14 at lines 18-20, matching `claim-excerpt-map.md:32,35`.

```
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS   (exit 0)
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r93-m2-kojiki-cluster
OBLIGATIONS raw=12 mapped=12
RESULT PASS   (exit 0)
```

This raw-JSON-to-map comparison corroborates the 14/14 obligation inventory independently of the markdown-side lexical receipt. Disclosure: my first invocation used a path that does not exist (`corpus/fixtures/r93-canonical-map`), which correctly produced `FINDING cluster_missing … RESULT ERROR` (exit 2); the real r93 fixture path is `corpus/fixtures/r93-m2-kojiki-cluster`, whose run is the PASS quoted above. That was my invocation error, not a tool or fixture defect.

## 8. Observations (non-blocking, no claim falsified)

1. **Map-side inheritance gap.** The r94 map's R9 declaration table declares only `fictional-excerpts.md:12-20` (`claim-excerpt-map.md:11`); r88's map additionally declared the inherited verse at `fictional-excerpts.md:7–8` (`r88-m3-maya-cluster/claim-excerpt-map.md`, R9 declarations table, “no JSON fact points to this source”). No r94 row anchors at lines 7/8 (grep for `fictional-excerpts.md\` | 7` / `| 8` → `none`), the map's stated scope is the 14 obligations plus 2 editorial comparisons (`:3`), and `support_check.py` reports `MODES 16/16`, so no declared rule is broken. This is a documentation-scope difference in the map, not a change to the JSON bible or to the inherited excerpt bytes.
2. **Relation row has no stewardship-object field.** `relations.json#/0` records the agreeing pair and the scoped type; the object of stewardship (Chalk Stair) appears only in the type qualifier and in the excerpt (`:19`), and the map's J11 field list is `(from, to, type, source_id)` (`claim-excerpt-map.md:32`). Consistent with the bounded claim, but a reader of the JSON alone cannot recover what is co-stewarded.
3. **J11 antecedent lives one line earlier.** The J11 anchor line 19 opens with the pronoun “they”; its antecedent (“Aru and Evin”) is on line 18. The fixture discloses this (`knowledge/r94-cross-myth-design-comparison.md:35`), and the map's own note says anchors are lexical preflight (`claim-excerpt-map.md:50`). Whole-claim reading must include line 18.

## Bottom line

**PASS** — the r94 fixture is a genuine value- and byte-preserving continuation of `r88-m3-maya-cluster` (inherited entities/events/sources value-equal, `cmp`-identical source-excerpt/inspiration-note/contradictions, r88 excerpt file an exact byte prefix, no modified corpus path in `abbc3e0`), the two tick-9 places stay distinct with the tick-10 event depending on both resolvable earlier entries, the new minute adds a bounded consequence without rewriting the inherited accounts, source IDs are explicitly path-qualified in all 14 map rows, and the relation encodes only the source-supported one-crossing co-stewardship agreement (no alliance/perpetual claim anywhere; `check_bible` CLEAN, `support_check` PASS 14/14, `map_obligations` PASS raw=14 mapped=14).
