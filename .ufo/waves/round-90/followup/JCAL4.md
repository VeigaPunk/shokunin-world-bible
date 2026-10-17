# JCAL4 — Calibration judge #4 (wording audit), round-90 follow-up

Seat scope: audit the restored definite strings on the delivered tree at `ca7f9ef` against the E1 wording panel — over-claim sweep, qualifier presence on all disclosure lines, voice consistency, conformance to `.ufo/waves/round-90/patches/E1-r90-wording.md` — plus the r88-I1 freeze-then-verify (delivered checker must hash-match X2+X3 composed on `e97613c`).

## Work performed

- Delivered tree under audit: `git rev-parse HEAD` = `ca7f9ef1646cf3fcbe58747785a8cb2e9075ae13`; no tracked diff at audit start. The 2×60 s wait-checks ran while the tree stayed at `ca7f9ef`; sibling follow-up seats wrote only untracked files (`H2-delta.json`, `H4-*.json`, `JCAL5-delta.json`, `corpus/tools/__pycache__/`), none of which alters the committed artifact.
- Wait-check receipt (exact command): `for i in 0 1 2; do printf '%s check=%d head=%s status=[%s]\n' "$(date --iso-8601=seconds)" "$i" "$(git rev-parse HEAD)" "$(git status --porcelain | tr '\n' ';')"; [ "$i" -lt 2 ] && sleep 60; done`
  Observed: `2026-10-17T06:56:21-03:00 check=0 head=ca7f9ef…`; `06:57:21 check=1 head=ca7f9ef…`; `06:58:21 check=2 head=ca7f9ef…`.
- **Freeze-then-verify (r88-I1).** Exact commands (cwd `lore-shokunin/`):
  ```sh
  mkdir -p /tmp/jcal4/apply/corpus/fixtures
  git show e97613c:corpus/fixtures/check_bible.py > /tmp/jcal4/apply/corpus/fixtures/check_bible.py
  cd /tmp/jcal4/apply
  patch -p1 --no-backup-if-mismatch < …/.ufo/waves/round-90/patches/X2-c1-nullonly.patch
  patch -p1 --no-backup-if-mismatch < …/.ufo/waves/round-90/patches/X3-c1-tickonly.patch
  sha256sum corpus/fixtures/check_bible.py
  sha256sum /home/vgpnk/Projects/shokunin/lore-shokunin/corpus/fixtures/check_bible.py
  ```
  Observed: `patching file corpus/fixtures/check_bible.py` ×2 (`X3` hunk succeeded at 321, offset 2);
  composed `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421` = delivered `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`. **MATCH — no blocking finding.** The delivered checker is exactly X2+X3 composed on `e97613c`, nothing more.
- Code inspected on the delivered tree: `corpus/fixtures/check_bible.py` lines 168–175 (`holder_identity_detail` + X2 `None` gate), 208–210 (disclosure line), 322–345 (tick / chain / first-record branches). Line map: tick definite 326, qualified chain 335, definite chain 337, qualified first-record 341, definite first-record 343, disclosure 210.
- Six scratch probes (controls only, all under `/tmp`; scratch area had `308` free tmpfs inodes at start, `df -i /tmp`):
  ```sh
  mkdir -p /tmp/jcal4/probes && python3 - <<'PY'
  import json, shutil, subprocess, sys
  from pathlib import Path
  repo = Path('/home/vgpnk/Projects/shokunin/lore-shokunin'); check = repo/'corpus/fixtures/check_bible.py'
  scratch = Path('/tmp/jcal4/probes')
  def copy(s, d):
      dst = scratch/d
      if dst.exists(): shutil.rmtree(dst)
      shutil.copytree(repo/'corpus/fixtures'/s, dst); return dst
  def edit(d, n, fn):
      p = d/n; rows = json.loads(p.read_text()); fn(rows); p.write_text(json.dumps(rows, indent=2)+'\n')
  def run(d, label):
      r = subprocess.run([sys.executable, str(check), str(d)], capture_output=True, text=True)
      print(f'===== {label} ====='); print(r.stdout, end=''); print(f'exit={r.returncode} stderr_empty={not r.stderr}')
  a = copy('r89-fn2-control','A'); edit(a,'entities.json', lambda r: r[3]['provenance'][1].update(tick=0, from_holder=None))
  run(a,'A null-from + tick inversion, previous holder resolved')
  b = copy('r89-fn2-unresolved-chain-break','B'); edit(b,'entities.json', lambda r: r[4]['provenance'][1].update(tick=0))
  run(b,'B unresolved non-null chain + tick inversion')
  c = copy('r89-fn2-unresolved-chain-break','C'); edit(c,'entities.json', lambda r: r[4]['provenance'][0].update(from_holder='f3-dup'))
  run(c,'C first-record unresolved non-null from_holder')
  d = copy('r89-fn2-control','D'); edit(d,'entities.json', lambda r: r[3]['provenance'][0].update(from_holder='mira'))
  run(d,'D first-record resolved non-null from_holder')
  e = copy('r89-fn2-control','E'); edit(e,'entities.json', lambda r: r[3]['provenance'][1].update(tick=0, from_holder=None)); edit(e,'sources.json', lambda r: r.append(dict(r[0])))
  run(e,'E ambiguous-source prefix on definite null-from + tick')
  g = copy('r89-fn2-unresolved-chain-break','G'); edit(g,'entities.json', lambda r: r[4]['provenance'][1].update(from_holder=None))
  run(g,'G null-from with unresolved previous holder')
  PY
  ```
  Before-outputs were produced with the same probe directories and the pinned baseline: `git show e97613c:corpus/fixtures/check_bible.py > /tmp/jcal4/base-check.py; python3 /tmp/jcal4/base-check.py /tmp/jcal4/probes/<X>`.
