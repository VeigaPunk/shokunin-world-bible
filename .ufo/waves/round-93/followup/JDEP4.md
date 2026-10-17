# JDEP4 — Capabilities assessment (round-93 FOLLOW-UP)

Seat JDEP4, world-bible lane (`lore-shokunin`). Judged tree: committed HEAD
`65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` (the r93 WORK commit; baseline
`87779a0`). `git status --porcelain --untracked-files=no` was empty at seat
start and at write time; the only untracked paths are the sibling follow-up
artifacts under `.ufo/waves/round-93/followup/`. All probes ran from
`/home/vgpnk/Projects/shokunin/lore-shokunin`. No tracked file was modified; no
commit or push. Scratch: several single `mktemp` files under `/tmp`, each
removed immediately after its run (`df -i /tmp` sat at `IFree=13771`, 99% used —
file-frugal observed).

**Question posed to this seat:** recommend for or against a FOURTH
`capabilities` row; evidence must be a runnable command. Candidates examined:
(i) *boundary-document certification* — the r93 committed certifier
`corpus/tools/boundary_doc_check.py`; (ii) the discrimination-harness promotion
to `corpus/tools/discriminate_check.py`; (iii) the third sourced cluster
`r93-m2-kojiki-cluster`; (iv) the C9 watch's second re-check.

**Recommendation: FOR — admit exactly one fourth row, `boundary-document
certification` (first-working round r93), carrying the bounds in F2.** The r92
closure wrote the admission contract itself (JDEP5 F5): "A committed, fail-closed
certifier … that returns `CERTIFICATION PASS` on a frozen tree would meet the
`AXES.md` gate for a row such as *instruction-surface certification*, with the
command as evidence pointer." r93 delivered that contract and this seat
demonstrates it running on the committed tree: one command returns `CERTIFIED`
exit 0 (3/3 receipts, 14/14 cases replayed byte-exact against the live pinned
checker), and three independent fail-closed probes each return exit 1 with a
named `FAIL:` line (receipt drift, anchor beyond range, checker-pin drift).
The row must claim **lexical certification only** — semantic (AST/content-signature
anchor) validation and contradiction-class detection remain named r94 debt; the
C9 gate as delivered misses CB-audit's verbatim contradiction phrasing (F3/F4).
Every other candidate is an existing row's hardening or instance, not repertoire.

## Work performed

