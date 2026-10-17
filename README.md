# shokunin-world-bible — lore

The question this lane answers is whether a fictional-world record is internally consistent: entities, relations, and timeline events, with contradictions reported and not silently resolved (`PROVINCE.md`, `corpus/fixtures/check_bible.py`).

**Rank:** `SHONEN.md` is a promotion checklist. Two boxes are `[ ]`. Two are `[~]`, and both say the evidence is a lane assertion, not external promotion verification. That is not a promotion.

## Owns / refuses

Owns fictional-world records — characters, places, factions, items, relations, timeline events — with consistency verification and sourced inspiration (`PROVINCE.md`).

Refuses canon without an in-world citation, silently resolving contradictions, real-world rights claims, and game-mechanics verification (game-dev-2d). Writes stay in this repository, its fleet round report, and allowed append-only L0 questions. Siblings and domain source trees stay read-only (`PROVINCE.md`).

There is no root `SKILL.md`. `corpus/knowledge/2026-10-12-lore-decision-table.md` is the decision table named from `corpus/README.md`. `l0-questions.md` is the question file at the repo root.

## Start here

The checker that exists is `corpus/fixtures/check_bible.py`. It takes one directory of JSON arrays (`sources`, `entities`, `relations`, `timeline`). Exit 0 prints `CLEAN: ...`. Exit 1 prints each `VIOLATION:` and `N violation(s); no canon changed` (`corpus/fixtures/check_bible.py`).

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/consistent
```

`corpus/fixtures/README.md` still shows `.shokunin/lore/corpus/fixtures/check_bible.py`. That path is not where the file lives in this repository. The fixtures README is line-cited (for example `corpus/fixtures/README.md:110-128` in `corpus/knowledge/holder-assessment-boundary.md`, and older `.shokunin/lore/corpus/fixtures/README.md` lines in `reports/`), so this change does not rewrite it. Use the path above.

`corpus/fixtures/README.md` also says the consistent example exits 0 and the contradictions example exits 1. Re-read that file before treating a later fixture directory as part of the same pair.

## How to read the corpus

`corpus/README.md` is ten lines: knowledge notes, then the checker, then `live/runs/` for preserved stdout. It was left as the index. `corpus/knowledge/seed.md` is a mint proposal, not a validated schema (`corpus/README.md`). `corpus/knowledge/reference-ledger.md` keeps real-world method citations separate from rights and training questions. Fixtures are fictional (`corpus/README.md`).

## Map

| Path | What it is |
|---|---|
| `PROVINCE.md` | Lore boundary |
| `SHONEN.md` | Promotion checklist, not externally verified |
| `LOG.md` | Append-only record |
| `SCORECARD.md` | Axis verdicts |
| `l0-questions.md` | Append-only questions |
| `corpus/README.md` | Short index |
| `corpus/fixtures/check_bible.py` | Consistency checker |
| `corpus/fixtures/README.md` | Run notes; the `.shokunin/lore/...` command path is stale |
| `corpus/knowledge/` | Decision table, ledger, error patterns |
| `corpus/live/` | Preserved checker runs |
| `reports/` | Round reports |

## Neighbors

game-dev-2d owns mechanics verification. Real-world rights claims are refused here (`PROVINCE.md` names art-east-asian-design). Audio may ask for a separately approved brief and must not set canon (`shokunin-game-audio/PROVINCE.md`).

Fleet protocol: [VeigaPunk/shokunin](https://github.com/VeigaPunk/shokunin).
