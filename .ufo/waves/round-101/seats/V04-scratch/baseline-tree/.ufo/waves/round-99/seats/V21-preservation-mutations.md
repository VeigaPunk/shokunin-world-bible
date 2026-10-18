# V21 preservation-mutations — round 99 seat report

- Seat: V21 (verifier). Lane repo `/home/vgpnk/Projects/shokunin/lore-shokunin`. Baseline r98 closure `4265df5`. Commands from the lane root with `python3`.
- Written: this report (`.ufo/waves/round-99/seats/V21-preservation-mutations.md`) plus scratch under `.ufo/waves/round-99/seats/V21-scratch/` (poll log only). No corpus writes, no commits, no network, no nested agents.
- Assigned matrix, not run: span break → support fail; row drop → map fail; claims rename → schema_drift; claims+row deletion → inventory_mismatch; edge drop → REDUCTION-DETECTED; prose word edit → DIGEST-MISMATCH. Those exits were not observed. The freeze half cannot bind without a delivered `r99-window-lapse` pin.

## Poll-wait

Producer-artifact poll, 20 s cadence, 40-try budget (~13 min). Gate required all five producer reports (`S1-freeze-hygiene.md`, `S2-tools-docs.md`, `S3-fixture-author.md`, `S4-fixture-docs.md`, `S5-knowledge-notes.md`), both S5 knowledge files, and a contract pin `r99-window-lapse` with `payload_schema_version` 2 and ten file digests. Endgame convention does not apply: this poll waits on producers and the pin, not on other verifier reports.

```
POLL try=1 t=20s 22:04:05 tool=1728ed892442 con=153ebc5b2092 map=d2fe20e581d1 readme=b93209417a91 contract_rc=3 map_rc=0 missing=[ S1-freeze-hygiene.md S2-tools-docs.md S5-knowledge-notes.md r99-gate-blind-spot-table.md r99-lapse-scope-note.md]
  contract: schema=1 pins=6 r99=no r99files=0 r99psv=None cases=17 md_tamper=False
  map: **Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.
…
POLL try=40 t=800s 22:17:06 tool=6f81f8be1974 con=8c2561b043c2 map=d2fe20e581d1 readme=b93209417a91 contract_rc=3 map_rc=0 missing=[ S1-freeze-hygiene.md S2-tools-docs.md S5-knowledge-notes.md r99-gate-blind-spot-table.md r99-lapse-scope-note.md]
  contract: schema=2 pins=6 r99=no r99files=0 r99psv=None cases=18 md_tamper=True
  map: **Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.
POLL_EXHAUSTED try=40 missing=[ S1-freeze-hygiene.md S2-tools-docs.md S5-knowledge-notes.md r99-gate-blind-spot-table.md r99-lapse-scope-note.md] contract_rc=3 map_rc=0
```

Full cadence is `.ufo/waves/round-99/seats/V21-scratch/poll.log`. From try 16 (22:09:05) through try 40 the contract sha prefix `8c2561b043c2`, tool prefix `6f81f8be1974`, and map prefix `d2fe20e581d1` did not move, and `r99=no` on every try. No stability window opened. No mutation copy was built.

## Confirmation after the budget (22:29:50)

Twelve minutes after `POLL_EXHAUSTED`, the same absences still held. Quoted observation:

```
$ python3 - << 'PY'   # lane root; hashes of delivered files
contract sha 8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628
tool sha 6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067
schema 2 payload 2 pins ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing']
False
cases 18 markdown_tamper True
fixture exists True files ['README.md', 'claim-excerpt-map.md', 'contradictions.json', 'entities.json', 'fictional-excerpts.md', 'inspiration-note.md', 'relations.json', 'source-excerpt.md', 'sources.json', 'timeline.json']
```

`False` is `'r99-window-lapse' in contract["pins"]`. Seat reports present at confirmation included `S3-fixture-author.md` (5069 bytes, 22:01) and `S4-fixture-docs.md` (9303 bytes, 22:03). No `S1-*.md`, `S2-*.md`, or `S5-*.md` under `.ufo/waves/round-99/seats/`. `corpus/knowledge/r99-gate-blind-spot-table.md` and `corpus/knowledge/r99-lapse-scope-note.md`: `No such file or directory`. `S2-scratch/` empty (mtime 22:00). `S1-scratch/before/` holds a mirror copied at 22:08; that is not a report and not an r99 pin.

Read-only verify of the canonical fixture (no mutation, no corpus write):

```
$ python3 corpus/tools/dependency_freeze.py corpus/fixtures/r99-window-lapse
FINDING UNPINNED-FIXTURE: no pin for 'r99-window-lapse' in corpus/tools/dependency-freeze-contract.json (pinned: ['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'r97-crossing-acknowledgment', 'r98-clerk-filing'])
RESULT ERROR
EXIT:2
```

That exit is `UNPINNED-FIXTURE`, not `REDUCTION-DETECTED` and not `DIGEST-MISMATCH`. It is evidence the pin is absent, not a substitute for the assigned matrix.

## What was on disk, and why it was not measured

Present and stable inside the poll window, but not sufficient for the assigned matrix:

- `corpus/fixtures/r99-window-lapse/` (ten files). Map declaration, stable from try 1: `**Expected inventory:** 21 JSON facts; 2 editorial rows; 23 total mapped rows; 19 distinct excerpt anchors.` Last JSON-facts row is J21 `timeline.json#/7` (`clerk-lapse-note`).
- `corpus/tools/dependency_freeze.py` sha `6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067` (moved during tries 1–12, then stable). Contract sha `8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628`: schema 2, six pins, each with ten file digests on the inherited chain, `self_test.expected` length 18 including `markdown_tamper`. No seventh pin.

The edge-drop and prose-word mutations are defined against the delivered r99 pin. Running them on a copy while the canonical fixture is `UNPINNED-FIXTURE` would measure a plan (a pin that has not been written), which this seat is forbidden to do. The span / row / claims half was not run either: the assigned deliverable is one accumulated matrix with quoted exits, and a partial matrix would not be that deliverable.

## Bottom line

**ABSENT** — after 40 polls (22:04–22:17) and a 22:29 confirmation, `S1-freeze-hygiene.md`, `S2-tools-docs.md`, `S5-knowledge-notes.md`, both r99 knowledge notes, and the `r99-window-lapse` pin were still absent; canonical freeze verify exited 2 `UNPINNED-FIXTURE`; the preservation mutation matrix was not run.
