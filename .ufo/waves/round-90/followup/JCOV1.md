# JCOV1 — Coverage judge #1 (receipts)

Seat: JCOV1 (follow-up wave, world-bible lane). Delivered tree: `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13`
(baseline `e97613c`), `git status --porcelain --untracked-files=no` empty at start, mid-verification, and end.
Mission: reproduce the C2 support receipts, re-run M4's wrong-line attack against the delivered script,
determinism, and freeze-then-verify. All repository access was read-only; scratch lived on `/dev/shm`
(because `/tmp` had 0 free inodes at start — see Findings) and was removed after use.

## Work performed

- Two 60 s wait-checks with tree/artifact snapshots (protocol requirement), run as one background command; no dependency
  was declared in my block, so these double as stability checks that the delivered tree did not move under the judge.
- Ran the delivered support command on both clusters from the repository root and recorded exit codes and receipt lines.
- Ran the live R9 probe on the pre-existing `r89-inspiration-paraphrase` fixture.
- Determinism: two runs each, per cluster and as M4's combined shell command; stdout/stderr compared byte-wise and hashed.
- Re-ran M4's wrong-line attack, and M4's full 6-case harness plus the two M5 attack variants, against an exact
  `ca7f9ef` archive (`git archive ca7f9ef corpus/tools corpus/fixtures/r87-myth-cluster`), in `/dev/shm`;
  the archive's checker/map/excerpt hashes were confirmed equal to the delivered working-tree files before the attack.
- Three R9 sensitivity probes (excerpt-vs-map mode mismatch; map-vs-excerpt mismatch; nulled inline declaration).
- Exit-code contract probes (missing cluster, non-map file).
- Freeze-then-verify (r88-I1): composed `e97613c + X2 + X3 + M1 + M2 + M3 + M5` in a baseline extract and hash-compared
  every file those patches touch against the delivered tree.
- Coverage census: JSON fact counts per cluster vs mapped rows; explicit trace of which facts each row covers.

## Before → after measurements

### 1. Tree state and stability (two 60 s wait-checks)

```sh
printf 'wait1_start='; date --iso-8601=seconds; sleep 60; printf 'wait1_end='; date --iso-8601=seconds
printf 'head='; git -C "$REPO" rev-parse HEAD
printf 'tracked_status='; git -C "$REPO" status --porcelain --untracked-files=no; echo "(end)"
printf 'support_check_sha256='; sha256sum "$REPO/corpus/tools/support_check.py" | cut -d' ' -f1
sleep 60
# (same head/status/sha block again)
```

Observed:

```text
wait1_start=2026-10-17T06:57:26-03:00
wait1_end=2026-10-17T06:58:26-03:00
head=ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13
tracked_status=(end)
support_check_sha256=66a3c4bb2ae7fc2049227e480864661606b65a629c64cbc3ce05e14589add472
wait2_end=2026-10-17T06:59:26-03:00
head=ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13
tracked_status=(end)
support_check_sha256=66a3c4bb2ae7fc2049227e480864661606b65a629c64cbc3ce05e14589add472
```

### 2. Positive receipts (delivered tree, repo root)

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster; echo "r87_exit=$?"
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster; echo "r88m3_exit=$?"
```

Observed (per-row PASS lines omitted except the summaries; every one of the 22 + 10 rows printed `PASS`):

```text
SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
RESULT PASS
r87_exit=0
SOURCE-SUPPORT 10/10; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 10/10
RESULT PASS
r88m3_exit=0
```

Both expected receipts reproduce exactly as claimed by C2/W3/SE3/M5. The r87 run's 22 per-row lines each carry the
grep hit line number and text (e.g. `PASS E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.`).

### 3. Live R9 probe (pre-existing paraphrase fixture)

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r89-inspiration-paraphrase; echo "r89paraphrase_exit=$?"
```

Observed:

```text
PASS entities.json#/0/claims/0: retelling-support-only; anchor=found; mode=paraphrase; 9:A modern paraphrase says that the keeper later summarized the ledger for the court: the tide-mark had been moved to the west stair.
SOURCE-SUPPORT 0/0; RETELLING-SUPPORT-ONLY 1 entries (1/1 anchors); MODES 1/1
RESULT PASS
r89paraphrase_exit=0
```

