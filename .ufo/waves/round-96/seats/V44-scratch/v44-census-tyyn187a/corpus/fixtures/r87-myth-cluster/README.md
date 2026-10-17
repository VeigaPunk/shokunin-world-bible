# Round 87 myth cluster

A small, newly authored world-bible cluster around the Mother-Tide Gate, the Moon-Basin Vow, and a reciprocal Shellweaver–Reedwarden pledge. `entities.json`, `relations.json`, `sources.json`, and `timeline.json` use the local checker schema. The alliance has one sourced `allied_with` edge in each direction; the timeline contains an explicit `depends_on` edge.

`contradictions.json` records a place disagreement between two uniquely sourced, resolvable timeline-event references: Hara's account places the single Moon-Basin Vow at the Mother-Tide Gate, while Sen's account places that same vow at Ash-Dune Sanctuary. **The contradiction is reported, not resolved.** The checker validates the event and source references but does not judge source truth or select canon.

`lowwater-hymn-excerpt.md` and `symbolism-clause-map.md` separate invented verse from editorial interpretation. `inspiration-note.md` cites a real-world mythology parallel and keeps attribution, rights, and AI-training permission as three distinct questions.

Replay from the repository root:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster
```
