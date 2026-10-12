# Round 10 independent verifier (non-author)

## Scope and method

I did not edit source, fixture JSON, excerpts, or the round log. I inspected the checker and fixture artifacts, replayed all 20 fixture directories, compared the 19 pre-existing outputs with `corpus/live/runs/20261012T172227Z`, and compared the first five table prefixes in `r10-registry-witness/` against `consistent/`. This is an independent structural/output check, not proof of fictional events.

## Replay and integrity evidence

- All 19 pre-existing fixtures were run with `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<fixture>`. Each exit code and stdout byte sequence matches its corresponding saved 20261012T172227Z record. All stderr files were empty (0 bytes); the saved records encode stdout and exit but do not separately record stderr.
- The new `r10-registry-witness` fixture exited **0**, stderr empty, stdout exactly `CLEAN: schema, citations, relations, timeline; 0 violations
`.
- Checker SHA-256 is `29f3bdf8132533e5e42d8fd683ac10cfcc3306b7b1851e5a98fdd57502a99a99`; it matches the checker at baseline commit `29159c263771d425f215f275491c6614219cea59`.
- All 94 JSON files across the 19 existing fixture directories have current SHA-256 hashes matching their byte contents at baseline commit `29159c263771d425f215f275491c6614219cea59`. The five new fixture JSON SHA-256 hashes are:
  - `contradictions.json`: `37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570`
  - `entities.json`: `d5de731c11d97f199758faaec08a8115a816dc062b0f40ea4da4464e43c9c22c`
  - `relations.json`: `10f93a0ef1b241c8e704f9eaa60e72b67397a819d768f4d4626be26aafa58c37`
  - `sources.json`: `d2535b5cefcca327a7a535d8b50eede2e8cb41cbd80f9992a3f7646b528834f7`
  - `timeline.json`: `f66f43af06f5dc4c84f005a663db0a5130b048804156a8306a13e53de9ee78cc`

## Five-table prefix comparison

Parsed JSON comparison confirms the old table rows are exact semantic prefixes of the new tables, in the same order; no fields changed on any old row. Counts before → after and appended data:

| Table | Rows | Appended |
|---|---:|---|
| `sources.json` | 2 → 3 | `registrar-copy` (title `Sella’s Harbor Register carbon, year 12`, fictional handwritten register excerpt, reliability note bounds Sella to own observation/entry) |
| `entities.json` | 4 → 5 | `sella` (`character`, name `Sella`, `first_appearance: registrar-copy`), claim `Sella is a registrar at Lantern Harbor.` sourced to `registrar-copy` |
| `relations.json` | 1 → 2 | `sella` → `mira`, type `records_departure`, source `registrar-copy` |
| `timeline.json` | 2 → 3 | `registry-entry`, tick 1, entity `sella`, place `harbor`, no dependencies, description “At first bell, Sella records seeing Mira leave; at Mira’s request she leaves the registry destination blank and keeps the carbon.”, source `registrar-copy` |
| `contradictions.json` | 0 → 0 | none |

## Excerpt-to-assertion review

The new excerpt is explicitly headed “Fictional source excerpt — invented fixture text (not recovered evidence)” and says:

> At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.

Direct textual matches:

- The entity name `Sella` is matched by “I, Sella”; the entity claim that Sella is a registrar at Lantern Harbor is matched by “Sella, registrar there” in “At first bell at Lantern Harbor, I, Sella, registrar there”. This does not independently verify identity or office.
- The `records_departure` relation from Sella to Mira is matched by “recorded seeing Mira leave”. It asserts what Sella recorded/said she saw, not independent proof Mira left.
- The `registry-entry` description’s time/place match “At first bell at Lantern Harbor”; its observation match is “recorded seeing Mira leave”; destination omission and reason match “At Mira’s request, I left the registry destination blank”; keeping the carbon matches “and kept the carbon.” The fixture's wording “first bell” is not a conversion of tick 1: tick 1 is only the local sequence label, and the excerpt defines no tick mapping. The event’s tick aligns with the baseline departure's tick, but no causal ordering is inferred (no dependency edge).
- The new source's title/format and its limitation note describe the authored artifact and bound its intended in-world reliability; these metadata are not themselves validated by an independent source.

Important boundary: the excerpt does **not** say Mira actually went to North Tower, and cannot support or independently confirm that claim. That destination appears in unchanged baseline `courier-log` assertions only. The blank registry destination is an omission, not an assertion of an alternative destination or a contradiction. The new excerpt is authored together with this fixture; a textual match shows internal correspondence only, not source recovery, witness honesty/access, independent corroboration, event truth, or canon. Checker success establishes structural/schema/citation-ID/timeline validity only; it does not validate prose entailment or truth.

## Verifier conclusion

The replay, preservation, prefix, and bounded textual-correspondence checks passed. The added material is specific and connected (an identified registrar records Mira’s departure while leaving destination blank at her request), rather than merely extra rows. This provides evidence for the narrow **depth** claim of an additional documented perspective, subject to the authored-fiction limits above. No evidence here warrants claiming independent historical truth or canon verification. I found no coverage/calibration regression in the checker or prior fixtures; this replay is not a broad proof about all possible inputs.
