## Work performed

- Axes: **method robustness of the census claim**, **census completeness**, **no-regression calibration**, and **stored-baseline-receipt integrity**.
- Seat JCAL5, method-varied census at HEAD `65838f867d6ece8e7b8bdcc4ffc667a08a1b785e` on `main`. Variation vs prior censuses: B1 = sorted order + live tree; B2 = reverse order + `git archive` extraction; JCAL1 = sorted + live rerun; H4 = sorted + live. **Mine: seed-9301 shuffled traversal, and BOTH sides regenerated — the 166-row baseline re-censused from `git archive 87779a0` and the 167-row after-census from `git archive 65838f8` — so no stored receipt is trusted as ground truth and the checker never runs from the live tree.**
- Same instrument and tuple schema as the wave baseline (`python3 -I corpus/fixtures/check_bible.py corpus/fixtures/<name>`; rows `{exit, stdout_sha256, violation_count}`), so deltas are directly comparable. Seeded order was re-derived a second time in-process and asserted identical (determinism check); it is neither sorted nor reverse-sorted.
- Dependency wait-checks: two 60s polls per wave rule; both targets present on first check (`POLL_HIT elapsed=0s checks=0`), no gaps, no waiting needed.
- An initial wholesale cross-check against H4's receipt flagged 167/167 "mismatches"; resolved as a schema difference (H4 rows carry an extra `stderr_len` field). On the three shared tuple fields H4 agrees on all 167 rows — both probes recorded below.
- Wrote only `.ufo/waves/round-93/followup/JCAL5.md`, `JCAL5-delta.json`, `JCAL5-tuples.json`. No commit, no push; scratch under `/tmp` removed by trap.

## Before → after measurements

**Baseline identity** — exact command:

```sh
git rev-parse HEAD && git status --porcelain --untracked-files=all | grep -v '^?? .ufo/waves/round-93/followup/' ; printf 'tracked_diff_exit=' && git diff --quiet HEAD --; echo "$?" && git branch --show-current && sha256sum corpus/fixtures/check_bible.py
```

Observed output:

```text
65838f867d6ece8e7b8bdcc4ffc667a08a1b785e
tracked_diff_exit=0
main
ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
```

(Tracked tree clean; the checker hash matches the C9 pin `ff9fd2aa…1421`, so before/after tuples are same-instrument.)

**Dependency wait-checks** — exact commands:

```sh
bash .ufo/waves/poll_wait.sh .ufo/waves/round-93/patches/B1-tuples.json 60
bash .ufo/waves/poll_wait.sh .ufo/waves/round-93/followup/JCAL1-tuples.json 60
```

Observed output:

```text
===WAITCHECK-1===
POLL_HIT path=.ufo/waves/round-93/patches/B1-tuples.json elapsed=0s checks=0
===WAITCHECK-2===
POLL_HIT path=.ufo/waves/round-93/followup/JCAL1-tuples.json elapsed=0s checks=0
```

**Method-varied double census** — shell wrapper: `mktemp -d /tmp/lore-r93-JCAL5.XXXXXX`; `git archive --format=tar 87779a00f25bd1855ede479e490123843e5f056e corpus/fixtures | tar -xf - -C "$scratch/base"`; same for HEAD into `$scratch/after`; both `archive_exit=0`. Driver (run with `JCAL5_SCRATCH`, `JCAL5_BASE_SHA`, `JCAL5_HEAD_SHA`, `PYTHONDONTWRITEBYTECODE=1 python3 -I`): per census root, `names = sorted(dirs)`, `order = random.Random(9301).shuffle(list(names))` (re-derived and asserted identical), then one checker subprocess per dir in that order, building `{exit, stdout_sha256, violation_count}` rows; then delta + cross-checks; artifacts written to `followup/`. Exact driver command as run:

