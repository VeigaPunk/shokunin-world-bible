# V15 — preservation and fixture census (2026-10-17)

Scope: independent round-100 inherited-path preservation and fixture-directory census, after all four producers delivered artifacts and reports. Axes: inherited-byte/mode preservation, fixture-count coverage, and evidence completeness. This is not a round-wide admission verdict.

All commands ran from `/home/vgpnk/Projects/shokunin/lore-shokunin`, with `python3` for Python. Required baseline: `fe1ce466e9d7427948c0abe4ecfbf961880b72ff`; dispatch/live HEAD: `b5fe472957ab1e4e9c90f5613acc14cd24a288ae`. I did not replace the required baseline with HEAD.

## Verdict and findings

- **Census PASS:** 173 baseline fixture directories become 174 delivered directories. Only `r100-docket-review` was added; none was removed; there are no symlink fixture directories. The complete enumeration is below.
- **Inherited fixtures PASS:** every inherited path under `corpus/fixtures/` is byte/mode-identical to `fe1ce46`.
- **Strict baseline preservation FAIL:** all 76,539 inherited entries were checked, including all 18 symlinks without following their targets. There were zero read errors, 76,533 unchanged entries and six changed entries. Four changes are exactly the authorized producer paths; **`LOG.md` and `SCORECARD.md` are additional inherited changes**, outside the seat's stated allowlist.
- **Attribution:** both additional changes are committed before this wave's producer work: `LOG.md:3349` is the r100 declaration in `b5fe472`, and `SCORECARD.md:564` is the r99 closure addendum in `ae67105`. The producer worktree delta relative to dispatch HEAD is exactly the four authorized inherited paths, so producer scope passes under that different comparison. This does not erase the literal `fe1ce46` finding.
- **Delivered additions:** ten new r100 fixture files and two new r100 knowledge files are present. Together with the modified inherited blind-spot table, these are the three producer-owned knowledge deliverables; there is no claim of a separately declared third new knowledge filename.

No artifact was repaired or deleted. Parent adjudication should explicitly reconcile the baseline/allowlist discrepancy rather than silently rebase or attribute the two committed documentation changes to producers.

## Producer/artifact wait

The required bounded poll checked both nonempty artifacts and nonempty T1–T4 reports, every 20 seconds, for at most 40 attempts. Exact command:

```sh
python3 - <<'PY'
from pathlib import Path
import datetime, json, re, time
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root
seats = root / '.ufo/waves/round-100/seats'
prior = root / 'corpus/fixtures/r99-window-lapse'
required = [root / 'corpus/tools/dependency-freeze-contract.json', root / 'corpus/tools/README.md', root / 'SKILL.md', root / 'corpus/knowledge/r100-crossing-arc-synthesis.md', root / 'corpus/knowledge/r100-provenance-semantics-boundary.md', root / 'corpus/knowledge/r99-gate-blind-spot-table.md']
required += [root / 'corpus/fixtures/r100-docket-review' / item.name for item in prior.iterdir() if item.is_file()]
for attempt in range(1, 41):
    reports = sorted(p for p in seats.glob('T*.md') if re.match(r'^T[1-4](?:[-_.]|$)', p.name)) if seats.is_dir() else []
    found = {int(re.match(r'^T([1-4])', p.name).group(1)) for p in reports if p.stat().st_size > 0}
    missing = [str(p.relative_to(root)) for p in required if not p.is_file() or p.stat().st_size == 0]
    print(json.dumps({'attempt': attempt, 'observed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(), 'producer_reports': [str(p.relative_to(root)) for p in reports], 'missing_producer_ids': sorted({1, 2, 3, 4} - found), 'missing_artifacts': missing}), flush=True)
    if not missing and found == {1, 2, 3, 4}:
        print('PRODUCERS_AND_ARTIFACTS_PRESENT', flush=True)
        break
    if attempt < 40:
        time.sleep(20)
else:
    print('ABSENT: poll exhausted after 40 attempts at 20-second cadence', flush=True)
    raise SystemExit(3)
PY
```

Observed exit 0 after 480 seconds; final output, verbatim:

