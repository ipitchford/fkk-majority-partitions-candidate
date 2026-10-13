# Weighted partition certificates

This supplement verifies the fixed-partition weighted criterion without floating-point eigenvalues. Python 3.9 or later and its standard library suffice for certificate replay. The optional discovery script additionally requires nauty's `geng` executable.

## Certificate replay

Run from this directory:

```sh
python3 verify_certificates.py > new-replay.json
python3 -O verify_certificates.py > new-replay-optimized.json
python3 check_family.py > new-family-normal.json
python3 -O check_family.py > new-family-optimized.json
```

The supplied receipts record successful executions in both interpreter modes. Each certificate checker uses explicit exceptions, so Python optimization does not disable verification. The 441-graph certificate file has SHA-256 `7eb484bf5dbc95c395cef7172f1f6d278f3e18a50b73fdf2e9702c034db0cfc0`.

`weighted-certificates.json` supplies graph6 encodings, partitions, and positive rational weights. `verify_certificates.py` reconstructs each integer matrix C and checks Cz>=0 exactly. It then tests every nonempty partition, modulo exchanging parts. All 441 graphs have no strict-majority partition; 338 also have no such partition in their complements. All saved witnesses have strictly positive residual. Negative controls corrupt a valid witness to all ones and to a negative coordinate; both must be rejected. A positive control tests the majority detector on K_2.

`check_family.py` checks formal polynomial identities for the family obtained from K_{k,k} by deleting k-2 edges at one vertex. For every integer 4<=k<=100 it constructs the graph and verifies the integer witness (4k-7 at the exceptional vertex, 5 at its missing neighbors, 1 elsewhere), its residual, the minimum residual-to-degree ratio, and the stated spectral lower bound greater than 1/8. It exhaustively excludes majority partitions in both graph and complement for k=4,5,6. The general theorem is justified by the accompanying mathematical proof, not inferred from these finite tests.

## Discovery replay and trusted enumeration

```sh
python3 search_weighted.py 8 /path/to/geng > new-search-portable.jsonl
```

The generator emits all connected unlabeled graphs; the discovery script examines every partition of each graph lacking an ordinary majority partition. It uses exact integer PSD elimination, then rational Gaussian elimination for successful nonsingular matrices. The final certificate checker is a separate direct positive-vector check and does not use that PSD routine. `search-portable.jsonl` records the successful matrices and witnesses plus counts.

| Order | Connected graphs from geng | Without majority | Weighted successes among those |
|---|---:|---:|---:|
|5|21|8|0|
|6|112|46|0|
|7|853|530|0|
|8|11117|6612|441|

These counts trust nauty's isomorph-free enumeration and connected-graph generation. The generator is not formally verified by this supplement, and the discovery log alone is not a completeness certificate independent of nauty. Saved certificate validity and exhaustive partition rejection on each saved graph can be replayed without nauty. No order beyond eight was searched for this comparison.

The discovery and portable replay agreed graph for graph, matrix for matrix and witness for witness; elapsed times can vary. General positive-vector/PSD equivalence is established matrix theory. The purpose of these data is to demonstrate additional graph-class coverage, not to claim a new matrix-theoretic equivalence or a resolution of the full Nordhaus–Gaddum conjecture.

## Effective-strictness check

```sh
python3 check_parity.py /path/to/geng > parity-normal.json
python3 -O check_parity.py /path/to/geng > parity-optimized.json
```

`check_parity.py` independently checks the rational uniform spectral surplus `1/[2(n-1)^2(n-2)]` on all connected graphs of orders four through seven admitting a nonsingleton strict-majority partition. It uses exact rational Schur elimination on the generalized spectral-threshold matrix and covers both-even, both-odd and mixed-parity partitions. This supplements the all-order proof; it does not establish that proof by extrapolation. The nauty trust limitation above applies. Singular-positive and indefinite-negative matrix controls are included. Both interpreter-mode receipts agree.