A paraphrase row contributes 0 to source support even though its anchor matches — R9's "a paraphrase cannot count as
source-text support" holds on a live corpus fixture, not only in the synthetic attack.

### 4. Determinism

```sh
python3 - <<'PY'
import hashlib, subprocess
cmd = 'python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster && python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster'
outs = []
for _ in range(2):
    r = subprocess.run(cmd, shell=True, text=True, capture_output=True)
    outs.append((r.returncode, r.stdout, r.stderr))
a, b = outs
print(f'combined_command_exit run1={a[0]} run2={b[0]} stdout_byte_identical={a[1]==b[1]} stderr_byte_identical={a[2]==b[2]}')
print(f'combined_stdout_sha256={hashlib.sha256(a[1].encode()).hexdigest()}')
PY
```

Observed:

```text
combined_command_exit run1=0 run2=0 stdout_byte_identical=True stderr_byte_identical=True
combined_stdout_sha256=9b983f02a56eb77fde604ddd99ffc12356e67faaa43df5192a207f643ab6fef4
```

Per-cluster runs were also compared: r87 stdout `sha256=18d1ef6299f1ffcb7dd2ec1c849434db56e8cdd68118914b0dfaf08876f83a2a`,
r88-m3 stdout `sha256=db1493177719c575582db02206117bb2fa74e3009dfd0b4a00a1966245f2579e`; both byte-identical across runs;
stderr empty (`e3b0c442…b855` = SHA-256 of empty input). No nondeterminism (no dict-ordered or path-dependent output).

### 5. Wrong-line attack re-run (M4 case) + full adversarial harness — against delivered script

Archive integrity before the attack (`del` = `git archive ca7f9ef`):

```text
66a3c4bb2ae7fc2049227e480864661606b65a629c64cbc3ce05e14589add472  del/corpus/tools/support_check.py
8c1b600d28c130f998a0765ae9c4ae30d828b11fe96e3cbd763cd0cf79089b9d  del/.../claim-excerpt-map.md
c8011512451658e681ae7accdd12932d4bef70e2aa854ddf025e92e7a9236b84  del/.../gate-witness-excerpt.md
del_matches_delivered_checker=yes
```

Harness: M4's exact mutations (map row + excerpt declaration restored after every case), each run with
`python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster` at the archive root. Observed:

```text
paraphrase-consistent: exit=0 expected=0 PASS
   PASS E1: retelling-support-only; anchor=found; mode=paraphrase; 7:> I am Hara, keeper of the Mother-Tide Gate.
   SOURCE-SUPPORT 19/19; RETELLING-SUPPORT-ONLY 3 entries (3/3 anchors); MODES 22/22
summary-consistent: exit=0 expected=0 PASS
   PASS E1: retelling-support-only; anchor=found; mode=summary; 7:> I am Hara, keeper of the Mother-Tide Gate.
   SOURCE-SUPPORT 19/19; RETELLING-SUPPORT-ONLY 3 entries (3/3 anchors); MODES 22/22
undeclared-mode: exit=1 expected=1 PASS
   FAIL E1: source-support; mode=undeclared; excerpt-mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.
   SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 21/22
   FAIL: E1: delivery mode missing or mismatched
invalid-mode: exit=1 expected=1 PASS
   FAIL E1: source-support; mode=undeclared; excerpt-mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.
   SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 21/22
   FAIL: E1: delivery mode missing or mismatched
wrong-line-7-to-6: exit=1 expected=1 PASS
   FAIL E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.; span=6; outside-span=7
   SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
   FAIL: E1: anchor hit outside declared line span 6 (hit lines: 7)
missing-excerpt: exit=1 expected=1 PASS
   FAIL E1: source-support; mode=verbatim; excerpt-mode=undeclared; anchor=not-found
   SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 21/22
   FAIL: E1: delivery mode missing or mismatched
   FAIL: E1: source-support anchor missing
   FAIL: E1: excerpt path missing or outside cluster
missing-span: exit=1 expected=1 PASS
   FAIL E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.; span=undeclared
   SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
   FAIL: E1: missing or invalid declared line span
duplicate-hit-outside-span: exit=1 expected=1 PASS
   FAIL E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.; 12:> I am Hara, keeper of the Mother-Tide Gate.; span=7; outside-span=12
   SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
   FAIL: E1: anchor hit outside declared line span 7 (hit lines: 12)
all_cases_as_expected=True (8/8)
post_attack_map_restored=True post_attack_excerpt_restored=True
post_attack_map_sha256=8c1b600d28c130f998a0765ae9c4ae30d828b11fe96e3cbd763cd0cf79089b9d
```

