# V19 — c3-r96-repair-scope (round 97)

Seat: V19 c3-r96-repair-scope. Scope: after R4's cosmetic repair, diff r96's map pre/post
(`git diff f3e09f9 -- corpus/fixtures/r96-crossing-response/claim-excerpt-map.md`) must show
exactly the two declared cosmetic changes and nothing else; r96 `support_check` receipt identical;
r96 `map_obligations` receipt identical.

Baseline: r96 closure commit f3e09f9 (HEAD of lane at start = 2393934, working tree clean for the fixture).
Pre-repair map sha256 = 5093d72e... (working tree byte-identical to f3e09f9 at capture time).
Post-repair map sha256 = e851f068...