- Durable-fixture replays (delivered checker, exact command): `for d in r90-c1-rawpresent-from r90-c1-rawpresent-source r90-c1-rawpresent-to r90-c1-three-causes r89-fn2-unresolved-chain-break r89-fn2-control; do echo "== $d"; python3 corpus/fixtures/check_bible.py corpus/fixtures/$d; echo "exit=$?"; done`. All four r90-c1 fixtures reproduce their README-declared after-state verbatim (5/4/5/4 violations, exit 1), and both r89 controls reproduce the claimed shapes.
- Corpus-wide wording scan (exact command): `for d in corpus/fixtures/*/; do [ -f "$d/entities.json" ] || continue; out=$(python3 corpus/fixtures/check_bible.py "$d" 2>/dev/null); if printf '%s' "$out" | grep -q "provenance chain break\|provenance tick"; then printf '== %s\n' "${d%/}"; printf '%s\n' "$out" | grep "provenance chain break\|provenance tick"; fi; done`
  Fixtures emitting the provenance-chain/tick families: `item-chain-broken`, `r87-chain-unique-broken`, `r87-probe-record-and-chain`, `r87-probe-source-prefix`, `r89-fn2-control`, `r89-fn2-unresolved-chain-break`. **No delivered fixture emits `got None`**; no delivered fixture emits a tick inversion with an unresolved compared holder. The four new `r90-c1-*` fixtures exercise only the raw-present/stop-cause disclosure path.
- Voice/history check (exact command): `for rev in 2ea9ef1 51b286b 1b09f3f e97613c ca7f9ef; do echo "== $rev"; git show $rev:corpus/fixtures/check_bible.py | grep -n "provenance chain break\|provenance tick\|first record must have\|not sourced-canon\|holder identity is not uniquely resolvable"; done`. r88 (`2ea9ef1`/`51b286b`) lines 306/308/310 are the definite tick/chain/first-record format strings; r89 (`1b09f3f`/`e97613c`) replaces them with the identity-note tick form (328–333) and the qualified branches (342/348); `ca7f9ef` restores the r88 format strings at 326/337/343 (line 337 byte-identical to r88 line 308; 343 to 310; 326 to 306 modulo the extracted `prefix` variable) and drops the `holder identity is not uniquely resolvable:` note entirely (no match in the delivered file).
- Over-claim sweep (exact command): `grep -n "canon\|truth\|real\|story\|proof\|prove" corpus/fixtures/check_bible.py` → matches only `provenance*` identifiers and line 426 `print(f'{len(violations)} violation(s); no canon changed')`. `grep -n "must be\|must have"` → 326 (tick ordering), 341/343 (first-record null requirement), 385 (timeline tick nonnegative) — all input-constraint statements. No unhedged line asserts beyond the input.
- Corpus inventory corroboration (exact commands): `ls -d corpus/fixtures/*/ | wc -l` = `164`; `git diff --name-status e97613c ca7f9ef -- corpus/fixtures` = 26 `A` + 7 `M` — the additions are the two claim→excerpt maps and the four new `r90-c1-*` fixture dirs (6 files each), and the modifications are the checker plus 6 markdown excerpt files (C2 mode labels); **no pre-existing fixture JSON was modified**, so the census exit tuples of the prior 160 dirs are preserved by construction.
- Scratch cleanup: `/tmp/jcal4` removed after this report was written (probes are scratch, not deliverables; the report carries the reconstruction commands). No commit, no push, no tracked writes outside the two follow-up files. Sibling follow-up seats later modified the tracked `followup/Q1-r90-debt.json` and added further untracked artifacts; `HEAD` remained `ca7f9ef` and the audited checker was untouched by those writes.

