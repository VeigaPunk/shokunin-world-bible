# V11 — c2-anchors (round 96)

Seat: V11 c2-anchors. Scope per seat spec: independently verify that ALL 16
anchors in `corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`
resolve in-span via my own `grep -nF` implementation; every inherited anchor
must exist at the SAME line numbers as in r95's map; the new anchor only
inside the appended response section; report any drift with path:line.

Baseline: r95 closure `dcb2d92`. Repo root
`/home/vgpnk/Projects/shokunin/lore-shokunin`. No commits; no network; no
repo writes except this report and my scratch dir
`.ufo/waves/round-96/seats/V11-scratch/`. No nested agents.

## 0. Poll-wait evidence (target = Q5's map + Q4/Q5 reports)

Skeleton draft — filled after READY.

## 1. Method

Checker: `.ufo/waves/round-96/seats/V11-scratch/v11_check.py` (my own
implementation). Parses both maps' row tables; for every r96 row runs
`grep -nF -e "<anchor>" -- <excerpt>` via `subprocess` and cross-checks line
numbers against a pure-Python `line.count(anchor)` scan; checks in-span
containment, outside-span occurrences, inherited-row anchor/span byte
equality + resolved line sets r95 vs r96, new-row occurrence placement,
byte-prefix discipline, and the declared inventory. Parser validated first
on r95↔r94 (`validate` mode): ALL-ANCHOR-CHECKS-PASS, inventory
declared=[15, 2, 17, 13] == parsed, exit 0 — reproducing the r95 map's
declared inventory exactly.

## 2. Result — full checker output

Skeleton draft — filled after READY.

## 3. Inherited anchors — same line numbers

Skeleton draft — filled after READY.

## 4. New response anchor — only in the appended section

Skeleton draft — filled after READY.

## 5. Copy discipline (independent, pre-verified during poll window)

```
$ for f in source-excerpt.md entities.json relations.json contradictions.json inspiration-note.md; do cmp -s r95/$f r96/$f && echo "$f IDENTICAL"; done
source-excerpt.md IDENTICAL
entities.json IDENTICAL
relations.json IDENTICAL
contradictions.json IDENTICAL
inspiration-note.md IDENTICAL
```

sources.json / timeline.json prefix discipline: the r95 four entries are
unchanged prefixes of the r96 tables (python `r96[:4] == r95` → True for
both); r96 adds exactly `evin-response-note` (source 5) and
`response-evin-salt-court` (tick 12, evin, salt-court,
depends_on [aftermath-missing-evin]).

## 6. Drift findings

Skeleton draft — filled after READY.

## 7. Boundaries (not verified by this seat)

- Anchor resolution is lexical (`grep -nF` + substring scan); not semantic
  entailment, chronology, or canon judgment.
- `support_check.py` / `map_obligations.py` receipts and `check_bible` were
  not re-run by me; the map's declared inventory was checked against my own
  parse only.
- Timeline/sources counts and sibling-file copy discipline are supporting
  evidence, not the seat's anchor claim.

## Bottom line

Skeleton draft — filled after READY.
