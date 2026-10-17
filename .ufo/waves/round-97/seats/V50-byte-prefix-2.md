# V50 byte-prefix-2 — round 97 seat report

- Seat: V50 (verifier, byte-prefix-2). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; all commands run from the lane repo root with `python3`. Baseline `f3e09f9`.
- Scope: (1) `cmp` r96-post-repair vs r97 copied files; (2) `sources.json` / `timeline.json` JSON-level diff — appended rows only; (3) `fictional-excerpts.md` strict byte-prefix.
- Scratch (mine, exclusive): `.ufo/waves/round-97/seats/V50-scratch/` (`verify_byte_prefix.py`, `verify_pass2.py`, `verify_pass3.py`, `pass1..4.txt`, `final1.txt`, `final_all.txt`, `final_receipts.txt`). No writes outside scratch + this report. No commits, no pushes, no network.
- Poll-wait: fixture appeared at try=5 (~80 s); R4 report present before final verification; R5's map/README landed mid-poll. Verified revision: r97 fixture as of `2026-10-17T21:51:05Z`.

## 1. Byte-copy identity — `cmp` r96 (post-repair) vs r97 copies

```
$ for f in entities.json relations.json contradictions.json inspiration-note.md source-excerpt.md; do cmp corpus/fixtures/r96-crossing-response/$f corpus/fixtures/r97-crossing-acknowledgment/$f && echo "$f IDENTICAL"; done
entities.json IDENTICAL
relations.json IDENTICAL
contradictions.json IDENTICAL
inspiration-note.md IDENTICAL
source-excerpt.md IDENTICAL
```

All five `cmp` calls rc=0, empty stdout/stderr. sha256 (r96 = r97, 16-hex prefix): entities `026af0bc2cdab150` (1449 B), relations `c279254bc7de0636` (139 B), contradictions `37517e5f3dc66819` (3 B), inspiration-note `58f5390e5928ebad` (1956 B), source-excerpt `b5edc2fd3c2e3d4f` (640 B).

r96-side provenance: all five r96 working-tree files are byte-equal to the committed `f3e09f9` blobs (`git show f3e09f9:<path>` byte-compare → MATCH-HEAD), so the copies are identical to both the pre-repair and post-repair r96 state — R4's map-only cosmetic repair cannot have altered them. The only r96 file differing from HEAD is `claim-excerpt-map.md` (the intended repair; `git diff --numstat` = `2 2`).

## 2. `sources.json` / `timeline.json` — appended rows only

JSON level (deep equality of the inherited prefix, order and values):

```
sources.json : rows r96=5 r97=6 delta=1 ; inherited prefix deep-equal: True
timeline.json: rows r96=5 r97=6 delta=1 ; inherited prefix deep-equal: True
```

Byte level (pure insertion before the closing bracket; line diff `difflib.unified_diff` n=1):

```
$ diff corpus/fixtures/r96-crossing-response/sources.json corpus/fixtures/r97-crossing-acknowledgment/sources.json
30a31,36            # pure append, no deletions
>   },
>   { "id": "aru-acknowledgment-note", "title": "Aru's Chalk Stair Acknowledgment Note",
>     "kind": "fictional first-person note", "reliability_note": "...receipt only; not evidence of a
>     resolution, a reconciliation, an accusation, a winner between the accounts, a continuing duty,
>     or an external historical fact." }
$ diff corpus/fixtures/r96-crossing-response/timeline.json corpus/fixtures/r97-crossing-acknowledgment/timeline.json
52a53,63            # pure append, no deletions
>   }, { "id": "acknowledgment-aru-records", "tick": 13, "entity_id": "aru",
>        "place_id": "chalk-stair", "depends_on": [ "response-evin-salt-court" ],
>        "description": "At the Chalk Stair at tick 13, Aru reports receiving Evin's response and states
>        that both first-person accounts stand unresolved; the note asserts no accusation, no
>        reconciliation, no winner between the accounts, and no new duty beyond this crossing.",
>        "source_id": "aru-acknowledgment-note" }
```

Added lines = 6 (sources) / 11 (timeline), removed lines = 0, hunk count = 1 each. Position proof: with `X = r96[:-len(b"  }\n]\n")]`, both files satisfy `r97.startswith(X)` and `r97.endswith(b"  }\n]\n")`; inserted bytes 500 (sources) / 502 (timeline) sit exactly between the last inherited row's closing brace and the array close. Key sets of the appended rows equal the inherited rows' key sets; ids unique (6/6 each) and inherited ids unchanged in order.

