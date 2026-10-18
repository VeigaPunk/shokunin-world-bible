## Work performed

- **Axes:** boundary-document fidelity; checker freeze integrity; scope integrity.
- Read the round-91 wave spec, the tracked boundary-document path, and the r90 CB1 audit/proposal. Compared the r90-delivered revision (`ca7f9ef`) with the r90-closure baseline (`a7c6a17`), then checked the post-poll worktree and r91 patch artifacts.
- Polled the wave artifacts at 60-second intervals against the original 20-minute cutoff. The first background shell hit its 600-second runner limit; I resumed against the original cutoff in a second shell. The timing irregularity and observed cutoff inventory are recorded below.
- No tracked file was changed; no commit or push; no other repository accessed. No scratch file was created.

## Before → after measurements

### Checker freeze

Exact command:

```sh
printf 'HEAD='; git rev-parse HEAD; printf 'r90-delivered checker: '; git show ca7f9ef:corpus/fixtures/check_bible.py | sha256sum; printf 'current HEAD checker: '; git show HEAD:corpus/fixtures/check_bible.py | sha256sum; printf 'worktree checker: '; sha256sum corpus/fixtures/check_bible.py; git diff --quiet ca7f9ef..HEAD -- corpus/fixtures/check_bible.py; printf 'r90_to_HEAD_checker_diff_exit=%s\n' "$?"; git diff --quiet -- corpus/fixtures/check_bible.py; printf 'worktree_checker_diff_exit=%s\n' "$?"
```

Observed:

```text
HEAD=a7c6a1773d5994246a76e4eff30d645f161920e0
r90-delivered checker: ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  -
current HEAD checker: ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  -
worktree checker: ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421  corpus/fixtures/check_bible.py
r90_to_HEAD_checker_diff_exit=0
worktree_checker_diff_exit=0
```

A patch-header search for `check_bible.py` under `.ufo/waves/round-91/patches` returned no matches. The tracked worktree diff was empty at the post-poll check.

### Boundary-document lineage

Exact command:

```sh
printf 'r90-delivered doc: '; git show ca7f9ef:corpus/knowledge/holder-assessment-boundary.md | sha256sum; printf 'r90-closure tracked doc: '; git show HEAD:corpus/knowledge/holder-assessment-boundary.md | sha256sum; printf 'r90 proposal: '; sha256sum .ufo/waves/round-90/followup/CB1-boundary-refresh.md; if cmp -s corpus/knowledge/holder-assessment-boundary.md .ufo/waves/round-90/followup/CB1-boundary-refresh.md; then printf 'tracked_doc_equals_proposal=yes\n'; else printf 'tracked_doc_equals_proposal=no\n'; fi; git diff --stat ca7f9ef..HEAD -- corpus/knowledge/holder-assessment-boundary.md
```

Observed:

```text
r90-delivered doc: a4b1b331ba96ff5d57200517cfe1d9e4c8f6030b4fd9ec2e46f38e7fbb4b3fd2  -
r90-closure tracked doc: 0d42c9881e1a13351ef865f6940ca6e15a717c1123056fc361ec42e346c3a60c  -
r90 proposal: 0d42c9881e1a13351ef865f6940ca6e15a717c1123056fc361ec42e346c3a60c  .ufo/waves/round-90/followup/CB1-boundary-refresh.md
tracked_doc_equals_proposal=yes
 corpus/knowledge/holder-assessment-boundary.md | 896 ++++++++-----------------
 1 file changed, 291 insertions(+), 605 deletions(-)
```

Exact revision-header check:

```sh
for rev in ca7f9ef HEAD; do printf '%s boundary document: ' "$rev"; git show "$rev":corpus/knowledge/holder-assessment-boundary.md | python3 -c 'import sys; s=sys.stdin.read(); lines=s.splitlines(); print("lines=" + str(len(lines)) + " title=" + repr(lines[0]) + " proposal_marker=" + str(any("Status: proposal only" in line for line in lines))); print("\n".join(lines[:4]))'; done
```

Observed:

