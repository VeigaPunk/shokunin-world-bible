# V52 — inherited-tools (round 96) — DRAFT (pre-final)

Seat: leaf verifier. Claim under test: git diff dcb2d92 shows
check_bible / support_check / boundary / discriminate / contract byte-untouched;
r88–r95 fixtures untouched. Baseline dcb2d92; HEAD 60dba0c.

Stable evidence so far:
- snapshot-1 manifest (manifest-1.txt sha256 e802243f8e553141a7b681f2b049938afd0ba60d8e7dcc4113bd5ebd0f905c1f): 174 lines, 0 diffs.
- 164 tracked r88–r95 fixture files; file sets identical baseline vs worktree.
- behavioral: check_bible r95 CLEAN exit 0; support_check r95 15/2/17 PASS exit 0;
  boundary CERTIFIED exit 0 + self-test 8 PASS exit 0; discriminate HELD exit 0.
- contract wrinkle: map-obligations-contract.json Q2-owned, expected 22→24 per C1(b).