Appended event conforms field-for-field to the round-97 declaration: `{id: acknowledgment-aru-records, tick: 13, entity_id: aru, place_id: chalk-stair, depends_on: [response-evin-salt-court]}` — True. Its `source_id` (`aru-acknowledgment-note`) resolves to the appended source row — True. No resolution/accusation/reconciliation wording introduced; `contradictions.json` remains `[]` (3 bytes, identical).

## 3. `fictional-excerpts.md` — strict byte-prefix

```
r96 bytes=2588  r97 bytes=3410  prefix=True  strict=True
r96 sha=06b11bec604f6d68…  r97 sha=8ba491cb249dd57f…  appended tail bytes=822
$ diff <(git show f3e09f9:corpus/fixtures/r96-crossing-response/fictional-excerpts.md) corpus/fixtures/r97-crossing-acknowledgment/fictional-excerpts.md
42a43,53            # single append hunk, nothing removed/reordered
```

r96's 2588 bytes are an exact prefix of the r97 file (and the r96 file itself is MATCH-HEAD, so the prefix is the frozen-baseline bytes). The 822-byte appended tail is the section `## Round 97 acknowledgment note (2026-10-17)`, folio 7, lines 44–53: four quoted tick-13 lines plus the receipt-only scope paragraph; no inherited line altered.

## 4. Cross-checks and context (not my ownership)

- R4's report corroborates: five JSON tables + `sources`/`timeline`/`fictional-excerpts` pure-append; `check_bible` CLEAN exit 0 on r97 (and r96 control); census 171; r96 map repair `2 2` with `support_check`/`map_obligations` receipts identical before/after under both frozen and interim tool revisions.
- r96 map repair scope independently measured: `git diff -U0` vs `f3e09f9` changes exactly 2 lines — editorial delimiter `|---|---|---|---|---|---:|---|---|` → `|---|---|---|---|---:|---|---|` (8 → 7 cells, matching the 7-column header), and the stale sentence "The new relation encodes only the agreement…" → "The new tick-12 event encodes only Evin's second account…". All 18 `J*`/`S*` data rows byte-unchanged (head vs live line lists equal); file length 56 lines both sides.
- The r97 `README.md` and `claim-excerpt-map.md` were byte-copies of the r96 files at R4 creation time, but R5 has since rewritten both — they are **no longer** copies at my verification time: map `e851f068cfd7ed02…` → `49d4834e124fa6cf…` (18:48), README `ff52ced48bf42147…` → `d9387b7d73264dfc…` (18:49). Any sibling claim that "all 10 r97 files are byte-copies of r96" is only true of the 8 files I verified plus the map/README at creation time, not at closure.
- Producer-report status at my close: `R1-map-pinning.md`, `R2-contract-docs.md`, `R4-fixture-author.md` present; R3/R5/R6 reports not yet written. R4 is the producer of every file in my scope, and its report is present — my verification is not against a plan.

## 5. Bounds

- I verified bytes/JSON structure only: that the appended rows and section are the only deltas, that they match the declared ids/fields, and that the inherited bytes are untouched. I did not adjudicate semantic entailment, source authenticity, or the 17-obligation inventory (other seats).
- Verification is a snapshot of the working tree at `2026-10-17T21:51:05Z`; the fixture is uncommitted (r97 closure not yet run). Hashes are recorded above and in `V50-scratch/` for re-check after closure.
- Harness self-validated: synthetic positive fixture (r96 + 1 source + 1 event + appended section) → all checks PASS; negative control (mutated inherited `tick`) → `FAILURES: ['sources-delta-not-1', 'timeline-inherited-changed', 'timeline-delta-not-1']` plus `excerpts-not-strict-no-appended-tail`, so the checks are load-bearing rather than vacuous.

## Bottom line

**PASS** — r97 copies of the five r96 files are byte-identical (`cmp` rc=0) to the post-repair r96 tree; `sources.json` 5→6 and `timeline.json` 5→6 are strict EOF appends (1 hunk, 0 deletions, inherited prefix deep-equal, appended event matches the declared tick-13 `acknowledgment-aru-records`); `fictional-excerpts.md` is a strict byte-prefix of r96 (2588 B prefix, 822 B appended section).
