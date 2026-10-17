# JDEP5 — Capabilities assessment (round-92 FOLLOW-UP)

Seat JDEP5, world-bible lane (`lore-shokunin/`). Judged tree: committed HEAD
`c4d4823b9a8165a88e8199af136e62d6e961b6b9` (baseline `396c568`).
`git status --porcelain --untracked-files=no` was empty at seat start and at write
time; the only untracked paths are sibling follow-up artifacts under
`.ufo/waves/round-92/followup/`. No tracked file was modified by this seat; no
commit or push. Scratch: three `mktemp` files under `/tmp`, all removed; `df -i /tmp`
sat at `IFree=15351..15474` (inode pressure, file-frugal).

**Question posed to this seat:** recommend for or against a FOURTH row in the
`SCORECARD.md` `## Capabilities` table (current rows: *provenance stop-cause
assessment* r88, *checker-regression discrimination* r91, *in-world excerpt support
verification* r89), candidate *none* — the r92 anchor-based re-derivation is process,
not repertoire — or argue otherwise; evidence must be runnable.

**Recommendation: AGAINST — admit no fourth row this round; the table stays at three
rows.** No r92 deliverable is a new repertoire mechanism with a passing runnable
demonstration, which is what `AXES.md` §Capabilities requires for a row to enter
(cited in M9). The nearest candidate — anchored instruction-surface re-derivation /
certification — has no implementation in the tree (`tools/certify_boundary_doc.py`
absent; `B3-certify-spec.md` is a spec by design), and the certification run that did
happen at the frozen tree (peer seat JDEP1, untracked follow-up artifact, judged tree
`c4d4823`) is **overall FAIL, blocking on gate (b) anchor resolution**. Rows 2 and 3
both ran at the frozen tree and remain operational (M5, M6); the round's gains there
are activation and hardening of existing rows, which is not repertoire.

## Work performed

- Read the row contract (`AXES.md:57-64`), the delivered table (`SCORECARD.md:72-78`,
  three rows), the r92 wave spec and W2's scorecard proposal, and the r92 depth
  artifacts `T1.md`/`T1-certification.json`, `CB.md`/`CB-audit.json`, `B3.md`,
  `B3-certify-spec.md`, `SF1.md`/`SF1-freeze.json`, `Q1-r92-debt.json` (all committed;
  wave-path line refs were read from the committed tree).
- Read the peer follow-up artifacts `JDEP1-certification.json`/`JDEP1.md` and
  `JDEP4.md` (untracked follow-up files) and cross-checked their load-bearing
  findings with my own commands (M4, M8).
- Ran at HEAD: identity/freeze; the r92 corpus numstat; the certifier-absence sweep;
  the boundary doc's structure, replay and a 15-span anchor sample; the C9 watch's
  pinned pair; the row-2 verbatim check (`JDEP4-check.md`) in both modes; the row-3
  support command — three positive receipts and five failure-contract probes.
- Two 60 s wait-checks (one background call, timestamps + directory listings):
  `t0 10:27:20` → `H4-census.json H4-lineage.json H4-probes.json JCAL1-delta.json
  JCAL3-evidence.json JCAL3.md JCAL5-delta.json SF1-freeze.json SF1.md SF2.md`;
  `t1 10:28:20` → adds `H3.md H3-r92-discrimination.json H3-r92-replay.json
  H3-r92-scan.json H4.md JCOV1.md JCOV2.md JCOV3-census.json K1.md`;
  `t2 10:29:20` → adds `JCAL2.md JCAL2-receipts.json JDEP1-certification.json
  JDEP4-evidence.json JDEP4.md`. No JDEP5-blocking dependency existed: the work-wave
  artifacts are committed and self-contained; peer artifacts were read where present.
- Repo writes: this report only. No `JDEP5-*.json` was needed; every receipt is pasted
  inline.

## Before → after measurements

**M1 — identity and freeze.** Exact commands and observed output:

```sh
git rev-parse HEAD                → c4d4823b9a8165a88e8199af136e62d6e961b6b9
git status --porcelain --untracked-files=no → (empty)
sha256sum corpus/fixtures/check_bible.py    → ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
```

**M2 — what r92 actually changed (the admission surface).**

```sh
git diff --numstat 396c568..c4d4823 -- corpus/
44      0  corpus/fixtures/README.md
8       6  corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md
282     160 corpus/knowledge/holder-assessment-boundary.md
9       8  corpus/knowledge/r88-sourced-inspiration-decision-table.md
163     0  corpus/knowledge/r91-c9-watch.md
38      17 corpus/tools/support_check.py
git diff --name-only 396c568..c4d4823 -- SCORECARD.md → (empty)
find corpus/fixtures -mindepth 1 -maxdepth 1 -type d | wc -l → 166
```

Classification: documentation and map text, one watch log append, one existing tool's
failure-contract hardening. No new tool, no new fixture directory (166, as at the r91
census), no new executable or fixture mechanism — nothing that could carry a new row's
evidence pointer. The `## Capabilities` table itself is untouched by the round.

**M3 — the nearest candidate has no implementation.**

```sh
ls tools/                                → ls: cannot access 'tools/': No such file or directory
find . -name "*certify*"                 → ./.ufo/waves/round-92/patches/B3-certify-spec.md
git grep -n "certify_boundary_doc" HEAD  → spec/debt text only (B3-certify-spec.md:10; Q1-r92-debt.json; SF1.md:206 "…is absent")
ls corpus/tools/                         → README.md  support_check.py
sha256sum corpus/tools/support_check.py  → 55a5eb2753901be70f2647008fc6379626654922fe94aed141e7f3a3be2b442c
```

**M4 — the delivered document and its certification state.** My own run at HEAD
(structure + Gate-B replay + anchor sample), observed output:

```text
doc_sha256=8e1fe8774a70f06c31efd783b4313a1639c1da4bcfd830be92134e8964536728
doc_lines=671
h1_count=1 duplicate_headings=[] instruction_markers=[]
replay_receipts=3/3
replay_cases=14/14
mismatches=[]
anchor raw counters 38-39: PASS            anchor to_holder ambiguity 277-277: PASS
anchor raw accumulation 72-76: PASS        anchor from_holder ambiguity 290-290: PASS
anchor index() 85-91: PASS                 anchor latch 315-321: PASS
anchor holder detail 168-175: PASS         anchor comparison gate 322-322: PASS
anchor relation ambiguity 184-184: PASS    anchor tick comparison 323-326: PASS
anchor disclosure template 208-210: PASS   anchor qualified chain (corrected needle) 330-335: PASS
anchor first-record form 339-341: PASS     anchor detail call sites 328-329: PASS
anchor CLI/exit 418-428: PASS
```

