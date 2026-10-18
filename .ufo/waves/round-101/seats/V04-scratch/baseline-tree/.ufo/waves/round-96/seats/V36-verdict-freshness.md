# V36 — verdict-freshness (round 96)

Seat: V36 verdict-freshness. Role: independent per-axis verdict for **FRESHNESS** on the
**delivered bytes** — were the carried freshness findings repaired, merely absent, or still
reproducing, and what did the round actually deliver on this axis? Basis: the two
freshness-surface verifier reports read in full — **V28 `freshness`** and **V29 `doc-parity`** —
each reconciled against my own re-runs on the frozen revision (stale-pin sweep, receipt
replays, contract/pin cross-checks, demo reproductions). Integration items (index/README/SKILL/
C9 additions) are **L1's**, judged here as delivered-or-pending state only. Read-only; this file
is the sole artifact written (scratch in `.ufo/waves/round-96/seats/V36-scratch/`; no commits,
no pushes, no network, no nested agents).

## Read state and freeze

- HEAD `60dba0c2aa344860b10a2fc63e00468d1b134f27` (r95 close — SCORECARD admitted section;
  `dcb2d92..HEAD` touches `SCORECARD.md` only). Working tree exactly the declared r96 set:
  `M LOG.md` (round declaration), `M corpus/tools/{README.md, map-obligations-contract.json,
  map_obligations.py}`, untracked `.ufo/waves/round-96/`, `corpus/fixtures/r96-crossing-response/`,
  `corpus/knowledge/r96-response-scope-note.md`, `corpus/tools/{dependency-freeze-contract.json,
  dependency_freeze.py}` — nothing else. `git diff --stat HEAD` over the r87/r88/r89/r93/r94/r95
  fixtures: empty (inherited corpora byte-untouched).
- Delivered revision measured by me (16 new bytes; **every producer-claimed hash reproduced
  exactly** on my own `sha256sum` runs):

```
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
97b76bb8b1fea97f166ef7586eba69c427ec15bbe7b34eb5345ec65c936493b6  corpus/tools/map-obligations-contract.json
965b29cd41a8af14293eb2e1948f58f310e58c6e752b8fe322c5445b20a91f24  corpus/tools/README.md
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
6db32ca24f5eff5baa3ebe589e8d3bcb6b256fec18dee2468211d7d0fae157c6  corpus/knowledge/r96-response-scope-note.md
ff52ced48bf4214721f248328d76da64a42773d44e78154ef1eaf6eb3558c456  corpus/fixtures/r96-crossing-response/README.md
5093d72eb3f22b249033d7ac4c1a85c7df7f5e09bfa673a598aee6a83045bfd8  corpus/fixtures/r96-crossing-response/claim-excerpt-map.md
06b11bec604f6d68e4d4bc43e78093c00ce7fb8fb86c8cac153e24ee41cb2fe3  corpus/fixtures/r96-crossing-response/fictional-excerpts.md
9f973f634cf325a33047020407ffb67b0a0f0a1643e507ebd3771abf9fabf32d  corpus/fixtures/r96-crossing-response/sources.json
ea0225f9270db79685ea6f55828c2031d7ac67cd413b04f28b25770b208815b9  corpus/fixtures/r96-crossing-response/timeline.json
026af0bc2cdab1509f58f0a8235731de681e5ba8e68cc09f952818b5792ae03b  corpus/fixtures/r96-crossing-response/entities.json
c279254bc7de0636d91823b6bf336edc780fad4aade9c63cc4b0ac65cc4a6ff9  corpus/fixtures/r96-crossing-response/relations.json
37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570  corpus/fixtures/r96-crossing-response/contradictions.json
58f5390e5928ebad9b7feb3d60d1351919226a4bb00e2e3b9c4a5457bcc82d37  corpus/fixtures/r96-crossing-response/inspiration-note.md
b5edc2fd3c2e3d4fed0f1c98c17f38f69fc0f4d3c385001db292b79b4d76d4cd  corpus/fixtures/r96-crossing-response/source-excerpt.md
```

