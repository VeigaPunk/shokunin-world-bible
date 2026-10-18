# Round 14 executor — authored excerpts and exact clause map

## Artifacts and evidence boundary

Created only these two fixture files and this report:

- `corpus/fixtures/r10-registry-witness/courier-log-excerpt.md`
- `corpus/fixtures/r10-registry-witness/archive-ledger-excerpt.md`
- `reports/r14-executor.md`

Both excerpts are **newly authored fictional fixture text, not recovered evidence**. They use the exact existing IDs `courier-log` and `archive-ledger`. They are retrospective editorial renderings keyed to rows already in the fixture, not independent sources, corroboration, or proof of truth. No JSON row, checker, existing registrar excerpt, shared document, or LOG was changed. Checker prose support is not evaluated by the CLI.

## Exact clause map to existing rows

Quoted clauses below are verbatim from the newly authored courier/archive files unless marked `existing registrar excerpt`. “Supports” means wording correspondence within this designed fixture only. `first_appearance` is an index/source assignment, not proof of literal historical first appearance.

| Existing row (path and selector) | Source ID | Exact excerpt clause | Boundary |
|---|---|---|---|
| `entities.json` `$[0].first_appearance` (`mira`) | `courier-log` | “I am Mira.” | Identifies the in-fiction narrator; does not verify identity or historical first appearance. |
| `entities.json` `$[0].claims[0].statement` (“Mira carried the blue seal.”) | `courier-log` | “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | States carry; no ownership or custody outside this clause. |
| `entities.json` `$[1].first_appearance` (`harbor`) | `archive-ledger` | “Lantern Harbor has a registry.” | Names the place; no historical-first/completeness claim. |
| `entities.json` `$[1].claims[0].statement` (“Lantern Harbor has a registry.”) | `archive-ledger` | “Lantern Harbor has a registry.” | Direct wording correspondence only. |
| `entities.json` `$[2].first_appearance` (`tower`) | `archive-ledger` | “North Tower has a watch bell.” | Names the place; no historical-first/completeness claim. |
| `entities.json` `$[2].claims[0].statement` (“North Tower has a watch bell.”) | `archive-ledger` | “North Tower has a watch bell.” | Direct wording correspondence only. |
| `entities.json` `$[3].first_appearance` (`seal`) | `courier-log` | “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | Names the item; no historical-first, origin, or provenance claim. |
| `entities.json` `$[3].claims[0].statement` (“The seal accompanied Mira.”) | `courier-log` | “I am Mira.” + “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | Passage depicts accompaniment at that clause/event; does not extend duration/custody. |
| `entities.json` `$[4].first_appearance` (`sella`) | `registrar-copy` | Existing registrar excerpt: “I, Sella, registrar there…” | Existing file only; no new excerpt claims to map this row. First appearance remains an index, not historical proof. |
| `entities.json` `$[4].claims[0].statement` (“Sella is a registrar at Lantern Harbor.”) | `registrar-copy` | Existing registrar excerpt: “At first bell at Lantern Harbor, I, Sella, registrar there…” | Existing text, not authored in this task. |
| `relations.json` `$[0]` (`mira` → `seal`, `carries`) | `courier-log` | “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | Corresponds to carries; no legal possession or broader duration. |
| `relations.json` `$[1]` (`sella` → `mira`, `records_departure`) | `registrar-copy` | Existing registrar excerpt: “I, Sella, … recorded seeing Mira leave.” | Existing text; does not identify Mira’s destination. |
| `timeline.json` `$[0]` (`departure`, tick 1, `mira` at `harbor`) | `courier-log` | “At local tick 1, I leave Lantern Harbor carrying the blue seal.” | Matches departure/place and states local tick 1; no route or tick duration. |
| `timeline.json` `$[1]` (`arrival`, tick 2, `mira` at `tower`) | `courier-log` | “At local tick 2, I reach North Tower.” | Matches arrival/place and states local tick 2; no route, travel duration, or intervening event. |
| `timeline.json` `$[2]` (`registry-entry`, tick 1, `sella` at `harbor`) | `registrar-copy` | Existing excerpt: “At first bell at Lantern Harbor, I, Sella, registrar there, recorded seeing Mira leave. At Mira’s request, I left the registry destination blank and kept the carbon.” | Existing prose maps to the stated acts/place, but does **not** equate “first bell” with fixture tick 1. Its blank destination remains blank. |

`archive-ledger-excerpt.md` contains only the two quoted place statements. No relation or timeline row cites `archive-ledger`; it makes no chronology or destination claim. The courier excerpt names no route between endpoints and asserts no ownership. Neither excerpt adds lore beyond the already encoded assertions; they expose those assertions in bounded, inspectable in-fiction wording.

## Validation and limits

Ran `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/<case>` for all 28 fixture directories. Compared stdout, stderr, and exit code with the saved Round-13 outputs in `corpus/live/runs/20261012T180109Z/`: **28/28 byte-identical** (the saved files wrap stdout with command/exit metadata; compared the stdout payload and exit status). Six exited 0 and 22 exited 1; these are fixture-specific outcomes, not an aggregate pass claim. The registry-witness fixture exited 0. Replay establishes no prose-to-row support.

Hashed all 139 fixture JSON files before and after: per-path SHA-256 maps identical; sorted path/hash manifest SHA-256 `b125ecccd1a2c8a8130fa33fc4c59225e16e69c1a68d3acb885b5022a97ad2e5` both times. Checker SHA-256: `eaa2f1178c4571d8a911cb3d880068216614766d8f35922cb78d6584179dad80`.

The critic’s challenge stands: these excerpts are retrospectively composed to match existing rows, so the match is circular editorial traceability, not independent support. The files add inspectable prose but only restate the assertions; file count or prose alone may not constitute substantive depth. A non-author may reasonably judge depth unchanged (or unproven); no extra detail has been invented to force an improvement.
