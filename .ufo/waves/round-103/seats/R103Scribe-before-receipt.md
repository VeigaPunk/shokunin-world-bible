# R103 scribe — lore BEFORE receipt

- Lane: `lore-shokunin` (worktree `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/lore-shokunin`)
- Branch: `kaika/round`
- Revision measured against: `6cec83aede47575beeeda6b7dc0e4ea74927be78` (`git rev-parse HEAD`, 2026-10-19T21:32:07Z)
- Measured: 2026-10-19T21:32:07Z, before any r103 seat output existed (`.ufo/waves/round-103/` was absent; this file creates `seats/`).
- Role: record only. No product file was edited, no commit/push, no judge.

## Measurement method and concurrency note

Sibling L2s can write new files concurrently, so every tracked-file quantity is measured
against the base commit, not an assumed-clean working tree:

- `git show 6cec83a:<path>` — file bytes at base (README, PROVINCE, SCORECARD, QUALITY, SOURCES).
- `git ls-tree <rev>` / `git ls-tree -r --name-only <rev>` — path inventory at base.
- `git grep ... 6cec83a -- <paths>` — citations at base.
- Working tree is used only for (a) `git status`, (b) `git diff --name-only 6cec83a -- ...`,
  (c) the gate battery, whose scripts/fixtures were confirmed unmodified vs base
  (`git status --porcelain=v1 -- corpus/fixtures corpus/tools | wc -l` → `0`), and
  (d) the two explicitly labelled "working-tree, literal" census commands.

