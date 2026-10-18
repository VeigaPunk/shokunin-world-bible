# V22 — c3-tamper (round 96)

- Seat: V22 `c3-tamper`. Scope per seat spec: poll for Q3, then tamper demonstrations on
  `corpus/tools/dependency_freeze.py` + `corpus/tools/dependency-freeze-contract.json`:
  (a) one non-edge fixture JSON byte changed → exit 2 digest mismatch; (b) `--freeze` on a
  copy then verify → clean; (c) confirm pins pin CONTENT (not just edges) so silent non-edge
  edits are caught.
- Leaf seat: no nested agents, no commits, no network. Writes: this report plus
  `.ufo/waves/round-96/seats/V22-c3-tamper.scratch/` only. All mutations ran inside the
  scratch workspace; the real corpus was never written (verified below).
- Repo root `/home/vgpnk/Projects/shokunin/lore-shokunin`; baseline r95 closure `dcb2d92`;
  working-tree HEAD `60dba0c` (r95 SCORECARD closure). All commands from the repo root with
  `python3`.
- **Frozen revision verified** (hash-stable through all final runs; Q3 report
  `Q3-dependency-freeze.md` sha256 `5e97f7e94fb83e08f661b6ca8c123adbbda512bbaeecac63404a8fb4ed3d035a`):

```
$ sha256sum corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
a3b57978f0cbf314389ee3f9862920a46cf109fca6d1eec488c39be0457f0980  corpus/tools/dependency_freeze.py
7d568cc422cda42297b7506a1a3e083e8798866efd16d58617bf4ea468576975  corpus/tools/dependency-freeze-contract.json
$ stat -c "%y %s %n" corpus/tools/dependency_freeze.py corpus/tools/dependency-freeze-contract.json
2026-10-17 17:44:37.812881330 -0300 20552 corpus/tools/dependency_freeze.py
2026-10-17 17:44:27.305998265 -0300 12032 corpus/tools/dependency-freeze-contract.json
```

## 0. Poll-wait log

- Poll 1 (20 s cadence, started ~17:38:40): tool+contract first present at t=220–240 s
  (~17:42:35/47); producer report absent — Q3 was still iterating (contract changed size
  8113 → 10348 → 12032 bytes; tool 20457 → 20499 → 20552). POLL_HIT at t=260 s matched only
  `Q3-scratch/` (a directory), so verification was **not** started on that revision.
- Poll 2 (20 s cadence + 30 s mtime-stability gate, started 17:44:5x):
  `POLL_STABLE checks=9 report=…/Q3-dependency-freeze.md tool_mtime=1792269877 contr_mtime=1792269867`
  — i.e. the Q3 report exists and both artifacts were mtime-stable for 30 s (17:44:27/37,
  unchanged at 17:47:42 and 17:49). All results below are on this frozen revision.

## 1. Precondition — declared chain verifies 4/4 clean

```
$ for d in r88-m3-maya-cluster r94-paired-crossing r95-crossing-aftermath r96-crossing-response; do
    python3 corpus/tools/dependency_freeze.py corpus/fixtures/$d; echo "EXIT=$?"; done
FREEZE r88-m3-maya-cluster: events 2/2; dependency-edges 0/0; relations 0/0
DIGEST 15ef230ef806ea7e7431f5afc7d999aee978b024cf47f2a20cbba726fc3fc279
RESULT PASS  EXIT=0
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
DIGEST 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75
RESULT PASS  EXIT=0
FREEZE r95-crossing-aftermath: events 4/4; dependency-edges 3/3; relations 1/1
DIGEST d541ae641f3189e1586f011ec565ee8982a389949580d2b052b9b9e8e66d2ec9
RESULT PASS  EXIT=0
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
DIGEST d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6
RESULT PASS  EXIT=0
```

`--self-test` on the frozen revision: `SELF-TEST 14/14` / `RESULT PASS` / exit 0 (full run in
`scratch/final-pass.log`). r96 verifies clean with Q5's `README.md` + `claim-excerpt-map.md`
present — consistent with Q3 §1: the digest covers the five JSON tables only.

## 2. Non-edge JSON byte tamper → exit 2 DIGEST-MISMATCH

All mutations on copies under `scratch/muts/`; the pinned basename is preserved so the pin
resolves.