- Aggregate md5 of that 16-digest set, sampled three times inside my verification window:
  `dd7a50ac07f669008ef6644925d71460` at 17:56:23, 17:56:57 and 17:58:05 — **frozen** through
  verification (my window 17:38–17:58 local). One mid-window observation: `corpus/tools/README.md`
  was still being finalized by Q2 (my 17:50:5x hash `40ca92c2…` ≠ final `965b29cd…`, mtime
  17:51:26); the final bytes match Q2's report, and I re-read the final addendum text and re-ran
  its receipts against it.
- Carried r95 bytes unchanged where not owned: r95 note `f87ed42a…`, checker `ff9fd2aa…`,
  support_check `55a5eb27…`, boundary doc `7f815a93…`, C9 watch `835c63e5…`.

## Verdict question, answered directly

The carried freshness finding **r95 F-1 is not repaired** — it reproduces exactly on the
delivered bytes and is now doubly superseded (the note pins `9224a684…`; the delivered tool is
`2b0ba815…`, two revisions later). The round's own new bytes introduce **no false pin, no live
HEAD reference, and no dangling revision**: V28's sweep found only the runtime `git rev-parse
HEAD` inside `dependency_freeze.py --freeze` (`:292`), which stores fixed shas; I re-ran the
sweep and every sha the new durable bytes name was the true revision at its stated time, and
every quoted receipt reproduces on the delivered revision (my re-runs below). Two bounded new
items land in durable bytes — **(N-1)** the r96 note records an in-flight, never-delivered tool
revision `6634e176…` (plus the old contract `8173bb97…`), the same self-caveated class as F-1;
**(N-2)** the delivered `dependency-freeze-contract.json` carries a **foreign pin `c3red`
pointing at a scratch path** inside the wave directory. One doc-parity gap confirmed
independently: **(N-3)** the tools README Round-96 addendum registers only `map_obligations`;
`dependency_freeze` has **zero mentions** in `corpus/tools/README.md`. The five L1 closure-doc
sites are still pending and are inventoried with exact texts by V29. Net movement of the axis:
**none** — no repair, no live-pin drift, bounded disclosed items only.

## Carried r95 F-1 — stale revision pin in the r95 knowledge note (REPRODUCES, unrepaired)

`corpus/knowledge/r95-aftermath-scope-note.md:51` still pins the in-flight r95 revision while
the delivered tool has moved twice:

```
$ sed -n '51p' corpus/knowledge/r95-aftermath-scope-note.md   # excerpt
Tool revisions at these receipts (2026-10-17T16:25-03:00): … `map_obligations.py` `9224a684…`. …
Re-run all three commands against the delivered revision before citing these receipts.

