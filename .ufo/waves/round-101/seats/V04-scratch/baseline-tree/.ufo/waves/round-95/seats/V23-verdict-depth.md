# V23 — verdict-depth (round 95)

Seat: V23 `verdict-depth`. Scope per seat spec: read the C2 verification seats
(V08–V14), run 2 own spot replays, issue exactly one DEPTH verdict on the declared
C2 before→after ("first reported-non-performance class", 5/1/3→5/1/4 preserving
continuation) with named bounds.

Baseline: r94 closure `fb118c4`. Working tree during the window: `M LOG.md`,
`?? .ufo/waves/round-95/`, `?? corpus/fixtures/r95-crossing-aftermath/`,
`M corpus/tools/map_obligations.py` (P1 iterating from 16:22 onward),
`?? corpus/knowledge/r95-aftermath-scope-note.md` (P5). Writes by this seat: this
report + scratch dir `.ufo/waves/round-95/seats/V23-scratch/` (poll script, replay
script, replay output, hash captures). No commits, no network, no nested agents.

## 1. Poll record and method

- Target 1 (fixture `corpus/fixtures/r95-crossing-aftermath/`): first 8 P3 files at
  16:18:01, all still byte-copies of r94 at that instant; modifications landed
  16:18:34 (mtime `2026-10-17 16:18:34` for timeline/sources/excerpts); P4's map
  16:21:10, README 16:21:27; P3 report 16:20, P4 report 16:22. My 20 s-cadence
  poller (40 tries) saw 10/10 files at try 15 (16:21:44) and reported fixture
  complete.
- Target 2 (C2 verification seats V08–V14): **V08, V10, V11, V12, V14 present and
  read; V09, V13 ABSENT** (V10 landed 16:28; last check 16:29:21; poller cutoff
  ~16:30). The verdict below therefore rests on my own replays plus the eleven
  landed C2/C2-adjacent seat reports (V08, V10, V11, V12, V14, V35, V36, V44,
  V50, V20, and V24 §3); the two absent seats are named as unavailable
  cross-checks, and none of their content was guessed.
- Fixture frozen for verification: 10-file sha256 capture
  (`V23-scratch/fixture-hashes-before.txt`); re-checked after all replays →
  `sha256sum -c` reports OK for all 10 files (no write during the verify window).
  Key hashes: timeline `3c0faad6…`, sources `fd9e30e8…`, excerpts `0ef6734a…`,
  map `30281ff1…`, README `9d27af4a…`; all equal P3/P4/V08/V12 captures.

## 2. Before-state replays (r94-paired-crossing)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r94-paired-crossing
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
RESULT PASS
exit=0
counts: entities 5 relations 1 events 3 sources 3
timeline ids ['aru-ninth-bell', 'evin-ninth-bell', 'paired-crossing-decision']
source ids ['veil-verse', 'paired-clock', 'crossing-minute']
```

## 3. Spot replay 1 — check_bible on the delivered r95 fixture

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r95-crossing-aftermath
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
```

Checker revision: `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`
(V44 §2 and V20 §1 reproduce this pin; `git status --porcelain` clean for the file
— unchanged since baseline). Before → after: CLEAN exit 0 → CLEAN exit 0.

## 4. Spot replay 2 — map_obligations + preservation battery

Tool revisions sampled: `c37f298b…` (16:22, first post-P1 receipt), `9224a684…`
(16:26), and the settled `d1c239cc…` (16:29, with 22-case contract
`8173bb97…`; `--self-test` → `RESULT PASS`, exit 0). P1 iterated during the
round; every sampled stable revision behaves identically on these clusters:

```
$ sha256sum corpus/tools/map_obligations.py   → d1c239cc… (settled)
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r95-crossing-aftermath
OBLIGATIONS raw=15 mapped=15
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17
RESULT PASS
exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r94-paired-crossing
OBLIGATIONS raw=14 mapped=14
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 16/16
RESULT PASS
exit=0
```

Preservation battery (`V23-scratch/replay.sh`, output kept verbatim at
`V23-scratch/replay-output.txt`):

```
counts: entities 5 relations 1 events 4 sources 4
timeline ids [..., 'aftermath-missing-evin']
new event: {"id": "aftermath-missing-evin", "tick": 11, "entity_id": "aru",
 "place_id": "chalk-stair", "depends_on": ["paired-crossing-decision"],
 "source_id": "aru-aftermath-note", ...}
entities.json BYTE_IDENTICAL; relations.json BYTE_IDENTICAL;
contradictions.json BYTE_IDENTICAL; inspiration-note.md BYTE_IDENTICAL;
source-excerpt.md BYTE_IDENTICAL
timeline.json inherited_prefix_identical=True; sources.json inherited_prefix_identical=True
fictional-excerpts.md: r94 1116 bytes / r95 1845 bytes; r95[:1116] == r94 → True
map rows: 16 inherited rows (J01–J14, S01, S02) identical modulo cluster-path
qualification; only J15 new (pointer timeline.json#/3, source aru-aftermath-note,
span 22-31, anchor line 26)
$ python3 corpus/tools/support_check.py corpus/fixtures/r95-crossing-aftermath
INVENTORY JSON-FACTS 15/15; EDITORIAL-ROWS 2/2; TOTAL-ROWS 17/17; DISTINCT-ANCHORS 13/13
SOURCE-SUPPORT 15/15; EDITORIAL-ANCHORS 2/2; MODES 17/17; VALIDATED-ROWS 17/17
RESULT PASS   exit=0
```

