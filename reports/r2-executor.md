# Round 2 executor report — faction `allied_with` symmetry

Implemented the narrow checker rule in `corpus/fixtures/check_bible.py`. For each `allied_with` relation between two distinct, resolvable faction IDs, it requires a reversed `allied_with` row whose `source_id` resolves in `sources.json`. Missing witnesses are reported at the original relation's `relations[index]` location. An unknown-source reverse row does not qualify and independently retains the existing unknown-source diagnostic. The checker does not change fixture/canon data or infer relations from prose.

Self-edges are explicitly outside the two-distinct-faction symmetry scope and are skipped. Missing/ambiguous entity IDs (duplicate IDs), dangling endpoints, and endpoints that are not factions are likewise skipped by this rule; their existing checker behavior is preserved. No other relation type is inspected. This is the declared fixture convention, not a general relation ontology.

## Evidence

Baseline fixtures:

- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/consistent` — exit 0; clean.
- `python3 .shokunin/lore/corpus/fixtures/check_bible.py .shokunin/lore/corpus/fixtures/contradictions` — exit 1; same three prior violations (dangling endpoint, timeline inversion, double booking).

Focused temporary probes (generated outside the repository from baseline fixture data; no canon files changed):

- One-way sourced faction edge — exit 1; reports `relations[0]` as lacking a sourced reciprocal.
- Reciprocal sourced faction edges — exit 0.
- Reverse edge with unknown source — exit 1; reports the reverse row's unknown source and the original row's missing sourced reciprocal.
- Self-edge — exit 0 (outside scope).
- Nonfaction endpoint — exit 0 for symmetry (outside scope).
- Unknown endpoint — exit 1 with the existing dangling endpoint only; no symmetry cascade.

No commit made. The reciprocal-source probe specifically addresses the critic's unknown-source reverse-witness concern.