$ sha256sum corpus/tools/map_obligations.py corpus/knowledge/r95-aftermath-scope-note.md
2b0ba815326b1cb3f65f7eab1842b85abedb9823228a37adc6a9335edc4a3ba8  corpus/tools/map_obligations.py
f87ed42ad4d42143bb84f13539f2db8ca0d5f221aaf4eaffdbd6874b5ef1ab9a  corpus/knowledge/r95-aftermath-scope-note.md
```

The r95 closure carried this as "correctable next touch"; r96 did not correct it (the note file
is byte-unchanged from the r95 delivery, `f87ed42a…`). Characterisation unchanged from V27/r95:
a timestamped historical receipt provenance with an explicit re-run caveat, whose receipt
values I re-verified green at the delivered revision (§Receipts) — a **real bounded defect
under a strict pin-currency reading**, a **carried condition** under the r94 convention.
Closure action C-F1 below (drop the value or re-pin).

## N-1 — r96 note records the in-flight revision, not the delivered one (same class as F-1)

`corpus/knowledge/r96-response-scope-note.md:55` (durable, non-seat artifact):

```
Tool revisions at these receipts: `check_bible.py` sha256 `ff9fd2aa…` and `support_check.py` `55a5eb27…`
at `2026-10-17T17:43-03:00`; the `map_obligations.py` line was re-run at `17:46-03:00` at revision
`6634e176…` (the r96 C1 hardening in flight; `--self-test` at that revision printed 22 case lines and
the contract file was still `8173bb97…`). … Re-run all three commands against the delivered revision
before citing these receipts.
```

Measured against the delivered tree: `6634e176…` and `8173bb97…` are **not** the delivered
revisions (delivered: tool `2b0ba815…`, contract `97b76bb8…`). The note labels `6634e176…` as
"in flight" and instructs a re-run — the same self-limiting pattern as F-1, with a stronger
in-flight label. I re-ran all three receipts at the delivered revision: values identical
(`OBLIGATIONS raw=16 mapped=16` / `INVENTORY 16/16; 2/2; 18/18` / `RESULT PASS` exit 0), so the
recorded receipt content is accurate and only the revision pin is superseded. V28 observation 3
reaches the same finding; it reads the note more generously ("not repeated with a false pin") —
under a strict pin-currency reading this is the F-1 class recurring in new bytes, and I record
both readings rather than smoothing the item. Closure action C-NOTE below.

## N-2 — foreign `c3red` scratch pin inside the delivered freeze contract

Direct verification (my run):

```
$ python3 -c "import json; c=json.load(open('corpus/tools/dependency-freeze-contract.json'));
  print(list(c['pins'].keys())); print(c['pins']['c3red']['fixture'])"
['r88-m3-maya-cluster', 'r94-paired-crossing', 'r95-crossing-aftermath', 'r96-crossing-response', 'c3red']
.ufo/waves/round-96/seats/V41-scratch/c3red

