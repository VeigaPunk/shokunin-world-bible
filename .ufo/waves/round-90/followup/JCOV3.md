# JCOV3 — coverage judge #3 (denominators)

Verdict on the judged axis (C2 coverage, denominator/pointer angle): **improved**.
Freeze-then-verify (r88-I1): **PASS** — the delivered checker hash-matches X2+X3
composed on `e97613c`. No blocking finding.

Delivered tree judged: `ca7f9ef` (baseline `e97613c`), tracked tree clean; all
scratch under `/tmp/jcov3/`; no repo writes outside
`.ufo/waves/round-90/followup/JCOV3.md` and `JCOV3-denominators.json`.

## Work performed

1. Re-derived the source-attributed JSON-fact census from the raw cluster JSONs with
   an independent resolver (`/tmp/jcov3/denominators.py`): a fact is counted if it
   carries an explicit `source_id` (claims, relations, timeline, contradictions) or is
   a `first_appearance` pointer naming a source.
2. Cross-checked the same count by a second, non-Python method (`grep -c` of
   `"source_id"` / `"first_appearance"` keys per file).
3. Parsed both `claim-excerpt-map.md` tables myself and resolved **every** backticked
   JSON pointer in the "JSON fact and fields" / "Clause reading" cell against the real
   JSON documents (`/tmp/jcov3/denominators.py`), including leaf-vs-node classification.
4. Re-ran the delivered receipt `corpus/tools/support_check.py` on both clusters, then
   reproduced the same N/N with my own parser + own `grep -nF` + own span check
   (`/tmp/jcov3/independent_support.py`), so the receipt is not self-referential.
5. Ran three adversarial controls against the delivered checker (scratch copies only):
   mode mismatch, paraphrase declared on both sides, wrong declared span.
6. Ran the freeze check: applied `X2-c1-nullonly.patch` then `X3-c1-tickonly.patch`
   (C9 ruling composition) to `e97613c:corpus/fixtures/check_bible.py` in `/tmp` and
   compared SHA-256 with the delivered file.
7. Two timestamped 60-second stability checks of HEAD + checker hash + followup dir
   (no blocking dependency artifact was declared for this seat; the target tree was
   already frozen and clean, so the checks are stability receipts, not waits).

Durable artifact: `.ufo/waves/round-90/followup/JCOV3-denominators.json`
(per-fact census, per-row pointer resolution, receipt lines, HEAD stamp).

## Before → after measurements

**BEFORE** — claims in the delivered wave at `ca7f9ef` (commit message, maps, script):

- r87 map: 22 rows (14 JSON rows + 8 hymn rows); r88-m3 map: 10 rows.
- Receipts claimed: r87 22/22, r88-m3 10/10.

**AFTER** — my independent recount (all commands from the repository root):

Raw census, independent resolver:

```sh
python3 /tmp/jcov3/denominators.py
```

```text
=== r87: raw source-attributed JSON facts = 22 {'first_appearance': 7, 'claim': 7, 'relation': 4, 'event': 4}
=== r88-m3: raw source-attributed JSON facts = 10 {'first_appearance': 4, 'claim': 4, 'event': 2}
```

Second method (grep key counts; `source_id` + `first_appearance`):

```sh
cd corpus/fixtures && grep -c '"source_id"' r87-myth-cluster/*.json r88-m3-maya-cluster/*.json \
  && grep -c '"first_appearance"' r87-myth-cluster/*.json r88-m3-maya-cluster/*.json
```

```text
r87: entities 7 + relations 4 + timeline 4 = 15 source_id; entities 7 first_appearance  -> 22
r88-m3: entities 4 + timeline 2 = 6 source_id; entities 4 first_appearance              -> 10
```

