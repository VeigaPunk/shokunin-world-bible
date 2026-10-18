# JDEP3 — Depth judge #3 (register + referents), round 90

Seat JDEP3, round-90 follow-up (world-bible lane), repo `/home/vgpnk/Projects/shokunin/lore-shokunin`.
Judged on the DELIVERED tree at `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13` (`ca7f9ef`), baseline `e97613c`.
Scratch: `/dev/shm/jdep3r90/` — `/tmp` on this host is inode-exhausted (`df -i /tmp` → `100%` IUse);
no `/tmp` file was created by this seat. Receipts: `.ufo/waves/round-90/followup/JDEP3-probes.json`.
Tree at measure: `git status --porcelain --untracked-files=no | wc -l` → `0` at both wait-checks;
two timestamped 60 s wait-checks ran (`06:55:07`→`06:56:07`, `06:56:18`→`06:57:18` local), HEAD stayed
`ca7f9ef` and no tracked modification appeared, so no evidence gap was left by the wait window.

**Seat mission.** On `ca7f9ef`: (1) re-run the cross-cluster shared-referent comparison (must stay empty);
(2) verify r90's new fixtures/maps created no false shared referent; (3) confirm
`corpus/knowledge/cross-cluster-contradictions.md` remains absent; (4) verify no incoming README carries a
false `## R10 comparison outcomes` section. Plus the wave-wide freeze-then-verify (r88-I1) hash check.

**Scoped depth verdicts (register + referents).**

| sub-axis | verdict | basis |
|---|---|---|
| R10 appendix + register no-false-entry boundary (decided matching-name sub-case) | **improved** | the appendix lands as an additive +37 lines / 0 deletions in the decision table (R10 row text byte-untouched, demo byte-identical); it names names/IDs as comparison *triggers*, routes dismissed overlaps to the incoming README `## R10 comparison outcomes` and candidates to `l0-questions.md`, and reserves the live register for a demonstrated shared referent+field+occasion; the live register stays absent and no false entry exists |
| Cross-cluster referent state (R10 trigger) | **unchanged — correctly empty** | zero intersection at entity/source/timeline ids, place ids, relation tuples, map anchor strings, and whole-word text sweeps; identical state to baseline (register file absent at both `e97613c` and `ca7f9ef`) |
| Referent hygiene of r90's new artifacts (4 C1 fixtures, 2 cluster maps) | **unchanged — no harm** | corpus-wide sweep (164 dirs): 0 shared ids involving either cluster or any r90 fixture; new fixtures contain no cluster nouns; the maps' anchor strings intersect empty and neither cluster path is referenced in the other's directory |
| Register operability (first real cross-cluster entry) | **unprovable-but-better** | no genuine cross-cluster conflict exists (no referent overlap), so the register has no trigger to exercise; the r90 appendix now defines the dismissed/candidate audit-trail destinations outside the live register, keeping the no-false-entry boundary specified |

No axis is harmed: the only corpus knowledge change is the additive appendix (0 deleted lines), the r89
demo is byte-identical to baseline (sha `7f56bdd6…0cb580`), and both clusters still replay `CLEAN` exit `0`
with the r90 checker. Freeze-then-verify passed (check 8) — delivered `check_bible.py` is byte-identical
to X2+X3 composed on `e97613c`; **no blocking finding**.

## Work performed

- Read the delivered R10 row + the three new decider appendices (`r88-sourced-inspiration-decision-table.md`
  lines 28–60), both new claim→excerpt maps in full, the four new C1 fixture READMEs, and `corpus/tools/README.md`.
- Re-ran the R10 comparison at all three levels the row names plus the two extra levels this seat used at r89
  (place ids, relation tuples) and two text levels (whole-word proper nouns both directions; capitalized-token
  intersection), now including the new map files, on the delivered tree.
- Ran the corpus-wide ID-collision sweep over all 164 fixture directories, explicitly testing r90-fixture and
  cluster involvement; re-checked the cluster-signature artifact set (`inspiration-note.md` + `symbolism-clause-map.md`).
- Ran the R10 cross-check specific to the new artifacts: cluster-noun scan inside all four r90 fixtures, anchor-string
  intersection between the two maps, and cross-cluster path references inside each cluster directory.
