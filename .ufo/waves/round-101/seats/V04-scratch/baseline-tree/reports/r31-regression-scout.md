# Round 31 regression scout

## Prior-fixture coverage

The r7 precedent is not a direct control for the proposed relation class: `.shokunin/lore/corpus/fixtures/r7-ally-reverse-ambiguous/relations.json:1-13` has two `allied_with` rows, and only the reverse row at lines 8-12 cites duplicated `harbor-compact`. The duplicate source records are at `sources.json:3-16`; the forward relation instead cites `separate-compact` (`relations.json:2-6`). This establishes existing ambiguous relation-citation coverage, but specifically in the alliance fixture. Do not describe generic relation ambiguity as entirely untested.

The `consistent` seed has one `mira -> seal / carries` relation citing `courier-log` (`.shokunin/lore/corpus/fixtures/consistent/relations.json:1-8`) and exactly one `courier-log` source (`sources.json:8-13`). Thus a paired fixture duplicating only that source row exercises ambiguity for a non-alliance relation while preserving the relation row. Checker source counting maps counts to `unknown`/`unique`/`ambiguous` (`.shokunin/lore/corpus/fixtures/check_bible.py:54-66`); `source()` emits the location-specific ambiguity diagnostic (`:68-74`), and the generic relation loop calls it for each row (`:123-130`).

## Regression and expected test

Replay the baseline’s 81 fixtures and 404 pre-existing JSON paths, comparing each invocation’s stdout, stderr, and exit status and each JSON path’s bytes to baseline commit `635f8b6a91ed408f067a58a8fbff51388c49c568`. This is a plan, not a replay result. Do not claim invariance until independently tested. For the proposed new pair, run the documented checker on both fixture directories: the unique-source control should exit 0; the duplicate-source variant should include `relations[0].source_id: ambiguous in-world source 'courier-log'`. Inventory the entire output delta: the duplicated source can legitimately make other records using that ID ambiguous too, so do not assert that only one diagnostic changes. The checker’s relation call site and shared source resolver establish this risk (`check_bible.py:68-74,123-130`).

This adds coverage only for a controlled non-alliance relation citing an ambiguous in-world source. Duplicate IDs make citation resolution ambiguous; they do not establish that the relation is false, settle canon, establish source authenticity, or grant citation rights. No checker rule change is indicated: this is generic behavior already implemented, tested on alliance relations in r7, and proposed for a distinct input class. Depth and calibration are outside this coverage-only claim.
