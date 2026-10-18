# V82 — crosscheck-operability (round 99)

Seat: V82 verdict-crosscheck-operability. Lane root `/home/vgpnk/Projects/shokunin/lore-shokunin` (session cwd is the parent repo; every path below is absolute or lane-root anchored). Baseline r98 closure `4265df5` (`4265df5e86e4121bde4125b649b89bb1676676a5`). HEAD during the wave `337f0fa52b02626b7687eedbb2d99fab30446fe4` (wave tree uncommitted). Leaf seat: no nested agents, no commits, no pushes, no network. Writes: this report and `.ufo/waves/round-99/seats/V82-scratch/` only. `realpath` of the seats dir before the write: `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats`.

Charge: independent operability verdict; compare V31. Operability is a witnessed axis (owned set is depth, coverage, calibration). The verdict surface is every documented command in the round's new documentation (S2 tools README addendum + SKILL.md freeze row, S4 r99 README replay block, S5 blind-spot table + lapse scope note), the 0/1/2 exit contract, and the C1 operability behavior (full-file pin, `DIGEST-MISMATCH` naming the file, chain 6/6, self-test 17→18). Never verify a plan.

## 0. Poll-wait (20 s cadence, 40 tries) — ABSENT

Command (lane root, started 2026-10-17T22:14:57-03:00):

```
/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-99/seats/V82-scratch/poll.sh
```

Content gates: r99 README must contain `r99-window-lapse`; map must contain `clerk-lapse-recorded` or `r99-window-lapse`; timeline must contain `clerk-lapse-recorded`; contract must have ≥18 self-test cases or a pin payload naming a Markdown file; tools README must contain `Round-99` / `Round 99` / `r99`; S1–S5 reports must exist as non-empty `S*-*.md`. SELF was not in the wait set. No all-reports poll was run (endgame convention: nothing to subtract SELF from).

Observed, identical missing set on tries 1 through 40 (`V82-scratch/poll.log`):

```
TRY 1 2026-10-17T22:14:57-03:00 MISSING 6 ABSENT:corpus/knowledge/r99-gate-blind-spot-table.md ABSENT:corpus/knowledge/r99-lapse-scope-note.md BASELINE:TOOLS-README REPORT:S1 REPORT:S2 REPORT:S5
TRY 40 2026-10-17T22:27:58-03:00 MISSING 6 ABSENT:corpus/knowledge/r99-gate-blind-spot-table.md ABSENT:corpus/knowledge/r99-lapse-scope-note.md BASELINE:TOOLS-README REPORT:S1 REPORT:S2 REPORT:S5
ABSENT after 40 tries
```

The poll process exited 2 after 780 s. No stall-escape was taken on the producer poll: the missing set did not shrink across 40 tries, and the protocol caps the wait at 40.

**Gate defect, recorded so the log is not misread.** The SKILL.md gate (`grep -q '18 cases\|18-case\|markdown'`) false-passed because the r98 freeze row already contains the word `Markdown` ("fixture Markdown is not pinned"). `BASELINE:SKILL` never appeared in the missing list. Independent check, not the gate:

```
$ stat -c '%y %n' SKILL.md corpus/tools/README.md
2026-10-17 21:34:23.607913842 -0300 SKILL.md
2026-10-17 21:32:05.149195103 -0300 corpus/tools/README.md
$ sed -n '96,100p' SKILL.md
- **entry command:** … frozen chain: r88-m3-maya-cluster, … r98-clerk-filing
- **self-test command:** … 17 cases (… r98 added `self_test_mismatch`) …
- **pinned-values path:** … content SHA-256 over the five JSON tables …
- **scope:** … over the five JSON tables per fixture. … BR-01's markdown/prose half remains open.
```

Both files are pre-wave (mtimes 21:32 / 21:34, before the 22:00 dispatch). The freeze row still documents 17 cases and a five-JSON-table payload. S2's documented command surface has not landed.

## 1. Re-check at report time (2026-10-17T22:36:08-03:00) — still absent

