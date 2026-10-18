# V81 r99-frozen — seventh pin

Seat: V81. Read-only except this report and `.ufo/waves/round-99/seats/V81-scratch/`. Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline declaration: r99 in `LOG.md` (C1 re-freezes the existing chain 6/6; C2 adds `corpus/fixtures/r99-window-lapse/`). Question: after S1, was `r99-window-lapse` pinned? If yes, verify clean and name the seventh pin. If no, record the bound for L1.

## Poll-wait

Cadence 20s, 40 tries, 2026-10-17 22:01–22:34:56 -0300. Log: `.ufo/waves/round-99/seats/V81-scratch/poll.log`. Required pair: S1 producer report (`seats/S1*.md`) and S1 artifacts (`corpus/tools/dependency_freeze.py`, `corpus/tools/dependency-freeze-contract.json`).

- S1 report: absent on every try, including try 40 at `2026-10-17T22:34:56-0300`. `find .ufo/waves/round-99/seats -maxdepth 1 -name 'S1*.md'` printed nothing. S3 (`S3-fixture-author.md`, 22:01:40) and S4 (`S4-fixture-docs.md`, 22:03:54) landed. No stall-escape past 40. Not an all-reports poll, so SELF was not subtracted.
- Contract artifact did land and then stayed byte-stable: sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`, mtime `2026-10-17 22:08:46.248249589 -0300`, size 25987, unchanged through the deadline re-check at `2026-10-17T22:38:34-0300`.
- Tool was not stable. sha256 `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067` from 22:07:33 through try 40; rewritten at 22:38:11 to `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c` (wording-only: DIGEST-MISMATCH detail `"fixture bytes changed outside the frozen inventory"` → `"pinned-file bytes changed outside the semantic inventory"`). S1 was still editing the tool after the poll closed, and still had not filed a report.

This is not a closed S1 handoff. The pin fact below is an observation of the stable contract bytes, not a signed producer close.

## Was r99-window-lapse pinned?

No. There is no seventh pin.

Contract at sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`:

- `schema_version` 2, `payload_schema_version` 2, `revision` `337f0fa52b02626b7687eedbb2d99fab30446fe4`
- `pinned_files`: `entities.json`, `relations.json`, `timeline.json`, `sources.json`, `contradictions.json`, `README.md`, `claim-excerpt-map.md`, `fictional-excerpts.md`, `inspiration-note.md`, `source-excerpt.md`
- `self_test.expected`: 18 cases, including `markdown_tamper` (`exit` 2, `finding_ids` `['DIGEST-MISMATCH']`, `names_file` `fictional-excerpts.md`). This seat did not run `--self-test`.
- `pins` has exactly six keys, each `payload_schema_version` 2 and 10 file digests, each pin `revision` `337f0fa52b02626b7687eedbb2d99fab30446fe4`:

1. `r88-m3-maya-cluster`
2. `r94-paired-crossing`
3. `r95-crossing-aftermath`
4. `r96-crossing-response`
5. `r97-crossing-acknowledgment`
6. `r98-clerk-filing`

`r99-window-lapse` is not a key. The fixture directory exists and has all ten declared files (`claim-excerpt-map.md`, `contradictions.json`, `entities.json`, `fictional-excerpts.md`, `inspiration-note.md`, `README.md`, `relations.json`, `source-excerpt.md`, `sources.json`, `timeline.json`), so the miss is not a missing-file freeze refusal.

## Commands and observed output

From the lane root, deadline re-check `2026-10-17T22:38:34-0300`, tool sha256 `fb9bb9ff608c3333cdc3a5daba49c68c2424940d6bf4cdcdf0af80636310131c`, contract sha256 unchanged `8c2561b0…`:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
EXIT:2
```

stderr empty (0 bytes). Same finding and exit 2 were observed earlier on tool sha256 `65c1ae309385feed37b859ff78a6f28eac168888095df61c3820ed5da7b87319` at 22:02, before the contract re-freeze, and the pin set did not gain `r99-window-lapse` afterward.

Six existing pins, same tool and contract, each exit 0, stderr empty:

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r88-m3-maya-cluster
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST acf677a7085be3f6b72e3435a7e72bb1f0503359b5178dd88e433c8a9af96aae
RESULT PASS
EXIT:0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r94-paired-crossing
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 048b8ff39e4a5232641940df7f25b7e43073847f9d1c3c073d56ce015bf153ef
RESULT PASS
EXIT:0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r95-crossing-aftermath
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST 97cffd7bfe6e0c926f5b771eaf2d712dddbc25c00eb00ca6813042721120c710
RESULT PASS
EXIT:0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r96-crossing-response
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST 43911900923c110b3b67a0ad2f5f7c46c0bba2d112294f1ca4828e9da044aa7c
RESULT PASS
EXIT:0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 5/5; relations 1/1
DIGEST a28b9ea0d65ec355dd9a28098e935c15605c84fed58fdd4d3f867c706cb01d54
RESULT PASS
EXIT:0

$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 6/6; relations 1/1
DIGEST 5ecf84e19121ea1283ec99bd8104b93da182a5de28a16642727fb85caf0495f0
RESULT PASS
EXIT:0
```

Those six PASS lines match an earlier run on tool sha256 `6f81f8be…` (pre-wording rewrite). The rewrite did not change pin membership or those digests.

## Bound for L1

Do not claim `dependency_freeze` coverage of `corpus/fixtures/r99-window-lapse`. As of contract sha256 `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628` (stable 22:08:46 through 22:38:34), the pin set is the six names above and no other. There is no seventh pin to name. Verify of the lapse fixture exits 2 `UNPINNED-FIXTURE`. The new `clerk-lapse-recorded` edge and that fixture's prose are outside the freeze until a later guarded `--freeze` adds a pin. The six chain pins verify clean; that cleanliness does not extend to r99. C1's declaration asked for a 6/6 re-freeze, not a seventh pin, so this absence is consistent with the declared chain scope and is still a coverage hole for the new fixture.

Not a closed S1 verdict: the producer report never landed in 40 polls, and the tool was still being edited at 22:38:11. A pin added after this report was not verified here.

ABSENT — S1 report never landed in 40 polls; on the stable contract r99-window-lapse is not pinned (exit 2 UNPINNED-FIXTURE), so there is no seventh pin. L1 bound: freeze does not cover the lapse fixture.