Pointer resolution (mission's exact criterion — a row pointing at a non-existent field):

```text
r87: map rows = 22; row pointers checked = 42; non-resolving = 0
r88-m3: map rows = 10; row pointers checked = 10; non-resolving = 0
r87 rows with source_id cell disagreeing with the pointed-at JSON value = 0
r88-m3 rows with source_id cell disagreeing with the pointed-at JSON value = 0
```

Coverage classification of the raw census against row pointers:

```text
r87 raw facts NOT referenced by any row pointer = 2:
  entities[2].first_appearance     (appears_in_map_text=True)
  entities[2].claims[0].source_id  (appears_in_map_text=True)
r88-m3 raw facts NOT referenced by any row pointer = 0
```

Delivered receipt, re-run:

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster; echo "exit=$?"
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster; echo "exit=$?"
```

```text
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS
exit=0
SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS
exit=0
```

Independent reimplementation of the receipt (own parser, own `grep`, own span check):

```sh
python3 /tmp/jcov3/independent_support.py; echo "exit=$?"
```

```text
corpus/fixtures/r87-myth-cluster: rows=22 verified=22 exit_equivalent=0
corpus/fixtures/r88-m3-maya-cluster: rows=10 verified=10 exit_equivalent=0
TOTAL rows=32 verified=32
exit=0
```

Freeze-then-verify (r88-I1):

```sh
git show e97613c:corpus/fixtures/check_bible.py > /tmp/jcov3/compose/corpus/fixtures/check_bible.py
cd /tmp/jcov3/compose && patch -p1 -i .../X2-c1-nullonly.patch && patch -p1 -i .../X3-c1-tickonly.patch
sha256sum /tmp/jcov3/compose/corpus/fixtures/check_bible.py corpus/fixtures/check_bible.py
diff /tmp/jcov3/compose/corpus/fixtures/check_bible.py corpus/fixtures/check_bible.py
```

```text
Hunk #1 succeeded at 321 (offset 2 lines).
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  /tmp/jcov3/compose/.../check_bible.py
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
FREEZE_MATCH=PASS   (diff empty)
```

Two timestamped 60-second stability checks (HEAD, checker hash, followup inventory):

```sh
for i in 1 2; do echo "check#$i $(date '+%Y-%m-%dT%H:%M:%S%z') HEAD=$(git rev-parse --short HEAD) \
  dirty=$(git status --porcelain | wc -l) checker=$(sha256sum corpus/fixtures/check_bible.py | cut -c1-16) ..."; \
  test $i -eq 1 && sleep 60; done
```

```text
check#1 2026-10-17T06:59:41-0300 HEAD=ca7f9ef dirty=16 checker=ff9fd2aa6811a813
check#2 2026-10-17T07:00:41-0300 HEAD=ca7f9ef dirty=30 checker=ff9fd2aa6811a813
```

HEAD and the checker hash are stable across both checks; the dirty count is untracked
sibling follow-up artifacts only (`git status --porcelain | grep -v '^??'` shows no file
of mine; the lone `M` is Q1's own debt file, written by that seat).

Adversarial controls on the delivered checker (scratch copies under `/tmp/jcov3/control*`,
delivered tree untouched):

```text
control1 map says paraphrase, excerpt file says verbatim : exit 1, 10 FAIL lines (mode mismatch)
control2 map and excerpt both declare paraphrase         : exit 0,
         "SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 10 entries (10/10 anchors); MODES 10/10"
control3 one row's span changed 12 -> 1                  : exit 1,
         "SOURCE-SUPPORT 5/10 ...", "FAIL P1: anchor hit outside declared line span 1 (hit lines: 12)"
```

## Findings & named debt

- **F1 — denominators confirmed, both clusters.** Raw source-attributed JSON facts:
  r87 22, r88-m3 10; both by two independent methods. r88-m3 is an exact bijection
  (10 raw facts = 10 rows, all referenced). No map row points at a non-existent field
  (52 pointer checks, 0 unresolved); no row's `source_id` cell disagrees with the JSON
  value it points at.
- **F2 — r87 has two different 22s; name the receipt's denominator.** The r87 raw census
  is 22 (7 `first_appearance` + 7 claims + 4 relations + 4 timeline), and the map's row
  count is also 22 — but the sets differ: rows carry pointers for 20 of the raw facts
  (14 rows, with the 6 claim rows co-mapping 6 `first_appearance` pointers); the other 2
  raw facts (`entities[2].first_appearance`, `entities[2].claims[0]`) appear only in the
  scope note at `claim-excerpt-map.md:56`, anchored to H4's line 5; and 8 of the 22 rows
  (H1–H8) are hymn-clause readings with no JSON pointer. The map itself discloses all of
  this (lines 3, 38, 56), so raw-fact coverage is 22/22 (20 row-level, 2 note-level) —
  but the printed `SOURCE-SUPPORT 22/22` counts rows, and a reader can take it as
  "22 source-attributed JSON facts verified". Debt: the receipt should print the row
  denominator and the JSON-fact denominator separately (e.g. `ROWS 22/22;
  JSON-FACTS 20/22 via rows + 2/22 via note`).
- **F3 — pointer precision debt (r88-m3).** 6 of 10 r88-m3 rows point at JSON nodes, not
  fields (`entities[N].claims[0]` ×4, `timeline[N]` ×2; T1/T2 do name `description` and
  `source_id` parenthetically, and both exist). All resolve, so no non-existent-field
  flag; but node pointers do not pin which field was mapped and would survive a field
  rename. The r87 map names leaf fields in all 14 JSON rows (42/42 leaf).
- **F4 — R9 enforcement is real, not vacuous.** Controls 1–3 show the checker's exit code
  is load-bearing: paraphrase smuggled against a verbatim declaration fails; paraphrase
  declared on both sides is demoted to `RETELLING-SUPPORT-ONLY` and removed from the
  source-support denominator; a wrong span fails with the hit lines printed.
- **F5 — external comparison is outside the receipt's denominator (r88-m3).** The two
  Spence comparisons are map bullets, not rows; no row points at `source-excerpt.md`, so
  `10/10` says nothing about them. `source-excerpt.md` also carries no inline
  `Delivery mode (R9)` line (all five r87 excerpts and `fictional-excerpts.md` do), so its
  R9 `verbatim` declaration is map-only and unverified by the script's inline check.
  Named debt, not a regression: the map labels the passage `verbatim` + the underlying
  K'iche text `external-only` at `claim-excerpt-map.md:11`.
- **F6 — no fabrication observed.** Every number in the r90 C2 receipt reproduced from
  the delivered tree, including exit codes; my own reimplementation agrees 32/32 rows.
- Out of scope for this seat: the 164-directory census and exit-code deltas (calibration
  judges), C3 depth decisions, and the L1 prose/SCORECARD wording.

## Handoff

- **Axis verdicts (this seat):** coverage (denominators/pointers) **improved** — the
  receipt now reproduces independently and every map pointer resolves; F2/F3/F5 are
  labeling/precision debts, none of which is a coverage loss. Calibration: freeze check
  **PASS** (hash match, no mismatch to report as blocking); otherwise not assessed here.
  Depth: not assessed here.
- **Files written (only these):** `.ufo/waves/round-90/followup/JCOV3.md`,
  `.ufo/waves/round-90/followup/JCOV3-denominators.json`. No tracked file touched; no
  commit or push.
- **Reproduction:** `/tmp/jcov3/denominators.py`, `/tmp/jcov3/independent_support.py`,
  `/tmp/jcov3/emit.py`, `/tmp/jcov3/control{,2,3}/` are scratch and may be deleted; the
  JSON artifact carries the same census data durably.
- **For the integrator:** if F2 is accepted, the one-line fix is in the print statement of
  `corpus/tools/support_check.py:276-281` (add a JSON-fact denominator or a row/fact label);
  F3/F5 are wording/pointer-precision items for r91, no exit-code impact.
- **Corroboration (independent, read after my own recount closed):** sibling coverage judges
  reached the same denominator finding on their own trees — `JCOV1.md:300` (JCOV1-N1: "the
  22/22 receipt counts rows, not JSON facts") and `JCOV2.md:252` (do not forward `22/22` as a
  22-JSON-fact receipt). Three independent recounts agree, so F2 is a corroborated
  non-blocking wording debt, not a lone reading; my seat adds the exact set arithmetic
  (20 raw facts via row pointers + 2 via the H4 note = 22 raw; 14 JSON rows + 8 hymn rows = 22 rows).
- **Side effects:** the module probe created `corpus/tools/__pycache__/`, which I removed;
  `find . -name __pycache__` is now empty and no tracked file of mine is modified.