$ python3 corpus/tools/dependency_freeze.py .ufo/waves/round-96/seats/V41-scratch/c3red
FREEZE c3red: events 3/3; dependency-edges 1/1; relations 1/1
DIGEST eff4b354c092a9c4a3ea6de6857ee1a21be1ab4bafac957568b6813dac8dbd28
RESULT PASS
rc=0
```

A delivered, durable contract file embeds a pin whose `fixture` path is a **round-scoped
scratch directory**, written by a verifier's `--freeze` probe (Q3 §7 discloses it and left it
because V22/V33 receipts quote the pin list; V28 observation 1 and V29 §6 flag it too). It is
inert to chain verification (pins are basename-keyed; the four corpus pins verify — below) but
it is a real tool hazard (`--freeze` on an out-of-corpus path rewrites the delivered contract)
and a doc wart. All four corpus pins match the delivered fixture bytes (my independent digest
comparison: `chain pins match delivered bytes: True`). Closure action C-C3RED below.

## N-3 — `dependency_freeze` is unregistered in `corpus/tools/README.md`

```
$ grep -c "dependency_freeze\|dependency-freeze" corpus/tools/README.md
0
```

The tools README registers `support_check.py`, the boundary-document checker,
`discriminate_check.py`, and `map_obligations.py` (addenda at `:88`, `:101`, `:121`), but the
new r96 gate appears nowhere — its only in-tree documentation is the contract's own
`scope`/`exit_codes`/`self_test` fields. Cross-check worth flagging to L1: V29's proposed
`corpus/fixtures/README.md` Round-96 text says "The new `dependency_freeze` gate (see the tools
README Round-96 addendum) …" — that section does not exist. Either add a `dependency_freeze`
subsection to the tools README (Q2-owned path, or L1 at closure) or re-point that citation to
`corpus/tools/dependency-freeze-contract.json`. Closure action C-TOOLSREADME below.

## N-4/N-5 — remaining low-severity items (disclosed by V28, re-checked by me)

- **N-4 (V28 obs 2):** all five freeze pins carry `revision: 60dba0c…` = HEAD at freeze time;
  for the r96 pin the covered bytes were untracked at `60dba0c`, so the label means "when
  frozen", not "where the content lives". Inert to verification (`compare()` ignores it); the
  contract does not document the field. Verified: `"revision": "60dba0c2…"` at contract
  lines 22/26/64/119/184/259.
- **N-5 (V28 obs 4):** `claim-excerpt-map.md:18` says "The 15 inherited rows carry the **r94**
  JSON pointers … unchanged" — inherited from r95 where it was accurate for 14 rows; J15's
  pointer is r95-authored. "Previously delivered" would be exact; no count, pointer, or gate is
  affected. Also V28 obs 5: Q1's report §8 points to an addendum that is not present
  (report-only; the 24-case contract landed and verifies — confirmed independently by me).

## Live pins — independently re-run, all fresh

- Checker pin: `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` = contract pin
  (`boundary-doc-contract.json`), `discriminate_check.py` pin, C9 watch pin; blob `20c56dbb…`
  identical at `dcb2d92`/HEAD/worktree (V51, spot-confirmed).
- Frozen r93 snapshot digests vs live r93 bytes: **4/4 MATCH** (entities/relations/timeline/
  map); `--frozen .ufo/waves/round-94/frozen/map-obligations-r93` → `SNAPSHOT inputs=4
  digests=verified` / `RESULT PASS` exit 0.
- Chain pins vs delivered bytes: contract per-file digests == measured hashes for all four
  fixtures (`True`), and `dependency_freeze.py` verifies 4/4 clean with the digests printed by
  Q3 (`15ef230e…`, `2527beb9…`, `d541ae64…`, `d422a9b3…`) — my runs byte-identical.
- Boundary document `7f815a93…` fresh; `boundary_doc_check.py` → `CERTIFIED (bounded: …)` exit 0;
  `discriminate_check.py` → `RESULT: DISCRIMINATION HELD` exit 0 (r96 C9 pair held, V51/V26).
- C9 watch file carries the r95 row 4 as its last row (`Next re-check: r96`) — the r96 row is
  owed to L1 (V51 lists the exact append; V29 §4 repeats it).

## Receipts at the delivered revision — my re-runs (freshness of quoted receipts)

- r95 note/README receipts still reproduce: `check_bible` r95 → `CLEAN … 0 violations` exit 0;
  `support_check` r95 → `RESULT PASS` exit 0; `map_obligations` r95 → `raw=15 mapped=15` /
  `INVENTORY 15/15; 2/2; 17/17` / `RESULT PASS` exit 0.
- r96 fixture receipts: `check_bible` → `CLEAN` exit 0; `support_check` → `INVENTORY JSON-FACTS
  16/16; EDITORIAL-ROWS 2/2; TOTAL-ROWS 18/18; DISTINCT-ANCHORS 14/14` / `SOURCE-SUPPORT 16/16;
  … MODES 18/18; VALIDATED-ROWS 18/18` / `RESULT PASS` exit 0; `map_obligations` →
  `OBLIGATIONS raw=16 mapped=16` / `INVENTORY 16/16; 2/2; 18/18` / `RESULT PASS` exit 0.
- `map_obligations.py --self-test` → `SELF-TEST CASES 24/24 pinned` … `RESULT PASS` exit 0
  (contract `self_test.cases` = 24, including `schema_drift` and `inventory_mismatch`).
- Tools README Round-96 addendum receipts reproduced **verbatim** on scratch copies:
  deletion-class demo → `FINDING inventory_mismatch: declared JSON-facts/editorial-rows/total-rows
  14/2/16; observed 13/2/15` / `RESULT FAIL` exit 1; `dual_pointer` demo → `FINDING dual_pointer:
  row P1 (line 23) names a second pointer token 'entities[0].claims[0]' alongside
  entities.json#/0/first_appearance` / `RESULT FAIL` exit 1.
- Non-regression receipt surface: r88 `raw=10 mapped=10` PASS; r93 `12/12` PASS; r94 `14/14`
  PASS; frozen replay PASS; r87/r89 exit 2 `unsupported_map` with unchanged finding text.