## Before → after measurements

Checker sha256 (delivered, both at audit start and after the wait-checks): `ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421`.

**Probe A — null-from + tick inversion, previous holder resolved** (`entities[3].provenance[1]`):
- Before (`e97613c`, exact observed):
  ```text
  VIOLATION: entities[3].provenance[1].tick: input-structural finding, not sourced-canon; holder identity is not uniquely resolvable: from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index); provenance tick 0 must be greater than previous tick 0
  VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup'; got None; from_holder None is not uniquely resolvable (0 raw entity rows carry this id, but only 0 is in the resolved index)
  ```
- After (delivered):
  ```text
  VIOLATION: entities[3].provenance[1].tick: provenance tick 0 must be greater than previous tick 0
  VIOLATION: entities[3].provenance[1]: provenance chain break; expected from_holder 'f3-dup', got None
  ```
- Verdict: the two definite strings match E1's templates exactly; the vacuous `None`-as-holder identity predicate is gone. Improved.

**Probe B — unresolved non-null chain + tick inversion** (`entities[4].provenance[1]`):
- Before: tick line carried `holder identity is not uniquely resolvable: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows …); provenance tick 0 must be greater than previous tick 0`; chain line qualified.
- After:
  ```text
  VIOLATION: entities[4].provenance[1].tick: provenance tick 0 must be greater than previous tick 0
  VIOLATION: entities[4].provenance[1]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got 'mira'
  ```
- Verdict: X3's integer-only tick wording confirmed; C9's ruling case (tick definite while the compared holder stays unresolved) holds on the delivered tree. Improved.

**Probe D — first-record resolved non-null `from_holder`**: after = `entities[3].provenance[0]: provenance chain break; first record must have from_holder null` (plus a resolved definite chain line). Matches E1's guard template. Improved.

**Probe E — ambiguous source + definite null-from/tick**: after keeps the source prefix on both definite lines:
```text
VIOLATION: entities[3].provenance[1].tick: input-structural finding, not sourced-canon; provenance tick 0 must be greater than previous tick 0
VIOLATION: entities[3].provenance[1]: input-structural finding, not sourced-canon; provenance chain break; expected from_holder 'f3-dup', got None
```
Verdict: E1's "preserve the prefix only for an independently ambiguous source citation" holds. Improved.

**Probe C — first-record unresolved non-null `from_holder`** (deviation):
- Before and after are the same qualified line:
  ```text
  VIOLATION: entities[4].provenance[0]: input-structural finding, not sourced-canon; possible provenance chain break, not a definite identity mismatch: from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); first record must have from_holder null
  ```
- E1's guard template (`{record_label}: {"input-structural finding, not sourced-canon; " if …}provenance chain break; first record must have from_holder null`) is definite for this case ("a non-null value violates it even if that holder ID is unresolved"). Delivered retains the r89 qualified frame → **unchanged, non-conformant**.

**Probe G — null-from with unresolved previous holder** (deviation):
- Before: `… possible provenance chain break, … : expected from_holder 'f3-dup' is not uniquely resolvable (…); got None; from_holder None is not uniquely resolvable (0 raw … but only 0 …)`.
- After: `… possible provenance chain break, not a definite identity mismatch: expected from_holder 'f3-dup' is not uniquely resolvable (2 raw entity rows carry this id, but only 1 is in the resolved index); got None`.
- E1's null-chain section: "The definite break holds even if the preceding non-null holder ID is unresolved". Delivered removed the vacuous `None` detail (improved) but kept the qualifier instead of the definite string → **non-conformant** (over-hedge, not over-claim).

## Findings & named debt

**Freeze-then-verify: PASS** — delivered checker hash-matches X2+X3 composed on `e97613c` (`ff9fd2aa…`). No blocking finding. The composition is exactly the declared frozen pair; the sub-case gaps below are inherited from r89 and sit outside both patches' scope, not integration drift.