```text
{"attempt": 25, "observed_at": "2026-10-18T02:40:16.692157+00:00", "producer_reports": [".ufo/waves/round-100/seats/T1-chain-seven.md", ".ufo/waves/round-100/seats/T2-fixture-author.md", ".ufo/waves/round-100/seats/T3-fixture-docs.md", ".ufo/waves/round-100/seats/T4-knowledge-author.md"], "missing_producer_ids": [], "missing_artifacts": []}
PRODUCERS_AND_ARTIFACTS_PRESENT
```

Then read the producer reports. No plan was accepted as a delivered artifact. No all-reports poll or stall escape was used, and no needed background task remains.

## Exhaustive inherited-byte/mode audit and census

This audit computes the Git blob object ID from each actual inherited file's bytes and compares it with `git ls-tree fe1ce46`; it separately compares regular/executable/symlink mode. Symlink payloads are `readlink` bytes, not target contents. This covers all inherited paths, including historical `.ufo` and reports, rather than sampling only the corpus. A filename-only sensitive-path preflight found no blocked path before byte hashing.

Exact command:

```sh
python3 - <<'PY'
from pathlib import Path, PurePosixPath
from collections import Counter
import datetime, hashlib, json, os, stat, subprocess
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root
baseline = 'fe1ce46'
allowed = {'corpus/tools/dependency-freeze-contract.json', 'corpus/tools/README.md', 'SKILL.md', 'corpus/knowledge/r99-gate-blind-spot-table.md'}
new_knowledge = {'corpus/knowledge/r100-crossing-arc-synthesis.md', 'corpus/knowledge/r100-provenance-semantics-boundary.md'}
rows = subprocess.check_output(['git', 'ls-tree', '-r', '-z', baseline]).split(b'\0')
entries = []
for row in rows:
    if row:
        meta, path = row.split(b'\t', 1)
        mode, kind, oid = meta.decode().split()
        entries.append((mode, kind, oid, path.decode()))
blocked_names = {'.env', 'auth.json', 'credentials', 'credentials.json', 'id_rsa', 'id_dsa', 'id_ecdsa', 'id_ed25519', 'known_hosts'}
blocked = []
for _, _, _, name in entries:
    p = PurePosixPath(name)
    env_like = p.name.startswith('.env.') and p.name not in {'.env.example', '.env.sample', '.env.template'}
    if p.name in blocked_names or env_like or '.ssh' in p.parts:
        blocked.append(name)
assert not blocked, blocked
print('AUDIT_START_UTC', datetime.datetime.now(datetime.timezone.utc).isoformat(), flush=True)
print('BASELINE', subprocess.check_output(['git', 'rev-parse', baseline], text=True).strip(), flush=True)
print('HEAD', subprocess.check_output(['git', 'rev-parse', 'HEAD'], text=True).strip(), flush=True)
print('BASELINE_ENTRIES', len(entries), flush=True)
changes, unchanged, errors = [], 0, []
for mode, kind, oid, name in entries:
    p = root / name
    try:
        info = p.lstat()
        if stat.S_ISLNK(info.st_mode):
            current_mode, payload = '120000', os.fsencode(os.readlink(p))
        elif stat.S_ISREG(info.st_mode):
            current_mode = '100755' if info.st_mode & 0o111 else '100644'
            payload = p.read_bytes()
        else:
            changes.append({'path': name, 'status': 'TYPE-CHANGED', 'baseline_mode': mode})
            continue
        current_oid = hashlib.sha1(b'blob ' + str(len(payload)).encode() + b'\0' + payload).hexdigest()
        if current_mode == mode and current_oid == oid:
            unchanged += 1
        else:
            changes.append({'path': name, 'baseline_mode': mode, 'current_mode': current_mode, 'baseline_oid': oid, 'current_oid': current_oid, 'allowed': name in allowed})
    except FileNotFoundError:
        changes.append({'path': name, 'status': 'MISSING', 'allowed': name in allowed})
    except OSError as exc:
        errors.append({'path': name, 'error': str(exc)})
print('UNCHANGED_INHERITED_ENTRIES', unchanged)
print('CHANGED_INHERITED_ENTRIES', len(changes))
print('INHERITED_READ_ERRORS', json.dumps(errors))
for item in changes:
    print('INHERITED_CHANGE', json.dumps(item, sort_keys=True))
unexpected = [item['path'] for item in changes if item['path'] not in allowed]
print('UNEXPECTED_INHERITED_PATHS', json.dumps(unexpected))
print('BASELINE_MODE_COUNTS', json.dumps(dict(Counter(item[0] for item in entries)), sort_keys=True))
base_fixtures = sorted({name.split('/')[2] for _, _, _, name in entries if name.startswith('corpus/fixtures/') and len(name.split('/')) > 3})
fixture_root = root / 'corpus/fixtures'
current_fixtures = sorted(p.name for p in fixture_root.iterdir() if p.is_dir())
print('BASELINE_FIXTURE_DIRECTORY_COUNT', len(base_fixtures))
print('DELIVERED_FIXTURE_DIRECTORY_COUNT', len(current_fixtures))
print('ADDED_FIXTURE_DIRECTORIES', json.dumps(sorted(set(current_fixtures) - set(base_fixtures))))
print('MISSING_FIXTURE_DIRECTORIES', json.dumps(sorted(set(base_fixtures) - set(current_fixtures))))
print('FIXTURE_SYMLINK_DIRECTORIES', json.dumps(sorted(p.name for p in fixture_root.iterdir() if p.is_dir() and p.is_symlink())))
print('FIXTURE_DIRECTORY_ENUMERATION_BEGIN')
for number, name in enumerate(current_fixtures, 1):
    print(f'{number:03d} {name}')
print('FIXTURE_DIRECTORY_ENUMERATION_END')
untracked = [os.fsdecode(p) for p in subprocess.check_output(['git', 'ls-files', '--others', '--exclude-standard', '-z']).split(b'\0') if p]
wave_prefix = '.ufo/waves/round-100/seats/'
non_wave = sorted(name for name in untracked if not name.startswith(wave_prefix))
print('NON_WAVE_UNTRACKED_PATHS', json.dumps(non_wave, indent=2))
unexpected_untracked = [name for name in non_wave if not name.startswith('corpus/fixtures/r100-docket-review/') and name not in new_knowledge]
print('UNEXPECTED_NON_WAVE_UNTRACKED_PATHS', json.dumps(unexpected_untracked))
print('NEW_FIXTURE_FILE_COUNT', len([name for name in non_wave if name.startswith('corpus/fixtures/r100-docket-review/')]))
print('NEW_KNOWLEDGE_PATHS', json.dumps(sorted(name for name in non_wave if name in new_knowledge)))
print('INHERITED_FIXTURE_CHANGES', json.dumps([item['path'] for item in changes if item['path'].startswith('corpus/fixtures/')]))
print('AUDIT_END_UTC', datetime.datetime.now(datetime.timezone.utc).isoformat())
assert not errors
assert unchanged + len(changes) == len(entries)
assert len(current_fixtures) == 174
assert set(current_fixtures) - set(base_fixtures) == {'r100-docket-review'}
assert not set(base_fixtures) - set(current_fixtures)
print('CENSUS PASS 173 -> 174; all inherited fixture directories retained')
print('PRESERVATION', 'FAIL' if unexpected else 'PASS', 'unexpected inherited paths=' + json.dumps(unexpected))
PY
```

