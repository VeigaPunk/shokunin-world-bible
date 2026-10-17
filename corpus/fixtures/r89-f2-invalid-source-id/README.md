# r89 F2: unknown source_id is the first stop

Run from the lane root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-f2-invalid-source-id
```

Record [0] is a valid transfer. Record [1] has a nonempty source_id that is absent from sources.json; records [2] and [3] are individually valid and continuous with each other. The expected first-stop disclosure names `source reference 'r89-f2-unknown-source' absent from raw sources and absent from the resolved index` at `entities[3].provenance[1]` on records [1], [2], and [3]. No chain-break or tick-order comparison is reported after the stop; this probes an unresolved source ID, not source-text support or canon. The four provenance records are fictional checker inputs; no story or real-world fact is asserted.