Concurrency observed: `git status --porcelain=v1 -uall` printed **nothing** at start and end,
and `git diff --name-only 6cec83a -- corpus README.md PROVINCE.md SKILL.md SCORECARD.md LOG.md | wc -l`
was `0` at start and end. No sibling write was visible during the receipt window. This worktree has
no untracked `.scratch/` (the W1 dossier's `.scratch/` belonged to the main checkout).

Output convention: outputs are shown as captured, with stdout/stderr separated where both were
present. `[exit N]` is the exit of the command as written; where a command ends
`; echo exit=$?`, the embedded `exit=N` line is the measured command's own status and the
wrapper `[exit 0]` is the final `echo`.

A first K15 form, `git ls-tree -d --name-only 6cec83a -- corpus/fixtures`, returned `1` because the
pathspec selects the `corpus/fixtures` directory entry itself. The corrected subdir forms returned
`174`, corroborated by the dossier's working-tree `find` form.

## Identity and cleanliness (base 6cec83a)

```text
$ git rev-parse HEAD
6cec83aede47575beeeda6b7dc0e4ea74927be78
[exit 0]

$ git rev-parse --abbrev-ref HEAD
kaika/round
[exit 0]

$ git status --porcelain=v1 -uall
(no output)
[exit 0]

$ git diff --name-only 6cec83a -- corpus README.md PROVINCE.md SKILL.md SCORECARD.md LOG.md | wc -l
0
[exit 0]
```

`git status --porcelain=v1 -uall` was re-run after the gate battery: still no output; the durable-surface
diff count was still `0`.

## K10 — knowledge count

```text
$ git ls-tree -r --name-only 6cec83a -- corpus/knowledge | wc -l
25
[exit 0]

$ git ls-tree -r --name-only 6cec83a -- corpus/knowledge | grep -c '\.md$'
24
[exit 0]
```

## K11 — entries opening with all three fields in lines 1–3

```text
$ git ls-tree -r --name-only 6cec83a -- corpus/knowledge | grep '\.md$' | while read -r f; do git show "6cec83a:$f" | head -n 3 | grep -cE '^(source|verified-at|recheck):'; done | grep -c '^3$'
10
[exit 0]
```

## K12 — entries missing each field (anchored at line start)

```text
$ git ls-tree -r --name-only 6cec83a -- corpus/knowledge | grep '\.md$' | while read -r f; do git show "6cec83a:$f" | grep -qE '^source:' || echo "$f"; done | wc -l
12
[exit 0]

$ git ls-tree -r --name-only 6cec83a -- corpus/knowledge | grep '\.md$' | while read -r f; do git show "6cec83a:$f" | grep -qE '^verified-at:' || echo "$f"; done | wc -l
12
[exit 0]

$ git ls-tree -r --name-only 6cec83a -- corpus/knowledge | grep '\.md$' | while read -r f; do git show "6cec83a:$f" | grep -qE '^recheck:' || echo "$f"; done | wc -l
13
[exit 0]
```

## K14 — lessons / QUALITY / SOURCES absence

At base:

```text
$ git ls-tree -r --name-only 6cec83a -- corpus/lessons | wc -l
0
[exit 0]

$ git ls-tree 6cec83a -- corpus/QUALITY.md | wc -l
0
[exit 0]

$ git ls-tree 6cec83a -- corpus/SOURCES.md | wc -l
0
[exit 0]
```

Working-tree check (literal absence form; not commit-scoped):

```text
$ ls corpus/lessons 2>/dev/null | wc -l; test -f corpus/QUALITY.md; echo QUALITY_test_exit=$?; test -f corpus/SOURCES.md; echo SOURCES_test_exit=$?
0
QUALITY_test_exit=1
SOURCES_test_exit=1
[exit 0]
```

## K15 — fixture census

```text
$ git ls-tree -d --name-only 6cec83a:corpus/fixtures | wc -l
174
[exit 0]

$ git ls-tree 6cec83a:corpus/fixtures | grep -c '^040000'
174
[exit 0]

$ echo $(( $(find corpus/fixtures -maxdepth 1 -type d | wc -l) - 1 ))
174
[exit 0]
```

## K16 — dead seat-scratch pointers cited by durable surfaces

Commit-scoped existence check:

```text
$ git grep -ohE '\.ufo/waves/round-[0-9]+/seats/[A-Za-z0-9_./-]+' 6cec83a -- corpus/knowledge corpus/tools/README.md corpus/README.md corpus/fixtures/README.md SKILL.md | sed -E 's/[.,;:)]+$//' | sort -u | while read -r p; do git cat-file -e "6cec83a:$p" 2>/dev/null || echo "$p"; done | wc -l
24
[exit 0]
```

Working-tree form (dossier K16):

```text
$ git grep -ohE '\.ufo/waves/round-[0-9]+/seats/[A-Za-z0-9_./-]+' -- corpus/knowledge corpus/tools/README.md corpus/README.md corpus/fixtures/README.md SKILL.md | sed -E 's/[.,;:)]+$//' | sort -u | while read -r p; do [ -e "$p" ] || echo "$p"; done | wc -l
24
[exit 0]
```

## K17 — coverage map / gaps / frontier / PROVINCE sections

```text
$ git show 6cec83a:corpus/README.md | grep -ciE 'coverage map'
0
[exit 1]

$ git show 6cec83a:corpus/README.md | grep -ciE 'frontier'
0
[exit 1]

$ git show 6cec83a:corpus/README.md | grep -ciE 'gaps'
0
[exit 1]

$ git show 6cec83a:PROVINCE.md | grep -cE '^(#+ )?(Core|Frontier|Adjacent)'
0
[exit 1]
```

## K08 — SCORECARD capabilities rows

```text
$ git show 6cec83a:SCORECARD.md | awk '/^## Capabilities/{f=1;next} /^## /{f=0} f && /^\| [a-z]/' | wc -l
4
[exit 0]
```

## C1 counting commands (coverage; before)

Base-scoped:

```text
$ git show 6cec83a:corpus/README.md | grep -cE '^\| CM-[a-z0-9]+ '
0
[exit 1]

$ git show 6cec83a:corpus/README.md | grep -c '^## Frontier'
0
[exit 1]

$ git ls-tree -r --name-only 6cec83a -- corpus/knowledge | grep '\.md$' | while read -r f; do git show "6cec83a:$f" | grep -qE '^coverage-row: CM-' && echo "$f"; done | wc -l
0
[exit 0]
```

Literal working-tree forms from the round context (worktree tracked content equal to base):

```text
$ grep -cE '^\| CM-[a-z0-9]+ ' corpus/README.md; echo cm_rows_exit=$?
0
cm_rows_exit=1
[exit 0]

$ grep -c '^## Frontier' corpus/README.md; echo frontier_exit=$?
0
frontier_exit=1
[exit 0]

$ grep -lE '^coverage-row: CM-' corpus/knowledge/*.md | wc -l; echo coverage_row_exit=$?
0
coverage_row_exit=0
[exit 0]
```

## C2 counting commands (QUALITY; before)

```text
$ grep -cE '^\| Q[0-9]{2} ' corpus/QUALITY.md; echo exit=$?
stdout: exit=2
stderr: grep: corpus/QUALITY.md: No such file or directory
[exit 0]
```

Base-scoped equivalent over the absent file prints `0`:

```text
$ git show 6cec83a:corpus/QUALITY.md 2>/dev/null | grep -cE '^\| Q[0-9]{2} '
0
[exit 1]
```

## C3 counting commands (SOURCES; before)

Registry row count:

```text
$ grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md; echo exit=$?
stdout: exit=2
stderr: grep: corpus/SOURCES.md: No such file or directory
[exit 0]

$ git show 6cec83a:corpus/SOURCES.md 2>/dev/null | grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
0
[exit 1]
```

Contract-v1 census, run literally against the working tree (file absent, so every awk fails at open):

```text
$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md; echo exit=$?
stdout: exit=2
stderr: awk: fatal: cannot open file `corpus/SOURCES.md' for reading: No such file or directory
[exit 0]

$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {t=$5; gsub(/[[:space:]]/,"",t); n[t]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md; echo exit=$?
stdout: exit=2
stderr: awk: fatal: cannot open file `corpus/SOURCES.md' for reading: No such file or directory
[exit 0]

$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {s=$9; gsub(/[[:space:]]/,"",s); n[s]++} END{for(k in n) printf "%s=%d ", k, n[k]; print ""}' corpus/SOURCES.md; echo exit=$?
stdout: exit=2
stderr: awk: fatal: cannot open file `corpus/SOURCES.md' for reading: No such file or directory
[exit 0]

$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ {i=$2; gsub(/[[:space:]]/,"",i); print i}' corpus/SOURCES.md | sort | uniq -d; echo exit=$?
stdout: exit=0
stderr: awk: fatal: cannot open file `corpus/SOURCES.md' for reading: No such file or directory
[exit 0]

$ awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF==13 {i=$2;k=$4;t=$5;s=$9; gsub(/[[:space:]]/,"",i); gsub(/[[:space:]]/,"",k); gsub(/[[:space:]]/,"",t); gsub(/[[:space:]]/,"",s); if (t !~ /^[ABC]$/) print "tier", i, t; if (s !~ /^(queued|mined|rejected)$/) print "status", i, s; if (k !~ /^(spec|docs|paper|code|tool|dataset|talk|book|community|own-work)$/) print "kind", i, k; if (t=="A" && k=="community") print "tier-inflation", i}' corpus/SOURCES.md; echo exit=$?
stdout: exit=2
stderr: awk: fatal: cannot open file `corpus/SOURCES.md' for reading: No such file or directory
[exit 0]
```

The duplicate-id pipeline's wrapper exit is `0` because `uniq -d` succeeded on empty awk stdout; the
underlying awk still failed at file open (`exit=2` in stdout). No census can pass or fail on row content
while the file is absent.

## K31 — gate battery (working tree, verify modes only)

`corpus/fixtures` and `corpus/tools` were clean against base before this battery
(`git status --porcelain=v1 -- corpus/fixtures corpus/tools | wc -l` → `0`). No `--freeze`, no
`--self-test`, no writes into the tree.

```text
$ python3 -B corpus/fixtures/check_bible.py corpus/fixtures/r100-docket-review; echo exit=$?
CLEAN: schema, citations, relations, timeline; 0 violations
exit=0
[exit 0]

$ python3 -B corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster; echo exit=$?
INVENTORY JSON-FACTS 14/14; EDITORIAL-ROWS 8/8; TOTAL-ROWS 22/22; DISTINCT-ANCHORS 22/22
ANCHORS repeated-references=0; DUPLICATE-ROWS 0
PASS E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.
PASS E2: source-support; mode=verbatim; anchor=found; 7:> I, Sen, serve as recorder at Ash-Dune Sanctuary.
PASS E3: source-support; mode=verbatim; anchor=found; 8:> Place of keeping: Ash-Dune Sanctuary is a record-keeping place.
PASS E4: source-support; mode=verbatim; anchor=found; 9:> Shellweavers signed this charter as a signatory faction.
PASS E5: source-support; mode=verbatim; anchor=found; 10:> Reedwardens signed this charter as a signatory faction.
PASS E6: source-support; mode=verbatim; anchor=found; 11:| 1 | We carried the Reed Bell for the low-water signal. |
PASS R1: source-support; mode=verbatim; anchor=found; 11:> By this charter, Shellweavers stand allied with Reedwardens.
PASS R2: source-support; mode=verbatim; anchor=found; 12:> By this charter, Reedwardens stand allied with Shellweavers.
PASS R3: source-support; mode=verbatim; anchor=found; 13:> Watch clause: Under this charter's pledge, Shellweavers keep watch with the Reed Bell.
PASS R4: source-support; mode=verbatim; anchor=found; 9:> At Ash-Dune Sanctuary, Sen kept the register.
PASS T1: source-support; mode=verbatim; anchor=found; 8:> I sounded the Reed Bell at the Mother-Tide Gate before the Moon-Basin Vow, at the first low-water bell.
PASS T2: source-support; mode=verbatim; anchor=found; 12:| 2 | At Ash-Dune Sanctuary, Sen's tally records the return of the first low-water signal before the Moon-Basin Vow. |
PASS T3: source-support; mode=verbatim; anchor=found; 9:> I record the single Moon-Basin Vow of Saltmonth 4 at the Mother-Tide Gate during the first low-water bell.
PASS T4: source-support; mode=verbatim; anchor=found; 10:> I record that same single Moon-Basin Vow of Saltmonth 4 at Ash-Dune Sanctuary during the first low-water bell.
PASS H1: editorial-row; mode=verbatim; anchor=found; 5:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS H2: editorial-row; mode=verbatim; anchor=found; 5:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS H3: editorial-row; mode=verbatim; anchor=found; 5:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS H4: editorial-row; mode=verbatim; anchor=found; 5:> At low water we set the shell ring beside the bowl at the Mother-Tide Gate.
PASS H5: editorial-row; mode=verbatim; anchor=found; 6:> The bowl keeps no name, and no voice owns the tide.
PASS H6: editorial-row; mode=verbatim; anchor=found; 6:> The bowl keeps no name, and no voice owns the tide.
PASS H7: editorial-row; mode=verbatim; anchor=found; 7:> We pass the reed-bell hand to hand and let the water return it.
PASS H8: editorial-row; mode=verbatim; anchor=found; 7:> We pass the reed-bell hand to hand and let the water return it.
RECEIPT JSON-FACTS 14; EDITORIAL-ROWS 8; TOTAL-ROWS 22
SOURCE-SUPPORT 14/14; EDITORIAL-ANCHORS 8/8; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22; VALIDATED-ROWS 22/22
RESULT PASS
exit=0
[exit 0]

$ python3 -B corpus/tools/map_obligations.py corpus/fixtures/r100-docket-review; echo exit=$?
OBLIGATIONS raw=22 mapped=22
INVENTORY JSON-FACTS 22/22; EDITORIAL-ROWS 2/2; TOTAL-ROWS 24/24
RESULT PASS
exit=0
[exit 0]

$ for f in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response r97-crossing-acknowledgment r98-clerk-filing r99-window-lapse r100-docket-review; do out=$(python3 -B corpus/tools/dependency_freeze.py corpus/fixtures/$f); code=$?; printf '%s | %s | exit=%s\n' "$f" "$(printf '%s\n' "$out" | grep '^RESULT')" "$code"; done
r88-m3-maya-cluster | RESULT PASS | exit=0
r94-paired-crossing | RESULT PASS | exit=0
r95-crossing-aftermath | RESULT PASS | exit=0
r96-crossing-response | RESULT PASS | exit=0
r97-crossing-acknowledgment | RESULT PASS | exit=0
r98-clerk-filing | RESULT PASS | exit=0
r99-window-lapse | RESULT PASS | exit=0
r100-docket-review | RESULT PASS | exit=0
[exit 0]

$ out=$(python3 -B corpus/tools/discriminate_check.py); code=$?; printf '%s\n' "$out"; echo exit=$code
mode=delivered checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421 matches_pin=True
r91-c1-null-chain: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
r91-c1-tick-unresolved: run_exit=1 stderr_empty=True README_exact=True baseline_README_exact=True changed_line_pairs=1/1 (old<->new)
  pinned_semantic_gate=PASS
RESULT: DISCRIMINATION HELD — silent-revert check would fail on regression
exit=0
[exit 0]

$ out=$(python3 -B corpus/tools/boundary_doc_check.py); code=$?; printf '%s\n' "$out"; echo exit=$code
CHECK pinned inputs: PASS
CHECK receipt replay: PASS
CHECK explicit anchor ranges: PASS
CHECK document structure: PASS
scope=frozen-document drift + receipts + explicit-anchor range + structure; not semantic or AST validation
replay_receipts=3/3
replay_cases=14/14
anchors=2/2
h1_count=1
duplicate_headings=0
instruction_markers=0
CERTIFIED (bounded: frozen-document drift + receipts + explicit-anchor range + structure; no semantic/AST validation)
exit=0
[exit 0]
```

## Findings (observed, not inferred)

1. **Base census matches the W1 STATE dossier.** knowledge `25` files (`24` `.md` + `r102-debt-ledger.json`);
   triplet headers `10/24`; missing `source:` `12`, `verified-at:` `12`, `recheck:` `13`;
   fixtures `174`; dead seat-scratch pointers `24`; README `coverage map`/`frontier`/`gaps` mentions `0/0/0`;
   PROVINCE Core/Frontier/Adjacent sections `0`; SCORECARD capabilities rows `4`.
2. **C1 before:** coverage-map CM rows `0`; `## Frontier` headings `0`; knowledge entries carrying
   `coverage-row: CM-` `0`.
3. **C2 before:** `corpus/QUALITY.md` absent at base (`git ls-tree` row count `0`); literal Q-row grep exits `2`
   (`No such file or directory`), base-scoped Q-row count `0`.
4. **C3 before:** `corpus/SOURCES.md` absent at base (`git ls-tree` row count `0`); literal row census exits `2`
   (`No such file or directory`); every contract-v1 awk census fails at file open, so no tier/status/duplicate/
   enum result exists to report.
5. **Gate battery is green at base:** `check_bible` CLEAN 0 (exit `0`); `support_check` 22/22 PASS (exit `0`);
   `map_obligations` raw=22 mapped=22 PASS (exit `0`); `dependency_freeze` 8/8 `RESULT PASS` (each exit `0`);
   `discriminate_check` DISCRIMINATION HELD (exit `0`); `boundary_doc_check` CERTIFIED (exit `0`).
6. **No contamination observed:** start and end `git status --porcelain=v1 -uall` were both empty; tracked diff
   vs base on the durable surfaces was `0`; fixtures/tools were clean; `.ufo/waves/round-103/` did not exist
   before this receipt.
7. **Known limit:** the working-tree checks are snapshots at 2026-10-19T21:32Z. A sibling writing after that
   timestamp can change `git status`/working-tree greps, but cannot change any base-scoped figure above.

## Out of scope / not done

- No product code, contract, README, PROVINCE, QUALITY, SOURCES, lesson, or knowledge entry was edited.
- No `git commit`, `git push`, freeze, self-test, or judge invocation.
- No main-checkout, sibling-lane, or fleet file was written.
- No claim is made about content that was not measured; absent files are reported as absent, not as failing checks.