- Read the row contract (`AXES.md` §Capabilities, parent repo: rows enter only
  through a round that demonstrates the capability running; a capability
  without a passing demonstration is pre-claiming), the delivered
  `SCORECARD.md:72-80` table (three rows: r88 stop-cause, r91
  checker-regression discrimination, r89 in-world excerpt support
  verification), the r90→r92 precedents (r90 JDEP4 "against — pre-claiming";
  r91 JDEP4 "for, bounded"; r92 JDEP5 "against — nearest candidate has no
  implementation", whose F5 names this round's completion contract), the r93
  wave spec, and the r93 work commit message.
- Read the r93 work artifacts bearing on the candidates: `CERT.md`,
  `CB-audit.md`, `X2.md`, `Q1.md` + `patches/Q1-r94-proposal.md`,
  `patches/W2-scorecard-r93.proposal.md`, and the committed
  `corpus/tools/{boundary_doc_check.py,discriminate_check.py,README.md}`.
- Ran on the committed tree: identity/pin checks; the certifier positive run;
  four certifier fail-closed probes (receipt drift, anchor beyond range,
  checker-pin drift via the `e97613c` source, missing doc); two C9
  contradiction phrasings (CB-audit's verbatim `{details}` sentence and the
  tool's own `{expected}` needle); `discriminate_check.py` in both modes; the
  row-3 support command on `r93-m2-kojiki-cluster` and `r88-m3-maya-cluster`;
  the R8 dossier through the certifier and its own embedded replay; R9/R8
  appendix placement greps; fixtures-README round-index and doc-header greps.
- Two 60 s dependency wait-checks (one background call, timestamped directory
  listings): `12:15:39-03:00` → `JCAL1-delta.json JCAL1.md JCAL1-tuples.json
  JCAL3.md`; `12:16:39-03:00` → unchanged. Post-window listing (12:26) added
  `H4-census.json H4-lineage.json H4-probes.json H5.md JCAL2.md P3.md`; all
  were read and cross-checked against this seat's independent measurements
  (M8). No blocking gap.
- Repo writes: this report and `followup/JDEP4-evidence.json` only.

## Before → after measurements

**M1 — identity and pin.** Exact commands and observed output:

```sh
git rev-parse HEAD                                   → 65838f867d6ece8e7b8bdcc4ffc667a08a1b785e
git status --porcelain --untracked-files=no          → (empty)
sha256sum corpus/fixtures/check_bible.py
  → ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
sha256sum corpus/tools/boundary_doc_check.py
  → 8e439b5129d0e2d26e6fac725f0231f07059e8dedf462c5219115240d371af3c
sha256sum corpus/tools/discriminate_check.py
  → 6c7b7cd8b6676619c6f00eb692c946cfe8d007dc963de5c4a2114757f6108eef
sha256sum corpus/knowledge/holder-assessment-boundary.md
  → 7f815a9389c415de906ecd4fe14795ee30d5935ae0ed13ee0a5c6b06a74ec33e (648 lines)
```

The checker hash equals the pin inside the certifier (`boundary_doc_check.py:389`)
and the r91 C9 watch. `corpus/tools/boundary_doc_check.py` and
`corpus/tools/discriminate_check.py` are tracked at `65838f8` — r92 JDEP5 M3
measured the certifier **absent**; that is the before→after delta this verdict
turns on.

**M2 — the candidate running (positive run, `time`-measured).** Command:
`python3 corpus/tools/boundary_doc_check.py`. Observed:

```text
CHECK receipt replay: PASS
CHECK code anchors: PASS
CHECK document structure: PASS
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED
real	0m0.380s   exit=0
```

Byte-identical to CERT's patch-stage run, H5's landing replay
(`H5.md:53`), and JCAL2's A1 — four independent executions agree.

**M3 — fail-closed probes on the committed tool (scratch doc copy, removed).**

```sh
# probe: receipt drift (mutate one receipt byte in a /tmp copy)
FAIL: stdout mismatch for r85-control (receipt line 355)   CERTIFICATION FAIL   exit=1
# probe: anchor beyond EOF (check_bible.py:212-224 → 212-9999)
CHECK code anchors: FAIL
FAIL: unresolved anchor check_bible.py:212-9999: checker has 428 lines   CERTIFICATION FAIL   exit=1
# probe: reverted checker (--checker <e97613c source>) — silent-revert tripwire
FAIL: checker hash pin: e2bb9639a3247284... != pinned ff9fd2aa6811a813...   CERTIFICATION FAIL   exit=1
# probe: missing --doc
FileNotFoundError traceback; true exit=1 (captured without a pipe)
```

(Probe-discipline note: a first sed needle,
`provenance chain break; expected from_holder 'mira', got None`, matched zero
lines — the delivered doc's receipts replay schema fixtures such as
`r85-control`, not the r91 pair — so that mutation was a verified no-op, not a
false pass. The receipt-drift probe above mutates a receipt line that exists.)

**M4 — the C9 gate's needle precision (the sharpest finding).** The gate is two
required needles plus one forbidden needle
`holder identity is not uniquely resolvable: {expected}`
(`boundary_doc_check.py:390-391`). CB-audit's falsification probe appended the
contradiction with the tree's own historical phrasing, which uses `{details}`
(the `c2ab3d0` doc contained `…: {details}; provenance tick` — CB-audit's
parity table). Re-run against the committed tool:

```sh
printf '\nLegacy rule: holder identity is not uniquely resolvable: {details}; provenance tick findings are qualified.\n' >> $T
python3 corpus/tools/boundary_doc_check.py --doc $T   → instruction_markers=0 CERTIFIED   exit=0
printf '\nLegacy rule: holder identity is not uniquely resolvable: {expected}; provenance tick findings are qualified.\n' >> $T
python3 corpus/tools/boundary_doc_check.py --doc $T   → FAIL: C9 semantics: required markers missing or a legacy tick-qualification claim present
                                                        CERTIFICATION FAIL   exit=1
```

So: the gate fires on the `{expected}` instantiation and **certifies CB-audit's
verbatim `{details}` sentence** — and would not have caught the historical harm
class as it actually appeared. JCAL2's A3 used the `{expected}` phrasing, hence
its finding 1 ("directly closes the holes CB-audit falsified") overclaims for
the contradiction class; the commit message's "both adversarial probes exit 1"
likewise holds for the pin probe plus a `{expected}`-phrased contradiction, not
for CB-audit's verbatim probe. The pin probe itself is genuinely closed (M3).
This is a bound the row must carry, not a disqualifier — see F2/F3.

**M5 — the discrimination-harness promotion (row-2 hardening, both modes).**

```sh
python3 corpus/tools/discriminate_check.py
  → mode=delivered checker_sha256=ff9fd2aa… matches_pin=True
    r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1
      pinned_semantic_gate=PASS
    r91-c1-tick-unresolved: (same shape) pinned_semantic_gate=PASS
    RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression   exit=0
python3 corpus/tools/discriminate_check.py --checker e97613c
  → REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved — pinned delivered semantics not present   exit=2
```

This closes r91-JDEP4's F2(iii) bound (the pass/fail wrapper was wave-resident
`.ufo/waves/round-91/followup/JDEP4-check.md`; the pointer is now
corpus-resident). C5 additionally showed a hash-only flip
(`matches_pin=False`, semantics PASS → `REGRESSION-DETECTED on checker-hash`,
exit 2 — `C5.md:77-82`), a row-2 bound the tool itself prints.

**M6 — row-3 receipts at the delivered tree.**

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster
  → INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15
    SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; RESULT PASS   exit=0
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
  → RECEIPT JSON-FACTS 10; EDITORIAL-ROWS 2; TOTAL-ROWS 12
    SOURCE-SUPPORT 10/10; EDITORIAL-ANCHORS 2/2; RESULT PASS   exit=0
```

Two receipt discrepancies for the record: the r93 commit message says the
Kojiki support receipt is "10 JSON + 3 editorial"; the committed cluster
measures **12 JSON + 3 editorial** (the wave claim and JCAL1's census agree
with the measurement). And `SCORECARD.md:78` (row 3's printed receipt) still
says `r88-m3-maya-cluster` → `10/10`; measured 12/12 (10 JSON + 2 editorial) —
the r92 JDEP5 F3 text-refresh remains pending.

**M7 — the R8 dossier's certification scope.** The dossier is NOT inside the
certifier's contract, by design:

```sh
python3 corpus/tools/boundary_doc_check.py --doc corpus/knowledge/r93-r8-worked-example.md
  → FAIL: C9 semantics: required markers missing or a legacy tick-qualification claim present
    FAIL: no checker output receipt blocks found / CERTIFICATION FAIL   true exit=1
# its own embedded replay (extracted sh block, run from repo root):
R8 record fields: 5/5 (all PASS)   exit=0
```

The C9-marker requirement makes the tool a boundary-doc certifier, not a
general document certifier; the dossier demonstrates via its own five-field
traceability check. Adjacent placement greps: the R9 manual gate sits inside
the R9 appendix (count 1) and the R8 duplicate label is resolved (count 1) in
the committed decision table — Q92-002's core repair landed as claimed.

**M8 — dependency waits and sibling cross-checks.** Wait-checks
`12:15:39` / `12:16:39` (only `JCAL1-*`/`JCAL3` present; gap noted,
non-blocking). Post-window (by 12:26), read and cross-checked:

- **H5** (`H5.md:53`): independent certifier replay — identical output and
  exit 0 (agrees with M2); `H5.md:85` independently found the README gap
  (below); `H5.md:87` confirms AST anchors remain named r94 debt.
- **JCAL2**: A1 CERTIFIED exit 0 (agrees with M2); A2 pin tripwire and A3 C9
  tripwire exit 1 — A3 used the `{expected}` phrasing (see M4 for the
  sharpening); its robustness-debt item 3 (unguarded `--doc`/`--checker`
  reads → traceback, still rc=1) matches my missing-doc probe; its A4 README
  finding matches mine.
- **H4-census.json**: delivered census at `65838f8` against the r92 B1
  authority (166 rows) — consistent with JCAL1's 167 dirs (0 changed + 1 new).
- **P3** (`P3.md:96`): log proposal says "capabilities table unchanged" — the
  one open classification disagreement, addressed in F4.
- **JCAL1/JCAL3**: census tuple agreement (no drift, checker pin match), no
  finding contradicts M1–M7.

## Findings & named debt

**F1 — Recommendation: FOR a fourth row, `boundary-document certification`,
r93 — bounded.** Proposed row text:

| Capability | What it can now do | Evidence pointer | First-working round |
|---|---|---|---|
| boundary-document certification | Certify the delivered holder-assessment boundary doc with one fail-closed command: replay every checker receipt byte-exact against the live pinned checker, line-existence-check `check_bible.py:NNN[-MMM]` citations, check structure (one H1, no duplicate headings, no instruction markers), pin the checker SHA-256, gate the C9 markers/needle — `CERTIFIED` exit 0 only when all pass, a named `FAIL:` line and exit 1 otherwise | `python3 corpus/tools/boundary_doc_check.py` → `CERTIFIED` exit 0 (3/3 receipts, 14/14 cases, 2/2 anchors); fails closed: receipt-drift, anchor-beyond-range, and checker-pin-drift probes each exit 1 (this seat's M3; JCAL2's A2/A3) | r93 |

Grounds: (a) the capability demonstrably runs on the committed tree with
receipts from four independent executions (M2, H5, JCAL2-A1, CERT's
patch-stage run agreeing byte-for-byte); (b) it fails closed, demonstrated by
this seat on three classes and by JCAL2 on two adversarial classes, with
single-failure isolation; (c) it meets the letter of the admission contract
the r92 closure itself wrote (JDEP5 F5: committed + fail-closed + `CERTIFIED`
on the frozen tree = admissible), and closes r92's named debt F4(ii) ("the B3
certifier implementation is absent and is the standing completion contract for
any future certification row"); (d) precedent: row 3 (r89) is the same
evidence class — a reproducible lexical preflight whose README explicitly
disclaims judgment — and before r93 certification was a manual, FAIL-prone
multi-gate process (the r92 record's own gate-(b) failure + manual
re-certification), after r93 it is a deterministic one-command gate. The
capabilities axis question is "what the shokunin can now *do*": before r93 it
could not certify the boundary doc with a command; now it can.

**F2 — Bounds the row must carry (named, not netted).**
(i) **Lexical scope only.** Anchor checks are line-existence against the
checker's 428-line count (2 strict-format citations validated of ~119
colon-number references in the doc — CB-audit's count); in-range but wrong
numbers pass (CB-audit's `:1-2` probe); AST/content-signature validation is
named r94 debt (commit message; CERT.md:185; H5.md:87).
(ii) **The C9 gate is needle-narrow.** Two required needles plus the single
forbidden needle `{expected}`; CB-audit's verbatim `{details}` contradiction
still certifies (M4) — and that `{details}` phrasing is the form the
historical `c2ab3d0` harm actually used. Contradiction-class detection is r94
debt. The gate is a real tripwire (fires on the needle it names, M4 probe 2),
but the row and any closure text must not describe it as closing CB-audit's
contradiction probe.
(iii) **Boundary-doc scope.** The tool certifies that document; `--doc` on the
R8 dossier exits 1 by design (M7). Generalization is not claimed.
(iv) **Unguarded input reads.** Missing `--doc`/`--checker` crash with an
uncaught traceback, exit 1 — fails closed, but without a named failure line
(JCAL2 item 3; my probe).
(v) **Undocumented tool.** `corpus/tools/README.md` (36 lines) has no
certifier section; `boundary_doc_check` has zero references outside
`.ufo/waves/round-93/` (my grep `grep_exit=1`; H5.md:85; JCAL2 A4). The row's
evidence pointer is the command itself (argparse-discoverable); the README
section — which should also state bounds (i)/(ii) and the r94 debt naming —
is doc-only follow-up (H5's and JCAL2's handoff converge on this).
(vi) **Pin coupling is intentional.** Any future checker change must
co-update `EXPECTED_CHECKER_SHA256` and the doc's pins in the same round or
certification fails; a future FAIL is the tripwire working, not a tool bug.

**F3 — Sharpenings of sibling claims (verdicts unchanged).**
(a) JCAL2 finding 1 ("the landed tool returns named rc=1 for both" of CB-audit's
falsified modes) overclaims the contradiction class: A3 injected
`{expected}`; CB-audit's verbatim `{details}` probe certifies (M4). (b) The r93
commit message's "both adversarial probes exit 1" is true for the pin probe
and a `{expected}`-phrased contradiction only. (c) CERT.md:185's "does not
implement … C9 semantic review" describes the pre-landing patch, not the
committed tool (JCAL2 item 4 concurs). None of these changes the FOR verdict;
they tighten what closure text may say.

**F4 — Reconciliation with the no-row reading (open item for L1; verdict
unchanged).** `P3.md:96` proposes the capabilities table unchanged; W2's
scorecard proposal says keep it unchanged "unless L1 adopts a verified change",
and its C1 paragraph critiques the *pre-integration* candidate for lacking the
hash pin and C9 gate — the committed tool has both (M1, M3, M4), so that
audit's factual basis is superseded on this point. The r91 F4 logic applies
verbatim: L1 should adopt one classification. Under the FOR reading, admit the
row with F2's bounds (the row name and one-liner claim lexical certification
only). Under the no-row reading, the mechanism lives in the depth/calibration
record and the r94 completion contract (AST anchors + contradiction-class
gate + README section) stands. The one dishonest state is entering a row that
reads as semantic certification — that would be the pre-claiming error r90
named. This seat recommends FOR because the demonstrated delta is exactly the
class rows 1 and 3 were admitted for, and the r92 closure pre-committed to the
admission rule this round satisfied.

**F5 — Not-rows dispositions (per the r90/r92 precedent: activation,
hardening, and instances are not repertoire).**
- *Discrimination-harness promotion* → row-2 hardening + evidence-pointer
  refresh (`corpus/tools/discriminate_check.py`; both modes re-verified, M5);
  closes r91-JDEP4 F2(iii). Not a row.
- *`r93-m2-kojiki-cluster`* → a row-3 instance; its support receipt passes on
  the committed tree (M6). Not a row.
- *C9 watch second re-check* → row-2's mechanism operating; the committed
  watch now carries two distinct dated rows (`2026-10-17`,
  `2026-10-17 (r93)`) with "Next re-check: r94" — the Q92-010 next-pointer is
  now present in wording (row 2's hash is abbreviated `ff9fd2aa…d1421`; the
  full hash remains in row 1 and the pinned header). Not a row.

**F6 — Adjacent named debt (capability-claim hygiene; not this seat's remit to
rule).** (i) Row 3's SCORECARD receipt is stale (`10/10` → measured 12/12,
M6); (ii) the Kojiki support receipt is misquoted in the r93 commit message
("10 JSON" → measured 12 JSON, M6); (iii) the fixtures README still has no
Round-91 section and no Round-93 section for the new cluster (Q91-003 open;
measured: round headings end at 88/89/90/92); (iv) the boundary doc's stale
provenance header ("Refreshed/Landed at round-90 closure") remains at
`65838f8` (Q91-002 residue) — no certifier gate can catch it; (v) the certifier
README section + r94 debt statement (F2(v)); (vi) r94 debt queue: AST/
content-signature anchors, contradiction-class C9 gate, guarded input reads
(JCAL2's queue concurs).

## Handoff

- **Verdict for L1: FOR a fourth capabilities row — `boundary-document
  certification`, r93 — with the F2 bounds attached.** The runnable evidence is
  M2/M3 (verbatim above): `python3 corpus/tools/boundary_doc_check.py` →
  `CERTIFIED` exit 0; receipt-drift / anchor-beyond-range / checker-pin-drift
  probes → exit 1 with named failures. Raw receipts in
  `followup/JDEP4-evidence.json`.
- Row-2 pointer refresh (`discriminate_check.py`, exit 0/2 both verified) and
  row-3 receipt refresh (r88-m3 12/12) are text-only follow-ups (F5/F6), not
  rows.
- F3's sharpenings should be reflected in closure wording (JCAL2 finding 1 and
  the commit message overclaim the C9 contradiction closure).
- Files written by this seat: `followup/JDEP4.md`,
  `followup/JDEP4-evidence.json`. No tracked-file edits, no commit, no push,
  no sibling-repo writes; all scratch removed.
- Gaps: none blocking. The full follow-up roster had not landed at this seat's
  wait window; cross-checks cover the seats bearing on this verdict (H4, H5,
  JCAL1–3, P3). JAXIS's synthesis and L1's axis verdicts were not yet present;
  this seat rules only the capabilities question.