```text
ca7f9ef boundary document: lines=630 title='# Holder-assessment boundary: reading provenance ambiguity disclosures' proposal_marker=False
# Holder-assessment boundary: reading provenance ambiguity disclosures

<!-- Refreshed at round-89 closure from seat CB1's verified proposal
     (.ufo/waves/round-89/followup/CB1-boundary-refresh.md) with seat E1's
HEAD boundary document: lines=316 title='# CB1 — Boundary-doc refresh proposal (for the round-90 closure)' proposal_marker=True
# CB1 — Boundary-doc refresh proposal (for the round-90 closure)

**Status: proposal only.** No `corpus/` file was changed by this seat. Ready to apply at the
r90 closure by the integrator, followed by the r88-I1 re-verification (replay the pasted blocks)
```

### r90 remap anchors against the unchanged checker

Exact command (read-only inline audit):

```sh
python3 - <<'PY'
from pathlib import Path
import hashlib, re
checker = Path('corpus/fixtures/check_bible.py').read_bytes()
source_lines = checker.decode().splitlines()
doc = Path('corpus/knowledge/holder-assessment-boundary.md').read_text().splitlines()
start = doc.index('## Consolidated anchor remap (r89 doc refs → delivered `ff9fd2aa`)')
anchors = []
rows = 0
for line in doc[start + 1:]:
    if line.startswith('## '):
        break
    if not line.startswith('|') or line.startswith('|---') or 'delivered ref' in line:
        continue
    cells = line.split('|')
    if len(cells) < 4:
        continue
    target = cells[2].strip()
    if target == '**removed**':
        continue
    rows += 1
    anchors.extend(int(n) for pair in re.findall(r':(\d+)(?:-(\d+))?', target) for n in pair if n)
checks = [
    ('null guard', 169, 170, 'if holder_id is None:'),
    ('identity detail', 171, 175, 'not uniquely resolvable'),
    ('comparison gate', 322, 322, 'if first_stop is None:'),
    ('integer tick branch', 323, 326, 'if tick <= previous_tick:'),
    ('chain comparison', 327, 337, 'provenance chain break; expected from_holder'),
    ('first-record comparison', 338, 343, 'first record must have from_holder null'),
    ('CLI/exit behavior', 418, 428, 'CLEAN: schema, citations, relations, timeline; 0 violations'),
]
print(f'checker_lines={len(source_lines)}')
print(f'checker_sha256={hashlib.sha256(checker).hexdigest()}')
print(f'remap_table_rows={rows} delivered_line_anchors={len(anchors)} max_anchor={max(anchors)} out_of_range={sum(n > len(source_lines) for n in anchors)}')
for name, first, last, needle in checks:
    excerpt = '\n'.join(source_lines[first - 1:last])
    print(f'{name} {first}-{last}: {"PASS" if needle in excerpt else "FAIL"} (needle={needle!r})')
PY
```

Observed after the round-91 artifact cutoff:

```text
checker_lines=428
checker_sha256=ff9fd2aa6811a813a20bf74d3931d299378bff7f6925576243d2413b857d1421
remap_table_rows=25 delivered_line_anchors=68 max_anchor=428 out_of_range=0
null guard 169-170: PASS (needle='if holder_id is None:')
identity detail 171-175: PASS (needle='not uniquely resolvable')
comparison gate 322-322: PASS (needle='if first_stop is None:')
integer tick branch 323-326: PASS (needle='if tick <= previous_tick:')
chain comparison 327-337: PASS (needle='provenance chain break; expected from_holder')
first-record comparison 338-343: PASS (needle='first record must have from_holder null')
CLI/exit behavior 418-428: PASS (needle='CLEAN: schema, citations, relations, timeline; 0 violations')
```

### Artifact poll and cutoff

The initial poll command was a 60-second loop with a 1200-second deadline and `trap` output. The runner killed that background process at its default 600-second cap (terminal status `timed_out`); it logged checks `00`–`09` and `POLL_TERMINAL 2026-10-17T07:26:17-03:00 exit=0`, but did not reach the deadline. I resumed with the original start time/deadline and a 900-second runner timeout. Exact continuation command:

