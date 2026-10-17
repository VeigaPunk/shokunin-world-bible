# shokunin-world-bible

Fictional-world records, with a checker that reports contradictions and
does not resolve them.

Entities, relations, timeline events. A claim needs an in-world citation.
A contradiction stays visible. Silently picking a winner is the failure
this lane exists to refuse. Real-world reference works are cited with
attribution, rights, and AI-training permission kept as three questions.

Rank: **shonen**. `SHONEN.md` is still here. Registered in the fleet
`MANIFEST.json` as lore-shokunin since 2026-10-11. There is no `SKILL.md`
in this checkout.

## Province

**Owns.** Fictional-world records — characters, places, factions, items —
their relations and timeline events, consistency verification, and sourced
inspiration. In-world documents live under `corpus/` once a round produces
them. The fixtures are fictional on purpose.

**Hands off.** Canon claimed without an in-world citation. Silent
resolution of contradictions. Real-world rights rulings. Game-mechanics
verification (game-dev-2d). Kotodama
([kotodama-shokunin](https://github.com/VeigaPunk/kotodama-shokunin))
generates linguistic-cultural systems and hands them off. This lane
records and verifies. A handoff packet is not canon until this lane says
so, and a sample packet in the other repository does not say so.

Writes stay in this repository, its own fleet round report, and allowed
append-only L0 questions (`l0-questions.md`).

## Start here

1. `PROVINCE.md` — the boundary.
2. `corpus/fixtures/README.md` — how the checker is supposed to behave,
   round by round, including the predecessor path
   `.shokunin/lore/corpus/fixtures/...`.
3. `corpus/fixtures/check_bible.py` — the checker. The module docstring:
   validate a small cited fictional-world bible; report, never resolve,
   contradictions.
4. `corpus/knowledge/` — `seed.md` is a mint proposal, not a validated
   schema. The decision tables name their limits.
5. `SCORECARD.md` — scores stay unmeasured. The fleet-round-1 section
   says the driver restarted the per-lane counter, and that earlier
   r1–r85 records remain historical evidence. An unmeasured axis is an
   unresolved tie, not a zero.

## Run the checker

In this checkout the checker and the two earliest fixtures are:

```sh
python3 corpus/fixtures/check_bible.py corpus/fixtures/consistent
python3 corpus/fixtures/check_bible.py corpus/fixtures/contradictions
```

`corpus/fixtures/README.md` records the predecessor invocation and the
expected pair: the consistent tree exits 0; the contradictions tree
exits 1 and prints all three seeded violations. Later rounds add narrower
fixtures (`ally-reciprocal`, `ally-one-way`, item chains, timeline order,
and others indexed in `corpus/README.md`). Round-4 duplicate-name inputs
were rejected and live only under `corpus/live/rejected-r4/`. A structural
exit 0 is not authenticated testimony, a shared occasion, or canon. The
scorecard repeats that bound on the later rounds.

## The tree

| Path | What it is |
|---|---|
| `corpus/fixtures/` | The checker and the fictional bibles, one directory per case |
| `corpus/knowledge/` | Decision tables, the reference ledger, malformed-input notes |
| `corpus/live/` | Preserved stdout, stderr, and rejected experiments |
| `reports/` | Reviewer and adjudicator reports |
| `l0-questions.md` | Append-only questions for the integrator |

## Fleet

Minted under [shokunin](https://github.com/VeigaPunk/shokunin).
