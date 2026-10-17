# R6 — knowledge-note (round 97)

Seat: R6 knowledge-note. Exclusive write scope per seat spec:
`corpus/knowledge/r97-acknowledgment-scope-note.md` — delivered (70 lines). Scratch:
`.ufo/waves/round-97/seats/R6-scratch/` (`verify_note.py`, `audit_note.py`, `draft.md`).
No other writes; no commits; no pushes; no network.

Baseline: r96 closure `f3e09f9` (HEAD at seat time `2393934`, working tree carried the
round-97 declaration in `LOG.md` before this seat ran).

## Poll-wait record

- At seat start (~`2026-10-17T18:41-03:00`) `corpus/fixtures/r97-crossing-acknowledgment/`
  and `.ufo/waves/round-97/seats/` did not exist; nothing was verified before it existed.
- Background poll (20 s × 40) first exited `READY try=7 nfix=10 seats=58 r4=1 r5=1` — but its
  glob had matched the *scratch directories* `R4-scratch`/`R5-scratch`, not reports. Noted
  honestly; relaunched a strict poll (`^R4.*\.md$`): `REPORTS READY try=22` (R4 report
  18:50:14, R5 report 18:51:25).
- Artifact landing (mtimes): r97 JSON tables + `fictional-excerpts.md` 18:44:30 (R4);
  R5's `claim-excerpt-map.md` 18:48:56 and `README.md` 18:49:14. Intermediate state observed
  honestly: at 18:44 the r97 `README.md`/`claim-excerpt-map.md` were R4's byte-copies of the
  (post-repair) r96 versions — header still "Round 96" — and no receipt was run on them; the
  map-dependent receipts were deferred until R5's rewrite landed.
- Never verified a plan; every check ran against real files on disk.

## What the note records

`corpus/knowledge/r97-acknowledgment-scope-note.md` opens with `source:` / `verified-at:` /
`recheck:` / `citation-convention:` metadata, then:

1. **The class** — *cross-account acknowledgment without reconciliation*: Aru's own first-person
   record that he received Evin's response, where the record asserts both accounts stand
   unresolved, selects no winner, makes no accusation, and asserts no reconciliation, no new
   duty, no obligation beyond the crossing. Named as the **third beat** of the crossing arc
   (r95 report → r96 response → r97 acknowledgment), with the dispute preserved unresolved and
   no new account of the occasion added.
2. **Supporting records (exact)** — `aru-acknowledgment-note` (`sources.json#/5`, id at `:33`,
   reliability note `:36`) and `acknowledgment-aru-records` (`timeline.json#/5`, id at `:55`;
   tick 13, `entity_id: aru`, `place_id: chalk-stair`, `depends_on: ["response-evin-salt-court"]`),
   note text at `fictional-excerpts.md:44-53` (quoted `:48-51`), map row J17 at
   `claim-excerpt-map.md:38` (span 44-53) with bounded reading at `:57`, plus the inherited
   r95/r96 rows.
3. **The r96 cosmetic repair** — recorded as part of this round: `:44` delimiter 8→7 cells,
   `:50` stale "new relation" sentence rewritten to the tick-12 event wording, data rows
   byte-unchanged (`git diff` = exactly 2 lines), r96 receipts unchanged; sha256
   `5093d72e…` → `e851f068…`.
4. **Bounds** — Aru's report only; no resolution truth; no winner/accusation/reconciliation/new
   duty; no contradiction asserted (different actors/places, `contradictions.json` stays `[]`);
   editorial tick/ID alignments; checker validates structure, not testimony.
5. **Precedent cross-reference** — `r95-aftermath-scope-note.md` (first account),
   `r96-response-scope-note.md` (second account), the r35 preservation precedent
   (`r35-bell7-conflict/contradictions.json#/0`; `manual-clause-pointer-map.md:3`, `:21`;
   `corpus/fixtures/README.md:746-771`, "Neither wins." at `:761`), and the r23 report-not-proof
   row (`2026-10-12-lore-decision-table.md:226-230`).
6. **Receipts and limits** — the three commands below with tool revisions and the census.