```sh
completed=0; trap 'if [ "$completed" -eq 1 ]; then printf "POLL_TERMINAL outcome=deadline %s\n" "$(date --iso-8601=seconds)"; else printf "POLL_TERMINAL outcome=interrupted %s\n" "$(date --iso-8601=seconds)"; fi' EXIT; start=$(date -d '2026-10-17T07:16:17-03:00' +%s); deadline=$((start + 1200)); check=10; while :; do now=$(date +%s); printf '\n--- poll %02d %s elapsed=%ss ---\n' "$check" "$(date --iso-8601=seconds)" "$((now - start))"; printf 'artifacts: '; shopt -s nullglob; files=(.ufo/waves/round-91/* .ufo/waves/round-91/patches/*); if ((${#files[@]})); then printf '%s ' "${files[@]}"; else printf 'none'; fi; printf '\n'; if [ "$now" -ge "$deadline" ]; then completed=1; break; fi; check=$((check + 1)); sleep 60; done; printf '\nPOLL_DEADLINE %s elapsed=%ss\n' "$(date --iso-8601=seconds)" "$(( $(date +%s) - start ))"
```

Observed timestamped checks (local `-03:00`): `00` 07:16:17; `01` 07:17:17; `02` 07:18:17; `03` 07:19:17; `04` 07:20:17; `05` 07:21:17; `06` 07:22:17; `07` 07:23:17; `08` 07:24:17; `09` 07:25:17; runner timeout/terminal at 07:26:17; resumed `10` 07:26:40; `11` 07:27:40; `12` 07:28:40; `13` 07:29:40; `14` 07:30:40; `15` 07:31:40; `16` 07:32:40; `17` 07:33:40; `18` 07:34:40; `19` 07:35:40; `20` 07:36:40. The continuation's terminal output was:

```text
POLL_DEADLINE 2026-10-17T07:36:40-03:00 elapsed=1223s
POLL_TERMINAL outcome=deadline 2026-10-17T07:36:40-03:00
```

The one-minute sampling interval caused the final sample to be 23 seconds after the nominal 07:36:17 cutoff; the runner timeout also caused an 83-second sampling gap between checks `09` and `10`. At the cutoff the visible report files were `B1.md`, `B2.md`, `B3.md`, `D2.md`, `E1.md`, `F2.md`, `J3.md`, `M3.md`, `S1.md`, `S2.md`, `SE1.md`, `W2.md`, and `wave-spec.md`; visible patches/receipts included B1/B2 tuples, B3 before-state, D2 edges, E1 wording, F2 fixtures, M1/M2 hardening, M3 wording, S1 C9 watch, W2 proposals/skeleton, and X1 fixtures. **W1.md was absent at cutoff.**

Inode preflight and cleanup: `df -i /tmp` reported `1048576` inodes, `1042979` used, `5597` free, `100%`; a final `df -i /tmp` reported `1043007` used and `5569` free. This seat created no scratch files, so there was nothing of ours to sweep; no scratch path or archive was used.

## Findings & named debt

- **Negative checker-drift result:** no r91 checker change was found. The checker remains byte-identical to the r90-delivered `ff9fd2aa…` baseline, the patch-header search found no r91 patch targeting it, and the r90 remap's 68 target-line anchors remain in range with the key semantic anchors matching. This is a valid r91 counter-case for checker drift.
- **Named pre-existing debt — `R90-CB1-PROPOSAL-COPIED-OVER-CONTRACT`:** the assumption that the tracked boundary contract was refreshed at r90 closure is false. At `ca7f9ef` it was a 630-line contract; at `a7c6a17` the tracked path contains the 316-line “proposal only” artifact verbatim. The remap table happens to match the unchanged checker, but the tracked file is not the delivered contract, so this seat cannot certify it as delivered-true. This regression occurred at r90 closure, not in r91; no tracked-file correction was made under this seat's constraints.
- **Cutoff gap — `R91-W1-LANDING-RECORD-MISSING`:** W1 was not present at the 20-minute cutoff. I assessed the current HEAD and the artifacts then available; no later integration was assumed.

## Handoff

- Only this permitted seat artifact was written: `.ufo/waves/round-91/CB1.md`. No `patches/CB1-*` file was needed.
- No tracked changes, commits, pushes, or sibling-repository access. Audit-only; no build/test command applies.
- Parent follow-up: treat the r91 checker result as negative, but do not mark the tracked boundary document delivered-true until the r90 proposal-copy problem is resolved in an authorized integration step. 