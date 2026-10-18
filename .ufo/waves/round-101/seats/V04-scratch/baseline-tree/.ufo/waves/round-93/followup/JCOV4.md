# JCOV4 — fresh-eyes province audit: cluster + dossier + tools (round-93 FOLLOW-UP)

Judgment surface: committed tree `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` (baseline
`87779a0`), tracked tree clean at judgment start and unchanged throughout (no tracked
file touched by this seat). Axes named: **(1) claim fidelity** — every r93 claim in my
slice re-measured on the committed tree; **(2) adversarial surface** — the certifier's
gates probed beyond the baseline run, including the probe re-verification Q1-followup
left open in DEP-H1; **(3) independent agreement** — second independent scan where a
sibling already ran a first (JCOV2's overlap scan, JCAL1's census, JCAL3's both-mode
discriminator); **(4) novel-defect sweep** — failures no seat had yet named. All
scratch under `/tmp/jcov4`, swept at end. Verdict evidence from the committed tree at
`65838f8` only; probes used scratch copies.

## Work performed

- Ran all three committed tools plus the cluster's two validators from the repository
  root; reproduced the full 167-fixture census and diffed it against the committed
  `patches/B1-tuples.json`.
- Adversarial battery on `corpus/tools/boundary_doc_check.py` (five probes, scratch
  copies under `/tmp/jcov4`): legacy C9 claim injected; checker byte-tampered; missing
  doc; missing checker; receipt text mutated — once in prose (probe E, control) and
  once inside a real receipt fence (probe F, using the tool's own `markdown_fences` to
  place the mutation).
- Independent cross-cluster normalized-key scan (entity ids, display names, aliases,
  epithets, relation endpoints, event ids, event endpoints, path-qualified source ids)
  across `r87-myth-cluster`, `r88-m3-maya-cluster`, `r93-m2-kojiki-cluster`.
- Replayed the R8 dossier's embedded 5-field traceability check; spot-verified the
  C1(i) venue repair by line-locating the manual-gate block against the R9 appendix
  span; verified the C9 watch's check-log rows and the discriminate tool in both
  modes; audited index coverage of every new r93 artifact in `corpus/` docs; read the
  committed cluster README's own pending-status hedge against M6's committed report.
- Two 60 s wait-checks (12:18:07 and 12:42:15 −03:00): `followup/` went 3 → 34
  artifacts during the window; no dependency gap (evidence used: committed tree +
  landed sibling reports JCOV1/JCOV2/JCAL1/JCAL3/Q1).
- Cross-read sibling follow-up seats before naming anything: Q1-r93-debt.json (ledger
  N1–N10), JCOV2 (cluster whole-claim audit), JCOV1 (receipt battery), JCAL1/JCAL3
  (census, discriminator). Everything below that they already name is marked
  corroboration; R93-N11/N12 are new.

## Before → after measurements

All commands run from `lore-shokunin/` at HEAD `65838f8`.

**Tool baseline runs (all verified):**

```sh
python3 corpus/tools/boundary_doc_check.py; echo rc=$?
```

```text
CHECK receipt replay: PASS / CHECK code anchors: PASS / CHECK document structure: PASS
replay_receipts=3/3  replay_cases=14/14  anchors=2/2
h1_count=1  duplicate_headings=0  instruction_markers=0
CERTIFIED
rc=0
```

```sh
python3 corpus/tools/discriminate_check.py; echo rc=$?
python3 corpus/tools/discriminate_check.py --checker e97613c; echo rc=$?
```

```text
mode=delivered … matches_pin=True; both fixtures README_exact=True, pairs=1/1, gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
rc=0
mode=e97613c … README_exact=False, pinned_semantic_gate=FAIL (both fixtures)
REGRESSION-DETECTED on r91-c1-null-chain,r91-c1-tick-unresolved
rc=2
```

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r93-m2-kojiki-cluster; echo rc=$?
python3 corpus/tools/support_check.py corpus/fixtures/r93-m2-kojiki-cluster; echo rc=$?
sha256sum corpus/fixtures/check_bible.py
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations   (rc=0)
INVENTORY JSON-FACTS 12/12; EDITORIAL-ROWS 3/3; TOTAL-ROWS 15/15; DISTINCT-ANCHORS 15/15
SOURCE-SUPPORT 12/12; EDITORIAL-ANCHORS 3/3; MODES 15/15; RESULT PASS   (rc=0)
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

**Census (before = committed `patches/B1-tuples.json`, 166 rows; after = delivered tree):**

```sh
PYTHONDONTWRITEBYTECODE=1 python3 -I - <<'PY'  # full per-fixture replay, rows diffed vs B1-tuples.json
PY
```

```text
fixture_dirs=167  exit_counts={0: 33, 1: 134}  violation_lines=421
stderr_nonempty_count=0  unexpected_exit_count=0
vs_committed_B1: changed=[] new=['corpus/fixtures/r93-m2-kojiki-cluster'] gone=[]
checker_sha256=ff9fd2aa…d1421
```