Census and non-regression (my own runs):

```
$ git ls-tree -d --name-only fb118c4 corpus/fixtures/ | wc -l   → 168
$ find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l  → 169
$ git diff --stat fb118c4 -- corpus/fixtures/r94-paired-crossing \
    corpus/tools/support_check.py corpus/fixtures/check_bible.py   → (empty)
```

## 5. "First reported non-performance" — independent bounding

- Corpus scan: `did not come|did not arrive|didn't come|failed to come|no-show|
  never came|did not appear|did not show` matches **only** r95 bytes
  (`fictional-excerpts.md:27`, `timeline.json:40`, `sources.json:24`, plus the
  r95 README/map/P5 note). No earlier fixture carries the wording class.
- Nearest prior report-not-proof classes checked directly: r23-note-class is
  Sella's report that a named *thing* was not found ("I did not find it there" —
  `sella-absence-note-excerpt.md`); r83-vela-joint-nonsighting is a sighting
  class. Both differ in object and scope from a person's reported non-arrival
  under a bounded agreement (P5's note documents the same distinction; my read
  of the two fixtures agrees).
- Scope audit (my grep over all 10 r95 files): every occurrence of
  breach/duty/obligation/perpetual/alliance is inside a negating or scoping
  clause; zero occurrences of betray/fault/guilt/abandonment. V12 §4 (13
  classified lines) and V36 §3–§4 (deontic scan; five adversarial broader-duty
  constructions, all failing) independently confirm.

## 6. C2 verification seats read (statuses at report time)

- **V08 c2-checker — PASS**: CLEAN exit 0 twice with identical hashes; counts
  exactly 5/1/4/4; `aftermath-missing-evin` tick 11 `depends_on ==
  ["paired-crossing-decision"]`; independent ID-integrity scan CLEAN; r94
  untouched and still CLEAN.
- **V10 c2-support-map — PASS** (landed 16:28): support_check 15/15 + 2/2
  PASS exit 0 and map_obligations raw=15 mapped=15 PASS exit 0 at the settled
  tool `d1c239cc…` (22 cases; `--self-test` RESULT PASS exit 0); all counting/
  preservation claims hold; J15 load-bearing (row deletion → `missing_obligation`
  exit 1; source-ID corruption → `source_id_mismatch` exit 1); C1 mutation class
  reproduced on r95 scratch bytes (not my axis).
- **V11 c2-anchors — PASS**: 15/15 JSON + 2/2 editorial anchors in-span; every
  inherited anchor byte-identical and at the same line numbers as r94; new
  anchor only at line 26; zero drift.
- **V12 c2-whole-claim — PASS**: every proposition traces to excerpt clauses and
  JSON rows; description fields do not out-claim; scope discipline holds;
  inheritance byte/value-exact. Non-blocking notes O1–O4 (bell referent, edge
  wording, actor slot, kind precedent).
- **V14 c2-dependency-probe — PASS with a blind-spot finding**: probes (b)
  unknown dep, (c) tick inversion, (d) removed tick-10 row all report exactly
  (exit 1); **probe (a) — dropping `depends_on` entirely — stays CLEAN exit 0**:
  `check_bible` has no dependency-presence rule (omission is silent). Reported
  as checker evidence, not a fixture defect.
- **V35 anchor-replica-2 — PASS**: third independent line-slice method, 15/15
  in-span, 0 misses, calibration control shows the method detects span shifts;
  obs: R9 declaration `fictional-excerpts.md:12-29` vs J15 span 22-31 is a
  declaration-granularity nit, anchor line 26 lies inside both.
- **V36 whole-claim-replica-2 — PASS**: five adversarial broader-duty
  constructions all fail; closest ("the agreed bell" referent gap) is a bounded
  ambiguity, not an assertion; census/untouched-tools checks reproduce.
- **V44 exit-contract-c2 — PASS**: r13/r16/r17/r19/r20 edge classes reproduce on
  scratch copies of the delivered fixture; unmutated copy CLEAN.
- **V50 byte-prefix — PASS**: five files `cmp`-identical; excerpt exact 1116-byte
  prefix + 729-byte append (0 removed lines); JSON append-only; all ten r94
  files match their `fb118c4` blobs.
