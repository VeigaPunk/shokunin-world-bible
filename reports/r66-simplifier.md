# Round 66 simplifier — README-only calibration decision

## Decision: NO-GO; make no README change

The smallest proposed correction would label the R59 nested-duplicate cascade as creation-time behavior and point at R60/current output. The mismatch is real, but the evidence does not establish a **material** calibration gain: the active README is explicitly divided into “Round 59” and “Round 60”; R59 says the cascade “can consequently” occur and qualifies it as missing loaded rows rather than entity absence; the immediately following R60 section specifically governs unavailable `entities.json` and says it does not call references dangling. That already supplies the current rule to a reader of the full guide. No evidence shows an operator stopped at R59 or made a wrong diagnostic/repair decision. Avoid treating a useful factual clarification as proof of material calibration improvement.

## Evidence

Present `.shokunin/lore/corpus/fixtures/README.md`, Round 59, reads: “Other files are still checked; as shown by `r59-nested-duplicate/`, unloading an entity table can consequently produce dangling-reference findings in other tables. Those are consequences of missing loaded rows, not proof that entities are absent.” It links to `../../reports/r59-executor.md` for raw candidate output and replay limits. Round 60 immediately follows and says that when `entities.json` is unavailable the checker “does not call referenced entities dangling, ambiguous, the wrong kind,” while still validating independent checks.

I ran from repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r59-nested-duplicate
```

Current result: exit 1, empty stderr, stdout exactly:

```text
VIOLATION: entities.json: duplicate object member 'source_id'; cannot load JSON
1 violation(s); no canon changed
```

By contrast, `.shokunin/lore/reports/r59-executor.md` records the creation-time run as the duplicate-member load diagnostic plus six dangling findings (`relations[0].from` mira, `relations[0].to` seal, `timeline[0].entity_id` mira, `timeline[0].place_id` harbor, `timeline[1].entity_id` mira, `timeline[1].place_id` tower), seven total, exit 1. This is historical output, not current output. `.shokunin/lore/reports/r60-executor.md` records the admitted R60 delta: for this same fixture only the duplicate-member load diagnostic remains, one total, exit 1. Thus the README’s R59-era example can be clearer, but the next section already explains the correction.

## Falsifier and limits

Evidence that readers use the R59 paragraph alone and consequently expect the six dangling messages or take the wrong repair action despite R60 would falsify this no-go materiality assessment. Conversely, a historical label would improve local precision but, absent that evidence, is not enough to claim material calibration movement. Do not rewrite old reports: R59 accurately documents its creation-time output. No candidate wording, README/checker/fixture/LOG edit, or candidate replay was made. This decision concerns documentation calibration only; it says nothing about fictional-world absence, source-text support, canon, chronology, rights, or permission.
