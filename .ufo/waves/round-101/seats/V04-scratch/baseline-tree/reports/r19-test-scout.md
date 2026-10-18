# Round 19 test scout — baseline replay and raw tick probes

Role: read-only test scout. I wrote only this report. No checker, fixture, shared document, or commit was changed. The two probes were made in `/tmp` from `r18-unique-pair`; each copied the five JSON inputs and changed only both timeline `tick` values. Probe scratch paths are recorded below; they are not repository fixtures.

## Raw observations

### Saved-output replay

Re-ran the 45 fixture commands represented in `.shokunin/lore/corpus/live/runs/20261012T185657Z/` against the working-tree checker and compared exit code and stdout to each saved transcript; stderr was captured separately. **45/45** had identical exit code and stdout, and empty stderr. No differences were observed. This is replay agreement with the saved outputs; it is not a separately established comparison against another checker revision.

### Paired tick probe

Both cases were copied from `r18-unique-pair`, whose two timeline rows use the same actor (`mira`) and distinct known places (`tower`, `harbor`). The only input-file difference between the probe cases is `timeline.json`; the only field changes within it are both `tick` values. Descriptions, citations, entities, relations, dependencies, and other fields remain as in the source fixture.

| Probe (scratch path) | Exit | Exact stdout findings (without `VIOLATION:` prefix) | Stderr |
|---|---:|---|---|
| negative pair (`/tmp/lore-r19-probe-jusc2ajs/negative-pair`), both ticks `-1` | 1 | `timeline[0].tick: must be nonnegative`; `timeline[1].tick: must be nonnegative`; `timeline[1]: double-booked 'mira' at tick -1 in timeline[0] ('tower') and 'harbor'`; `3 violation(s); no canon changed` | empty |
| valid control (`/tmp/lore-r19-probe-jusc2ajs/valid-control`), both ticks `9` | 1 | `timeline[1]: double-booked 'mira' at tick 9 in timeline[0] ('tower') and 'harbor'`; `1 violation(s); no canon changed` | empty |

The raw outputs confirm that the checker emits a double-booking finding for the negative-tick pair, and also emits one for the nonnegative control. The checker source at `HEAD` equals the declared baseline commit `9ee1e6eb18b7813a6fe2eda175d891b5d7f55308`; its `check_bible.py` SHA-256 matched the extracted baseline (`8ad6848022410e8c8519e0fffde55c4e96bab594fdc6895574c0eb7efe11997e`).

## Recommendations (not observations)

- The declared narrow calibration candidate is supported by this paired probe: consider retaining each negative-tick diagnostic and raw row while preventing that row from participating in the occupied-slot comparison/store. This would avoid reporting an asserted *definite* double-booking at an invalid numeric tick, without saying there was no in-world conflict.
- Preserve the nonnegative control finding. Probe valid-known-known rows before/after an invalid-tick row in both orders before claiming the narrower change preserves comparison across invalid rows.
- The replay establishes only exact agreement for these 45 saved transcripts on the current checker. It does not establish hidden-conflict behavior or source-text truth. Do not treat fixture IDs/citations as narrative attestation.
