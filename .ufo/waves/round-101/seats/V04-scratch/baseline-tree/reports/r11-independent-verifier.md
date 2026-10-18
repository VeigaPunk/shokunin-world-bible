# Round 11 independent verifier (non-author)

## Scope and method

I did not edit the checker or fixture JSON. I extracted `.shokunin/lore/corpus/fixtures/check_bible.py` from baseline commit `4337c6385ed3f00f45d03eb263028ae313507006` to `/tmp/r11-baseline-check_bible.py`, then ran that extracted checker and the working checker against all 24 raw fixture directories. For the 20 fixture directories present at baseline, I also compared the baseline checker’s relative-path CLI stdout and exit code to the saved `corpus/live/runs/20261012T174305Z/<fixture>.txt` records. Stderr was captured directly on each replay. This verifies input/output structure, not fictional canon.

## Integrity and baseline replay

- Baseline checker SHA-256: `29f3bdf8132533e5e42d8fd683ac10cfcc3306b7b1851e5a98fdd57502a99a99` (13,912 bytes). Current working checker SHA-256: `f0e87e2ff88529cdd46090324415462982d80c101d3466351df55ed46e1b804f` (14,097 bytes).
- I hashed all 119 fixture JSON files immediately before and after replay. The per-file hash mappings were identical. Their sorted-path/hash manifest SHA-256 is `e2ed8ef2c6421874a744248d09dceb9a1a01d022a64d53b6caf1db8d2bbf678e`. Thus this replay did not alter any fixture JSON.
- Baseline has 20 fixtures / 99 JSON files. On the 20 baseline fixtures, the extracted baseline checker’s stdout bytes and exit status match each saved live-run record exactly; all replay stderr streams are empty. The live records do not encode stderr, so stderr evidence is from this replay.
- Comparing baseline checker against the current checker on those same 20 fixtures, all 20 had identical stdout bytes, stderr bytes, and exit status. I replayed all 24 current raw fixture directories through both checker versions; no fixture or checker was edited by this verifier.

## Paired duplicate-harbor fixtures

`r11-place-character` and `r11-character-place` have byte-identical `sources.json`, `relations.json`, `timeline.json`, and `contradictions.json`. Their `entities.json` are the same rows, with only the order of the two schema-valid `harbor` rows swapped: `place` Lantern Harbor and `character` Harbor Keeper. Both timeline files reference `harbor` as `timeline[0].place_id`. All citations/source IDs are unchanged.

The extracted baseline checker demonstrates the reported last-wins defect:

- `r11-place-character` (last row is character): `entities[2].id: duplicate entities id 'harbor'` plus `timeline[0].place_id: not a place 'harbor'` (exit 1; 2 violations).
- `r11-character-place` (last row is place): only `entities[2].id: duplicate entities id 'harbor'` (exit 1; 1 violation); the place-kind finding is absent.

The current checker reports the same local ambiguity result for both permutations: `entities[2].id: duplicate entities id 'harbor'` and `timeline[0].place_id: ambiguous place entity 'harbor'` (exit 1; 2 violations). The ambiguous-place conclusion no longer depends on duplicate-row ordering; duplicate-ID reporting remains.

## Controls and limits

- Unique-place control `r9-unique-control`: both checker versions return exit 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`.
- Unique non-place control `r11-unique-nonplace`: both return exit 1 with `timeline[0].place_id: not a place 'mira'` and one violation.
- Dangling control `r11-dangling-place`: both return exit 1 with `timeline[0].place_id: dangling entity 'unlisted'` and one violation.
- All above runs had empty stderr. These controls establish the stated narrow behavior only; they do not test every consumer of duplicated entity IDs or all malformed inputs. No claim is made about canonical entity identity, relations, timeline actor identity, occupancy, provenance, homonyms, source truth, or lore/canon.

## Conclusion

Independent replay supports the narrow round-11 claim: duplicate valid entity rows for a timeline place reference receive an ambiguity finding regardless of row order, while a unique place remains accepted, a unique non-place remains rejected, and a dangling ID remains dangling. Prior 20-fixture CLI outputs were preserved byte-for-byte against the extracted baseline checker. No checker or fixture JSON was modified by this verification.