**T1 — r96 `sources.json`, one character (`…Response Note` → `…Response note`).**
`sources.json` carries no semantic inventory at all, so the digest is the only catcher:

```
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
FINDING DIGEST-MISMATCH: content digest f5656e9912583e96a29acf2a7d82d33c6cef862b074a0346c215e6350a36d89a != pin d422a9b3d95c4e0b8aac98cc87806a94949896adb962a50d2d55a6c11657d7f6; fixture bytes changed outside the frozen inventory
RESULT ERROR  EXIT=2
```

**T2 — r94 `timeline.json`, description text only (`south bell at Salt Court` → `South …`,
`depends_on`/endpoints untouched).** Inventory-neutral, still caught:

```
FREEZE r94-paired-crossing: events 3/3; dependency-edges 2/2; relations 1/1
FINDING DIGEST-MISMATCH: content digest af388b771ad67e270279f4a0d943dc707a87106c763eb23fcb203508fd988e3e != pin 2527beb938b474a28d66e1c716f54ba829ae3cc2e616513cd2960a8f7ecebe75; …
RESULT ERROR  EXIT=2
```

**T3 — contrast, edge tamper (BR-01 class):** r94 copy with `evin-ninth-bell` dropped from the
tick-10 `depends_on` → semantic path wins, digest not reached:

```
FREEZE r94-paired-crossing: events 3/3; dependency-edges 1/2; relations 1/1
FINDING REDUCTION-DETECTED: event paired-crossing-decision lost depends_on ['evin-ninth-bell']
RESULT FAIL  EXIT=1
```

Receipt counters move (`2/2` → `1/2`) with pinned totals held — same shape as Q3 §3/§4.

## 3. Pins pin CONTENT, not just edges (independent recomputation)

- Pin structure (contract `pins.<fixture>`): `files` = per-file sha256 for all five present
  JSON tables, plus `content_sha256` = sha256 over the sorted/compact JSON of those per-file
  digests (tool `content_digest()`), plus `events`/`relations`/`counts`.
- I recomputed the content digest independently with two methods (re-implementation, and a
  `sha256sum`-based reconstruction) via `scratch/indep_digest.py`; both agree for all four
  fixtures and **equal the pinned digests exactly** (output in `scratch/final-pass.log`):

```
r88-m3-maya-cluster   15ef230e…  (pin 15ef230e…)
r94-paired-crossing   2527beb9…  (pin 2527beb9…)
r95-crossing-aftermath d541ae64… (pin d541ae64…)
r96-crossing-response d422a9b3…  (pin d422a9b3…)
```

- Consequence demonstrated: T1/T2 (non-edge edits, including a file with zero semantic role)
  are caught; the pin proves byte identity to the recorded bytes, not merely edge-set equality.

## 4. `--freeze` on a copy then verify → clean

**T4 — freeze the T1-tampered r96 copy, then verify it:** re-pins the current bytes and passes.

```
FROZEN r96-crossing-response: events 5; dependency-edges 4; relations 1
DIGEST f5656e9912583e96a29acf2a7d82d33c6cef862b074a0346c215e6350a36d89a
FREEZE r96-crossing-response: events 5/5; dependency-edges 4/4; relations 1/1
RESULT PASS  EXIT=0
# verify after freeze: DIGEST f5656e99… / RESULT PASS / EXIT=0
```

**T4b — freeze a pristine r94 copy:** `FROZEN … DIGEST 2527beb9… / RESULT PASS / EXIT=0`;
verify after → `RESULT PASS / EXIT=0`.

These ran against the workspace's own contract copy (`scratch/ws/corpus/tools/…`), so the
delivered contract was not written; the repo contract's sha256 was `7d568cc4…` before and
after the whole matrix.

## 5. Named boundaries and hazards (reported, not hidden)