Exactly the claimed "167 dirs (was 166), 0 changed + 1 new, 0 exit changes"
(independently corroborates JCAL1).

**Certifier adversarial battery (scratch copies):**

- Probe A — legacy C9 claim re-injected into a doc copy:
  `python3 corpus/tools/boundary_doc_check.py --doc /tmp/jcov4/legacy-doc.md`

  ```text
  FAIL: C9 semantics: required markers missing or a legacy tick-qualification claim present
  CERTIFICATION FAIL
  rc=1
  ```

- Probe B — checker byte-tampered (`# tamper` appended):
  `python3 corpus/tools/boundary_doc_check.py --checker /tmp/jcov4/tampered-checker.py`

  ```text
  FAIL: checker hash pin: 2f0693cd086480f7... != pinned ff9fd2aa6811a813...
  CERTIFICATION FAIL
  rc=1
  ```

  A+B close DEP-H1's open item ("did NOT independently re-run the adversarial
  probes" — Q1-r93-debt.json): the integration claim "both adversarial probes exit 1
  with named failures" is TRUE on the committed tool.

- Probe C — missing doc (`--doc /tmp/jcov4/no-such-doc.md`):

  ```text
  FileNotFoundError: … No such file or directory: '/tmp/jcov4/no-such-doc.md'
  rc=1   (raw traceback — NOT the named-failure protocol)
  ```

- Probe D — missing checker (`--checker /tmp/jcov4/no-such-checker.py`): same shape,
  raw `FileNotFoundError` traceback, rc=1.

- Probe E (control) — `VIOLATION:`→`VIOLATIONX:` in PROSE (4 prose occurrences exist;
  first attempt landed outside any fence): tool correctly still CERTIFIED, rc=0 —
  receipt detection is fence-scoped, prose mentions are inert. No defect.

