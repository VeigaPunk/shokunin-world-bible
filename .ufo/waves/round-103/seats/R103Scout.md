<!-- verbatim final output of L2 seat W2RoundLore.R103Scout (read-only role), persisted by L1 lore round 103, 2026-10-19 -->
**Axes:** coverage classification; checker enforcement; governed-surface receipts. Read-only reconnaissance; no files changed.

### CM sweeps

Each command counted matching tracked files, using the full pathspec shown below; the count is **files**, not occurrences. The listed paths give substantive hits and representative incidental hits.

| CM | Pasteable `git grep -ciE` pattern | Matching files | Hits and verdict |
|---|---|---:|---|
| CM-a aliases/name variants | `alias|aka|homonym|epithet|name[- ]variant|name[- ]collision` | 7 | `corpus/knowledge/2026-10-12-lore-decision-table.md:17-18,49-56` explicitly says aliases are unchecked and the exact-name detector was rejected; `corpus/fixtures/README.md:74-80` records why. `corpus/knowledge/seed.md:24` is only a proposal (see `corpus/README.md:3`). **Uncovered** for active alias/name-variant governance. |
| CM-b free-text semantic contradiction | `free[- ]text|semantic contradiction|textual conflict|arbitrary prose|contradiction rationale` | 16 | `corpus/knowledge/2026-10-12-lore-decision-table.md:17-23,40-47` and `corpus/fixtures/README.md:43-54` govern a structural two-sided ledger, but explicitly exclude semantic validation; `corpus/fixtures/r30-explicit-negation/textual-conflict-map.md:1-5` is a manual example. **Partial.** |
| CM-c calendars/relative dating | `calendar|era|relative time|in.world dating|dating system|uncertain[- ]relative time|date conversion|calendar/ringing` | 74 | `corpus/fixtures/README.md:29-34` governs local integer ticks/order; `corpus/knowledge/2026-10-12-lore-decision-table.md:193-204` covers integer-tick behavior. `corpus/fixtures/r35-bell7-conflict/manual-clause-pointer-map.md:10,17,21` treats fictional calendar/date claims as unauthenticated. No alternate-calendar or era schema. **Partial.** |
| CM-d in-world reliability | `reliability_note|source reliabilit|source credibil|trustworthiness` | 168 | `corpus/fixtures/check_bible.py:26,79-83` requires a nonempty string; `corpus/knowledge/2026-10-12-lore-decision-table.md:47` says the ledger does not adjudicate reliability. Repeated `sources.json` metadata is not a reliability rule. **Partial.** |
| CM-e canon tiers/retcons/supersession | `canon tier|canon status|retcon|supersed(e|ed|es|ing)|continuity tier|status.*unresolved` | 31 | `SKILL.md:16,22-30` bounds what checker results establish; `corpus/knowledge/r88-sourced-inspiration-decision-table.md:18,26,87-102` governs preservation and manual unresolved R10 handling; `corpus/knowledge/r101-r10-register-first-entry.md:12,18,33-34` records an examined non-conflict. No canon-tier/retcon schema. **Partial.** |
| CM-f reveal order vs chronology | `reveal order|publication order|reading order|narrative order|spoiler|chronology vs|chronological reveal` | 0 | No hits in the searched surfaces. **Uncovered.** |
| CM-g kotodama handoff intake | `kotodama|handoff packet|packet intake|intake packet|dispatch packet|handoff` | 1 | `corpus/knowledge/r91-c9-watch.md:219` uses “handoff” for an owner transition; incidental, not packet intake. No kotodama/packet governance hit. **Uncovered.** |

For every row, the executed command form was `git grep -ciE '<pattern>' -- SKILL.md PROVINCE.md corpus/README.md corpus/knowledge corpus/fixtures corpus/tools | wc -l`; this includes tracked fixture JSON.

### `check_bible.py` enforcement inventory

Common loader/schema behavior for all five JSON tables: duplicate object member → `duplicate object member …; cannot load JSON` (`corpus/fixtures/check_bible.py:16-21,48-50`); unreadable/invalid JSON → `cannot load JSON` (`:52-55`); non-array → `expected array` (`:56-59`); non-object row → `expected object` (`:67-71`); required fields use exact Python types and nonblank strings (`:77-83`); repeated table IDs → `duplicate <section> id …` (`:85-102`). Unlisted extra row keys are not rejected.

| JSON | Required fields and checks (error strings / lines) |
|---|---|
| `sources.json` | `id,title,kind,reliability_note` (`:25-26`); only required-type/nonempty and duplicate-ID checks (`:79-96`). `kind` has no enum. References report `unknown in-world source …` / `ambiguous in-world source …` (`:104-116`). |
| `entities.json` | `id,kind,name,first_appearance,claims` (`:27`). Kind must be in `KINDS` (`:7,152-154`); first appearance and each claim’s `source_id` resolve against sources (`:155-161`); malformed claims → `expected nonempty statement and source_id` (`:156-161`). Relation/provenance references also resolve entity IDs (`:163-185,271-299`). |
| `relations.json` | `from,to,type,source_id` (`:28`). Endpoints → `dangling entity …` / `ambiguous entity …` (`:177-185`); only distinct faction `allied_with` edges get a sourced reciprocal check (`:347-365`). Relation `type` otherwise has no enum. |
| `timeline.json` | `id,tick,entity_id,place_id,depends_on,description,source_id` (`:29-30`). Tick must be exact `int` at field screening (`:77-83`), then nonnegative (`:384-385`); entity/place refs, place kind, source, double-booking, and dependency type/self/repeat/unknown/ambiguous/inversion checks are at `:367-414`. Errors include `not a place`, `double-booked`, `expected event-id strings`, `self dependency`, `repeated dependency`, `unknown event`, `ambiguous dependency event`, and `timeline inversion`. |
| `contradictions.json` | `id,claim_a,claim_b,why` (`:31`). Pointer fields are limited to `place_id,tick,depends_on`; each side must resolve to exactly one timeline event with a resolvable event source; identical event+field pointers fail (`:118-150`). `why` is required nonempty text via common screening, but its meaning is not checked. |

