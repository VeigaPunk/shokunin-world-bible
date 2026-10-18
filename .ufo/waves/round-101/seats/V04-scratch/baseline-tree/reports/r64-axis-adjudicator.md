# Round 64 — independent Sol axis adjudication

**Verdict: REJECT before implementation.** The proposed raw-invalid-ID “cannot assess” finding has no demonstrated material improvement in repair actionability over the current row-local schema error **plus each referencing field’s dangling pointer**. No checker candidate exists; this is a no-change judgment, not a candidate validation or a claim that any hypothetical implementation works. Seven scouts recommended NO-GO; the scribe proposed only a conditional probe. The non-author reviewer independently recommended NO-GO before executor, and the independent verifier confirmed the old corpus and current behavior. I read `LOG.md`, all eight r64 scout leaves, the reviewer and verifier, and the r26/r56/r60 adjudications; I also reproduced the checks below independently.

## Independent pinned baseline and raw replay

I extracted pinned r63 **report commit `3367b22043c55a2e207ca446b916b462e66a0791`** using `git archive` into `/tmp/r64-sol-archive-4f0c4ng6`, outside the repository. Inventories of the *full* `.shokunin/lore/corpus` compared relative paths and actual raw file bytes: **1,298/1,298 files identical**, no added/removed/changed files (the recursive directory-inclusive inventory contains 1,455 entries in each root, including 157 directories). All **623/623 old fixture JSON** paths and bytes match, and all **125/125 old fixture directory names** match. The checker bytes match too; no active checker, fixture README, fixture JSON, or other corpus delta was found.

I separately invoked every one of the 125 old fixture names under *each* root using the same repo-root-relative command form, `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<name>`, with the archived process run from the archived root. Raw stdout bytes, raw stderr bytes and exit status were captured separately: **125/125 exact tuples, zero mismatches**. This proves no-change preservation of those old cases, not a new policy’s behavior. The independent verifier reports the same full-file/fixture/replay counts from its own archive.

## Matched current-checker probes (not candidate output)

Outside the repo, I copied `fixtures/consistent/` into seven temporary directories under `/tmp/r64-sol-probes-n04d76ad`; `sources.json`, `relations.json`, `timeline.json`, and `contradictions.json` remained byte-identical in every copy. Only `entities.json` varied. The unchanged checker was invoked with each absolute temporary fixture path. Every stderr was empty. The references to `mira` are unchanged: `relations[0].from`, `timeline[0].entity_id`, and `timeline[1].entity_id`.

| Entities variant | Exit | Raw stdout distinction |
| --- | ---: | --- |
| Valid referenced `mira` | 0 | `CLEAN: schema, citations, relations, timeline; 0 violations` |
| Referenced `mira` absent, remaining valid rows retained | 1 | Three `dangling entity 'mira'` lines at the relation and two timeline fields; `3 violation(s); no canon changed` |
| Referenced `mira` row has usable `id` but required `name` omitted | 1 | `entities[0].name: required nonempty str` **and the same three field-local dangling lines**; summary 4 |
| Rejected `mira` row has no `id` (other fields retained) | 1 | `entities[0].id: required nonempty str` **and those same three dangling lines**; summary 4 |
| Valid duplicate `mira` row | 1 | `entities[4].id: duplicate entities id 'mira'`; relation `ambiguous entity 'mira'`; two timeline `ambiguous actor entity 'mira'`; summary 4 |
| Loaded `[]` | 1 | Six dangling findings: relation `from`/`to`, both timeline `entity_id`/`place_id`; summary 6 |
| Whole-file invalid `{bad json` | 1 | `entities.json: cannot load JSON: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)` alone; summary 1 |

Each line above is current output, not an expected or observed proposed diagnostic. In particular **referenced absence does yield three reference-specific dangling findings**. The verifier’s phrase “An absent ID produces no reference-specific diagnostic” referred to its *unreferenced* malformed `ghost` row, not the referenced-`mira` absent control. The valid duplicate remains ambiguous, and loaded-empty is not conflated with whole-file unavailable. The row-invalid result already locates the required-field defect and all affected reference sites. These are supplied-input/index findings only.

## Materiality, prior boundary, and axes

The checker admits a row to its entity index only after all required fields pass. The new suggestion would use a **second index of raw IDs from rejected rows** to replace or supplement `dangling` at matching references with “cannot assess … matching entity row invalid.” A raw ID token in a rejected row cannot establish a valid unique entity or serve as kind, holder, place, faction, or occupancy witness. Without the second index, the current “dangling” correctly states absence from the admitted index; it does not assert anything about a fictional world. The proposed wording is plausibly more explicit about a raw match, but these probes show no changed repair decision: fix the row’s named defect or correct/add a valid target, while the current dangling lines identify exactly which references require resolution. Replacement risks losing those useful pointers or hiding a missing valid target when a malformed row shares its ID; emitting both could duplicate noise. Those are *prospective risks*, not measured harms from a nonexistent candidate.

R26’s malformed duplicate retained a raw `seal` ID but did **not** become an admitted second identity, unlike its valid-duplicate pair. R56 rejected technically accurate additional local ambiguity findings because the existing duplicate-ID error and withheld chain already supported the repair decision; extra precision alone was insufficient. R60 admitted a measured unavailable-versus-loaded distinction and expressly kept loaded arrays available over retained valid rows even when a malformed row is rejected. R64 reopens that explicitly bounded row-filter case; it is not implied by r60. Neither prior art nor the current probes demonstrates an operator action improved by the new status, and no candidate output, regression cascade, or operator exercise exists.

| Axis | Judgment | Basis |
| --- | --- | --- |
| **Depth** | **Unchanged** | No new structural inference, checker behavior, or candidate rule was admitted. |
| **Coverage** | **Unchanged** | No new admitted cases, checker paths, or fixtures; the 125 old raw tuples and 623 JSON paths remain fixed. |
| **Calibration** | **Unchanged; material improvement unproved** | Raw-ID nuance is conceivable, but current row schema error and dangling reference pointers remain actionable; a second raw-ID index adds identity ambiguity and may obscure them. No candidate harm is asserted as observed. |

**Admission requires a material gain on at least one axis with none harmed; that bar is not met. REJECT the hypothesis for this round and leave the active checker/corpus untouched.** Revisit only after a concrete, matched repair exercise shows current schema-plus-dangling misdirects action and a candidate reference-local status improves it, preserving row errors, genuinely absent-ID dangling, valid-duplicate ambiguity, unavailable/loaded distinctions, and independent source/tick/dependency findings. This report makes no source-prose, world-truth, chronology, canon, rights, license, or permission judgment. No push, merge, or commit by this adjudicator.