**H1 — the digest scope is the five JSON tables; Markdown is not pinned.** T5b: appending a
comment line to a copy's `README.md` leaves the gate green (`DIGEST 2527beb9… / RESULT PASS /
EXIT=0`). README/`claim-excerpt-map.md`/`fictional-excerpts.md`/`inspiration-note.md`/
`source-excerpt.md` edits are invisible to this gate. Consistent with the contract's
`data_files` scope and Q3 §1; disclosed as a bound, not a defect.

**H2 — `--freeze` writes the delivered contract from any path (confirmed pollution + rebind).**
`CONTRACT_PATH` is resolved from the script location, so running the repo tool's `--freeze`
on *any* directory rewrites `corpus/tools/dependency-freeze-contract.json`. Consequences
observed in the frozen revision:

- The contract carries a foreign fifth pin `c3red` (`fixture:
  ".ufo/waves/round-96/seats/V41-scratch/c3red"`, digest `eff4b354…`, counts events 3 /
  edges 1 / relations 1 — the BR-01-mutated r94 inventory). Evidence: V41's
  `V41-scratch/c3-freeze.out` (`FROZEN c3red … RESULT PASS`) and `c3-interim.log` line
  `--freeze on scratch copy EXIT=0`. Q3 §7 documents it and deliberately left it because
  verifier receipts cite the pinned list. Chain verification is unaffected (pins are
  basename-keyed; no corpus fixture is named `c3red`), but the delivered contract now
  references a scratch path and pins a mutated inventory under a foreign key — cleanup
  decision belongs to closure.
- Stronger variant (my T4c, workspace only): freeze a **mutated** copy named
  `r94-paired-crossing` → the pin for that basename is rebound to the mutated inventory
  (`dependency-edges 1`); verifying the **pristine** fixture then reports
  `FINDING ADDITION-DETECTED: event paired-crossing-decision gained depends_on
  ['evin-ninth-bell']` / exit 1 — a false positive on untouched delivered content. Restoring
  the contract → `RESULT PASS / EXIT=0`. This extends Q3 §7's recommendation: a `--freeze`
  scope guard (refuse paths outside `corpus/fixtures/`) or an explicit `--out` target would
  close the class; the guard was intentionally not added mid-round (tool hash frozen for the
  verifier battery), so it stands as a named r97/closure item.

## 6. Corroboration of Q3's self-test defect disclosure

Independently observed before the report landed: at the 17:43 revisions `--self-test` printed
`SELF-TEST 5/14`, every mutated case failing with the *same* `FILE-MISSING … missing_timeline/…`
receipt — the late-binding bug Q3 §5 reports (all case lambdas capturing one `scratch`
variable), plus a traceback-vs-`INVALID-ARGUMENTS` issue. After the 17:44:37 fix the frozen
revision prints `SELF-TEST 14/14 / RESULT PASS / exit 0`. Q3's defect history is accurate and
the frozen revision is the fixed one; verify semantics were unaffected (T0–T4c all reproduce
on the frozen revision).

## 7. Write audit

```
$ git status --short
 M LOG.md                                       # round declaration (pre-seat)
 M corpus/tools/map_obligations.py              # Q1
?? .ufo/waves/round-96/                         # seats/scratch (incl. this report)
?? corpus/fixtures/r96-crossing-response/       # Q4/Q5
?? corpus/knowledge/r96-response-scope-note.md  # Q6
?? corpus/tools/dependency-freeze-contract.json # Q3
?? corpus/tools/dependency_freeze.py            # Q3
```

Repo tool/contract sha256 unchanged across my entire run (`a3b57978…` / `7d568cc4…`); the four
chain fixtures' `timeline.json`/`relations.json` sha256 match the values pinned in the
contract and my pre-pin baseline. All writes confined to this report + `V22-c3-tamper.scratch/`.

## Bottom line

PASS — on the frozen revision (`dependency_freeze.py` `a3b57978…`, contract `7d568cc4…`,
Q3 report present and stable): chain verifies 4/4 clean, `--self-test` 14/14, a one-byte
non-edge JSON edit (even in a semantically inert file) exits 2 `DIGEST-MISMATCH`, the BR-01
edge drop exits 1 `REDUCTION-DETECTED`, `--freeze` on copies re-pins and re-verifies clean, and
pins are independently confirmed to pin file CONTENT (two-method recomputation equals the
pinned digests); two named residuals reported, not concealed — the foreign `c3red` scratch pin
present in the delivered contract (cleanup at closure) and the unguarded `--freeze`
contract-rewrite/rebind hazard (T4c false positive demonstrated in workspace), plus the
Markdown-outside-digest boundary.
