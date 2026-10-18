# V39 — whole-claim-replica-2: constructibility of an official-ruling reading (round 98)

Seat: **V39 whole-claim-replica-2** (verifier). Second independent whole-claim replica of the
round-98 C3 fixture, with one explicit obligation per the seat spec — **attempt to construct an
official-ruling reading over the delivered bytes and report its constructibility**. Baseline: r97
closure `9a3d648` (wave tree uncommitted during the round; every pre-round byte compared via
`git show 9a3d648:<path>`). All commands ran from the lane root
`/home/vgpnk/Projects/shokunin/lore-shokunin` with `python3`. Leaf seat: no nested agents, no
commits, no pushes, no network. Writes: this report plus
`.ufo/waves/round-98/seats/V39-scratch/` (absolute lane paths); **no corpus file was modified** —
all probes ran on scratch copies under `V39-scratch/`.

## 0. Poll-wait record (artifact-based; content-gated; no plan verified)

Cadence 20 s; the fixture directory and producer reports were polled; every receipt below was
taken only after the relevant bytes were content-ready (markers `clerk-maren` /
`clerk-filing-open` / `clerk-filing-note`, map/README moved off the r97 placeholder hashes).

| Time (-03:00) | Observation |
|---|---|
| 20:28:20 (try 1) | `corpus/fixtures/r98-clerk-filing/` **absent**; no producer reports |
| 20:28:24 | directory appeared with 10 files **byte-identical to r97** (placeholder phase; hashes `026af0bc…` entities, `438fb513…` sources, `73063a86…` timeline, `8ba491cb…` excerpts, `d9387b7d…` README, `49d4834e…` map). I did **not** verify this state |
| 20:28:34 | S3's r95 map repair landed (`30281ff1…` → `80440d61…`) |
| 20:28:55 | S3's four content files landed (entities `db2d8e5d…`, sources `32ee15b1…`, timeline `eb24e084…`, excerpts `29e384bf…`) |
| 20:30:28 | S4's map landed (`c1099d0e…`, 20 obligations) |
| 20:31:05 | S4's README landed (`32efc78f…`) |
| 20:32:34 | `corpus/knowledge/r98-clerk-scope-note.md` present (`1162262c…`) |
| 20:33:36 | S1's final contract revision `153ebc5b…` (r97+r98 pins) |
| 20:34:06 | S2's `corpus/tools/README.md` addendum (`1d299c16…`) |

Reports read in full: `S3-fixture-author.md`, `S4-fixture-docs.md`, `S5-knowledge-notes.md`,
`S2-tools-docs.md`, and — late-landing — `S1-freeze-hygiene.md`. **S1's producer report was
ABSENT** at my first finalization check (poll try 18, 20:35:14) and **landed at try 19
(20:35:34)**; S1's *artifacts* (`dependency_freeze.py` `03d04365…`, contract `153ebc5b…`) were
present and exercised directly throughout, so no verification depended on the report. S1's
report was then read and cross-checked: its C1(a) before/after diff (`emit(1,…)/return 1` →
`emit(2,…)/return 2`), its 17-case self-test output, its C1(b) migration receipts
(`CONTRACT-INVALID`/`SCOPE-REFUSED` before, `MIGRATED …` after, same-named-different-path
refusal unchanged) and its freeze receipts match my independent measurements exactly. The
r96/r97 endgame class did not recur here: no poll waited on all reports, and no poll waited on
SELF. One in-flight sequence was handled by content-gating rather than existence (the r97
byte-copy placeholder between 20:28:24 and 20:30:28) — the same hazard V11/S3/S4 independently
flagged.

## 1. Frozen revision identity (hashes at my receipts, 20:33–20:35)

