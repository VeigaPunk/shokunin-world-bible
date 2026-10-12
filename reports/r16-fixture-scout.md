# Round 16 fixture scout — same-actor/same-tick place pair

## Observed baseline (raw)

Working directory: `/home/vgpnk/Projects/prymeagnt/lore`. The existing valid-place positive-control input is `.shokunin/lore/corpus/fixtures/r12-unique-actor/`. Its raw `entities.json` has one `mira` character and unique `harbor` and `tower` place entities; raw `timeline.json` has two rows, both `entity_id: "mira"`, `tick: 7`, with `place_id` respectively `harbor` and `tower`. Both cite `courier-log`. No dependency is needed for this same-tick test.

Exact baseline CLI and observed result:

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r12-unique-actor
exit_code=1
stdout: VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'
1 violation(s); no canon changed

stderr: <empty>
```

This is a raw same-actor/same-tick/two-resolved-different-places positive control. Independent of the pair, the existing missing-place control `.shokunin/lore/corpus/fixtures/r11-dangling-place/` has `timeline[0].place_id: "unlisted"` and no entity with that ID. Its exact raw CLI result is:

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r11-dangling-place
exit_code=1
stdout: VIOLATION: timeline[0].place_id: dangling entity 'unlisted'\n1 violation(s); no canon changed\n
stderr: <empty>
```

That control does **not** itself pair the dangling place with another row for the same actor and tick.

## Paired probe (temporary raw inputs, not repository fixtures)

I copied the `r12-unique-actor` raw fixture to `/tmp/lore-r16-scout-57d_ea3f/valid/` and `/tmp/lore-r16-scout-57d_ea3f/absent/`. The valid copy retains both timeline rows unchanged. In the absent copy only the second row's `place_id` changed from `tower` to `unlisted`; all entities and all other fields are identical. Thus both are the same actor (`mira`), same tick (`7`), same rows/citations, with the one place-ID resolution status as the sole changed input. Both probes used the exact CLI form below (absolute temp path for each raw copy):

```text
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r16-scout-57d_ea3f/valid
exit_code=1
stdout: VIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'tower'\n1 violation(s); no canon changed\n
stderr: <empty>

$ python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/lore-r16-scout-57d_ea3f/absent
exit_code=1
stdout: VIOLATION: timeline[1].place_id: dangling entity 'unlisted'\nVIOLATION: timeline[1]: double-booked 'mira' at tick 7 in timeline[0] ('harbor') and 'unlisted'\n2 violation(s); no canon changed\n
stderr: <empty>
```

Raw baseline source paths for exact construction: `.shokunin/lore/corpus/fixtures/r12-unique-actor/entities.json` and `timeline.json`. Raw absent pair: `/tmp/lore-r16-scout-57d_ea3f/absent/entities.json` and `timeline.json`. These are disposable probe inputs, not committed fixture artifacts. The checker source observed at `.shokunin/lore/corpus/fixtures/check_bible.py` reports dangling place separately, then compares raw place-ID strings for occupancy; it currently emits a `double-booked` assertion involving `unlisted` despite that ID resolving to zero entities.

## Recommendation (not an implementation or verdict)

Use `r12-unique-actor` as the valid two-resolved-place control. Derive the absent-place sibling by changing only the second row's `place_id` to an ID absent from `entities.json` (e.g. `unlisted`), leaving actor, tick, source, and all other bytes/fields untouched. Expected behavior for the declared calibration claim: retain the dangling-place finding, but do not emit `double-booked` for the pair because one side is unresolved. Keep the original valid pair's `double-booked` output unchanged. This is a narrow fixture-design recommendation; it does not test ambiguous or malformed places and does not establish co-location, absence of conflict, or canon.

## Scope

Only this report was written. No checker, fixture, shared document, or commit was changed. CLI exit status 1 is expected for these deliberately diagnostic fixtures. The checker’s output is structural; it does not establish fictional-world truth.