- Probe F — same mutation placed INSIDE receipt fence 1 (line 360 of the copy, placed
  via the tool's own `markdown_fences`): 

  ```text
  CHECK receipt replay: FAIL
  replay_receipts=2/3  replay_cases=13/14
  FAIL: stdout mismatch for r85-unique-break-control (receipt line 355)
  CERTIFICATION FAIL
  rc=1
  ```

  The replay half of B3 catches doctored receipts byte-exactly.

**Venue repair (C1-i) line-located:**

```sh
grep -n "^### R[0-9]* appendix\|^\*\*Required record:\*\*\|^\*\*Worked example:\*\*" \
  corpus/knowledge/r88-sourced-inspiration-decision-table.md
```

```text
28:### R8 appendix …   42:**Worked example:** … Kesh Hymn …
44:### R9 appendix — translator known, source/version unknown …
75:**Required record:** add an `R9 manual review` entry … Only a recorded manual `PASS` can clear this gate.
79:**Worked example:** … 2011 reprint of the 1901 translation by M. A. Translator …
87:### R10 appendix …
```

Manual-gate record + restored worked example sit at :75/:79, inside the R9 appendix
span :44–:86 — Q92-002's venue repair verified on the committed tree (corroborates
Q1's closure ruling).

**Dossier replay (embedded check, verbatim):** `gate_result/contrary_evidence/
separability_rationale/scope/next_action` all PASS, `R8 record fields: 5/5`, rc=0.
The record table itself has 8 fields (adds Element/scope pointer, Creator account,
Reviewer/record date); the replay asserts 5 (Q1 R93-N3 corroborated; R1's mutation
result cited there).

**Cross-cluster referent scan (independent, this seat):**

```text
r87-myth-cluster: keys=32  r88-m3-maya-cluster: keys=16  r93-m2-kojiki-cluster: keys=17
r87 ∩ r93: EMPTY   r88 ∩ r93: EMPTY   (r87 ∩ r88: EMPTY, control)
```

Keys: entity ids, casefolded names, aliases, epithets, relation endpoints, event ids,
event endpoints, path-qualified source ids. Second independent corroboration of the
lexical half of the zero-shared-referents claim (JCOV2 ran the first); the semantic
half remains open (R93-N2).

**C9 watch / C3:**

```text
corpus/knowledge/r91-c9-watch.md check-log rows:
| 2026-10-17        | ff9fd2aa… (full 64-hex) | DISCRIMINATION HELD … |
| 2026-10-17 (r93)  | ff9fd2aa…d1421 (abbrev) | DISCRIMINATION HELD — re-check 2 (seat X1, r93) … Next re-check: r94. |
```

Two distinct dated rows, both HELD (claim verified). Residual nuances already in
Q1's Q92-010: abbreviated row-2 hash vs row-1 full hash; shared calendar date.

## Findings & named debt

Per-axis verdicts (this seat's slice; recommendations only — L1 owns):

- **C1 depth slice (dossier + certifier) — improved (bounded).** The certifier
  CERTIFIES the delivered document (exit 0) and now has verified adversarial
  behavior: C9 gate and hash pin both exit 1 with named failures (probes A/B), and a
  doctored in-fence receipt is caught byte-exactly (probe F). Bounds: AST/
  content-signature anchor validation absent (named r94 debt; R1's in-range-wrong-
  anchor CERTIFIED result stands unrefuted); tools/README documents
  `discriminate_check.py` but not `boundary_doc_check.py` — CERT's README hunk was
  dropped at integration (R93-N4, Q1-corroborated; C6 predicted the hunk conflict);
  dossier replay asserts 5 of 8 record fields and the dossier is referenced by no
  corpus doc (R93-N3, Q1-corroborated); Q92-004's stale wave-pointer command remains.
- **C2 coverage slice (Kojiki cluster) — improved (bounded).** Every committed
  cluster claim re-verified: 12/12 + 3/3 receipt PASS, check_bible CLEAN, census
  delta exactly 0 changed + 1 new. Zero-shared-referents is now lexically
  corroborated by two independent scans (JCOV2 + this seat), both EMPTY. Bounds: the
  cluster README itself still says the independent M2-specific scan/semantic review
  is pending, and committed M6.md covers the UNINTEGRATED M1 candidate — so the
  commit-message wording "the namespace check shows empty intersections" overstates
  the committed evidence class (author-side + JCOV2/JCOV4 lexical only; R93-N2).
  Fixtures README has no Round 93 entry (Q92-005 extended; Q1-corroborated).
- **C3 calibration — improved (bounded).** Check-log row 2 landed and both
  discriminate modes reproduce (exit 0 HELD / exit 2 REGRESSION-DETECTED). Bounds:
  Q92-010 residuals (abbrev hash, shared date, unpinned e97613c mention, watch does
  not reference the promoted tool).

**New debt named by this seat:**

- **R93-N11 — `boundary_doc_check.py` missing-input paths exit 1 via raw traceback,
  not the named-failure protocol (NEW).** `main()` calls
  `c9_semantics_check(pathlib.Path(args.doc).read_text())` (`boundary_doc_check.py:349`)
  and `checker_pin_check(args.checker)` (`:346`→`:395`) before the guarded document
  read at `:351-357`; a missing `--doc` or `--checker` therefore raises unhandled
  `FileNotFoundError` (probes C/D: rc=1 with traceback). Fail-closed — no gate hole —
  but the graceful "FAIL document: cannot read …" branch at `:351-357` is unreachable
  for the missing-file case, and the tool's contract "any failed check lists its
  failure" (CERT.md:190's patch README wording) does not hold for these inputs.
  One-line fix (guard both reads, emit named failures). r94 candidate.
- **R93-N12 — dossier replay wording/dependency warts (NEW, minor).** (a) The
  committed replay instruction says "after applying this dossier patch" — the dossier
  is already applied; the phrase is stale integration-era wording in a corpus
  contract doc. (b) The replay reads `.ufo/waves/round-92/patches/E1-edges.md` for
  its E1 comparisons — it resolves today (line 13 carries the worked example;
  verified), but a `corpus/knowledge/` doc's replay depends on a process-artifact
  path, the same fragility class as Q92-004's stale wave-pointer in the decision
  table.
- **Record-integrity corroboration (R93-N5).** The commit message says "support
  receipt 10 JSON + 3 editorial PASS"; the delivered tree measures JSON-FACTS 12/12
  (`M4.md:174` and `M5.md:149` agree; 10 was M1's unintegrated candidate, `M4.md:191`).
  Q1 named it first; this seat's independent receipt run confirms. The r93 closure
  log should record 12.

**Fresh-eyes soundness checks that found nothing new:** support receipt anchors/modes
(JCOV1/JCOV2 already exhaustive — not re-audited beyond re-running); the certifier's
fence-scoped receipt detection (probe E control); the discriminate tool's
`--checker e97613c` mode is a differential demonstration that always exits 2 on a
healthy pinned tree (documented in tools/README:36; a true revert yields INCONCLUSIVE
exit 1 via pin failure — signal hierarchy is sound, noting for the record).

Scratch swept: `/tmp/jcov4` removed.

## Handoff

- Written: `.ufo/waves/round-93/followup/JCOV4.md` only. No commit, no push, no other
  tracked or sibling write; l0-questions.md untouched (nothing rises to operator
  level beyond Q1's ledger).
- **For L1/r94, in priority order:** (1) land the R93-N11 guard (two lines) with the
  AST anchor work so the certifier's r94 pass closes B3 fully; (2) M6's M2-specific
  semantic review (R93-N2) — the lexical half now has two independent EMPTY scans, so
  only the semantic review blocks strengthening the claim; (3) restore CERT's
  tools/README section (R93-N4) + fixtures README Round 91/93 entries (Q92-005 ext);
  (4) dossier replay coverage 5→8 fields and drop the "after applying this dossier
  patch" phrase (R93-N3/N12); (5) r93 closure log records JSON-FACTS 12 (R93-N5).
- Per-axis verdicts above are recommendations only; the round is not admitted here.
- Sibling seats this seat cites rather than repeats: Q1-r93-debt.json (ledger),
  JCOV1 (receipt battery), JCOV2 (cluster whole-claim audit + live fetch), JCAL1
  (census), JCAL3 (discriminator modes).