```
c1099d0ee9eece241ea1f796320a84453dfc6b6aec33b7b9dd7e39bbef4a94ba  claim-excerpt-map.md
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  contradictions.json
db2d8e5d3866009bd5f98121080eb89eddb21adf58f20b803e58ae0c26872984  entities.json
29e384bf2eb2ab80858ace9423f29088a552553f87da7f6a9b694cbb050666de  fictional-excerpts.md
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  inspiration-note.md
32efc78f70e6de4f9670134080711923199e8693015d3ebea75a4a1ca6362926  README.md
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  relations.json
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  source-excerpt.md
32ee15b1f3d72d94f4228cbc9cefa69b7185d18b47bbe219833d7aaf30eed0f3  sources.json
eb24e0848e597efa29ed858cb8557d8f3126a47e1231f9469d719257e191e7af  timeline.json
```

Tool/doc revisions at these receipts: `check_bible.py` `ff9fd2aa…`, `support_check.py`
`55a5eb27…`, `map_obligations.py` `86b52949…`, `dependency_freeze.py` `03d04365…`,
`dependency-freeze-contract.json` `153ebc5b…`, `corpus/tools/README.md` `1d299c16…`, r95 map
`80440d61…`, r98 note `1162262c…`. The map/README/fixture bytes were stable across my window
(20:31:05 → 20:35); the contract moved once after my first pass (`c435239d…` → `153ebc5b…`) and
**every receipt below was re-run against `153ebc5b…`** (the chain digests are identical at both).

## 2. Gate receipts (all exit codes quoted; full outputs in `V39-scratch/final-receipts.txt`)

```
$ python3 corpus/fixtures/check_bible.py corpus/fixtures/r98-clerk-filing
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
$ python3 corpus/tools/support_check.py corpus/fixtures/r98-clerk-filing
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 18/18
ANCHORS repeated-references=4; DUPLICATE-ROWS 0
PASS J01 … PASS J17 (inherited lines 12/13/17/18/19/20/26/37/48)
PASS J18: source-support; mode=verbatim; anchor=found; 60:> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
PASS J19: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS J20: source-support; mode=verbatim; anchor=found; 59:> Tick 14: I filed both pending accounts at the Chalk Stair registry.
PASS S01 / PASS S02: editorial-row; mode=verbatim; anchor=found
RECEIPT JSON-FACTS 20; EDITORIAL-ROWS 2; TOTAL-ROWS 22
SOURCE-SUPPORT 20/20; EDITORIAL-ANCHORS 2/2; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS                                                            exit=0
$ python3 corpus/tools/map_obligations.py corpus/fixtures/r98-clerk-filing
OBLIGATIONS raw=20 mapped=20
INVENTORY JSON-FACTS 20/20; EDITORIAL-ROWS 2/2; TOTAL-ROWS 22/22
RESULT PASS                                                            exit=0
```

Chain and self-test at the same revision (`--freeze` pins r97+r98; path-bound):

```
$ python3 corpus/tools/dependency_freeze.py --self-test
… CASE self_test_mismatch: exit=2 expected=2 findings=['SELF-TEST-MISMATCH'] ok
SELF-TEST 17/17 / RESULT PASS                                          exit=0
$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath \
           r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$f | tail -2; done
r88 15ef230ef806… PASS;  r94 2527beb938b4… PASS;  r95 d541ae641f31… PASS
r96 d422a9b3d95c… PASS;  r97 3c922d20a01b… PASS;  r98 59a0f4fa3d4a… PASS   (6/6, all exit 0)
```

