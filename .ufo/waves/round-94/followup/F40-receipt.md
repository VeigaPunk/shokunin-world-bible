# F40 — receipt-bookkeeping (round-94 FOLLOW-UP wave mechanics audit)

**Seat role:** FOLLOW-UP leaf, receipt bookkeeping. Scope: count `F*.md` seat reports under
`.ufo/waves/round-94/followup/`, flag missing seats against the declared 40-seat roster, verify no
two seats wrote the same report file, and write the receipt skeleton `.ufo/waves/round-94/followup-receipt.json`
with per-seat `seat` / `report_path` / `outcome` and `agent_id: null` for the integrator to fill after
collection. Writes: this report and the receipt JSON only. No corpus edits, no commits, no nested agents.
Presence/mechanics only — this seat does not judge report content, C1/C2 claims, or any axis.

## Declared roster and receipt contract (evidence)

- `LOG.md:2683-2691` (declaration commit `65a93298cb100fdbf5732ac6de55f01a683c02d8`): "one batched
  AgentSwarm FOLLOW-UP of 40 seats on `opencode-go/deepseek-v4.1-flash`, each seat leaf with an
  exclusive report at `.ufo/waves/round-94/followup/F<NN>-<role>.md`."
  Observed via `grep -n "40 seats\|F<NN>" LOG.md` → `2687: one batched AgentSwarm FOLLOW-UP of 40 seats on`,
  `2689: .ufo/waves/round-94/followup/F<NN>-<role>.md`.
- **Committed-spec discrepancy (flag for integrator):** `python3 -c "import json;d=json.load(open('.ufo/waves/round-94/wave-spec.json'));print(json.dumps(d['followup']))"`
  → `{"requested_model": "opencode-go/deepseek-v4.1-flash", "requested_seats": 32, "status": "not-dispatched", "result": null}`.
  The committed spec still carries the pre-declaration 32-seat / not-dispatched value; the 40-seat
  declaration commit changed only `LOG.md` (`git show --stat 65a9329` → `LOG.md | 20 ++++++++++++++++++++`).
  My count is against the declared 40, per the seat instruction.
- Candidate under review: `abbc3e0186c89016d5cbe68b37a2c027bf11d548`; baseline
  `9c2eea3b58a090f8820c7a723d2f6a22b46ae52b` (`git rev-parse abbc3e0 9c2eea3 HEAD`); candidate is an
  ancestor of HEAD `65a9329` — `git merge-base --is-ancestor abbc3e0 HEAD` → `ANCESTOR_OK`.

## Collection window (observed counts)

Snapshots of `ls .ufo/waves/round-94/followup/F*.md | wc -l` during the live dispatch; the full curve
comes from a bounded background poller (45 s interval, 600 s cap, one call):

```
POLL 15:41:15 reports=4      POLL 15:46:30 reports=35
POLL 15:42:00 reports=6      POLL 15:47:15 reports=36
POLL 15:42:45 reports=12     POLL 15:48:00 reports=36
POLL 15:43:30 reports=27     POLL 15:48:45 reports=37
POLL 15:44:15 reports=30     POLL 15:49:30 reports=38
POLL 15:45:00 reports=31     POLL 15:50:15 reports=39
POLL 15:45:45 reports=34     POLL 15:51:00 reports=39
POLL_DONE 15:51:45 reports=40
```

All seats were still being written during the window; scratch directories observed at 15:46:24:
`F11-scratch F13-scratch F15-scratch F23-scratch F31-scratch` (`ls -d .ufo/waves/round-94/followup/F*-scratch`).

## Findings at final snapshot (2026-10-17 ~15:52 local)

1. **Count vs expected 40: 40/40 present.** Every seat F01–F40 has exactly one `F<NN>-<role>.md`
   report; missing list is empty. Final audit output: `FINAL_COUNT = 40`, `missing = []`.
2. **No two seats wrote the same file.** `duplicate_prefixes = {}` and `header_mismatches = []`:
   for all 40 reports, the seat ID in the first five lines equals the filename prefix
   (`header_seat` = prefix, `match=True` on every line). This is a prefix/header-consistency check —
   authorship of bytes cannot be proven from content alone, but no seat-ID collision or cross-seat
   header is present.
3. **Receipt skeleton written** at `.ufo/waves/round-94/followup-receipt.json`: 40 seat entries
   F01–F40 with `seat`, `report_path`, `report_sha256`, `outcome: "pending-collection"` and
   `agent_id: null` on every entry — the integrator fills agent IDs and outcomes from the AgentSwarm
   dispatch result after collection. No agent ID or served-backend echo is invented here.
4. **Auxiliary seat artifacts (not reports):** `F29-debt.json` (top-level, F29 debt-ledger evidence)
   plus the five scratch directories named above. Report counting used `F*.md` only, per the seat
   definition; these artifacts are recorded here so the integrator can account for them.

### Header/collision audit — command and observed output

```sh
python3 - <<'EOF'
import glob, hashlib, os, re
base = ".ufo/waves/round-94/followup"
files = sorted(glob.glob(base + "/F*.md"))
print("count =", len(files))
seen = {}; mismatch = []
for f in files:
    name = os.path.basename(f)
    prefix = name[:3] if re.match(r"F\d\d-", name) else "??"
    text = open(f, encoding="utf-8", errors="replace").read(1200)
    head5 = "\n".join(text.splitlines()[:5])
    hm = re.search(r"\bF\d{2}\b", head5)
    hseat = hm.group(0) if hm else None
    sha = hashlib.sha256(open(f, "rb").read()).hexdigest()
    seen.setdefault(prefix, []).append(name)
    ok = (prefix == hseat)
    if not ok: mismatch.append((name, head5[:80].replace("\n"," | ")))
    print(f"{prefix} sha256={sha[:16]}... header_seat={hseat} match={ok}")
print("duplicate_prefixes =", {k: v for k, v in seen.items() if len(v) > 1})
print("header_mismatches =", mismatch)
present = set(seen)
missing = [f"F{i:02d}" for i in range(1, 41) if f"F{i:02d}" not in present]
print("missing =", missing)
EOF
```

Final run (2026-10-17 ~15:52) observed: `FINAL_COUNT = 40`; all 40 lines `match=True`;
`duplicate_prefixes = {}`; `header_mismatches = []`; `missing = []`;
`top_level_non_md_F_files = ['F29-debt.json']`. An earlier run at 15:45:30 (35 present) observed
`missing = ['F20', 'F21', 'F27', 'F29', 'F40']` — those five seats landed later in the window
(F40 is this report, written at ~15:48).

## Limits

- Report **presence is not completion or verification**; this seat did not open or judge report
  content beyond the first-lines seat self-identification needed for the collision check.
- **Absent at snapshot ≠ failed.** At my earlier 15:45:30 snapshot five seats were absent and all
  landed later; the dispatch result itself had not returned at snapshot time, so `outcome` in the
  receipt stays `pending-collection` and the integrator resolves final outcomes from the dispatch result.
- The receipt skeleton's `agent_id`/`outcome` fields are intentionally `null`/`pending-collection`;
  filling them from the returned AgentSwarm record is the integrator's step, not this seat's.
- The stale `wave-spec.json` `requested_seats: 32` field is reported as observed; whether to update it
  is outside this seat's write scope.

Bottom line: PASS — 40/40 declared seats have exclusive reports, zero duplicate seat prefixes and zero
header/seat mismatches; receipt skeleton written with `agent_id: null` for integrator fill, and the
stale 32-seat `wave-spec.json` field is flagged.