- Verified register absence at both commits (`git cat-file -e` on baseline and HEAD), the complete set of files
  referencing the register destination, and the README inventory/heading sweep (34 corpus READMEs; case-insensitive
  phrase sweep within `corpus/`).
- Ran freeze-then-verify: extracted baseline `check_bible.py`, applied `X2-c1-nullonly.patch` then
  `X3-c1-tickonly.patch` (`patch -p3`, both clean, X3 hunk offset +2), compared sha256 and byte-diff to delivered.
- Replayed both clusters and ran the delivered `corpus/tools/support_check.py` on both clusters.
- No tracked file was written; the only repository writes are this report and `JDEP3-probes.json`. No commit, no push.

## Before → after measurements

All commands from the repository root. `BEFORE` evidence = baseline `e97613c` (register-absence check and
r89 receipts); `AFTER` = delivered tree at `ca7f9ef`.

**1. R10's three named levels + two extra levels — structured sets (AFTER).**

```sh
python3 - <<'EOF'
import json,pathlib
A=pathlib.Path('corpus/fixtures/r87-myth-cluster'); B=pathlib.Path('corpus/fixtures/r88-m3-maya-cluster')
for kind,key in [('entities','id'),('sources','id'),('timeline','id')]:
    a={r[key] for r in json.load(open(A/(kind+'.json')))}
    b={r[key] for r in json.load(open(B/(kind+'.json')))}
    print(kind,'INTERSECTION',sorted(a&b))
for kind,fld in [('entities','kind'),('timeline','place_id')]:
    a={r[fld] for r in json.load(open(A/(kind+'.json'))) if r.get(fld)}
    b={r[fld] for r in json.load(open(B/(kind+'.json'))) if r.get(fld)}
    print(kind+'.'+fld,'INTERSECTION',sorted(a&b))
ra={(r['from'],r['to'],r['type']) for r in json.load(open(A/'relations.json'))}
rb={(r['from'],r['to'],r['type']) for r in json.load(open(B/'relations.json'))}
print('relations INTERSECTION', sorted(ra&rb))
EOF
```

Observed:

```
entities INTERSECTION []
sources INTERSECTION []
timeline INTERSECTION []
entities.kind INTERSECTION ['character', 'place']
timeline.place_id INTERSECTION []
relations INTERSECTION []
```

`entities.kind` is schema vocabulary (`character`, `place`), not a referent — the same category overlap r89
recorded. Relation sets: r87 4 tuples (`allied_with` ×2, `records_at`, `keeps_watch_with`), r88-m3 `[]`.

**2. Whole-word cross-cluster noun greps (AFTER).**

```sh
grep -rniE '\b(hara|sen|mother-tide-gate|ash-dune|shellweavers|reedwardens|reed-bell|dune-register|gate-witness|lowwater-hymn|shell-charter|tide-bell-tally)\b' corpus/fixtures/r88-m3-maya-cluster/   # rc=1
grep -rniE '\b(aru|evin|quiet-rise|salt-court|paired-clock|veil-verse|chalk-stair)\b' corpus/fixtures/r87-myth-cluster/                        # rc=1
```

Observed: `rc=1` both directions (no matches). This now covers the r90-added `claim-excerpt-map.md` in each
cluster, so the new maps introduced no cross-cluster mention.

**3. Capitalized-token intersection, both cluster directories incl. new maps (AFTER).**

```sh
python3 - <<'EOF'   # \b[A-Z][a-z]+… over every file in both cluster dirs
EOF
```

