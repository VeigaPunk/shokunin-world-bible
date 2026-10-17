# JCOV5 — Coverage judge #5 (sibling adjacency), round 89

Seat JCOV5, round-89 FOLLOW-UP wave (world-bible lane). Judged on the DELIVERED
tree at `1b09f3ff8016b26a2259e086f673d0112f4f54e5` (baseline
`51b286b5a1e503e6e6ace1f8da0bd606a3c10d94`); `git status --porcelain` empty at
start. Baseline side is an unmodified `git archive 51b286b` under
`/tmp/jcov5-base`. Repo writes by this seat: this report and
`followup/JCOV5-probes.json` only. No commit, no push, no sibling-repo write.

Verdict vocabulary: improved / harmed / unchanged / unprovable-but-better. No
scalars. Every measurement below carries its exact command and observed output.

**Question posed to this seat.** Do the four delivered r87 excerpts, the R9/R10
artifacts, or the ETCSL ledger marker read as chousa province or kotodama
province? Record rejected-fit reasoning per sibling.

Dependencies: two 60s wait-checks were run (2026-10-17T04:30:12-03:00 and
04:31:12-03:00); all twelve sibling follow-up reports (JCAL1, JCAL3, JCOV1,
JCOV3, JCOV4, JDEP2, JDEP4, H1, H2, H5, P4, V2) were PRESENT at both checks, so
no gap was carried. Every artifact this seat judges is in the delivered tree;
the two sibling corpora are read-only reads.

## Work performed

- Read on the delivered tree: `PROVINCE.md`; the four r89 excerpts plus
  `lowwater-hymn-excerpt.md`, `symbolism-clause-map.md`, `inspiration-note.md`,
  `README.md`, `sources.json` in `corpus/fixtures/r87-myth-cluster/`; the R8/R9/R10
  rows and r89 integration notes in `corpus/knowledge/r88-sourced-inspiration-decision-table.md`;
  `corpus/knowledge/r89-cross-cluster-contradiction.md`; the R9 demo fixture
  `corpus/fixtures/r89-inspiration-paraphrase/` (all files);
  `corpus/knowledge/reference-ledger.md` (numbered, plus the r89 diff);
  `corpus/knowledge/seed.md:18-29`; `l0-questions.md`; `SCORECARD.md`.
- Read read-only in the siblings, to test each rejected-fit ruling against the
  sibling's own delivered corpus rather than its declaration alone:
  `chousa-shokunin/PROVINCE.md:3-17`, `chousa-shokunin/corpus/knowledge/{claim-verification-r2.md,archives-verified-r9.md,anchor-boundaries-r4.md}`;
  `kotodama-shokunin/PROVINCE.md`, `kotodama-shokunin/corpus/knowledge/synthesis/{worldbible-integration-contract.md,source-discipline-calibration.md,consistency-verification-checklist.md}`,
  `kotodama-shokunin/corpus/knowledge/verification/{real-world-inspiration-boundaries.md,citation-format-and-source-registry.md,provenance-audit-ledger-format.md}`.
- Ran the probes recorded below. Scratch: `/tmp/jcov5-base` (baseline archive),
  `/tmp/jcov5-{base,head}-{exits,out}.txt`.
- Second pass (same seat): every measurement below was re-run against a fresh
  `git archive 51b286b` baseline (`/tmp/jcov5b-base`) with new receipts
  (`/tmp/jcov5b-*`), and every sibling citation was re-grepped on the current
  sibling trees. All numbers reproduced; three line citations and one wording
  claim were corrected in place (`citation-format-and-source-registry.md:36`,
  `source-discipline-calibration.md:26`, `PROVINCE.md:13-15`, M2's
  "byte-identical"). Raw receipts: `followup/JCOV5-probes.json`.

## Before → after measurements

