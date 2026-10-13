# Round 44 fixture scout — actor ontology and probe

## Finding / recommendation: no-go on a character-only guard

There is a real, minimal false-positive *candidate*: a controlled copy of `consistent/` with only `timeline[0].entity_id` changed from unique character `mira` to unique place `harbor` runs CLEAN (observed command below). But that alone does not show a defect. The checker’s data contract deliberately calls this generic `entity_id`, not `character_id`; no source establishes a character-only actor ontology. Thus the proposed “not a character” diagnostic would invent a convention and can reject valid place/faction/item-subject events. Do not implement without a narrower documented semantic scope.

## Evidence

- `.shokunin/lore/corpus/fixtures/check_bible.py:7-13`: allowed kinds include character/place/faction/item; timeline requires string `entity_id` and `place_id`; no actor kind constraint in schema.
- `check_bible.py:229-250`: timeline loop verifies string fields, actor presence/uniqueness, place kind, then occupancy keyed by raw `(entity_id,tick)`. It never checks the resolved actor kind. A clean baseline first event `mira` -> `harbor` is accepted.
- `.shokunin/lore/corpus/fixtures/README.md:30-35`: prose says “A character cannot occupy different places at the same tick”; that documents the occupancy rule, not a universal character-only type rule for every timeline subject.
- README:243-265 documents r12 actor identity/occupancy, still by actor ID; ambiguity suppresses definite inference. It does not constrain entity kind.
- README:220-241 and `r11-unique-nonplace`: r11 tests non-place as `place_id`, not non-character as `entity_id`. Its diagnostics cannot establish the latter convention.
- `LOG.md:167-182` summarizes r11/r12 as entity membership/actor identity and occupancy behavior; no actor kind rule. `LOG.md:311-319` r21 concerns guarded occupancy and malformed dependencies, not ontology.

## Independent observed probe (no repository files changed)

Commands from repo root:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent
# CLEAN: schema, citations, relations, timeline; 0 violations
python3 .shokunin/lore/corpus/fixtures/check_bible.py /tmp/r44-place-actor-probe
# CLEAN: schema, citations, relations, timeline; 0 violations
```

The `/tmp` probe was copied from `consistent/`; only first event `entity_id` changed `mira` → `harbor`. Its `place_id=harbor`, source, tick, and all other data remained unchanged. Paired control is the unmodified `consistent/` CLEAN result above. This demonstrates checker acceptance, not semantic invalidity. Additional observed existing probes: r11 unique nonplace-place exits 1 with `timeline[0].place_id: not a place 'mira'`; r12 unique actor and r21 clean expose same-actor double-booked diagnostics. These test place typing/identity/occupancy, not character-only actors.

## Risks and falsifiable decision

- An unconditional actor-kind guard harms calibration if any timeline event legitimately has a place, faction, or item as subject; current schema permits those entity kinds and no cited convention excludes them.
- A future test could establish a narrower rule only if an existing, explicit event class says its actor must be a character. No such class/field is present in the current timeline schema.
- **Go** only if independent project evidence identifies such a scoped convention and a paired valid non-character actor control proves the guard does not reject legitimate events; then test one invalid character-location event versus unchanged clean control and preserve old baselines.
- **No-go now**: observed CLEAN is reproducible, but the ontology premise is unproven. No checker/fixture/README/LOG change warranted; coverage gain cannot be claimed without defining what invalid input is.