Observed: A 14 files, B 11 files; intersection = `['Anchors','Attribution','Bell','Consult','Delivery','Each',
'Editorial','Exact','Excerpt','It','Limit','Newly','Parallel','Public','Replay','Rights','Round','Scope','Source',
'Sourced','Status','Symbolism','The','These','This','We']` — governance/table vocabulary only (the `Bell` near-miss
is the r89-documented field-vocabulary overlap: r87 `reed-bell`/`tide-bell-tally` vs r88-m3 `paired-clock`
"Ninth Bell Paired Clock Register"; ticks still r87 `[1,2,3]` vs r88-m3 `[9]`, and R10's referent test filters it).
No proper noun of either cluster occurs in the other.

**4. Corpus-wide ID-collision sweep incl. r90 fixtures (AFTER).**

```sh
python3 - <<'EOF'   # id -> dirs over entities/sources/timeline for every dir under corpus/fixtures
EOF
```

Observed: `dirs scanned 164`; `unique ids 146`; `shared ids 55`;
`shared ids involving a cluster dir: {}`; `r90 dirs: ['r90-c1-rawpresent-from','r90-c1-rawpresent-source','r90-c1-rawpresent-to','r90-c1-three-causes']`;
`shared ids involving an r90 dir: {}`. The 55 shared ids are the known scaffolding vocabulary; none involves a
cluster or any r90 fixture. Cluster-signature dirs (both `inspiration-note.md` and `symbolism-clause-map.md`)
remain exactly `r87-myth-cluster` and `r88-m3-maya-cluster` — the four r90 fixtures did not enter cluster scope.

**5. New-artifact referent hygiene (AFTER).**

```sh
grep -rniE '\b(hara|sen|mother-tide-gate|ash-dune|shellweavers|reedwardens|reed-bell|aru|evin|quiet-rise|salt-court|paired-clock|veil-verse)\b' corpus/fixtures/r90-c1-*    # rc=1
grep -rn 'r88-m3\|r88/m3' corpus/fixtures/r87-myth-cluster/     # rcA=1
grep -rn 'r87-myth\|r87/' corpus/fixtures/r88-m3-maya-cluster/  # rcB=1
python3 - <<'EOF'   # backticked anchor strings of the two maps, anchor-like subset, intersect
EOF
```

Observed: no cluster nouns inside any r90 fixture (`rc=1`); no cross-cluster path reference inside either
cluster dir (`rcA=1`, `rcB=1`); map anchor-string intersection `[]` (r87 23 anchor-like strings incl. the
`external-only / unverified inspiration` marker, r88-m3 8 strings incl. Spence/K'iche prose anchors — the two
clusters' external references are different works, and each is marked external-only, so no referent exists at
that level either). New fixture ids (`…-seal`, `…-mira`, `…-ghost`, `…-ghostsrc`, `…-source`, `…-absent-holder`,
`…-absent-source`) are all fixture-local and prefixed.

**6. Register absence — BEFORE and AFTER, and what references it.**

```sh
git cat-file -e e97613c:corpus/knowledge/cross-cluster-contradictions.md   # fatal: does not exist → ABSENT-AT-BASELINE
git cat-file -e ca7f9ef:corpus/knowledge/cross-cluster-contradictions.md   # fatal: does not exist → ABSENT-AT-DELIVERED
find . -name 'cross-cluster-contradictions.md' -not -path './.git/*' | wc -l   # 0
grep -rln 'cross-cluster-contradictions' . --exclude-dir=.git   # corpus: decision table, r89 demo; rest are wave artifacts
```

Observed: the register file is absent at both commits and nowhere on disk (count `0`). The only tracked
`corpus/` references are the R10 row + appendix (decision table) and the r89 worked example; the demo is
byte-identical to baseline (unchanged in `git diff e97613c..ca7f9ef`), and everything else is `.ufo` wave
artifact text. No live register entry exists and none was created.

**7. README sweep — no false `## R10 comparison outcomes` section (AFTER).**

```sh
find corpus -name README.md | wc -l                                   # 34
grep -rn 'R10 comparison outcomes' --include=README.md .              # rc=1
grep -rni 'comparison outcomes' corpus/                               # 1 hit: decision table line 54, inline backticked destination
git diff --stat e97613c..ca7f9ef -- '*README.md'                      # 5 added files, 100 insertions (4 C1 fixture READMEs + corpus/tools/README.md)
```

Observed: no README anywhere carries the heading; the phrase occurs in `corpus/` exactly once, as the
inline `` `## R10 comparison outcomes` `` destination inside the new R10 appendix (line 54), and the five
READMEs r90 added do not mention R10 at all (`grep -rln 'R10' corpus --include=README.md` → rc=1). The four
new fixture READMEs describe only their own checker before/after outputs; `corpus/tools/README.md` describes
only the support command. So requirement (4) is satisfied: no incoming README carries a false comparison-outcome
section, and none carries a true one either (correct — no incoming cluster landed this round).

**8. Freeze-then-verify — delivered checker hash-matches X2+X3 composed on baseline.**

```sh
git show e97613c:corpus/fixtures/check_bible.py > /dev/shm/jdep3r90/freeze/check_bible.py
cd /dev/shm/jdep3r90/freeze && sha256sum check_bible.py
patch -p3 < …/X2-c1-nullonly.patch && patch -p3 < …/X3-c1-tickonly.patch
sha256sum check_bible.py
sha256sum /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py
diff check_bible.py …/check_bible.py   # IDENTICAL
```

Observed: baseline sha256 `e2bb9639a3247284e272200861a642829a39c97f01c60b80e507eb94f50e3556`; composed sha256
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`; delivered sha256
`ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` → byte-identical. X2 applied clean;
X3 applied clean with `Hunk #1 succeeded at 321 (offset 2 lines)` (X2 shifts it by 2). **No mismatch — no
blocking finding.** This is a supporting cross-check for the C1 lane; C1's tuple census is judged by its own seats.

**9. Cluster replays (AFTER).**

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/r87-myth-cluster       # CLEAN: … 0 violations; exit=0
python3 corpus/fixtures/check_bible.py corpus/fixtures/r88-m3-maya-cluster   # CLEAN: … 0 violations; exit=0
```

**10. Delivered support command — independent map check (AFTER).**

```sh
python3 corpus/tools/support_check.py corpus/fixtures/r87-myth-cluster
python3 corpus/tools/support_check.py corpus/fixtures/r88-m3-maya-cluster
```

Observed: r87 `SOURCE-SUPPORT 22/22; RETELLING-SUPPORT-ONLY 0 entries (0/0 anchors); MODES 22/22` →
`RESULT PASS`, exit `0`; r88-m3 `SOURCE-SUPPORT 10/10; … MODES 10/10` → `RESULT PASS`, exit `0` — matching the
wave's declared C2 receipt. From this seat the relevant fact is that both maps are entirely in-cluster: every
anchor resolves within its own cluster's excerpts; nothing cross-cluster is validated or claimed.

**11. Decision-table delta and appendix neutrality.**

```sh
git diff e97613c..ca7f9ef -- corpus/knowledge/r88-sourced-inspiration-decision-table.md
… | grep -c '^-[^-]'        # 0 deletions
sed -n '28,60p' … | grep -niwE 'ema|reed-arch|moon-basin|hypothetical'   # rc=1
```

Observed: +37 lines, 0 deletions; the R10 row body is unchanged context. The delivered appendices carry **no**
example names at all (D1's `moon-basin`/D2's `Ema` hypotheticals were not carried into the knowledge file;
whole-word grep rc=1), so the r90 governance text inserted no token that could later be misread as a shared
referent. The R10 appendix states the register's first real entry "awaits a genuine conflict" — consistent with
the measured empty state.

## Findings & named debt

**F1 (primary). R10 comparison stays empty on the delivered tree — a clean negative, not an oversight.**
Zero intersection at entity ids, source ids, timeline ids, place ids, relation tuples, whole-word text, and
map anchor strings between `r87-myth-cluster` and `r88-m3-maya-cluster`. The register file is absent at both
`e97613c` and `ca7f9ef`. The r90 appendices assert no cross-cluster outcome; the R10 appendix correctly keeps
the register prospective and inserts no example names. Requirement (1) verified.

**F2. r90's new fixtures and maps created no false shared referent.** The four C1 fixtures share no id with any
other fixture directory (corpus sweep: shared ids involving an r90 dir = `{}`), borrow no cluster noun
(`rc=1`), and do not carry the cluster signature, so they stay outside R10 scope. Both new maps reference only
their own cluster's files (`rcA=1`, `rcB=1`); their anchor sets are disjoint. The r90 maps therefore strengthen
in-cluster provenance without manufacturing any cross-cluster claim. Requirement (2) verified.

**F3. No README carries a false `## R10 comparison outcomes` section; none carries a true one either —
correct, because no incoming cluster landed.** No README anywhere in the repo has that heading; the phrase
exists in `corpus/` only as the inline backticked destination in the new R10 appendix. The five READMEs r90
added contain no R10 text. Requirement (4) verified.

**F4. Register absence is by design and unchanged from r89.** `cross-cluster-contradictions.md` is absent at
both ends (`git cat-file -e` fatal on `e97613c` and `ca7f9ef`); the r89 demo remains the only tracked
cross-cluster knowledge file, byte-identical to baseline. Requirement (3) verified. The r89 F1 conclusion
(the register's emptiness is the correct trigger-state) therefore still holds under r90.

**F5. Freeze-then-verify passes.** Delivered `corpus/fixtures/check_bible.py` sha256
`ff9fd2aa…d1421` = X2+X3 composed on `e97613c` (byte-identical), and both clusters replay `CLEAN`/exit 0.
No mismatch to report as blocking.

**Named debt (register + referents).**
- *Scoping rule still unstated (carried from r89 F2).* The delivered R10 governance still does not state that
  the comparison is scoped to **landed clusters** rather than fixture directories; the appendix says names/IDs
  trigger comparison but defines scope by referent evidence, not by directory class. The corpus still contains
  55 ids shared across scaffolding dirs (`harbor`, `mira`, `seal`, `tower`, …), and an unscoped application
  would manufacture candidates. None does today (by construction — no cluster involvement), but the guard is
  documented only in `.ufo` wave text, not in the knowledge file.
- *Register file/format conventions.* Still no file, header, ordering, or ID-uniqueness convention for
  `cross-cluster-contradictions.md`; the first real entry must create it. Unchanged from r89; not a defect
  while no genuine conflict exists.
- *`## R10 comparison outcomes` has no schema.* The appendix names the fields (paths, claim pointers, support
  occasions/scope, rationale) in prose only; no checker reads either destination. Manual gate as stated.
  Unexercisable until an incoming cluster lands — not verifiable, not defective.
- *Adjacent, outside this seat's verdict:* the r89 ledger-row placement oddity in `reference-ledger.md`
  (Spence row after the closing paragraph) is unchanged at `ca7f9ef` and remains for the C2/C7 ledger lane.

## Handoff

- **Answers.** (1) The cross-cluster shared-referent comparison is empty at every level tested, including the
  new r90 artifacts — the register's trigger state is correctly empty. (2) r90's four new fixtures and two new
  maps introduce no false shared referent: no shared ids, no cross-mentions, disjoint anchors, no cross-cluster
  path references. (3) `corpus/knowledge/cross-cluster-contradictions.md` remains absent at baseline and
  delivered. (4) No README carries a `## R10 comparison outcomes` section — false or otherwise; the only
  corpus-side mention is the appendix's inline destination. Freeze-then-verify passed (check 8).
- **Verdicts.** R10 appendix + register no-false-entry boundary: **improved**; referent state: **unchanged —
  correctly empty**; referent hygiene of r90's new artifacts: **unchanged — no harm**; register operability:
  **unprovable-but-better**. No axis harmed; no blocking finding.
- **Files written:** `.ufo/waves/round-90/followup/JDEP3.md`,
  `.ufo/waves/round-90/followup/JDEP3-probes.json`. Scratch under `/dev/shm/jdep3r90/` (no `/tmp` writes;
  `/tmp` is inode-exhausted on this host — worth passing to the wave as a local environment fact). No tracked
  file touched, no commit, no push.
- **For the integrator.** Fold F1–F4 as the register-integrity evidence for C3's R10 sub-case: the decided
  governance landed, the live register correctly stays absent, and the new artifacts manufactured no referent.
  The still-open scoping-rule debt (r89 F2) is the one concrete item to add when the register file is first
  created. My freeze check (8) independently confirms the C1 checker freeze; tuple-census judgment remains with
  the C1 seats.
- **Gaps.** No gap from the wait window (HEAD constant `ca7f9ef`, dirty `0` at both checks; sibling follow-up
  artifacts landed — `followup/` went 1 → 2 files, Q1-r90-debt.json → H2-delta.json). Unresolved by
  construction: no genuine cross-cluster conflict exists, so no end-to-end register-append receipt can be
  produced this round, and the README audit section remains unexercised.