(The first anchor pass flagged `330-335` on my needle `not uniquely resolvable`; that
literal lives in the helper at `:168-175`, while `:330-335` builds the qualified form
from `holder_identity_detail` calls at `:328-329` — a probe-needle artifact, corrected
above and re-run PASS. Sample, not B3 gate C's full catalog.)

Two doc-anchor residuals are real and independently confirmed: the document's own
line 330 cites the item-level first-stop tests as `` `:198-203` `` while the delivered
span is `:200-205` (doc lines 164, 331 and 540 give the correct range), and peer seat
JDEP1's untracked certification at this same tree reports
`"overall": "FAIL — blocking on gate (b): anchor resolution"` with gates (a) 3/3
blocks / 14/14 cases PASS, (c) PASS, (d) PASS, (e) PARTIAL — my independent run
reproduces gates (a) and (c) exactly.

**M5 — row 2 still runs at the frozen tree (no change needed).** The committed
evidence pointer `.ufo/waves/round-91/followup/JDEP4-check.md` re-run verbatim:

```text
mode=delivered  … RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression   exit=0
mode=e97613c    … REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved             exit=2
```

The C9 watch's pinned pair (`corpus/knowledge/r91-c9-watch.md:10-20`) at HEAD:
`sha256sum` matches the pin; `r91-c1-null-chain` → 1 violation `rc=1`;
`r91-c1-tick-unresolved` → the definite tick line plus the separately qualified chain
line, 3 violations `rc=1` — byte-equal to the watch's check-log row 1. The round's
watch work is the row-2 mechanism operating, not new repertoire.

**M6 — row 3 runs and its failure contract is hardened.** At HEAD:

```text
support_check.py corpus/fixtures/r87-myth-cluster          → 22/22  RESULT PASS     rc=0
support_check.py corpus/fixtures/r88-m3-maya-cluster       → 12/12 (10 JSON + 2 editorial)  RESULT PASS  rc=0
support_check.py corpus/fixtures/r89-inspiration-paraphrase→ retelling-support-only 1/1, RESULT PASS  rc=0
map without inventory declaration   → FAIL: map must contain exactly one expected inventory declaration / RESULT FAIL   rc=1
malformed inventory declaration     → FAIL: expected inventory declaration is malformed      / RESULT FAIL            rc=1
missing map (/dev/null)             → FAIL: claim-to-excerpt map not found                   / RESULT ERROR           rc=2
fact table outside a section        → FAIL: fact table must be under a JSON facts or Editorial rows heading / RESULT ERROR rc=2
missing cluster                     → FAIL: cluster directory not found: corpus/fixtures/no-such-cluster / RESULT ERROR rc=2
```

Gap in my receipts only: the cell-count-mismatch → `RESULT ERROR` variant did not
reproduce from my crafted probe (it fell through to the inventory check); SF1's
pre-commit worktree receipt records it (`SF1.md:218-219`). This is a tool hardening of
an r89 row, not a new capability.

**M7 — the certification wording versus the committed receipts.** The commit message
says (verbatim):

```text
C1 (depth, the r91 deferral): the boundary doc re-derived ANCHOR-BASED (seat D2's
candidate applied directly; certified by T1: 3/3 receipts, 14/14 replay cases)
```

but `grep -rl "certified by T1" .ufo/waves/round-92/` → no files, and the committed
`T1-certification.json` (present in `c4d4823`) has `"overall": "FAIL"` with its 3/3
receipts / 14/14 cases under `baseline_control` — T1 ran before the candidate existed.
My own replay gives 3/3 and 14/14 on the delivered doc (M4), so those numbers are true
of it as re-measured, but no committed artifact records that run, and the full
gate-(b) certification fails (M4). For this seat's question the upshot is narrow and
decisive: the candidate capability has no passing, committed, runnable certification
receipt to point at.

**M8 — cross-checked peer findings relevant to any certification claim.** Peer seat
JDEP4 (untracked) found the R8 headline label doubled at HEAD; my check:
`git show HEAD:corpus/knowledge/r88-sourced-inspiration-decision-table.md | sed -n '40p' | grep -o "Failed-gate disposition (clarified r92)" | wc -l` → `2`.
The delivered doc's own provenance header still reads "Refreshed at round-90 closure"
/ "Landed at round-90 closure" and `verified-at: RUNTIME REPLAYED … at ca7f9ef`, while
its content is the r92 anchor remap (sha `8e1fe87…`, the candidate shape CB measured at
671 lines) — the header does not identify the r92 re-derivation.

**M9 — the gate and the table.** `AXES.md:57-64`: "…Rows enter only through a round
that demonstrates the capability running; a capability without a passing demonstration
in the round report is pre-claiming and does not enter the table." `SCORECARD.md:72-78`
shows three rows; the r92 commit does not touch `SCORECARD.md` (M2).

**Table verdict: `unchanged` — no fourth row admitted; rows 1-3 remain operational
(M5, M6).**

## Findings & named debt

**F1 — verdict basis (all receipts above).** (a) The round added no new mechanism:
its corpus delta is docs/map/README text, a watch log append, and hardening of an
existing tool (M2); no new tool, fixture, or command exists to be a row's evidence
pointer (M3). (b) The nearest candidate is inadmissible: `tools/certify_boundary_doc.py`
is absent by design (M3), and the ad-hoc certification at this tree is FAIL on gate (b)
(M4). (c) Even if implemented, what r92 demonstrated is a repair process — its product
is a document, not a repeatable mechanism; the document's own provenance header still
names r90 (M8). (d) Rows 2 and 3 gained activation/hardening, which per the r90
precedent ("no third row … not new repertoire") is not a new row.

**F2 — per-candidate disposition.**
- *Anchored instruction-surface re-derivation / certification*: process; no mechanism;
  certification FAIL at the frozen tree → no row (and pre-claiming if asserted).
- *C9 watch periodic re-check*: row 2's own mechanism operating; first check-log row
  appended corpus-resident → row 2, not a new row.
- *Support-command failure contract*: hardening of row 3's tool (M6) → no new row.
- *R8/R9 governance edges*: prospective policy text; no runnable mechanism → not
  repertoire.

**F3 — optional table text refreshes (PENDING-L1; not rows).** Row 3's printed receipt
in `SCORECARD.md` says `r88-m3-maya-cluster` → `10/10`; at HEAD it is `12/12`
(10 JSON + 2 editorial, WARN closed; M6). Row 2's evidence pointer could additionally
name the corpus-resident watch `corpus/knowledge/r91-c9-watch.md`, whose check-log row 1
and pinned pair I replayed byte-for-byte (M5). I recommend these as text refreshes only;
they change no capability and enter no row.

**F4 — named debt (capability-claim hygiene).** (i) The commit-message certification
wording is not backed by any committed passing receipt (M7); (ii) the B3 certifier
implementation is absent and is the standing completion contract for any future
certification row (M3, F5); (iii) the boundary doc's provenance header/`verified-at`
still describe r90 (M8); (iv) the doc's `:198-203` anchor is stale and JDEP1 records
orphaned-tail anchor debt (M4); (v) the R8 label is doubled at HEAD (M8). Items (iii)-(v)
are for the C1/depth judges to rule on; I record them because any fourth row of the
certification class would inherit them.

**F5 — the bar for a future fourth row (if L1 wants one).** A committed, fail-closed
certifier (B3's `tools/certify_boundary_doc.py` or equivalent) that returns
`CERTIFICATION PASS` on a frozen tree would meet the `AXES.md` gate for a row such as
*instruction-surface certification*, with the command as evidence pointer. Until that
exists and passes, the correct table state is unchanged.

**F6 — bounds of this seat's evidence.** The anchors check is a 15-span sample, not
B3 gate C's full 140-site catalog; the JDEP1/JDEP4 artifacts cited are untracked
follow-up files used as peer evidence and cross-checked where cheap; the cell-mismatch
failure variant was not re-run by me (cited to SF1); JDEP1 counts the doc at 672 lines
where `wc -l` reports 671 (identical sha — a counting convention nuance). All primary
verdict evidence is from the committed tree at `c4d4823`.

## Handoff

- **Verdict for L1:** capabilities table **unchanged** — do not admit a fourth row this
  round; no r92 deliverable meets the `AXES.md:57-64` demonstration gate. The nearest
  future candidate is named with its completion contract in F5.
- **For the closure record:** the round's capability-relevant work is row-2 activation
  (watch check-log row 1, re-checked) and row-3 hardening (failure contract), both with
  runnable receipts in M5/M6; optional row text refreshes are F3 (PENDING-L1).
- **Debt handed over:** F4 (certification wording, missing certifier, doc provenance
  header, stale anchor, R8 duplication).
- **Files:** this report only —
  `lore-shokunin/.ufo/waves/round-92/followup/JDEP5.md`. No tracked write, no commit,
  no push. Scratch: three `/tmp` files, removed.
- **Gaps:** no JDEP5-blocking dependency was missing; peer artifacts used are untracked
  and cited as such. Two 60 s wait-check receipts are in "Work performed".