```sh
JCAL5_SCRATCH="$scratch" JCAL5_BASE_SHA="$BASE_SHA" JCAL5_HEAD_SHA="$HEAD_SHA" PYTHONDONTWRITEBYTECODE=1 python3 -I - <<'PY'
import hashlib, json, os, pathlib, random, subprocess, sys, time

SEED = 9301
PIN = "ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421"
REPO = pathlib.Path.cwd()
SCRATCH = pathlib.Path(os.environ["JCAL5_SCRATCH"])
FUP = REPO / ".ufo/waves/round-93/followup"
FUP.mkdir(parents=True, exist_ok=True)

def seeded_order(names):
    order = list(names); random.Random(SEED).shuffle(order)
    replay = list(names); random.Random(SEED).shuffle(replay)
    assert order == replay, "seeded order not deterministic"
    return order

def census(root):
    fixtures = root / "corpus/fixtures"
    names = sorted(p.name for p in fixtures.iterdir() if p.is_dir())
    order = seeded_order(names)
    rows = {}; exit_counts = {}; stderr_nonempty = []; unexpected = []
    t0 = time.time()
    for name in order:
        rel = f"corpus/fixtures/{name}"
        p = subprocess.run([sys.executable, "-I", "corpus/fixtures/check_bible.py", rel],
                           cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        exit_counts[p.returncode] = exit_counts.get(p.returncode, 0) + 1
        if p.stderr:
            stderr_nonempty.append(rel)
        if p.returncode not in (0, 1):
            unexpected.append((rel, p.returncode))
        rows[rel] = {
            "exit": p.returncode,
            "stdout_sha256": hashlib.sha256(p.stdout).hexdigest(),
            "violation_count": sum(line.startswith(b"VIOLATION:") for line in p.stdout.splitlines()),
        }
    meta = {
        "root": str(root), "dirs": len(names),
        "order_first": order[0], "order_last": order[-1],
        "order_sorted": order == sorted(order), "order_reverse_sorted": order == sorted(order, reverse=True),
        "seed": SEED, "elapsed_s": round(time.time() - t0, 1),
        "exit_counts": {str(k): v for k, v in sorted(exit_counts.items())},
        "violation_lines": sum(r["violation_count"] for r in rows.values()),
        "stderr_nonempty": stderr_nonempty, "unexpected_exits": unexpected,
        "checker_sha256": hashlib.sha256((fixtures / "check_bible.py").read_bytes()).hexdigest(),
    }
    return rows, meta

base_rows, base_meta = census(SCRATCH / "base")
after_rows, after_meta = census(SCRATCH / "after")
print("BASE", json.dumps(base_meta, sort_keys=True))
print("AFTER", json.dumps(after_meta, sort_keys=True))

changed = sorted(k for k in base_rows if k in after_rows and base_rows[k] != after_rows[k])
new = sorted(set(after_rows) - set(base_rows))
removed = sorted(set(base_rows) - set(after_rows))
flips = sorted(k for k in base_rows if k in after_rows and base_rows[k]["exit"] != after_rows[k]["exit"])
print(f"delta base_rows={len(base_rows)} after_rows={len(after_rows)} common={len(set(base_rows) & set(after_rows))}")
print(f"delta changed={len(changed)} {changed}")
print(f"delta new={len(new)} {new}")
print(f"delta removed={len(removed)} {removed}")
print(f"delta exit_flips={len(flips)} {flips}")
for k in new:
    print(f"new_tuple {k}: {json.dumps(after_rows[k], sort_keys=True)}")

b1 = json.loads((REPO / ".ufo/waves/round-93/patches/B1-tuples.json").read_bytes())
b1_mismatch = sorted(k for k in set(base_rows) & set(b1) if base_rows[k] != b1[k])
print(f"crosscheck regenerated_base_vs_B1_receipt rows={len(b1)} key_mismatch={sorted(set(base_rows) ^ set(b1))} tuple_mismatches={len(b1_mismatch)}")

j1 = json.loads((FUP / "JCAL1-tuples.json").read_bytes())
j1_mismatch = sorted(k for k in set(after_rows) & set(j1) if after_rows[k] != j1[k])
print(f"crosscheck after_vs_JCAL1_receipt rows={len(j1)} key_mismatch={sorted(set(after_rows) ^ set(j1))} tuple_mismatches={len(j1_mismatch)}")

h4 = json.loads((FUP / "H4-census.json").read_bytes())
delivered = h4["delivered_rows"]
h4_mismatch = sorted(k for k in set(after_rows) & set(delivered) if after_rows[k] != delivered[k])
print(f"crosscheck after_vs_H4_delivered_rows rows={len(delivered)} key_mismatch={sorted(set(after_rows) ^ set(delivered))} tuple_mismatches={len(h4_mismatch)}")
# ... plus full-receipt assembly (JCAL5-tuples.json: method + both censuses + both row sets)
# and JCAL5-delta.json assembly; both written into FUP; hashes printed.
PY
```

Observed output (full-receipt and delta assembly lines abbreviated to the recorded hashes at the end):