```
$ date -Is
2026-10-17T22:36:08-03:00
ABSENT corpus/knowledge/r99-gate-blind-spot-table.md
ABSENT corpus/knowledge/r99-lapse-scope-note.md
$ ls -1 .ufo/waves/round-99/seats/S*.md
.ufo/waves/round-99/seats/S3-fixture-author.md
.ufo/waves/round-99/seats/S4-fixture-docs.md
$ ls -1 .ufo/waves/round-99/seats/V31*.md
no V31 md
$ find .ufo/waves/round-99/seats -maxdepth 1 \( -name 'S1*' -o -name 'S2*' -o -name 'S5*' -o -name 'V31*' \)
d … 22:00 .ufo/waves/round-99/seats/S2-scratch          (empty, mtime unchanged since dispatch)
d … 22:36 .ufo/waves/round-99/seats/S1-scratch
d … 22:37 .ufo/waves/round-99/seats/S5-scratch
d … 22:32 .ufo/waves/round-99/seats/V31-scratch
```

No `S1-*.md`, `S2-*.md`, `S5-*.md`, or `V31-*.md` exists under the seats directory. S2's scratch directory is empty (0 bytes, mtime 22:00). S1 and S5 scratch directories were still being written after the cap (S5 `replay.py` 14,967 bytes at 22:32; S5 dir mtime 22:37; S1 dir mtime 22:36). That is late producer activity, not a delivered artifact. It does not reopen the 40-try cap.

## 2. What had landed — observed, not scored

These exist. They are not the operability surface this seat is charged to replay, and they are not treated as the delivered revision.

- S3 report `.ufo/waves/round-99/seats/S3-fixture-author.md` (5,069 bytes, 22:01) and the r99 fixture directory (ten files; timeline contains `clerk-lapse-recorded`).
- S4 report `.ufo/waves/round-99/seats/S4-fixture-docs.md` (9,303 bytes, 22:03). The r99 README is no longer the r98 placeholder: it is titled "Round 99 window-lapse continuation" and its replay block (lines 25–29) names `check_bible.py`, `support_check.py`, and `map_obligations.py` against `corpus/fixtures/r99-window-lapse`.
- In-flight freeze bytes, mtimes 22:07 / 22:08, **no S1 report**:

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
6f81f8be19742372ddc6819f6cf50dad985fe2bca2bee2b6e7c579613f5f4067  corpus/tools/dependency_freeze.py
8c2561b043c25db77f2628e02c38ba0691cbf7123c37bf295350479f7c197628  corpus/tools/dependency-freeze-contract.json
```

A read of that contract (not a verdict) showed `schema_version` 2, `payload_schema_version` 2, 18 self-test cases including `markdown_tamper` (`exit` 2, `finding_ids` `["DIGEST-MISMATCH"]`, `names_file` `fictional-excerpts.md`), and each of the six existing pins listing ten files. r99 is not in the pin set. The r98 baseline extracted to scratch (`git show 4265df5:…`) is still `03d04365…` / `153ebc5b…`, schema 1, 17 cases, five JSON files per pin. The live bytes differ from that baseline. Without S1's report and without S2's documented commands, those bytes are an unclosed edit, not a delivered operability surface. This seat did not run `--self-test`, the chain, or a Markdown-tamper probe against them.

## 3. Comparison to V31 — not possible

V31's report is absent. No file matching `.ufo/waves/round-99/seats/V31*.md` exists. V31's scratch holds a poll log (updated 22:33) and battery transcripts (22:32). Those are not a seat report. This seat did not read them as a verdict and did not form an independent operability verdict to compare against, because the documented command surfaces had not landed. There is no agreement, contradiction, or divergence to record.

## 4. What was not done

- No replay of S4's three commands, S2's (unwritten) addendum, or S5's (unwritten) table. Running them against an unclosed tree would be verifying a plan.
- No before/after Markdown-tamper demonstration. The before half is the committed r98 pin (five JSON tables; excerpt edits are outside the payload). The after half requires the delivered pin plus the documented command that names the file. Neither the S1 report nor the S2/S5 docs exist.
- No operability axis call (improved / unchanged / harmed / unprovable). An axis call on in-flight bytes would be a verdict on a plan.

## Bottom line

ABSENT — after 40 tries (22:14:57–22:27:58 -03) the operability surfaces were still missing (S1/S2/S5 reports, tools README Round-99 addendum, both r99 knowledge files) and V31's report was absent, so no independent operability verdict and no comparison were issued.
