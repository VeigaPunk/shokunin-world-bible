# Round 87 provenance probe — entry shape

A minimal authored micro-bible exercising the provenance entry gate in `check_bible.py`. `seal` (item) carries a present-but-empty `provenance` list, `lamp` (item) carries a non-array `provenance` value, and `rope` (item) carries a would-be chain break while its identity `rope` is duplicated by a second row.

The duplicate rows and the malformed value are test scaffolding, not a choice between identities or evidence about custody. Source IDs resolve only to supplied in-world records and do not establish source support or canon.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-probe-entry-shape
```

Expected: two findings — `entities[6].id: duplicate entities id 'rope'` and `entities[4].provenance: expected array` — exit 1. The empty list on `seal` produces no finding, and the duplicated `rope` identity disables chain eligibility for both `rope` rows, so the would-be break at `rope` record 2 is not compared.

---

**r88 revision note** (commit at r88 closure; measured on the delivered tree: exit 1, 8 findings): delivered checker now reports 8 findings (non-holder stops now disclose their first cause).