**D-M4-1 is closed on the delivered tree.** At work-wave time M4 recorded `wrong-line: exit=0 … SOURCE-SUPPORT 22/22`
(a blocking finding); the delivered script fails the identical mutation with exit 1, `21/22`, and an explicit
`outside declared line span` message, and the duplicate-hit variant proves a second out-of-span hit cannot be masked
by an in-span one. Attack tree restored byte-identically; the repository itself was never mutated.

### 6. R9 sensitivity probes (delivered script, archive)

```text
excerpt-paraphrase-vs-map-verbatim: exit=1
   FAIL E1: source-support; mode=verbatim; excerpt-mode=paraphrase; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.
   SOURCE-SUPPORT 19/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 19/22
map-translation-vs-excerpt-verbatim: exit=1
   FAIL E1: source-support; mode=translation; excerpt-mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.
   SOURCE-SUPPORT 21/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 21/22
excerpt-inline-mode-line-neutered-same-linecount: exit=0
   PASS E1: source-support; mode=verbatim; anchor=found; 7:> I am Hara, keeper of the Mother-Tide Gate.
   SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22
   RESULT PASS
excerpt_restored=True map_untouched=True
```

Mismatches between the excerpt's own declaration and the map fail in both directions (exit 1). When the excerpt
carries no inline declaration at all, the map's declaration table alone is trusted and the row passes (exit 0):
mode truthfulness remains a self-declaration; the checker enforces consistency, anchor presence, and span only.
(My first attempt at this probe removed the declaration line and failed for the wrong reason — a one-line shift moved
the anchor to line 6 while the span stayed 7; the rerun preserved the line count, which isolates the mode question.)

### 7. Exit-code contract

```sh
python3 corpus/tools/support_check.py corpus/fixtures/no-such-cluster; echo "missing_cluster_exit=$?"
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster --map corpus/fixtures/r87-myth-cluster/README.md; echo "non_map_file_exit=$?"
```

Observed:

```text
FAIL: cluster directory not found: corpus/fixtures/no-such-cluster
missing_cluster_exit=2
FAIL: no Markdown table found with fact, excerpt path, delivery mode, and anchor columns
non_map_file_exit=2
```

Exit contract holds: 0 = all rows supported and modes consistent; 1 = support/mode/span failure; 2 = map/cluster/read
error. This matters for the receipt — only exit 0 with `RESULT PASS` should be read as support evidence.

### 8. Freeze-then-verify (r88-I1): composed patches vs delivered tree

```sh
git -C "$REPO" archive e97613c corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster corpus/fixtures/r88-m3-maya-cluster | tar -x -C "$up"
for p in X2-c1-nullonly X3-c1-tickonly M1-r87-map M2-r88m3-map M3-support-script M5-span-fix; do (cd "$up" && git apply "$W/$p.patch"); done
# then sha256sum "$up/<file>" vs sha256sum "$REPO/<file>" for every path named by those patches
```

Observed (all six patches applied cleanly; 11 files compared; 0 mismatches):

