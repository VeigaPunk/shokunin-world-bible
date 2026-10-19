<!-- verbatim final output of L2 seat W2RoundLore.R103Connector (read-only role), persisted by L1 lore round 103, 2026-10-19 -->
# UFO-FSD Connector: Sibling-Overlap Scan & Synthesis (Round 103)

### 1. Sibling Knowledge Overlap & Contested Scope
- **Aliases / Name Variants:** Held by `kotodama-shokunin` (`naming-systems.md:1-53,136`, `naming-canon-workflow.md:1-23,44-53`, `naming-collision-gate.md`). Kotodama owns linguistic derivation, slot grammar, and taboo rules; lore owns entity identity and canon naming. **Verdict: CM-a is NOT contested.**
- **In-World Dating / Time:** Held by `kotodama-shokunin` (`calendar-festival-systems.md:1-53,175`, `era-periodization-models.md:1-53,143`, `era-language-staging.md`). Kotodama models calendar mechanics and era cycles; lore owns chronology, timeline ticks, and event dates. **Verdict: CM-c is NOT contested.**
- **Canon Status / Retcons / Supersession:** Held by NO sibling. All siblings explicitly refuse canon (`kotodama/PROVINCE.md:16-17`, `audio/PROVINCE.md:15`, `game-dev-2d/PROVINCE.md:10`, `game-dev-3d/PROVINCE.md:35`, `revenger/PROVINCE.md:23`). **Verdict: CM-e is NOT contested (exclusively lore).**
- **Reveal Order:** Held by NO sibling (0 matches; `lore-state.md:161` notes CM-f uncovered).
- **Source Reliability:** `chousa-shokunin/SKILL.md:8-11,18-20` owns real-world research method (primary>secondary>aggregator>unsourced). In-world chronicler reliability is uncovered lore scope.

### 2. Chousa Research-Method Boundary
- **Contract Rule 3:** Claim admission stays in `corpus/QUALITY.md`; research method stays chousa's (`chousa-shokunin/SKILL.md`). `SOURCES.md` duplicates neither.
- **Duplication Risk:** Lore must not define general citation-chain, claim-span, or real-world source-ranking engines. Lore evaluates in-world bible consistency and excerpt support.
- **Boundary Quote (`chousa-shokunin/SKILL.md:8-11`):**
  > "Domain: the reusable METHOD of source research — how a question is framed, which sources outrank which, how a citation chain is followed, and how a claim is verified against its source. Not the bounty programs (kasegi) and not model quality (kengaku)."

### 3. Kotodama Contract Digest & Acknowledgement
- **Command:** `sha256sum kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`
- **Current Digest:** `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (commit `e1694ba`).
- **Lore Recorded Digests (`l0-questions.md:5-7`):** `e834f50309bd93b11894e7f96d03f7000fc224a3a3ea4d654fd4d1aaaa0831f7` (r89) and `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1` (r93). Both are STALE; digest drifted a 3rd time unacknowledged.
- **Acknowledgement Record Requirement Quote (`worldbible-integration-contract.md:14`):**
  > "Before the first transfer, both lanes read the whole file and record `lane, contract_id, revision, file_sha256, reader, read_at, evidence_pointer` in their own permitted records."

### 4. Sibling SOURCES.md & Cross-Referencable URLs
- **Sibling SOURCES.md:** None active in sibling roots (`*-shokunin/corpus/SOURCES.md` = 0).
- **Cross-Referencable URLs:**
  - W3C PROV-DM: `https://www.w3.org/TR/prov-dm/` (`kotodama/.../worldbible-integration-contract.md:31`)
  - W3C SKOS: `https://www.w3.org/TR/skos-reference/` (`kotodama/.../worldbible-integration-contract.md:32`)
  - SemVer 2.0.0: `https://semver.org/spec/v2.0.0.html` (`kotodama/.../worldbible-integration-contract.md:33`)
  - Star & Griesemer (1989): `https://doi.org/10.1177/030631289019003001` (`kotodama/.../contract.md:30`)
  - W3C PROV-O: `https://www.w3.org/TR/prov-o/` (`lore/corpus/knowledge/reference-ledger.md:5`)

### 5. Reusable Cross-Lane Patterns & Connector Move
- **QUALITY.md Pattern:** `game-dev-2d-shokunin/corpus/QUALITY.md:7-24` and `kaidoku-shokunin/corpus/QUALITY.md:9-25`: couple each `Q##` criterion to its mined lesson/mistake, define a `## Signals of weak material` table, and append an executable command block (`## Check`).
- **Proposed Move:** In lore's round-103 C1/C3 execution, cross-reference kotodama's shared reference URLs (PROV-DM, SKOS) in `corpus/SOURCES.md`, and record an explicit bilateral contract acknowledgement line in lore's corpus matching `worldbible-integration-contract.md:14` against current hash `5f4c02b...`.
- **Axes Affected:** Improves **Coverage** (resolves CM-g intake gap) and **Depth** (contract activation) without harming **Calibration**.
- **Risks & Verification:** Risk of absorbing kotodama generative rules is prevented by adhering to contract §3 ownership table. Verification: run census commands on `corpus/SOURCES.md` and check acknowledgement tuple formatting.