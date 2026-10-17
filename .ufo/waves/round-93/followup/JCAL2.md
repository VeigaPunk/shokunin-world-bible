# JCAL2 — Tool judge (certification), round-93 follow-up

Tree judged: `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` (HEAD == r93 work commit; `git status --porcelain` empty at probe start). Target: `corpus/tools/boundary_doc_check.py` (16,780 bytes, 405 lines) against `corpus/knowledge/holder-assessment-boundary.md` + `corpus/fixtures/check_bible.py`.

## Work performed

Axes: (A1) baseline certification run; (A2) tampered-checker adversarial → hash pin; (A3) contradictory-C9-doc adversarial → C9 gate; (A4) tool README names AST/content-signature anchor validation as unimplemented r94 debt; plus one missing-file robustness control. All probes ran from the repo root; adversarial inputs were scratch copies under `/tmp` (removed after evidence capture). No repo writes besides this file. Two wave-dir checks: `followup/` absent at probe start; at handoff time it holds JCAL1/JCAL3 artifacts — my mission consumed no sibling artifacts, so no wait was needed.

## Before → after measurements

**A1 — baseline (expect CERTIFIED, exit 0). Command:** `python3 corpus/tools/boundary_doc_check.py; echo "[rc=$?]"`. Observed:

```
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
[rc=0]
```

Precondition verified: `sha256sum corpus/fixtures/check_bible.py` → `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` — byte-exact match to the pin at `boundary_doc_check.py:389`. The delivered doc hashes `7f815a93…4ec33e` (matches the value pinned in `patches/W2-scorecard-r93.proposal.md`).

**A2 — tampered checker (expect exit 1, named hash-pin failure). Command:** `cp corpus/fixtures/check_bible.py /tmp/jcal2-tampered-checker.py && printf '\n# tampered\n' >> /tmp/jcal2-tampered-checker.py && python3 corpus/tools/boundary_doc_check.py --checker /tmp/jcal2-tampered-checker.py; echo "[rc=$?]"`. Observed: the three CHECK lines all PASS and `replay_receipts=3/3`, `replay_cases=14/14`, `anchors=2/2` (the appended comment does not change behavior, so receipts still replay byte-identically — the pin is the sole tripwire), then:

```
FAIL: checker hash pin: 2a84b41e1b111cd0... != pinned ff9fd2aa6811a813...
CERTIFICATION FAIL
[rc=1]
```

**A3 — contradictory C9 doc (expect exit 1, named C9 failure). Command:** `cp corpus/knowledge/holder-assessment-boundary.md /tmp/jcal2-c9-contradiction.md && printf '\nholder identity is not uniquely resolvable: {expected}\n' >> /tmp/jcal2-c9-contradiction.md && python3 corpus/tools/boundary_doc_check.py --doc /tmp/jcal2-c9-contradiction.md; echo "[rc=$?]"`. Observed: the only edit is the forbidden legacy tick-qualification sentence appended at EOF; all CHECK lines PASS, `replay_cases=14/14`, `anchors=2/2`, then the single failure line:

```
FAIL: C9 semantics: required markers missing or a legacy tick-qualification claim present
CERTIFICATION FAIL
[rc=1]
```

**Control — missing `--checker` input. Command:** `python3 corpus/tools/boundary_doc_check.py --checker /tmp/jcal2-nonexistent.py 2>&1 | tail -4`. Observed: uncaught `FileNotFoundError: [Errno 2] No such file or directory: '/tmp/jcal2-nonexistent.py'` traceback, rc=1. Fails closed but without a named failure line (see debt below).

**A4 — README r94 naming. Evidence:** `git grep -c -i "boundary" -- corpus/tools/README.md` → no match; the landed README (36 lines) documents only `support_check.py` and `discriminate_check.py`. `git grep -n "boundary_doc_check" -- .` outside `.ufo/waves/round-93/` → zero hits tree-wide: no corpus README references the tool at all. The unlanded proposal `patches/CERT-tool.patch` adds a 14-line `## Boundary document certification` README section — and even that proposed section names only usage (replay/citations/H1/markers), not the AST/content-signature limitation.

## Findings & named debt

1. **A1 improved / A2 improved / A3 improved — confirmed on the committed tree.** The tool certifies the delivered pair (rc 0) and fails closed with exactly one named failure per adversarial mode; single-failure isolation in A2/A3 shows no collateral gate noise and no trade. This directly closes the holes CB-audit falsified in the patch-only candidate (`.ufo/waves/round-93/CB-audit.md:277`: changed checker and injected contradiction both returned `exit=0` `CERTIFIED` there; the landed tool returns named rc=1 for both).
2. **A4 NOT CONFIRMED — named debt (README gap).** The claim "the tool's README names the AST/content-signature anchor validation as unimplemented (r94 debt)" is false at 65838f8: `corpus/tools/README.md` contains no boundary_doc_check section, and `r94` / `content-signature` / `AST anchor` have zero occurrences under `corpus/` anywhere. The limitation IS named in the committed tree, but only in wave artifacts: `.ufo/waves/round-93/CERT.md:3` ("Anchor checks are line-existence only … they do not verify source-content signatures") and `CERT.md:185`, plus `patches/Q1-r93-debt.json` / `Q1-r94-proposal.md`. Follow-up: land a README usage section for the tool that explicitly states anchor checks are line-count-existence only (no AST/content-signature validation) and name it r94 debt. Note the substance is real: `check_anchors` (boundary_doc_check.py:262-282) validates cited `check_bible.py:NNN[-MMM]` ranges against the checker's line count only.
3. **Robustness debt — unguarded input reads.** `checker_pin_check(args.checker)` (line 346) and `c9_semantics_check(pathlib.Path(args.doc).read_text())` (line 349) run before the guarded doc read (lines 351-357); a missing `--checker` or `--doc` path crashes with an uncaught traceback instead of printing a named `FAIL:` line. Exit is still non-zero (fails closed), so no false-pass risk — candidate r94 item alongside AST anchor validation.
4. **Cosmetic/stale narrative, not a tool defect:** `CERT.md:185` says the tool "does not implement B3's broader AST/content-signature or C9 semantic review", but the landed tool does implement the C9 gate; that sentence describes the pre-landing patch candidate.

## Handoff

- Verdict words per axis: A1 improved, A2 improved, A3 improved, A4 unchanged (README gap — naming exists only in `.ufo/waves/round-93/CERT.md:3,185`, not in `corpus/tools/README.md`).
- r93 C1 certification claim holds for tool behavior (pin + C9 gate both trip named failures); the C1 claim as worded ("AST anchor validation named r94 debt" in the tool's README) is only half-landed: debt named in wave artifacts, absent from the tool README.
- Suggested r94 queue additions: (1) land the README section with the r94 AST/content-signature debt statement; (2) guard missing `--doc`/`--checker` inputs into named failures; (3) AST/content-signature anchor validation (pre-existing r94 item).
- Repo state after my probes: untouched except this file; `git status --porcelain` shows only `?? .ufo/waves/round-93/followup/` (siblings' untracked files + mine). Scratch files under `/tmp` removed. No commits, no pushes.
