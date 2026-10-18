# Round 31 reviewer — controlled non-alliance source ambiguity

## Scope and artifact inspection

The unique control is byte-identical to `corpus/fixtures/consistent/` across all five JSON tables. The ambiguous variant appends one source row with duplicate ID `courier-log`; `entities.json`, `relations.json`, `timeline.json`, and `contradictions.json` are byte-identical between pair. In particular, `relations[0]` remains the `mira` → `seal` `carries` relation with `source_id: courier-log`.

## Replay

Replayed from repository root with:

```sh
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r31-source-unique
python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/r31-source-ambiguous
```

The unique case exits 0 with `CLEAN: schema, citations, relations, timeline; 0 violations`. The ambiguous case exits 1 with eight findings: duplicate `sources[2].id`; ambiguous-source findings at `entities[0].first_appearance`, `entities[0].claims[0].source_id`, `entities[3].first_appearance`, `entities[3].claims[0].source_id`, `relations[0].source_id`, `timeline[0].source_id`, and `timeline[1].source_id`. This inventories all affected references rather than presenting the relation-local result as the only delta.

## Prior round / novelty boundary

Replayed `r7-ally-reverse-ambiguous`: it exits 1 with duplicate `harbor-compact`, ambiguity at `relations[1].source_id`, and the missing sourced reciprocal finding. Round 7 therefore already exercised an ambiguous relation citation, specifically on the reverse `allied_with` relation. Round 31 is novel only as a controlled, non-alliance `carries` relation case; it is not the first relation-source ambiguity and establishes no new checker rule.

The duplicate identifier makes the source reference ambiguous. It does not establish that the `carries` relation is false, true, or canonically resolved, and this inspection supports no source authenticity, rights, or other canon inference.
