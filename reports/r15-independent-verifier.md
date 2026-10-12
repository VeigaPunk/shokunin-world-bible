# Round 15 independent verifier — non-author evidence

Scope: independently hashed/replayed existing and new fixtures and reviewed the excerpt-to-row mapping. No source or fixture files were edited. Checks establish byte/structural consistency only, not truth, canon, game mechanics, or independent corroboration.

## Baseline and inherited-artifact evidence

Baseline commit: `2c5b2f1c13f42f4c42c31ff07773c61043be43a7`. Its checker was extracted to `/tmp/lore-r15-baseline-checker.py`; SHA-256 `eaa2f1178c4571d8a911cb3d880068216614766d8f35922cb78d6584179dad80`. Active checker has the same SHA-256. The baseline commit has 139 fixture JSON inputs; compared each current old-fixture relative path and SHA-256 against `git show <baseline>:<path>`: **139/139 identical**. The old fixture set also remains 28 cases.

Replayed 28 old cases, using the extracted baseline checker and repo-relative arguments. Compared process exit code, stdout bytes, stderr bytes to each corresponding saved record under `corpus/live/runs/20261012T180109Z/` (saved stdout includes the final newline). **28/28 exact matches**; stderr empty in every case; outcomes: 6 exit 0, 22 exit 1. Replayed again with active checker: all 28 outputs also match the extracted-checker replay byte-for-byte. The newly added fixture makes 29 current cases. Its active-checker invocation was:

```
$ python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r15-carbon-followup
exit_code=0
stdout: CLEAN: schema, citations, relations, timeline; 0 violations
stderr: <empty>
```

New fixture JSON SHA-256 (raw-file hashes):
- `contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
- `entities.json`: `d5de731c11d97f199758faaec08a8115a816dc062b0f40ea4da4464e43c9c22c`
- `relations.json`: `10f93a0ef1b241c8e704f9eaa60e72b67397a819d768f4d4626be26aafa58c37`
- `sources.json`: `ad4b10031590b9a12498a4f70c21f2d94864144206034ddcf0ea3c62a9c304fe`
- `timeline.json`: `2a5a759bed30e15cd3ec4e3a3eb823f9a54a04c0698d0fb577212f0b49eae1f3`
- `registrar-copy-excerpt.md`: `0e5dfba243dc76e4130ce7587f25c360fb3ecb0573987baf22aade787ee028f5`
- `sella-carbon-followup-excerpt.md`: `a779cba3fea36b9eb06bef4d4f28b1ff4cc9ae8df03ab1047f4ec75a5026c961`

The new fixture’s `contradictions.json`, `entities.json`, and `relations.json` are byte-identical to r10. Parsed JSON confirms all 3 inherited source rows are an unchanged prefix in `sources.json`, and all 3 inherited timeline rows unchanged prefix in `timeline.json`; exactly one source and one event were appended. The original and copied `registrar-copy-excerpt.md` are byte-identical (hash above). No inherited r10 JSON row was altered.

I captured a pre/post hash snapshot of the active checker, all 144 fixture JSON files, and both new-fixture excerpt files around the CLI replay; hashes were identical. This verifier created only this report.

## Exact source/event and excerpt clause review

New source `sella-carbon-followup` is labeled “fictional private note”; its reliability note says “Newly authored fictional text for this fixture, not recovered; Sella reports her own later observation and uncertainty, not omniscient truth.” This correctly bounds evidentiary status. The new excerpt labels itself “Fictional private-note excerpt — newly authored for this fixture (not recovered evidence)” and identifies that source ID.

Exact excerpt:

> Later, at Lantern Harbor, I looked again at the carbon I had kept. I saw a blurred blue oval mark on it. I cannot identify where the mark came from, and I do not attribute it to Mira’s Blue Seal.

The single new timeline row is `carbon-followup`: `entity_id=sella`, `place_id=harbor`, `tick=3`, `depends_on=["registry-entry"]`, source `sella-carbon-followup`. Its description: “Sella reports looking again at the carbon she kept and observing a blurred blue oval mark whose origin she cannot identify; she does not attribute it to Mira’s Blue Seal.”

Clause-to-field map (manual semantic review; checker does not parse prose):

| Excerpt clause | Event/source mapping | Limit |
|---|---|---|
| “Later, at Lantern Harbor, I looked again at the carbon I had kept.” | `carbon-followup` places Sella at `harbor`, reports looking again at the carbon she kept; dependency on `registry-entry` supplies ordering, and the source ID is `sella-carbon-followup`. | This is the authorial account by Sella; dependency is fixture sequencing, not proof/corroboration of custody. “Later” asserts no duration. Tick 3 is local event order only. |
| “I saw a blurred blue oval mark on it.” | Event reports Sella’s observation of a blurred blue oval mark; source is the stated private note. | A report, not objective verification; no maker, time of marking, or independent witness. |
| “I cannot identify where the mark came from” | Event repeats Sella’s uncertainty about origin. | Reports her limit, not universal unknowability. |
| “I do not attribute it to Mira’s Blue Seal.” | Event explicitly says she does not attribute the mark to Mira’s Blue Seal. | Does not establish or refute a causal connection; do not describe it as a seal-mark or Mira’s mark. |

## Scope and limits

All inherited rows are preserved; new row citations resolve, and ordering dependency is from tick 3 to `registry-entry` tick 1. Existing arrival at tick 2 is not a dependency, so this does not claim the inspection follows Mira’s arrival. Tick 3 does not convert “first bell” to a numeric time, establish elapsed time, or establish a causal relationship. No added text claims mark origin, motive, destination, objective mark authenticity, source recovery, corroboration, or truth. The mark’s blue color can evoke the Blue Seal motif; the explicit non-attribution is important and is present in both note and event. The excerpt and event are one authored account, not two witnesses. Clean CLI means schema/reference/timeline checks passed, not prose entailment or lore truth.

