# Round 72 independent verifier

## Pinned baseline and whole-corpus comparison

Pinned archive: `274906575c3462aabb9f27752513e7c588c511a5` (also the current HEAD). I extracted its `.shokunin/lore/corpus/fixtures/` tree to `/tmp/lore-r72-verify/base` and compared raw file bytes with the candidate worktree. The baseline has 130 immediate fixture directories and 709 files total (707 fixture-internal files, plus `README.md` and `check_bible.py`). Every baseline path remains present. Of those paths, 708/709 are byte-identical; the only changed prior path is `README.md` (baseline 57,314 bytes; candidate 57,937 bytes). The candidate adds 16 paths, all inside `r72-vela-slate-claim/`. The checker is byte-identical at both pins: SHA-256 `88c9b1d003f51738b9fa9b2921a939f94e7ebbc2369c4445a947b282cfed9b81`.

## Raw regression replay

For each of the 130 baseline fixture directories, I ran the root-relative CLI from each respective repository root with identical argv:

```text
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture-directory>
```

I captured process exit status, stdout bytes, and stderr bytes without normalization. **130/130 raw tuples match byte-for-byte**; mismatches: none. Baseline outcomes: 25 exit 0, 105 exit 1. The sorted immediate-directory manifest SHA-256 is `d0f6fda324abf8818ecce42609df07cb3729b3f4c4c7f8735d0a568352d1b12a`. Replay tuples are in `/tmp/lore-r72-verify/replays.json` for audit.

The new candidate command exits **0**, stdout bytes decode to `CLEAN: schema, citations, relations, timeline; 0 violations
`, stderr is empty. This is structural checker evidence only; the checker does not parse the excerpt or map.

## r43 clone and append-only audit

The candidate has all 14/14 files from `r43-jorin-vela-sighting`, unchanged byte-for-byte except for the declared additions in `sources.json` and `entities.json`; it adds only `vela-slate-note-excerpt.md` and `vela-slate-clause-map.md` to the clone. The source array is an exact prefix of the prior array plus one row, `vela-slate-note`. Every prior entity row is unchanged except `vela`: all its non-claim fields and prior claims are unchanged, with exactly one appended claim citing `vela-slate-note`. The five tables are accounted for: `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical to r43; `sources.json` has one appended row; `entities.json` has one appended Vela claim. No slate entity, event, dependency, relation, or contradiction was added.

## Excerpt, claim, map, and pointer review

The excerpt says: “I leaned close to the slate and could read, ‘KEEP THE EAST GATE CLEAR.’ The cramped letters made me wonder if whoever wrote them had been in a hurry. I could not tell who wrote them.” The sole new Vela claim preserves the attribution and observation/inference distinction: Vela reports reading the wording, tentatively infers that the unknown writer might have been hurried, and says she could not identify the writer. The source row identifies a newly authored, fictional, unverified first-person report and explicitly disclaims an authenticated slate or writer.

The map's three excerpt spans match the excerpt literally, including the nested curly double quotation marks. It labels claim text as paraphrase and points to the new claim at `entities.json` `/6/claims/1`, its `source_id` at `/6/claims/1/source_id`, and the cited source at `sources.json` `/6` (`vela-slate-note`). Each span is present verbatim in both excerpt and map. The claim/map do not identify a writer or assert artifact authentication. No new date, Bell-7 reference, place assignment, or sequence is introduced; there is no timeline pointer because there is no new event. The inherited timeline remains unchanged. README changed from baseline as part of round documentation; this verifier did not edit it or any fixture.

## Limits

This review verifies file preservation, old CLI behavior, structural cleanliness, and the literal excerpt-to-claim/map attribution pointers. It does not establish the fictional report's truth, slate existence/text/placement/authorship, quote-to-claim entailment beyond the stated manual correspondence, narrative depth, chronology, canon, real-world rights, or game mechanics. A clean checker result proves none of those. No axis verdict is made here.