**M1 — closure census and delta (my own re-derivation, not the wave's).** Exit
status of every fixture directory at both revisions, one fresh process per dir:

```sh
cd /tmp/jcov5-base && for d in corpus/fixtures/*/; do python3 corpus/fixtures/check_bible.py "$d" >/dev/null 2>&1; rc=$?; echo "$(basename "$d") $rc"; done > /tmp/jcov5-base-exits.txt
cd /home/vgpnk/Projects/shokunin/lore-shokunin && for d in corpus/fixtures/*/; do python3 corpus/fixtures/check_bible.py "$d" >/dev/null 2>&1; rc=$?; echo "$(basename "$d") $rc"; done > /tmp/jcov5-head-exits.txt
awk '{print $2}' /tmp/jcov5-base-exits.txt | sort | uniq -c
awk '{print $2}' /tmp/jcov5-head-exits.txt | sort | uniq -c
join -j1 <(sort /tmp/jcov5-base-exits.txt) <(sort /tmp/jcov5-head-exits.txt) | awk '$2!=$3{print "CHANGED",$0}' | wc -l
```

```text
baseline:  lines=149   31 0 / 118 1
delivered: lines=160   32 0 / 128 1
exit changes across the 149 common dirs: 0
```

Stdout (not just exit) compared per directory, `###<dir>` framed:

```text
common dirs compared: 149
stdout-changed dirs: 4
 - r87-probe-multi-invalid
 - r87-probe-record-and-chain
 - r88-mixed-stop
 - r88-nonholder-stop
```

New directories (11), with delivered exit status: the four `r89-c1-*` branch
fixtures, `r89-c1-multi-cause-valid`, the three `r89-f2-*`, `r89-fn2-control`,
`r89-fn2-unresolved-chain-break` all exit 1; `r89-inspiration-paraphrase` exits
0. So the 31→32 clean delta is the R9 demo, and the C1 claim
(`4 changed + 11 new of 160 dirs, 0 exit changes`) **reproduces exactly**.

**M2 — the "22/22 under the D1 rule" figure is rule-dependent.** M4's own
baseline support script, re-run verbatim on both trees:

```sh
python3 -c 'import json,pathlib; p=pathlib.Path("corpus/fixtures/r87-myth-cluster"); ...'   # M4-verify.json before.d1_support.command
```

```text
delivered tree: D1 r87 baseline: facts=22 OK=8 not-OK=14; delivered source excerpts=['dune-register', 'gate-witness', 'lowwater-hymn', 'shell-charter', 'tide-bell-tally']
baseline tree:  D1 r87 baseline: facts=22 OK=8 not-OK=14; delivered source excerpts=['lowwater-hymn']
```

The numeric result is identical on both trees (`facts=22 OK=8 not-OK=14`); only
the trailing excerpt inventory differs. That script measures whole-statement
containment, so it cannot produce the after-state; the 22/22 number rests on a
*different* rule — the 14 per-anchor `grep -nF` checks in
`patches/M4-verify.json`.

**M3 — anchors and cluster replay on the delivered tree.** Every
`M4-verify.json.after.checks` anchor re-grepped against its delivered excerpt
path:

```text
E1..E6, R1..R4, T1..T4  PASS
anchors on delivered tree: 14/14  fails=[]
```

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
python3 corpus/fixtures/check_bible.py corpus/fixtures/r89-inspiration-paraphrase; echo "exit=$?"
grep -nF -- 'moved to the west stair' corpus/fixtures/r89-inspiration-paraphrase/ash-ledger-excerpt.md
```

```text
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
```

**M4 — ledger shape and the ETCSL marker.**

```sh
python3 - <<'EOF'  # count lines starting with '|', split cells
EOF
git diff 51b286b 1b09f3f -- corpus/knowledge/reference-ledger.md
```

```text
table rows incl header: 6   (header + 5 data rows; every row 4 cells)
```

The r89 diff touches exactly one line: the ETCSL row's `Use here` cell, now
`external-only / text not delivered at lore; citation is a research lead with
verified line locators, not delivered support. …`. The other four rows are
byte-identical.

**M5 — sibling receipts.**

```sh
sha256sum kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md
wc -l kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md
git grep -n "kotodama-lore-adjacency" 1b09f3f | wc -l
git grep -n "file_sha256\|contract_id" 1b09f3f -- corpus/ | wc -l
```

```text
e834f50309bd93b11894e7f96d03f7000fc224a3a3ea4d654fd4d1aaaa0831f7   (206 lines)
committed tree 1b09f3f: kotodama-lore-adjacency 0 hits; receipt fields in lore corpus 0 hits
working tree at this writing: the only hits are this wave's own follow-up files
(JCOV4.md:220, K1.md:84,93,154, this report) and K1's uncommitted l0-questions.md:5 append
```

## Findings & named debt

**F1 — coverage verdict: improved (bounded).** Agrees with JCOV1 and JCOV4. The
14 previously metadata-only facts each gain a source-local, grep-hittable anchor
in a delivered excerpt (14/14); the denominator resolves (7/7 pointers, 7/7
claim source IDs); both fixtures replay `CLEAN`, exit 0; the census delta is
exactly as declared. The excerpts' footers also track their `sources.json`
`reliability_note` values one-for-one (gate-witness/dune-register "unverified",
tide-bell-tally "ordering is fixture-local", shell-charter "records a pledge, not
its performance"), so the delivered support text does not overstate its sources.

**F2 — the 22/22 figure is not reproducible by the script that produced the
baseline (new).** M2: the same M4 script prints `OK=8` on the delivered tree as
on the baseline. The "22/22 under the D1 rule" claim is therefore true only under
the anchor rule, and the round's headline evidence mixes two rules under one
number. Not a harm to the corpus (the anchors do match, M3), but the coverage
receipt should state which rule yields which number; the D1 support row at
`r88-sourced-inspiration-decision-table.md:16` is anchor-based, so 22/22 is the
rule-conformant reading and `OK=8` is an artifact of M4's stricter script.

**F3 — chousa: rejected-fit holds; method re-derivation without cross-reference.**
Ruling: the four excerpts, the R9/R10 artifacts, and the ledger marker **cannot
be absorbed by chousa and do not read as chousa province**, but R9 and the
ledger marker restate a method chousa already owns and has hardened.

- chousa owns it by declaration: "source hierarchy (primary / secondary /
  aggregator / unsourced); citation chaining and hop resolution; claim-vs-source
  verification" (`chousa-shokunin/PROVINCE.md:5-7`), and it refuses "external
  live-target research without operator approval (loopback-only otherwise)"
  (`:13-14`).
- chousa has already implemented the same rule: `verify-claims` resolves each
  claim's verbatim span byte-exactly (`claim-verification-r2.md:56`), and its
  source boundary fails closed on URLs — `CLAIM_SOURCE_EXTERNAL` (crit, "url
  source refused (no external fetch)") at `claim-verification-r2.md:49`. That is
  precisely the distinction the ledger marker draws ("external-only / text not
  delivered") and that R8's non-delivery disposition governs.
- chousa has already named R9's fidelity limit: "Named residual distortion, not
  fixed: `text` cells paraphrase — only `span` cells and chain anchors are
  verbatim, so read span+pointer, not prose" and "**verifying a conversion is not
  verifying the original**" (`archives-verified-r9.md:176-182`); and
  "anchors and claim spans matched by SUBSTRING" as a named limit
  (`anchor-boundaries-r4.md:31-35`). R9's "a fixed-string anchor proves only that
  the phrase occurs in the delivered representation" is the same finding.
- Rejected-fit reasoning: the deliverables are lore's canon-support records
  (in-world `source_id` → delivered excerpt → claim), not research-window
  records with a ranked source list, hop ledger and external-target approval
  table; chousa has no in-world source concept and no canon. Absorption would be
  a province violation in the other direction.
- Named debt: the rule text is re-derived locally without citing the chousa
  records that already establish the same limits, and the boundary question the
  lane itself raised at `l0-questions.md:3` ("C3 source-method adjacency with
  chousa … confirm boundary — research method shared, world-bible record stays
  in lore?") is still unanswered. Per "Out of province → report, never absorb",
  the honest cheap repair is a cross-reference line in R8/R9, not a new rule.

**F4 — kotodama: rejected-fit holds; sibling entries already cover R8/R9's
subject matter more fully.** Ruling: **not kotodama province**, but the overlap
is larger than the r87 scan saw.

- Rejected-fit for the four excerpts: they are narrow attributed in-world
  records (a witness slip, a register, a charter clause, a tally) for source IDs
  that already existed at r87. They specify no phonology, morphology, script,
  naming slot grammar, era staging, costume/material system, or variant myth
  register — none of the generative surfaces kotodama's contract §5 requires —
  so they are record inputs on lore's side, not a system. kotodama's contract §3
  hands "who holds a belief; whether any supernatural claim is true" to lore, and
  the excerpts assert no supernatural claim, so no handoff was owed.
- Rejected-fit for R10: bible-wide contradiction handling is lore's by kotodama's
  own contract — §3 row "Contradiction | Finding, reproducer, impacted candidate
  records, repair alternatives | Bible-wide verification and canon resolution |
  Kotodama never silently repairs a canon conflict"
  (`worldbible-integration-contract.md:43`). The delivered R10 record preserves
  that boundary ("A real-world parallel cannot adjudicate this in-world
  disagreement", `r89-cross-cluster-contradiction.md:32`). Cleanest in-province
  artifact of the three.
- Rejected-fit for the ledger marker: kotodama **refuses** it — "real-world
  rights/attribution rulings on reference works" (`kotodama-shokunin/PROVINCE.md:13-15`)
  — and chousa cannot own it either (external-target research needs operator
  approval). lore's own `PROVINCE.md:3,7` and `seed.md:26-29` claim it. The
  marker is lore's by elimination as well as by declaration.
- **Named debt (the real finding):** R8's materiality/disposition screen and R9's
  delivery-mode taxonomy duplicate a sibling's existing, sourced craft:
  kotodama's `verification/real-world-inspiration-boundaries.md` §4 already
  defines the stop / consult / unknown routes and a non-additive sensitivity
  screen, §5 a transformation checklist with a "residue test", and §6
  sacred-material stop rules; its `verification/citation-format-and-source-registry.md:36`
  already requires distinguishing "published translation versus own translation
  versus machine-assisted draft" with `(to-verify)` on unreviewed translations
  (R9's `translation` mode, one lane over); its `synthesis/source-discipline-calibration.md:26`
  already states "Source quality and borrowing permission are separate
  questions" (the R8/R1/R2 separation). None of these is cited by the R8/R9 rows.
  This is the reverse of "Out of province → report, never absorb": the material
  is not absorbed, but a sibling's method is silently re-derived instead of
  referenced.
- **Refinement to JCOV4's contract note:** JCOV4 recorded the missing
  `kotodama-lore-adjacency` acknowledgement as an open seam. Precisely, the
  contract's precondition is "Before the first transfer, both lanes read the
  whole file and record `lane, contract_id, revision, file_sha256, reader,
  read_at, evidence_pointer`" (`worldbible-integration-contract.md:11-12`). No
  lore↔kotodama transfer occurred in r89 (lore authored its own in-world text;
  kotodama delivered no packet), so the precondition is **not yet breached** —
  it is untriggered, not violated. What *is* stale is the r88 L0 premise:
  `l0-questions.md:4` still reads "that file is absent in both lanes (kotodama's
  synthesis/ dir is empty)", while the file is present and tracked at 206 lines,
  sha256 `e834f503…`, authored by kotodama (answering the L0 line's own "should
  kotodama (the generator) or lore (the world-bible recorder) author it?"). In
  the working tree, K1's follow-up append (`l0-questions.md:5`, uncommitted at
  this writing) already updates that premise; it is not part of `1b09f3f`.

**F5 — the ledger's Spence row is structurally detached from the table
(pre-existing, on a C2 surface).** `reference-ledger.md:3-8` is the contiguous
four-column table (header, delimiter, 3 method rows, ETCSL row); lines 9-12 are
blank + a three-line prose paragraph; line 13 is the Spence row. With no header
and no delimiter row adjacent, it does not render as a table row. Introduced at
`51b286b` (r88 closure) — `git log -S "Lewis Spence" --oneline -- corpus/knowledge/reference-ledger.md`
→ `51b286b` — and untouched by r89's one-line ETCSL edit, so it is inherited,
not caused. Low severity (the row's content is correct and 4-celled) but it is
on the ledger the C2 claim names, and a reader parsing the table loses the
Spence registration.

**F6 — agreeing deferrals (not re-derived here).** JCOV4's D1 (no in-corpus
claim-to-excerpt map; the 14 path/line anchors live only in
`.ufo/waves/round-89/patches/M4-verify.json`) and D2 (no R9 delivery-mode
declaration on the four new excerpts, `grep -rn "Delivery mode" corpus/fixtures/r87-myth-cluster/`
→ exit 1, even though delivering four excerpts is a content touch of r87) stand
on my read too; I confirmed both and add no contradiction. JCOV4's D4 (marker
literal) also stands: the table asks for `external-only / unverified`
(`r88-sourced-inspiration-decision-table.md:15`), the delivered marker reads
`external-only / text not delivered at lore`.

## Handoff

- **Verdict recommendation: C2 coverage — improved (bounded)**, on 14/14
  delivered anchors, a resolving 22-fact denominator, two `CLEAN` replays, and a
  census delta that reproduces exactly (149→160 dirs, 31→32 clean, 4 stdout
  changes, 11 new, 0 exit changes).
- **Sibling rulings (the seat's deliverable):** all three artifact groups
  (four excerpts / R9+R10 artifacts / ledger marker) are **rejected as
  chousa/kotodama province** and correctly stay in lore — for R10 and the ledger
  marker by the siblings' own declarations, for the excerpts because they
  generate no system and assert no supernatural claim. Named debt is
  cross-referencing, not re-homing: R8/R9 re-derive chousa's claim-vs-source
  limits and kotodama's inspiration-boundary/translation-labeling craft without
  citing them.
- **Cheap repairs for the closure commit:** (1) state in the coverage receipt
  that 22/22 is the anchor rule and that M4's script yields `OK=8` on both trees;
  (2) add one cross-reference line each to R8/R9 pointing at
  `kotodama-shokunin/corpus/knowledge/verification/{real-world-inspiration-boundaries.md,citation-format-and-source-registry.md}`
  and at `chousa-shokunin/corpus/knowledge/{claim-verification-r2.md,archives-verified-r9.md}`;
  (3) repair the Spence row into the ledger table; (4) land K1's
  `l0-questions.md` update (in flight in the working tree) or re-state the line
  in the closure commit — the r88 premise at `l0-questions.md:4` is obsolete
  once landed.
- **Sibling cross-checks:** JCOV1, JCOV3, JCOV4, and JDEP4 also rule coverage
  improved (bounded); H2 confirms the census delta; H1 finds no harm on any
  axis; H5's documentation-surface harms (three r89 F2 README cause strings,
  stale `holder-assessment-boundary.md`, no Round-89 section in
  `corpus/fixtures/README.md`) are consistent with this report's F2/F5 and
  belong in the same closure pass.
- **Second-pass re-verification:** all M1–M5 measurements were re-run against a
  fresh baseline archive and reproduced the numbers above; three line citations
  and one wording claim were corrected in place. Raw receipts:
  `followup/JCOV5-probes.json`.
- **Files written by this seat:** `.ufo/waves/round-89/followup/JCOV5.md`,
  `.ufo/waves/round-89/followup/JCOV5-probes.json`. No tracked source, patch,
  commit, or push; sibling repositories read-only.