```text
base_archive_exit=0
after_archive_exit=0 scratch=/tmp/lore-r93-JCAL5.M5Ss1D
BASE {"checker_sha256": "ff9fd2aa...1421", "dirs": 166, "elapsed_s": 4.1, "exit_counts": {"0": 32, "1": 134}, "order_first": "r27-both-ambiguous", "order_last": "r43-jorin-vela-sighting", "order_reverse_sorted": false, "order_sorted": false, "seed": 9301, "stderr_nonempty": [], "unexpected_exits": [], "violation_lines": 421}
AFTER {"checker_sha256": "ff9fd2aa...1421", "dirs": 167, "elapsed_s": 4.1, "exit_counts": {"0": 33, "1": 134}, "order_first": "r27-target-only", "order_last": "r43-jorin-vela-sighting", "order_reverse_sorted": false, "order_sorted": false, "seed": 9301, "stderr_nonempty": [], "unexpected_exits": [], "violation_lines": 421}
base_census_clean=True
after_census_clean=True
delta base_rows=166 after_rows=167 common=166
delta changed=0 []
delta new=1 ['corpus/fixtures/r93-m2-kojiki-cluster']
delta removed=0 []
delta exit_flips=0 []
delta base_violation_lines=421 after_violation_lines=421
new_tuple corpus/fixtures/r93-m2-kojiki-cluster: {"exit": 0, "stdout_sha256": "afe570fcebf45fe3913b8b87c65a2e0408e99e9c69854757a2498d5be420c07e", "violation_count": 0}
crosscheck regenerated_base_vs_B1_receipt rows=166 key_mismatch=[] tuple_mismatches=0 []
crosscheck after_vs_JCAL1_receipt rows=167 key_mismatch=[] tuple_mismatches=0 []
crosscheck after_vs_H4_delivered_rows rows=167 key_mismatch=[] tuple_mismatches=167 [all 167 paths listed]
written JCAL5-tuples.json bytes=63988 sha256=ad6b6e6b2978dd3cbe9f4330507c343648043682348fb760c642826782a8abca
written JCAL5-delta.json bytes=2759 sha256=005a34b04a693106e99ec9ae24f73bad11c191d4dec60b5930b768f4132a8ee5
JCAL5_DONE
driver_exit=0
scratch_cleaned=true
```

