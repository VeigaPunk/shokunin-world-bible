# V10 c2-checker — round 99

Seat: V10 (verifier, c2-checker). Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). All commands from the lane root with `python3`. Leaf seat: no nested agents, no commits, no pushes, no network. Exclusive writes: this report (absolute path) and `.ufo/waves/round-99/seats/V10-scratch/` (`poll.log`, `audit.py.txt`). Nothing else written.

Poll target: S3. Subject: `corpus/fixtures/r99-window-lapse/` on the delivered revision, plus r98 still CLEAN.

## Poll

Try 1 at `2026-10-17T22:02:24-03:00` (recorded in `V10-scratch/poll.log`). Both required artifacts already existed; no sleep, no plan verified.

- `corpus/fixtures/r99-window-lapse/` present (ten files; S3-owned JSON/excerpt mtimes `2026-10-17 22:01:13`).
- `.ufo/waves/round-99/seats/S3-fixture-author.md` present, 5069 bytes, mtime `2026-10-17 22:01:40`. Read in full. It is a finished producer report (commands, observed `CLEAN` / `EXIT:0`, byte-prefix checks, trailing `PASS:` line), not a plan.

## check_bible

Re-run after S4 rewrote `README.md` and `claim-excerpt-map.md` (those files are outside this seat's checklist; JSON tables did not move — hashes below match the pre-rewrite run).

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r99-window-lapse ; echo EXIT-R99=$?
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT-R99=0
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing ; echo EXIT-R98=$?
CLEAN: schema, citations, relations, timeline; 0 violations
EXIT-R98=0
```

Captured subprocess (same commands, after the S4 rewrite): r99 `rc=0` stdout `'CLEAN: schema, citations, relations, timeline; 0 violations\n'` stderr `''`; r98 identical. Earlier independent capture in `V10-scratch/audit.py.txt` matches.

## Counts

```
$ python3 -c "import json; from pathlib import Path
d=Path('corpus/fixtures/r99-window-lapse')
[print(t, len(json.loads((d/f'{t}.json').read_text()))) for t in ('entities','relations','timeline','sources','contradictions')]"
entities 6
relations 1
timeline 8
sources 8
contradictions 0
```

Declared 6 entities / 1 relation / 8 events / 8 sources. Contradictions remain `[]` (not part of the count claim; recorded so the empty ledger is visible). r98 worktree, same command: entities 6, relations 1, timeline 7, sources 7, contradictions 0. r98 worktree bytes of all ten files equal `git show 4265df5:corpus/fixtures/r98-clerk-filing/<f>` (ten `identical_to_baseline=True`).

## clerk-lapse-recorded

Parsed last timeline row (only row with that id; `lapse_count 1`):

```
{
  "id": "clerk-lapse-recorded",
  "tick": 15,
  "entity_id": "clerk-maren",
  "place_id": "chalk-stair",
  "depends_on": ["clerk-filing-open"],
  "description": "At the Chalk Stair at tick 15, the clerk records that the crossing-window named in the original minute has closed; the agreement was unfulfilled; no claim was lodged; the matter stands as a historical open entry.",
  "source_id": "clerk-lapse-note"
}
```

`tick == 15` and `depends_on == ["clerk-filing-open"]` both True. Predecessor `clerk-filing-open` is present at tick 14 (strictly earlier, so the dependency is not an inversion). Actor `clerk-maren` and place `chalk-stair` are existing entity ids; source `clerk-lapse-note` is the appended eighth source (`Maren's Chalk Stair Lapse Note`).

Event chain observed: ticks 9, 9, 10, 11, 12, 13, 14, 15. The new edge is the only addition to `depends_on` relative to the r98 prefix.

## Dangling / duplicates

Id spaces: entities `aru, evin, quiet-rise, salt-court, chalk-stair, clerk-maren`; sources the seven inherited ids plus `clerk-lapse-note`; events the seven inherited ids plus `clerk-lapse-recorded`.

```
dups {'entities': [], 'sources': [], 'events': []}
dangling []
```

Walk covered `first_appearance`, every claim `source_id`, both relation endpoints (`from`/`to`) and relation `source_id`, every timeline `entity_id` / `place_id` / `source_id`, and every `depends_on` target. Relation remains the single inherited row (`aru` → `evin`, `agreed_co_stewardship_for_this_crossing`, `crossing-minute`). No new entity or claim: `claims_total 6`.

Parsed prefix versus worktree r98 and versus `4265df5` blobs: `entities` equal (not merely prefix), `relations` equal, `contradictions` equal, `timeline[:-1]` equal, `sources[:-1]` equal. `fictional-excerpts.md` startswith the r98 blob and the blob plus a newline (`excerpt_prefix_is_blob True`, appended 927 bytes). The seven files S3 left as copies (`README.md`, `claim-excerpt-map.md`, `contradictions.json`, `entities.json`, `inspiration-note.md`, `relations.json`, `source-excerpt.md`) were byte-identical to `4265df5` at the S3-settled moment (measured before S4's rewrite). After S4, only `README.md` and `claim-excerpt-map.md` moved; the five JSON tables did not.

## Stability

JSON/excerpt hashes unchanged across an 8 s window that caught S4 rewriting the two docs, and unchanged again on the post-rewrite re-check (`2026-10-17T22:04:16-03:00`):

```
2cdb9fda5baae1a496b31c004a7e0a9345ac580b257da0d9a04c045214c4c069  timeline.json
8c215b38dc02400910ff935eab46ecf82b0381b63a75d092b03bd601a9915f15  sources.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
fefebaf93d148dbe3304ef473602c91287b45b52841638c4348f0f065d32002d  fictional-excerpts.md
```

`timeline.json` / `sources.json` / `fictional-excerpts.md` mtime stayed `22:01:13`. S3 report bytes were not re-read after 22:01:40; the checker verdict is on the fixture bytes, not on S3's prose.

## Scope note (not a failure of this seat's checklist)

`check_bible` CLEAN is structural: schema, citation-id resolution, relation endpoints, timeline order. It does not prove excerpt entailment or canon. The event description itself does not contain the words resolution / blame / reconciliation; the appended excerpt and the source reliability note use those words only as negations (`I record no resolution, assign no blame, and reconcile nothing.` / `It asserts no resolution, no blame, and no reconciliation`). That reading is quoted text, not a semantic proof.

S4's rewrite is outside this seat. Observed, not judged: after 22:02:39 the map's expected-inventory line reads `21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors`, and a `J21` row points at `timeline.json#/7` / `clerk-lapse-note`. This seat did not run `map_obligations` or a census.

## Bottom line

PASS — r99-window-lapse `check_bible` CLEAN exit 0; counts 6/1/8/8; `clerk-lapse-recorded` tick 15 `depends_on ["clerk-filing-open"]`; no dangling refs and no duplicate entity/source/event ids; r98 still CLEAN exit 0.
