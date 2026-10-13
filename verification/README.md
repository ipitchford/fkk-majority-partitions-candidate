# Exact verification

Python 3 is required. `review_checks.py` additionally requires SymPy. Enumeration
requires nauty `geng` on PATH, or an explicit `--geng /path/to/geng` argument.
The archived candidate audit uses included `data/n10_small.g6` and
`data/recorded_minimizers.g6`; provenance hashes record their derivation. It
validates the supplied 72,677 candidates, not their selection completeness.

Run from this directory:

```sh
python3 self_test.py
python3 -O self_test.py
python3 review_checks.py
python3 -O review_checks.py
python3 exact_small_graphs.py --max-n 9
python3 -O exact_small_graphs.py --max-n 9
python3 audit_recorded_candidates.py
python3 -O audit_recorded_candidates.py
```

Each command prints a JSON receipt only on success. Validation raises exceptions
under both ordinary and optimised Python. `self_test.py` intentionally submits
invalid cases and verifies rejection; a passing receipt means those negative
controls were rejected. Original submitted verifier scripts are preserved
byte-for-byte in `originals/`. Use the hardened scripts in this directory for
release verification; the historical originals rely on assertions.

`independent-checks-*.json` records a different exact PSD criterion on 600
deterministic matrices and two symbolic identities. It compares PSD decisions,
not the rank returned by the fraction-free routine. Enumeration relies on nauty
for coverage and isomorphism classes. No order-10/11 exhaustive replay is claimed.