## Receipts (measured this pass, from the lane root)

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r97-crossing-acknowledgment
# CLEAN: schema, citations, relations, timeline; 0 violations   exit 0
python3 corpus/tools/support_check.py corpus/fixtures/r97-crossing-acknowledgment
# INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19; DISTINCT-ANCHORS 15/15
# ANCHORS repeated-references=4; DUPLICATE-ROWS 0
# RECEIPT JSON-FACTS 17; EDITORIAL-ROWS 2; TOTAL-ROWS 19
# SOURCE-SUPPORT 17/17; EDITORIAL-ANCHORS 2/2; MODES 19/19; VALIDATED-ROWS 19/19 / RESULT PASS   exit 0
python3 corpus/tools/map_obligations.py corpus/fixtures/r97-crossing-acknowledgment
# OBLIGATIONS raw=17 mapped=17 / INVENTORY JSON-FACTS 17/17; EDITORIAL-ROWS 2/2; TOTAL-ROWS 19/19 / RESULT PASS   exit 0
```

Tool revisions at my receipts: `check_bible.py` `ff9fd2aa…`, `support_check.py` `55a5eb27…`
at both runs; `map_obligations.py` `70795150…` at 18:46 and `86b52949…` at 18:52 — identical
r97 result under both (R1's revision was still moving; the note records this). Fixture bytes
were frozen across both runs: all ten r97 file sha256 match R5's receipt list exactly
(`sources.json 438fb513…`, `timeline.json 73063a86…`, `fictional-excerpts.md 8ba491cb…`,
`README.md d9387b7d…`, `claim-excerpt-map.md 49d4834e…`, five inherited files unchanged).
r96 receipts re-run post-repair: `check_bible` CLEAN exit 0; `support_check` `16/16` +
`18/18` PASS exit 0; `map_obligations` `raw=16 mapped=16` PASS exit 0.

## Independent checks behind the note's claims

- **Inheritance:** five files (`entities/relations/contradictions.json`, `inspiration-note.md`,
  `source-excerpt.md`) byte-identical r96↔r97 (`cmp`); `r97 timeline.json[:5] == r96 timeline.json`
  and `r97 sources.json[:5] == r96 sources.json` parsed-equal (`True`); map rows J01–J16 identical
  modulo the namespace column (0 diffs), J17 the only new row; counts 5/1/6/6; census 171.
- **r96 repair:** pre-repair sha256 recorded at seat start (`5093d72e…`); `git diff` shows
  exactly the two cosmetic lines; post-repair `e851f068…`; receipts unchanged (above).
  R4's and R5's reports independently agree on both hashes.
- **Citation audit:** `R6-scratch/audit_note.py` resolves all 52 path/line and JSON-pointer
  citations in the delivered note under the declared convention (bare `file:line` → r97 fixture;
  other fixtures full-path) → `BAD: 0`; 19 content probes at exact cited lines → `BAD: 0`.
  Two initial audit hits were context ambiguity in the *auditor* (multi-fixture paragraphs); I
  fixed the ambiguity properly by declaring the citation convention in the note rather than
  weakening the check.

## Adjacent observations (outside my scope, reported exactly)

- `map_obligations.py --self-test` now passes with the expanded case set (26 lines incl. RESULT
  at 18:53) — C1's contract 24→25 has landed.
- **`dependency_freeze` was mid-flight at my last check (18:53):** `--self-test` exits ERROR —
  `FINDING CONTRACT-INVALID: self-test expectation set mismatch; missing=['path_mismatch', 'scope_refused']`
  (`dependency_freeze.py` `b06275f3…` in tree vs contract `c65ac3bd…`); `dependency_freeze.py
  corpus/fixtures/r97-crossing-acknowledgment` → `UNPINNED-FIXTURE` (r97 not yet in the pin list;
  pinned: r88/r94/r95/r96). C2's declared 16-case self-test and the r96 re-freeze are R3's
  in-flight work; I do not adjudicate it — recorded as observed.
- `corpus/fixtures/README.md:1217` still states the r96 census (170); the file is read-only this
  round (no producer owns it), so the 170→171 text update is a closure-side item.

## Caveats

- This is an author-seat knowledge note, not independent verification of C3; the class name and
  bounds are my reading of the delivered records, and the note says so.
- The census 171 was measured while other seats were still writing; it counts directories only.
- No writes outside the seat's exclusive scope and `R6-scratch/`; `git status` shows my only
  new file as `corpus/knowledge/r97-acknowledgment-scope-note.md`.

Bottom line: **PASS** — `corpus/knowledge/r97-acknowledgment-scope-note.md` delivered (70 lines)
with every cited path/line and JSON pointer verified (52 resolved, 0 BAD; 19 content probes 0 BAD),
three receipts PASS (exit 0) on the frozen delivered fixture, inheritance and the r96 cosmetic
repair independently confirmed, and no writes outside the seat's exclusive scope.