Per-axis verdicts (wording-audit axes, delivered evidence only):
- **Over-claim control — improved.** The before-state over-assertions are removed: tick lines no longer assert holder-identity uncertainty on a numeric predicate; the null chain no longer states `from_holder None is not uniquely resolvable (0 raw/0 indexed)`. Corpus grep shows no unhedged line asserting canon/story truth; the definite family asserts only explicit record-field inconsistencies, matching E1's risk notes. No new over-claim found.
- **Qualifier presence on disclosure lines — improved (bounded).** The disclosure line (`… remain unassessed (input-structural finding, not sourced-canon); first stop: …`, line 210) is hedged in every fixture and probe run; the `input-structural finding, not sourced-canon` prefix now appears on definite lines exactly when source ambiguity independently requires it (probe E). Residual bound: the qualifier is still over-present on two non-identity predicates (F1/F2) — over-hedging, never a missing hedge.
- **Voice consistency — improved (one residual).** The definite tick/chain/first-record strings are byte-identical restorations of the r88 format strings (`2ea9ef1`/`51b286b` lines 306/308/310 → delivered 326/337/343); the qualified family is unchanged from r89; the disclosure line is unchanged since r88. Residual: line 341's frame is internally inconsistent (F2) — it hedges with "possible … not a definite identity mismatch" while embedding the definite requirement "first record must have from_holder null", and labels a positional requirement as an identity mismatch.
- **Conformance to E1-r90-wording.md — improved but incomplete.** Verified exact-conforming paths: null-from with resolved previous holder (A/E), tick inversion including null transition and unresolved compared holder (A/B), first-record resolved non-null (D); boundary qualified chain and prefix gating per E1 (B/E). Deviating paths: F1 and F2 below. Because two E1 templates remain unimplemented for their unresolved sub-cases, this seat does not report full conformance for the wording lane.
- **Durable-fixture evidence for the restored strings — gap (F3).** The null-chain definite string (`got None`) appears in zero delivered fixture outputs, and no fixture pins the tick-definite-under-unresolved-holder shape. The canonical FN-2 pair pins only the resolved-definite chain and the qualified unresolved chain. Both repaired shapes are evidenced here by scratch probes plus the r89 JCAL2 receipt; they are not regression-visible in the delivered census.

Named debt (for phase-2 ruling / r91):
- **JCAL4-F1 — null-from chain with unresolved previous holder stays qualified.** Delivered line 335 branch triggers on `expected_detail` alone; E1's null-chain rationale requires the definite form "even if the preceding non-null holder ID is unresolved" (`patches/E1-r90-wording.md:17`). Probe G receipt above. Safe direction (under-claim), but blocks E1 conformance and leaves a "null chains ⇒ definite" claim overstated.
- **JCAL4-F2 — first-record guard with unresolved non-null id stays qualified and voice-inconsistent.** Delivered line 341; E1's guard template is definite and explicitly classifies the case as non-identity (`patches/E1-r90-wording.md:35-45`). Probe C receipt above.
- **JCAL4-F3 — restored definite strings not pinned by durable fixtures.** r91 candidate: add one durable null-from fixture (expect `got None` definite line) and one tick-inversion/unresolved-holder fixture (expect clean tick line), so the X2/X3 repairs are regression-visible in the canonical census.
- **JCAL4-F4 — claim-text precision.** The C1 summary "null chains and tick findings definite" holds for tick findings and for null-from chains with a resolved previous holder; the unresolved-previous sub-case (probe G) is a counterexample. The emitted strings never over-claim; the claim sentence needs the sub-case qualifier.
- Items the crown already bounds / not mine to re-rule: C9's spec-alignment debt (`C9.md:69`), C9's r91 falsification path for the tick reading, and Q1's open Q89-001/Q89-002 ledger rows — all still consistent with these receipts.

## Handoff

- `.ufo/waves/round-90/followup/JCAL4.md` — this report (sections in required order).
- `.ufo/waves/round-90/followup/JCAL4-probes.json` — machine-readable receipt: freeze hashes, probe before/after lines, fixture replay counts, per-axis verdicts, named debt.
- Parent integrator: freeze check clean; wording lane = improved but bounded by JCAL4-F1/F2, with F3/F4 as carry-forward debt. No blocking finding. Scratch `/tmp/jcal4` removed; no tracked write outside the two follow-up files; no commit or push.