- `dependency_freeze.py` chain 4/4 clean (exit 0) and `--self-test` `14/14` `RESULT PASS` exit 0.
- Census: `ls -d corpus/fixtures/*/ | wc -l` → **170** (my count; V29's full replica
  170/36/134/421 validated against a `dcb2d92` materialization 169/35/134/421).
- New-byte pin sweep: r96 fixture directory (all 10 files) — no HEAD/commit/sha256/hex matches
  (grep exit 1); tools README addendum — no sha/hex tokens; map contract — none. The only
  revision pins in new durable bytes are the note's receipt-time provenance (N-1) and the
  contract's `revision` labels (N-4, fixed and resolvable).

## V28 / V29 read and reconciled

- **V28 `freshness` — PASS.** Its four checks (stale-pin sweep; note metadata header; README
  commands replayable; carried r95 wording accurate with updated counts) match my independent
  runs; its five observations are all reflected above (N-2 = obs 1, N-4 = obs 2, N-1 = obs 3,
  N-5 = obs 4/5). One nuance: V28 reads the note's in-flight pin as "not repeated with a false
  pin"; I record the stricter reading (F-1 class recurring) alongside.
- **V29 `doc-parity` — PASS.** Verified the same delivered hashes I froze; census 170/36/134/421
  validated; inventories the five L1 closure-doc targets with exact proposed texts (fixtures
  README Round-96 section ABSENT; corpus/README bullets stale/absent; SKILL.md
  `dependency_freeze` row ABSENT + `map_obligations` row stale; C9 r96 row ABSENT; `c3red`
  anomaly). Its stale-wording classification (live vs historical) is consistent with my checks:
  `corpus/README.md:36` still "(rounds 94–95) … (22 persisted cases)"; `SKILL.md:87` still
  "22 cases (r95 added `map_missing`, `invalid_arguments`)"; the tools README r95 "receipt, not
  a gate" sentence is explicitly superseded in place by the r96 addendum (my read of the final
  bytes). Its proposed fixtures/README cross-reference has the N-3 defect noted above.

## What improved, what was repaired, what was harmed

- **Repaired by this round: nothing.** No carried freshness finding was repaired (F-1
  reproduces); the r94-era and r95-closure repairs are intact at baseline (fixtures README
  Round-95 section `:1177`, corpus/README r95 bullet `:22`, SKILL.md r95 row, C9 watch row 4,
  tools README r95 addendum).
- **Maintained against the round's own change:** Q2's Round-96 addendum keeps
  `corpus/tools/README.md` in parity with the delivered `map_obligations` behavior (both demos
  reproduce verbatim; 24-case self-test matches; the r95 "receipt, not a gate" sentence is
  superseded in place, not silently stale). Every new deliverable byte except the two named
  items is pin-free, and every quoted receipt reproduces. This is freshness *maintenance*, not
  net improvement (the round also created the need).
- **Newly harmed (bounded, all disclosed):** N-1 (r96 note in-flight revision pin — same class
  as F-1, self-caveated, receipt values green) and N-2 (foreign `c3red` scratch pin in the
  delivered contract — new this round, verifier-probe artifact, inert to verification). N-3 is
  a doc-parity gap (new tool unregistered in the tools README); N-4/N-5 are low-severity
  wording/label items. Under the r94 convention (disclosed findings carried as conditions are
  not netted as axis harm) these are **conditions**; under a strict pin-currency/cleanliness
  reading N-1/N-2 are bounded harms. I record both readings rather than smoothing them.

## Verdict

**FRESHNESS: UNCHANGED** — no freshness finding was repaired and none was removed by the
round's own writes; every live pin (checker `ff9fd2aa…`, boundary document `7f815a93…`, frozen
r93 digests 4/4, the four chain content pins vs delivered bytes, C9 watch) is fresh and
verified on the delivered revision; every receipt quoted in the new durable artifacts
reproduces verbatim (including both tools README demos, 24/24 and 14/14 self-tests, chain 4/4);
the round's own new durable bytes carry one self-caveated superseded revision pin (N-1, same
class as the carried F-1) and one foreign scratch pin (N-2), both disclosed, bounded, and named
as closure conditions; N-3 is a doc-parity gap for the new tool; the five L1 closure-doc sites
are pending and inventoried, not concealed. Nothing on this axis improved, and nothing
regressed materially.

