# r89 F2: dangling from_holder is the first stop

Run from the lane root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-f2-dangling-from
```

Record [0] is a valid transfer. Record [1] has a nonempty from_holder ID absent from entities.json; records [2] and [3] are individually valid and continuous with each other. The expected first-stop disclosure names `dangling holder from_holder 'r89-f2-missing-from'` at `entities[3].provenance[1]` on records [1], [2], and [3]. No chain-break or tick-order comparison is reported after the stop; this is input-structure coverage, not a custody or canon assertion. The four provenance records are fictional checker inputs; no story or real-world fact is asserted.