Observed exit 0: the audit executed completely; its preservation verdict is explicitly FAIL, not inferred from that execution exit code. Complete observed output follows:

```text
AUDIT_START_UTC 2026-10-18T02:40:36.148477+00:00
BASELINE fe1ce466e9d7427948c0abe4ecfbf961880b72ff
HEAD b5fe472957ab1e4e9c90f5613acc14cd24a288ae
BASELINE_ENTRIES 76539
UNCHANGED_INHERITED_ENTRIES 76533
CHANGED_INHERITED_ENTRIES 6
INHERITED_READ_ERRORS []
INHERITED_CHANGE {"allowed": false, "baseline_mode": "100644", "baseline_oid": "07b8445b01b51142e693612681fa420c3b102de8", "current_mode": "100644", "current_oid": "4bca2540d19dff3e43112e5f1cf3a670ed5cd795", "path": "LOG.md"}
INHERITED_CHANGE {"allowed": false, "baseline_mode": "100644", "baseline_oid": "3dd12ed8134113125f9f0b7ece1770b050c486ab", "current_mode": "100644", "current_oid": "5dfc77113e7ca2a7d9031b6b923e38cd8037b466", "path": "SCORECARD.md"}
INHERITED_CHANGE {"allowed": true, "baseline_mode": "100644", "baseline_oid": "2cc9b170e71a6d1e13ceb558d51f890e19c4e9a0", "current_mode": "100644", "current_oid": "27b9b6ff201c0e191777087e58fac2fb14f9891d", "path": "SKILL.md"}
INHERITED_CHANGE {"allowed": true, "baseline_mode": "100644", "baseline_oid": "ab63cd30edfd754df4dcbde54589c046d8cb2376", "current_mode": "100644", "current_oid": "d794e0ef140ad72cd07140a640762621a6315ec6", "path": "corpus/knowledge/r99-gate-blind-spot-table.md"}
INHERITED_CHANGE {"allowed": true, "baseline_mode": "100644", "baseline_oid": "45119aa9d28bd8a81200d60e214fb45d4961b066", "current_mode": "100644", "current_oid": "309341ba810de097352e1016168110c738352782", "path": "corpus/tools/README.md"}
INHERITED_CHANGE {"allowed": true, "baseline_mode": "100644", "baseline_oid": "7da596be4dc31fc13cf4ceb8ebebbcf8baaf0de7", "current_mode": "100644", "current_oid": "936a2082e134b9d84d64b849417c3c6dbc26d600", "path": "corpus/tools/dependency-freeze-contract.json"}
UNEXPECTED_INHERITED_PATHS ["LOG.md", "SCORECARD.md"]
BASELINE_MODE_COUNTS {"100644": 76182, "100755": 339, "120000": 18}
BASELINE_FIXTURE_DIRECTORY_COUNT 173
DELIVERED_FIXTURE_DIRECTORY_COUNT 174
ADDED_FIXTURE_DIRECTORIES ["r100-docket-review"]
MISSING_FIXTURE_DIRECTORIES []
FIXTURE_SYMLINK_DIRECTORIES []
FIXTURE_DIRECTORY_ENUMERATION_BEGIN
001 ally-one-way
002 ally-reciprocal
003 consistent
004 contradictions
005 contradictions-ledger-malformed
006 item-chain-broken
007 item-chain-valid
008 r10-registry-witness
009 r100-docket-review
010 r11-character-place
011 r11-dangling-place
012 r11-place-character
013 r11-unique-nonplace
014 r12-ambiguous-actor
015 r12-unique-actor
016 r13-missing-actor
017 r13-unique-actor
018 r15-carbon-followup
019 r16-missing-first
020 r16-missing-place
021 r16-mixed-three
022 r16-valid-places
023 r17-valid-places
024 r17-wrong-after
025 r17-wrong-before
026 r17-wrong-first
027 r17-wrong-last
028 r17-wrong-middle
029 r18-duplicate-first-known
030 r18-duplicate-pair
031 r18-duplicate-reverse
032 r18-known-through-ambiguous
033 r18-mixed-kind
034 r18-unique-pair
035 r19-negative-first-valid
036 r19-negative-tick
037 r19-valid-around-negative
038 r19-valid-tick
039 r20-both-negative
040 r20-mixed-edges
041 r20-negative-dependent
042 r20-negative-prereq
043 r20-valid-equal
044 r20-valid-inversion
045 r20-valid-order
046 r21-ambiguous-actor
047 r21-clean
048 r21-clean-reverse
049 r21-invalid-tick
050 r21-malformed
051 r21-malformed-reverse
052 r21-same-place
053 r21-wrong-kind-place
054 r22-clean-inversion
055 r22-malformed-only
056 r22-mixed-first
057 r22-mixed-last
058 r22-multiple-invalid
059 r22-self-repeated
060 r22-unknown-mixed
061 r22-valid-order
062 r23-note-class
063 r25-to-ambiguous
064 r25-to-unique
065 r26-to-malformed
066 r27-both-ambiguous
067 r27-target-only
068 r28-courier-excerpt
069 r29-near-miss
070 r30-explicit-negation
071 r31-source-ambiguous
072 r31-source-unique
073 r32-source-malformed
074 r33-tarin-envelope
075 r34-tarin-hearsay
076 r35-bell7-conflict
077 r36-bell7-wrong-date
078 r37-ledger-ambiguous
079 r37-ledger-unique
080 r39-ledger-source-missing
081 r39-ledger-source-unique
082 r40-vela-listener
083 r41-vela-direct-bell
084 r43-jorin-vela-sighting
085 r5-invalid-citation
086 r5-invalid-json
087 r5-missing-file
088 r5-row-shape
089 r5-wrong-top-level
090 r59-duplicate-harbor-tower
091 r59-duplicate-tower-harbor
092 r59-nested-duplicate
093 r59-unique-control
094 r60-empty
095 r60-partial
096 r60-unavailable
097 r60-unavailable-independent
098 r61-allied-empty
099 r61-allied-unavailable
100 r61-direct-ambiguous
101 r61-direct-duplicate-member
102 r61-direct-empty
103 r61-direct-malformed
104 r61-direct-nonarray
105 r61-direct-partial
106 r61-direct-unavailable
107 r61-independent-empty
108 r61-independent-unavailable
109 r61-ledger-unavailable
110 r62-duplicate
111 r62-duplicate-member
112 r62-empty
113 r62-independent
114 r62-loaded
115 r62-malformed
116 r62-malformed-side
117 r62-missing
118 r62-nonarray
119 r62-partial
120 r67-claim-source-loaded-control
121 r67-claim-source-loaded-empty
122 r67-claim-source-unavailable-control
123 r67-claim-source-unavailable-empty
124 r67-claim-source-unavailable-whitespace
125 r7-ally-reverse-ambiguous
126 r7-item-ambiguous
127 r72-vela-slate-claim
128 r73-jorin-slate-claim
129 r8-deps-anomalous
130 r8-deps-distinct
131 r83-vela-joint-nonsighting
132 r87-chain-unique-broken
133 r87-chain-unique-valid
134 r87-masked-break-from-ambiguous
135 r87-masked-break-to-ambiguous
136 r87-myth-cluster
137 r87-probe-entry-shape
138 r87-probe-multi-invalid
139 r87-probe-nonitem-kinds
140 r87-probe-record-and-chain
141 r87-probe-rowshape-rejected
142 r87-probe-shape-ambiguous
143 r87-probe-source-prefix
144 r88-m3-maya-cluster
145 r88-mixed-stop
146 r88-nonholder-stop
147 r88-shape-ambiguous-armed
148 r89-c1-invalid-from-holder
149 r89-c1-invalid-tick
150 r89-c1-invalid-to-holder
151 r89-c1-malformed-source-id
152 r89-c1-multi-cause-valid
153 r89-f2-dangling-from
154 r89-f2-dangling-to
155 r89-f2-invalid-source-id
156 r89-fn2-control
157 r89-fn2-unresolved-chain-break
158 r89-inspiration-paraphrase
159 r9-dup-high-low
160 r9-dup-low-high
161 r9-unique-control
162 r90-c1-rawpresent-from
163 r90-c1-rawpresent-source
164 r90-c1-rawpresent-to
165 r90-c1-three-causes
166 r91-c1-null-chain
167 r91-c1-tick-unresolved
168 r93-m2-kojiki-cluster
169 r94-paired-crossing
170 r95-crossing-aftermath
171 r96-crossing-response
172 r97-crossing-acknowledgment
173 r98-clerk-filing
174 r99-window-lapse
FIXTURE_DIRECTORY_ENUMERATION_END
NON_WAVE_UNTRACKED_PATHS [
  ".ufo/waves/round-100/scratch/V08-c2-anchors/independent_anchors.py",
  ".ufo/waves/round-100/scratch/V19-freshness/audit-output.txt",
  ".ufo/waves/round-100/scratch/V19-freshness/audit.py",
  ".ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md",
  "corpus/fixtures/r100-docket-review/README.md",
  "corpus/fixtures/r100-docket-review/claim-excerpt-map.md",
  "corpus/fixtures/r100-docket-review/contradictions.json",
  "corpus/fixtures/r100-docket-review/entities.json",
  "corpus/fixtures/r100-docket-review/fictional-excerpts.md",
  "corpus/fixtures/r100-docket-review/inspiration-note.md",
  "corpus/fixtures/r100-docket-review/relations.json",
  "corpus/fixtures/r100-docket-review/source-excerpt.md",
  "corpus/fixtures/r100-docket-review/sources.json",
  "corpus/fixtures/r100-docket-review/timeline.json",
  "corpus/knowledge/r100-crossing-arc-synthesis.md",
  "corpus/knowledge/r100-provenance-semantics-boundary.md"
]
UNEXPECTED_NON_WAVE_UNTRACKED_PATHS [".ufo/waves/round-100/scratch/V08-c2-anchors/independent_anchors.py", ".ufo/waves/round-100/scratch/V19-freshness/audit-output.txt", ".ufo/waves/round-100/scratch/V19-freshness/audit.py", ".ufo/waves/round-98/seats/V58-scratch/original-run-resume-note.md"]
NEW_FIXTURE_FILE_COUNT 10
NEW_KNOWLEDGE_PATHS ["corpus/knowledge/r100-crossing-arc-synthesis.md", "corpus/knowledge/r100-provenance-semantics-boundary.md"]
INHERITED_FIXTURE_CHANGES []
AUDIT_END_UTC 2026-10-18T02:40:36.828515+00:00
CENSUS PASS 173 -> 174; all inherited fixture directories retained
PRESERVATION FAIL unexpected inherited paths=["LOG.md", "SCORECARD.md"]
```

