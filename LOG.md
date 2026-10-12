# lore append-only log

## Mint 2026-10-12
- Explicit operator directive; no craft round, no verdict or promotion yet.
- Evidence: .shokunin/mints/lore.md; seed knowledge: corpus/knowledge/seed.md.
- Lane git identity for all round commits: lore-shokunin <lore@shokunin.local>.
- Next falsifiable move: declare one axis-move claim, cite before/after, named non-author review, L1 closure.

## Round 1 — 2026-10-12 (depth axis-move)
- Claim declared before work: “A sourced example bible and a seeded contradiction corpus can be checked by one executable schema-and-consistency checker: the clean bible exits 0, while the contradiction corpus exits 1 and reports every seeded violation.” Baseline at mint `de12cb9c1c20d0a3d6c8aebccd282f5dd847cd7a`: no fixtures or runnable checker (`git ls-tree -r --name-only de12cb9 -- .shokunin/lore/corpus/fixtures` → empty).
- Built `corpus/fixtures/check_bible.py`, four JSON tables per fixture, instructions, cited decision table and method ledger; fictional records cite `sources.json`. The three seeded conflicts are preserved in `fixtures/contradictions/`, not resolved.
- Run evidence: `corpus/live/runs/20261012T155644Z/consistent.txt` exit 0 / zero violations; `contradictions.txt` exit 1 / three violation lines (dangling endpoint, inverted dependency, double booking). Independent non-author `lore-r1-independent-verifier` reran both commands with matching results and reported no blocker; no SHONEN box self-checked.
- Per-axis verdict: **depth improved** (runnable schema, decision table and three conflict classes where baseline had only a checklist); **coverage improved** (four sourced record types plus three executed conflict classes versus no fixture; aliases/free text still not covered); **calibration unchanged** (limits documented and verifier confirmed, but no prior calibrated prediction baseline to prove movement). Admit: at least one improved, none harmed.
- Next falsifiable move: add explicit contradiction records with `claim_a`, `claim_b`, `why` and source citations, then test preservation without automatic resolution. No promotion claim.