- **V20 doc-parity — PASS**: census 169 / 35 clean / 134 negative / 421 lines /
  zero stderr; one added directory, zero changed inherited tuples; fixture
  matches C2's declaration exactly.
- **V24 verdict-coverage (sibling seat, coverage axis) — INTERIM**: its §3
  independently confirms r95 `raw=15 mapped=15` and a load-bearing negative
  control (deleting J15 → `missing_obligation` exit 1). Its coverage verdict is
  INCONCLUSIVE on C3 because P1's tool was still iterating; not my axis, noted
  for context only.
- **V09, V13 — ABSENT** at 16:29:21 (poller cutoff ~16:30): two designated C2
  seats' reports were unavailable; their findings are neither quoted nor
  inferred.

## 7. DEPTH VERDICT (exactly one)

**DEPTH — IMPROVED (bounded).** On the delivered revision, the lane's fixture
corpus gains its first reported non-performance against a crossing-scoped
agreement as a preserving continuation: before r94 = 5/1/3 entities/relations/
events, 3 sources, 14 map obligations, no reported non-performance anywhere in
the corpus; after r95 = 5/1/4, 4 sources, 15 map obligations (14 inherited rows
carried unchanged + the new tick-11 event row, load-bearing per V24's deletion
control), `check_bible` CLEAN exit 0, census 168→169 with zero inherited
changes, and the scope discipline (crossing-only; no breach/other-duty
assertion) verified by adversarial whole-claim review. No harm observed in my
scope: r94 fixture, `check_bible.py`, and `support_check.py` byte-unchanged vs
`fb118c4`; no new claims, entities, or relations.

Named bounds:

1. **Structural/lexical only.** The verdict is on delivered bytes (hashes in §1)
   plus hand scope review; no semantic entailment, testimony, canon-truth,
   chronology, rights, or identity claim.
2. **"First" is corpus-bounded.** First within this lane's delivered fixture
   corpus; nearest prior report-not-proof classes (r23 thing-not-found, r83
   nonsighting) differ in object/scope. Not a claim about any wider corpus.
3. **Checker blind spot.** `check_bible` cannot detect a dropped `depends_on`
   (V14 probe a: CLEAN exit 0); the tick-11→tick-10 link is verified as
   delivered bytes + prose + map-row binding, not by a checker rule. A future
   silent edge omission would not be caught.
4. **Tool-revision flux (settled).** `map_obligations.py` changed repeatedly
   during the round (cc1df4dc → … → 9224a684 → settled `d1c239cc` with 22-case
   contract `8173bb97`); every sampled stable revision gives r95 15/15 and r94
   14/14, and at the settled revision `--self-test` → `RESULT PASS` exit 0. The
   earlier `self_test_contract` mismatch (P2's contract not yet landed) cleared
   ~16:27; the two transient tracebacks V10 saw were mid-write states, never
   produced by a delivered revision on this fixture. C1/C3 remain other seats'
   claims.
5. **Preserving continuation at named levels.** Byte-level for the five copies,
   JSON-value prefix for timeline/sources, 1116-byte prefix for the excerpts;
   the map file itself is re-qualified (namespace column), so "14 inherited rows
   carried unchanged" holds at pointer/span/mode/anchor level (my check + V50
   obs 1 + V24 §3 parser comparison), not at map-file byte level.
6. **Carried bounded ambiguities.** "the agreed bell" referent gap (V12 O1, V36
   §4A — unresolved referent, not an asserted duty); R9 declaration `12-29` vs
   J15 span `22-31` (V35 obs 1, V36 obs 2); `kind` = `fictional first-person
   note` interpretation flag (P3 flag 1; V12 O4 finds 60-row corpus precedent).

## 8. Non-axis observations (for the integrator)

- V08 process note: a stray copy of its report landed in the **parent** repo
  (`/home/vgpnk/Projects/shokunin/.ufo/waves/round-95/seats/`) and was deleted;
  a `V30-shonen-format.md` sits in the parent's seats dir and is absent from the
  lane's — possible misplacement to check at closure.
- Transient repo-root temp dirs from `--self-test` runs
  (`map-obligations-self-test-*`) appeared and were cleaned (V36 obs 4);
  baseline behavior, no stray artifact at my final sweep.
- P4's report "Addendum — post-P1 re-run" is still empty (pending); P4's receipt
  to fill, not a C2 artifact defect.
- V09/V13 ABSENT through the poll cutoff (try 40, 16:30:04); if they land before
  closure, their findings are additive to §6 and do not change the artifact
  evidence in §3–§5.

## Bottom line

**PASS — DEPTH verdict: improved (bounded)** — the delivered r95 fixture is the
lane's first verified reported-non-performance continuation (5/1/3→5/1/4, 14→15
map obligations, CLEAN/PASS receipts, byte/value/prefix preservation, adversarial
scope discipline), with the named bounds in §7 (structural-only evidence, corpus-
bounded "first", dependency-presence blind spot, settled tool revisions, and two
absent designated seats: V09/V13).
