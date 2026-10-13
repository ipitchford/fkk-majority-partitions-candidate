# Retained replay evidence

The checks in this package passed under both ordinary and optimized Python. Exact commands and scope are in [verification/README.md](verification/README.md) and [verification/weighted/README.md](verification/weighted/README.md). JSON records identify the actual implementation and input hashes; the manifest binds all shipped records.

| Obligation | Evidence |
|---|---|
| Explicit validation and semantic controls | verification/self-test-normal.json; self-test-optimized.json |
| Different exact PSD criterion, 600 matrices; symbolic identities | verification/independent-checks-normal.json; independent-checks-optimized.json |
| All 288,248 graphs of orders 5–9 | verification/enumeration-normal.json; enumeration-optimized.json |
| All 72,677 supplied order-ten candidates and seven minimizers | verification/candidates-normal.json; candidates-optimized.json |
| Direct rational replay of 441 weighted witnesses and all-partition exclusions | verification/weighted/replay.json; replay-optimized.json |
| Family algebra and finite parameter tests | verification/weighted/family-normal.json; family-optimized.json |
| Independent finite checks of the parity surplus | verification/weighted/parity-normal.json; parity-optimized.json |

Normal/optimized agreement does not make two independent algorithms. The separate principal-minor oracle concerns PSD decisions, not returned rank. Family parameter checks and small-order surplus checks supplement the general written proofs. Discovery completeness trusts nauty, while replay of saved weighted witnesses does not require it.

The publication process additionally runs a hash-bound gate batch from a clean extraction of the frozen release archive. Its operational receipts are retained outside the archive to avoid circular self-hashing and do not alter the recorded scientific scope. CI supplies an additional execution environment; green CI is not a mathematical proof.