**Specific answers:** no entity-`name` uniqueness check; the active checker’s schema only requires `name` to be a nonempty string (`:27,79-83`). The duplicate-name detector was rejected for false-positive homonyms (`corpus/fixtures/README.md:74-80`; decision table `:49-56`). Timeline and provenance ticks are integer-only, including rejecting booleans/floats (`check_bible.py:29-30,259-260`). There is no calendar/era field. `reliability_note` is checked only as a required nonempty string; it is not read by a semantic check. No status/canon/superseded field is declared or checked; extra keys are ignored.

### Twelve governed surfaces: artifact and executed command

| Surface | Governing artifact | Command → observed exit |
|---|---|---|
| Entity schema/refs | `corpus/fixtures/check_bible.py:25-31,79-90,152-185,367-382` | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r12-ambiguous-actor` → **1**, duplicate entity ID/ambiguous refs |
| Relations + reciprocity | `corpus/fixtures/check_bible.py:177-185,347-365`; `corpus/fixtures/README.md:18-27` | `python3 corpus/fixtures/check_bible.py corpus/fixtures/ally-one-way` → **1**, missing sourced reciprocal |
| Timeline ticks/dependencies/inversion/double-booking | `corpus/fixtures/check_bible.py:367-414`; `corpus/fixtures/README.md:29-34` | `python3 corpus/fixtures/check_bible.py corpus/fixtures/contradictions` → **1**, inversion and double-booking observed |
| Contradictions ledger | `corpus/fixtures/check_bible.py:118-150`; `corpus/fixtures/README.md:43-54` | `python3 corpus/fixtures/check_bible.py corpus/fixtures/contradictions-ledger-malformed` → **1**, invalid event pointer |
| Source-ID resolution | `corpus/fixtures/check_bible.py:93-116,152-185`; `corpus/fixtures/README.md:36-39` | `python3 corpus/fixtures/check_bible.py corpus/fixtures/r39-ledger-source-missing` → **1**, unresolved source |
| Provenance chains | `corpus/fixtures/check_bible.py:187-345`; `corpus/knowledge/holder-assessment-boundary.md` | `python3 corpus/fixtures/check_bible.py corpus/fixtures/item-chain-broken` → **1**, chain break |
| R8 sourced inspiration | `corpus/knowledge/r88-sourced-inspiration-decision-table.md:28-42`; `corpus/knowledge/r93-r8-worked-example.md:75-204` | Corrected embedded replay (`r93-r8-worked-example.md:107-204`) → **0**, 12/12 example-record cells; not source-use verification |
| R9 claim→excerpt support | `corpus/knowledge/r88-sourced-inspiration-decision-table.md:25,44-79`; `corpus/tools/support_check.py` | `python3 corpus/tools/support_check.py corpus/fixtures/r94-paired-crossing` → **0**, `RESULT PASS`, 14/14 JSON facts; lexical preflight only |
| R10 cross-cluster comparison | `corpus/knowledge/r88-sourced-inspiration-decision-table.md:26,87-110`; `corpus/knowledge/r101-r10-register-first-entry.md` | `git grep -nE 'R10 —|shared referent, field, and occasion|cross-cluster-contradictions.md' -- corpus/knowledge/r88-sourced-inspiration-decision-table.md corpus/knowledge/r101-r10-register-first-entry.md` → **0**, text-location check only; comparison is manual |
| Dependency-edge freeze | `corpus/tools/dependency_freeze.py`; `corpus/tools/dependency-freeze-contract.json` | `python3 corpus/tools/dependency_freeze.py corpus/fixtures/r100-docket-review` → **0**, 9/9 events, 8/8 edges |
| Boundary-document certification | `corpus/tools/boundary_doc_check.py`; `corpus/tools/boundary-doc-contract.json` | `python3 corpus/tools/boundary_doc_check.py` → **0**, `CERTIFIED` within its bounded scope |
| Real-world reference ledger | `corpus/knowledge/reference-ledger.md:1-16` | `git grep -nE '^\| .*https?://' -- corpus/knowledge/reference-ledger.md` → **0**, ledger rows located; no ledger-specific validator observed |

`lsp` was unavailable (`xd://lsp` is not mounted), so I used literal source search for the checker’s callers: `corpus/tools/discriminate_check.py:47,56-58,82` executes it; `corpus/tools/boundary_doc_check.py:20,35-45` pins/reads it.