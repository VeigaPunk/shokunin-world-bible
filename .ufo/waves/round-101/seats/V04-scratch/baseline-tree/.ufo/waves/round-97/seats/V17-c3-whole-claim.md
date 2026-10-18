# V17 — c3-whole-claim (round 97)

- Seat: V17 c3-whole-claim (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline `f3e09f9`; all commands from the lane root with `python3`.
- Scope: manual whole-proposition review of the r97 acknowledgment note — propositions traced to excerpt clauses and JSON rows; no resolution/accusation/reconciliation/new-duty constructible; descriptions scoped.
- Writes: this report and `.ufo/waves/round-97/seats/V17-scratch/` only (notes.md, frozen-hashes.txt, receipts-r97.txt, whole-claim-trace.txt). No commits, no pushes, no network, no nested agents, no other writes.

## Poll-wait record

- r97 fixture first observed 18:44 (R4's authored files); R5's `README.md`/`claim-excerpt-map.md` still byte-copies of the r96 versions at 18:47 — I did not verify that interim state.
- My first poll matched `R4-scratch`/`R5-scratch` directories by the `^R4`/`^R5` prefix — a false positive I caught; re-polled with `.ufo/waves/round-97/seats/R4*.md` / `R5*.md` file globs.
- Producer reports: `R4-fixture-author.md` mtime 18:50:14; `R5-fixture-docs.md` mtime 18:51:25; both detected by my poll (`REPORTS at try 22`). Every check below ran against real files on disk; no plan was verified.

## Frozen revision (all hashes stable across my window 18:51:34 → 18:52:24, re-checked after all runs)

```
49d4834e124fa6cfaa1a73cd5d1a7bc2cb59711c6233b418fe7485a17eedc94f  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  entities.json
8ba491cb249dd57f6aee8ca216133b07c06287c0240be658ea2e68da0cf5703c  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
d9387b7d73264dfc6c01d27cc6bf24c58ef6bdb4461d2ae8fbfdb6376d9e019f  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
438fb513a62496c41179ead3ea2a55a69ff4ce1fd191c3a7ebccb10651a8dc73  sources.json
73063a863a68fc4feae073ce74cfa9e5fddb4f9cc4060d12b333d495a255895b  timeline.json
```

Tool revisions at my receipts: `check_bible.py` `ff9fd2aa…`, `support_check.py` `55a5eb27…`, `map_obligations.py` `86b52949…`. R5's report pins the same three; the two doc hashes above match R5's report exactly.

## Receipts (my runs, from the lane root)

```sh
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
CLEAN: schema, citations, relations, timeline; 0 violations            EXIT=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J16 (anchors at the same line numbers as r96)
PASS J17: source-support; mode=verbatim; anchor=found; 48:> Tick 13: I received Evin's response at the Chalk Stair.
PASS S01 / PASS S02: editorial-row; mode=verbatim; anchor=found
RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/19; VALIDATED-ROWS 19/19
RESULT PASS                                                             EXIT=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
OBLIGATIONS raw=17 mapped=17
INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19
RESULT PASS                                                             EXIT=0
```

Full outputs: `.ufo/waves/round-97/seats/V17-scratch/receipts-r97.txt`.

## Whole-proposition trace (manual)

Excerpt clauses (1-based lines, verified by script): line 44 section header; line 46 attribution; lines 48-51 quoted note; line 53 scope.

| Clause (line) | Excerpt wording | JSON rows | Map / README |
|---|---|---|---|
| 1 (48) | `Tick 13: I received Evin's response at the Chalk Stair.` | `timeline.json#/5` `acknowledgment-aru-records` ("Aru **reports** receiving Evin's response", tick 13, `aru`, `chalk-stair`); `sources.json#/5` `aru-acknowledgment-note` ("Aru reports receiving Evin's response at the Chalk Stair") | J17 row: pointer `timeline.json#/5`, source `aru-acknowledgment-note`, span 44-53, anchor line 48 (grep hit 48, within span) |
| 2 (49) | `I hold to my own account; both accounts stand unresolved.` | `timeline.json#/5` "states that both first-person accounts stand unresolved" | Map line 57 "the retained account … remain unresolved"; README line 9 "while holding to his own account" |
| 3 (50) | `I make no accusation against Evin, and I select no winner between us.` | `timeline.json#/5` "asserts no accusation … no winner"; `sources.json#/5` "not evidence of a … accusation, a winner between the accounts" | Map line 57 "asserts no accusation and no reconciliation and selects no winner"; README line 11 |
| 4 (51) | `I assert no reconciliation, no new duty, and no obligation beyond this crossing.` | `timeline.json#/5` "no reconciliation … no new duty beyond this crossing"; `sources.json#/5` "not evidence of a resolution, a reconciliation, … a continuing duty" | Map line 57; README line 11 crossing-only bound |

Whole-proposition readings (bounded, matching the record's own scoping):

- Clause 1 is a first-person **receipt report**; the JSON preserves report status ("Aru reports receiving"), names no location for Evin, asserts no meeting, and attributes nothing about the response's truth. `timeline.json#/5.source_id == sources.json#/5.id == aru-acknowledgment-note` (verified); `depends_on ["response-evin-salt-court"]` resolves to the tick-12 row.
- Clause 2 **retains** Aru's account and restates the unresolved status already asserted at `fictional-excerpts.md:40`; "hold to" is a retention, not a truth declaration or adjudication (the map's own gloss is "the retained account").
- Clauses 3-4 are explicit **negations**, mirrored in every downstream description.
- No new account of the occasion is added; the arc still carries exactly two first-person accounts.

## Negative constructibility (adversarial attempts)

Attempted to construct each forbidden reading from every r97 record (excerpt, both JSON rows, README, map, scope lines); each attempt fails on explicit record wording:

1. **Resolution** — `:49` "both accounts stand unresolved"; `:51` "no reconciliation"; `:53` "records receipt only"; `timeline#/5` "stand unresolved"; `sources#/5` "not evidence of a resolution"; README "neither overturns, confirms, adjudicates, nor reconciles". NOT CONSTRUCTIBLE.
2. **Accusation** — `:50` "I make no accusation against Evin"; `timeline#/5` and `sources#/5` repeat it; the tick-13 description does not restate the inherited non-arrival or attach fault. NOT CONSTRUCTIBLE.
3. **Reconciliation** — `:51` "I assert no reconciliation"; README/map repeat; one-directional receipt is not a reunion/agreement. NOT CONSTRUCTIBLE.
4. **New duty** — `:51` "no new duty, and no obligation beyond this crossing"; README retains the crossing-only bound; `relations.json` is byte-identical to r96 with exactly one relation (`agreed_co_stewardship_for_this_crossing`); no new relation/entity row. NOT CONSTRUCTIBLE.
5. (Extra) **Contradiction** — `contradictions.json` is `[]` (parsed `True`); README/map state no contradiction is asserted; the two accounts name different actors/places as inherited. NOT CONSTRUCTIBLE.
6. (Extra) **Verdict/truth of either account** — no record declares either true/false; README line 9 "does not … convert either account into a verdict". NOT CONSTRUCTIBLE.

Term sweep across all r97 `.md`/`.json` files for `resolv|accus|reconcil|winner|new duty|breach|blame|fault|settle|adjudicat|verdict|alliance|continuing`: every hit is either an explicit negation, a scoping caveat, or inherited r95/r96 text (full listing in scratch `whole-claim-trace.txt` section E). No positive construct appears.

## Descriptions scoped (enumerated)

- `sources.json#/5` reliability note: "It records receipt only and is not evidence of a resolution, a reconciliation, an accusation, a winner between the accounts, a continuing duty, or an external historical fact."
- `timeline.json#/5` description: receipt report + unresolved + "no accusation, no reconciliation, no winner …, and no new duty beyond this crossing".
- Map J17 scope (line 57): span "exactly the appended acknowledgment section"; negations repeated; `entity_id` single-actor-slot caveat ("does not exclude the other participant").
- Map line 51: tick/`depends_on` "editorial encodings … not literal JSON syntax"; "encodes only Aru's receipt".
- README lines 9/11/21: "adds one receipt record"; "does not change earlier locations, resolve or create a contradiction, or convert either account into a verdict"; 17 obligations; `support_check` "lexical preflight only".
- Excerpt scope line 53 and attribution line 46: "records receipt only"; "appended after the preserved r96 text … inherited wording is unchanged".

## Inherited-row discipline (my checks)

- `timeline.json` r97[:5] == r96 parsed `True`; `sources.json` r97[:5] == r96 parsed `True`; new rows exactly `acknowledgment-aru-records` (tick 13) and `aru-acknowledgment-note`.
- `entities.json`, `relations.json`, `contradictions.json`, `inspiration-note.md`, `source-excerpt.md` byte-identical to r96 (`True` each).
- Map J01-J16 vs r96: all 16 cell diffs are the namespace column only (`r96-crossing-response:` → `r97-crossing-acknowledgment:`); J17 is the only extra row. Counts 5 entities / 1 relation / 6 events / 6 sources / 0 contradictions; census `ls -d corpus/fixtures/*/ | wc -l` = 171.

## Bounds

- The three receipts are structural/lexical only; the whole-claim reading above is my manual review and does not authenticate the fictional sources, adjudicate the fiction, or assess rights/permission.
- My receipts are pinned to `map_obligations.py` `86b52949…` (in-tree revision at my run; R1's hardening was still in flight per R4/R5); re-run under the closure revision for the round's own record.
- Everything outside the cited paths was read-only for me; this report does not extend to any other fixture or seat.

## Bottom line

**PASS** — on the frozen r97 revision (hashes above; check_bible CLEAN, support_check 17/17 / 19/19 PASS, map_obligations raw=17 mapped=17 PASS), the acknowledgment note's four clauses trace to their excerpt lines (48-51) and to `timeline.json#/5` + `sources.json#/5` with J17 anchored in-section; no resolution, accusation, reconciliation, or new-duty reading is constructible from any r97 record, and all descriptions are explicitly scoped.