(`checker_sha256` values are the full `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` in the raw output; elided here once for width. The archived full outputs are the driver's own prints above; nothing was truncated that carries a verdict.)

**H4 mismatch resolution** — first probe showed 167/167 wholesale mismatches. Row-level diff — exact command:

```sh
python3 - <<'PY'
import json
h4 = json.load(open('H4-census.json')); mine = json.load(open('JCAL5-tuples.json'))
k = 'corpus/fixtures/ally-one-way'
print('H4_row:', json.dumps(h4['delivered_rows'][k], sort_keys=True))
print('MY_row:', json.dumps(mine['after_rows'][k], sort_keys=True))
PY
```

Observed output:

```text
H4_row: {"exit": 1, "stderr_len": 0, "stdout_sha256": "568425ed6a574bf54e2e0645f24f5b4e9ba5770a8d3a1f98955badd67b20a141", "violation_count": 1}
MY_row: {"exit": 1, "stdout_sha256": "568425ed6a574bf54e2e0645f24f5b4e9ba5770a8d3a1f98955badd67b20a141", "violation_count": 1}
```

Shared-field-only re-check — exact command:

```sh
python3 -I - <<'PY'
import json, pathlib
fup = pathlib.Path('.ufo/waves/round-93/followup')
mine = json.loads((fup/'JCAL5-tuples.json').read_bytes())
h4 = json.loads((fup/'H4-census.json').read_bytes())
shared_fields = ('exit', 'stdout_sha256', 'violation_count')
mismatch = sorted(k for k, row in mine['after_rows'].items()
                  if any(row.get(f) != h4['delivered_rows'][k].get(f) for f in shared_fields))
extra_keys = sorted(set(next(iter(h4['delivered_rows'].values()))) - set(next(iter(mine['after_rows'].values()))))
print(f"H4_shared_field_tuple_mismatches={len(mismatch)} {mismatch}")
print(f"H4_extra_fields={extra_keys} (schema difference only)")
PY
```

Observed output:

```text
H4_shared_field_tuple_mismatches=0 []
H4_extra_fields=['stderr_len'] (schema difference only)
```

**Artifact validation + tree/scratch check** — exact commands:

```sh
python3 -I -m json.tool .ufo/waves/round-93/followup/JCAL5-delta.json >/dev/null && echo "JCAL5-delta.json valid=PASS"
python3 -I -m json.tool .ufo/waves/round-93/followup/JCAL5-tuples.json >/dev/null && echo "JCAL5-tuples.json valid=PASS"
sha256sum .ufo/waves/round-93/followup/JCAL5-delta.json .ufo/waves/round-93/followup/JCAL5-tuples.json
git status --porcelain --untracked-files=all | head; git diff --quiet HEAD --; echo "tracked_diff_exit=$?"; ls /tmp | grep -c lore-r93-JCAL5 || echo "scratch_roots=0"
```

Observed output:

```text
JCAL5-delta.json valid=PASS
JCAL5-tuples.json valid=PASS
005a34b04a693106e99ec9ae24f73bad11c191d4dec60b5930b768f4132a8ee5  .ufo/waves/round-93/followup/JCAL5-delta.json
ad6b6e6b2978dd3cbe9f4330507c343648043682348fb760c642826782a8abca  .ufo/waves/round-93/followup/JCAL5-tuples.json
?? .ufo/waves/round-93/followup/...   (peer + my untracked wave artifacts only)
tracked_diff_exit=0
0
scratch_roots=0
```

## Findings & named debt

- **Claim confirmed under a third method**: 167 dirs (0 changed + 1 new, 0 removed, 0 exit flips). The regenerated 166-row baseline (`git archive 87779a0`, shuffled order) reproduces the stored B1 receipt tuple-for-tuple (0 mismatches), and the regenerated 167-row after-census (`git archive 65838f8`) matches JCAL1's receipt tuple-for-tuple. The only delta is `corpus/fixtures/r93-m2-kojiki-cluster` — exit 0, 0 violations, stdout sha `afe570fc…c07e`.
- **Method robustness: improved.** The census result is now invariant across traversal order (sorted B1/JCAL1/H4, reverse B2, seed-9301 shuffled here) and across extraction (live tree vs `git archive`), with all five receipt sets agreeing on shared fields (B1=B2 byte-identical; JCAL1=mine exactly; H4=mine on shared fields, extra `stderr_len` field). The stored baseline receipts are also proven faithful (regenerated base == B1). No method choice affects any verdict-bearing number: 166→167, 0 changed, 421 = 421 violation lines, no stderr, no exits outside 0/1.
- Per-axis verdicts (evidence from the committed tree at 65838f8 only; probes in `/tmp` archives of it):
  - **census completeness: improved** — coverage 166 → 167 with the third sourced-mythology cluster fixture inventoried and passing; no gaps.
  - **preexisting-fixture behavior: unchanged** (the desired no-regression property, not a trade) — 0 changed tuples, 0 exit flips, common violation lines 421 = 421; exit mix moved only by the new passing dir ({0: 32→33, 1: 134}).
  - **method robustness: improved** — see above.
  - **checker pin integrity: unchanged** — sha `ff9fd2aa…1421` at both archive roots and the live tree; matches the pin inside `corpus/tools/boundary_doc_check.py:389`.
  - **Overall r93 census axis: improved**, no trade observed in this seat's scope.
- Named debt (carried/observed, none blocking):
  1. All censuses (including mine) prove behavior-level identity under the unchanged checker, not byte-level identity of pre-existing fixture file contents.
  2. AST-anchor validation in `corpus/tools/boundary_doc_check.py` remains named r94 debt (per its README and JCAL2) — untouched here.
  3. Minor: peer census receipts use divergent row schemas (H4 adds `stderr_len`); wholesale receipt diffs across seats will false-positive until everyone diffs on the shared `{exit, stdout_sha256, violation_count}` fields. My delta JSON records this.
- Verdict recommendation for the wave's census judge: **improved** on C2 coverage, zero calibration regression on C3, and the census claim is now method-robust.

## Handoff

- `.ufo/waves/round-93/followup/JCAL5.md` — this report.
- `.ufo/waves/round-93/followup/JCAL5-delta.json` — machine-readable delta (sha256 `005a34b0…8ee5`, JSON-valid): method, both census metas, delta rows, cross-checks, per-axis verdict recommendation.
- `.ufo/waves/round-93/followup/JCAL5-tuples.json` — full regenerated 166-row baseline + 167-row after-census receipts with method metadata (63,988 bytes, sha256 `ad6b6e6b…abca`) for later seats to diff without re-running.
- Tracked files unchanged (`git diff --quiet HEAD` exit 0); only untracked followup/ wave artifacts present. `/tmp` scratch removed (`scratch_roots=0`). No commit, no push.
- Cross-seat census agreement for the judge: B1 = B2 (byte-identical, 166 rows @ 87779a0) ; JCAL1 = JCAL5 = H4-on-shared-fields (167 rows @ 65838f8) ; JCAL5's regenerated baseline == B1 — the claim "167 dirs (0 changed + 1 new)" holds under every method tried.