The `NON_WAVE` labels above mechanically exclude only `.ufo/waves/round-100/seats/`, not every permitted per-seat scratch location. The V08 script is explicitly declared at `V08-c2-anchors.md:13-17`; the V19 paths are under a seat-named scratch directory (no V19 report was present when checked). These three paths are not inherited-file mutations, and I do not turn their mechanical classification into a byte-preservation failure. The old untracked r98 `original-run-resume-note.md` was already present in the initial `git status --short --untracked-files=normal` observation before any V15 write; it is an ancillary pre-existing artifact, not a changed inherited path or a V15 creation. None was removed or altered by this seat.

## Independent Git diff and strict failure receipt

The following exact command independently separated baseline-relative, committed pre-dispatch, and uncommitted producer deltas. The final two checks produced no output; the command exited 0:

```sh
git diff --no-ext-diff --no-textconv --no-renames --name-status fe1ce46 -- && git diff --no-ext-diff --no-textconv --no-renames --name-status fe1ce46 HEAD -- && git diff --no-ext-diff --no-textconv --no-renames --name-status HEAD -- && git diff --no-ext-diff --no-textconv --exit-code fe1ce46 -- corpus/fixtures PROVINCE.md corpus/tools/dependency_freeze.py && git diff --check
```

Complete stdout; the first six lines are baseline-relative, the next two pre-dispatch, and the final four producer-relative:

```text
M	LOG.md
M	SCORECARD.md
M	SKILL.md
M	corpus/knowledge/r99-gate-blind-spot-table.md
M	corpus/tools/README.md
M	corpus/tools/dependency-freeze-contract.json
M	LOG.md
M	SCORECARD.md
M	SKILL.md
M	corpus/knowledge/r99-gate-blind-spot-table.md
M	corpus/tools/README.md
M	corpus/tools/dependency-freeze-contract.json
```

A separate strict predicate deliberately returned exit 1 for the observed out-of-allowlist inherited paths. Exact command:

```sh
python3 - <<'PY'
from pathlib import Path
import json, subprocess
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root
allowed = {'SKILL.md', 'corpus/knowledge/r99-gate-blind-spot-table.md', 'corpus/tools/README.md', 'corpus/tools/dependency-freeze-contract.json'}
actual = set(subprocess.check_output(['git', 'diff', '--no-ext-diff', '--no-textconv', '--name-only', 'fe1ce46', '--'], text=True).splitlines())
producer = set(subprocess.check_output(['git', 'diff', '--no-ext-diff', '--no-textconv', '--name-only', 'HEAD', '--'], text=True).splitlines())
pre_dispatch = set(subprocess.check_output(['git', 'diff', '--no-ext-diff', '--no-textconv', '--name-only', 'fe1ce46', 'HEAD', '--'], text=True).splitlines())
print('STRICT_ALLOWED_INHERITED_PATHS', json.dumps(sorted(allowed)))
print('BASELINE_RELATIVE_INHERITED_PATHS', json.dumps(sorted(actual)))
print('PRE_DISPATCH_COMMITTED_DELTA', json.dumps(sorted(pre_dispatch)))
print('PRODUCER_WORKTREE_DELTA', json.dumps(sorted(producer)))
print('PRODUCER_WORKTREE_SCOPE', 'PASS' if producer == allowed else 'FAIL')
unexpected = sorted(actual - allowed)
print('STRICT_BASELINE_SCOPE', 'FAIL' if unexpected else 'PASS', json.dumps(unexpected))
raise SystemExit(1 if unexpected else 0)
PY
```