```text
applied=X2-c1-nullonly … applied=X3-c1-tickonly … applied=M1-r87-map … applied=M2-r88m3-map
applied=M3-support-script … applied=M5-span-fix
MATCH corpus/fixtures/check_bible.py ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
MATCH corpus/fixtures/r87-myth-cluster/claim-excerpt-map.md 8c1b600d28c130f998a0765ae9c4ae30d828b11fe96e3cbd763cd0cf79089b9d
MATCH corpus/fixtures/r87-myth-cluster/dune-register-excerpt.md 23754ebe792898c3b9399c8f55404149c1cf90b7cd436cf6a613a92945aa690a
MATCH corpus/fixtures/r87-myth-cluster/gate-witness-excerpt.md c8011512451658e681ae7accdd12932d4bef70e2aa854ddf025e92e7a9236b84
MATCH corpus/fixtures/r87-myth-cluster/lowwater-hymn-excerpt.md 0cb263e8d5fd79a617f16dc57f476f9dc4d526e4f9ba90f05be68d8f8cc5cc6c
MATCH corpus/fixtures/r87-myth-cluster/shell-charter-excerpt.md 7e06891ae849771bc52c064447fca04d3b2cfee22ffd07055ba5a217d5350b7f
MATCH corpus/fixtures/r87-myth-cluster/tide-bell-tally-excerpt.md ca589fd27e737832510a41d65d3b95e46121939af0a7447362fccd70583569a8
MATCH corpus/fixtures/r88-m3-maya-cluster/claim-excerpt-map.md d314d22ec2bbba149354ef30df96f39468f8f7a54e6c3a4cf824eb9d58dad290
MATCH corpus/fixtures/r88-m3-maya-cluster/fictional-excerpts.md e456bb1204b88792d4fe6396e9e8b0deb9ff6f47e1821b0e875738431b9bda89
MATCH corpus/tools/README.md 998aa427aaaece58dcfda3f0f45583ddee174fa5ca110256d5bc21a82e1c80f2
MATCH corpus/tools/support_check.py 66a3c4bb2ae7fc2049227e480864661606b65a629c64cbc3ce05e14589add472
freeze_mismatches=0
```

No blocking finding: the delivered C2 artifacts are exactly the composition of the work-wave patches on `e97613c`,
with no integrator amendment. The same composition check covers the C1 repair: `X2 + X3` on
`e97613c:corpus/fixtures/check_bible.py` hash-matches the delivered file (`ff9fd2aa…`). That is supporting evidence
only — I do not rule on C1 behaviour from it (not my lane).

### 9. Coverage census (JSON facts vs mapped rows)

```sh
python3 - <<'PY'  # enumerates JSON facts per cluster and reuses the delivered checker's parse_map for rows
...
PY
```

Observed:

```text
r87-myth-cluster: JSON facts claims=7 pointers=7 relations=4 timeline=4 total=22
r87-myth-cluster: map rows=22 ids=E1..E6,R1..R4,T1..T4,H1..H8
r88-m3-maya-cluster: JSON facts claims=4 pointers=4 relations=0 timeline=2 total=10
r88-m3-maya-cluster: map rows=10 ids=P1..P4,E1..E4,T1..T2
```

Per-entity trace (all 7 r87 entities have exactly one claim and one `first_appearance`; `entities[2]` is
`mother-tide-gate`, `first_appearance='lowwater-hymn'`, claim source `lowwater-hymn`):

- r87: rows E1–E6 each cover one claim **and** its co-mapped `first_appearance` pointer (12 JSON facts), R1–R4
  cover the 4 relations, T1–T4 the 4 timeline events → 20 JSON facts in 14 rows. The remaining 2 JSON facts
  (`entities[2].claims[0]` and `entities[2].first_appearance`, both `lowwater-hymn`) are co-mapped onto H4
  (hymn line 5) as the map's scope note declares; the other 7 hymn rows are interpretive readings, not JSON facts.
- r88-m3: 1:1 — P1–P4 pointers, E1–E4 claims, T1–T2 timeline = 10 rows, 10 facts.

So **all JSON facts are covered**, and the receipt denominator (22/22, 10/10) counts map rows, which for r87 is a
different set from the 22 JSON facts (see JCOV1-N1).

## Findings & named debt

- **C2 coverage verdict (my axis, delivered tree at `ca7f9ef`): improved, bounded.** One committed script
  (`corpus/tools/support_check.py`, sha256 `66a3c4bb…`) is the receipt: r87 `SOURCE-SUPPORT 22/22 … RESULT PASS` exit 0,
  r88-m3 `10/10 … RESULT PASS` exit 0; both reproduce byte-identically run-to-run; the live paraphrase fixture counts
  0/0 source support; M4's wrong-line mutation now fails exit 1 with an explicit out-of-span message; the freeze check
  has zero mismatches across all 11 touched files. No evidence of harm on any other axis was observed by this seat
  (the checker is read-only; it writes nothing and mutates nothing).
