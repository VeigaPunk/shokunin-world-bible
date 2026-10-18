# DRAFT — Round-96 addendum for corpus/tools/README.md (Q2, fill actuals after Q1 lands)

### Round-96 addendum: gating inventory mismatch, `dual_pointer`, 24-case self-test (2026-10-17)

This addendum extends the r95 instructions above; every earlier sentence remains as delivered history.

#### Gating inventory mismatch (closes the r95 deletion class)

Before (r95 revision, scratch copy of `corpus/fixtures/r94-paired-crossing` with entity 0's `claims` key deleted and its `entities.json#/0/claims/0` map row removed):

```
OBLIGATIONS raw=13 mapped=13
INVENTORY JSON-FACTS 13/14; EDITORIAL-ROWS 2/2; TOTAL-ROWS 15/16 MISMATCH
RESULT PASS
exit 0
```

After (r96 revision, same scratch copy): [FILL actual output + exit]

#### `dual_pointer` in legacy-dialect cells (closes r95 V37-D1)

Before (r95 revision, scratch copy of `corpus/fixtures/r88-m3-maya-cluster` with P1 cell = `entities[0].first_appearance` (Aru; also `entities[0].claims[0]`)):

```
OBLIGATIONS raw=10 mapped=10
INVENTORY JSON-FACTS 10/10; EDITORIAL-ROWS 2/2; TOTAL-ROWS 12/12
RESULT PASS
exit 0
```

After: [FILL]

#### Persisted self-test: 24 cases

[FILL]

#### Unchanged

[FILL]