Complete stdout, exit 1:

```text
STRICT_ALLOWED_INHERITED_PATHS ["SKILL.md", "corpus/knowledge/r99-gate-blind-spot-table.md", "corpus/tools/README.md", "corpus/tools/dependency-freeze-contract.json"]
BASELINE_RELATIVE_INHERITED_PATHS ["LOG.md", "SCORECARD.md", "SKILL.md", "corpus/knowledge/r99-gate-blind-spot-table.md", "corpus/tools/README.md", "corpus/tools/dependency-freeze-contract.json"]
PRE_DISPATCH_COMMITTED_DELTA ["LOG.md", "SCORECARD.md"]
PRODUCER_WORKTREE_DELTA ["SKILL.md", "corpus/knowledge/r99-gate-blind-spot-table.md", "corpus/tools/README.md", "corpus/tools/dependency-freeze-contract.json"]
PRODUCER_WORKTREE_SCOPE PASS
STRICT_BASELINE_SCOPE FAIL ["LOG.md", "SCORECARD.md"]
```

Exact attribution command:

```sh
git log --format='%h %s' --name-only fe1ce46..HEAD -- LOG.md SCORECARD.md
```

Complete stdout, exit 0:

```text
b5fe472 lore r100: declare sol-max 32-seat round before dispatch

LOG.md
ae67105 lore r99: close round — SCORECARD admitted section

SCORECARD.md
```

