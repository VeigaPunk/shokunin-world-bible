# V01 — c1-commits (round 102, capstone)

- lane: lore-shokunin; round 102; seat V01 (verifier, commit-hash axis); model zai-coding-plan/glm-5.3-flash-low; date 2026-10-18
- baseline: r101 closure `542021a`; HEAD at verification time `8fa2e87` ("lore r102: declare capstone round before dispatch"); wave tree uncommitted per convention
- verified target: `corpus/knowledge/r102-push-synthesis-r95-r102.md` (U1-owned, present at poll try ~35, 15804 bytes)
- producer report polled and found: `.ufo/waves/round-102/seats/U1-synthesis.md`
- poll protocol honored: 5 batches × 14 tries × 20 s ≈ 23 min (within the 40-try cap); artifacts absent for the first ~28 tries, found mid-batch-5
- read-only seat: no file written except this report; no commits, no pushes, no network, no nested agents

## Method

Every SHA-like token was extracted from the synthesis, then each token was
classified and checked:

```
grep -oE '\b[0-9a-f]{7,40}\b' corpus/knowledge/r102-push-synthesis-r95-r102.md | sort -u
→ 27 unique tokens
```

Classification of the 27:

- **25 are commit-hash citations** (the 24 in the record's §4 self-audit
  list, plus `e97613c` cited in §3 as the negative-control `--checker`
  reference).
- **2 are not commits:** `ff9fd2aa6811` and `857d1421` — the first/last 12
  hex chars of the checker pin in `corpus/tools/boundary-doc-contract.json`
  line 12: `"sha256": "ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421"`.
  Both correctly fail `git cat-file -t` (`fatal: Not a valid object name`),
  confirming they are file-content pin fragments, not git objects. Correctly
  excluded from the commit audit.

Checks per commit token (run from lane root, 2026-10-18):

```
git cat-file -e <hash>^{commit}          # existence
git merge-base --is-ancestor <hash> HEAD # ancestry of HEAD (exit 0 = yes)
git log -1 --format='%h %ad %s' --date=short <hash>
```

## Results — 25/25 exist, 25/25 ancestors of HEAD, 0 fail

| Hash | exists | ancestor | Subject observed |
|---|---|---|---|
| 9c2eea3 | OK | YES | r93: close verified claims and correct historical admission records |
| abbc3e0 | OK | YES | r94: checkpoint Luna WORK candidate pending DeepSeek review |
| 65a9329 | OK | YES | r94: declare DeepSeek FOLLOW-UP before dispatch |
| ac69044 | OK | YES | r94: land admission conditions C-1..C-4,C-6 — map_obligations registry row… |
| fb118c4 | OK | YES | r94: close round — SCORECARD admitted section + LOG closure… |
| dcb2d92 | OK | YES | r95: freeze admitted wave + closure docs … receipt 64/64 |
| 60dba0c | OK | YES | r95: close round — SCORECARD admitted section |
| f3e09f9 | OK | YES | r96: freeze admitted wave + closure docs … receipt 64/64 |
| 2393934 | OK | YES | r96: close round — SCORECARD admitted section |
| 9d25df9 | OK | YES | r97: freeze admitted wave + closure docs (pinning/ freeze hardening…) |
| 9a3d648 | OK | YES | r97: drop embedded scratch clone (V37 mirror-freeze gitlink)… |
| 4265df5 | OK | YES | r98: freeze admitted wave + closure docs (hyper completion wave…) |
| 111b9a3 | OK | YES | r98: close round — SCORECARD admitted section |
| 337f0fa | OK | YES | r99: record blocked dispatch attempt (xai-oauth credential pool missing)… |
| fe1ce46 | OK | YES | r99: freeze admitted wave + closure docs (ten-file pins…) receipt 128/128 |
| ae67105 | OK | YES | r99: close round — SCORECARD admitted section |
| b5fe472 | OK | YES | r100: declare sol-max 32-seat round before dispatch |
| 6f86bf2 | OK | YES | r100: freeze admitted wave + closure docs (chain seven…) receipt 34/34 |
| a04f986 | OK | YES | r100: close round — SCORECARD admitted section |
| ebec6bb | OK | YES | r101: declare GLM 28-seat round before dispatch |
| ceeef43 | OK | YES | r101: freeze admitted wave + closure docs (chain eight…) receipt 30/30 |
| 542021a | OK | YES | r101: patch receipt with the L1-added 30th seat row |
| 60e88bf | OK | YES | r101: close round — SCORECARD admitted section |
| 8fa2e87 | OK | YES | r102: declare capstone round before dispatch (HEAD itself) |
| e97613c | OK | YES | r89: closure — verdicts ruled … (the `--checker` reference) |

Every hash's observed subject matches the role the synthesis assigns it
(declare → freeze → close per round; `337f0fa` as the blocked r99 attempt;
`9a3d648` as the r97 scratch-clone drop; `8fa2e87` = HEAD). Round ordering
in §1/§2 (e.g. r95 `fb118c4` → `dcb2d92`; r101 `6f86bf2` → `ceeef43` +
`542021a`) is consistent with the observed history.

## Finding (calibration residue, not a broken citation)

The synthesis §4 states: "Commit-hash verification (this pass): **all 24
hashes cited in this record** were checked…" — the record actually cites
**25** commit hashes: the 24 listed plus `e97613c` (§3, `discriminate_check.py`
negative control `--checker e97613c`). `e97613c` itself is valid (exists,
ancestor of HEAD, r89 closure), so the falsifiable C1 core "every cited
commit hash exists" holds — but the self-audit's count and list are
incomplete by one. U1's own producer report (`U1-synthesis.md` line 34)
repeats the same "all 24 hashes" count. A dated one-line addendum by U2 or
acceptance as a recorded erratum would close it; it does not affect
admissibility of C1's commit axis.

Case-insensitive re-sweep (`grep -oiE`) confirmed no additional uppercase
hash variants; token set stable at 27.

## Per-axis verdict

- **coverage (of my mandate): improved** — all 27 SHA-like tokens in the
  synthesis classified; all 25 commit citations checked for existence AND
  ancestry (the mandate's two predicates), 0 failures.
- **calibration: improved, bounded** — one self-audit undercount found
  (24 claimed vs 25 actual commit citations; the omitted hash is itself
  valid); no false existence claim, no dead hash.
- **depth/operability/freshness/adjacency:** not in this seat's scope;
  witnessed unharmed (read-only pass; no corpus bytes touched).

Bottom line: **PASS** — all 25 commit hashes cited in the synthesis exist
(`git cat-file -e`) and are ancestors of HEAD (`git merge-base
--is-ancestor`), subjects match their assigned roles; sole residue is the
record's "all 24 hashes" self-audit undercounting by one (missing valid
`e97613c`).
