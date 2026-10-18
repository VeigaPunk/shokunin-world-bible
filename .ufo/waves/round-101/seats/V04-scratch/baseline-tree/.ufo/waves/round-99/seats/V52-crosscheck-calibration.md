# V52 — verdict-crosscheck-calibration (round 99)

Seat: V52 `verdict-crosscheck-calibration`. Exclusive report:
`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V52-crosscheck-calibration.md`.
Scratch: `.ufo/waves/round-99/seats/V52-scratch/` (poll log only, plus one superseded
mid-write mirror that was not used as a verdict). Leaf seat: no nested agents, no
commits, no pushes, no network, no product-file writes.

Task: independent calibration verdict on C1 (full-file freeze pinning), then compare
with V28. Protocol: artifacts AND producer reports must exist; 20 s cadence, 40 tries;
ABSENT, never verify a plan. Endgame: this seat did not run an all-reports poll, so
SELF subtraction was not required. Baseline declared as r98 closure `4265df5`
(`4265df5e86e4121bde4125b649b89bb1676676a5`, ancestor of HEAD). HEAD during the wait:
`337f0fa52b02626b7687eedbb2d99fab30446fe4`. Lane root for every command:
`/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo).

## 1. Poll-wait record

Wait set (SELF excluded): `S1-*.md`, `S2-*.md`, `dependency_freeze.py` changed vs
`4265df5`, `dependency-freeze-contract.json` changed vs `4265df5`. V28 was not in
this wait set; comparison was a second check after the producer gate.

First poll process (`V52-scratch/poll.sh`, background) was killed by a 600 s host
timeout after try 30 (bounded stall-escape, recorded, not treated as a verdict).
Tries 31–40 were completed in a second process. Log:
`.ufo/waves/round-99/seats/V52-scratch/poll.log`.

```
try 1  2026-10-17T22:02:20-03:00 missing: REPORT:S1 REPORT:S2 CONTRACT-UNCHANGED
try 7  2026-10-17T22:04:20-03:00 missing: REPORT:S1 REPORT:S2
try 30 2026-10-17T22:12:00-03:00 missing: REPORT:S1 REPORT:S2
try 31 2026-10-17T22:26:10-03:00 missing: REPORT:S1 REPORT:S2
try 40 2026-10-17T22:29:10-03:00 missing: REPORT:S1 REPORT:S2
try 40 2026-10-17T22:29:30-03:00 ABSENT
```

(The second process exited 2 on the ABSENT line. Gap 22:12→22:26 is the killed
process plus the restart, not a skipped try count: tries 1–30 and 31–40 are both
in the log.)

Producer reports never appeared. Final existence check, quoted:

```
$ date -Is
2026-10-17T22:32:40-03:00
$ find .ufo/waves/round-99/seats -maxdepth 1 \( -name 'S1-*.md' -o -name 'S2-*.md' -o -name 'V28-*.md' \) -printf '%f\n'
(empty)
```

No calibration battery was run against a claimed delivered revision. No `--self-test`,
no chain verify, no Markdown-tamper demo, no guarded `--freeze`. Those would be
verifying an unreported plan.

## 2. What existed, and why it was not scored

Bytes moved, but without S1/S2 reports they are not a delivered revision.

```
$ git rev-parse HEAD
337f0fa52b02626b7687eedbb2d99fab30446fe4
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
$ git diff --quiet 4265df5 -- corpus/tools/dependency_freeze.py; echo tool_unchanged=$?
tool_unchanged=1
$ git diff --quiet 4265df5 -- corpus/tools/dependency-freeze-contract.json; echo contract_unchanged=$?
contract_unchanged=1
$ git diff --quiet 4265df5 -- corpus/tools/README.md; echo readme_unchanged=$?
readme_unchanged=0
$ git diff --quiet 4265df5 -- SKILL.md; echo skill_unchanged=$?
skill_unchanged=0
```

Mtimes at that check: tool `2026-10-17 22:07:33 -0300`, contract `2026-10-17 22:08:46 -0300`,
README `2026-10-17 21:32:05 -0300`, SKILL.md `2026-10-17 21:34:23 -0300` (both docs
pre-wave; S2's owned surfaces had not changed). Baseline tool/contract hashes at
`4265df5` (extracted, not live): tool `03d04365cf00903e783562d8d760a0f751e477af218b79e6484ab34a9315a24b`,
contract `153ebc5b2092948ef43a8693bc1ebd6a0ace80d798210a8d54c96d6e0573a947`.

Superseded mid-write, not a verdict: at tool hash `1728ed892442…` (before
`6f81f8be…`), a scratch-mirror verify of `r95-crossing-aftermath` against the
still-baseline contract exited 2 with
`FINDING CONTRACT-INVALID: pin r95-crossing-aftermath payload_schema_version None != 2`.
That hash was replaced. It is not evidence about the later bytes, and those later
bytes were not verified.

## 3. Comparison with V28

V28's report was absent at the 22:32:40 check (`V28-*.md` not under
`.ufo/waves/round-99/seats/`). No verdict text existed to compare. V28 scratch
was not treated as a verdict. Comparison: **ABSENT**.

## 4. Verdict

Independent calibration verdict: **not derived**. C1 was not admitted, not
rejected, and not scored improved/unchanged/harmed. Producer reports S1 and S2
did not land within 40 tries. Scoring the unreported tool/contract bytes would
have been verifying a plan.

ABSENT — S1 and S2 reports never landed (40 tries); C1 not verified; V28 report absent, no comparison.