- **D-M4-1 — closed.** Pre-M5 receipt (`wrong-line: exit=0; SOURCE-SUPPORT 22/22`) no longer reproduces; the delivered
  script enforces the declared span, including the duplicate-hit case where an in-span hit could otherwise mask an
  out-of-span one.
- **D-M4-2 — adjudicated, not blocking.** The spec's C2 (ii) requires "one reproducible support command … a committed
  checker script whose exit code + N/N print IS the receipt". The delivered tree has exactly one committed script that
  prints both receipts and exits 0; the N/N receipts are per-cluster, with no aggregate `32/32`. Under the spec's
  wording this is satisfied — the "one command" is the script, and two invocations of it are two receipts. An optional
  r91 nicety would be an aggregate mode/flag; nothing in the claim text requires it.
- **JCOV1-R1 (new, bounded): mode truthfulness is self-declared.** If an excerpt carries no inline declaration, the
  map's excerpt-declaration table alone satisfies R9 and the row passes (proved: exit 0 after neutering only the inline
  line, line count preserved). Both delivered clusters currently declare modes inline *and* in the map, and mismatches
  in either direction fail (exit 1), so the live receipts are not weakened. Bound to record: this checker verifies
  consistency, anchor presence, and span — not that "verbatim" is true; `corpus/tools/README.md` already disclaims
  exactly this. No repair demanded; if r91 wants a stronger gate, it would need evidence-based mode justification,
  which is out of a lexical preflight's reach.
- **JCOV1-N1 (new, no harm): the 22/22 receipt counts rows, not JSON facts.** For r87 the two sets coincide
  numerically (22) but not compositionally: 14 JSON rows carrying 20 facts + 8 hymn rows, with 2 facts folded into
  H4 by prose. The map's scope note states this correctly and the count is honest — but a reader could misread
  `22/22` as 22/22 JSON facts. Suggested (non-blocking) wording: “rows” in the summary line or in the README.
- **Environment debt (not a tree defect): `/tmp` is inode-exhausted.** At 06:56 `df -i /tmp` reported
  `1048576 1048576 0 100%`, and even a 30-file scratch could not be created (`mktemp -d /tmp/… : No space left
  on device`). M4 already recorded this pressure; it has since worsened to the point that scratch is impossible for
  any seat. I placed my scratch on `/dev/shm` (a deviation from "scratch under /tmp", chosen over deleting another
  seat's scratch) and removed it afterwards; `/dev/shm` was restored to baseline (330 inodes used, 1%). By 07:00
  `/tmp` showed 2613 free inodes, so space was freed by someone mid-run. r91 planning should treat `/tmp` hygiene
  (or an approved alternate scratch root) as an active constraint.
- No blocking findings: every required receipt reproduced, the freeze hash-match holds, and I found no contradiction
  between the work-wave claims and the delivered tree.

## Handoff

- **Verdict recommendation for C2 coverage (JCOV1 receipts axis): improved, bounded** — accept, with the named
  residuals JCOV1-R1 (mode self-declaration; README-documented) and JCOV1-N1 (row-vs-fact denominator wording), and
  with D-M4-2 ruled satisfied as written.
- Evidence base for the parent: all commands and outputs above were produced against the delivered tree at `ca7f9ef`
  (working tree clean; checker hash stable across both wait-checks); the attack and freeze-composition work used
  throw-away extracts of `e97613c`/`ca7f9ef` that were byte-compared to the delivered files and then deleted.
- Not verified by this seat (out of lane): C1 behavioural correctness beyond the X2+X3 byte-composition match, the
  census delta (0 changed / 4 new of 164), C3 decision content, and doc-parity/SCORECARD wording. If the parent wants
  a second, differently-seeded receipt, the cheapest independent check is to re-run the two commands from
  `corpus/tools/README.md` on a fresh clone at `ca7f9ef`; the expected stdout hashes are recorded above
  (r87 `18d1ef62…`, r88-m3 `db149317…`, combined `9b983f02…`).
- My only repository write was this file: `lore-shokunin/.ufo/waves/round-90/followup/JCOV1.md`. No commit, no push,
  no sibling-repo access, no tracked-file modification (`git status --porcelain --untracked-files=no` empty at start
  and end).