r95 receipts (S3's repair half) are unchanged: `support_check` `JSON-FACTS 15/15` … `RESULT
PASS` exit 0; `map_obligations` `raw=15 mapped=15` … `RESULT PASS` exit 0; `dependency_freeze`
r95 `DIGEST d541ae64…` `RESULT PASS` exit 0. This matches V15's independent pre/post equality.

## 3. Inheritance, counts, census (my own measurement)

```
entities.json : r97 rows=5  r98 rows=6  inherited_equal=True   added=1 (clerk-maren)
relations.json: r97 rows=1  r98 rows=1  inherited_equal=True   added=0  (BYTE-IDENTICAL)
timeline.json : r97 rows=6  r98 rows=7  inherited_equal=True   added=1 (clerk-filing-open)
sources.json  : r97 rows=6  r98 rows=7  inherited_equal=True   added=1 (clerk-filing-note)
contradictions.json: [] both   (BYTE-IDENTICAL)
fictional-excerpts.md: r97 bytes are a byte prefix of r98 (3410 → 4187; append starts line 55)
inspiration-note.md, source-excerpt.md: BYTE-IDENTICAL r97→r98
counts r98: entities=6 relations=1 timeline=7 sources=7
census: ls -d corpus/fixtures/*/ | wc -l = 172   (baseline 9a3d648 = 171)
```

So the declared C3 shape (5/1/6/6 → 6/1/7/7, census 171→172, 20 obligations = 17 inherited +
first_appearance + claim + event) replicates on the delivered bytes.

## 4. Core — constructibility of an official-ruling reading

Method: (a) lexical token scan over all ten fixture files for the ruling class
(`ruling|ruled|rules|verdict|finding|adjudicat*|judg*|decree|determin*|official*|authorit*|
jurisdict*|order*|open|filed|filing|pending`) with negation-context flagging; (b) hand clause
analysis of the appended section (`fictional-excerpts.md:55-64`) and of **every** surface that
describes the filing (`sources.json#/6`, `entities.json#/5`, `timeline.json#/6`, `README.md:3-15`,
map rows J18-J20 and their bounded paragraphs); (c) structural scan of the JSON tables for any
adjudicative actor, act, or effect; (d) gate-blindness probes on scratch copies (§5); (e) a token
scan of the five inherited chain fixtures for a pre-existing in-world institution that could
supply ruling authority.

The delivered section reads (lines 59-64):

```
> Tick 14: I filed both pending accounts at the Chalk Stair registry.
> I am Maren, clerk of the Chalk Stair registry, and I record the matter OPEN.
> I assert no finding.
> I reach no verdict and reconcile nothing.
Scope: … It is an institutional filing only: it asserts no finding and no resolution,
reaches no verdict, and reconciles nothing; the two first-person accounts stand unresolved …
```

| # | Construction attempted (official-ruling reading) | Evidence | Outcome |
|---|---|---|---|
| R1 | `record the matter OPEN` is an official determination that the matter stands open — i.e. an adjudicative status ruling | `fictional-excerpts.md:60`; `timeline.json#/6` "… recorded the matter OPEN, asserting no finding and no resolution."; `README.md:9`, `:11`; map `:66` | **Constructible only as an official *status record***; fails as a ruling — the same surfaces state "asserting no finding and no resolution", and `README.md:11` "The filing does not overturn, confirm, adjudicate, or reconcile the accounts". No normative effect on the parties is named |
| R2 | The filing act (`I filed both pending accounts`) is an official reception whose registration decides the accounts | `fictional-excerpts.md:59`; `entities.json#/5/claims/0`; `timeline.json#/6`; map J19/J20 | Fails — the record asserts the act of filing, not any ruling; map `:62` "it assigns no authority beyond the filing itself"; `README.md:15` "it asserts no office beyond the filing" |
| R3 | The clerk's office ("clerk of the Chalk Stair registry") is an authority whose record adjudicates the matter | `fictional-excerpts.md:60`; `sources.json#/6` reliability note; `README.md:15`; r98 note "First-appearance bound" | Fails — the office wording is the note's own attributed self-description (`fictional-excerpts.md:60`, bounded at `README.md:15` / map `:62`); no adjudicative power is asserted, and no prior in-world institution exists anywhere in the chain (scan (e): only `salt-court` place-name matches; all other institution tokens sit in boilerplate negations) |
| R4 | "I assert no finding" is an implicit *negative* ruling — a clean bill / finding of no breach | `fictional-excerpts.md:61`; `sources.json#/6` "It asserts no finding, no verdict, no reconciliation, and no resolution; it is not evidence of a breach …"; map `:66` | Fails — the sentence asserts the absence of a finding, not a finding of absence; the same note "reaches no verdict" and "reconciles nothing". The record blocks a ruling in **both** directions |
| R5 | `OPEN` is a procedural order/reservation with legal effect (the institution keeps the matter live) | `fictional-excerpts.md:60`; `timeline.json#/6`; `README.md:11` | Closest surviving construction, bounded: an institutional status entry; **no** procedural consequence, order, obligation, or effect is named, and the record "adds no duty beyond this crossing" (map `:66`) |
| R6 | The registry adopts "unresolved" as its own official position (institutional endorsement) | `timeline.json#/6`; `fictional-excerpts.md:64` scope; `README.md:11` | Constructible as an *institutional status position* ("the matter is open"); fails as a ruling on the merits — it selects no winner and asserts no resolution |
| R7 | Declination-of-adjudication reading ("the clerk declined to rule") | `fictional-excerpts.md:61-62` | Fails — no petition, dispute submission, or ruling request exists anywhere in the fixture; the two sentences are scope statements of the note itself |
| R8 | Structural: a hidden ruling actor/act/effect in the JSON (entity, relation, event, ledger) | `entities.json` (6 rows, `clerk-maren` is `kind: character`; **no institution entity exists** — the registry is named only in prose), `relations.json` (1 inherited row), `timeline.json#/6` (a filing), `contradictions.json` (`[]`) | Fails — the three added rows are exactly the declared first_appearance/claim/event; the added event is a filing, not an adjudication |

**Result.** On the delivered bytes **no official-ruling reading is constructible as an
assertion**. The fixture asserts exactly the C3-declared content — an institutional filing
record that asserts no finding and no resolution — and nothing adjudicative. The closest
surviving constructions (R1/R5/R6) are all *status-record* readings, each explicitly bounded by
the record's own words ("asserts no finding", "reaches no verdict", "reconciles nothing") and by
`README.md:11,15` and map `:62,:66`. The one structural asymmetry worth naming: the record does
assert positive institutional *acts* (filing, recording OPEN) while negating every adjudicative
*outcome* — so the class boundary is "act of recording vs ruling", not "silence vs speech".

## 5. Probes — the class is invisible to the delivered gates (restraint is editorial)

All probes ran on scratch copies under `.ufo/waves/round-98/seats/V39-scratch/probe-ruling/`;
the delivered corpus was never modified.

**Probe A — fabricated ruling row.** Appended to a scratch copy an entity `clerk-ruling` with
claim "The registry clerk ruled that Aru's account prevails." plus a tick-15 event
`clerk-ruling-issued` ("The clerk issues an official ruling adopting Aru's account and closing
the matter."). (First attempt put the event at tick 14 and the gate caught the unrelated
timeline-inversion class: `VIOLATION: timeline[7].depends_on: timeline inversion …` exit 1 —
included for honesty; the ruling class itself is what the final probe isolates.)

```
$ python3 corpus/fixtures/check_bible.py …/probe-ruling/cluster
CLEAN: schema, citations, relations, timeline; 0 violations            exit=0
```

**Probe B — semantically inverted clerk claim.** On a second scratch copy, the delivered
`clerk-maren` claim and the tick-14 description were rewritten to assert a ruling
("… ruled that Aru's account prevails and the matter is decided." / "… issued an official ruling
that adopts Aru's account and closes the matter."), with the delivered map untouched:

```
check_bible     : CLEAN … 0 violations                                  exit=0
support_check   : … SOURCE-SUPPORT 20/20 … RESULT PASS                  exit=0
map_obligations : OBLIGATIONS raw=20 mapped=20 … RESULT PASS            exit=0
```

So all three gates are blind to the ruling class; the delivered restraint is an **editorial**
choice verified by manual review, not a gate outcome. (This replicates the r96 V46 pattern for a
new class.)

**Chain demo — C2's discharge, replicated.** In a mirrored scratch root (tool + contract +
fixture, as the self-test itself mirrors), dropping the r97 tick-13 edge and the r98 tick-14
edge respectively:

```
$ python3 …/chain-demo/corpus/tools/dependency_freeze.py …/chain-demo/corpus/fixtures/r97-crossing-acknowledgment
FREEZE r97-crossing-acknowledgment: events 6/6; dependency-edges 4/5; relations 1/1
FINDING REDUCTION-DETECTED: event acknowledgment-aru-records lost depends_on ['response-evin-salt-court']
RESULT FAIL                                                            exit=1
$ … r98-clerk-filing
FREEZE r98-clerk-filing: events 7/7; dependency-edges 5/6; relations 1/1
FINDING REDUCTION-DETECTED: event clerk-filing-open lost depends_on ['acknowledgment-aru-records']
RESULT FAIL                                                            exit=1
```

The r97 edge — V46's recorded r97 FAIL (unfrozen) — is now pinned and its scratch drop is
detected; the r98 edge is likewise. The freeze layer catches *inventory* mutations; it does not
(and cannot) detect the semantic ruling class of §4 — only the digest/inventory classes.

**PATH-MISMATCH bound intact.** A byte-identical copy at a foreign path exits 2:
`FINDING PATH-MISMATCH: pin r98-clerk-filing names corpus/fixtures/r98-clerk-filing …` exit 2.

## 6. Cross-checks of the round's other claims (replica scope, bounded)

- **C1(a):** `--self-test` prints `SELF-TEST 17/17` `RESULT PASS` exit 0 with
  `self_test_mismatch` persisted (`self_test.expected` has 17 entries; contract `153ebc5b…`), and
  the code path `emit(2, [("SELF-TEST-MISMATCH", …)])` confirms the exit-2 alignment
  (`dependency_freeze.py:572`).
- **C1(b):** the `--freeze` migration path is present (`dependency_freeze.py:376` prints
  `MIGRATED {name}: path-less legacy pin now names …`); S2's addendum documents the before/after
  on a scratch contract copy (before: `SCOPE-REFUSED … already names None`, exit 2; after:
  `MIGRATED …`, exit 0). I did not re-run the legacy-pin mutation myself (S2 and the self-test
  cover it); recorded as read-evidence, not my receipt.
- **C1(c):** the delivered contract `precedence` text names the full exit-2 order (UNPINNED-FIXTURE
  / CONTRACT-INVALID → FIXTURE-MISSING → PATH-MISMATCH → FILE-MISSING / MALFORMED-JSON /
  MALFORMED-MODEL → DIGEST-MISMATCH → INVALID-ARGUMENTS → SELF-TEST-MISMATCH) and the
  path-less-legacy migration sentence; `map_obligations.py` and `support_check.py` are
  byte-identical to baseline (`86b52949…`, `55a5eb27…`).
- **C2:** chain 6/6 PASS with both new pins path-bound; V46's r97 FAIL discharged (my §5
  replication, independent of seat V06).
- **C3:** confirmed end-to-end (§3, §4); the r95 map repair is byte-minimal (V15 PASS, my diff
  of the map against `9a3d648` shows only line 49) and r95 receipts are unchanged.

## 7. Bounded observations (evidence, not verdicts on other seats)

- **O1 — carried stale sentence in `corpus/tools/README.md`.** The delivered text (lines 99,
  103, 123, 179, and the new line 232) says the self-test scratch "is created under the
  repository root and is not gitignored". The delivered `.gitignore` contains
  `*-self-test-*/` (added at r97 closure `9d25df9`; present in baseline `9a3d648`), and
  `git check-ignore -v dependency_freeze-self-test-abc/` → `.gitignore:4:*-self-test-*/`
  (match). The "not gitignored" clause is false in the delivered text; the r98 addendum's
  "unchanged in r98" carries the r94-class wording forward. The r97 closure record (C-4)
  already recorded the gitignore discharge. Doc-accuracy bound for the closure pass.
- **O2 — literal imprecision, same file.** `corpus/tools/README.md:283` says
  "`git diff 9a3d648 -- corpus/tools/` lists only `dependency_freeze.py` and
  `dependency-freeze-contract.json`". At the delivered revision the command lists three files
  (`git diff --name-only 9a3d648 -- corpus/tools/` → `README.md`, `dependency-freeze-contract.json`,
  `dependency_freeze.py` — the README itself is the third). The sentence's *intent* holds
  (no other tool code changed; verified hashes above), but the literal claim is falsified by
  its own file's modification.
- **O3 — scan-window artifacts (no positive assertion).** `README.md:9` "…or convert either
  account into a verdict" and `README.md:11` "…an adjudication…" appear `neg-before=False` in my
  50-char window but are negated in the fuller sentence ("does not change … or convert";
  "It is not evidence of … an adjudication"). Same class as r96 V46 O5. No surface asserts a
  finding, verdict, adjudication, or ruling.
- **O4 — the r98 knowledge note's receipt paragraph is stale on one sentence.** It says the C1
  files "still read their r97-closure bytes at this pass's measurement" — true at S5's
  20:28:35 pass, false at the delivered revision (`dependency_freeze.py` `03d04365…`, contract
  `153ebc5b…`). The note instructs re-measurement before citing, so the bound is disclosed;
  flag for the closure doc pass.
- **O5 — no institution exists to rule.** No institution entity is created (the registry is
  prose-only; `clerk-maren` is `kind: character`), and the five inherited fixtures contain no
  tribunal/registry/authority surface (token scan). The lane's earlier institutional-record
  precedent (`corpus/fixtures/r10-registry-witness/`) is bounded the same way — verified quotes:
  `corpus/fixtures/README.md:209-210` "The blank public destination does **not** assert a
  different destination or settle whether Sella's report is true", and
  `corpus/knowledge/2026-10-12-lore-decision-table.md:112` "This is an authored second
  perspective, not external corroboration or canon resolution." The r98 note's cross-reference
  to r10 is accurate.
- **O6 — the note/README/map all bound the office wording as attributed self-description, not
  identity or authority proof** (`README.md:15`; map `:62`; r98 note "First-appearance bound").
  Consistent across surfaces; no over-claim found in the r98 note.
- **O7 — parent-tree stray (not this seat's write; r94-F01 class, observed).** The parent repo
  `/home/vgpnk/Projects/shokunin` carries one untracked file, `baseline-analyze.txt` (105 bytes,
  mtime 20:30:10), whose content is a failed-command redirect:
  `python3: can't open file '/home/vgpnk/Projects/shokunin/analyze.py': [Errno 2] No such file or
  directory`. It is not mine (no command of mine ran outside the lane root; my writes are this
  report and `V39-scratch/` only), and seats V13 and V54 independently record the same file.
  Evidence for the closure hygiene pass; zero strays attributable to this seat.

## 8. Limits of this seat

Same-lane replica review on the delivered bytes: lexical/structural scans plus hand clause
analysis, on scratch copies only. Not source authentication, canon truth, rights or permission
review, not an admission decision, and not a verdict on C1/C2 beyond the spot-checks above.
Producer reports were read for cross-consistency only; S1's report landed after my first
finalization check and was then read and cross-checked (its receipts match mine). No external
URL was fetched; no network was used.

**Bottom line: PASS — the official-ruling reading is not constructible as an assertion on the
delivered r98 bytes: every `finding`/`verdict`/`adjudicat*` token sits under negation, the only
positive institutional surfaces are the filing act and the `OPEN` status record (bounded by
"asserts no office beyond the filing" and "assigns no authority beyond the filing itself"), no
prior in-world institution exists anywhere in the chain, and the closest surviving constructions
collapse to an official *status record*, not a ruling; the C3 whole claim itself replicates
(6/1/7/7, 20 obligations, `check_bible` CLEAN, `support_check` 20/20 PASS, `map_obligations`
raw=20 mapped=20 PASS, chain 6/6, census 172), the class is invisible to all three gates (probe
B PASSes them with an inverted ruling claim), and the r97-edge `REDUCTION-DETECTED` demo
discharging V46's r97 FAIL was independently replicated.**