Earlier `git diff --no-ext-diff --no-textconv fe1ce46 -- LOG.md SCORECARD.md` showed append-only hunks `@@ -3345,3 +3345,60 @@` and `@@ -560,3 +560,36 @@`; direct Reads locate their headings at LOG:3349 and SCORECARD:564. No attribution to producers is warranted.

## Ownership, initial absences, and limits

Only `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V15-preservation-census.md` was written by V15. No V15 scratch was created. No nested agents, commits, pushes, network, live fixture changes, contract writes, or other edits.

Immediately before the report Write, this exact lane-root command exited 0:

```sh
python3 - <<'PY'
from pathlib import Path
root = Path('/home/vgpnk/Projects/shokunin/lore-shokunin')
assert Path.cwd().resolve() == root
report = Path('/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V15-preservation-census.md')
assert report.resolve() == root / '.ufo/waves/round-100/seats/V15-preservation-census.md'
assert report.parent.resolve() == root / '.ufo/waves/round-100/seats'
assert report.parent.is_dir()
assert not report.is_symlink()
assert not report.exists()
print('REPORT_PATH_VERIFIED', report.resolve())
print('REPORT_PARENT_VERIFIED', report.parent.resolve())
print('REPORT_ABSENT_BEFORE_WRITE', not report.exists())
PY
```

Complete stdout:

```text
REPORT_PATH_VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats/V15-preservation-census.md
REPORT_PARENT_VERIFIED /home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-100/seats
REPORT_ABSENT_BEFORE_WRITE True
```

Initial direct Read of lane `AGENTS.md` returned absent; a recursive AGENTS glob found none. Initial `pwd && git rev-parse --show-toplevel && git rev-parse fe1ce46 && ls .ufo/waves/round-100/seats` confirmed the correct lane and baseline, then exited 2 because the seats directory did not exist yet. The bounded producer wait resolved that initial absence. A later direct Read of `V19-freshness.md` and V19 report glob also found no report; this is not a missing producer or an all-reports requirement for V15.

No production test suite or semantic gate was required or claimed by this preservation/census seat. The exhaustive audit, independent Git checks, and intentional failing strict allowlist predicate are the verification receipts. The unresolved item is the required-baseline/allowlist mismatch, not fixture loss or an unverified census.

FAIL — census 174 and inherited fixture preservation pass, but strict comparison with fe1ce46 finds two additional inherited changes, LOG.md and SCORECARD.md, already committed before dispatch; producer-only worktree scope passes.