**Conditions for L1 at closure (named, from the findings — none are seat-work claims):**

1. **C-F1 (from carried r95 F-1):** drop `9224a684…` from
   `corpus/knowledge/r95-aftermath-scope-note.md:51` or re-pin it to the closure revision; the
   surrounding caveat already tells readers to re-run against the delivered revision.
2. **C-NOTE (N-1):** in `corpus/knowledge/r96-response-scope-note.md:55`, re-pin the
   `map_obligations.py` line to the closure revision (`2b0ba815…`) or drop the value, keeping
   the re-run caveat; optionally note the delivered contract `97b76bb8…` supersedes
   `8173bb97…`.
3. **C-C3RED (N-2):** delete `pins.c3red` from `corpus/tools/dependency-freeze-contract.json`
   at closure (noting V22/V33 receipts quote the pin list), or add a `--freeze` scope guard
   refusing paths outside `corpus/fixtures/`; the four chain pins must stay byte-identical.
4. **C-DOC (from V29 §1–§4, re-checked):** append the fixtures README Round-96 section (census
   **170 / 36 clean / 134 negative / 421 violation lines / zero non-0/1 exits**); add the
   `fixtures/r96-crossing-response` and `knowledge/r96-response-scope-note` bullets and refresh
   `corpus/README.md:36` (rounds 94–96; 24 persisted cases) and `:37`; append the fifth C9
   re-check row (V51/V29 give the exact wording); update `SKILL.md` (`map_obligations` row:
   24 cases, new findings, residuals closed) and append the `dependency_freeze` registry row.
5. **C-TOOLSREADME (N-3):** register `dependency_freeze` in `corpus/tools/README.md` (a
   Round-96 subsection) or re-point V29's proposed fixtures/README citation to
   `corpus/tools/dependency-freeze-contract.json`; do not let closure text cite a tools README
   section that does not exist.

## Limits

- I re-ran V28's and V29's freshness-surface checks and my own pin/receipt sweeps; I did not
  re-derive C1/C2/C3 semantics (other seats own those verdicts), did not re-run the full
  170-directory census sweep myself (I counted directories only, 170; V29's 170/36/134/421
  sweep is cited, not re-measured), and did not audit producer scratch beyond what the named
  items required. My runs are point-in-time (17:38–17:57 local) bracketed by two identical
  aggregate freeze samples; a later write outside the declared set would not be caught here.
- I read V28 and V29 in full (230 and 246 lines). One `corpus/tools/README.md` mid-window
  revision was observed and resolved (final `965b29cd…` matches Q2's report; addendum re-read
  and receipts re-run against the final bytes).
- The `c3red` scratch directory is round-scoped and may be cleaned at closure; its pin then
  dangles (verification-inert, but it is exactly why C-C3RED should run).

**Bottom line: PASS (FRESHNESS: UNCHANGED) — on the frozen r96 delivered revision all live pins
and every quoted receipt are fresh and reproduce (checker `ff9fd2aa…`, boundary `7f815a93…`,
frozen r93 4/4, chain pins 4/4, 24/24 + 14/14 self-tests, both addendum demos verbatim), the
carried r95 F-1 stale pin reproduces unrepaired, and the round's own new durable bytes add one
self-caveated in-flight revision pin (r96 note `6634e176…`) plus one foreign `c3red` scratch pin
in the delivered freeze contract — bounded, disclosed, and carried as L1 closure conditions
(C-F1/C-NOTE/C-C3RED/C-DOC/C-TOOLSREADME); nothing on this axis improved, nothing regressed
materially.**
